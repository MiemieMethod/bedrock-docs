# -*- coding: utf-8 -*-

import json
import lobbyGame.netgameApi as netgameApi
import apolloCommon.redisPool as redisPool
import logout
import neteaseJewelScript.jewelConst as jewelConst
import server.extraServerApi as serverApi

ServerSystem = serverApi.GetServerSystemCls()


def post_json_loads(p_object):
	if isinstance(p_object, dict):
		return {post_json_loads(key): post_json_loads(value) for key, value in p_object.iteritems()}
	elif isinstance(p_object, list):
		return [post_json_loads(item) for item in p_object]
	elif isinstance(p_object, unicode):
		return p_object.encode('utf-8')
	else:
		return p_object


json_loads = lambda s, encoding=None, cls=None, object_hook=None, parse_float=None, parse_int=None, parse_constant=None, object_pairs_hook=None, **kwargs: post_json_loads(json.loads(s, encoding, cls, object_hook, parse_float, parse_int, parse_constant, object_pairs_hook, **kwargs))


class JewelServerSystem(ServerSystem):
	def __init__(self, namespace, systemName):
		ServerSystem.__init__(self, namespace, systemName)
		if not self.InitRedisPool():
			return
		if not self.InitJewelCfg():
			return

		self.ListenForEvent(jewelConst.ModName, jewelConst.ClientSystemName, jewelConst.PlayerOfferArmEvent, self, self.OnPlayerOfferArm)
		self.ListenForEvent(jewelConst.ModName, jewelConst.ClientSystemName, jewelConst.PlayerClaimArmEvent, self, self.OnPlayerClaimArm)
		self.ListenForEvent(jewelConst.ModName, jewelConst.ClientSystemName, jewelConst.PlayerOfferGemEvent, self, self.OnPlayerOfferGem)
		self.ListenForEvent(jewelConst.ModName, jewelConst.ClientSystemName, jewelConst.PlayerClaimGemEvent, self, self.OnPlayerClaimGem)
		self.ListenForEvent(jewelConst.ModName, jewelConst.ClientSystemName, jewelConst.PlayerEnterEvent, self, self.OnPlayerEnter)
		self.ListenForEvent(jewelConst.ModName, jewelConst.ClientSystemName, 'SOS', self, self.OnSOS)

	def InitRedisPool(self):
		try:
			redisPool.InitDB(20)
		except:
			logout.error("Exception in InitRedisPool")
			return False
		return True

	def InitJewelCfg(self):
		import apolloCommon.commonNetgameApi as commonNetgameApi
		cfg = commonNetgameApi.GetModJsonConfig("neteaseJewelScript")
		if not cfg:
			logout.error("nothing in InitJewelCfg")
			return False
		self.mArms = cfg['Arms']
		for v in self.mArms.itervalues():
			if not isinstance(v, int) or v not in xrange(1, 4):
				return False
		self.mGems = cfg['Gems']
		return True
	# ----------------------------------------------------------------------------------------
	# rawer
	# 代码设置宝石类型
	def RegisterGemType(self, name):
		self.mGems[name] = {}
		return True

	# 代码设置装备插槽
	def RegisterEquipSlot(self, name, slot):
		self.mArms[name] = slot
		return True

	def OutputJewelCfg(self):
		for name, slot in self.mArms.iteritems():
			print "equip name={} slot={}".format(name, slot)
		for name in self.mGems.iterkeys():
			print "{} is gem".format(name)
	# ----------------------------------------------------------------------------------------

	def Destroy(self):
		self.UnListenForEvent(jewelConst.ModName, jewelConst.ClientSystemName, jewelConst.PlayerOfferArmEvent, self, self.OnPlayerOfferArm)
		self.UnListenForEvent(jewelConst.ModName, jewelConst.ClientSystemName, jewelConst.PlayerClaimArmEvent, self, self.OnPlayerClaimArm)
		self.UnListenForEvent(jewelConst.ModName, jewelConst.ClientSystemName, jewelConst.PlayerOfferGemEvent, self, self.OnPlayerOfferGem)
		self.UnListenForEvent(jewelConst.ModName, jewelConst.ClientSystemName, jewelConst.PlayerClaimGemEvent, self, self.OnPlayerClaimGem)
		self.UnListenForEvent(jewelConst.ModName, jewelConst.ClientSystemName, jewelConst.PlayerEnterEvent, self, self.OnPlayerEnter)
		self.UnListenForEvent(jewelConst.ModName, jewelConst.ClientSystemName, 'SOS', self, self.OnSOS)
		redisPool.Finish()

	def Update(self):
		pass

	def Preview(self, data):
		"""
		检查client发送的指定背包格的物品信息是否与server一致，假如不一致，驱动bagSystem的sync逻辑（打包发送背包信息给client）
		"""
		playerId = data.get("playerId", "-1")
		uid = netgameApi.GetPlayerUid(playerId)
		if not uid:
			print 'can not get uid by playerId: %s' % playerId
			return
		slot = data.get('slot')
		stuff = data.get('stuff')
		if not (isinstance(slot, int) and isinstance(stuff, str)):
			return
		itemComp = self.CreateComponent(playerId, 'Minecraft', 'item')
		itemDict = itemComp.GetPlayerItem(serverApi.GetMinecraftEnum().ItemPosType.INVENTORY, slot)
		cur = json.dumps(itemDict)
		if itemDict is None or stuff != cur:
			comp = self.CreateComponent(playerId, 'Minecraft', 'command')
			alertSystem = serverApi.GetSystem("neteaseAlert", "neteaseAlertDev")
			if alertSystem:
				alertSystem.Alert(playerId, '§e背包数据发生变化，请重新选择。', 2, 0.5, 0.8)
			else:
				comp.SetCommand('tellraw @s {"rawtext": [{"text": "%s"}]}' % '§c背包数据发生变化', playerId)
				comp.SetCommand('tellraw @s {"rawtext": [{"text": "%s"}]}' % '§e请重新选择', playerId)
			serverApi.GetSystem(jewelConst.ModName, "bag").sync(uid)
			return
		return uid, slot, cur, itemDict

	def OnPlayerEnter(self, args):
		"""
		client初始化完成后发送的第一条消息，发送宝石与装备（可镶嵌孔数）配置信息给client
		"""
		playerId = args.get("playerId", None)
		if not playerId:
			return
		eventData = {
			"mGems": self.mGems,
			"mArms": self.mArms,
		}
		self.NotifyToClient(playerId, jewelConst.SyncJewelConfigEvent, eventData)

	def PostPlayerClaimGem(self, uid, slot, stuff, p):
		"""
		从宝石镶嵌台上的装备中，取出一个指定镶嵌孔的宝石，并放置到背包中
		"""
		if stuff is None:
			return
		playerId = netgameApi.GetPlayerIdByUid(uid)
		if not playerId:
			return
		itemComp = self.CreateComponent(playerId, 'Minecraft', 'item')
		if not itemComp:
			return
		if itemComp.GetPlayerItem(serverApi.GetMinecraftEnum().ItemPosType.INVENTORY, slot) is not None:
			logout.error('inconsistent data PostPlayerClaimGem uid: {} slot: {} p: {} stuff: {}'.format(uid, slot, p, stuff))
			serverApi.GetSystem(jewelConst.ModName, "bag").sync(uid)
			return
		arm = json_loads(stuff)
		if not arm:
			logout.error('unlikely Exception in PostPlayerClaimGem uid: {} slot: {} p: {} stuff: {}'.format(uid, slot, p, stuff))
			return
		try:
			data = json_loads(arm['extraId'].strip() or '{}')  # type: dict
			gems = data.setdefault('calculator:{}'.format(jewelConst.ModName), [None, None, None])
			if not gems[p]:
				return
			itemComp.SpawnItemToPlayerInv(gems[p], playerId, slot)
			gems[p] = None
			arm['extraId'] = json.dumps(data)
			stuff = json.dumps(arm)
		except Exception as e:
			logout.error('invalid data PostPlayerClaimGem uid: {} slot: {} stuff: {} p: {} e: {}'.format(uid, slot, stuff, p, e))
			import traceback
			traceback.print_exc()
			return
		redisPool.AsyncSet(
			'{}:jewel:arm'.format(uid),
			stuff,
			lambda rtn: self.OpenJewelBoard(uid, stuff=stuff) if rtn else logout.error('lost in PostPlayerClaimGem uid: {} slot: {} p: {} stuff: {} rtn: {}'.format(uid, slot, p, stuff, rtn))
		)

	def OnPlayerClaimGem(self, data):
		"""
		从宝石镶嵌台上的装备中，取出一个指定镶嵌孔的宝石，并放置到背包中，完整的步骤有：
		1、检查背包中的空位置
		2、从redis中获取宝石镶嵌台中的装备以及其镶嵌的宝石信息
		3、取出指定镶嵌孔的宝石放置到背包中
		4、把取出宝石后的装备信息，重新存储到redis中
		5、把新的背包信息和宝石镶嵌台信息同步给client
		"""
		playerId = data.get("playerId", "-1")
		uid = netgameApi.GetPlayerUid(playerId)
		if not uid:
			print 'can not get uid by playerId: %s' % playerId
			return
		itemComp = self.CreateComponent(playerId, 'Minecraft', 'item')
		demand = 1
		free = []
		inv = serverApi.GetMinecraftEnum().ItemPosType.INVENTORY
		for i in xrange(36):
			if itemComp.GetPlayerItem(inv, i) is None:
				free.append(i)
				if len(free) >= demand:
					break
		if len(free) < demand:
			comp = self.CreateComponent(playerId, 'Minecraft', 'command')
			alertSystem = serverApi.GetSystem("neteaseAlert", "neteaseAlertDev")
			if alertSystem:
				alertSystem.Alert(playerId, '§e背包无空位格子。', 2, 0.5, 0.8)
			else:
				comp.SetCommand('tellraw @s {"rawtext": [{"text": "%s"}]}' % '§e背包无空位格子', playerId)
			return
		slot = free[0]
		# slot = data.get('slot')
		# if not (isinstance(slot, int) and -1 < slot < 36):
		# 	return
		p = data.get('p')
		if not (isinstance(p, int) and -1 < p < 3):
			return
		# if self.CreateComponent(playerId, 'Minecraft', 'item').GetPlayerItem(serverApi.GetMinecraftEnum().ItemPosType.INVENTORY, slot) is not None:
		# 	comp = self.CreateComponent(playerId, 'Minecraft', 'command')
		# 	alertSystem = serverApi.GetSystem("neteaseAlert", "neteaseAlertDev")
		# 	if alertSystem:
		# 		alertSystem.Alert(playerId, '§e请选择空位格子。', 2, 0.5, 0.8)
		# 	else:
		# 		comp.SetCommand('tellraw @s {"rawtext": [{"text": "%s"}]}' % '§e请选择空位格子', playerId)
		# 	return
		redisPool.AsyncGet('{}:jewel:arm'.format(uid), lambda stuff: self.PostPlayerClaimGem(uid, slot, stuff, p))

	def PostPlayerOfferGem(self, uid, slot, cur, stuff, p):
		"""
		往宝石镶嵌台上的装备的指定镶嵌孔中，镶嵌背包指定格子中的一颗宝石
		"""
		if stuff is None:
			return
		playerId = netgameApi.GetPlayerIdByUid(uid)
		if not playerId:
			return
		itemComp = self.CreateComponent(playerId, 'Minecraft', 'item')
		if not itemComp:
			return
		itemDict = itemComp.GetPlayerItem(serverApi.GetMinecraftEnum().ItemPosType.INVENTORY, slot)
		if itemDict is None or json.dumps(itemDict) != cur:
			logout.error('inconsistent data PostPlayerOfferGem uid: {} slot: {} cur: {} stuff: {}'.format(uid, slot, cur, stuff))
			serverApi.GetSystem(jewelConst.ModName, "bag").sync(uid)
			return
		arm = json_loads(stuff)
		if not arm:
			logout.error('unlikely Exception in PostPlayerOfferGem uid: {} slot: {} cur: {} stuff: {}'.format(uid, slot, cur, stuff))
			return
		try:
			data = json_loads(arm['extraId'].strip() or '{}')  # type: dict
			gems = data.setdefault('calculator:{}'.format(jewelConst.ModName), [None, None, None])
			if gems[p]:
				if itemDict['count'] == 1:
					itemComp.SpawnItemToPlayerInv(gems[p], playerId, slot)
				else:
					demand = 1
					free = []
					inv = serverApi.GetMinecraftEnum().ItemPosType.INVENTORY
					for i in xrange(36):
						if itemComp.GetPlayerItem(inv, i) is None:
							free.append(i)
							if len(free) >= demand:
								break
					if len(free) < demand:
						return
					itemComp.SetInvItemNum(slot, itemDict['count'] - 1)
					itemComp.SpawnItemToPlayerInv(gems[p], playerId, free.pop())
			else:
				itemComp.SetInvItemNum(slot, itemDict['count'] - 1)
			itemDict['count'] = 1
			gems[p] = itemDict
			arm['extraId'] = json.dumps(data)
			stuff = json.dumps(arm)
		except Exception as e:
			logout.error('invalid data PostPlayerOfferGem uid: {} slot: {} cur: {} stuff: {} p: {} e: {}'.format(uid, slot, cur, stuff, p, e))
			import traceback
			traceback.print_exc()
			return
		redisPool.AsyncSet(
			'{}:jewel:arm'.format(uid),
			stuff,
			lambda rtn: self.OpenJewelBoard(uid, stuff=stuff) if rtn else logout.error('lost in PostPlayerOfferGem uid: {} slot: {} cur: {} stuff: {} rtn: {}'.format(uid, slot, cur, stuff, rtn))
		)

	def OnPlayerOfferGem(self, data):
		"""
		往宝石镶嵌台上的装备的指定镶嵌孔中，镶嵌背包指定格子中的一颗宝石，完整的步骤有：
		1、检查client发送的背包格中的宝石信息是否一致
		2、从redis中获取宝石镶嵌台中的装备以及其镶嵌的宝石信息
		3、取出背包中的宝石，镶嵌到装备中
		4、把镶嵌宝石后的装备信息，重新存储到redis中
		5、把新的背包信息和宝石镶嵌台信息同步给client
		"""
		print 'OnPlayerOfferGem', data
		args = self.Preview(data)
		if args:
			p = data.get('p')
			if not (isinstance(p, int) and -1 < p < 3):
				return
			uid, slot, cur, itemDict = args
			if itemDict['itemName'] in self.mGems or '{}:{}'.format(itemDict['itemName'], itemDict['auxValue']) in self.mGems:
				redisPool.AsyncGet('{}:jewel:arm'.format(uid), lambda stuff: self.PostPlayerOfferGem(uid, slot, cur, stuff, p))

	def OnSOS(self, data):
		print 'OnSOS', data
		playerId = data.get("playerId", "-1")
		uid = netgameApi.GetPlayerUid(playerId)
		if not uid:
			print 'can not get uid by playerId: %s' % playerId
			return
		serverApi.GetSystem(jewelConst.ModName, "bag").sos(uid, data.get('f'), data.get('t'))

	def getset(self, conn, name, value):
		try:
			return conn.getset(name, value)
		except:
			return -1

	def PostPlayerOfferArm(self, uid, slot, cur, pre):
		"""
		把背包中的一件装备，放上宝石镶嵌台
		"""
		if pre == -1:
			logout.error('Exception in PostPlayerOfferArm uid: {} slot: {} cur: {} pre: {}'.format(uid, slot, cur, pre))
			return
		playerId = netgameApi.GetPlayerIdByUid(uid)
		if not playerId:
			logout.error('rollback PostPlayerOfferArm uid: {} slot: {} cur: {} pre: {}'.format(uid, slot, cur, pre))
			return redisPool.AsyncDelete(
				'{}:jewel:arm'.format(uid),
				lambda *args: logout.info('rollback done PostPlayerOfferArm uid: {} slot: {} cur: {} pre: {} args: {}'.format(uid, slot, cur, pre, args))
			) if pre is None else redisPool.AsyncSet(
				'{}:jewel:arm'.format(uid),
				pre,
				lambda *args: logout.info('rollback done PostPlayerOfferArm uid: {} slot: {} cur: {} pre: {} args: {}'.format(uid, slot, cur, pre, args))
			)
		itemComp = self.CreateComponent(playerId, 'Minecraft', 'item')
		itemDict = itemComp.GetPlayerItem(serverApi.GetMinecraftEnum().ItemPosType.INVENTORY, slot)
		if itemDict is None or json.dumps(itemDict) != cur:
			logout.error('inconsistent data PostPlayerOfferArm uid: {} slot: {} cur: {} pre: {}'.format(uid, slot, cur, pre))
			serverApi.GetSystem(jewelConst.ModName, "bag").sync(uid)
			return redisPool.AsyncDelete(
				'{}:jewel:arm'.format(uid),
				lambda *args: logout.info('rollback done PostPlayerOfferArm uid: {} slot: {} cur: {} pre: {} args: {}'.format(uid, slot, cur, pre, args))
			) if pre is None else redisPool.AsyncSet(
				'{}:jewel:arm'.format(uid),
				pre,
				lambda *args: logout.info('rollback done PostPlayerOfferArm uid: {} slot: {} cur: {} pre: {} args: {}'.format(uid, slot, cur, pre, args))
			)
		itemDict = pre and json_loads(pre) or {
			'itemName': "minecraft:air",
			'count': 0,
			'auxValue': 0,
		}
		itemComp.SpawnItemToPlayerInv(itemDict, playerId, slot)
		redisPool.AsyncSet(
			'{}:jewel:arm'.format(uid),
			cur,
			lambda rtn: self.OpenJewelBoard(uid, stuff=cur) if rtn else logout.error('lost in PostPlayerOfferArm uid: {} slot: {} cur: {} pre: {} rtn: {}'.format(uid, slot, cur, pre, rtn))
		)

	def OnPlayerOfferArm(self, data):
		"""
		把背包中的一件装备，放上宝石镶嵌台（宝石镶嵌台上的装备信息，保存在redis数据库中）
		假如宝石镶嵌台上已经有装备了，那么就把对应的装备放到背包中
		"""
		print 'OnPlayerOfferArm', data
		args = self.Preview(data)
		if args:
			uid, slot, cur, itemDict = args
			if itemDict['itemName'] in self.mArms or '{}:{}'.format(itemDict['itemName'], itemDict['auxValue']) in self.mArms:
				redisPool.AsyncFuncWithKey(
					self.getset,
					"player_{}_offer_arm".format(uid),
					lambda pre: self.PostPlayerOfferArm(uid, slot, cur, pre),
					'{}:jewel:arm'.format(uid), 'null'
				)

	def PostPlayerClaimArm(self, uid, slot, stuff):
		"""
		把宝石镶嵌台上的装备，取下放置到背包中
		"""
		if stuff == -1:
			logout.error('Exception in PostPlayerClaimArm uid: {} slot: {} stuff: {}'.format(uid, slot, stuff))
			return
		if stuff is None:
			return redisPool.AsyncDelete(
				'{}:jewel:arm'.format(uid),
				lambda *args: logout.info('rollback done PostPlayerClaimArm uid: {} slot: {} stuff: {} args: {}'.format(uid, slot, stuff, args))
			)
		playerId = netgameApi.GetPlayerIdByUid(uid)
		if not playerId:
			return redisPool.AsyncSet(
				'{}:jewel:arm'.format(uid),
				stuff,
				lambda *args: logout.info('rollback done PostPlayerClaimArm uid: {} slot: {} stuff: {} args: {}'.format(uid, slot, stuff, args))
			)
		itemComp = self.CreateComponent(playerId, 'Minecraft', 'item')
		itemDict = itemComp.GetPlayerItem(serverApi.GetMinecraftEnum().ItemPosType.INVENTORY, slot)
		# if itemDict is None:
		# 	itemComp.SpawnItemToPlayerInv(json_loads(stuff), playerId, slot)
		# 	return redisPool.AsyncDelete(
		# 		'{}:jewel:arm'.format(uid),
		# 		lambda *args: self.OpenJewelBoard(uid, stuff=None)
		# 	)
		# if itemDict['itemName'] in self.mArms or '{}:{}'.format(itemDict['itemName'], itemDict['auxValue']) in self.mArms:
		# 	itemComp.SpawnItemToPlayerInv(json_loads(stuff), playerId, slot)
		# 	stuff = json.dumps(itemDict)
		# 	redisPool.AsyncSet(
		# 		'{}:jewel:arm'.format(uid),
		# 		stuff,
		# 		lambda rtn: self.OpenJewelBoard(uid, stuff=stuff) if rtn else logout.error('lost in PostPlayerClaimArm uid: {} slot: {} stuff: {} rtn: {}'.format(uid, slot, stuff, rtn))
		# 	)
		if itemDict is None:
			itemComp.SpawnItemToPlayerInv(json_loads(stuff), playerId, slot)
			return redisPool.AsyncDelete(
				'{}:jewel:arm'.format(uid),
				lambda *args: self.OpenJewelBoard(uid, stuff=None)
			)
		else:
			logout.error('inconsistent data PostPlayerClaimArm uid: {} slot: {} stuff: {}'.format(uid, slot, stuff))
			serverApi.GetSystem(jewelConst.ModName, "bag").sync(uid)
			redisPool.AsyncSet(
				'{}:jewel:arm'.format(uid),
				stuff,
				lambda *args: logout.info('rollback done PostPlayerClaimArm uid: {} slot: {} stuff: {} args: {}'.format(uid, slot, stuff, args))
			)

	def OnPlayerClaimArm(self, data):
		"""
		把宝石镶嵌台上的装备，取下放置到背包中
		"""
		print 'OnPlayerClaimArm', data
		playerId = data.get("playerId", "-1")
		uid = netgameApi.GetPlayerUid(playerId)
		if not uid:
			print 'can not get uid by playerId: %s' % playerId
			return
		itemComp = self.CreateComponent(playerId, 'Minecraft', 'item')
		demand = 1
		free = []
		inv = serverApi.GetMinecraftEnum().ItemPosType.INVENTORY
		for i in xrange(36):
			if itemComp.GetPlayerItem(inv, i) is None:
				free.append(i)
				if len(free) >= demand:
					break
		if len(free) < demand:
			comp = self.CreateComponent(playerId, 'Minecraft', 'command')
			alertSystem = serverApi.GetSystem("neteaseAlert", "neteaseAlertDev")
			if alertSystem:
				alertSystem.Alert(playerId, '§e背包无空位格子。', 2, 0.5, 0.8)
			else:
				comp.SetCommand('tellraw @s {"rawtext": [{"text": "%s"}]}' % '§e背包无空位格子', playerId)
			return
		slot = free[0]
		# slot = data.get('slot')
		# if not (isinstance(slot, int) and -1 < slot < 36):
		# 	return
		# itemComp = self.CreateComponent(playerId, 'Minecraft', 'item')
		# itemDict = itemComp.GetPlayerItem(serverApi.GetMinecraftEnum().ItemPosType.INVENTORY, slot)
		# if itemDict is None or itemDict['itemName'] in self.mArms or '{}:{}'.format(itemDict['itemName'], itemDict['auxValue']) in self.mArms:
		# 	redisPool.AsyncFuncWithKey(
		# 		self.getset,
		# 		"player_{}_claim_arm".format(uid),
		# 		lambda stuff: self.PostPlayerClaimArm(uid, slot, stuff),
		# 		'{}:jewel:arm'.format(uid), 'null'
		# 	)
		redisPool.AsyncFuncWithKey(
			self.getset,
			"player_{}_claim_arm".format(uid),
			lambda stuff: self.PostPlayerClaimArm(uid, slot, stuff),
			'{}:jewel:arm'.format(uid), 'null'
		)

	def OpenJewelBoard(self, uid, **kwargs):
		"""
		通知client打开宝石镶嵌界面，需要向client同步背包信息与宝石镶嵌台上的装备信息
		"""
		print 'OpenJewelBoard', uid
		playerId = netgameApi.GetPlayerIdByUid(uid)
		if not playerId:
			print 'can not get playerId by uid: %s' % uid
			return
		if 'stuff' in kwargs:
			try:
				comp = self.CreateComponent(playerId, 'Minecraft', 'item')
				inv = serverApi.GetMinecraftEnum().ItemPosType.INVENTORY
				self.NotifyToClient(playerId, jewelConst.DisplayJewelBoardEvent, {
					'inventory': [json.dumps(comp.GetPlayerItem(inv, i)) for i in xrange(36)],
					'stuff': kwargs['stuff'],
					'arms': self.mArms,
					'gems': self.mGems
				})
			except:
				logout.error("Exception in OpenJewelBoard")
		else:
			redisPool.AsyncGet('{}:jewel:arm'.format(uid), lambda stuff: self.OpenJewelBoard(uid, stuff=stuff))
