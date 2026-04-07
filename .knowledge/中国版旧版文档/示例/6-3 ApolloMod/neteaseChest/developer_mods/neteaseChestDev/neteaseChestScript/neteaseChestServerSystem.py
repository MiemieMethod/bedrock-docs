# -*- coding: utf-8 -*-

import server.extraServerApi as serverApi

ServerSystem = serverApi.GetServerSystemCls()
import netgame.apolloCommon.commonNetgameApi as commonNetgameApi
import lobbyGame.netgameApi as lobbyGameApi
import chestConsts as chestConsts
import operator
import uuid
from coroutineMgrGas import CoroutineMgr

class ChestGas(object):
	def __init__(self, args):
		self.mCid = args.get('cid')
		self.mPosX = args.get('x')
		self.mPosY = args.get('y')
		self.mPosZ = args.get('z')
		self.mAuxData = args.get('auxData')
		self.mOwnerList = {} #uid:nickname
		self.mUserList = {}
		self.mApplicatorList = {}
		self.mOtherCid = -1 #和他合并的箱子的id

BLOCK_TEST = {
	"chest":"箱子",
	"ender_chest":"末影箱",
	"trapped_chest":"陷阱箱",
	"hopper":"漏斗",
	"dropper":"投掷器",
	"dispenser":"发射器",
	"barrel":"木桶",
	"undyed_shulker_box":"潜影盒",
	"shulker_box":"潜影盒",
}

