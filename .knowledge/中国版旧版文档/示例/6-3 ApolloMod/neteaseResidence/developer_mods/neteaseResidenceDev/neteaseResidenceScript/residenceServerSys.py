# -*- coding: utf-8 -*-
import server.extraServerApi as serverApi
ServerSystem = serverApi.GetServerSystemCls()
import neteaseResidenceScript.dbApi as dbApi
import neteaseResidenceScript.residenceGasMgr as residenceGasMgr
import neteaseResidenceScript.playerMgr as playerMgr
import neteaseResidenceScript.residenceConsts as residenceConsts
import lobbyGame.netgameApi as lobbyGameApi
import neteaseResidenceScript.util as util
import logout
import timer

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

class ResidenceServerSys(ServerSystem):
	"""
	该mod的服务端类
	"""
	def __init__(self, namespace, systemName):
		ServerSystem.__init__(self, namespace, systemName)
		print 'Init ResidenceServerSys'
		util.SetResidenceSystem(self)
		util.LoadModConf()
		dbApi.Init()
		self.ListenForEvent(residenceConsts.ModNameSpace, residenceConsts.ClientSystemName,
									residenceConsts.LoginRequestEvent, self, self.OnLoginRequest)
		self.ListenForEvent(serverApi.GetEngineNamespace(), serverApi.GetEngineSystemName(), "AddServerPlayerEvent",
							self, self.OnAddServerPlayer)
		self.ListenForEvent(serverApi.GetEngineNamespace(), serverApi.GetEngineSystemName(), "DelServerPlayerEvent",
							self, self.OnDelerverPlayer)
		self.ListenForEvent(serverApi.GetEngineNamespace(), serverApi.GetEngineSystemName(),
							'ServerChatEvent', self, self.OnServerChat)
		self.ListenForEvent(serverApi.GetEngineNamespace(), serverApi.GetEngineSystemName(),
							'OnScriptTickServer', self, self.OnScriptTickServer)
		self.ListenForEvent(serverApi.GetEngineNamespace(), serverApi.GetEngineSystemName(),
		                    'LoadServerAddonScriptsAfter', self, self.OnLoadServerAddonScriptsAfter)
		self.ListenForEvent(residenceConsts.ModNameSpace, residenceConsts.ClientSystemName,
							'ShowCreateTipsFromClient', self, self.OnShowCreateTipsFromClient)
		self.mLaterWork = []
		self.mResidenceMgr = residenceGasMgr.ResidenceGasMgr(self)
		self.mPlayerMgr = playerMgr.PlayerMgr()
		self.Init()
		self.mTransferResidenceTimer = timer.TimerManager.addRepeatTimer(4, self.PollTransfer)  # 4S 轮询一次
		self.mTransferResList = []
		self.mTransferResInfoDict = {}
		self.mTransData = {}
		
	def PollTransfer(self):
		if len(self.mTransferResList) == 0:
			return
		uidNum = len(self.mTransferResList)
		for i in xrange(uidNum):
			if i < len(self.mTransferResList):
				self.RealTransferResidenceOwner(self.mTransferResList[i])
		
	def OnLoadServerAddonScriptsAfter(self, args):
		self.mPlayerMgr.AddPlayer(residenceConsts.SERVER_PLAYER_PLAYERID, residenceConsts.SERVER_PLAYER_UID)
		
	def OnShowCreateTipsFromClient(self, data):
		entityId = data.get("entityId")
		tips = data.get("tips")
		util.NotifyOneMessage(entityId, tips)

	def OnServerChat(self, args):
		playerId = args['playerId']
		playerGas = self.mPlayerMgr.GetPlayerById(playerId)
		line = args["message"].split(" ")
		command = line[0]
		params = line[1:]
		# print "OnServerChat", command
		# if command == "riding":
		# 	playerGas.CheckAndStopRading()
		# elif command == "pos":
		# 	pos = util.GetEntityPos(playerId)
		# 	print "now at", pos
		# elif command == "h":
		# 	self.TransferResidenceOwner(1, residenceConsts.SERVER_PLAYER_UID,None, {"PlacedBlock":1, "UseDoor":1, "Enter":1})
		# elif command == "g":
		# 	uid = lobbyGameApi.GetPlayerUid(playerId)
		# 	self.TransferResidenceOwner(1, uid,None, {"PlacedBlock": 1, "UseDoor": 1, "Enter": 1})
		# elif command == "item":
		# 	self.DoAddItem(playerId, params[0], params[1], params[2])
		# elif command == "uidsByRes":
		# 	self.QueryResidenceAllOwners(int(params[0]), self.AsyncCallBack)
		# elif command == "resByUid":
		# 	self.QueryAllPlayerResidence(int(params[0]), self.AsyncCallBack)
		# elif command == "checkpos":
		# 	resInfoList = self.FindResidenceByPos(0, (int(params[0]),int(params[1]),int(params[2])))
		# 	if not resInfoList:
		# 		print "FindResidenceByPos find empty!"
		# 	for resInfo in resInfoList:
		# 		print "resInfo =", resInfo
		# elif command == "del":
		# 	self.DeleteResidenceById(int(params[0]))
		# elif command == "1":
		# 	self.NotifyToClient(playerId, "ShowUIFromClient", {"UI":"ResidenceApplyUI", "bool":False})
		# elif command == "2":
		# 	self.NotifyToClient(playerId, "ShowUIFromClient", {"UI":"ResidenceManageUI", "bool":True})
		# elif command == "3":
		# 	self.NotifyToClient(playerId, "ShowUIFromClient", {"UI":"ResidenceTransferUI"})
		# elif command == "4":
		# 	self.NotifyToClient(playerId, "ShowUIFromClient", {"UI":"ResidenceGiveUI"})
		# elif command == "5":
		# 	self.NotifyToClient(playerId, "ShowUIFromClient", {"UI":"ResidenceMyUI"})
		# elif command == "mail_group":
		#	system = serverApi.GetSystem("neteaseAnnounce", "neteaseAnnounceDev")
		#	system.SendMailToGroup("插件群发邮件", "插件群发邮件，检查回调函数", 1609811779)
		# elif command == "mail_send":
		#	system = serverApi.GetSystem("neteaseAnnounce", "neteaseAnnounceDev")
		#	system.SendMailToUser([playerGas.mUid, ], "插件单发邮件", "插件单发邮件，检查回调函数")
		# elif command == "mail_check":
		#	system = serverApi.GetSystem("neteaseAnnounce", "neteaseAnnounceDev")
		#	def checkUnreadCallback(suc, hasUnread):
		#		print "checkUnreadCallback suc={}, hasUnread={}".format(suc, hasUnread)
		#	system.CheckHasUnreadMail(playerGas.mUid, checkUnreadCallback)
		# elif command == "resTop":
		#	minPos = (20, 0, 20)
		#	maxPos = (40, 0, 40)
		#	def callback(suc, reason):
		#		print "resTop callback", suc, reason
		#	self.CreateTopLevelResidence(callback, playerGas.mUid, "测试领地", minPos, maxPos)
		# elif command == "resAdd":
		#	def callback(suc, reason):
		#		print "resAdd callback", suc, reason
		#	self.AddPlayerToResidence(callback, playerGas.mUid, int(params[0]))
		
	def ShowResidenceUI(self, playerId, UIKey = "ResidenceApplyUI"):
		self.NotifyToClient(playerId, "ShowUIFromClient", {"UI": UIKey})

	def AsyncCallBack(self, suc, message, result):
		print "AsyncCallBack suc=%s" % suc
		if suc:
			for one in result:
				print "single :", one
		else:
			print "fail reason =", message

	def DoAddItem(self, playerId, itemId, auxValue, count):
		comp = self.CreateComponent(playerId, 'Minecraft', 'item')
		if not comp:
			return
		try:
			itemId = int(itemId)
			auxValue = int(auxValue)
			count = int(count)
		except:
			return
		slot = self.GetEmptySlot(playerId)
		if slot is None:
			return
		itemDict = {
			'itemId': itemId,
			'count': count,
			'enchantData': [],
			'auxValue': auxValue,
			'customTips': '',
			'extraId': ''
		}
		comp.SpawnItemToPlayerInv(itemDict, playerId, slot)

	def GetEmptySlot(self, playerId):
		comp = self.CreateComponent(playerId, 'Minecraft', 'item')
		for slot in xrange(36):
			item = comp.GetPlayerItem(serverApi.GetMinecraftEnum().ItemPosType.INVENTORY, slot)
			if not item:
				return slot
		return None

	def GetResidenceMgr(self):
		return self.mResidenceMgr

	def GetPlayerMgr(self):
		return self.mPlayerMgr
	# ---------------------------------------------------------------------------------------------
	# 新建顶层领地
	# def CreateTopLevelResidence(self, uid, name, minPos, maxPos, dimension=0, bornPos=None):
	#	return self.mResidenceMgr.TryCreateTopResidence(uid, name, dimension, minPos, maxPos, bornPos)

	# 申请指定数量的预备用领地ID
	# 用于打算使用代码大规模创建领地之前，防止领地创建失败
	def PrepareBatchResidenceId(self, batchNum, cbFunc):
		self.mResidenceMgr.QueryMaxResidenceId(batchNum, cbFunc)

	# 新建顶层领地 -- 新版
	def CreateTopLevelResidence(self, cbFunc, uid, name, minPos, maxPos, dimension=0, bornPos=None):
		self.mResidenceMgr.TryCreateTopResidenceStart(cbFunc, uid, name, dimension, minPos, maxPos, bornPos)

	# 新建子领地
	def CreateSubResidence(self, parentResId, name, minPos, maxPos, bornPos=None):
		return self.mResidenceMgr.TryCreateSubResidence(name, parentResId, minPos, maxPos, bornPos)

	# 删除领地
	def DeleteResidenceById(self, resId):
		return self.mResidenceMgr.TryDeleteResidence(resId)

	# 获取指定维度的指定位置所在的领地列表，从子领地到父领地，按照领地层级从大到小排序
	def FindResidenceByPos(self, dimension, pos):
		return self.mResidenceMgr.FindResidenceByPos(dimension, pos)

	# 获取指定ID领地的在线所有者的uid列表
	def FindResidenceOnlineOwners(self, resId):
		topLevelResId = self.mResidenceMgr.GetTopLevelResidenceIdFromId(resId)
		return self.mPlayerMgr.FindResidenceOnlineOwners(topLevelResId)
	
	# 转移领地领主
	def TransferResidenceOwner(self, resId, toUid, callback = None, needDetleteMainAuth = {"PlacedBlock": 1, "UseDoor": 1, "Enter": 1}):
		if resId not in self.mTransferResList:
			self.mTransferResInfoDict[resId] = toUid, needDetleteMainAuth , callback
			self.mTransferResList.append(resId)
		else:
			self.mResidenceMgr.ShowTipsByUid(toUid, "领地 %s 转让中，稍后再试" % resId)
			self.doCallBack(False, resId, toUid, "领地 %s 转让中，稍后再试" % resId, callback)
	
	def RealTransferResidenceOwner(self, resId):
		toUid, needDetleteMainAuth, callback = self.mTransferResInfoDict[resId]
		#print "TransferResidenceOwner1)", resId, toUid, needDetleteMainAuth
		resInfo = self.mResidenceMgr.mResidenceMap.get(resId, None)
		#print "TransferResidenceOwner2)", resInfo
		if resInfo is None:
			logout.info("Residence %s doesn't exist" % resId)
			self.mResidenceMgr.ShowTipsByUid(toUid, "领地 %s 不存在" % resId)
			self.doCallBack(False, resId, toUid, "领地 %s 不存在" % resId, callback)
			return False
		owners = self.FindResidenceOnlineOwners(resId)
		if len(owners) >= 2:
			logout.info("Residence %s has more than two owners"%resId)
			self.mResidenceMgr.ShowTipsByUid(toUid, "领地 %s 有两个领主"%resId)
			self.doCallBack(False, resId, toUid, "领地 %s 有两个领主"%resId, callback)
			return False
		elif len(owners) <= 0:
			logout.info("Residence %s doesn't have any online owners"%resId)
			self.mResidenceMgr.ShowTipsByUid(toUid, "领地 %s 没有任何在线的领主"%resId)
			self.doCallBack(False, resId, toUid, "领地 %s 没有任何在线的领主"%resId, callback)
			return False
		currentOwnerUid = owners[0]
		if currentOwnerUid == toUid:
			logout.info("Residence %s Cannot transfer the same player" % resId)
			self.mResidenceMgr.ShowTipsByUid(toUid, "领地不能转让给同一个玩家")
			self.mResidenceMgr.ShowTipsByUid(currentOwnerUid, "领地不能转让给同一个玩家")
			self.doCallBack(False, resId, toUid, "Residence %s Cannot transfer the same player" % resId, callback)
			return False
		currentOwner = self.mPlayerMgr.GetPlayerByUid(currentOwnerUid)
		toOwner = self.mPlayerMgr.GetPlayerByUid(toUid)
		if currentOwner is None or toOwner is None:
			logout.info("Residence %s Cannot transfer because player is not online" % resId)
			self.mResidenceMgr.ShowTipsByUid(toUid, "%s或者%s不在线，无法进行领地转让。" % (currentOwnerUid, toUid))
			self.mResidenceMgr.ShowTipsByUid(currentOwnerUid, "%s或者%s不在线，无法进行领地转让。" % (currentOwnerUid, toUid))
			self.doCallBack(False, resId, toUid, "Residence %s Cannot transfer because player is not online" % resId, callback)
			return False
		checkChunkUid = currentOwnerUid if currentOwnerUid != residenceConsts.SERVER_PLAYER_UID else toUid
		checkChunkPlayerId = lobbyGameApi.GetPlayerIdByUid(checkChunkUid)
		#查找chunk的私有箱子
		resMaxPos = resInfo["maxPos"]
		resMinPos = resInfo["minPos"]
		exDataComp = serverApi.CreateComponent(checkChunkPlayerId, "Minecraft", "blockInfo")
		if currentOwnerUid == residenceConsts.SERVER_PLAYER_UID:
			currentOwnerUserName = residenceConsts.SERVER_PLAYER_NICKNAME
		else:
			currentOwnerPlayerId = lobbyGameApi.GetPlayerIdByUid(currentOwnerUid)
			currentOwnerUserName = lobbyGameApi.GetPlayerNickname(currentOwnerPlayerId)
		for x in range(resMinPos[0], resMaxPos[0] + 1):
			for y in range(resMinPos[1], resMaxPos[1] + 1):
				for z in range(resMinPos[2], resMaxPos[2] + 1):
					blockDict = exDataComp.GetBlockNew((x, y, z))
					blockName = blockDict["name"]
					#print "TransferResidenceOwner2)", blockName
					if blockName == "minecraft:air":
						continue
					chestEntity = exDataComp.GetBlockTileEntityWholeCustomData((x, y, z))
					if not chestEntity:
						continue
					if (str(toUid) not in chestEntity["mOwnerList"].keys() and len(chestEntity["mOwnerList"].keys()) > 0) or (str(toUid) in chestEntity["mOwnerList"].keys() and len(chestEntity["mOwnerList"].keys()) > 1):
						logout.info("Residence %s Cannot transfer because there is one private chest" % resId)
						cutIndex = blockName.find(":")
						real_blockName = blockName[cutIndex + 1:]
						self.mResidenceMgr.ShowTipsByUid(toUid, "领地%s中包含%s的私有容器：%s， 无法进行转让。" % (resId, currentOwnerUserName, BLOCK_TEST.get(real_blockName, "容器")))
						self.mResidenceMgr.ShowTipsByUid(currentOwnerUid, "领地%s中包含%s的私有容器：%s，无法进行转让。" % (resId, currentOwnerUserName, BLOCK_TEST.get(real_blockName, "容器")))
						self.doCallBack(False, resId, toUid,"Residence %s Cannot transfer because there is one private chest" % resId, callback)
						return False
		resUidMainAuth = self.mResidenceMgr.mResAuthority.get(resInfo["id"], {})
		for authType, retainType in needDetleteMainAuth.iteritems():
			if retainType == 0:
				for uid, UidMessage in resUidMainAuth.iteritems():
					if UidMessage["authority"].has_key(authType):
						UidMessage["authority"][authType] = False
		if 0 in needDetleteMainAuth.values():
			for uid, UidMessage in resUidMainAuth.iteritems():
				dbApi.UpdateOutPlayerResidenceMainAuthority(self.mResidenceMgr.mServerType, uid, resId, UidMessage["authority"])
		currentOwner.LeaveResidence(resInfo)
		toOwner.JoinResidence(resInfo)
		if toUid == residenceConsts.SERVER_PLAYER_UID:
			userName = residenceConsts.SERVER_PLAYER_NICKNAME
		else:
			toPlayerId = lobbyGameApi.GetPlayerIdByUid(toUid)
			userName = lobbyGameApi.GetPlayerNickname(toPlayerId)
		dbApi.ChangePlayerResidence(self.mResidenceMgr.mServerType, toUid, userName, currentOwnerUid, resId)
		self.mResidenceMgr.ShowTipsByUid(toUid, "领地:%s 成功转让给:%s" % (resId,userName))
		self.mResidenceMgr.ShowTipsByUid(currentOwnerUid, "领地:%s 成功转让给:%s" % (resId,userName))
		self.doCallBack(True, resId, toUid, "Residence %s transfer success from %s to %s" % (resId,currentOwnerUid,toUid), callback)
		return True
	
	def popTransferResId(self, resId):
		if resId in self.mTransferResList:
			self.mTransferResList.remove(resId)
		if resId in self.mTransferResInfoDict:
			del self.mTransferResInfoDict[resId]
	
	def doCallBack(self, suc, resId, toUid, message, callback):
		self.popTransferResId(resId)
		if callback is not None:
			callback(suc, resId, toUid, message)
			
	# 获取某个玩家的领地数量，玩家可以不在线
	def QueryAllPlayerResidence(self, uid, callback):
		dbApi.QueryPlayerResidence(uid, lambda records:self._OnQueryAllPlayerResidence(uid, records, callback))

	def _OnQueryAllPlayerResidence(self, uid, records, callback):
		if not records:
			records = []
		records = util.UnicodeConvert(records)
		result = []
		for one in records:
			resId, name, serverType, resLevel = one
			data = {
				"serverType": serverType,
				"resId": resId,
				"name": name,
				"resLevel": resLevel,
			}
			result.append(data)
		if callable(callback):
			callback(True, "", result)
		return

	# 获取领地的全部所有者，包括不在线的
	def QueryResidenceAllOwners(self, resId, callback):
		resInfo = self.mResidenceMgr.FindResidenceById(resId)
		if not resInfo:
			callback(False, "residence [%s] not exist" % resId, [])
			return
		topLevelResId = self.mResidenceMgr.GetTopLevelResidenceIdFromId(resId)
		import apolloCommon.commonNetgameApi as commonNetgameApi
		dbApi.QueryAllOwnersByResId(commonNetgameApi.GetServerType(), topLevelResId, lambda records:self._OnQueryResidenceAllOwners(resId, records, callback))

	def _OnQueryResidenceAllOwners(self, resId, records, callback):
		if not records:
			records = []
		records = util.UnicodeConvert(records)
		result = []
		for one in records:
			result.append(int(one[0]))
		if callable(callback):
			callback(True, "", result)
		return

	# 获取指定领地当前的特殊权限设置
	def GetAllAuthorityByResidence(self, resId):
		return self.mResidenceMgr.GetAllAuthorityByResidence(resId)

	# 把某个玩家加入某个零级领地的所有者列表中
	def AddPlayerToResidence(self, cbFunc, uid, resId):
		self.mResidenceMgr.TryAddPlayerToResidenceStart(cbFunc, uid, resId)

	# 把某个玩家从某个零级领地的所有者列表中剔除
	def RemovePlayerFromResidence(self, uid, resId):
		return self.mResidenceMgr.TryRemovePlayerFromResidence(uid, resId)

	# 设置指定领地的特殊权限
	def ChangeResidenceAuthority(self, resId, authority):
		return self.mResidenceMgr.TryChangeResidenceAuthority(resId, authority)

	# 获取指定uid的玩家在指定领地的特殊权限设置
	def GetAllAuthorityByUid(self, uid, resId):
		return self.mResidenceMgr.GetAllAuthorityByUid(uid, resId)

	# 获取指定entityId的玩家在指定领地的特殊权限设置
	def GetAllAuthorityByEntityId(self, playerId, resId):
		return self.mResidenceMgr.GetAllAuthorityByEntityId(playerId, resId)

	# 设置指定玩家在指定领地的特殊权限
	def ChangePlayerResidenceAuthority(self, uid, resId, authority):
		return self.mResidenceMgr.TryChangePlayerResidenceAuthority(uid, resId, authority)

	# 设置指定领地的传送点坐标
	def ChangeResidenceTeleportPos(self, resId, pos):
		return self.mResidenceMgr.TryChangeResidenceTeleportPos(resId, pos)

	# 把指定玩家传送到指定领地的传送点
	def TeleportPlayerToRedidence(self, uid, resId):
		return self.mResidenceMgr.TryTeleportPlayerToResidence(resId, uid)

	# 判定一个区域是否在领地内
	def FindOverlapResidenceByArea(self, dimension, minPos, maxPos):
		return self.mResidenceMgr.GetOverlapTopLevelResidenceByArea(dimension, minPos, maxPos)
	# -------------------------------------------------------------------------------------------
	def OnLoginRequest(self, data):
		"""
		客户端登录完成后的第一个事件，通知服务端客户端初始化完毕了
		"""
		playerId = data['playerId']
		player = self.mPlayerMgr.GetPlayerById(playerId)
		if player:
			player.mClientKnock = True
			if player.mResDataQueryed:
				self.SendLoginResponse(player)
		uid = lobbyGameApi.GetPlayerUid(playerId)
		self.mPlayerMgr.SlowAddPlayer(playerId, uid)
		
		self.Init()
		
		if self.mTransData.has_key(uid):
			playerArgs = self.mTransData[uid]
			dim = playerArgs["dim"]
			bornPos = playerArgs["bornPos"]
			dimComp = serverApi.CreateComponent(playerId, "Minecraft", "dimension")
			dimComp.ChangePlayerDimension(dim, tuple(bornPos))
			self.mTransData.pop(uid)
		
	def Init(self):
		# 管理方块在脚本层的监听
		listenBlocks = util.GetModConfByField('cannot_interact_block_list')
		for block in listenBlocks:
			comp = self.CreateComponent(serverApi.GetLevelId(), "Minecraft", "blockUseEventWhiteList")
			comp.AddBlockItemListenForUseEvent(block)

	def SendLoginResponse(self, player):
		responseData = {
			"uid": player.mUid,
			"dimensionId": util.GetEntityDimensionId(player.mPlayerId),
			"modConf": util.GetModJsonConfig(),
		}
		self.NotifyToClient(player.mPlayerId, residenceConsts.LoginResponseEvent, responseData)
		player.RefreshResidence()

	def SyncResidenceData(self, player, needSyncList):
		responseData = {
			"playerId": player.mPlayerId,
			"needSyncList": needSyncList,
		}
		self.NotifyToClient(player.mPlayerId, residenceConsts.SyncResidenceDataEvent, responseData)

	def SyncPersonalData(self, player, resDataList, authorityDataList, delResidenceList, delAuthorityList):
		responseData = {
			"playerId": player.mPlayerId,
			"resDataList": resDataList,
			"authorityDataList": authorityDataList,
			"delResidenceList": delResidenceList,
			"delAuthorityList": delAuthorityList,
		}
		self.NotifyToClient(player.mPlayerId, residenceConsts.SyncPersonalDataEvent, responseData)

	def RegisterLaterWork(self, func):
		self.mLaterWork.append(func)

	def OnScriptTickServer(self):
		if self.mLaterWork:
			for func in self.mLaterWork:
				func()
			self.mLaterWork = []
		if self.mPlayerMgr:
			self.mPlayerMgr.OnScriptTickServer()

	def OnAddServerPlayer(self, data):
		'''
		玩家进入服务器
		'''
		playerId = data['id']
		uid = data['uid']
		self.mPlayerMgr.AddPlayer(playerId, uid)
		transferParam = data.get("transferParam", "")
		if transferParam != "":
			import json
			try:
				self.mTransData[uid] = json.loads(transferParam)
			except Exception as e:
				pass
		# posComp = self.CreateComponent(playerId, "Minecraft", "pos")
		# posComp.SetPos((1395, 72, 35.5))

	def OnDelerverPlayer(self, data):
		'''
		玩家退出服务器
		'''
		playerId = data['id']
		self.mPlayerMgr.DelPlayer(playerId)

	def Destroy(self):
		print 'Destroy ResidenceServerSys'
		self.UnListenForEvent(residenceConsts.ModNameSpace, residenceConsts.ClientSystemName,
									residenceConsts.LoginRequestEvent, self, self.OnLoginRequest)
		self.UnListenForEvent(serverApi.GetEngineNamespace(), serverApi.GetEngineSystemName(), "AddServerPlayerEvent",
							self, self.OnAddServerPlayer)
		self.mPlayerMgr.Destroy()
		self.mResidenceMgr.Destroy()
		dbApi.Destroy()
		util.Destroy()
