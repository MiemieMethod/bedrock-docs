# -*- coding: utf-8 -*-

import time
import lobbyGame.netgameApi as netgameApi
# import apolloCommon.commonNetgameApi as commonNetgameApi
import logout
import neteaseDailyScript.dailyConst as dailyConst
# import neteaseDailyScript.timermanager as timermanager
import server.extraServerApi as serverApi

ServerSystem = serverApi.GetServerSystemCls()


class DailyServerSystem(ServerSystem):
	"""
	该mod的服务端类
	中转客户端请求至service
	与同步service返回至客户端
	"""

	def __init__(self, namespace, systemName):
		ServerSystem.__init__(self, namespace, systemName)
		self.mRewards = None
		if not self.InitDailyCfg():
			return

		self.ListenForEvent(dailyConst.ModName, dailyConst.ClientSystemName, dailyConst.PlayerRecvEvent, self, self.OnPlayerRecv)  # 领取请求

	def InitDailyCfg(self):
		import apolloCommon.commonNetgameApi as commonNetgameApi
		cfg = commonNetgameApi.GetModJsonConfig("neteaseDailyScript")
		if not cfg:
			logout.error("nothing in InitDailyCfg")
			return False
		raw = {}
		for reward in cfg[dailyConst.CfgKeyRewards]:
			departure = time.strptime(reward['date'], '%Y-%m-%d')
			if departure.tm_wday:
				# 这天不是周一
				# 配置有误
				logout.warning('配置段 {} 不生效因日期 {} 非周一'.format(reward, reward['date']))
				continue
			date = time.strftime('%Y-%m-%d', departure)
			if date in raw:
				logout.warning('配置段 {} 被配置段 {} 替换'.format(raw[date][-1], reward))
			raw[date] = (time.mktime(departure), reward['weekly'])
		if not raw:
			logout.warning('所有配置段均不生效')
			return False
		raw = raw.values()
		raw.sort()
		self.mRewards = raw
		return True

	def Destroy(self):
		self.UnListenForEvent(dailyConst.ModName, dailyConst.ClientSystemName, dailyConst.PlayerRecvEvent, self, self.OnPlayerRecv)
		self.mRewards = None

	def Update(self):
		# timermanager.timerManager.tick()
		pass

	def DailyServerRender(self, playerId, eventName, respData):
		print playerId, eventName, respData
		if eventName == dailyConst.DisplayDailyRewardEvent:
			if respData['code'] == dailyConst.RespCodeSuccess:
				stamp = respData['entity']['stamp']
				tm = time.localtime(stamp)
				date = time.strftime('%Y-%m-%d', tm)
				if stamp >= self.mRewards[-1][0]:
					# 当前时间已经超过最后一段配置的起始时间
					weekly = self.mRewards[-1][-1]
				elif stamp < self.mRewards[0][0]:
					print 'not yet', self.mRewards[0][0]
					return
				else:
					for i, v in enumerate(self.mRewards[1:]):
						if stamp < v[0]:
							weekly = self.mRewards[i][-1]
							break
				self.NotifyToClient(playerId, eventName, {
					'valid': date,
					'tm_wday': tm.tm_wday,
					'weekly': weekly,
					'recv': respData['entity']['recv']
				})
		elif eventName == dailyConst.PlayerRecvEvent:
			logout.info('玩家 {} 领取每日签到奖励返回 {}'.format(playerId, respData))  # TODO
			print respData
			comp = self.CreateComponent(playerId, 'Minecraft', 'command')
			if respData['code'] == dailyConst.RespCodeSuccess:
				date = respData['entity']['date']
				tm = time.strptime(date, '%Y-%m-%d')
				result = self.Preview(playerId, tm, comp)
				if not result:
					# 需要回滚
					logout.warning('玩家 {} 于日期 {} 领取每日签到奖励回滚'.format(playerId, date))
					uid = netgameApi.GetPlayerUid(playerId)
					if not uid:
						print 'can not get uid by playerId: %s' % playerId
						return
					self.RequestToService(
						dailyConst.ModName,
						'DailyRollback',
						{'uid': uid, 'date': date},
						lambda rtn, data: logout.info('玩家 {} 于日期 {} 领取每日签到奖励回滚返回 {}'.format(playerId, date, (rtn, data)))
					)
					return
				rewards, free = result
				logout.info('准备发放每日签到奖励至玩家 {} 背包的 {} 空格中'.format(playerId, free))
				itemComp = self.CreateComponent(playerId, 'Minecraft', 'item')
				# 发奖
				for reward in rewards:
					item = (reward['reward_item_id'], reward['reward_item_count'])
					auxValue = item[0].split(':')[-1]
					itemDict = {
						'itemName': item[0][:-1 - len(auxValue)],
						'count': item[-1],
						'enchantData': [],
						'auxValue': int(auxValue or 0),
						'extraId': ''
					}
					itemComp.SpawnItemToPlayerInv(itemDict, playerId, free.pop(0))
				alertSystem = serverApi.GetSystem("neteaseAlert", "neteaseAlertDev")
				if alertSystem:
					alertSystem.Alert(playerId, '§a领取成功。', 2, 0.5, 0.8)
				else:
					comp.SetCommand('tellraw @s {"rawtext": [{"text": "%s"}]}' % '§a领取成功', playerId)
				self.NotifyToClient(playerId, eventName, {
					'valid': date,
					'wday': (tm.tm_wday + 1) % 7
				})
			else:
				if 'entity' in respData:
					date = respData['entity']['date']
					tm = time.strptime(date, '%Y-%m-%d')
					w = (tm.tm_wday + 1) % 7
					self.NotifyToClient(playerId, eventName, {
						'valid': date,
						'wday': w
					})
					alertSystem = serverApi.GetSystem("neteaseAlert", "neteaseAlertDev")
					if alertSystem:
						alertSystem.Alert(playerId, '§c{}。'.format(respData['message']), 2, 0.5, 0.8)
					else:
						comp.SetCommand('tellraw @s {"rawtext": [{"text": "%s"}]}' % '§c{}'.format(respData['message']), playerId)
				else:
					# 数据库操作失败
					alertSystem = serverApi.GetSystem("neteaseAlert", "neteaseAlertDev")
					if alertSystem:
						alertSystem.Alert(playerId, '§c领取失败。', 2, 0.5, 0.8)
					else:
						comp.SetCommand('tellraw @s {"rawtext": [{"text": "%s"}]}' % '§c领取失败', playerId)

	def Preview(self, playerId, tm, alert):
		# 查询背包空格是否足够领取奖励
		stamp = time.mktime(tm)
		if stamp < self.mRewards[0][0]:
			print 'not yet', self.mRewards[0][0], playerId
			return
		w = str((tm.tm_wday + 1) % 7)
		# if stamp >= self.mRewards[0][0]:
		if stamp >= self.mRewards[-1][0]:
			weekly = self.mRewards[-1][-1]
		else:
			for i, v in enumerate(self.mRewards[1:]):
				if stamp < v[0]:
					weekly = self.mRewards[i][-1]
					break
		if w not in weekly or weekly[w].get('rewards') is None:
			alertSystem = serverApi.GetSystem("neteaseAlert", "neteaseAlertDev")
			if alertSystem:
				alertSystem.Alert(playerId, '§c无奖励。', 2, 0.5, 0.8)
			else:
				alert.SetCommand('tellraw @s {"rawtext": [{"text": "%s"}]}' % '§c无奖励', playerId)
			return
		demand = len(weekly[w]['rewards'])
		free = []
		if len(free) < demand:
			itemComp = self.CreateComponent(playerId, 'Minecraft', 'item')
			if not itemComp:
				return
			inv = serverApi.GetMinecraftEnum().ItemPosType.INVENTORY
			for i in xrange(36):
				if itemComp.GetPlayerItem(inv, i) is None:
					free.append(i)
					if len(free) >= demand:
						break
		if len(free) < demand:
			alertSystem = serverApi.GetSystem("neteaseAlert", "neteaseAlertDev")
			if alertSystem:
				alertSystem.Alert(playerId, '§c领取奖励需要{}个空格。'.format(demand), 2, 0.5, 0.8)
			else:
				alert.SetCommand('tellraw @s {"rawtext": [{"text": "%s"}]}' % '§c领取奖励需要{}个空格'.format(demand), playerId)
			return
		return weekly[w]['rewards'], free

	def OnPlayerRecv(self, data):
		now = time.localtime()
		date = time.strftime('%Y-%m-%d', now)
		print 'OnPlayerRecv', data, date
		playerId = data.get("playerId", "-1")
		uid = netgameApi.GetPlayerUid(playerId)
		if not uid:
			print 'can not get uid by playerId: %s' % playerId
			return
		comp = self.CreateComponent(playerId, 'Minecraft', 'command')
		if date != data.get('valid'):  # 验证客户端点击领取的时刻是否为服务器时间的同一天
			alertSystem = serverApi.GetSystem("neteaseAlert", "neteaseAlertDev")
			if alertSystem:
				alertSystem.Alert(playerId, '§c领取失败。', 2, 0.5, 0.8)
			else:
				comp.SetCommand('tellraw @s {"rawtext": [{"text": "%s"}]}' % '§c领取失败', playerId)
			return
		if not self.Preview(playerId, now, comp):  # 查询背包格子是否足够
			# comp.SetCommand('tellraw @s {"rawtext": [{"text": "%s"}]}' % '§c领取失败', playerId)
			return
		alertSystem = serverApi.GetSystem("neteaseAlert", "neteaseAlertDev")
		if alertSystem:
			alertSystem.Alert(playerId, '§e领取中，请稍候……', 2, 0.5, 0.8)
		else:
			comp.SetCommand('tellraw @s {"rawtext": [{"text": "%s"}]}' % '§e领取中，请稍候……', playerId)
		self.RequestToService(
			dailyConst.ModName,
			dailyConst.PlayerRecvEvent,
			{'uid': uid, 'date': date},
			lambda rtn, data: self.DailyServerRender(playerId, dailyConst.PlayerRecvEvent, data) if rtn else (alertSystem.Alert(playerId, '§c领取超时。', 2, 0.5, 0.8) if alertSystem else comp.SetCommand('tellraw @s {"rawtext": [{"text": "%s"}]}' % '§c领取超时', playerId)),
			4
		)

	def OpenDailyReward(self, uid):
		"""
		使一个玩家打开每日登录奖励的界面
		"""
		stamp = time.time()
		print 'OpenDailyReward', uid, stamp
		playerId = netgameApi.GetPlayerIdByUid(uid)
		if not playerId:
			print 'can not get playerId by uid: %s' % uid
			return
		if self.mRewards is None:
			logout.warning('因无可用奖励配置无法打开每日登录奖励界面')
			return
		if stamp < self.mRewards[0][0]:
			print 'not yet', self.mRewards[0][0]
			return
		self.RequestToService(
			dailyConst.ModName,
			dailyConst.DisplayDailyRewardEvent,
			{'uid': uid, 'stamp': stamp},
			lambda rtn, data: rtn and self.DailyServerRender(playerId, dailyConst.DisplayDailyRewardEvent, data)
		)