class ChestServerSystem(ServerSystem):
	def __init__(self, namespace, systemName):
		ServerSystem.__init__(self, namespace, systemName)
		print "ChestServerSystem", namespace, systemName
		modConfig = commonNetgameApi.GetModJsonConfig('neteaseChestScript')
		#chestEntity = {}  # cid:ChestGas
		self.toCheckEntity = {} #pos:chestentity
		self.pos2ChestId = {} # pos:cid
		self.isPlacedOwner = modConfig.get("is_placed_owner", True)
		self.blockUser = {}
		#self.mMysqlMgr.InitMysqlDb()
		self.mSType = commonNetgameApi.GetServerType()
		
		self.mUidToPlayerId = {}  # 记录在线玩家的uid:playerId
		
		self.levelId = serverApi.GetLevelId()
		
		self.mCoroutineMgr = CoroutineMgr()
		
		self.enabledBlock = ["chest", "ender_chest", "trapped_chest", "hopper", "dropper", "dispenser", "barrel", "shulker_box", "undyed_shulker_box"]
		comp = self.CreateComponent(self.levelId, "Minecraft", "blockUseEventWhiteList")
		comp.AddBlockItemListenForUseEvent("minecraft:chest:*")
		comp.AddBlockItemListenForUseEvent("minecraft:ender_chest:*")
		comp.AddBlockItemListenForUseEvent("minecraft:trapped_chest:*")
		comp.AddBlockItemListenForUseEvent("minecraft:hopper:0")
		comp.AddBlockItemListenForUseEvent("minecraft:hopper:2")
		comp.AddBlockItemListenForUseEvent("minecraft:hopper:3")
		comp.AddBlockItemListenForUseEvent("minecraft:hopper:4")
		comp.AddBlockItemListenForUseEvent("minecraft:hopper:5")
		comp.AddBlockItemListenForUseEvent("minecraft:dropper:*")
		comp.AddBlockItemListenForUseEvent("minecraft:undyed_shulker_box:*")
		comp.AddBlockItemListenForUseEvent("minecraft:shulker_box:*")
		comp.AddBlockItemListenForUseEvent("minecraft:dispenser:*")
		comp.AddBlockItemListenForUseEvent("minecraft:barrel:*")
		
		
		self.ListenForEvent(serverApi.GetEngineNamespace(), serverApi.GetEngineSystemName(), "ServerBlockUseEvent",self, self.OnServerBlockUseEvent)
		self.ListenForEvent(serverApi.GetEngineNamespace(), serverApi.GetEngineSystemName(), "ServerItemUseOnEvent",self, self.OnServerItemUseOnEvent)
		self.ListenForEvent(serverApi.GetEngineNamespace(), serverApi.GetEngineSystemName(), "HopperTryPullInServerEvent",self, self.OnHopperTryPullInServerEvent)
		self.ListenForEvent(serverApi.GetEngineNamespace(), serverApi.GetEngineSystemName(), "HopperTryPullOutServerEvent",self, self.OnHopperTryPullOutServerEvent)
		self.ListenForEvent(serverApi.GetEngineNamespace(), serverApi.GetEngineSystemName(), "ServerPlayerTryDestroyBlockEvent",self, self.OnServerPlayerTryDestroyBlockEvent)
		self.ListenForEvent(serverApi.GetEngineNamespace(), serverApi.GetEngineSystemName(), "ServerEntityTryPlaceBlockEvent",self, self.OnServerEntityTryPlaceBlockEvent)
		self.ListenForEvent(serverApi.GetEngineNamespace(), serverApi.GetEngineSystemName(), "ServerPlaceBlockEntityEvent",self, self.OnServerPlaceBlockEntityEvent)
		self.ListenForEvent(serverApi.GetEngineNamespace(), serverApi.GetEngineSystemName(), "ChestBlockTryPairWithServerEvent",self, self.OnChestBlockTryPairWithServerEvent)
		self.ListenForEvent(serverApi.GetEngineNamespace(), serverApi.GetEngineSystemName(), "AddServerPlayerEvent", self, self.OnAddServerPlayer)
		self.ListenForEvent(serverApi.GetEngineNamespace(), serverApi.GetEngineSystemName(), "ServerChatEvent", self, self.OnServerChat)
		#self.ListenForEvent(serverApi.GetEngineNamespace(), serverApi.GetEngineSystemName(), "LoadServerAddonScriptsAfter", self, self.OnLoadServerAddonScriptsAfter)
		self.ListenForEvent(chestConsts.ModNameSpace, chestConsts.ClientSystemName, chestConsts.ApplicateFromClientEvent, self, self.OnApplicateFromClientEvent)
		self.ListenForEvent(chestConsts.ModNameSpace, chestConsts.ClientSystemName, chestConsts.DeletUserFromClientEvent, self, self.OnDeletUserFromClientEvent)
		self.ListenForEvent(chestConsts.ModNameSpace, chestConsts.ClientSystemName, chestConsts.AcceptUserFromClientEvent, self, self.OnAcceptUserFromClientEvent)
		self.ListenForEvent(chestConsts.ModNameSpace, chestConsts.ClientSystemName, chestConsts.RefuseUserFromClientEvent, self, self.OnRefuseUserFromClientEvent)
		#self.ListenForEvent(chestConsts.ModNameSpace, chestConsts.MasterSystemName, chestConsts.ChangeChestAuthFromMasterEvent , self, self.OnChangeChestAuthFromMaster)

	def Init(self):
		pass
	
	def Update(self):
		self.mCoroutineMgr.Tick()
		
	def OnHopperTryPullInServerEvent(self, args):
		print "OnHopperTryPullInServerEvent", args
		pos1 = (int(args.get("x")), int(args.get("y")), int(args.get("z")))
		pos2 = (args.get("abovePosX"), args.get("abovePosY"), args.get("abovePosZ"))
		chestEntity = self.exDataComp.GetBlockTileEntityWholeCustomData(pos1)
		otherChestEntity = self.exDataComp.GetBlockTileEntityWholeCustomData(pos2)
		if not chestEntity:
			chestEntity = self.toCheckEntity.get(pos1)
		if not chestEntity:
			return
		mOwnerList1 = chestEntity.get("mOwnerList")
		if not otherChestEntity:
			return
		mOwnerList2 = otherChestEntity.get("mOwnerList")
		print "OnChestBlockTryPairWithServerEvent", mOwnerList1, mOwnerList2
		# print "OnChestBlockTryPairWithServerEvent", chest1["mOwnerList"].keys(), chest2["mOwnerList"].keys()
		if mOwnerList1 and mOwnerList2 and mOwnerList1.keys() == mOwnerList2.keys():
			args["canHopper"] = True
		else:
			args["canHopper"] = False
	
	def OnHopperTryPullOutServerEvent(self, args):
		print "OnHopperTryPullOutServerEvent", args
		pos1 = (int(args.get("x")), int(args.get("y")), int(args.get("z")))
		pos2 = (args.get("attachedPosX"), args.get("attachedPosY"), args.get("attachedPosZ"))
		chestEntity = self.exDataComp.GetBlockTileEntityWholeCustomData(pos1)
		otherChestEntity = self.exDataComp.GetBlockTileEntityWholeCustomData(pos2)
		if not chestEntity:
			chestEntity = self.toCheckEntity.get(pos1)
		if not chestEntity:
			return
		mOwnerList1 = chestEntity.get("mOwnerList")
		if not otherChestEntity:
			return
		mOwnerList2 = otherChestEntity.get("mOwnerList")
		print "OnChestBlockTryPairWithServerEvent", mOwnerList1, mOwnerList2
		# print "OnChestBlockTryPairWithServerEvent", chest1["mOwnerList"].keys(), chest2["mOwnerList"].keys()
		if mOwnerList1 and mOwnerList2 and mOwnerList1.keys() == mOwnerList2.keys():
			args["canHopper"] = True
		else:
			args["canHopper"] = False
	
	def OnServerChat(self, data):
		playerId = data['playerId']
		uid = lobbyGameApi.GetPlayerUid(playerId)
		#dimensionComp = self.CreateComponent(playerId, "Minecraft", "dimension")
		#dimensionComp.ChangePlayerDimension(0, (1400, 70,  32))
		isSilent = lobbyGameApi.GetUidIsSilent(uid)
		print "isSilent", uid, " ",isSilent
		
	def OnApplicateFromClientEvent(self, args):
		print "OnApplicateFromClientEvent", args
		playerId = args.get("playerId")
		cid = args.get("cid")
		pos = args.get('pos')
		self.exDataComp = serverApi.CreateComponent(playerId, "Minecraft", "blockInfo")
		chestEntity = self.exDataComp.GetBlockTileEntityWholeCustomData(pos)
		print "OnApplicateFromClientEvent chestEntity", chestEntity
		if chestEntity is None or chestEntity["mCid"] != cid:
			data = {"code": chestConsts.BoxMoved, "message": chestConsts.ResponseText[chestConsts.BoxMoved]}
			self.NotifyToClient(playerId, chestConsts.ShowTipsFromServerEvent, data)
			return
		playerUID = lobbyGameApi.GetPlayerUid(playerId)
		if len(chestEntity["mUserList"]) >= 5:
			data = {"code": chestConsts.UserNumLimit, "message": chestConsts.ResponseText[chestConsts.UserNumLimit]}
			self.NotifyToClient(playerId, chestConsts.ShowTipsFromServerEvent, data)
			return
		# TODO 获取pair
		comp = serverApi.CreateComponent(playerId, "Minecraft", "blockInfo")
		otherPos = comp.GetChestPairedPosition(pos)
		otherEntity = self.exDataComp.GetBlockTileEntityWholeCustomData(otherPos) if otherPos else None
		nickname = lobbyGameApi.GetPlayerNickname(playerId)
		#chestEntity.mApplicatorList[playerUID] = nickname
		if otherEntity:
			allUserList = dict(chestEntity["mUserList"].items() + otherEntity["mUserList"].items())
			if len(allUserList) >= 5:
				data = {"code": chestConsts.UserNumLimit,"message": chestConsts.ResponseText[chestConsts.UserNumLimit]}
				self.NotifyToClient(playerId, chestConsts.ShowTipsFromServerEvent, data)
				return
			otherEntity["mApplicatorList"][str(playerUID)] = nickname
			self.SetChestDataInTrunk(otherPos, otherEntity)
		chestEntity["mApplicatorList"][str(playerUID)] = nickname
		print "OnApplicateFromClientEvent chestEntity2", chestEntity
		self.SetChestDataInTrunk(pos, chestEntity)
		#userChestDict = {"uid": playerUID, "cid": cid, "own_auth": 3, "stype": self.mSType}

	def OnDeletUserFromClientEvent(self, args):
		playerUID = args.get('uid')
		cid = args.get('cid')
		pos = args.get('pos')
		opPlayerId = args.get('opPlayerId')
		self.exDataComp = serverApi.CreateComponent(opPlayerId, "Minecraft", "blockInfo")
		chestEntity = self.exDataComp.GetBlockTileEntityWholeCustomData(pos)
		if chestEntity is None or chestEntity["mCid"] != cid:
			data = {"code": chestConsts.BoxMoved, "message": chestConsts.ResponseText[chestConsts.BoxMoved]}
			self.NotifyToClient(opPlayerId, chestConsts.ShowTipsFromServerEvent, data)
		if chestEntity and playerUID in chestEntity["mUserList"].keys():
			chestEntity["mUserList"].pop(playerUID)
			self.SetChestDataInTrunk(pos, chestEntity)
		# TODO 获取pair
		comp = serverApi.CreateComponent(opPlayerId, "Minecraft", "blockInfo")
		otherPos = comp.GetChestPairedPosition(pos)
		otherEntity = self.exDataComp.GetBlockTileEntityWholeCustomData(otherPos) if otherPos else None
		if otherEntity:
			if playerUID in otherEntity["mUserList"].keys():
				otherEntity["mUserList"].pop(playerUID)
				self.SetChestDataInTrunk(otherPos, otherEntity)
			data = {
				"cid": chestEntity["mCid"],
				"ownerList": dict(chestEntity["mOwnerList"].items() + otherEntity["mOwnerList"].items()),
				"userList": dict(chestEntity["mUserList"].items() + otherEntity["mUserList"].items()),
				"applicatorList": dict(chestEntity["mApplicatorList"].items() + otherEntity["mApplicatorList"].items()),
			}
		else:
			data = {
				"cid": chestEntity["mCid"],
				"ownerList": chestEntity["mOwnerList"],
				"userList": chestEntity["mUserList"],
				"applicatorList": chestEntity["mApplicatorList"],
			}
		print "ShowChestManageFromServerEvent", data
		self.NotifyToClient(opPlayerId, chestConsts.ShowChestManageFromServerEvent, data)

	def OnAcceptUserFromClientEvent(self, args):
		playerUID = args.get('uid')
		cid = args.get('cid')
		pos = args.get('pos')
		opPlayerId = args.get('opPlayerId')

		playerId = lobbyGameApi.GetPlayerIdByUid(int(playerUID))
		self.exDataComp = serverApi.CreateComponent(opPlayerId, "Minecraft", "blockInfo")
		chestEntity = self.exDataComp.GetBlockTileEntityWholeCustomData(pos)
		if chestEntity is None or chestEntity["mCid"] != cid:
			data = {"code": chestConsts.BoxMoved, "message": chestConsts.ResponseText[chestConsts.BoxMoved]}
			self.NotifyToClient(opPlayerId, chestConsts.ShowTipsFromServerEvent, data)
		nickname = chestEntity["mApplicatorList"].get(playerUID)
		if nickname is None:
			nickname = lobbyGameApi.GetPlayerNickname(playerId)
		if len(chestEntity["mUserList"]) >= 5:
			data = {"code": chestConsts.UserNumLimit, "message": chestConsts.ResponseText[chestConsts.UserNumLimit]}
			self.NotifyToClient(opPlayerId, chestConsts.ShowTipsFromServerEvent, data)
			return
		chestEntity["mUserList"][playerUID] = nickname
		if chestEntity["mApplicatorList"].has_key(playerUID):
			chestEntity["mApplicatorList"].pop(playerUID)
			self.SetChestDataInTrunk(pos, chestEntity)
		#TODO 获取pair
		comp = serverApi.CreateComponent(opPlayerId, "Minecraft", "blockInfo")
		otherPos = comp.GetChestPairedPosition(pos)
		otherEntity = self.exDataComp.GetBlockTileEntityWholeCustomData(otherPos) if otherPos else None
		if otherEntity:
			allUserList = dict(chestEntity["mUserList"].items() + otherEntity["mUserList"].items())
			if len(allUserList) >= 5:
				data = {"code": chestConsts.UserNumLimit,
				        "message": chestConsts.ResponseText[chestConsts.UserNumLimit]}
				self.NotifyToClient(playerId, chestConsts.ShowTipsFromServerEvent, data)
				return
			otherEntity["mUserList"][playerUID] = nickname
			if otherEntity["mApplicatorList"].has_key(playerUID):
				otherEntity["mApplicatorList"].pop(playerUID)
				self.SetChestDataInTrunk(otherPos, otherEntity)
			data = {
				"cid": chestEntity["mCid"],
				"ownerList": dict(chestEntity["mOwnerList"].items() + otherEntity["mOwnerList"].items()),
				"userList": dict(chestEntity["mUserList"].items() + otherEntity["mUserList"].items()),
				"applicatorList": dict(chestEntity["mApplicatorList"].items() + otherEntity["mApplicatorList"].items()),
			}
		else:
			data = {
				"cid": chestEntity["mCid"],
				"ownerList": chestEntity["mOwnerList"],
				"userList": chestEntity["mUserList"],
				"applicatorList": chestEntity["mApplicatorList"],
			}
		print "ShowChestManageFromServerEvent", data
		self.NotifyToClient(opPlayerId, chestConsts.ShowChestManageFromServerEvent, data)
		#userChestDict = {"uid": playerUID, "cid": cid, "own_auth": 2}

	def ChangeChestAuth(self, args):
		playerUid = args.get("playerUid", -1)
		ChestPos = args.get("ChestPos")
		playerId = lobbyGameApi.GetPlayerIdByUid(playerUid)
		playerUid = str(playerUid)
		self.exDataComp = serverApi.CreateComponent(playerId, "Minecraft", "blockInfo")
		chestEntity = self.exDataComp.GetBlockTileEntityWholeCustomData(ChestPos)
		if not chestEntity:
			chestEntity = self.NewOneChestData(str(uuid.uuid1()))
		isOpen = args.get("isOpen")
		if isOpen == False:
			if chestEntity and playerUid in chestEntity["mUserList"].keys():
				chestEntity["mUserList"].pop(playerUid)
				#TODO 获取pair
				comp = serverApi.CreateComponent(playerId, "Minecraft", "blockInfo")
				otherPos = comp.GetChestPairedPosition(ChestPos)
				otherEntity = self.exDataComp.GetBlockTileEntityWholeCustomData(otherPos) if otherPos else None
				if otherEntity and playerUid in otherEntity["mUserList"].keys():
					otherEntity["mUserList"].pop(playerUid)
					self.SetChestDataInTrunk(otherPos, otherEntity)
		else:
			if chestEntity:
				if len(chestEntity["mUserList"]) >= 5:
					return
				playerId = lobbyGameApi.GetPlayerIdByUid(playerUid)
				nickname = lobbyGameApi.GetPlayerNickname(playerId)
				chestEntity["mUserList"][playerUid] = nickname
				if chestEntity["mApplicatorList"].has_key(playerUid):
					chestEntity["mApplicatorList"].pop(playerUid)
				# TODO 获取pair
				comp = serverApi.CreateComponent(playerId, "Minecraft", "blockInfo")
				otherPos = comp.GetChestPairedPosition(ChestPos)
				otherEntity = self.exDataComp.GetBlockTileEntityWholeCustomData(otherPos) if otherPos else None
				if otherEntity:
					allUserList = dict(chestEntity["mUserList"].items() + otherEntity["mUserList"].items())
					if len(allUserList) >= 5:
						return
					otherEntity["mUserList"][playerUid] = nickname
					if otherEntity["mApplicatorList"].has_key(playerUid):
						otherEntity["mApplicatorList"].pop(playerUid)
						self.SetChestDataInTrunk(otherPos, otherEntity)
			self.SetChestDataInTrunk(ChestPos, chestEntity)
			#userChestDict = {"uid": playerUid, "cid": cid, "own_auth": 2}
		
	def ChangeChestOwn(self, args):
		playerUid = args.get("playerUid", -1)
		ChestPos = args.get("ChestPos")
		playerId = lobbyGameApi.GetPlayerIdByUid(playerUid)
		playerUid = str(playerUid)
		self.exDataComp = serverApi.CreateComponent(playerId, "Minecraft", "blockInfo")
		chestEntity = self.exDataComp.GetBlockTileEntityWholeCustomData(ChestPos)
		if not chestEntity:
			chestEntity = self.NewOneChestData(str(uuid.uuid1()))
		nickname = lobbyGameApi.GetPlayerNickname(playerId)
		chestEntity["mOwnerList"] = {}
		chestEntity["mOwnerList"][playerUid] = nickname
		self.SetChestDataInTrunk(ChestPos, chestEntity)
		#TODO 获取pair
		comp = serverApi.CreateComponent(playerId, "Minecraft", "blockInfo")
		otherPos = comp.GetChestPairedPosition(ChestPos)
		otherEntity = self.exDataComp.GetBlockTileEntityWholeCustomData(otherPos) if otherPos else None
		if otherEntity:
			otherEntity["mOwnerList"] = {}
			otherEntity["mOwnerList"][playerUid] = nickname
			self.SetChestDataInTrunk(otherPos, otherEntity)
		
	def OnRefuseUserFromClientEvent(self, args):
		playerUID = args.get('uid')
		cid = args.get('cid')
		pos = args.get('pos')
		opPlayerId = args.get('opPlayerId')
		self.exDataComp = serverApi.CreateComponent(opPlayerId, "Minecraft", "blockInfo")
		chestEntity = self.exDataComp.GetBlockTileEntityWholeCustomData(pos)
		if chestEntity is None or chestEntity["mCid"] != cid:
			data = {"code": chestConsts.BoxMoved, "message": chestConsts.ResponseText[chestConsts.BoxMoved]}
			self.NotifyToClient(opPlayerId, chestConsts.ShowTipsFromServerEvent, data)
		chestEntity["mApplicatorList"].pop(playerUID)
		self.SetChestDataInTrunk(pos, chestEntity)
		#TODO 获取pair
		comp = serverApi.CreateComponent(opPlayerId, "Minecraft", "blockInfo")
		otherPos = comp.GetChestPairedPosition(pos)
		otherEntity = self.exDataComp.GetBlockTileEntityWholeCustomData(otherPos) if otherPos else None
		if otherEntity:
			if playerUID in otherEntity["mApplicatorList"].keys():
				otherEntity["mApplicatorList"].pop(playerUID)
			self.SetChestDataInTrunk(otherPos, otherEntity)
			data = {
				"cid": chestEntity["mCid"],
				"ownerList": dict(chestEntity["mOwnerList"].items() + otherEntity["mOwnerList"].items()),
				"userList": dict(chestEntity["mUserList"].items() + otherEntity["mUserList"].items()),
				"applicatorList": dict(chestEntity["mApplicatorList"].items() + otherEntity["mApplicatorList"].items()),
			}
		else:
			data = {
				"cid": chestEntity["mCid"],
				"ownerList": chestEntity["mOwnerList"],
				"userList": chestEntity["mUserList"],
				"applicatorList": chestEntity["mApplicatorList"],
			}
			
		print "refuseUserChest, ShowChestManageFromServerEvent", data
		self.NotifyToClient(opPlayerId, chestConsts.ShowChestManageFromServerEvent, data)
		
	def OnAddServerPlayer(self, args):
		'''
		玩家登陆的监听函数
		'''
		playerId = args.get('id', '-1')
		playerUid = lobbyGameApi.GetPlayerUid(playerId)
		self.mUidToPlayerId[playerUid] = playerId
	
	def OnChestBlockTryPairWithServerEvent(self, args):
		print "OnChestBlockTryPairWithServerEvent", args
		pos1 = (args.get("blockX"), args.get("blockY"), args.get("blockZ"))
		pos2 = (args.get("otherBlockX"), args.get("otherBlockY"), args.get("otherBlockZ"))
		chestEntity = self.exDataComp.GetBlockTileEntityWholeCustomData(pos1)
		otherChestEntity = self.exDataComp.GetBlockTileEntityWholeCustomData(pos2)
		if not chestEntity:
			chestEntity = self.toCheckEntity.get(pos1)
		if not chestEntity:
			return
		mOwnerList1 = chestEntity.get("mOwnerList")
		if not otherChestEntity:
			return
		mOwnerList2 = otherChestEntity.get("mOwnerList")
		print "OnChestBlockTryPairWithServerEvent", mOwnerList1, mOwnerList2
		#print "OnChestBlockTryPairWithServerEvent", chest1["mOwnerList"].keys(), chest2["mOwnerList"].keys()
		if mOwnerList1 and mOwnerList2 and mOwnerList1.keys() == mOwnerList2.keys():
			args["cancel"] = False
		else:
			args["cancel"] = True
		
	# def CheckChestByPos(self, pos):
	# 	truePos = (pos[0], pos[1], pos[2])
	# 	cid = self.pos2ChestId.get(truePos)
	# 	chestGas = chestEntity.get(cid)
	# 	return chestGas
		# for cid, chestGas in chestEntity.iteritems():
		# 	print "CheckChestByPos", cid, chestGas
		# 	if chestGas.mPosX == pos[0] and chestGas.mPosY == pos[1] and chestGas.mPosZ == pos[2]:
		# 		return chestGas
		# return None
		
	def OnServerBlockUseEvent(self, args):
		print "OnServerBlockUseEvent", args
		playerID = args.get("playerId")
		playerUID = lobbyGameApi.GetPlayerUid(playerID)
		x = args.get('x')
		y = args.get('y')
		z = args.get('z')
		auxData = args.get("aux")
		blockName = args.get("blockName")
		cutIndex = blockName.find(":")
		real_blockName = blockName[cutIndex + 1:]
		print "OnServerBlockUseEvent  ", args
		if real_blockName not in self.enabledBlock:
			return
		print "OnServerBlockUseEvent2  ", real_blockName
		comp = self.CreateComponent(playerID, "Minecraft", "player")
		isSneaking = comp.IsSneaking()
		self.exDataComp = serverApi.CreateComponent(playerID, "Minecraft", "blockInfo")
		chestEntity = self.exDataComp.GetBlockTileEntityWholeCustomData((x, y, z))
		print "chestEntity  ", chestEntity
		if not chestEntity:
			#self.InsertChestCb(str(uuid.uuid1()), x, y, z, playerID, playerUID)
			return
		#TODO 获取他的pair
		comp = serverApi.CreateComponent(playerID, "Minecraft", "blockInfo")
		otherPos = comp.GetChestPairedPosition((x, y, z))
		otherEntity = self.exDataComp.GetBlockTileEntityWholeCustomData(otherPos) if otherPos else None
		print "===================mOwnerList", chestEntity
		if str(playerUID) in chestEntity["mOwnerList"].keys():
			if isSneaking == True:
				args["cancel"] = True
				if otherEntity:
					data = {
						"cid": chestEntity["mCid"],
						"ownerList":  dict(chestEntity["mOwnerList"].items() + otherEntity["mOwnerList"].items()),
						"pos": (x, y, z),
						"blockText": BLOCK_TEST.get(real_blockName, "容器"),
						"userList":  dict(chestEntity["mUserList"].items() + otherEntity["mUserList"].items()),
						"applicatorList":  dict(chestEntity["mApplicatorList"].items() + otherEntity["mApplicatorList"].items()),
					}
				else:
					data = {
						"cid": chestEntity["mCid"],
						"ownerList": chestEntity["mOwnerList"],
						"pos": (x, y, z),
						"blockText": BLOCK_TEST.get(real_blockName, "容器"),
						"userList": chestEntity["mUserList"],
						"applicatorList": chestEntity["mApplicatorList"] ,
					}
				print "ShowChestManageFromServerEvent", data
				self.NotifyToClient(playerID, chestConsts.ShowChestManageFromServerEvent, data)
			else:
				args["cancel"] = False
		elif str(playerUID) in chestEntity["mUserList"].keys() or len(chestEntity["mOwnerList"].keys()) == 0:
			args["cancel"] = False
		elif otherEntity and str(playerUID) in otherEntity["mUserList"].keys():
			args["cancel"] = False
		else:
			args["cancel"] = True
			data = {
				"cid": chestEntity["mCid"],
				"pos": (x, y, z),
				"blockText":BLOCK_TEST.get(real_blockName, "容器"),
				"owner": chestEntity["mOwnerList"].values()[0]
			}
			self.NotifyToClient(playerID, chestConsts.ShowApplicationTipsFromServerEvent, data)
	
	def OnServerPlayerTryDestroyBlockEvent(self, args):
		x = args.get('x')
		y = args.get('y')
		z = args.get('z')
		playerID = args.get("playerId")
		playerUID = lobbyGameApi.GetPlayerUid(playerID)
		blockName = args.get("blockName")
		if blockName not in self.enabledBlock:
			return
		cancel = True
		self.exDataComp = serverApi.CreateComponent(playerID, "Minecraft", "blockInfo")
		chestEntity = self.exDataComp.GetBlockTileEntityWholeCustomData((x, y, z))
		if not chestEntity:
			return
		if chestEntity and str(playerUID) in chestEntity["mOwnerList"].keys():
			cancel = False
				#self.pos2ChestId.pop((x, y, z))
				# if mOtherPos != None and self.exDataComp.GetBlockTileEntityCustomData((x, y, z), "mOtherPos") != None:
				# 	self.exDataComp.SetBlockTileEntityCustomData("mOtherPos", None)
				# 	self.exDataComp.SetBlockTileEntityCustomData("mOtherPos", None)
		args["cancel"] = cancel
		print "OnServerPlayerTryDestroyBlockEvent", args
		
	def OnServerPlaceBlockEntityEvent(self, args):
		print "OnServerPlaceBlockEntityEvent", args
		
	def OnServerItemUseOnEvent(self, args):
		print "OnServerItemUseOnEvent", args
		# itemName = args.get("itemName")
		# cutIndex = itemName.find(":")
		# real_blockName = itemName[cutIndex + 1:]
		# if real_blockName not in self.enabledBlock:
		# 	return
		# x = args.get('x')
		# y = args.get('y') + 1
		# z = args.get('z')
		# playerID = args.get("entityId")
		# self.exDataComp = serverApi.CreateComponent(playerID, "Minecraft", "blockInfo")
		# chestEntity = self.exDataComp.GetBlockTileEntityWholeCustomData((x, y, z))
		# if not chestEntity:
		# 	playerUID = lobbyGameApi.GetPlayerUid(playerID)
		# 	self.InsertChestCb(str(uuid.uuid1()), x, y, z, playerID, playerUID)
		
	def OnServerEntityTryPlaceBlockEvent(self, args):
		print "OnServerEntityTryPlaceBlockEvent test", args
		blockName = args.get("blockName")
		if blockName not in self.enabledBlock:
			return
		x = args.get('x')
		y = args.get('y')
		z = args.get('z')
		playerID = args.get("entityId")
		playerUID = lobbyGameApi.GetPlayerUid(playerID)
		self.InsertChestCb(str(uuid.uuid1()), x, y, z, playerID, playerUID)
		#isSilent = lobbyGameApi.GetUidIsBan(playerUID)
		#print "isSilent", isSilent
		
	def InsertChestCb(self, cid, x, y, z, playerID, playerUID):
		print "InsertChestCb", cid, x, y, z, playerUID
		#chestInfo = {"cid": cid, "auxData": auxData, "x": x, "y": y, "z": z}
		chestDict = self.NewOneChestData(cid)
		self.pos2ChestId[(x, y, z)] = cid
		if self.isPlacedOwner:
			if (playerUID in chestDict["mOwnerList"].keys()) == False:
				playerId = lobbyGameApi.GetPlayerIdByUid(playerUID)
				nickname = lobbyGameApi.GetPlayerNickname(playerId)
				chestDict["mOwnerList"][str(playerUID)] = nickname
				self.exDataComp = serverApi.CreateComponent(playerID, "Minecraft", "blockInfo")
				self.toCheckEntity[(x,y,z)] = chestDict
				self.mCoroutineMgr.StartCoroutine(self.DelaySetChestDataInTrunk((x, y, z), chestDict, 1))
				#self.SetChestDataInTrunk((x, y, z), chestDict)
				
				#userChestDict = {"uid": playerUID, "cid": cid, "own_auth": 1, "stype":self.mSType}
	
	def DelaySetChestDataInTrunk(self, pos, chestDict, delayFrame = 0):
		yield -1 * delayFrame
		print "DelaySetChestDataInTrunk",pos, chestDict
		self.SetChestDataInTrunk(pos, chestDict)
		
	def SetChestDataInTrunk(self, pos, chestDict):
		print "SetChestDataInTrunk", pos, chestDict
		#self.exDataComp = serverApi.CreateComponent(playerId, "Minecraft", "blockInfo")
		for key, value in chestDict.iteritems():
			self.exDataComp.SetBlockTileEntityCustomData(pos, key, value)
			
	def NewOneChestData(self, cid):
		chestInfo = {"mCid": cid, "mOwnerList": {}, "mUserList": {}, "mApplicatorList": {}}
		return chestInfo
		
	def Destroy(self):
		#self.extraDataComp.SetExtraData("chestDict", chestEntity)
		pass