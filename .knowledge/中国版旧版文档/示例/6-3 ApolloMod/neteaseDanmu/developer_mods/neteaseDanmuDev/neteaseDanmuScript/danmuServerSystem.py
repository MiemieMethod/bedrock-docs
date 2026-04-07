# -*- coding: utf-8 -*-

import re, time, pickle, random
import lobbyGame.netgameApi as netgameApi
import apolloCommon.commonNetgameApi as commonNetgameApi
import logout
import neteaseDanmuScript.danmuConst as danmuConst
import apolloCommon.mysqlPool as mysqlPool
import apolloCommon.redisPool as redisPool
import server.extraServerApi as serverApi

ServerSystem = serverApi.GetServerSystemCls()


class DanmuServerSystem(ServerSystem):
	"""
	该mod的服务端类
	与客户端通信
	处理弹幕发送与推动送到其他客户端
	使用redis作弹幕数据中转站
	"""

	def __init__(self, namespace, systemName):
		ServerSystem.__init__(self, namespace, systemName)
		self.mPlayerId2InteractCD = {}  # 玩家发送弹幕间隔时间记录
		self.mDanmuBan = False  # 当前不允许发送弹幕，默认不允许，该标志跟随redis中的key
		self.mDanmuWaitlist = []  # 当前服务器玩家发出的弹幕堆积列表，客户端请求发过来的弹幕经过验证后先进入该列表，该列表每隔1秒都会将自身堆积的弹幕存入redis，并清空
		if not self.InitMysqlPool():
			return
		if not self.InitRedisPool():
			return
		if not self.InitDanmuCfg():
			return

		self.ListenForEvent(serverApi.GetEngineNamespace(), serverApi.GetEngineSystemName(), 'LoadServerAddonScriptsAfter', self, self.ServeForever)  # 服务端mod加载完成后开始跑一些直到服务器结束都在运作的逻辑

		self.ListenForEvent(danmuConst.ModName, danmuConst.ClientSystemName, 'DanmuPublishEvent', self, self.OnDanmuPublish)  # 客户端请求发送一条弹幕
		self.ListenForEvent(danmuConst.ModName, danmuConst.ClientSystemName, 'HintIconUnlockTextEvent', self, self.OnHintIconUnlockText)  # 未解锁的头像弹出解锁提示信息

	def InitMysqlPool(self):
		try:
			mysqlPool.InitDB(20)
		except:
			logout.error("Exception in InitMysqlPool")
			return False
		return True

	def InitRedisPool(self):
		try:
			redisPool.InitDB(20)
		except:
			logout.error("Exception in InitRedisPool")
			return False
		return True

	def InitDanmuCfg(self):
		"""
		加载mod.json中的配置
		详见mod.json
		"""

		cfg = commonNetgameApi.GetModJsonConfig("neteaseDanmuScript")
		if not cfg:
			logout.error("nothing in InitDanmuCfg")
			return False
		self.mIcons = cfg['icons']
		self.mColors = cfg['colors']
		self.mInterval = cfg['interval']
		self.mIconMapping = {item['icon_id']: item for item in self.mIcons}
		self.mIconMapping[()] = {  # 这个代表弹幕不携带头像
			"icon": -1,
			"lock": 0
		}
		self.mRR = cfg['rr']
		self.mMR = cfg['mr']
		self.mP = cfg['p']
		self.mPartition = cfg['partition']
		return True

	def Destroy(self):
		self.UnListenForEvent(serverApi.GetEngineNamespace(), serverApi.GetEngineSystemName(), 'LoadServerAddonScriptsAfter', self, self.ServeForever)

		self.UnListenForEvent(serverApi.GetEngineNamespace(), serverApi.GetEngineSystemName(), 'AddServerPlayerEvent', self, self.OnAddServerPlayer)
		self.UnListenForEvent(danmuConst.ModName, danmuConst.ClientSystemName, 'DanmuPublishEvent', self, self.OnDanmuPublish)
		mysqlPool.Finish()
		redisPool.Finish()

	def Trim(self, conn):
		"""
		暂定为7秒钟可以更新弹幕
		由于redis命令的原子性
		使用了简易的分布式锁来控制多个包含该mod进程（例如部署在很多个game）执行该方法是单点的
		弹幕存储的结构在redis中为一个list
		每次操作将弹幕列表左侧起（压入是用了lpush）的最多100条数据取出（所以一定是较新的100条）
		然后删除弹幕列表和“弹幕实时列表”（实时列表用于poll方法去获取弹幕数据推送到客户端）
		并用刚取出的数据创建新的“弹幕实时列表”
		更新自增版本号
		"""

		lock = conn.set('netease:danmu:lock', 1, ex=7, nx=True)  # 过期时间决定更新频率，暂定锁7秒过期，且每4s才执行该方法
		if lock:
			# 只有成功设置锁的进程此处才为True，其他进程则为False
			l = conn.lrange('netease:danmu:list', 0, 100)  # 存的多可以让消费时长增加，暂定取最多100条
			conn.delete('netease:danmu:list', 'netease:danmu:latest')
			if l:  # 可能仍未有任何玩家发送过弹幕
				conn.lpush('netease:danmu:latest', *l)
			conn.incr('netease:danmu:ver')  # 版本自增，poll取到数据能否推送推全取决于ver

	def Push(self):
		"""
		将堆积的弹幕压入redis的弹幕列表中
		"""

		if self.mDanmuWaitlist:
			waitlist = self.mDanmuWaitlist
			self.mDanmuWaitlist = []
			redisPool.AsyncFuncWithKey(
				lambda conn, values: conn.lpush('netease:danmu:list', *values),
				"push_latest_danmu",
				None,
				waitlist
			)

	def Poll(self, conn, closure={}):
		"""
		暂定每2s去取“弹幕实时列表”
		但取的频率较更新弹幕的频率高（更新无需过快，毕竟客户端播放也需要时间）
		有可能取到的是已经下放过的版本
		所以使用一个闭包保存已推送过的弹幕的版本
		"""

		data = {'ban': conn.get('netease:danmu:ban')}  # 顺便查看一下当前弹幕是否被禁了，如果为真值则取出来返回到主线程也不会下放到客户端
		ver = conn.get('netease:danmu:ver')
		if closure.get('ver') != ver:
			closure['ver'] = ver
			data['l'] = conn.lrange('netease:danmu:latest', 0, -1)
		return data

	def PostPoll(self, data):
		"""
		取到弹幕数据之后需要验证并且反序列化
		"""

		if isinstance(data, dict):
			if data['ban']:
				# master设置了禁止弹幕
				self.mDanmuBan = True
			elif self.mDanmuBan:
				self.mDanmuBan = False
			l = data.get('l', ())
			latest = []
			for raw in l:
				rec = pickle.loads(raw)
				if rec['iconId'] in self.mIconMapping:
					latest.append({
						'icon': self.mIconMapping[rec['iconId']]['icon'],
						'content': rec['content'],
						'playerId': rec['playerId'],
						'mode': rec['mode'],
						'rand': rec['rand']
					})
			if latest:
				self.BroadcastToAllClient('DanmuPollEvent', {'latest': latest, 'protocol': self.mPartition})  # 直接推到该服所有的客户端

	def ServeForever(self, *args):
		"""
		注册循环timer，弹幕插件的server端核心逻辑都是由timer驱动的
		"""
		comp = self.CreateComponent(serverApi.GetLevelId(), "Minecraft", "game")
		comp.AddRepeatedTimer(2.0, lambda: redisPool.AsyncFuncWithKey(  # 每2秒钟从redis中获取一批最新的弹幕
			self.Poll,
			"poll_latest_danmu",
			lambda data: self.PostPoll(data)
		))
		comp.AddRepeatedTimer(1.0, self.Push)  # 每秒钟将堆积的弹幕压进redis
		comp.AddRepeatedTimer(4.0, lambda: redisPool.AsyncFuncWithKey(  # 每隔4秒尝试清理弹幕，只留下较为新的弹幕
			self.Trim,
			"trim_latest_danmu",
			None
		))

	def OnDanmuPublish(self, data):
		"""
		客户端请求发送一条弹幕
		"""
		playerId = data.get("playerId", "-1")
		uid = netgameApi.GetPlayerUid(playerId)
		if not uid:
			print 'can not get uid by playerId: %s' % playerId
			return

		now = time.time()

		if netgameApi.GetUidIsSilent(uid) != 2:
			alertSystem = serverApi.GetSystem("neteaseAlert", "neteaseAlertDev")
			if alertSystem:
				alertSystem.Alert(playerId, '§c当前处于禁言状态。', 2, 0.5, 0.5)
			else:
				comp = self.CreateComponent(playerId, 'Minecraft', 'command')
				comp.SetCommand('tellraw @s {"rawtext": [{"text": "%s"}]}' % '§c当前处于禁言状态', playerId)
			return

		if self.mDanmuBan:
			alertSystem = serverApi.GetSystem("neteaseAlert", "neteaseAlertDev")
			if alertSystem:
				alertSystem.Alert(playerId, '§c当前无法发送弹幕！', 2, 0.5, 0.5)
			else:
				comp = self.CreateComponent(playerId, 'Minecraft', 'command')
				comp.SetCommand('tellraw @s {"rawtext": [{"text": "%s"}]}' % '§c当前无法发送弹幕', playerId)
			return

		try:
			content = data['content']
			content = re.sub(r'\s', ' ', content.strip())
			if not content[3:]:
				# 除了颜色代码以外没有任何其他字符
				raise ValueError
			comp = self.CreateComponent(serverApi.GetLevelId(), "Minecraft", "game")
			if not comp.CheckWordsValid(content[3:]) or len(content[3:].decode('utf-8')) > 20:
				# 屏蔽字
				raise ValueError
			iconId = data['iconId']
			if iconId == -1:
				iconId = ()  # 不携带头像
			if iconId not in self.mIconMapping:
				raise KeyError
		except:
			import traceback
			traceback.print_exc()
			alertSystem = serverApi.GetSystem("neteaseAlert", "neteaseAlertDev")
			if alertSystem:
				alertSystem.Alert(playerId, '§c内容不合法或存在敏感词。', 2, 0.5, 0.5)
			else:
				comp = self.CreateComponent(playerId, 'Minecraft', 'command')
				comp.SetCommand('tellraw @s {"rawtext": [{"text": "%s"}]}' % '§c内容不合法或存在敏感词', playerId)
			return

		if playerId in self.mPlayerId2InteractCD and now - self.mPlayerId2InteractCD[playerId] < self.mInterval:
			alertSystem = serverApi.GetSystem("neteaseAlert", "neteaseAlertDev")
			if alertSystem:
				alertSystem.Alert(playerId, '§e发言过快，请稍事休息。', 2, 0.5, 0.5)
			else:
				comp = self.CreateComponent(playerId, 'Minecraft', 'command')
				comp.SetCommand('tellraw @s {"rawtext": [{"text": "%s"}]}' % '§e发言过快，请稍事休息。', playerId)
			return

		p = random.randint(1, 100)
		mode = p > self.mP and 'm' or 'r'  # 出现在中部的弹幕是概率判定产生的
		rand = random.randint(*(mode == 'm' and self.mMR or self.mRR))  # 这个影响到弹幕的存活时间，也是配置的

		self.NotifyToClient(playerId, 'DanmuPublishEvent', {  # 自己发送的弹幕直接推下去，客户端优先“伪造”显示
			'icon': self.mIconMapping[iconId]['icon'],
			'content': content,
			'mode': mode,
			'rand': rand
		})

		rec = pickle.dumps({  # 序列化
			'playerId': playerId,
			'iconId': iconId,
			'content': content,
			'mode': mode,
			'rand': rand
		}, 2)
		self.mDanmuWaitlist.append(rec)
		self.mPlayerId2InteractCD[playerId] = now  # 记录发送冷却

	def OnHintIconUnlockText(self, data):
		"""
		弹出头像标识解锁提示信息
		"""
		print 'OnHintIconUnlockText', data
		playerId = data.get("playerId", "-1")
		uid = netgameApi.GetPlayerUid(playerId)
		if not uid:
			print 'can not get uid by playerId: %s' % playerId
			return
		iconId = data['iconId']
		if iconId in self.mIconMapping:
			hint = self.mIconMapping[iconId]['unlock_text']
			alertSystem = serverApi.GetSystem("neteaseAlert", "neteaseAlertDev")
			if alertSystem:
				alertSystem.Alert(playerId, hint, 2, 0.5, 0.5)
			else:
				comp = self.CreateComponent(playerId, 'Minecraft', 'command')
				comp.SetCommand('tellraw @s {"rawtext": [{"text": "%s"}]}' % '§e{}'.format(hint), playerId)

	def PreOpenDanmuFrame(self, conn, uid):
		try:
			c = conn.cursor()
			c.execute('SELECT icon_id FROM neteaseDanmuIconInfo WHERE uid=%s', (uid,))
			return tuple(row[0] for row in c.fetchall())
		except:
			conn.rollback()

	def OpenDanmuFrame(self, uid, **kwargs):
		"""
		打开弹幕操作界面
		:param uid: 玩家的uid
		:param kwargs: 这个外部调用不可以填写
		"""

		print 'OpenDanmuFrame', uid
		playerId = netgameApi.GetPlayerIdByUid(uid)
		if not playerId:
			print 'can not get playerId by uid: %s' % uid
			return
		if 'data' in kwargs:
			# 代表数据库查询回来了
			unlocks = []
			locks = []
			assets = kwargs['data'] or ()
			for item in self.mIcons:
				pair = (item['icon_id'], item['icon'])
				if item['lock'] and item['icon_id'] not in assets:
					if pair not in locks:
						locks.append(pair + (1,))
				elif pair not in unlocks:
					unlocks.append(pair + (0,))
			self.NotifyToClient(playerId, 'DisplayDanmuFrameEvent', {
				'icons': unlocks + locks,
				'colors': self.mColors
			})
		else:
			# 打开前先去数据库查询玩家已解锁的头像
			mysqlPool.AsyncExecuteFunctionWithOrderKey(
				self.PreOpenDanmuFrame,
				'PLAYER_%s_OPEN_DANMU_FRAME' % uid,
				lambda data: self.OpenDanmuFrame(uid, data=data),
				uid
			)
