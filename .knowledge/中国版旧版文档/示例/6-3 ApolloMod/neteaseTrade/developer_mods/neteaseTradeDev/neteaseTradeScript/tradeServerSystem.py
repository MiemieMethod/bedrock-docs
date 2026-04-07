# -*- coding: utf-8 -*-

import json, time
import lobbyGame.netgameApi as netgameApi
import apolloCommon.commonNetgameApi as commonNetgameApi
import apolloCommon.mysqlPool as mysqlPool
import logout
import neteaseTradeScript.tradeConst as tradeConst
# import neteaseTradeScript.timermanager as timermanager
import server.extraServerApi as serverApi

ServerSystem = serverApi.GetServerSystemCls()


class TradeServerSystem(ServerSystem):
	def __init__(self, namespace, systemName):
		ServerSystem.__init__(self, namespace, systemName)
		self.mD2P = {}
		self.mStallBlocks = {}
		self.mPlayerId2InteractCD = {}
		self.mX = set()
		if not self.InitMysqlPool():
			return
		if not self.InitTradeCfg():
			return

		self.ListenForEvent(serverApi.GetEngineNamespace(), serverApi.GetEngineSystemName(), "ServerBlockEntityTickEvent", self, self.OnServerBlockEntityTick)
		self.ListenForEvent(serverApi.GetEngineNamespace(), serverApi.GetEngineSystemName(), "ServerPlaceBlockEntityEvent", self, self.OnServerPlaceBlockEntity)
		self.ListenForEvent(serverApi.GetEngineNamespace(), serverApi.GetEngineSystemName(), "ServerEntityTryPlaceBlockEvent", self, self.OnServerEntityTryPlaceBlock)
		self.ListenForEvent(serverApi.GetEngineNamespace(), serverApi.GetEngineSystemName(), "ServerBlockUseEvent", self, self.OnServerBlockUse)
		self.ListenForEvent(serverApi.GetEngineNamespace(), serverApi.GetEngineSystemName(), "ServerPlayerTryDestroyBlockEvent", self, self.OnServerPlayerTryDestroyBlock)

		self.ListenForEvent(tradeConst.ModName, tradeConst.ClientSystemName, tradeConst.QueryPlayerDoughsEvent, self, self.OnQueryPlayerDoughs)
		self.ListenForEvent(tradeConst.ModName, tradeConst.ClientSystemName, tradeConst.PlayerPurchaseEvent, self, self.OnPlayerPurchase)
		self.ListenForEvent(tradeConst.ModName, tradeConst.ClientSystemName, tradeConst.MerchOnSaleEvent, self, self.OnMerchOnSale)
		self.ListenForEvent(tradeConst.ModName, tradeConst.ClientSystemName, tradeConst.PlayerWithdrawMerchEvent, self, self.OnPlayerWithdrawMerch)
		self.ListenForEvent(tradeConst.ModName, tradeConst.ClientSystemName, tradeConst.PlayerOpenStallEvent, self, self.OnPlayerOpenStall)
		self.ListenForEvent(tradeConst.ModName, tradeConst.ClientSystemName, tradeConst.PlayerCloseStallEvent, self, self.OnPlayerCloseStall)
		self.ListenForEvent(tradeConst.ModName, tradeConst.ClientSystemName, tradeConst.PlayerSpotMerchEvent, self, self.OnPlayerSpotMerch)
		self.ListenForEvent(tradeConst.ModName, tradeConst.ClientSystemName, 'SOS', self, self.OnSOS)

		self.ListenForEvent(tradeConst.ModName, tradeConst.ServiceSystemName, tradeConst.StallSaleUpdateEvent, self, self.OnStallSaleUpdate)
		self.ListenForEvent(tradeConst.ModName, tradeConst.ServiceSystemName, tradeConst.PlayerCloseStallEvent, self, self.OnSomeoneCloseStall)

		self.ListenForEvent(tradeConst.ModName, tradeConst.ServiceSystemName, 'PlayerDoughsUpdateEvent', self, self.OnSomeoneUpdateDoughs)

	def Destroy(self):
		self.UnListenForEvent(serverApi.GetEngineNamespace(), serverApi.GetEngineSystemName(), "ServerBlockEntityTickEvent", self, self.OnServerBlockEntityTick)
		self.UnListenForEvent(serverApi.GetEngineNamespace(), serverApi.GetEngineSystemName(), "ServerPlaceBlockEntityEvent", self, self.OnServerPlaceBlockEntity)
		self.UnListenForEvent(serverApi.GetEngineNamespace(), serverApi.GetEngineSystemName(), "ServerEntityTryPlaceBlockEvent", self, self.OnServerEntityTryPlaceBlock)
		self.UnListenForEvent(serverApi.GetEngineNamespace(), serverApi.GetEngineSystemName(), "ServerBlockUseEvent", self, self.OnServerBlockUse)
		self.UnListenForEvent(serverApi.GetEngineNamespace(), serverApi.GetEngineSystemName(), "ServerPlayerTryDestroyBlockEvent", self, self.OnServerPlayerTryDestroyBlock)

		self.UnListenForEvent(tradeConst.ModName, tradeConst.ClientSystemName, tradeConst.QueryPlayerDoughsEvent, self, self.OnQueryPlayerDoughs)
		self.UnListenForEvent(tradeConst.ModName, tradeConst.ClientSystemName, tradeConst.PlayerPurchaseEvent, self, self.OnPlayerPurchase)
		self.UnListenForEvent(tradeConst.ModName, tradeConst.ClientSystemName, tradeConst.MerchOnSaleEvent, self, self.OnMerchOnSale)
		self.UnListenForEvent(tradeConst.ModName, tradeConst.ClientSystemName, tradeConst.PlayerWithdrawMerchEvent, self, self.OnPlayerWithdrawMerch)
		self.UnListenForEvent(tradeConst.ModName, tradeConst.ClientSystemName, tradeConst.PlayerOpenStallEvent, self, self.OnPlayerOpenStall)
		self.UnListenForEvent(tradeConst.ModName, tradeConst.ClientSystemName, tradeConst.PlayerCloseStallEvent, self, self.OnPlayerCloseStall)
		self.UnListenForEvent(tradeConst.ModName, tradeConst.ClientSystemName, tradeConst.PlayerSpotMerchEvent, self, self.OnPlayerSpotMerch)
		self.UnListenForEvent(tradeConst.ModName, tradeConst.ClientSystemName, 'SOS', self, self.OnSOS)

		self.UnListenForEvent(tradeConst.ModName, tradeConst.ServiceSystemName, tradeConst.StallSaleUpdateEvent, self, self.OnStallSaleUpdate)
		self.UnListenForEvent(tradeConst.ModName, tradeConst.ServiceSystemName, tradeConst.PlayerCloseStallEvent, self, self.OnSomeoneCloseStall)

		self.UnListenForEvent(tradeConst.ModName, tradeConst.ServiceSystemName, 'PlayerDoughsUpdateEvent', self, self.OnSomeoneUpdateDoughs)

		mysqlPool.Finish()

	def Update(self):
		if self.mX:
			self.RequestToService(
				tradeConst.ModName,
				'BatchCheckEvent',
				{'samples': list(self.mX)},
				lambda rtn, data: rtn and self.SaleServerRender(None, 'BatchCheckEvent', data)
			)
			self.mX.clear()
		try:
			flag = False
			comp = self.CreateComponent(serverApi.GetLevelId(), "Minecraft", 'extraData')
			b = comp.GetExtraData("expired_stall_blocks")
			if not isinstance(b, dict):
				return
			for k, v in b.iteritems():
				dimension = int(k)
				if dimension in self.mD2P:
					blockInfoComp = self.CreateComponent(self.mD2P[dimension], "Minecraft", "blockInfo")
					if not blockInfoComp:
						continue
					chunkSourceComp = self.CreateComponent(self.mD2P[dimension], "Minecraft", "chunkSource")
					if not chunkSourceComp:
						continue
					try:
						for i in xrange(len(v) - 1, -1, -1):
							p = tuple(json.loads(v[i]))
							if chunkSourceComp.CheckChunkState(dimension, p):
								blockDict = blockInfoComp.GetBlockNew(p)
								if blockDict and blockDict['name'] == 'netease_trade:stall':
									if blockInfoComp.SetBlockNew(p, {'name': 'minecraft:air', 'aux': 0}):
										flag = True
										del v[i]
								else:
									flag = True
									del v[i]
					except:
						continue
			if flag:
				comp.SetExtraData("expired_stall_blocks", b)
			e = comp.GetExtraData("expired_floating_texts")
			if not isinstance(b, dict):
				return
			if e:
				e.pop(404, -1)
				for entityId in e:
					self.DestroyEntity(entityId)
				e.clear()
				comp.SetExtraData("expired_floating_texts", e)
		except:
			pass

	def OnServerPlayerTryDestroyBlock(self, data):
		if data['fullName'] == 'netease_trade:stall':
			flag = True
			playerId = data['playerId']
			uid = netgameApi.GetPlayerUid(playerId)
			if uid:
				comp = self.CreateComponent(playerId, "Minecraft", "dimension")
				if comp:
					dimension = comp.GetPlayerDimensionId()
					p = (data['x'], data['y'], data['z'])
					comp = self.CreateComponent(serverApi.GetLevelId(), "Minecraft", "blockEntityData")
					if comp:
						blockEntityData = comp.GetBlockEntityData(dimension, p)
						s = str(uid)
						if blockEntityData and blockEntityData['owner'] == s:
							posComp = serverApi.GetEngineCompFactory().CreatePos(str(blockEntityData['label']))
							if posComp and posComp.GetPos():
								# 改的需求
								# 摆摊后不能破坏该摆摊方块
								pass
							else:
								comp = self.CreateComponent(serverApi.GetLevelId(), "Minecraft", 'extraData')
								m = comp.GetExtraData("stall_blocks")
								if not isinstance(m, dict):
									m = {}
								if s in m:
									e = comp.GetExtraData("expired_floating_texts")
									if not isinstance(e, dict):
										e = {}
									label = blockEntityData['label']
									if label:
										e[label] = 1
										comp.SetExtraData("expired_floating_texts", e)
									m.pop(s, -1)
									comp.SetExtraData("stall_blocks", m)
								flag = False
			if flag:
				data['cancel'] = True

	def OnServerBlockEntityTick(self, data):
		if data['blockName'] == 'netease_trade:stall':
			p = (data['posX'], data['posY'], data['posZ'])
			comp = self.CreateComponent(serverApi.GetLevelId(), "Minecraft", "blockEntityData")
			if comp:
				blockEntityData = comp.GetBlockEntityData(data['dimension'], p)
				if blockEntityData and blockEntityData['count']:
					count = blockEntityData['count']
					if count:
						count += 1
						if not count % 44:
							count = 1
							self.mX.add(int(blockEntityData['owner']))
						blockEntityData['count'] = count

	def OnServerPlaceBlockEntity(self, data):
		if data['blockName'] == 'netease_trade:stall':
			p = (data['posX'], data['posY'], data['posZ'])
			if p in self.mStallBlocks:
				comp = self.CreateComponent(serverApi.GetLevelId(), "Minecraft", "blockEntityData")
				if comp:
					blockEntityData = comp.GetBlockEntityData(data['dimension'], p)
					if blockEntityData:
						blockEntityData['owner'] = self.mStallBlocks[p]
						blockEntityData['stamp'] = int(time.time())
						blockEntityData['label'] = 404
						blockEntityData['count'] = 1
						self.mStallBlocks.pop(p, -1)

	def OnServerBlockUse(self, data):
		if data['blockName'] == 'netease_trade:stall':
			playerId = data['playerId']
			now = time.time()
			if now - self.mPlayerId2InteractCD.get(playerId, 0.0) < 1.6:
				return
			else:
				self.mPlayerId2InteractCD[playerId] = now
			uid = netgameApi.GetPlayerUid(playerId)
			if not uid:
				print 'can not get uid by playerId: %s' % playerId
				return
			comp = self.CreateComponent(playerId, "Minecraft", "dimension")
			if not comp:
				return
			dimension = comp.GetPlayerDimensionId()
			p = (data['x'], data['y'], data['z'])
			comp = self.CreateComponent(serverApi.GetLevelId(), "Minecraft", "blockEntityData")
			if comp:
				blockEntityData = comp.GetBlockEntityData(dimension, p)
				if blockEntityData:
					owner = blockEntityData['owner']
					if not owner:
						blockEntityData['owner'] = owner = self.mStallBlocks.get(p, str(uid))
						self.mStallBlocks.pop(p, -1)
						blockEntityData['stamp'] = int(time.time())
						blockEntityData['label'] = 404
						blockEntityData['count'] = 1
					self.DisplayStall(uid, int(owner))

	def OnServerEntityTryPlaceBlock(self, data):
		uid = netgameApi.GetPlayerUid(data['entityId'])
		if not uid:
			print 'can not get uid by playerId: %s' % data['entityId']
			return
		comp = self.CreateComponent(data['entityId'], "Minecraft", "blockInfo")
		blockDict = comp.GetBlockNew((data['x'], data['y'] + 1, data['z']))
		if blockDict and blockDict['name'] == 'netease_trade:stall':
			data['cancel'] = True
			return
		blockDict = comp.GetBlockNew((data['x'], data['y'] - 1, data['z']))
		if blockDict and blockDict['name'] == 'netease_trade:stall':
			data['cancel'] = True
			return
		if data['fullName'] == 'netease_trade:stall':
			serverType = commonNetgameApi.GetServerType()
			if not self.mStallRules["openStall"]:
				data['cancel'] = True
				comp = self.CreateComponent(data['entityId'], 'Minecraft', 'command')
				alertSystem = serverApi.GetSystem("neteaseAlert", "neteaseAlertDev")
				if alertSystem:
					alertSystem.Alert(data['entityId'], '§c摊位方块只能放置于规定的摆摊区域。', 2, 0.5, 0.8)
				else:
					comp.SetCommand('tellraw @s {"rawtext": [{"text": "%s"}]}' % '§c摊位方块只能放置于规定的摆摊区域', data['entityId'])
				return
			p = (data['x'], data['y'], data['z'])
			if self.mStallRules["limitStallArea"]:
				valid = False
				for pair in self.mStallRules['validStallArea']:
					if pair['min'][0] < p[0] < pair['max'][0] and pair['min'][1] < p[1] < pair['max'][1] and pair['min'][-1] < p[-1] < pair['max'][-1]:
						valid = True
						break
				if not valid:
					data['cancel'] = True
					comp = self.CreateComponent(data['entityId'], 'Minecraft', 'command')
					alertSystem = serverApi.GetSystem("neteaseAlert", "neteaseAlertDev")
					if alertSystem:
						alertSystem.Alert(data['entityId'], '§c摊位方块只能放置于规定的摆摊区域。', 2, 0.5, 0.8)
					else:
						comp.SetCommand('tellraw @s {"rawtext": [{"text": "%s"}]}' % '§c摊位方块只能放置于规定的摆摊区域', data['entityId'])
					return
			comp = self.CreateComponent(serverApi.GetLevelId(), "Minecraft", 'extraData')
			m = comp.GetExtraData("stall_blocks")
			if not isinstance(m, dict):
				m = {}
			s = str(uid)
			if s in m:
				data['cancel'] = True
				comp = self.CreateComponent(data['entityId'], 'Minecraft', 'command')
				alertSystem = serverApi.GetSystem("neteaseAlert", "neteaseAlertDev")
				if alertSystem:
					alertSystem.Alert(data['entityId'], '§c您已放置摊位方块在{}处，无法放置多个摊位方块。'.format('({})'.format(m[s][0][1:-1])), 2, 0.5, 0.8)
				else:
					comp.SetCommand('tellraw @s {"rawtext": [{"text": "%s"}]}' % '§c您已放置摊位方块在{}处，无法放置多个摊位方块'.format('({})'.format(m[s][0][1:-1])), data['entityId'])
				return
			try:
				m[s] = [json.dumps(p), str(self.CreateComponent(data['entityId'], "Minecraft", "dimension").GetPlayerDimensionId())]
			except:
				data['cancel'] = True
				comp = self.CreateComponent(data['entityId'], 'Minecraft', 'command')
				alertSystem = serverApi.GetSystem("neteaseAlert", "neteaseAlertDev")
				if alertSystem:
					alertSystem.Alert(data['entityId'], '§未知错误。', 2, 0.5, 0.8)
				else:
					comp.SetCommand('tellraw @s {"rawtext": [{"text": "%s"}]}' % '§未知错误', data['entityId'])
				return
			comp.SetExtraData("stall_blocks", m)
			self.mStallBlocks[p] = s

	def InitMysqlPool(self):
		try:
			mysqlPool.InitDB(44)
		except:
			logout.error("Exception in InitMysqlPool")
			return False
		return True

	def InitTradeCfg(self):
		cfg = commonNetgameApi.GetModJsonConfig("neteaseTradeScript")
		if not cfg:
			logout.error("nothing in InitTradeCfg")
			return False
		typeDefineConfig = cfg.get("typeDefineConfig", {})
		self.mStallRules = {
			"openStall": False,
			"limitStallArea": False,
			"validStallArea": [],
		}
		self.mStallRules.update(typeDefineConfig.get("default", {}))
		gameType = commonNetgameApi.GetServerType()
		self.mStallRules.update(typeDefineConfig.get(gameType, {}))
		# print "InitTradeCfg gameType={}".format(gameType)
		# print self.mStallRules
		return True

	def TradeServerRender(self, playerId, eventName, respData):
		print playerId, eventName, respData
		if respData['code'] == tradeConst.RespCodeSuccess:
			# TODO: 后续再优化
			if eventName in (tradeConst.DisplayGroceryEvent,):
				self.NotifyToClient(playerId, eventName, respData['entity'])
		if eventName == tradeConst.PlayerPurchaseEvent:
			logout.info('玩家 {} 购买商品返回 {}'.format(playerId, respData))  # TODO
			print respData
			comp = self.CreateComponent(playerId, 'Minecraft', 'command')
			if respData['code'] == tradeConst.RespCodeSuccess:
				qty = respData['entity']['qty']

				# 发货
				free = self.Preview(playerId, comp, qty=qty)
				if not free:
					# 需要回滚
					logout.warning('玩家 {} 购买商品回滚'.format(playerId))
					uid = netgameApi.GetPlayerUid(playerId)
					if not uid:
						print 'can not get uid by playerId: %s' % playerId
						return
					self.RequestToService(
						tradeConst.ModName,
						'TradeRollback',
						{'uid': uid, 'groceryId': respData['entity']['groceryId'], 'goodId': respData['entity']['goodId'], 'qty': qty},
						lambda rtn, data: logout.info('玩家 {} 购买商品回滚返回 {}'.format(playerId, (rtn, data)))
					)
					return
				logout.info('准备发放商品至玩家 {} 背包的 {} 空格中'.format(playerId, free))
				item = respData['entity']['item'].copy().popitem()
				auxValue = item[0].split(':')[-1]
				itemDict = {
					'itemName': item[0][:-1 - len(auxValue)],
					'count': item[-1],
					'enchantData': [],
					'auxValue': int(auxValue or 0),
					'extraId': ''
				}
				for _ in xrange(qty):
					self.CreateComponent(playerId, 'Minecraft', 'item').SpawnItemToPlayerInv(itemDict, playerId, free.pop())
				self.NotifyToClient(playerId, eventName, respData['entity'])
				logout.info('玩家 {} 购买商品发货成功'.format(playerId))  # TODO
				alertSystem = serverApi.GetSystem("neteaseAlert", "neteaseAlertDev")
				if alertSystem:
					alertSystem.Alert(playerId, '§a购买成功。', 2, 0.5, 0.8)
				else:
					comp.SetCommand('tellraw @s {"rawtext": [{"text": "%s"}]}' % '§a购买成功', playerId)
			else:
				alertSystem = serverApi.GetSystem("neteaseAlert", "neteaseAlertDev")
				if alertSystem:
					alertSystem.Alert(playerId, '§c{}，购买失败。'.format(respData['message']), 2, 0.5, 0.8)
				else:
					comp.SetCommand('tellraw @s {"rawtext": [{"text": "%s"}]}' % '§c{}'.format(respData['message']), playerId)
					comp.SetCommand('tellraw @s {"rawtext": [{"text": "%s"}]}' % '§c购买失败', playerId)
		if eventName == tradeConst.UpdatePlayerDoughsEvent:
			comp = self.CreateComponent(playerId, 'Minecraft', 'command')
			if respData['code'] == tradeConst.RespCodeSuccess:
				self.NotifyToClient(playerId, eventName, {'doughs': respData['entity']})
				# comp.SetCommand('tellraw @s {"rawtext": [{"text": "%s"}]}' % '§a操作成功，返回信息为`{}`'.format(respData['entity']), playerId)
				alertSystem = serverApi.GetSystem("neteaseAlert", "neteaseAlertDev")
				if alertSystem:
					alertSystem.Alert(playerId, '§a已更新您的货币。', 2, 0.5, 0.8)
				else:
					comp.SetCommand('tellraw @s {"rawtext": [{"text": "%s"}]}' % '§a已更新您的货币', playerId)
				pass
			else:
				# comp.SetCommand('tellraw @s {"rawtext": [{"text": "%s"}]}' % '§c操作失败，错误信息为`{}`'.format(respData['message']), playerId)
				pass

	def Find(self, conn, operation, parameters):
		try:
			c = conn.cursor()
			c.execute(operation, parameters)
			return c.fetchall()
		except Exception as e:
			conn.rollback()
			logout.error('Exception in Find e: {} operation: {} parameters: {}'.format(e, operation, parameters))
			return False

	def ManipulateOneMerch(self, conn, operation, parameters):
		try:
			c = conn.cursor()
			c.execute(operation, parameters)
			rowcount = c.rowcount
			conn.commit()
		except Exception as e:
			conn.rollback()
			logout.error('Exception in ManipulateOneMerch e: {} operation: {} parameters: {}'.format(e, operation, parameters))
			return False
		return rowcount

	def SaleServerRender(self, playerId, eventName, respData, **kwargs):
		print playerId, eventName, respData
		if eventName == 'BatchCheckEvent':
			outcasts = []
			now = time.time()
			comp = self.CreateComponent(serverApi.GetLevelId(), "Minecraft", 'extraData')
			m = comp.GetExtraData("stall_blocks")
			if not (m and isinstance(m, dict)):
				return
			comp = self.CreateComponent(serverApi.GetLevelId(), "Minecraft", "blockEntityData")
			if not comp:
				return
			for uid, label in respData.iteritems():
				s = str(uid)
				if s in m:
					dimension = int(m[s][-1])
					p = tuple(json.loads(m[s][0]))
					blockEntityData = comp.GetBlockEntityData(dimension, p)
					if blockEntityData:
						if label == -1:
							stamp = blockEntityData['stamp']
							if not stamp or now - stamp > 1800:
								outcasts.append(uid)
						else:
							pre = blockEntityData['label']
							if pre == 404:
								entityId = self.CreateEngineEntityByTypeStr('netease_trade:floating_text', (p[0] + 0.5, p[1] + 1, p[2] + 0.5), (0.0, 0.0), dimension)
								if entityId is None:
									print '43964396439643964396439643964396439643964396'
								else:
									blockEntityData['label'] = entityId
									nameComp = self.CreateComponent(entityId, "Minecraft", "name")
									if nameComp:
										if not nameComp.SetName(label):
											print '22002200220022002200220022002200220022002200'
			if outcasts:
				self.OnSomeoneCloseStall({'outcasts': outcasts})
		elif eventName == tradeConst.MerchOnSaleEvent:
			comp = self.CreateComponent(playerId, 'Minecraft', 'command')
			if respData['code'] == tradeConst.RespCodeSuccess:
				success = False
				try:
					slot = kwargs['slot']
					itemComp = self.CreateComponent(playerId, 'Minecraft', 'item')
					itemDict = itemComp.GetPlayerItem(serverApi.GetMinecraftEnum().ItemPosType.INVENTORY, slot)
					cur = json.dumps(itemDict)
					if respData['entity']['stuff'] != cur:
						logout.warning('uid: {} playerId: {} inconsistent slot: {} cur: {} pre: {}'.format(respData['entity']['uid'], playerId, slot, cur, respData['entity']['stuff']))
						alertSystem = serverApi.GetSystem("neteaseAlert", "neteaseAlertDev")
						if alertSystem:
							alertSystem.Alert(playerId, '§e背包数据发生变化，请重新选择', 2, 0.5, 0.8)
						else:
							comp.SetCommand('tellraw @s {"rawtext": [{"text": "%s"}]}' % '§c背包数据发生变化', playerId)
							comp.SetCommand('tellraw @s {"rawtext": [{"text": "%s"}]}' % '§e请重新选择', playerId)
						serverApi.GetSystem(tradeConst.ModName, "bag").sync(respData['entity']['uid'])
						raise RuntimeError('inconsistent data')
					else:
						itemComp.SetInvItemNum(slot, itemDict['count'] - respData['entity']['qty'])
						# 背包发生变化
						serverApi.GetSystem(tradeConst.ModName, "bag").sync(respData['entity']['uid'])
						mysqlPool.AsyncExecuteFunctionWithOrderKey(
							self.ManipulateOneMerch,
							'PLAYER_%s_U' % respData['entity']['uid'],
							lambda *args: 0,
							'UPDATE {} SET available = 1 WHERE _id=%s'.format(tradeConst.TableTradeSaleMerch),
							(respData['entity']['_id'],)
						)
						success = True
				except Exception as e:
					logout.warning('Exception in SaleServerRender e: {}'.format(e))
					mysqlPool.AsyncExecuteFunctionWithOrderKey(
						self.ManipulateOneMerch,
						'PLAYER_%s_D' % respData['entity']['uid'],
						lambda *args: 0,
						'DELETE FROM {} WHERE _id=%s AND uid=%s'.format(tradeConst.TableTradeSaleMerch),
						(respData['entity']['_id'], respData['entity']['uid'])
					)
				if success:
					# TODO: 可以发事件出来
					alertSystem = serverApi.GetSystem("neteaseAlert", "neteaseAlertDev")
					if alertSystem:
						alertSystem.Alert(playerId, '§a商品上架成功。', 2, 0.5, 0.8)
					else:
						comp.SetCommand('tellraw @s {"rawtext": [{"text": "%s"}]}' % '§a商品上架成功', playerId)
					# self.NotifyToClient(playerId, eventName, {'upgradable': 1, 'msg': 'a商品上架成功'})
					merch = {
						'_id': respData['entity']['_id'],
						'currency': respData['entity']['currency'],
						'unit': respData['entity']['unit'],
						'qty': respData['entity']['qty'],
						'init': respData['entity']['init'],
						'stuff': respData['entity']['stuff'],
					}
					# self.NotifyToClient(playerId, eventName, {'upgradable': 1, 'msg': 'a商品上架成功', 'merch': merch})
					self.NotifyToClient(playerId, eventName, {'reset': 1, 'msg': 'a商品上架成功', 'merch': merch})
				else:
					# comp.SetCommand('tellraw @s {"rawtext": [{"text": "%s"}]}' % '§c商品上架出现异常', playerId)
					self.NotifyToClient(playerId, eventName, {'msg': '4商品上架出现异常', 'reset': 1})
			else:
				self.NotifyToClient(playerId, eventName, {'msg': 'c商品上架失败'})
				if respData['message']:
					alertSystem = serverApi.GetSystem("neteaseAlert", "neteaseAlertDev")
					if alertSystem:
						alertSystem.Alert(playerId, '§c{}。'.format(respData['message']), 2, 0.5, 0.8)
					else:
						comp.SetCommand('tellraw @s {"rawtext": [{"text": "%s"}]}' % '§c{}'.format(respData['message']), playerId)
		elif eventName == tradeConst.DisplayStallEvent:
			comp = self.CreateComponent(playerId, 'Minecraft', 'command')
			if respData['code'] == tradeConst.RespCodeSuccess:
				if respData['entity']['owner'] == respData['entity']['uid']:
					try:
						comp = self.CreateComponent(playerId, 'Minecraft', 'item')
						inv = serverApi.GetMinecraftEnum().ItemPosType.INVENTORY
						respData['entity']['inventory'] = [json.dumps(comp.GetPlayerItem(inv, i)) for i in xrange(36)]
						self.NotifyToClient(playerId, eventName, respData['entity'])
					except:
						logout.error("Exception in DisplayStallEvent")
				else:
					self.NotifyToClient(playerId, eventName, respData['entity'])
			elif respData['message']:
				alertSystem = serverApi.GetSystem("neteaseAlert", "neteaseAlertDev")
				if alertSystem:
					alertSystem.Alert(playerId, '§c{}。'.format(respData['message']), 2, 0.5, 0.8)
				else:
					comp.SetCommand('tellraw @s {"rawtext": [{"text": "%s"}]}' % '§c{}'.format(respData['message']), playerId)
		elif eventName == tradeConst.PlayerOpenStallEvent:
			if respData['code'] == tradeConst.RespCodeSuccess:
				self.NotifyToClient(playerId, eventName, respData['entity'])
			elif respData['message']:
				comp = self.CreateComponent(playerId, 'Minecraft', 'command')
				alertSystem = serverApi.GetSystem("neteaseAlert", "neteaseAlertDev")
				if alertSystem:
					alertSystem.Alert(playerId, '§c{}。'.format(respData['message']), 2, 0.5, 0.8)
				else:
					comp.SetCommand('tellraw @s {"rawtext": [{"text": "%s"}]}' % '§c{}'.format(respData['message']), playerId)
				self.NotifyToClient(playerId, eventName, {})
		elif eventName == tradeConst.PlayerCloseStallEvent:
			if respData['code'] == tradeConst.RespCodeSuccess:
				self.NotifyToClient(playerId, eventName, {})
			elif respData['message']:
				comp = self.CreateComponent(playerId, 'Minecraft', 'command')
				alertSystem = serverApi.GetSystem("neteaseAlert", "neteaseAlertDev")
				if alertSystem:
					alertSystem.Alert(playerId, '§c{}。'.format(respData['message']), 2, 0.5, 0.8)
				else:
					comp.SetCommand('tellraw @s {"rawtext": [{"text": "%s"}]}' % '§c{}'.format(respData['message']), playerId)
		elif eventName == tradeConst.PlayerSpotMerchEvent:
			comp = self.CreateComponent(playerId, 'Minecraft', 'command')
			if respData['code'] == tradeConst.RespCodeSuccess:
				logout.info('玩家 uid: {} 购买摊位商品返回 {}'.format(respData['entity']['uid'], respData))
				# 发货
				try:
					free = self.Preview(playerId, comp)
				except:
					free = None
				if not free:
					# 需要回滚
					logout.warning('玩家 uid: {} 购买摊位商品 _id: {} 回滚'.format(respData['entity']['uid'], respData['entity']['_id']))
					mysqlPool.AsyncExecuteFunctionWithOrderKey(
						self.ManipulateOneMerch,
						'PLAYER_%s_U' % respData['entity']['uid'],
						lambda rowcount: rowcount or logout.error('玩家 uid: {} 购买摊位商品 _id: {} 回滚库存失败'.format(respData['entity']['uid'], respData['entity']['_id'])),
						'UPDATE {} t SET t.qty = t.qty + %s WHERE t._id=%s'.format(tradeConst.TableTradeSaleMerch),
						(respData['entity']['qty'], respData['entity']['_id'])
					)
					if respData['entity']['subtotal']:
						self.RequestToService(
							tradeConst.ModName,
							'TradeSaleRollback',
							{
								'uid': respData['entity']['uid'],
								'currency': respData['entity']['currency'],
								'subtotal': respData['entity']['subtotal'],
							},
							lambda rtn, data: logout.info('玩家 uid: {} 购买摊位商品 _id: {} 回滚返回 {}'.format(respData['entity']['uid'], respData['entity']['_id'], (rtn, data)))
						)
					return
				logout.info('准备发放摊位商品 _id: {} 至玩家 {} 背包的 {} 空格中'.format(respData['entity']['_id'], playerId, free))
				itemDict = json.loads(respData['entity']['stuff'])
				itemDict['count'] = respData['entity']['qty']
				self.CreateComponent(playerId, 'Minecraft', 'item').SpawnItemToPlayerInv(itemDict, playerId, free.pop())
				# 背包发生变化
				serverApi.GetSystem(tradeConst.ModName, "bag").sync(respData['entity']['uid'])
				self.NotifyToClient(playerId, eventName, {'_id': respData['entity']['_id'], 'qty': respData['entity']['qty']})
				logout.info('玩家 uid: {} 购买摊位商品 _id: {} 发货成功'.format(respData['entity']['uid'], respData['entity']['_id']))  # TODO
				alertSystem = serverApi.GetSystem("neteaseAlert", "neteaseAlertDev")
				if alertSystem:
					alertSystem.Alert(playerId, '§a购买成功。', 2, 0.5, 0.8)
				else:
					comp.SetCommand('tellraw @s {"rawtext": [{"text": "%s"}]}' % '§a购买成功', playerId)
				dealData = {
					'uid': respData['entity']['uid'],
					'_id': respData['entity']['_id'],
					'owner': respData['entity']['owner'],
					'currency': respData['entity']['currency'],
					'unit': respData['entity']['unit'],
					'qty': respData['entity']['qty'],
					'subtotal': respData['entity']['subtotal'],
					'stuff': respData['entity']['stuff'],
				}
				self.RequestToService(
					tradeConst.ModName,
					tradeConst.StallSaleUpdateEvent,
					dealData,
					lambda rtn, data: rtn and data['code'] == tradeConst.RespCodeSuccess and 1 or logout.error('玩家 uid: {} 购买摊位商品 _id: {} 生成交易记录失败 dealData: {}'.format(respData['entity']['uid'], respData['entity']['_id'], dealData))
				)
			else:
				if 'entity' in respData:
					self.NotifyToClient(playerId, eventName, respData['entity'])
				alertSystem = serverApi.GetSystem("neteaseAlert", "neteaseAlertDev")
				if alertSystem:
					alertSystem.Alert(playerId, '§c{}，购买失败。'.format(respData['message']), 2, 0.5, 0.8)
				else:
					comp.SetCommand('tellraw @s {"rawtext": [{"text": "%s"}]}' % '§c{}'.format(respData['message']), playerId)
					comp.SetCommand('tellraw @s {"rawtext": [{"text": "%s"}]}' % '§c购买失败', playerId)

	def OnQueryPlayerDoughs(self, data):
		playerId = data.get("playerId", "-1")
		uid = netgameApi.GetPlayerUid(playerId)
		if not uid:
			print 'can not get uid by playerId: %s' % playerId
			return
		comp = self.CreateComponent(playerId, "Minecraft", "dimension")
		if comp:
			dimension = comp.GetPlayerDimensionId()
			self.mD2P[dimension] = playerId
		self.RequestToService(
			tradeConst.ModName,
			tradeConst.QueryPlayerDoughsEvent,
			{'uid': uid, 'activate': True, 'void': True},
			lambda rtn, data: rtn and self.TradeServerRender(playerId, 996, data)
		)

	def Preview(self, playerId, alert, msg=None, qty=1):
		demand = qty
		free = []
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
				alertSystem.Alert(playerId, '{}。'.format(msg or '§c购买商品需要{}个空格'.format(demand)), 2, 0.5, 0.8)
			else:
				alert.SetCommand('tellraw @s {"rawtext": [{"text": "%s"}]}' % (msg or '§c购买商品需要{}个空格'.format(demand)), playerId)
			return
		return free

	def OnPlayerPurchase(self, data):
		playerId = data.get("playerId", "-1")
		uid = netgameApi.GetPlayerUid(playerId)
		if not uid:
			print 'can not get uid by playerId: %s' % playerId
			return
		groceryId = data.get('groceryId')
		goodId = data.get('goodId')
		forgery = data.get('forgery')
		if forgery:
			self.RequestToService(
				tradeConst.ModName,
				tradeConst.PlayerPurchaseEvent,
				{'uid': uid, 'groceryId': groceryId, 'goodId': goodId, 'qty': 1},
				lambda rtn, data: forgery(playerId, rtn, data),
				4
			)
		else:
			qty = data['qty']
			comp = self.CreateComponent(playerId, 'Minecraft', 'command')
			# comp.SetCommand('tellraw @s {"rawtext": [{"text": "%s"}]}' % '§e购买中，商店标识为`{}`，商品标识为`{}`，请稍候……'.format(groceryId, goodId), playerId)
			alertSystem = serverApi.GetSystem("neteaseAlert", "neteaseAlertDev")
			if alertSystem:
				alertSystem.Alert(playerId, '§e购买中，请稍候……', 2, 0.5, 0.8)
			else:
				comp.SetCommand('tellraw @s {"rawtext": [{"text": "%s"}]}' % '§e购买中，请稍候……', playerId)
			if not groceryId or not goodId:
				alertSystem = serverApi.GetSystem("neteaseAlert", "neteaseAlertDev")
				if alertSystem:
					alertSystem.Alert(playerId, '§c购买失败。', 2, 0.5, 0.8)
				else:
					comp.SetCommand('tellraw @s {"rawtext": [{"text": "%s"}]}' % '§c购买失败', playerId)
				return
			if not self.Preview(playerId, comp, qty=qty):
				# comp.SetCommand('tellraw @s {"rawtext": [{"text": "%s"}]}' % '§c购买失败', playerId)
				return
			self.RequestToService(
				tradeConst.ModName,
				tradeConst.PlayerPurchaseEvent,
				{'uid': uid, 'groceryId': groceryId, 'goodId': goodId, 'qty': qty},
				lambda rtn, data: self.TradeServerRender(playerId, tradeConst.PlayerPurchaseEvent, data) if rtn else (alertSystem.Alert(playerId, '§c购买超时。', 2, 0.5, 0.8) if alertSystem else comp.SetCommand('tellraw @s {"rawtext": [{"text": "%s"}]}' % '§c购买超时', playerId)),
				4
			)

	def FindOneMerchAndDelete(self, _id, uid, playerId, step=0, **kwargs):
		print 'FindOneMerchAndDelete', _id, uid, playerId, step, kwargs
		if not step:
			mysqlPool.AsyncExecuteFunctionWithOrderKey(
				self.Find,
				'PLAYER_%s_S' % uid,
				lambda rows: self.FindOneMerchAndDelete(_id, uid, playerId, 1, rows=rows),
				'SELECT * FROM {} WHERE _id=%s AND available=0'.format(tradeConst.TableTradeSaleMerch),
				(_id,)
			)
		elif step == 1:
			rows = kwargs['rows']
			if rows is None:
				logout.error('unlikely Exception in FindOneMerchAndDelete')
				return
			if not rows:
				logout.error('玩家 uid: {} 下架商品 _id: {} 失败且处于不可见状态'.format(uid, _id))
				return
			merch = rows[0]
			comp = self.CreateComponent(playerId, 'Minecraft', 'command')
			if merch[4] > 0:
				free = self.Preview(playerId, comp, '§c下架商品需要1个空格')
				if not free:
					mysqlPool.AsyncExecuteFunctionWithOrderKey(
						self.ManipulateOneMerch,
						'PLAYER_%s_U' % uid,
						lambda *args: self.NotifyToClient(playerId, tradeConst.PlayerWithdrawMerchEvent, {'_id': _id}),
						'UPDATE {} SET available = 1 WHERE _id=%s'.format(tradeConst.TableTradeSaleMerch),
						(_id,)
					)
					return
				logout.info('准备归还商品至玩家 {} 背包的 {} 空格中'.format(playerId, free))
				itemDict = json.loads(merch[-2])
				itemDict['count'] = merch[4]
				self.CreateComponent(playerId, 'Minecraft', 'item').SpawnItemToPlayerInv(itemDict, playerId, free.pop())
				# 背包发生变化
				serverApi.GetSystem(tradeConst.ModName, "bag").sync(uid)
			mysqlPool.AsyncExecuteFunctionWithOrderKey(
				self.ManipulateOneMerch,
				'PLAYER_%s_D' % uid,
				lambda *args: self.NotifyToClient(playerId, tradeConst.PlayerWithdrawMerchEvent, {'upgradable': 1, '_id': _id}),
				'DELETE FROM {} WHERE _id=%s'.format(tradeConst.TableTradeSaleMerch),
				(_id,)
			)

	def OnPlayerWithdrawMerch(self, data):
		print 'OnPlayerWithdrawMerch', data
		playerId = data.get("playerId", "-1")
		uid = netgameApi.GetPlayerUid(playerId)
		if not uid:
			print 'can not get uid by playerId: %s' % playerId
			return
		_id = data.get("_id")
		comp = self.CreateComponent(playerId, 'Minecraft', 'command')
		alertSystem = serverApi.GetSystem("neteaseAlert", "neteaseAlertDev")
		mysqlPool.AsyncExecuteFunctionWithOrderKey(
			self.ManipulateOneMerch,
			'PLAYER_%s_U' % uid,
			lambda rowcount: self.FindOneMerchAndDelete(_id, uid, playerId) if rowcount else (alertSystem.Alert(playerId, '§c商品下架失败。', 2, 0.5, 0.8) if alertSystem else comp.SetCommand('tellraw @s {"rawtext": [{"text": "%s"}]}' % '§c商品下架失败', playerId)),
			'UPDATE {} SET available = 0 WHERE _id=%s AND uid=%s AND available=1'.format(tradeConst.TableTradeSaleMerch),
			(_id, uid)
		)

	def OnMerchOnSale(self, data):
		print 'OnMerchOnSale', data
		playerId = data.get("playerId", "-1")
		uid = netgameApi.GetPlayerUid(playerId)
		if not uid:
			print 'can not get uid by playerId: %s' % playerId
			return
		slot = data.get('slot')
		qty = data.get('qty')
		stuff = data.get('stuff')
		if not (isinstance(slot, int) and isinstance(qty, int) and isinstance(stuff, str)):
			return
		itemComp = self.CreateComponent(playerId, 'Minecraft', 'item')
		itemDict = itemComp.GetPlayerItem(serverApi.GetMinecraftEnum().ItemPosType.INVENTORY, slot)
		cur = json.dumps(itemDict)
		if itemDict is None or itemDict['count'] < qty or stuff != cur:
			comp = self.CreateComponent(playerId, 'Minecraft', 'command')
			alertSystem = serverApi.GetSystem("neteaseAlert", "neteaseAlertDev")
			if alertSystem:
				alertSystem.Alert(playerId, '§e背包数据发生变化，请重新选择', 2, 0.5, 0.8)
			else:
				comp.SetCommand('tellraw @s {"rawtext": [{"text": "%s"}]}' % '§c背包数据发生变化', playerId)
				comp.SetCommand('tellraw @s {"rawtext": [{"text": "%s"}]}' % '§e请重新选择', playerId)
			serverApi.GetSystem(tradeConst.ModName, "bag").sync(uid)
			self.NotifyToClient(playerId, tradeConst.MerchOnSaleEvent, {'msg': 'c商品上架出现异常', 'reset': 1})
			return
		self.RequestToService(
			tradeConst.ModName,
			tradeConst.MerchOnSaleEvent,
			{
				'uid': uid,
				'currency': data.get('currency'),
				'qty': qty,
				'unit': data.get('unit'),
				'stuff': stuff,
			},
			lambda rtn, data: self.SaleServerRender(playerId, tradeConst.MerchOnSaleEvent, data, slot=slot) if rtn else self.NotifyToClient(playerId, tradeConst.MerchOnSaleEvent, {'msg': '4商品上架超时'})
		)

	def OnPlayerOpenStall(self, data):
		print 'OnPlayerOpenStall', data
		playerId = data.get("playerId", "-1")
		uid = netgameApi.GetPlayerUid(playerId)
		if not uid:
			print 'can not get uid by playerId: %s' % playerId
			return
		self.RequestToService(
			tradeConst.ModName,
			tradeConst.PlayerOpenStallEvent,
			{
				'uid': uid,
				'duration': data.get('duration'),
				'label': data.get('label'),
			},
			lambda rtn, data: rtn and self.SaleServerRender(playerId, tradeConst.PlayerOpenStallEvent, data)
		)

	def OnPlayerCloseStall(self, data):
		print 'OnPlayerCloseStall', data
		playerId = data.get("playerId", "-1")
		uid = netgameApi.GetPlayerUid(playerId)
		if not uid:
			print 'can not get uid by playerId: %s' % playerId
			return
		self.RequestToService(
			tradeConst.ModName,
			tradeConst.PlayerCloseStallEvent,
			{'uid': uid},
			lambda rtn, data: rtn and self.SaleServerRender(playerId, tradeConst.PlayerCloseStallEvent, data)
		)

	def OnPlayerSpotMerch(self, data):
		print 'OnPlayerSpotMerch', data
		playerId = data.get("playerId", "-1")
		uid = netgameApi.GetPlayerUid(playerId)
		if not uid:
			print 'can not get uid by playerId: %s' % playerId
			return
		comp = self.CreateComponent(playerId, 'Minecraft', 'command')
		if not self.Preview(playerId, comp):
			# comp.SetCommand('tellraw @s {"rawtext": [{"text": "%s"}]}' % '§c购买失败', playerId)
			return
		alertSystem = serverApi.GetSystem("neteaseAlert", "neteaseAlertDev")
		if alertSystem:
			alertSystem.Alert(playerId, '§e购买中，请稍候……', 2, 0.5, 0.8)
		else:
			comp.SetCommand('tellraw @s {"rawtext": [{"text": "%s"}]}' % '§e购买中，请稍候……', playerId)
		# gg = self.CreateComponent(playerId, "Minecraft", "game")
		# gg.SetOnePopupNotice(playerId, '§e购买中，请稍候……', '')
		self.RequestToService(
			tradeConst.ModName,
			tradeConst.PlayerSpotMerchEvent,
			{'uid': uid, '_id': data['_id'], 'qty': data['qty']},
			lambda rtn, data: self.SaleServerRender(playerId, tradeConst.PlayerSpotMerchEvent, data) if rtn else (alertSystem.Alert(playerId, '§c购买超时。', 2, 0.5, 0.8) if alertSystem else comp.SetCommand('tellraw @s {"rawtext": [{"text": "%s"}]}' % '§c购买超时', playerId)),
			4
		)

	def OnStallSaleUpdate(self, data):
		print 'OnStallSaleUpdate', data
		playerId = netgameApi.GetPlayerIdByUid(data['uid'])
		if not playerId:
			print 'can not get playerId by uid: %s' % data['uid']
			return
		comp = self.CreateComponent(playerId, 'Minecraft', 'command')
		alertSystem = serverApi.GetSystem("neteaseAlert", "neteaseAlertDev")
		if alertSystem:
			alertSystem.Alert(playerId, '§a商品成功售出，出售记录已更新。', 2, 0.5, 0.8)
		else:
			comp.SetCommand('tellraw @s {"rawtext": [{"text": "%s"}]}' % '§a商品成功售出，出售记录已更新', playerId)
		self.NotifyToClient(playerId, tradeConst.StallSaleUpdateEvent, {'deal': data['deal']})

	def OnSomeoneCloseStall(self, data):
		print 'OnSomeoneCloseStall', data
		flag = False
		comp = self.CreateComponent(serverApi.GetLevelId(), "Minecraft", 'extraData')
		m = comp.GetExtraData("stall_blocks")
		b = comp.GetExtraData("expired_stall_blocks")
		e = comp.GetExtraData("expired_floating_texts")
		if not isinstance(m, dict):
			m = {}
		if not isinstance(b, dict):
			b = {}
		if not isinstance(e, dict):
			e = {}
		if not m:
			return
		blockEntityDataComp = self.CreateComponent(serverApi.GetLevelId(), "Minecraft", "blockEntityData")
		for uid in data['outcasts']:
			s = str(uid)
			if s in m:
				if blockEntityDataComp:
					dimension = int(m[s][-1])
					p = tuple(json.loads(m[s][0]))
					blockEntityData = blockEntityDataComp.GetBlockEntityData(dimension, p)
					if blockEntityData:
						label = blockEntityData['label']
						if label:
							e[label] = 1
				b.setdefault(m[s][1], []).append(m[s][0])
				m.pop(s, -1)
				flag = True
		if flag:
			comp.SetExtraData("stall_blocks", m)
			comp.SetExtraData("expired_stall_blocks", b)
			comp.SetExtraData("expired_floating_texts", e)

	def OnSomeoneUpdateDoughs(self, data):
		self.BroadcastEvent('PlayerDoughsUpdateEvent', data)

	def OnSOS(self, data):
		print 'OnSOS', data
		playerId = data.get("playerId", "-1")
		uid = netgameApi.GetPlayerUid(playerId)
		if not uid:
			print 'can not get uid by playerId: %s' % playerId
			return
		serverApi.GetSystem(tradeConst.ModName, "bag").sos(uid, data.get('f'), data.get('t'))

	def DisplayStall(self, uid, owner):
		print 'DisplayStall', uid, owner
		playerId = netgameApi.GetPlayerIdByUid(uid)
		if not playerId:
			print 'can not get playerId by uid: %s' % uid
			return
		comp = self.CreateComponent(playerId, "Minecraft", "name")
		name = comp.GetName()
		self.RequestToService(
			tradeConst.ModName,
			tradeConst.DisplayStallEvent,
			{'uid': uid, 'name': name, 'owner': owner},
			lambda rtn, data: rtn and self.SaleServerRender(playerId, tradeConst.DisplayStallEvent, data),
			4
		)

	def CloseStall(self, uid, cb):
		print 'CloseStall', uid
		playerId = netgameApi.GetPlayerIdByUid(uid)
		if playerId:
			self.RequestToService(
				tradeConst.ModName,
				tradeConst.PlayerCloseStallEvent,
				{'uid': uid},
				lambda rtn, data: rtn and self.SaleServerRender(playerId, tradeConst.PlayerCloseStallEvent, data) or cb(rtn, data)
			)
		else:
			self.RequestToService(
				tradeConst.ModName,
				tradeConst.PlayerCloseStallEvent,
				{'uid': uid},
				cb
			)

	def OpenGrocery(self, uid, groceryId):
		"""
		使一个玩家打开某种商店的界面
		"""
		print 'OpenGrocery', uid, groceryId
		playerId = netgameApi.GetPlayerIdByUid(uid)
		if not playerId:
			print 'can not get playerId by uid: %s' % uid
			return
		self.RequestToService(
			tradeConst.ModName,
			tradeConst.DisplayGroceryEvent,
			{'uid': uid, 'groceryId': groceryId},
			lambda rtn, data: rtn and self.TradeServerRender(playerId, tradeConst.DisplayGroceryEvent, data)
		)

	def UpdatePlayerDoughs(self, uid, mod):
		"""
		更改一个玩家持有的货币
		"""
		print 'UpdatePlayerDoughs', uid, mod
		playerId = netgameApi.GetPlayerIdByUid(uid)
		if not playerId:
			print 'can not get playerId by uid: %s' % uid
			return
		if not mod or not isinstance(mod, dict):
			print 'invalid arg mod: {}'.format(mod)
			return
		comp = self.CreateComponent(playerId, 'Minecraft', 'command')
		alertSystem = serverApi.GetSystem("neteaseAlert", "neteaseAlertDev")
		self.RequestToService(
			tradeConst.ModName,
			tradeConst.UpdatePlayerDoughsEvent,
			{'uid': uid, 'mod': mod},
			lambda rtn, data: self.TradeServerRender(playerId, tradeConst.UpdatePlayerDoughsEvent, data) if rtn else (alertSystem.Alert(playerId, '§c操作超时。', 2, 0.5, 0.8) if alertSystem else comp.SetCommand('tellraw @s {"rawtext": [{"text": "%s"}]}' % '§c操作超时', playerId)),
			4
		)

	def QueryPlayerDoughs(self, uid, cb):
		self.RequestToService(
			tradeConst.ModName,
			tradeConst.QueryPlayerDoughsEvent,
			{'uid': uid},
			cb
		)

	def CountStalls(self, cb):
		self.RequestToService(
			tradeConst.ModName,
			'CountStallsEvent',
			{},
			cb
		)
