# -*- coding: utf-8 -*-

import time
import lobbyGame.netgameApi as netgameApi
import apolloCommon.commonNetgameApi as commonNetgameApi
import logout
import neteasePeaceScript.peaceConst as peaceConst
import apolloCommon.mysqlPool as mysqlPool
import server.extraServerApi as serverApi

ServerSystem = serverApi.GetServerSystemCls()


class PeaceServerSystem(ServerSystem):
	"""
	该mod的服务端类
	记录了玩家pvp的过滤设置
	击败对象列表
	与仇敌列表
	"""

	def __init__(self, namespace, systemName):
		ServerSystem.__init__(self, namespace, systemName)
		self.mPlayerId2Hood = {}  # playerId与其好友
		self.mPlayerId2Crew = {}  # playerId与其队友
		self.mPlayerId2Gang = {}  # playerId与其公会人员
		self.mPVPSwitchInfo = {}  # uid与其pvp设置，用于直接做一些条件判断
		self.mPlayerId2InteractCD = {}  # 冷却
		if not self.InitMysqlPool():
			return
		if not self.InitPeaceCfg():
			return

		self.ListenForEvent(serverApi.GetEngineNamespace(), serverApi.GetEngineSystemName(), peaceConst.AddServerPlayerEvent, self, self.OnAddServerPlayer)
		self.ListenForEvent(serverApi.GetEngineNamespace(), serverApi.GetEngineSystemName(), peaceConst.DelServerPlayerEvent, self, self.OnDelServerPlayer)
		self.ListenForEvent(serverApi.GetEngineNamespace(), serverApi.GetEngineSystemName(), 'DamageEvent', self, self.OnDamage)
		self.ListenForEvent(serverApi.GetEngineNamespace(), serverApi.GetEngineSystemName(), 'PlayerDieEvent', self, self.OnPlayerDie)
		self.ListenForEvent(peaceConst.ModName, peaceConst.ClientSystemName, 'PVPSwitchEvent', self, self.OnPVPSwitch)
		self.ListenForEvent(peaceConst.ModName, peaceConst.ClientSystemName, 'DropProtectEvent', self, self.OnDropProtect)
		self.ListenForEvent("neteaseFriend", "neteaseFriendDev", "FriendsListChangeEvent", self, self.OnSyncFriends)
		self.ListenForEvent("neteaseGuild", "neteaseGuildDev", "PlayerGuildMembersChangeEvent", self, self.OnPlayerGuildMembersChangeEvent)
		self.ListenForEvent("neteaseGuild", "neteaseGuildGameDev", "PlayerGuildMembersChangeEvent", self, self.OnPlayerGuildMembersChangeEvent)

	def Destroy(self):
		self.UnListenForEvent(serverApi.GetEngineNamespace(), serverApi.GetEngineSystemName(), peaceConst.AddServerPlayerEvent, self, self.OnAddServerPlayer)
		self.UnListenForEvent(serverApi.GetEngineNamespace(), serverApi.GetEngineSystemName(), peaceConst.DelServerPlayerEvent, self, self.OnDelServerPlayer)
		self.UnListenForEvent(serverApi.GetEngineNamespace(), serverApi.GetEngineSystemName(), 'DamageEvent', self, self.OnDamage)
		self.UnListenForEvent(serverApi.GetEngineNamespace(), serverApi.GetEngineSystemName(), 'PlayerDieEvent', self, self.OnPlayerDie)
		self.UnListenForEvent(peaceConst.ModName, peaceConst.ClientSystemName, 'PVPSwitchEvent', self, self.OnPVPSwitch)
		self.UnListenForEvent(peaceConst.ModName, peaceConst.ClientSystemName, 'DropProtectEvent', self, self.OnDropProtect)
		self.UnListenForEvent("neteaseFriend", "neteaseFriendDev", "FriendsListChangeEvent", self, self.OnSyncFriends)
		self.UnListenForEvent("neteaseGuild", "neteaseGuildDev", "PlayerGuildMembersChangeEvent", self, self.OnPlayerGuildMembersChangeEvent)
		self.UnListenForEvent("neteaseGuild", "neteaseGuildGameDev", "PlayerGuildMembersChangeEvent", self, self.OnPlayerGuildMembersChangeEvent)
		mysqlPool.Finish()

	def InitMysqlPool(self):
		try:
			mysqlPool.InitDB(20)
		except:
			logout.error("Exception in InitMysqlPool")
			return False
		return True

	def InitPeaceCfg(self):
		cfg = commonNetgameApi.GetModJsonConfig("neteasePeaceScript")
		if not cfg:
			logout.error("nothing in InitPeaceCfg")
			return False
		self.mDropProtect = cfg['DropProtect']
		self.mPVPMode = cfg['PVPMode']
		self.mLoserListLenLimit = cfg['LoserListLenLimit']
		self.mFoeListLenLimit = cfg['FoeListLenLimit']
		self.mSwitchCD = cfg['SwitchCD']
		return True

	def Update(self):
		# timermanager.timerManager.tick()
		pass

	def InsertAndDelete(self, conn, f, t, fName, tName, now, fl, tl):
		"""
		一次击杀会产生一个仇敌和一个击败对象（相互）
		超过了列表上限则需要删掉最旧的
		f是击杀方的uid
		t是被击杀方的uid
		fl是击败对象列表上限
		tl是仇敌列表上限
		"""
		try:
			c = conn.cursor()
			c.execute('SELECT COUNT(1) FROM neteasePVPRec WHERE uid1=%s AND foe=%s AND uid2!=%s', (f, 0, t))
			cur = c.fetchone()[0]
			if cur >= fl:
				c.execute('SELECT uid1, uid2 FROM neteasePVPRec WHERE uid1=%s AND foe=%s ORDER BY t LIMIT 1', (f, 0))
				parameters = c.fetchone()
				if parameters:
					c.execute('DELETE FROM neteasePVPRec WHERE uid1=%s AND uid2=%s AND foe=%s', parameters + (0,))
			c.execute(
				'INSERT INTO neteasePVPRec VALUES (%s, %s, %s, %s, %s, %s) ON DUPLICATE KEY UPDATE uname = VALUES(uname), ts = ts + 1, t = VALUES(t)',
				(f, t, 0, tName, 1, now))

			c.execute('SELECT COUNT(1) FROM neteasePVPRec WHERE uid1=%s AND foe=%s AND uid2!=%s', (t, 1, f))
			cur = c.fetchone()[0]
			if cur >= tl:
				c.execute('SELECT uid1, uid2 FROM neteasePVPRec WHERE uid1=%s AND foe=%s ORDER BY t LIMIT 1', (t, 1))
				parameters = c.fetchone()
				if parameters:
					c.execute('DELETE FROM neteasePVPRec WHERE uid1=%s AND uid2=%s AND foe=%s', parameters + (1,))
			c.execute(
				'INSERT INTO neteasePVPRec VALUES (%s, %s, %s, %s, %s, %s) ON DUPLICATE KEY UPDATE uname = VALUES(uname), ts = ts + 1, t = VALUES(t)',
				(t, f, 1, fName, 1, now))
			conn.commit()
		except Exception as e:
			import traceback
			traceback.print_exc()
			conn.rollback()

	def AppendNewRec(self, f, t, fName, tName):
		"""
		一次击杀
		双方记录
		"""
		now = time.strftime('%Y-%m-%d %H:%M:%S')
		mysqlPool.AsyncExecuteFunctionWithOrderKey(
			self.InsertAndDelete,
			'NEW_PVP_REC',
			lambda *args: None,
			f, t, fName, tName, now, self.mLoserListLenLimit, self.mFoeListLenLimit
		)

	def OnPlayerDie(self, data):
		"""
		监听玩家死亡事件，建立仇恨记录
		"""
		# 假如使用了battle插件，死亡逻辑由battle插件代理
		s = serverApi.GetSystem("neteaseBattle", "neteaseBattleDev")
		if s:
			return
		# 击杀与被击杀双方必须都是玩家，才会产生仇恨记录
		f = netgameApi.GetPlayerUid(data['attacker'])
		t = netgameApi.GetPlayerUid(data['id'])
		if not f or not t:
			return
		comp = self.CreateComponent(data['attacker'], "Minecraft", "name")
		fName = comp.GetName()
		comp = self.CreateComponent(data['id'], "Minecraft", "name")
		tName = comp.GetName()
		self.AppendNewRec(f, t, fName, tName)

	def OnDamage(self, data):
		"""
		根据过滤列表屏蔽伤害
		"""
		# 假如使用了battle插件，伤害屏蔽功能由battle插件代理
		s = serverApi.GetSystem("neteaseBattle", "neteaseBattleDev")
		if s:
			return
		f = netgameApi.GetPlayerUid(data['srcId'])
		t = netgameApi.GetPlayerUid(data['entityId'])
		if not f or not t:
			return
		if self.mPVPMode:
			if self.GetPVPStatus(f) or self.GetPVPStatus(t):
				if self.CancelDamage(data['srcId'], f, t):
					data['damage'] = 0
					data['knock'] = False
					data['ignite'] = False
			else:
				data['damage'] = 0
				data['knock'] = False
				data['ignite'] = False
		elif self.GetPVPStatus(f) and self.GetPVPStatus(t):
			if self.CancelDamage(data['srcId'], f, t):
				data['damage'] = 0
				data['knock'] = False
				data['ignite'] = False
		else:
			data['damage'] = 0
			data['knock'] = False
			data['ignite'] = False

	def PostPVPSwitch(self, conn, operation, parameters):
		try:
			c = conn.cursor()
			c.execute(operation, parameters)
			rowcount = c.rowcount
			conn.commit()
		except Exception as e:
			conn.rollback()
			logout.error('Exception in PostPVPSwitch e: {} operation: {} parameters: {}'.format(e, operation, parameters))
			return False
		return int(rowcount)  # 返回数据库中影响的行数，python2中该数字原始格式为long

	def OnDropProtect(self, data):
		"""
		背包物品掉落限制
		"""
		playerId = data['playerId']
		uid = netgameApi.GetPlayerUid(playerId)
		if not uid:
			print 'can not get uid by playerId: %s' % playerId
			return
		if self.mDropProtect:
			comp = self.CreateComponent(playerId, "Minecraft", "player")
			comp.EnableKeepInventory(True)

	def OnPVPSwitch(self, data):
		"""
		切换PVP开关
		"""
		playerId = data.pop('playerId')
		uid = netgameApi.GetPlayerUid(playerId)
		if not uid:
			print 'can not get uid by playerId: %s' % playerId
			return
		now = time.time()
		if now - self.mPlayerId2InteractCD.get(playerId, 0.0) < self.mSwitchCD:
			data['switch'] = self.mPVPSwitchInfo[uid]['switch']
			comp = self.CreateComponent(playerId, 'Minecraft', 'command')
			alertSystem = serverApi.GetSystem("neteaseAlert", "neteaseAlertDev")
			if alertSystem:
				alertSystem.Alert(playerId, '冷却时间内，无法切换PVP模式。', 2, 0.5, 0.33)
			else:
				comp.SetCommand('tellraw @s {"rawtext": [{"text": "%s"}]}' % '{}'.format('§e冷却时间内，无法切换PVP模式。'), playerId)
		else:
			self.mPlayerId2InteractCD[playerId] = now
		new = {'switch': data['switch'], 'hood': data['hood'], 'crew': data['crew'], 'gang': data['gang']}
		if new != self.mPVPSwitchInfo.get(uid):
			# 设置的确发生了改变才存数据库
			self.mPVPSwitchInfo[uid] = new
			mysqlPool.AsyncExecuteFunctionWithOrderKey(
				self.PostPVPSwitch,
				'INSERT_OR_UPDATE_PLAYER_%s_PVP' % uid,
				lambda *args: None,
				'INSERT INTO neteasePVPPlayerInfo VALUES (%s, %s, %s, %s, %s) ON DUPLICATE KEY UPDATE switch = VALUES(switch), hood = VALUES(hood), crew = VALUES(crew), gang = VALUES(gang)',
				(uid, self.mPVPSwitchInfo[uid]['switch'], self.mPVPSwitchInfo[uid]['hood'], self.mPVPSwitchInfo[uid]['crew'], self.mPVPSwitchInfo[uid]['gang'])
			)

	def FindOne(self, conn, operation, parameters):
		try:
			c = conn.cursor()
			c.execute(operation, parameters)
			return c.fetchone()
		except Exception as e:
			conn.rollback()
			logout.error('Exception in Find e: {} operation: {} parameters: {}'.format(e, operation, parameters))
			return False

	def OnAddServerPlayer(self, data):
		"""
		服务端玩家进入游戏的时候去数据库取该玩家的pvp设置
		"""

		print 'OnAddServerPlayer', data
		playerId = data.get("id", "-1")
		uid = netgameApi.GetPlayerUid(playerId)
		if not uid:
			print 'can not get uid by playerId: %s' % playerId
			return
		self.mPVPSwitchInfo.pop(uid, -1)
		mysqlPool.AsyncExecuteFunctionWithOrderKey(
			self.FindOne,
			'QUERY_PLAYER_%s_PVP_INFO' % uid,
			lambda row: self.mPVPSwitchInfo.__setitem__(uid, row and {'switch': row[1], 'hood': row[2], 'crew': row[3], 'gang': row[4]} or {'switch': 0, 'hood': 0, 'crew': 0, 'gang': 0}),
			'SELECT * FROM neteasePVPPlayerInfo WHERE uid=%s',
			(uid,)
		)

		self.RequestFriendList(playerId, uid)

	def RequestFriendList(self, playerId, uid):
		"""
		通过向好友插件的service请求的方式拉取玩家的好友列表
		"""
		self.RequestToService(
			"neteaseFriend", "RequestFriendListsEvent", {"uid": uid},
			lambda suc, args: self.RequestFriendCb(suc, args, playerId), 3)

	def RequestFriendCb(self, suc, args, playerId):
		if not suc:
			return
		friendUidLists = args.get("friendUidLists")
		self.UpdatePlayerId2Hood(playerId, set(friendUidLists))

	def OnSyncFriends(self, args):
		"""
		监听好友变化的事件（来自好友插件的service）
		"""
		uid = args.get("uid")
		friendUidLists = args.get("friendUids")
		playerId = netgameApi.GetPlayerIdByUid(uid)
		if playerId == "":
			return
		self.UpdatePlayerId2Hood(playerId, set(friendUidLists))

	def OnPlayerGuildMembersChangeEvent(self, args):
		"""
		监听公会成员变化的事件（来自公会插件的service）
		"""
		uid = args.get("uid")
		guildMembers = args.get("guildMembers")
		playerId = netgameApi.GetPlayerIdByUid(uid)
		if playerId == "":
			return
		self.UpdatePlayerId2Gang(playerId, set(guildMembers))

	def OnDelServerPlayer(self, data):
		print 'OnDelServerPlayer', data
		self.mPlayerId2Gang.pop(data['id'], -1)
		self.mPlayerId2Crew.pop(data['id'], -1)
		self.mPlayerId2Hood.pop(data['id'], -1)
		self.mPlayerId2InteractCD.pop(data['id'], -1)

	def UpdatePlayerId2Hood(self, playerId, hood):
		if not hood:
			self.mPlayerId2Hood.pop(playerId, -1)
		else:
			self.mPlayerId2Hood[playerId] = hood

	def UpdatePlayerId2Crew(self, playerId, crew):
		if not crew:
			self.mPlayerId2Crew.pop(playerId, -1)
		else:
			self.mPlayerId2Crew[playerId] = crew

	def UpdatePlayerId2Gang(self, playerId, gang):
		if not gang:
			self.mPlayerId2Gang.pop(playerId, -1)
		else:
			self.mPlayerId2Gang[playerId] = gang

	# mod.json中配置的pvp模式，详见mod.json
	def GetPVPMode(self):
		return self.mPVPMode

	def SetPVPMode(self, mode):
		if isinstance(mode, int) and mode in (0, 1):
			self.mPVPMode = mode

	def SetPVPStatus(self, uid, switch):
		if uid in self.mPVPSwitchInfo:
			self.mPVPSwitchInfo[uid]['switch'] = int(bool(switch))
			return True
		return False

	def GetPVPStatus(self, uid):
		return uid in self.mPVPSwitchInfo and self.mPVPSwitchInfo[uid]['switch']

	def GetPVPSwitchInfo(self, uid):
		return self.mPVPSwitchInfo.get(uid)

	def SetPVPSwitchInfo(self, uid, info):
		if uid not in self.mPVPSwitchInfo:
			return False
		if 'hood' not in info or 'crew' not in info or 'gang' not in info:
			return False
		self.mPVPSwitchInfo[uid] = {
			'switch': self.mPVPSwitchInfo[uid]['switch'],
			'hood': int(bool(info['hood'])),
			'crew': int(bool(info['crew'])),
			'gang': int(bool(info['gang']))
		}
		return True

	def CancelDamage(self, playerId, f, t):
		if f in self.mPVPSwitchInfo and self.mPVPSwitchInfo[f]['hood'] and playerId in self.mPlayerId2Hood and t in self.mPlayerId2Hood[playerId]:
			return True
		if f in self.mPVPSwitchInfo and self.mPVPSwitchInfo[f]['crew'] and playerId in self.mPlayerId2Crew and t in self.mPlayerId2Crew[playerId]:
			return True
		if f in self.mPVPSwitchInfo and self.mPVPSwitchInfo[f]['gang'] and playerId in self.mPlayerId2Gang and t in self.mPlayerId2Gang[playerId]:
			return True

	def Fmt(self, t):
		try:
			dt = int(time.time() - time.mktime(time.strptime(t, '%Y-%m-%d %H:%M:%S')))
			if dt < 3600:
				return '刚刚'
			if dt < 86400:
				return '{}小时前'.format(dt // 3600)
			if dt < 604800:
				return '{}天前'.format(dt // 86400)
			return '7天前'
		except:
			pass
		return ''

	# 去数据库中获取击败对象与仇敌列表
	def PreOpenPeaceBoard(self, conn, uid, fl, tl):
		try:
			c = conn.cursor()
			c.execute('SELECT * FROM neteasePVPRec WHERE uid1=%s AND foe=%s ORDER BY t DESC LIMIT %s', (uid, 0, fl))
			haters = [{'uname': row[3], 'ts': row[4], 't': self.Fmt(row[5])} for row in c.fetchall()]
			c.execute('SELECT * FROM neteasePVPRec WHERE uid1=%s AND foe=%s ORDER BY t DESC LIMIT %s', (uid, 1, tl))
			fakers = [{'uname': row[3], 'ts': row[4], 't': self.Fmt(row[5])} for row in c.fetchall()]
			c.execute('SELECT * FROM neteasePVPPlayerInfo WHERE uid=%s', (uid,))
			row = c.fetchone()
			return {
				'haters': haters,
				'fakers': fakers,
				'filter': row
			}
		except:
			conn.rollback()
			return False

	def OpenPeaceBoard(self, uid, **kwargs):
		"""
		打开PVP界面
		"""
		print 'OpenPeaceBoard', uid
		playerId = netgameApi.GetPlayerIdByUid(uid)
		if not playerId:
			print 'can not get playerId by uid: %s' % uid
			return
		if 'data' in kwargs:
			row = kwargs['data']['filter']
			if uid in self.mPVPSwitchInfo:
				# 内存为准
				kwargs['data']['filter'] = self.mPVPSwitchInfo[uid]
			elif row:
				kwargs['data']['filter'] = self.mPVPSwitchInfo[uid] = {
					'switch': row[1],
					'hood': row[2],
					'crew': row[3],
					'gang': row[4]
				}
			else:
				# 玩家默认设置
				kwargs['data']['filter'] = self.mPVPSwitchInfo[uid] = {
					'switch': 0,
					'hood': 0,
					'crew': 0,
					'gang': 0
				}
			if playerId not in self.mPlayerId2InteractCD:
				left = 0
			else:
				left = self.mSwitchCD - int(time.time() - self.mPlayerId2InteractCD[playerId])
				if left < 0:
					left = 0
			kwargs['data']['left'] = left
			kwargs['data']['cd'] = self.mSwitchCD
			self.NotifyToClient(playerId, 'DisplayPeaceBoardEvent', kwargs['data'])
		else:
			mysqlPool.AsyncExecuteFunctionWithOrderKey(
				self.PreOpenPeaceBoard,  # 先去数据库中获取击败对象与仇敌列表
				'PLAYER_%s_OPEN_PEACE_BOARD' % uid,
				lambda data: data and self.OpenPeaceBoard(uid, data=data),
				uid, self.mLoserListLenLimit, self.mFoeListLenLimit
			)

	def QueryPVPInfo(self, uid, cb):
		"""
		获得一个玩家PVP相关信息（包含击败对象与仇敌）
		"""
		def demo(conn, uid):
			try:
				c = conn.cursor()
				c.execute('SELECT * FROM neteasePVPRec WHERE uid1=%s AND foe=%s ORDER BY t DESC', (uid, 0))
				l1 = [{'uname': row[3], 'ts': row[4], 't': row[5]} for row in c.fetchall()]  # 击败对象列表
				c.execute('SELECT * FROM neteasePVPRec WHERE uid1=%s AND foe=%s ORDER BY t DESC', (uid, 1))
				l2 = [{'uname': row[3], 'ts': row[4], 't': self.Fmt(row[5])} for row in c.fetchall()]  # 仇敌列表
				return {'l1': l1, 'l2': l2}
			except:
				conn.rollback()
				return False

		mysqlPool.AsyncExecuteFunctionWithOrderKey(
			demo,
			'DEMO',
			cb,
			uid
		)
