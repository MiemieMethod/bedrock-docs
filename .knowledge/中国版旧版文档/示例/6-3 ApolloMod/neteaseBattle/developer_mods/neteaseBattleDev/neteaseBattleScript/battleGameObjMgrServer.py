# -*- coding: utf-8 -*-

import logout
import server.extraServerApi as extraServerApi
from neteaseBattleScript.battleCommon.battleGameObjMgr import GameObjMgr
from neteaseBattleScript.battleCommon.battleConsts import SInterEvent
import neteaseBattleScript.battleCommon.battleConsts as battleConsts
import neteaseBattleScript.battleCommon.apiUtil as apiUtil
from neteaseBattleScript.battleCommon.battleConsts import GameObjType, GameEquipPart, EquipSetArmor, EquipSetExtra
import neteaseBattleScript.battleCommon.battleMob as battleMob
import neteaseBattleScript.battleCommon.battlePlayer as battlePlayer
import neteaseBattleScript.battleCommon.battleBullet as battleBullet
import neteaseBattleScript.battleCommon.battleEquip as battleEquip
import neteaseBattleScript.battleCommon.battleEmptyEquip as battleEmptyEquip

class GameObjMgrServer(GameObjMgr):
	"""
	该mod的服务端游戏对象管理器类
	监听了所有可能影响实体属性变化的事件
	监听了一些玩家道具改变的事件以用于同步背包
	将玩家属性的变化和同步分开执行
	避免了同时改变了属性的实体过多导致逻辑执行的卡顿
	"""
	def __init__(self):
		super(GameObjMgrServer, self).__init__()
		self.mMaxUniqueId = 0
		self.mNeedScanPlayers = set()  # 获得了装备的玩家需要扫描该玩家的装备修改这个装备的tips
		self.mActivePlayers = {}  # 活跃玩家列表，其结构是{玩家playerId: 感兴趣的实体清单}，因为有些实体之间互不关联，所以不会把所有实体都同步到客户端，只会同步客户端感兴趣的列表
		self.mWaitBagScanPlayers = set()  # 需要扫描背包同步的玩家
		self.mForceSyncBagPlayers = set()  # 调用接口要求背包同步的玩家列表
		self.mNeedSyncSet = set()  # 需要同步属性的实体清单，由于将所有操作一次性全部完成会在1tick中占用很多时间，所以分步骤分tick处理逻辑
		self.mNeedUpdateSet = set()  # 已知一些实体的属性将发生变化，但并不同时执行属性变化逻辑，则用这个集合记录一些属性有变化的实体id，分到其他tick的时候来计算属性的变化并扔到上一个集合里面等待同步到客户端

	def GenerateGuid(self):
		self.mMaxUniqueId += 1
		return "py:%d" % self.mMaxUniqueId

	def Init(self):
		apiUtil.GetServerSystem().RegisterEventServer("AddEntityServerEvent", self, self.OnEntityAdd)
		apiUtil.GetServerSystem().RegisterEventServer("EntityRemoveEvent", self, self.OnEntityDel)
		apiUtil.GetServerSystem().RegisterEventServer("AddServerPlayerEvent", self, self.OnPlayerAdd)
		apiUtil.GetServerSystem().RegisterEventServer("DelServerPlayerEvent", self, self.OnPlayerDel)
		apiUtil.GetServerSystem().RegisterEventServer("AddLevelEvent", self, self.OnPlayerLevelChange)
		apiUtil.GetServerSystem().RegisterEventServer("PlayerRespawnEvent", self, self.OnPlayerRespawn)
		apiUtil.GetServerSystem().RegisterEventServer("OnNewArmorExchangeServerEvent", self, self.OnArmorExchange)
		apiUtil.GetServerSystem().RegisterEventServer("OnOffhandItemChangedServerEvent", self, self.OnOffHandExchange)
		apiUtil.GetServerSystem().RegisterEventServer("OnCarriedNewItemChangedServerEvent", self, self.OnMainHandExchange)
		apiUtil.GetServerSystem().RegisterEventServer("ActorAcquiredItemServerEvent", self, self.OnPlayerGetItem)
		apiUtil.GetServerSystem().RegisterInterEvent(SInterEvent.ClientGetItem, self.OnPlayerClientGetItem)
		apiUtil.GetServerSystem().RegisterInterEvent(SInterEvent.ClientEnter, self.OnClientEnter)
		apiUtil.GetServerSystem().RegisterInterEvent(SInterEvent.ClientDeclearInterest, self.OnClientShowInterest)
		apiUtil.GetServerSystem().RegisterInterEvent(SInterEvent.ClientEquipAction, self.OnChangeEquipAction)
		apiUtil.GetServerSystem().RegisterInterEvent(SInterEvent.ExchangeBagItem, self.OnExchangeBagItem)

	def Destroy(self):
		apiUtil.GetServerSystem().UnRegisterEventServer("AddEntityServerEvent", self, self.OnEntityAdd)
		apiUtil.GetServerSystem().UnRegisterEventServer("EntityRemoveEvent", self, self.OnEntityDel)
		apiUtil.GetServerSystem().UnRegisterEventServer("AddServerPlayerEvent", self, self.OnPlayerAdd)
		apiUtil.GetServerSystem().UnRegisterEventServer("DelServerPlayerEvent", self, self.OnPlayerDel)
		apiUtil.GetServerSystem().UnRegisterEventServer("AddLevelEvent", self, self.OnPlayerLevelChange)
		apiUtil.GetServerSystem().UnRegisterEventServer("PlayerRespawnEvent", self, self.OnPlayerRespawn)
		apiUtil.GetServerSystem().UnRegisterEventServer("OnNewArmorExchangeServerEvent", self, self.OnArmorExchange)
		apiUtil.GetServerSystem().UnRegisterEventServer("OnOffhandItemChangedServerEvent", self, self.OnOffHandExchange)
		apiUtil.GetServerSystem().UnRegisterEventServer("OnCarriedNewItemChangedServerEvent", self, self.OnMainHandExchange)
		apiUtil.GetServerSystem().UnRegisterEventServer("ActorAcquiredItemServerEvent", self, self.OnPlayerGetItem)
		apiUtil.GetServerSystem().UnRegisterInterEvent(SInterEvent.ClientGetItem, self.OnPlayerClientGetItem)
		apiUtil.GetServerSystem().UnRegisterInterEvent(SInterEvent.ClientEnter, self.OnClientEnter)
		apiUtil.GetServerSystem().UnRegisterInterEvent(SInterEvent.ClientDeclearInterest, self.OnClientShowInterest)
		apiUtil.GetServerSystem().UnRegisterInterEvent(SInterEvent.ClientEquipAction, self.OnChangeEquipAction)
		apiUtil.GetServerSystem().UnRegisterInterEvent(SInterEvent.ExchangeBagItem, self.OnExchangeBagItem)
		super(GameObjMgrServer, self).DelAllObj()

	def Tick(self, frame):
		super(GameObjMgrServer, self).Tick(frame)
		if battleConsts.KeepHpFull and frame % 150 == 0:	# 每5秒钟一次
			self.DoKeepPlayerHpFull()
		if self.mWaitBagScanPlayers:
			for playerId in self.mWaitBagScanPlayers:
				self.ScanPlayerBags(playerId)
			self.mWaitBagScanPlayers = set()
		if self.mForceSyncBagPlayers:
			for playerId in self.mForceSyncBagPlayers:
				self.ScanPlayerBags(playerId, force=True)
			self.mForceSyncBagPlayers = set()
		if self.mNeedScanPlayers:
			for playerId in self.mNeedScanPlayers:
				self.ScanItemTips(playerId)
			self.mNeedScanPlayers = set()
		if self.mNeedSyncSet:
			for guid in self.mNeedSyncSet:
				obj = self.GetObject(guid)
				if not obj:
					continue
				data = obj.PackForSync()
				for playerId in obj.GetInterested():
					apiUtil.GetServerSystem().GetRpcUtil().ClientRpc(playerId).SyncGameObj([data,])
			self.mNeedSyncSet = set()
		if self.mNeedUpdateSet:
			for guid in self.mNeedUpdateSet:
				obj = self.GetObject(guid)
				if not obj:
					continue
				_, data = obj.PackForUpdate()
				for playerId in obj.GetInterested():
					apiUtil.GetServerSystem().GetRpcUtil().ClientRpc(playerId).UpdateGameObj([guid,], [data,])
			self.mNeedUpdateSet = set()
	# ---------------------------------------------------------------------------------------
	def CreateGameObj(self, entityId, objType):
		if not entityId:
			guid = self.GenerateGuid()
		else:
			guid = str(entityId)
		if objType == GameObjType.Mob:
			return battleMob.BattleMob(guid, objType)
		elif objType == GameObjType.Player:
			return battlePlayer.BattlePlayer(guid, objType)
		elif objType == GameObjType.Bullet:
			return battleBullet.BattleBullet(guid, objType)
		elif objType == GameObjType.Equip:
			return battleEquip.BattleEquip(guid, objType)
		elif objType == GameObjType.EmptyEquip:
			return battleEmptyEquip.BattleEmptyEquip(guid, objType)
		else:
			logout.error("CreateGameObj fail objType=%s guid=%s" % (objType, guid))
			return None

	def DoKeepPlayerHpFull(self):
		for playerId in self.mActivePlayers.iterkeys():
			player = self.GetObject(playerId)
			if not player or player.mIsDie:
				continue
			# 设置氧气值
			comp = apiUtil.GetServerSystem().CreateComponent(playerId, "Minecraft", "breath")
			comp.SetCurrentAirSupply(300)
			# 设置生命值
			comp = apiUtil.GetServerSystem().CreateComponent(playerId, "Minecraft", "attr")
			comp.SetAttrValue(extraServerApi.GetMinecraftEnum().AttrType.HEALTH, 20)
	#---------------------------------------------------------------------------------------
	def GetBulletSource(self, entityId):
		comp = apiUtil.GetServerSystem().CreateComponent(entityId, "Minecraft", "bulletAttributes")
		sourceId = comp.GetSourceEntityId()
		return self.GetObject(sourceId)

	def IsBullet(self, entityId):
		comp = apiUtil.GetServerSystem().CreateComponent(entityId, "Minecraft", "engineType")
		if not comp:
			return False
		engineType = comp.GetEngineType()
		if engineType & extraServerApi.GetMinecraftEnum().EntityType.Projectile == extraServerApi.GetMinecraftEnum().EntityType.Projectile:
			return True
		else:
			return False

	def IsMob(self, entityId):
		comp = apiUtil.GetServerSystem().CreateComponent(entityId, "Minecraft", "engineType")
		if not comp:
			return False
		engineType = comp.GetEngineType()
		if engineType & extraServerApi.GetMinecraftEnum().EntityType.Mob == extraServerApi.GetMinecraftEnum().EntityType.Mob:
			return True
		else:
			return False

	def ScanItemTips(self, playerId):
		comp = apiUtil.GetServerSystem().CreateComponent(playerId, 'Minecraft', 'item')
		posType = extraServerApi.GetMinecraftEnum().ItemPosType.INVENTORY
		for slot in xrange(36):
			itemDict = comp.GetPlayerItem(posType, slot)
			if not itemDict:
				continue
			if not battleConsts.IsEquip(itemDict["itemName"], itemDict["auxValue"]):
				# print "ChangeItemTips not equip item %s" % itemDict["itemName"]
				continue
			suc, extraData = apiUtil.UnpackItemExtra(itemDict)
			if not suc:
				continue
			guid = extraData.get("guid", None)
			if guid:
				continue
			extraData["guid"] = self.GenerateGuid()
			extraId = apiUtil.PackItemExtra(extraData)
			tips = battleConsts.FormatCustomTips(itemDict["itemName"], itemDict["auxValue"])
			suc = comp.ChangePlayerItemTipsAndExtraId(posType, slot, tips, extraId)
			print "ChangeItemTips for[%s] slot=%s suc=%s" % (playerId, slot, suc)

	def ScanPlayerBags(self, playerId, force=False):
		print "ScanPlayerBags playerId=%s start force=%s" % (playerId, force)
		player = self.GetObject(playerId)
		if not player:
			print "ScanPlayerBags cannot find player"
			return
		oldBagInfo = player.GetBagsInfo()
		comp = apiUtil.GetServerSystem().CreateComponent(playerId, 'Minecraft', 'item')
		posType = extraServerApi.GetMinecraftEnum().ItemPosType.INVENTORY
		newBagInfo = {}
		diffBagInfo = {}
		for slot in xrange(36):
			oldInfo = oldBagInfo.get(slot, None)
			itemDict = comp.GetPlayerItem(posType, slot, True)
			if itemDict:
				newInfo = (
					itemDict["itemName"],
					itemDict["auxValue"],
					itemDict["count"],
					itemDict['durability'],
					itemDict['userData'],
					itemDict['extraId']
				)
			else:
				newInfo = None
			newBagInfo[slot] = newInfo
			if oldInfo == newInfo:
				continue
			diffBagInfo[slot] = newInfo
		if diffBagInfo:
			print "ScanPlayerBags player %s bag changed" % playerId
			player.UpdateBagsInfo(newBagInfo)
			apiUtil.GetServerSystem().GetRpcUtil().ClientRpc(playerId).SyncBagsInfo(playerId, newBagInfo)
		elif force:
			print "ScanPlayerBags player %s bag with no changed but force sync" % playerId
			player.UpdateBagsInfo(newBagInfo)
			apiUtil.GetServerSystem().GetRpcUtil().ClientRpc(playerId).SyncBagsInfo(playerId, newBagInfo)
		else:
			print "ScanPlayerBags player %s bag not changed" % playerId
	#---------------------------------------------------------------------------------------
	def DeclearDirty(self, guid):
		self.mNeedUpdateSet.add(guid)

	def DelObjectById(self, guid):
		obj = self.GetObject(guid)
		if obj:
			for playerId in obj.GetInterested():
				apiUtil.GetServerSystem().GetRpcUtil().ClientRpc(playerId).DeleteGameObj([guid,])
		super(GameObjMgrServer, self).DelObjectById(guid)
	#---------------------------------------------------------------------------------------
	def OnEntityAdd(self, data):
		entityName, entityId = data["engineTypeStr"], data["id"]
		if self.IsBullet(entityId):
			bullet = self.CreateGameObj(entityId, GameObjType.Bullet)
			parent = self.GetBulletSource(entityId)
			if not parent:
				logout.error("AddBullet [%s] fail by no parent"%entityId)
				return
			bullet.OnCreateByInherit(parent)
			entity = bullet
			# print "OnEntityAdd is bullet name=%s parent=%s" % (entityName, parent)
		elif self.IsMob(entityId):
			mob = self.CreateGameObj(entityId, GameObjType.Mob)
			mob.OnCreate(entityName, 0)
			entity = mob
		else:
			return
		nameComp = apiUtil.GetServerSystem().CreateComponent(entityId, "Minecraft", "name")
		if nameComp:
			entity.SetEntityName(nameComp.GetName())
		suc = self.AddObject(entity)
		if not suc:
			logout.error("AddEntity [%s] fail, update instead"%entityId)
			self.UpdateObject(entity)
		self.mNeedSyncSet.add(entity.GetId())
		# print "AddEntity [%s] name=%s" % (entityId, entityName)

	def OnEntityDel(self, data):
		entityId = data["id"]
		self.DelObjectById(entityId)
		# print "DelEntity [%s]" % entityId
	
	def OnPlayerLevelChange(self, data):
		playerId = data["id"]
		newLevel = data["newLevel"]
		print "OnPlayerLevelChange playerId={} newLevel={}".format(playerId, newLevel)
		player = self.GetObject(playerId)
		if not player:
			return
		player.ChangeLevel(newLevel)
		self.DeclearDirty(player.GetId())

	def OnPlayerAdd(self, data):
		playerId = data["id"]
		lvComp = apiUtil.GetServerSystem().CreateComponent(playerId, "Minecraft", "lv")
		level = lvComp.GetPlayerLevel()
		print "OnPlayerAdd level={}".format(level)
		player = self.CreateGameObj(playerId, GameObjType.Player)
		player.OnCreate("player", level)
		suc = self.AddObject(player)
		if not suc:
			logout.error("AddPlayer [%s] fail, update instead" % playerId)
			self.UpdateObject(player)
		else:
			self.mNeedScanPlayers.add(playerId)
		self.mWaitBagScanPlayers.add(playerId)
		self.mNeedSyncSet.add(player.GetId())
		self.LoadPlayerExtra(playerId, player)
		self.mActivePlayers[playerId] = set()
		# 设置饥饿值
		if battleConsts.KeepHpFull:
			comp = apiUtil.GetServerSystem().CreateComponent(playerId, "Minecraft", "player")
			comp.SetPlayerMaxExhaustionValue(1000.0)
		# print "AddPlayer [%s]" % playerId

	def OnPlayerDel(self, data):
		playerId = data["id"]
		self.DelObjectById(playerId)
		# print "DelPlayer [%s]" % playerId
		# 玩家退出，清理关注列表
		for guid in self.mActivePlayers.get(playerId, []):
			obj = self.GetObject(guid)
			if not obj:
				continue
			obj.DiscardInterest(playerId)

	def OnPlayerRespawn(self, data):
		playerId = data["id"]
		player = self.GetObject(playerId)
		if player:
			player.SetRespawn()
			self.DeclearDirty(playerId)

	def OnArmorExchange(self, data):
		playerId, slot, newArmorName = data["playerId"], data["slot"], data["newArmorName"]
		player = self.GetObject(playerId)
		if not player:
			logout.error("OnArmorExchange with empty player[%s]" % playerId)
			return
		if player.GetGameObjType() != GameObjType.Player:
			logout.error("OnArmorExchange with entity[%s] type is not player" % playerId)
			return
		if not newArmorName or newArmorName == "minecraft:air":
			newArmor = None
		else:
			newArmorAuxValue, newArmorModExtralId = data["newArmorAuxValue"], data["newArmorModExtralId"]
			if battleConsts.IsEquip(newArmorName, newArmorAuxValue):
				newArmor = self.CreateGameObj(None, GameObjType.Equip)
			else:
				newArmor = self.CreateGameObj(None, GameObjType.EmptyEquip)
			newArmor.OnCreate(newArmorName, newArmorAuxValue)
			engineItemData = self.GetPlayerEngineItemData(playerId, slot)
			engineItemData['extraId'] = newArmorModExtralId
			newArmor.SaveExtraData(engineItemData)
		player.ChangeEquip(slot, newArmor)
		self.DeclearDirty(playerId)
		self.mWaitBagScanPlayers.add(playerId)
		# print "player [%s] ChangeEquip slot=%s name=%s" % (playerId, slot, newArmorName)

	def OnOffHandExchange(self, data):
		playerId, newItemName = data["playerId"], data["newItemName"]
		player = self.GetObject(playerId)
		if not player:
			logout.error("OnOffHandExchange with empty player[%s]" % playerId)
			return
		if player.GetGameObjType() != GameObjType.Player:
			logout.error("OnOffHandExchange with entity[%s] type is not player" % playerId)
			return
		if not newItemName or newItemName == "minecraft:air":
			newItem = None
		else:
			newItemAuxValue, newItemModExtralId = data["newItemAuxValue"], data["newItemModExtralId"]
			if battleConsts.IsEquip(newItemName, newItemAuxValue):
				newItem = self.CreateGameObj(None, GameObjType.Equip)
			else:
				newItem = self.CreateGameObj(None, GameObjType.EmptyEquip)
			newItem.OnCreate(newItemName, newItemAuxValue)
			engineItemData = self.GetPlayerEngineItemData(playerId, GameEquipPart.OffHand)
			engineItemData['extraId'] = newItemModExtralId
			newItem.SaveExtraData(engineItemData)
		player.ChangeEquip(GameEquipPart.OffHand, newItem)
		self.DeclearDirty(playerId)
		self.mWaitBagScanPlayers.add(playerId)
		# print "player [%s] ChangeOffhand name=%s" % (playerId, newItemName)

	def OnMainHandExchange(self, data):
		playerId, newItemName = data["playerId"], data["newItemName"]
		player = self.GetObject(playerId)
		if not player:
			logout.error("OnMainHandExchange with empty player[%s]" % playerId)
			return
		if player.GetGameObjType() != GameObjType.Player:
			logout.error("OnMainHandExchange with entity[%s] type is not player" % playerId)
			return
		if not newItemName or newItemName == "minecraft:air":
			newItem = None
		else:
			newItemAuxValue, newItemModExtralId = data["newItemAuxValue"], data["newItemModExtralId"]
			if battleConsts.IsEquip(newItemName, newItemAuxValue):
				newItem = self.CreateGameObj(None, GameObjType.Equip)
			else:
				newItem = self.CreateGameObj(None, GameObjType.EmptyEquip)
			newItem.OnCreate(newItemName, newItemAuxValue)
			newItem.SaveExtraData(self.GetPlayerEngineItemData(playerId, GameEquipPart.MainHand))
		player.ChangeEquip(GameEquipPart.MainHand, newItem)
		self.DeclearDirty(playerId)
		# print "player [%s] ChangeMainhand name=%s" % (playerId, newItemName)

	def OnChangeExtraEquip(self, playerId, part, itemDict):
		print "OnChangeExtraEquip", playerId, part, itemDict
		player = self.GetObject(playerId)
		if not player:
			logout.error("OnChangeExtraEquip with empty player[%s]" % playerId)
			return
		if itemDict:
			newItem = self.CreateGameObj(None, GameObjType.Equip)
			newItem.OnCreate(itemDict["itemName"], itemDict["auxValue"])
			extraData = {
				"enchantData": itemDict.get("enchantData", []),
				"customTips": itemDict.get("customTips", ""),
				"extraId": itemDict.get("extraId", ""),
			}
			if itemDict.has_key("durability"):
				extraData["durability"] = itemDict["durability"]
			if 'userData' in itemDict:
				extraData["userData"] = itemDict["userData"]
			newItem.SaveExtraData(extraData)
		else:
			newItem = None
		player.ChangeEquip(part, newItem)
		self.DeclearDirty(playerId)
		self.mWaitBagScanPlayers.add(playerId)
		if itemDict:
			print "player [%s] OnChangeExtraEquip name=%s part=%s" % (playerId, itemDict["itemName"], part)
		else:
			print "player [%s] OnChangeExtraEquip name=%s part=%s" % (playerId, "empty", part)
		self.SavePlayerExtra(playerId, player)

	def OnClientEnter(self, data):
		playerId = data["playerId"]
		player = self.GetObject(playerId)
		if not player:
			return
		player.AddInterest(playerId)
		data = player.PackForSync()
		apiUtil.GetServerSystem().GetRpcUtil().ClientRpc(playerId).SyncGameObj([data,])
		# 调试代码
		# self.TestAddItemForPlayer(playerId)

	def OnClientShowInterest(self, data):
		playerId = data["playerId"]
		intersetSet = self.mActivePlayers[playerId]
		for guid in data["addIds"]:
			obj = self.GetObject(guid)
			if not obj:
				continue
			obj.AddInterest(playerId)
			intersetSet.add(guid)
			apiUtil.GetServerSystem().GetRpcUtil().ClientRpc(playerId).SyncGameObj([obj.PackForSync(),])
		for guid in data["discardIds"]:
			obj = self.GetObject(guid)
			if not obj:
				continue
			intersetSet.discard(guid)
			obj.DiscardInterest(playerId)

	def OnPlayerGetItem(self, data):
		playerId = data["actor"]
		self.mNeedScanPlayers.add(playerId)
		self.mWaitBagScanPlayers.add(playerId)
		# print "[%s]add to mNeedScanPlayers for server get item"%playerId

	def OnPlayerClientGetItem(self, data):
		playerId = data["actor"]
		self.mNeedScanPlayers.add(playerId)
		self.mWaitBagScanPlayers.add(playerId)
		# print "[%s]add to mNeedScanPlayers for client get item"%playerId

	def DeclareBagChanged(self, playerId):
		self.mForceSyncBagPlayers.add(playerId)
	# ----------------------------------------------------------------------------------
	def LoadPlayerExtra(self, playerId, player):
		comp = extraServerApi.CreateComponent(playerId, "Minecraft", "extraData")
		if not comp:
			print "LoadPlayerExtra fail by no component"
			return
		for part in EquipSetExtra:
			strItemDict = comp.GetExtraData("equip%d" % part)
			if not strItemDict:
				continue
			itemDict = apiUtil.UnpackDict(strItemDict)
			if battleConsts.IsEquip(itemDict["itemName"], itemDict["auxValue"]):
				newItem = self.CreateGameObj(None, GameObjType.Equip)
			else:
				newItem = self.CreateGameObj(None, GameObjType.EmptyEquip)
			newItem.OnCreate(itemDict["itemName"], itemDict["auxValue"])
			extraData = {
				"enchantData": itemDict.get("enchantData", []),
				"customTips": itemDict.get("customTips", ""),
				"extraId": itemDict.get("extraId", ""),
			}
			if itemDict.has_key("durability"):
				extraData["durability"] = itemDict["durability"]
			newItem.SaveExtraData(extraData)
			player.ChangeEquip(part, newItem)
			print "LoadPlayerExtra part=%s" % part, itemDict

	def SavePlayerExtra(self, playerId, player):
		comp = extraServerApi.CreateComponent(playerId, "Minecraft", "extraData")
		if not comp:
			print "SavePlayerExtra fail by no component"
			return
		for part in EquipSetExtra:
			equip = player.GetEquipByPart(part)
			if equip:
				itemDict = equip.GetItemDict()
				strItemDict = apiUtil.PackDict(itemDict)
				suc = comp.SetExtraData("equip%d" % part, strItemDict)
			else:
				itemDict = None
				suc = comp.SetExtraData("equip%d" % part, "")
			if suc:
				print "SavePlayerExtra part=%s success" % part, itemDict
			else:
				print "SavePlayerExtra part=%s fail" % part, itemDict

	def TestAddItemForPlayer(self, playerId):
		for name in ("HelmetItems", "ClothesItems", "TrousersItems", "ShoesItems", "OffhandItems"):
			for equipName in getattr(battleConsts, name, []):
				equipName = equipName.split(":")
				if len(equipName) == 2:
					apiUtil.GetServerSystem().DoAddItem(playerId, "%s:%s" % (equipName[0], equipName[1]))
				elif len(equipName) == 3:
					apiUtil.GetServerSystem().DoAddItem(playerId, "%s:%s" % (equipName[0], equipName[1]), auxValue=int(equipName[2]))
		for name in ("NecklaceItems", "EarringsItems", "BeltItems", "RingItems"):
			for equipName in getattr(battleConsts, name, []):
				equipName = equipName.split(":")
				if len(equipName) == 2:
					apiUtil.GetServerSystem().DoAddItem(playerId, "%s:%s" % (equipName[0], equipName[1]), count=5)
				elif len(equipName) == 3:
					apiUtil.GetServerSystem().DoAddItem(playerId, "%s:%s" % (equipName[0], equipName[1]), count=5, auxValue=int(equipName[2]))
	# ----------------------------------------------------------------------------------
	def OnChangeEquipAction(self, data):
		playerId, part, invSlot = data["playerId"], data["part"], data["invSlot"]
		player = self.GetObject(playerId)
		if not player:
			print "OnChangeEquipAction player not exist playerId=%s" % playerId
			return
		if part in EquipSetExtra:
			opList = self.ChangeEquipExtraByScript(player, invSlot, part)
		else:
			opList = self.ChangeEquipArmorByScript(player, invSlot, part)
		if opList:
			apiUtil.GetServerSystem().GetRpcUtil().ClientRpc(playerId).EquipFlyAnimate(playerId, opList)

	def ChangeEquipArmorByScript(self, player, invSlot, part):
		oldEquip = player.GetEquipByPart(part)
		oldItemDict = self.GetPlayerEngineInvItem(player.GetId(), invSlot)
		if oldEquip:
			# 背包栏是空的，卸下装备
			if not oldItemDict:
				self.ClearEquipByPart(player.GetId(), part)
				self.SpawnEquipToBag(player.GetId(), oldEquip, invSlot)
				return [("equip", part, invSlot, oldEquip.mMcName, oldEquip.mAuxValue)]
			# 背包栏中的物品不是装备品，无效操作
			if not battleConsts.IsEquipByPart(oldItemDict["itemName"], oldItemDict["auxValue"], part):
				return None
			# 假如背包中的装备品是可重叠的且数量大于1，那么需要一个空的背包格来卸下当前装备
			if oldItemDict["count"] > 1:
				emptySlot = apiUtil.GetServerSystem().GetEmptySlot(player.GetId())
				if emptySlot is None:
					print "需要至少一个空的背包栏来放置卸下的装备"
					return None
				# 卸下当前装备，放置到空的背包栏中
				self.SpawnEquipToBag(player.GetId(), oldEquip, emptySlot)
				# 选中背包栏中的装备品数量减一
				self.DecreasePlayerEngineInvItemNumber(player.GetId(), oldItemDict, invSlot)
				# 选中背包栏中的装备品装备到对应位置
				self.SpawnEquipToArmorPart(player.GetId(), oldItemDict, part)
				return [("equip", part, emptySlot, oldEquip.mMcName, oldEquip.mAuxValue), ("bag", part, invSlot, oldItemDict["itemName"], oldItemDict["auxValue"])]
			# 假如背包装的装备品数量等于1，那么背包栏中的装备品与装备栏中的装备品对调
			else:
				# 卸下当前装备，放置到对应的背包栏中
				self.SpawnEquipToBag(player.GetId(), oldEquip, invSlot)
				# 选中背包栏中的装备品装备到对应位置
				self.SpawnEquipToArmorPart(player.GetId(), oldItemDict, part)
				return [("equip", part, invSlot, oldEquip.mMcName, oldEquip.mAuxValue), ("bag", part, invSlot, oldItemDict["itemName"], oldItemDict["auxValue"])]
		else:
			# 背包栏是空的，无效操作
			if not oldItemDict:
				return None
			# 背包栏中的物品不是装备品，无效操作
			if not battleConsts.IsEquipByPart(oldItemDict["itemName"], oldItemDict["auxValue"], part):
				return None
			# 选中背包栏中的装备品数量减一
			self.DecreasePlayerEngineInvItemNumber(player.GetId(), oldItemDict, invSlot)
			# 选中背包栏中的装备品装备到对应位置
			self.SpawnEquipToArmorPart(player.GetId(), oldItemDict, part)
			return [("bag", part, invSlot, oldItemDict["itemName"], oldItemDict["auxValue"])]

	def PrepareExtraEquipChanged(self, player, part, oldEquip, newItemDict):
		if oldEquip:
			extraData = oldEquip.GetExtraData()
			oldItemDict = {
				"itemName": oldEquip.mMcName,
				"auxValue": oldEquip.mAuxValue,
				"count": 1,
				"enchantData": extraData.get("enchantData", []),
				"customTips": extraData.get("customTips", ""),
				"extraId": extraData.get("extraId", ""),
			}
			if extraData.has_key("durability"):
				oldItemDict["durability"] = extraData["durability"]
		else:
			oldItemDict = None
		apiUtil.GetServerSystem().OnExtraEquipChanged(player.GetId(), part, oldItemDict, newItemDict)

	def ChangeEquipExtraByScript(self, player, invSlot, part):
		oldEquip = player.GetEquipByPart(part)
		oldItemDict = self.GetPlayerEngineInvItem(player.GetId(), invSlot)
		if oldEquip:
			# 背包栏是空的，卸下装备
			if not oldItemDict:
				self.PrepareExtraEquipChanged(player, part, oldEquip, None)
				self.SpawnEquipToBag(player.GetId(), oldEquip, invSlot)
				self.OnChangeExtraEquip(player.GetId(), part, None)
				return [("equip", part, invSlot, oldEquip.mMcName, oldEquip.mAuxValue)]
			# 背包栏中的物品不是装备品，无效操作
			if not battleConsts.IsEquipByPart(oldItemDict["itemName"], oldItemDict["auxValue"], part):
				print "此物品无法装备在此位置"
				return None
			# 假如背包中的装备品是可重叠的且数量大于1，那么需要一个空的背包格来卸下当前装备
			if oldItemDict["count"] > 1:
				emptySlot = apiUtil.GetServerSystem().GetEmptySlot(player.GetId())
				if emptySlot is None:
					print "需要至少一个空的背包栏来放置卸下的装备"
					return None
				self.PrepareExtraEquipChanged(player, part, oldEquip, oldItemDict)
				# 卸下当前装备，放置到空的背包栏中
				self.SpawnEquipToBag(player.GetId(), oldEquip, emptySlot)
				# 选中背包栏中的装备品数量减一
				self.DecreasePlayerEngineInvItemNumber(player.GetId(), oldItemDict, invSlot)
				# 选中背包栏中的装备品装备到对应位置
				self.OnChangeExtraEquip(player.GetId(), part, oldItemDict)
				return [("equip", part, emptySlot, oldEquip.mMcName, oldEquip.mAuxValue), ("bag", part, invSlot, oldItemDict["itemName"], oldItemDict["auxValue"])]
			# 假如背包装的装备品数量等于1，那么背包栏中的装备品与装备栏中的装备品对调
			else:
				self.PrepareExtraEquipChanged(player, part, oldEquip, oldItemDict)
				# 卸下当前装备，放置到对应的背包栏中
				self.SpawnEquipToBag(player.GetId(), oldEquip, invSlot)
				# 选中背包栏中的装备品装备到对应位置
				self.OnChangeExtraEquip(player.GetId(), part, oldItemDict)
				return [("equip", part, invSlot, oldEquip.mMcName, oldEquip.mAuxValue), ("bag", part, invSlot, oldItemDict["itemName"], oldItemDict["auxValue"])]
		else:
			if not oldItemDict:		# 背包栏是空的，无效操作
				return None
			# 背包栏中的物品不是装备品，无效操作
			if not battleConsts.IsEquipByPart(oldItemDict["itemName"], oldItemDict["auxValue"], part):
				print "此物品无法装备在此位置"
				return None
			self.PrepareExtraEquipChanged(player, part, None, oldItemDict)
			# 选中背包栏中的装备品数量减一
			self.DecreasePlayerEngineInvItemNumber(player.GetId(), oldItemDict, invSlot)
			# 选中背包栏中的装备品装备到对应位置
			self.OnChangeExtraEquip(player.GetId(), part, oldItemDict)
			return [("bag", part, invSlot, oldItemDict["itemName"], oldItemDict["auxValue"])]

	def DecreasePlayerEngineInvItemNumber(self, playerId, itemDict, invSlot):
		comp = apiUtil.GetServerSystem().CreateComponent(playerId, 'Minecraft', 'item')
		if not comp:
			print "DecreasePlayerEngineInvItemNumber fail, no Component"
			return
		suc = comp.SetInvItemNum(invSlot, itemDict["count"]-1)
		if not suc:
			print "DecreasePlayerEngineInvItemNumber fail, SetInvItemNum return fail"

	def ClearEquipByPart(self, playerId, part):
		if part == GameEquipPart.OffHand:
			comp = extraServerApi.CreateComponent(playerId, 'Minecraft', 'item')
			suc = comp.ClearPlayerOffHand(playerId)
			if not suc:
				print "ClearEquipByPart fail, ClearPlayerOffHand return fail"
		else:
			comp = extraServerApi.CreateComponent(playerId, 'Minecraft', 'armorSlot')
			suc = comp.SetArmorNew(part, "minecraft:air")
			if not suc:
				print "ClearEquipByPart fail, SetArmorNew return fail"

	def SpawnEquipToBag(self, playerId, equip, invSlot):
		extraData = equip.GetExtraData()
		itemDict = {
			"itemName": equip.mMcName,
			"auxValue": equip.mAuxValue,
			"count": 1,
			"enchantData": extraData.get("enchantData", []),
			"customTips": extraData.get("customTips", ""),
			"extraId": extraData.get("extraId", ""),
		}
		if extraData.has_key("durability"):
			itemDict["durability"] = extraData["durability"]
		comp = extraServerApi.CreateComponent(playerId, 'Minecraft', 'item')
		suc = comp.SpawnItemToPlayerInv(itemDict, playerId, invSlot)
		if not suc:
			print "SpawnEquipToBag fail, SpawnItemToPlayerInv fail"
			return

	def SpawnEquipToArmorPart(self, playerId, equip, part):
		if part == GameEquipPart.OffHand:
			comp = extraServerApi.CreateComponent(playerId, 'Minecraft', 'item')
			itemDict = {
				"itemName": equip.get("itemName", ""),
				"count": 1,
				"enchantData": equip.get("enchantData", []),
				"auxValue": equip.get("auxValue", 0),
				"customTips": equip.get("customTips", ""),
				"extraId": equip.get("extraId", ""),
			}
			if equip.has_key("durability"):
				itemDict["durability"] = equip["durability"]
			suc = comp.SpawnItemToPlayerOffHand(itemDict, playerId)
			if not suc:
				print "SpawnEquipToArmorPart fail, SpawnItemToPlayerOffHand fail"
		else:
			comp = extraServerApi.CreateComponent(playerId, 'Minecraft', 'armorSlot')
			suc = comp.SetArmorNew(part, equip.get("itemName", ""), equip.get("extraId", ""), equip.get("enchantData", []))
			if not suc:
				print "SpawnEquipToArmorPart fail, SetArmorNew fail"

	def GetPlayerEngineItemData(self, playerId, part):
		comp = apiUtil.GetServerSystem().CreateComponent(playerId, 'Minecraft', 'item')
		extraData = {}
		if part == GameEquipPart.OffHand:
			itemDict = comp.GetPlayerItem(extraServerApi.GetMinecraftEnum().ItemPosType.OFFHAND, 0, True)
		elif part == GameEquipPart.MainHand:
			itemDict = comp.GetPlayerItem(extraServerApi.GetMinecraftEnum().ItemPosType.CARRIED, 0, True)
		elif part in EquipSetArmor:
			itemDict = comp.GetPlayerItem(extraServerApi.GetMinecraftEnum().ItemPosType.ARMOR, part, True)
		else:
			itemDict = None
		print "GetPlayerEngineItemData", itemDict
		if itemDict:
			extraData["enchantData"] = itemDict.get("enchantData", [])
			extraData["customTips"] = itemDict.get("customTips", "")
			extraData["extraId"] = itemDict.get("extraId", "")
			if itemDict.has_key("durability"):
				extraData["durability"] = itemDict["durability"]
			if 'userData' in itemDict:
				extraData["userData"] = itemDict["userData"]
		return extraData

	def GetPlayerEngineInvItem(self, playerId, slot):
		comp = apiUtil.GetServerSystem().CreateComponent(playerId, 'Minecraft', 'item')
		if not comp:
			return None
		itemDict = comp.GetPlayerItem(extraServerApi.GetMinecraftEnum().ItemPosType.INVENTORY, slot, True)
		if not itemDict:
			return None
		return itemDict
	# -----------------------------------------------------------------------------------
	def OnExchangeBagItem(self, data):
		playerId, slot1, slot2 = data["playerId"], data["slot1"], data["slot2"]
		opList = self.DoExchangeBagItem(playerId, slot1, slot2)
		if not opList:
			return
		comp = extraServerApi.CreateComponent(playerId, 'Minecraft', 'item')
		suc = comp.SetInvItemExchange(slot1, slot2)
		if not suc:
			print "%s SetInvItemExchange from %s to %s fail" % (playerId, slot1, slot2)
			return
		self.mWaitBagScanPlayers.add(playerId)
		apiUtil.GetServerSystem().GetRpcUtil().ClientRpc(playerId).BagFlyAnimate(playerId, opList)

	def DoExchangeBagItem(self, playerId, slot1, slot2):
		item1 = self.GetPlayerEngineInvItem(playerId, slot1)
		item2 = self.GetPlayerEngineInvItem(playerId, slot2)
		if item1:
			if item2:
				return [(slot1, slot2, item1["itemName"], item1["auxValue"]), (slot2, slot1, item2["itemName"], item2["auxValue"])]
			else:
				return [(slot1, slot2, item1["itemName"], item1["auxValue"])]
		else:
			if item2:
				return [(slot2, slot1, item2["itemName"], item2["auxValue"])]
			else:
				return None







