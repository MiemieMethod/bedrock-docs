# -*- coding: utf-8 -*-

import hmac
import hashlib
import json
import lobbyGame.netgameApi as netgameApi
# import apolloCommon.commonNetgameApi as commonNetgameApi
import serverhttp
import logout
import neteaseChillScript.chillConst as chillConst
import neteaseChillScript.timermanager as timermanager
import server.extraServerApi as serverApi

ServerSystem = serverApi.GetServerSystemCls()


class ChillServerSystem(ServerSystem):
	"""
	该mod的服务端类
	"""
	def __init__(self, namespace, systemName):
		ServerSystem.__init__(self, namespace, systemName)
		# self.mChillClique = set()
		# self.mChillTrench = set()
		# self.mChillOnlinePlayers = {}
		self.mChillRewards = None
		# self.mChillURL = None
		# self.mChillGAMEID = None
		# self.mChillGAMEKEY = None
		if not self.InitChillCfg():
			return

		# self.ListenForEvent(serverApi.GetEngineNamespace(), serverApi.GetEngineSystemName(), chillConst.AddServerPlayerEvent, self, self.OnAddServerPlayer)
		# self.ListenForEvent(serverApi.GetEngineNamespace(), serverApi.GetEngineSystemName(), chillConst.DelServerPlayerEvent, self, self.OnDelServerPlayer)
		self.ListenForEvent(chillConst.ModName, chillConst.ClientSystemName, chillConst.PlayerRecvChillRewardEvent, self, self.OnPlayerRecv)  # 客户端请求领取活动奖励
		# self.ListenForEvent(chillConst.ModName, chillConst.ClientSystemName, chillConst.NavigateToShopEvent, self, self.OnNavigateToShop)
		# self.ListenForEvent(chillConst.ModName, chillConst.ClientSystemName, 'PlayerChillOutEvent', self, self.OnPlayerChillOut)

		# self.mChillTimer = timermanager.timerManager.addRepeatTimer(4, self.CheckChill)
		pass

	def InitChillCfg(self):
		import apolloCommon.commonNetgameApi as commonNetgameApi
		cfg = commonNetgameApi.GetModJsonConfig("neteaseChillScript")
		if not cfg:
			logout.error("nothing in InitChillCfg")
			return False
		self.mChillRewards = cfg[chillConst.CfgKeyRewards]
		# self.mChillURL = cfg['URL']
		# self.mChillGAMEID = cfg['GAMEID']
		# self.mChillGAMEKEY = cfg['GAMEKEY']
		print self.mChillRewards
		return True

	def Destroy(self):
		# if self.mChillTimer:
		# 	timermanager.timerManager.delTimer(self.mChillTimer)
		# 	self.mChillTimer = None
		# self.UnListenForEvent(serverApi.GetEngineNamespace(), serverApi.GetEngineSystemName(), chillConst.AddServerPlayerEvent, self, self.OnAddServerPlayer)
		# self.UnListenForEvent(serverApi.GetEngineNamespace(), serverApi.GetEngineSystemName(), chillConst.DelServerPlayerEvent, self, self.OnDelServerPlayer)
		self.UnListenForEvent(chillConst.ModName, chillConst.ClientSystemName, chillConst.PlayerRecvChillRewardEvent, self, self.OnPlayerRecv)
		# self.UnListenForEvent(chillConst.ModName, chillConst.ClientSystemName, chillConst.NavigateToShopEvent, self, self.OnNavigateToShop)
		# self.UnListenForEvent(chillConst.ModName, chillConst.ClientSystemName, 'PlayerChillOutEvent', self, self.OnPlayerChillOut)
		# self.mChillOnlinePlayers.clear()
		# self.mChillOnlinePlayers = None
		# self.mChillClique.clear()
		# self.mChillClique = None
		# self.mChillTrench.clear()
		# self.mChillTrench = None
		self.mChillRewards = None

	def Update(self):
		# timermanager.timerManager.tick()
		pass

	'''
	def CheckChill(self):
		if self.mChillClique and self.mChillURL:
			for uid in list(self.mChillClique):
				if uid not in self.mChillOnlinePlayers:
					self.mChillClique.discard(uid)
				# elif self.mChillOnlinePlayers.get(uid):
				else:
					# url = pro and "http://gasproxy.mc.netease.com:60002/get-mc-item-order-list" or "http://gasproxy.mc.netease.com:60001/get-mc-item-order-list"
					url = self.mChillURL
					requestBody = json.dumps({'uid': uid, 'gameid': self.mChillGAMEID})
					signature = hmac.new(self.mChillGAMEKEY, 'POST{}{}'.format('/get-mc-item-order-list', requestBody), hashlib.sha256).hexdigest()
					header = {
						'Content-Type': 'application/json',
						'Netease-Server-Sign': signature
					}
					print url, header, requestBody
					serverhttp.HttpPool().Request('POST', url, header, requestBody, lambda code, responseBody, stamp: self.OnCheckChill(uid, code, responseBody, stamp))
		if self.mChillTrench:
			for uid in list(self.mChillTrench):
				self.RequestToService(
					chillConst.ModName,
					chillConst.PlayerAchvChillRewardEvent,
					{'uid': uid},
					lambda rtn, data: rtn and self.ChillServerRender(None, chillConst.PlayerAchvChillRewardEvent, data)
				)

	def OnCheckChill(self, uid, code, responseBody, stamp):
		# if uid not in self.mChillClique or uid not in self.mChillOnlinePlayers:
		# 	return
		try:
			respData = json.loads(responseBody)
			if code != 200 or respData['code'] != chillConst.RespCodeSuccess:
				raise ValueError
			entities = respData['entities']
			for entity in entities or []:
				if int(entity['item_id']) in self.mChillRewards['triggers']:
					# 达成活动条件
					logout.info('玩家 uid: {} 购买付费商品 {} 达成活动奖励领取条件'.format(uid, entity['item_id']))
					self.mChillTrench.add(uid)
					self.mChillClique.discard(uid)
					break
		except:
			logout.error('查询玩家 uid: {} 未发货订单返回 {}'.format(uid, (code, responseBody, stamp)))  # TODO
			return

	def OnAddServerPlayer(self, data):
		print 'OnAddServerPlayer', data
		playerId = data.get("playerId", "-1")
		uid = netgameApi.GetPlayerUid(playerId)
		if not uid:
			print 'can not get uid by playerId: %s' % playerId
			return
		self.mChillOnlinePlayers[uid] = 0
		self.RequestToService(
			chillConst.ModName,
			chillConst.QueryPlayerChillEvent,
			{'uid': uid},
			lambda rtn, data: rtn and self.ChillServerRender(playerId, chillConst.QueryPlayerChillEvent, data)
		)

	def OnDelServerPlayer(self, data):
		print 'OnDelServerPlayer', data
		playerId = data.get("playerId", "-1")
		uid = netgameApi.GetPlayerUid(playerId)
		if not uid:
			print 'can not get uid by playerId: %s' % playerId
			return
		if uid in self.mChillOnlinePlayers:
			del self.mChillOnlinePlayers[uid]
		self.mChillClique.discard(uid)
	'''

	def ChillServerRender(self, playerId, eventName, respData):
		'''
		print playerId, eventName, respData
		if eventName == chillConst.QueryPlayerChillEvent:
			if respData['code'] == chillConst.RespCodeSuccess:
				uid = netgameApi.GetPlayerUid(playerId)
				if not uid:
					print 'can not get uid by playerId: %s' % playerId
					return
				qualified = respData['entity']['qualified']
				if abs(qualified) == 1:
					# 已经获得了领取资格
					# 不管是否已领
					if uid in self.mChillOnlinePlayers:
						del self.mChillOnlinePlayers[uid]
				else:
					# 无领取资格
					# 一直监控到下线
					if uid not in self.mChillOnlinePlayers:
						return
					self.mChillClique.add(uid)
		elif eventName == chillConst.DisplayChillRewardEvent:
			if respData['code'] == chillConst.RespCodeSuccess:
				# uid = netgameApi.GetPlayerUid(playerId)
				# if uid in self.mChillOnlinePlayers:
				# 	self.mChillOnlinePlayers[uid] = 1
				self.NotifyToClient(playerId, eventName, {
					'exhibits': self.mChillRewards['exhibits'],
					'desc': self.mChillRewards['desc'],
					'title': self.mChillRewards['title'],
					'qualified': respData['entity']['qualified']
				})
		elif eventName == chillConst.PlayerAchvChillRewardEvent:
			if respData['code'] == chillConst.RespCodeSuccess:
				uid = respData['entity']['uid']
				self.mChillClique.discard(uid)
				self.mChillTrench.discard(uid)
				playerId = netgameApi.GetPlayerIdByUid(uid)
				if not playerId:
					print 'can not get playerId by uid: %s' % uid
					return
				self.NotifyToClient(playerId, eventName, {'qualified': respData['entity']['qualified']})
		elif eventName == chillConst.PlayerRecvChillRewardEvent:
		'''
		if eventName == chillConst.PlayerAchvChillRewardEvent:
			if respData['code'] == chillConst.RespCodeSuccess:
				uid = respData['entity']['uid']
				# self.mChillClique.discard(uid)
				# self.mChillTrench.discard(uid)
				playerId = netgameApi.GetPlayerIdByUid(uid)
				if not playerId:
					print
					'can not get playerId by uid: %s' % uid
					return
				self.NotifyToClient(playerId, eventName, {'qualified': respData['entity']['qualified']})
		elif eventName == chillConst.DisplayChillRewardEvent:
			if respData['code'] == chillConst.RespCodeSuccess:
				# uid = netgameApi.GetPlayerUid(playerId)
				# if uid in self.mChillOnlinePlayers:
				# 	self.mChillOnlinePlayers[uid] = 1
				self.NotifyToClient(playerId, eventName, {
					'exhibits': self.mChillRewards['exhibits'],
					'desc': self.mChillRewards['desc'],
					'title': self.mChillRewards['title'],
					'qualified': respData['entity']['qualified']
				})
		elif eventName == chillConst.PlayerRecvChillRewardEvent:
			logout.info('玩家 {} 领取活动奖励返回 {}'.format(playerId, respData))  # TODO
			print respData
			comp = self.CreateComponent(playerId, 'Minecraft', 'command')
			if respData['code'] == chillConst.RespCodeSuccess:
				result = self.Preview(playerId, comp)
				if not result:
					# 需要回滚
					logout.warning('玩家 {} 领取活动奖励回滚'.format(playerId))
					uid = netgameApi.GetPlayerUid(playerId)
					if not uid:
						print 'can not get uid by playerId: %s' % playerId
						return
					self.RequestToService(
						chillConst.ModName,
						'ChillRollback',
						{'uid': uid},
						lambda rtn, data: logout.info('玩家 {} 领取活动奖励回滚返回 {}'.format(playerId, (rtn, data)))
					)
					return
				rewards, free = result
				logout.info('准备发放活动奖励至玩家 {} 背包的 {} 空格中'.format(playerId, free))
				itemComp = self.CreateComponent(playerId, 'Minecraft', 'item')
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
				self.NotifyToClient(playerId, eventName, {'qualified': -1})
			else:
				if 'entity' in respData:
					self.NotifyToClient(playerId, eventName, {'qualified': respData['entity']['qualified']})
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

	def Preview(self, playerId, alert):
		"""
		查背包是否有空余格子
		有格子则返回空格子位置
		没有则弹出提示并返回空
		"""
		if self.mChillRewards is None or 'rewards' not in self.mChillRewards:
			logout.error('无可用奖励配置')
			alertSystem = serverApi.GetSystem("neteaseAlert", "neteaseAlertDev")
			if alertSystem:
				alertSystem.Alert(playerId, '§c无奖励。', 2, 0.5, 0.8)
			else:
				alert.SetCommand('tellraw @s {"rawtext": [{"text": "%s"}]}' % '§c无奖励', playerId)
			return
		demand = len(self.mChillRewards['rewards'])
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
		return self.mChillRewards['rewards'], free

	def OnNavigateToShop(self, data):
		"""
		打开商城界面
		"""
		print 'OnNavigateToShop', data
		playerId = data.get("playerId", "-1")
		uid = netgameApi.GetPlayerUid(playerId)
		if not uid:
			print 'can not get uid by playerId: %s' % playerId
			return
		netgameApi.NotifyClientToOpenShopUi(playerId)

	'''
	def OnPlayerChillOut(self, data):
		print 'OnPlayerChillOut', data
		playerId = data.get("playerId", "-1")
		uid = netgameApi.GetPlayerUid(playerId)
		if not uid:
			print 'can not get uid by playerId: %s' % playerId
			return
		if uid in self.mChillOnlinePlayers:
			self.mChillOnlinePlayers[uid] = 0
	'''

	def OnPlayerRecv(self, data):
		"""
		客户端请求领取活动奖励，检查背包空格后转发给service
		"""
		print 'OnPlayerRecv', data
		playerId = data.get("playerId", "-1")
		uid = netgameApi.GetPlayerUid(playerId)
		if not uid:
			print 'can not get uid by playerId: %s' % playerId
			return
		comp = self.CreateComponent(playerId, 'Minecraft', 'command')
		if not self.Preview(playerId, comp):
			# comp.SetCommand('tellraw @s {"rawtext": [{"text": "%s"}]}' % '§c领取失败', playerId)
			return
		alertSystem = serverApi.GetSystem("neteaseAlert", "neteaseAlertDev")  # 通用提示插件
		if alertSystem:
			alertSystem.Alert(playerId, '§e领取中，请稍候……', 2, 0.5, 0.8)
		else:
			comp.SetCommand('tellraw @s {"rawtext": [{"text": "%s"}]}' % '§e领取中，请稍候……', playerId)
		self.RequestToService(
			chillConst.ModName,
			chillConst.PlayerRecvChillRewardEvent,
			{'uid': uid},
			lambda rtn, data: self.ChillServerRender(playerId, chillConst.PlayerRecvChillRewardEvent, data) if rtn else (alertSystem.Alert(playerId, '§c领取超时。', 2, 0.5, 0.8) if alertSystem else comp.SetCommand('tellraw @s {"rawtext": [{"text": "%s"}]}' % '§c领取超时', playerId)),
			4
		)

	def OpenChillReward(self, uid):
		"""
		使一个玩家打开活动奖励的界面
		"""
		print 'OpenChillReward', uid
		playerId = netgameApi.GetPlayerIdByUid(uid)
		if not playerId:
			print 'can not get playerId by uid: %s' % uid
			return
		if self.mChillRewards is None or 'rewards' not in self.mChillRewards:
			logout.warning('因无可用奖励配置无法打开活动奖励界面')
			return
		self.RequestToService(
			chillConst.ModName,
			chillConst.DisplayChillRewardEvent,
			{'uid': uid},
			lambda rtn, data: rtn and self.ChillServerRender(playerId, chillConst.DisplayChillRewardEvent, data)
		)

	def AchvChillReward(self, uid):
		"""
		使一个玩家达成活动奖励的条件
		"""
		print 'AchvChillReward', uid
		playerId = netgameApi.GetPlayerIdByUid(uid)
		if not playerId:
			print 'can not get playerId by uid: %s' % uid
			return
		self.RequestToService(
			chillConst.ModName,
			chillConst.PlayerAchvChillRewardEvent,
			{'uid': uid},
			lambda rtn, data: rtn and self.ChillServerRender(None, chillConst.PlayerAchvChillRewardEvent, data)
		)
