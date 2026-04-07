# -*- coding: utf-8 -*-
import json
import time
import neteaseResidenceScript.dbApi as dbApi
import neteaseResidenceScript.util as util
import apolloCommon.commonNetgameApi as commonNetgameApi
import neteaseResidenceScript.residenceConsts as residenceConsts
import neteaseResidenceScript.residenceBaseMgr as residenceBaseMgr
import lobbyGame.netgameApi as lobbyGameApi
import server.extraServerApi as serverApi

needCheckFieldData = {
	"can_flow_into": (
		lobbyGameApi.SetForbidFlowField,
		lobbyGameApi.DelForbidFlowField,
	),
	"can_dragon_egg_teleport_into": (
		lobbyGameApi.SetForbidDragonEggTeleportField,
		lobbyGameApi.DelForbidDragonEggTeleportField,
	),
}

class ResidenceGasMgr(residenceBaseMgr.ResidenceBaseMgr):
	"""
	服务端领地管理类
	"""
	def __init__(self, system):
		residenceBaseMgr.ResidenceBaseMgr.__init__(self, system)
		self.mSystem.ListenForEvent(residenceConsts.ModNameSpace, residenceConsts.MasterSystemName,
									residenceConsts.QueryServerResidenceEvent, self, self.OnQueryServerResidence)
		self.mSystem.ListenForEvent(serverApi.GetEngineNamespace(), serverApi.GetEngineSystemName(),
		                    'LoadServerAddonScriptsAfter', self, self.OnLoadServerAddonScriptsAfter)
		self.mSystem.ListenForEvent(residenceConsts.ModNameSpace, residenceConsts.MasterSystemName,
									residenceConsts.SetPlayerResidenceEvent, self, self.OnSetPlayerResidence)
		self.mSystem.ListenForEvent(residenceConsts.ModNameSpace, residenceConsts.MasterSystemName,
									residenceConsts.HttpDelResidenceEvent, self, self.OnHttpDelResidence)
		self.mSystem.ListenForEvent(residenceConsts.ModNameSpace, residenceConsts.MasterSystemName,
									residenceConsts.AddPlayerToResidenceEvent, self, self.OnHttpAddPlayerToResidence)
		self.mSystem.ListenForEvent(residenceConsts.ModNameSpace, residenceConsts.MasterSystemName,
									residenceConsts.RemovePlayerFromResidenceEvent, self, self.OnHttpRemovePlayerFromResidence)
		self.mSystem.ListenForEvent(residenceConsts.ModNameSpace, residenceConsts.MasterSystemName,
									residenceConsts.ChangeResidenceAuthorityEvent, self, self.OnHttpChangeResidenceAuthority)
		self.mSystem.ListenForEvent(residenceConsts.ModNameSpace, residenceConsts.MasterSystemName,
									residenceConsts.ChangePlayerResidenceAuthorityEvent, self, self.OnHttpChangePlayerResidenceAuthority)
		self.mSystem.ListenForEvent(residenceConsts.ModNameSpace, residenceConsts.MasterSystemName,
									residenceConsts.ChangeResidenceBornPosEvent, self, self.OnHttpChangeResidenceBornPos)
		self.mSystem.ListenForEvent(residenceConsts.ModNameSpace, residenceConsts.MasterSystemName,
									residenceConsts.ReleasePlayerResidenceLockEvent, self, self.OnHttpReleasePlayerResidenceLock)
		self.mSystem.ListenForEvent(residenceConsts.ModNameSpace, residenceConsts.ClientSystemName,
		                            "CreateParentResidenceFromClient", self, self.OnCreateParentResidenceFromClient)
		self.mSystem.ListenForEvent(residenceConsts.ModNameSpace, residenceConsts.ClientSystemName,
		                            "ChangeResidencePosFromClient", self, self.OnChangeResidencePosFromClient)
		self.mSystem.ListenForEvent(residenceConsts.ModNameSpace, residenceConsts.ClientSystemName,
		                            "CreateSubResidenceFromClient", self, self.OnCreateSubResidenceFromClient)
		self.mSystem.ListenForEvent(residenceConsts.ModNameSpace, residenceConsts.ClientSystemName,"CheckPlayerResidenceFromClient", self, self.OnCheckPlayerResidenceFromClient)
		self.mSystem.ListenForEvent(residenceConsts.ModNameSpace, residenceConsts.ClientSystemName,"CheckPlayerResidenceByIdFromClient", self, self.OnCheckPlayerResidenceByIdFromClient)
		self.mSystem.ListenForEvent(residenceConsts.ModNameSpace, residenceConsts.ClientSystemName,"CheckCanEnterPlayerResidenceByIdFromClient", self, self.OnCheckCanEnterPlayerResidenceByIdFromClient)
		self.mSystem.ListenForEvent(residenceConsts.ModNameSpace, residenceConsts.ClientSystemName,"ApplicationResidenceFromClient", self, self.OnApplicationResidenceFromClient)
		self.mSystem.ListenForEvent(residenceConsts.ModNameSpace, residenceConsts.ClientSystemName,"applicatorAcceptFromClientEvent", self, self.OnApplicatorAcceptFromClientEvent)
		self.mSystem.ListenForEvent(residenceConsts.ModNameSpace, residenceConsts.ClientSystemName,"applicatorRefuseFromClientEvent", self, self.OnApplicatorRefuseFromClientEvent)
		self.mSystem.ListenForEvent(residenceConsts.ModNameSpace, residenceConsts.ClientSystemName,"ChangeAuthFromClientEvent", self, self.OnChangeAuthFromClientEvent)
		self.mSystem.ListenForEvent(residenceConsts.ModNameSpace, residenceConsts.ClientSystemName,"GiveSendFromClientEvent", self, self.OnGiveSendFromClientEvent)
		self.mSystem.ListenForEvent(residenceConsts.ModNameSpace, residenceConsts.ClientSystemName,"TransferToResidenceFromClient", self, self.OnTransferToResidenceFromClient)
		self.mSystem.ListenForEvent(residenceConsts.ModNameSpace, residenceConsts.ClientSystemName,"DeleteAuthFromClientEvent", self, self.OnDeleteAuthFromClientEvent)
		self.mSystem.ListenForEvent(residenceConsts.ModNameSpace, residenceConsts.ClientSystemName,"TransferHasReadFromClientEvent", self, self.OnTransferHasReadFromClientEvent)
		self.mSystem.ListenForEvent(residenceConsts.ModNameSpace, residenceConsts.ClientSystemName,"ApplicatorHasReadFromClientEvent", self, self.OnApplicatorHasReadFromClientEvent)
		self.mSystem.ListenForEvent(residenceConsts.ModNameSpace, residenceConsts.ClientSystemName,"ShowTipsFromClientEvent", self, self.OnShowTipsFromClientEvent)
		
		self.mServerType = commonNetgameApi.GetServerType()
		if isinstance(self.mServerType, unicode):
			self.mServerType = self.mServerType.encode("utf-8")
		# 可用的领地ID，需要从数据库申请
		self.mUsableResIds = []
		self.mIsQueryId = False
		comp = serverApi.CreateComponent(serverApi.GetLevelId(), "Minecraft", "game")
		self.mQueryIdTimer = comp.AddRepeatedTimer(residenceConsts.QueryCheckTime, self.CheckAndAskforResId)
		self.mResidenceInfoLock = set()
		self.LoadAllResidenceArea()
		self.mLevelId = serverApi.GetLevelId()
		# self.OutputResidenceGridData()
		self.mResApplication = {}
		self.mResAuthority = {}
		self.mDefaultAuth = {}
		self.mResBornPos = {}
		self.mResServerType = {}
		self.mResDim = {}

	def CheckAndAskforResId(self):
		if self.mIsQueryId:
			return
		if len(self.mUsableResIds) >= residenceConsts.QueryResIdLimitMin:
			return
		self.mIsQueryId = True
		self.QueryMaxResidenceId(residenceConsts.QueryResIdLimitOnce)
	
	def QueryMaxResidenceId(self, queryNum, cbFunc=None):
		def queryCallback(suc, usedResId, askIndex):
			# 数据库调用失败，直接结束申请流程，等待下次timer触发新的申请流程
			if not suc:
				self.mIsQueryId = False
				if cbFunc and callable(cbFunc):
					cbFunc(False, [])
				return
			# 数据库是空的，说明是首次申请
			if usedResId is None or askIndex is None:
				self.InsertMaxResidenceId(queryNum, 0, 0, cbFunc)
			else:
				self.InsertMaxResidenceId(queryNum, usedResId, askIndex, cbFunc)
		dbApi.QueryMaxUsedResidenceId(queryCallback)
	
	def InsertMaxResidenceId(self, queryNum, usedResId, askIndex, cbFunc):
		askingResIds = []
		usedResIdNew = usedResId+queryNum
		for idx in xrange(usedResId+1, usedResIdNew+1):
			askingResIds.append(idx)
		def insertCallback(suc):
			# 数据库插入失败，直接结束申请流程，等待下次timer触发新的申请流程
			if not suc:
				self.mIsQueryId = False
				if cbFunc and callable(cbFunc):
					cbFunc(False, [])
				return
			self.OnAskforResIdSuc(askingResIds, cbFunc)
		dbApi.InsertMaxUsedResidenceId(usedResIdNew, askIndex, insertCallback)
	
	def OnAskforResIdSuc(self, askingResIds, cbFunc):
		print "OnAskforResIdSuc askingResIds={}".format(askingResIds)
		self.mUsableResIds.extend(askingResIds)
		self.mIsQueryId = False
		if cbFunc and callable(cbFunc):
			cbFunc(True, askingResIds)
		
	def OnShowTipsFromClientEvent(self, args):
		"""
		显示提示信息
		"""
		playerId = args.get("playerId")
		message = args.get("message")
		self.ShowTips(playerId, message)
		
		
	def ShowTips(self, playerId, message):
		"""
		显示提示信息，根据是否有插件，有不同的提示方式
		"""
		alertSystem = serverApi.GetSystem("neteaseAlert", "neteaseAlertDev")
		if alertSystem:
			alertSystem.Alert(playerId, message, 2, 0.5, 0.8)
		else:
			self.ShowCreateTips(message, playerId)
			
	def ShowTipsByUid(self, playerUid, message):
		"""
		显示提示信息
		"""
		if playerUid == residenceConsts.SERVER_PLAYER_UID:
			return
		playerId = lobbyGameApi.GetPlayerIdByUid(playerUid)
		self.ShowTips(playerId, message)
		
		
	def OnChangeResidencePosFromClient(self, args):
		"""
		修改领地占据的区域
		"""
		print "OnChangeResidencePosFromClient", args
		playerId = args.get("playerId")
		playerUid = lobbyGameApi.GetPlayerUid(playerId)
		minPos = args.get("minPos")
		maxPos = args.get("maxPos")
		dimension = args.get("dimension")
		resId = args.get("resId")
		self.real_ChangeResidencePos(playerId, playerUid, minPos, maxPos, resId, dimension)
			
	def real_ChangeResidencePos(self, playerId, playerUid, minPos, maxPos, resId, dimension):
		"""
		修改领地占据的区域
		"""
		suc, reason, tips = self.TryChangeResidencePos(playerUid, resId, dimension, minPos, maxPos)
		print "OnCreateParentResidenceFromClient2", tips
		# comp = serverApi.CreateComponent(playerId, "Minecraft", "game")
		# comp.SetNotifyMsg(tips)
		self.ShowCreateTips(tips, playerId)
		playerUid = lobbyGameApi.GetPlayerUid(playerId)
		playerName = lobbyGameApi.GetPlayerNickname(playerId)
		# 修改之后重新查询一次，刷新领地信息
		def QueryResidenceByUidCb(playerUid, resData):
			print "QueryResidenceByUidCb", playerUid, resData
			resList = []
			for oneResData in resData:
				if oneResData:
					resId = oneResData[0]
					resName = oneResData[1]
					serverType = oneResData[2]
					bornPos = oneResData[5]
					area = oneResData[4]
					minPos, maxPos = util.AreaStringToPos(area)
					resList.append(
						{"resId": resId, "resName": resName, "bornPos": util.StringToList(bornPos), "minPos": minPos,
						 "maxPos": maxPos})
					self.mResBornPos[resId] = util.StringToList(bornPos)
					self.mResServerType[resId] = serverType
			if len(resList) > 0:
				self.mSystem.NotifyToClient(playerId, "SearchResidenceResultByIdFromServerEvent",
				                            {"playerUid": playerUid, "resList": resList, "playerName": playerName})
		
		dbApi.QueryResidenceByUid(playerUid, lambda resData: QueryResidenceByUidCb(playerUid, resData))
		
	def OnTransferHasReadFromClientEvent(self, args):
		"""
		设置领地传送申请信息为已读
		"""
		playerId = args.get("playerId")
		playerUid = lobbyGameApi.GetPlayerUid(playerId)
		dbApi.DeleteTransferUnread(playerUid)
	
	def OnApplicatorHasReadFromClientEvent(self, args):
		"""
		设置领地权限申请信息为已读
		"""
		playerId = args.get("playerId")
		resId = args.get("resId")
		playerUid = lobbyGameApi.GetPlayerUid(playerId)
		dbApi.DeleteApplicationUnread(playerUid,resId)
		
	def OnDeleteAuthFromClientEvent(self, args):
		"""
		删除领地外部玩家特殊权限设置
		"""
		uid = args.get("uid")
		resId = args.get("resId")
		clientId = args.get("clientId")
		self.TryDeletePlayerResidenceAuthority(clientId, uid, resId)
		
	def OnTransferToResidenceFromClient(self, args):
		"""
		传送到领地出生点
		"""
		playerId = args.get("playerId")
		resId = args.get("resId")
		bornPos = self.mResBornPos.get(resId)
		serverType = self.mResServerType.get(resId)
		import apolloCommon.commonNetgameApi as commonNetgameApi
		localServerType = commonNetgameApi.GetServerType()  # 结果是:"gameBattleA"
		dim = self.mResDim.get(resId)
		print "OnTransferToResidenceFromClient", args, bornPos
		if bornPos:
			if localServerType == serverType:
				dimComp = serverApi.CreateComponent(playerId, "Minecraft", "dimension")
				print "dimension", dim
				dimComp.ChangePlayerDimension(dim, tuple(bornPos))
			else:
				import lobbyGame.netgameApi as lobbyGameApi
				transData = {'bornPos': bornPos, 'dim': dim}
				lobbyGameApi.TransferToOtherServer(playerId, str(serverType), json.dumps(transData))
		
	def OnChangeAuthFromClientEvent(self, args):
		"""
		修改指定外部玩家在指定领地的简化版权限（即放置/摧毁方块、使用门/箱子、进入领地）
		"""
		resId = args.get("resId")
		uid = args.get("uid")
		changeAuth = args.get("changeAuth")
		playerId = args.get("playerId")
		userName = args.get("userName")
		if self.mResAuthority.has_key(resId) == False:
			return
		if self.mResAuthority[resId].has_key(uid) == False:
			return
		print "self.mResAuthority", self.mResAuthority
		self.mResAuthority[resId][uid]["authority"][changeAuth] = not self.mResAuthority[resId][uid]["authority"][changeAuth]
		args["state"] = self.mResAuthority[resId][uid]["authority"][changeAuth]
		self.mSystem.NotifyToClient(playerId, "ChangeAuthFromServerEvent", args)
		if True not in self.mResAuthority[resId][uid]["authority"].values():
			self.mSystem.NotifyToClient(playerId, "SureDeleteAuthFromServerEvent", args)
		self.ServerTryChangePlayerResidenceAuthority(uid, resId, {"can_other_player_enter":args["state"]}, self.mResAuthority[resId][uid]["authority"])
		dbApi.UpdateOutPlayerResidenceMainAuthority(self.mServerType, uid, resId, self.mResAuthority[resId][uid]["authority"])
		
	
		
	def OnApplicatorAcceptFromClientEvent(self, args):
		"""
		领地所有者通过外部玩家的权限申请
		"""
		applicatorUid = args.get("applicatorUid")
		resId = args.get("resId")
		playerId = args.get("playerId")
		authority = args.get("authority")
		applicatorPlayerId = lobbyGameApi.GetPlayerIdByUid(applicatorUid)
		if authority.get("Enter", True) == True:
			if applicatorPlayerId != "":
				self.mSystem.NotifyToClient(applicatorPlayerId, "updateNewEnterAuthFromServerEvent", args)
			else:
				# 不在线记录一下未读
				dbApi.InSertTransferUnread(applicatorUid, resId)
				
		print "OnApplicatorAcceptFromClientEvent", args
		def OnRealAcceptApplication(data):
			if data is not None:
				if self.mResApplication.has_key(resId):
					if self.mResApplication[resId].has_key(applicatorUid):
						oneApplication = self.mResApplication[resId][applicatorUid]
						oneApplication.pop("applicationMessage")
						if self.mResApplication.has_key(resId) == False:
							self.mResApplication[resId] = {}
						self.mResApplication[resId][applicatorUid] = oneApplication
						self.mResApplication[resId].pop(applicatorUid)
						self.mSystem.NotifyToClient(playerId, "RemoveApplicationFromServerEvent", args)
						
						if self.mResAuthority.has_key(resId) == False:
							self.mResAuthority[resId] = {}
						self.mResAuthority[resId][applicatorUid] = oneApplication
						self.mSystem.NotifyToClient(playerId, "UpdateAuthorityFromServerEvent", {resId: {applicatorUid: oneApplication}})
						dbApi.InsertOutPlayerResidenceMainAuthority(self.mServerType, applicatorUid, resId, oneApplication["authority"], oneApplication["username"])
		dbApi.DeleteOutPlayerResidenceApplication(applicatorUid, resId, OnRealAcceptApplication)
		

	def OnApplicatorRefuseFromClientEvent(self, args):
		"""
		领地所有者拒绝外部玩家的权限申请
		"""
		applicatorUid = args.get("applicatorUid")
		resId = args.get("resId")
		playerId = args.get("playerId")
		def OnRealAcceptApplication(args):
			if self.mResApplication.has_key(resId):
				if self.mResApplication[resId].has_key(applicatorUid):
					self.mResApplication[resId].pop(applicatorUid)
					self.mSystem.NotifyToClient(playerId, "RemoveApplicationFromServerEvent", args)
		dbApi.DeleteOutPlayerResidenceApplication(applicatorUid, resId, OnRealAcceptApplication)
	
	def OnLoadServerAddonScriptsAfter(self, args):
		self.OnLoadDefaultAuth()
		self.DoQueryAllApplication()
		self.DoQueryAllAuthority()
		
	def OnLoadDefaultAuth(self):
		"""
		加载mod.json中的默认权限配置
		"""
		for key, value in residenceConsts.AuthorityForPlayer.iteritems():
			if value:
				if util.GetModJsonConfig().get(key) is not None:
					if residenceConsts.AuthorityValueType.get(key) != bool:
						self.mDefaultAuth[key] = {"set":util.GetModJsonConfig().get(key)}
					else:
						self.mDefaultAuth[key] = util.GetModJsonConfig().get(key)
		
	def DoQueryAllApplication(self):
		"""
		加载尚未处理的外部玩家的领地权限申请
		"""
		checkData = dbApi.QueryAllOutPlayerResidenceApplication(self.mServerType)
		for cData in checkData:
			if cData:
				uid = cData[1]
				resId = cData[2]
				applicationMessage = cData[3]
				authority = json.loads(cData[4])
				userName = cData[5]
				if self.mResApplication.has_key(resId) == False:
					self.mResApplication[resId] = {}
				self.mResApplication[resId][uid] = {"uid": uid, "username": userName, "authority": authority,
				                                    "applicationMessage": applicationMessage}
				
	def DoQueryAllAuthority(self):
		"""
		加载外部玩家的领地权限信息
		"""
		checkData = dbApi.QueryAllOutPlayerResidenceMainAuthority(self.mServerType)
		for cData in checkData:
			if cData:
				uid = cData[1]
				resId = cData[2]
				mainAuthority = json.loads(cData[3])
				userName = cData[4]
				if self.mResAuthority.has_key(resId) == False:
					self.mResAuthority[resId] = {}
				self.mResAuthority[resId][uid] = {"uid": uid, "username": userName, "authority": mainAuthority}
				# self.mSystem.NotifyToClient(playerId, "UpdateAuthorityFromServerEvent",
				#                             {resId: {applicatorUid: oneApplication}})
	
	
	def OnCheckPlayerResidenceByIdFromClient(self, args):
		'''
		查询指定玩家拥有的领地
		'''
		playerId = args.get("playerId")
		playerUid = lobbyGameApi.GetPlayerUid(playerId)
		playerName = lobbyGameApi.GetPlayerNickname(playerId)
		def QueryResidenceByUidCb(playerUid, resData):
			print "QueryResidenceByUidCb", playerUid, resData
			resList = []
			for oneResData in resData:
				if oneResData:
					resId = oneResData[0]
					resName = oneResData[1]
					serverType = oneResData[2]
					bornPos = oneResData[5]
					area = oneResData[4]
					dim = oneResData[3]
					minPos, maxPos = util.AreaStringToPos(area)
					resList.append({"resId":resId, "resName":resName, "bornPos":util.StringToList(bornPos), "minPos":minPos, "maxPos":maxPos})
					self.mResBornPos[resId] = util.StringToList(bornPos)
					self.mResServerType[resId] = serverType
					self.mResDim[resId] = dim
			self.mSystem.NotifyToClient(playerId, "SearchResidenceResultByIdFromServerEvent", {"playerUid":playerUid,"resList":resList, "playerName":playerName})
		dbApi.QueryResidenceByUid(playerUid, lambda resData: QueryResidenceByUidCb(playerUid, resData))
		
	def OnCheckCanEnterPlayerResidenceByIdFromClient(self, args):
		'''
		查询指定玩家拥有外部权限的领地以及对应的所有者信息
		'''
		playerId = args.get("playerId")
		playerUid = lobbyGameApi.GetPlayerUid(playerId)
		playerName = lobbyGameApi.GetPlayerNickname(playerId)
		def QueryPlayerResidenceMainAuthByUidCb(playerUid, resData):
			print "QueryPlayerResidenceMainAuthByUidCb", playerUid, resData
			resList = []
			for oneResData in resData:
				if oneResData:
					resId = oneResData[0]
					resName = oneResData[1]
					serverType = oneResData[2]
					dim = oneResData[3]
					bornPos = oneResData[5]
					resUserName = oneResData[6]
					mainAuth =  json.loads(oneResData[7])
					if mainAuth.get("Enter") == True:
						area = oneResData[4]
						minPos, maxPos = util.AreaStringToPos(area)
						resList.append(
							{"resId": resId, "resName": resName, "resUserName":resUserName, "bornPos": util.StringToList(bornPos), "minPos": minPos,
							 "maxPos": maxPos})
						self.mResBornPos[resId] = util.StringToList(bornPos)
						self.mResServerType[resId] = serverType
						self.mResDim[resId] = dim
			self.mSystem.NotifyToClient(playerId, "SearchCanEnterPlayerResidenceByIdFromServerEvent",
				                            {"playerUid": playerUid, "resList": resList, "playerName": playerName})
		
		dbApi.QueryPlayerResidenceMainAuthByUid(playerUid, lambda resData: QueryPlayerResidenceMainAuthByUidCb(playerUid, resData))
	
	def OnCheckPlayerResidenceFromClient(self, args):
		'''
		查询指定玩家拥有的领地（根据玩家昵称）
		'''
		print "OnCheckPlayerResidenceFromClient", args
		playerName = args.get("applicatorName")
		playerId = args.get("playerId")
		def QueryResidenceByUidCb(playerUid, resData):
			print "QueryResidenceByUidCb", playerUid, resData
			resList = []
			for oneResData in resData:
				if oneResData:
					resId = oneResData[0]
					resName = oneResData[1]
					resList.append({"resId":resId, "resName":resName})
			self.mSystem.NotifyToClient(playerId, "SearchResidenceResultFromServerEvent", {"playerUid":playerUid,"resList":resList})
				
		def QueryPlayerDataCb(playerData):
			print "QueryPlayerDataCb", playerData
			if playerData is None:
				return
			playerUid = playerData.get("playerUid")
			dbApi.QueryResidenceByUid(playerUid, lambda resData:QueryResidenceByUidCb(playerUid, resData))
		self.mSystem.mPlayerMgr.QueryPlayerDataUserName(playerName, True, QueryPlayerDataCb)
		
	def OnGiveSendFromClientEvent(self, args):
		'''
		给于指定的外部玩家（基于昵称）指定领地的特定权限
		'''
		playerId = args.get("playerId")
		giverName = args.get("giverName")
		resId = args.get("chosenResId")
		authority = args.get("authorityState")
		
		def QueryResidenceByUidCb(playerUid):
			
			suc, reason, message = self.ServerTryChangePlayerResidenceAuthority(playerUid, resId, self.mDefaultAuth, authority)
			self.ShowTips(playerId, message)
		def QueryPlayerDataCb(playerData):
			print "QueryPlayerDataCb", playerData
			if playerData is None:
				#self.mSystem.NotifyToClient(playerId, "GiveSendPlayerResultFromServerEvent", {"message":"你输入的玩家不存在！"})
				self.ShowTips(playerId, "你输入的玩家不存在！")
				return
			playerUid = playerData.get("playerUid")
			dbApi.QueryResidenceByUid(playerUid, QueryResidenceByUidCb(playerUid))
		self.mSystem.mPlayerMgr.QueryPlayerDataUserName(giverName, True, QueryPlayerDataCb)
		
		
	def OnApplicationResidenceFromClient(self, args):
		'''
		外部玩家请求申请指定领地的特定权限
		'''
		resId = args.get("chosenResId")
		playerId = args.get("playerId")
		playerUid = lobbyGameApi.GetPlayerUid(playerId)
		userName = lobbyGameApi.GetPlayerNickname(playerId)
		authority = args.get("authorityState")
		applicationMessage = args.get("applicationMessage")
		isOk = commonNetgameApi.CheckNameValid(applicationMessage)
		if not isOk:
			self.ShowTips(playerId, "申请语含敏感词")
			return
		serverType = commonNetgameApi.GetServerType()
		if self.mResApplication.has_key(resId) and self.mResApplication[resId].has_key(playerUid):
			self.ShowTips(playerId, "你已经成功申请")
			return
		dbApi.InsertOutPlayerResidenceApplication(serverType, playerUid, resId, applicationMessage, userName, authority, lambda args :self.OnInsertApplication(playerId, playerUid, authority, applicationMessage, userName, resId))
		
	def OnInsertApplication(self, playerId, uid, authority, applicationMessage, userName, resId):
		if self.mResApplication.has_key(resId) == False:
			self.mResApplication[resId] = {}
		self.mResApplication[resId][uid] = {"uid":uid, "username":userName, "authority":authority, "applicationMessage":applicationMessage}
		#self.mSystem.NotifyToClient(playerId, "ShowTipsFromServerEvent", {"message": "你已成功申请！"})
		self.ShowTips(playerId, "你已经成功申请")
		def QueryPlayerResidenceByResIdCb(records):
			playerUid = -1
			for record in records:
				if record:
					playerUid = record[4]
			if playerUid > 0:
				playerId = lobbyGameApi.GetPlayerIdByUid(playerUid)
				if playerId != "":
					myApplication = {}
					myApplication[resId] = {}
					myApplication[resId][uid] = {"uid":uid, "username":userName, "authority":authority, "applicationMessage":applicationMessage}
					self.mSystem.NotifyToClient(playerId, "UpdateApplicationFromServerEvent", myApplication)
					self.mSystem.NotifyToClient(playerId, "UpdateNewApplicationFromServerEvent", {"resId":resId, "applicatorUid":uid})
				else:
					dbApi.InSertApplicationUnread(playerUid, resId, uid)
		dbApi.QueryPlayerResidenceByResId([resId],QueryPlayerResidenceByResIdCb)
	
	# def OnAgreeResidenceApplicationFromClient(self, args):
	# 	'''
	# 	同意领地
	# 	'''
	# 	resId = args.get("resId")
	# 	playerId = args.get("playerId")
	# 	playerUid = lobbyGameApi.GetPlayerUid(playerId)
	# 	authority = args.get("authority")
	# 	# serverType = commonNetgameApi.GetServerType()
	# 	dbApi.DeleteOutPlayerResidenceApplication(playerUid, resId, lambda uid, resId, authority: self.OnDeleteApplication(playerUid, resId, authority))
	#
	# def OnDeleteApplication(self, uid, resId, authority):
	# 	if self.mResApplication.has_key(resId) == False:
	# 		self.mResApplication[resId] = {}
	# 	if self.mResApplication[resId].has_key(uid):
	# 		self.mResApplication[resId].pop(uid)
	# 	self.TryChangePlayerResidenceAuthority(uid, resId, authority)
		
	def OnCheckMyRes(self, args):
		'''
		查询指定玩家的全部领地
		'''
		playerId = args.get("playerId")
		playerUid = lobbyGameApi.GetPlayerUid(playerId)
		def QueryResidenceByUidCb(resData):
			self.mSystem.NotifyToClient(playerId, "SearchResidenceFromServerEvent", {"playerUid":playerUid, "resData":resData})
		dbApi.QueryResidenceByUid(playerUid, QueryResidenceByUidCb)
		
	def OnCheckApplicationByResId(self, args):
		'''
		查询指定领地的尚未处理的外部玩家权限申请
		'''
		resId = args.get("resId")
		playerId = args.get("playerId")
		def QueryOutPlayerResidenceApplicationCb(checkData):
			for cData in checkData:
				if cData:
					uid = cData[1]
					authority = cData[3]
					self.mResApplication[resId][uid] = authority
			self.mServerType.NotifyToClient(playerId, "CheckResidenceApplicationFromServerEvent", {"application":self.mResApplication[resId]})
		if self.mResApplication.has_key(resId) and self.mResApplication[resId]:
			self.mServerType.NotifyToClient(playerId, "CheckResidenceApplicationFromServerEvent", {"application":self.mResApplication[resId]})
		else:
			dbApi.QueryOutPlayerResidenceApplication(resId, self.mServerType, QueryOutPlayerResidenceApplicationCb)
		
	def OnCheckCanTransferResidence(self, args):
		"""
		已废弃函数
		"""
		playerId = args.get("playerId")
		playerUid = lobbyGameApi.GetPlayerUid(playerId)
		def QueryPlayerResidenceByResIdCb(records):
			residenceDataList = []
			for record in records:
				if record:
					residenceDataList.append(record)
			self.mSystem.NotifyToClient(playerId, "CheckCanTransferResidenceFromServerEvent", {"residenceDataList":residenceDataList})
		def QueryPlayerResidenceAuthorityCallback(records):
			resIdList = []
			for record in records:
				resId = record[2]
				authority = record[3]
				json_authority = json.loads(authority)
				if json_authority.has_key("can_other_player_enter"):
					resIdList.append(resId)
			dbApi.QueryPlayerResidenceByResId(resIdList,QueryPlayerResidenceByResIdCb)
		dbApi.QueryPlayerResidenceAuthority(playerUid, self.mServerType,
		                                    lambda records: QueryPlayerResidenceAuthorityCallback(records))
	
	def OnCreateParentResidenceFromClient(self, data):
		"""
		新创建顶层领地
		"""
		print "OnCreateParentResidenceFromClient", data
		playerId = data.get("playerId")
		playerUid = lobbyGameApi.GetPlayerUid(playerId)
		name =  data['name']
		dimension = data.get("dimension", 0)
		bornPos = data.get("bornPos")
		minPos , maxPos = data['minPos'], data['maxPos']
		def ServerTryCreateTopResidenceCallback(suc, reason):
			if reason:
				self.ShowCreateTips(reason, playerId)
			if suc:
				self.RefreshPlayerResidenceData(playerId)
		self.ServerTryCreateTopResidenceStart(ServerTryCreateTopResidenceCallback, playerUid, name, dimension, minPos, maxPos, bornPos)
	
	def RefreshPlayerResidenceData(self, playerId):
		playerUid = lobbyGameApi.GetPlayerUid(playerId)
		playerName = lobbyGameApi.GetPlayerNickname(playerId)
		
		def QueryResidenceByUidCb(playerUid, resData):
			print "QueryResidenceByUidCb", playerUid, resData
			resList = []
			for oneResData in resData:
				if oneResData:
					resId = oneResData[0]
					resName = oneResData[1]
					serverType = oneResData[2]
					bornPos = oneResData[5]
					area = oneResData[4]
					dim = oneResData[3]
					minPos, maxPos = util.AreaStringToPos(area)
					resList.append(
						{"resId": resId, "resName": resName, "bornPos": util.StringToList(bornPos), "minPos": minPos,
						 "maxPos": maxPos})
					self.mResBornPos[resId] = util.StringToList(bornPos)
					self.mResServerType[resId] = serverType
					self.mResDim[resId] = dim
			if len(resList) > 0:
				self.mSystem.NotifyToClient(playerId, "SearchResidenceResultByIdFromServerEvent",
				                            {"playerUid": playerUid, "resList": resList, "playerName": playerName})
		
		dbApi.QueryResidenceByUid(playerUid, lambda resData: QueryResidenceByUidCb(playerUid, resData))
	
	def OnCreateSubResidenceFromClient(self, data):
		"""
		基于指定领地创建子领地
		"""
		print "OnCreateSubResidenceFromClient", data
		parentId = data.get("parentId")
		playerId = data.get("playerId")
		suc, reason, tips = self.ServerTryCreateSubResidence(data['name'], parentId, data['minPos'], data['maxPos'],
		                                                     data.get("bornPos", None))
		self.ShowCreateTips(tips, playerId)
		
	def ShowCreateTips(self, tips, entityId):
		util.NotifyOneMessage(entityId, tips)

	def LoadAllResidenceArea(self):
		'''
		加载本服玩家领地信息
		'''
		serverType = commonNetgameApi.GetServerType()
		residenceRecords = dbApi.QueryAllServerResidence(serverType)
		for record in residenceRecords:
			record = util.UnicodeConvert(record)
			resId = record[0]
			resInfo = {
				"id": resId,
				"serverType": serverType,
				"dimension": record[1],
				"name": record[3],
				"resLevel": record[4],
				"parentResId": record[5],
				"version": int(time.time()),
			}
			area = record[2]
			resInfo['minPos'], resInfo['maxPos'] = util.AreaStringToPos(area)
			resInfo["bornPos"] = util.StringToList(record[7])
			if record[6]:
				resInfo["authority"] = json.loads(record[6])
			else:
				resInfo["authority"] = {}
			self.AddOneResidence(resInfo)

	# 新增领地的后处理
	def AddOneResidence(self, resInfo):
		super(ResidenceGasMgr, self).AddOneResidence(resInfo)	# 基类函数，维护一些方面查询的内存结构
		resId, dim, priority = resInfo["id"], resInfo["dimension"], resInfo["resLevel"]
		minPos, maxPos = resInfo['minPos'], resInfo['maxPos']
		# 利用引擎接口【SetForbidFlowField】设置【流体是否可流入领地】
		canFlowInto = resInfo["authority"].get("can_flow_into", None)
		if canFlowInto is None:
			canFlowInto = util.GetModConfByField("can_flow_into")
		isForbid = (not canFlowInto)
		lobbyGameApi.SetForbidFlowField(resId, dim, minPos, maxPos, priority, isForbid)
		# 利用引擎接口【SetForbidDragonEggTeleportField】设置【龙蛋是否可传入领地】
		canDragonEggTeleportInto = resInfo["authority"].get("can_dragon_egg_teleport_into", None)
		if canDragonEggTeleportInto is None:
			canDragonEggTeleportInto = util.GetModConfByField("can_dragon_egg_teleport_into")
		isForbid = (not canDragonEggTeleportInto)
		lobbyGameApi.SetForbidDragonEggTeleportField(resId, dim, minPos, maxPos, priority, isForbid)

	# 修改领地占据区域的后处理	
	def ChangeOneResidencePos(self, resInfo, oldMinPos, oldMaxPos):
		super(ResidenceGasMgr, self).ChangeOneResidence(resInfo, oldMinPos, oldMaxPos)
		resId, dim, priority = resInfo["id"], resInfo["dimension"], resInfo["resLevel"]
		minPos, maxPos = resInfo['minPos'], resInfo['maxPos']
		# 利用引擎接口【SetForbidFlowField】设置【流体是否可流入领地】
		canFlowInto = resInfo["authority"].get("can_flow_into", None)
		if canFlowInto is None:
			canFlowInto = util.GetModConfByField("can_flow_into")
		isForbid = (not canFlowInto)
		lobbyGameApi.SetForbidFlowField(resId, dim, minPos, maxPos, priority, isForbid)
		# 利用引擎接口【SetForbidDragonEggTeleportField】设置【龙蛋是否可传入领地】
		canDragonEggTeleportInto = resInfo["authority"].get("can_dragon_egg_teleport_into", None)
		if canDragonEggTeleportInto is None:
			canDragonEggTeleportInto = util.GetModConfByField("can_dragon_egg_teleport_into")
		isForbid = (not canDragonEggTeleportInto)
		lobbyGameApi.SetForbidDragonEggTeleportField(resId, dim, minPos, maxPos, priority, isForbid)
	

	# 删除领地的后处理
	def DelResidenceByResidenceId(self, resId):
		resInfo = super(ResidenceGasMgr, self).DelResidenceByResidenceId(resId)
		if not resInfo:
			return None
		resId = resInfo["id"]
		# 解除【流体是否可流入领地】限制
		lobbyGameApi.DelForbidFlowField(resId)
		# 解除【龙蛋是否可传入领地】限制
		lobbyGameApi.DelForbidDragonEggTeleportField(resId)
		return resInfo

	# 领地权限修改的生效逻辑实现
	def ApplyFieldAuthorityChange(self, resInfo, valueChangeDict):
		resId, dim, priority = resInfo["id"], resInfo["dimension"], resInfo["resLevel"]
		minPos, maxPos = resInfo['minPos'], resInfo['maxPos']
		for aukey, data in needCheckFieldData.iteritems():
			setFunc, delFunc = data
			if aukey not in valueChangeDict:
				continue
			old, new = valueChangeDict[aukey]["old"], valueChangeDict[aukey]["new"]
			if old is None:
				old = util.GetModConfByField(aukey)
			if new is None:
				new = util.GetModConfByField(aukey)
			isForbid = (not new)
			setFunc(resId, dim, minPos, maxPos, priority, isForbid)
	# --------------------------------------------------------------------------------------------
	# 检查新建领地的领地名、领地区域参数的正确性
	def CheckNewResidenceBase(self, residenceName, minPos, maxPos):
		import itertools
		# 领地名不能为空
		if not residenceName:
			return False, residenceConsts.ResponseCode.ResidenceNameEmpty
		# 领地名长度限制
		if len(residenceName) > residenceConsts.ResidenceNameLimit:
			return False, residenceConsts.ResponseCode.ResidenceNameLengthLimit
		# 领地名是否唯一
		if not self.CheckUniqueResidenceName(residenceName):
			return False, residenceConsts.ResponseCode.ResidenceNameConflict
		# 领地名是否含有敏感词
		isOk = commonNetgameApi.CheckNameValid(residenceName)
		if not isOk:
			return False, residenceConsts.ResponseCode.ResidenceNameNotValid
		# 领地区域的AABB包围盒参数是否正确（minPos是否均小于等于maxPos）
		if True in itertools.imap(lambda l, r: l > r, minPos, maxPos):
			return False, residenceConsts.ResponseCode.ResidenceAreaWrong
		return True, ""

	# 检查玩家是否可以执行修改领地的操作
	def CheckUpdateResidencePlayer(self, uid):
		# 玩家是否在线
		player = util.GetResidenceSystem().GetPlayerMgr().GetPlayerByUid(uid)
		if not player:
			reason = "CheckUpdateResidencePlayer fail! player [uid=%s] not online" % uid
			return False, reason
		# 玩家是否正在执行某些领地相关操作（并发限制）
		if not player.GetResidenceActionLock():
			reason = "CheckUpdateResidencePlayer fail! player [uid=%s] residence action is locked, please wait and try later" % uid
			return False, reason
		return True, player

	# 根据配置限制的Y坐标上下限，生成领地的区域的AABB包围盒
	def FitNewResidenceY(self, minPos, maxPos):
		if util.GetModConfByField("residence_support_y_axis"):
			return (int(minPos[0]), int(minPos[1]), int(minPos[2])), (int(maxPos[0]), int(maxPos[1]), int(maxPos[2]))
		minY, maxY = util.GetModConfByField("residence_y_size")
		return (int(minPos[0]), int(minY), int(minPos[2])), (int(maxPos[0]), int(maxY), int(maxPos[2]))

	# 检查申请的领地区域是否合法（大小限制等）
	def CheckNewResidenceSize(self, resLevel, minPos, maxPos):
		limitSize = util.GetModConfByField("size_limit").get("lv%d"%resLevel, None)
		if limitSize is None:
			return True, ""
		needCheckY =  util.GetModConfByField("residence_support_y_axis")
		for idx, posKey in enumerate(["x", "y", "z"]):
			if posKey == "y" and (not needCheckY):
				continue
			minSize, maxSize = limitSize[posKey]
			size = (maxPos[idx] - minPos[idx] + 1)
			if size < minSize or size > maxSize:
				reason = "CheckNewResidenceSize fail! size %s must between %d-%d" % (posKey, minSize, maxSize)
				return False, reason
		return True, ""

	# 检查传入的修改权限信息是否合法
	def CheckAuthority(self, authority, forPlayer):
		if (not authority) or (type(authority) != dict):
			reason = "CheckAuthority fail! authority must not be none empty dict"
			return False, reason
		actionDict = {}
		for keyword, value in authority.iteritems():
			vType = residenceConsts.AuthorityValueType.get(keyword, None)
			if not vType:
				reason = "CheckAuthority fail! keyword [%s] not exist" % keyword
				return False, reason
			openForPlayer = residenceConsts.AuthorityForPlayer.get(keyword, False)
			if forPlayer and (not openForPlayer):
				reason = "CheckAuthority fail! keyword [%s] not support for player" % keyword
				return False, reason
			if vType == bool:
				if value is None:
					actionDict[keyword] = {"del": None}
				else:
					actionDict[keyword] = {"set": bool(value)}
			elif vType == list:
				if type(value) != dict:
					reason = "CheckAuthority fail! keyword [%s] vType is list, only support dict with key 'add','remove','set'" % keyword
					return False, reason
				if value.has_key("set"):
					setValue = value["set"]
					if type(setValue) != list:
						reason = "CheckAuthority fail! keyword [%s] vType is list, set action only support list" % keyword
						return False, reason
					actionDict[keyword] = {"set": setValue}
				else:
					if value.has_key("add"):
						addValue = value["add"]
						if type(addValue) == str:
							actionDict[keyword] = {"add": [addValue, ]}
						elif type(addValue) == list:
							actionDict[keyword] = {"add": addValue}
						else:
							reason = "CheckAuthority fail! keyword [%s] vType is list, add action only support string or list" % keyword
							return False, reason
					elif value.has_key("remove"):
						removeValue = value["remove"]
						if type(removeValue) == str:
							actionDict[keyword] = {"remove": [removeValue, ]}
						elif type(removeValue) == list:
							actionDict[keyword] = {"remove": removeValue}
						else:
							reason = "CheckAuthority fail! keyword [%s] vType is list, remove action only support string or list" % keyword
							return False, reason
					else:
						reason = "CheckAuthority fail! keyword [%s] vType is list, only support dict with key 'add','remove','set'" % keyword
						return False, reason
			else:
				reason = "CheckAuthority fail! keyword [%s] not support" % keyword
				return False, reason
		return True, actionDict
	# --------------------------------------------------------------------------------------------
	def OnQueryServerResidence(self, data):
		"""
		查询当前服务器的领地信息
		"""
		startId = data.get("startId", 0)
		httpRes = {'code': residenceConsts.SuccessCode, 'message' : '', 'clientId': data['clientId']}
		reachEnd, resList = self.QueryResidenceByStartId(startId)
		httpRes['entity'] = {
			"startId": startId,
			"reachEnd": reachEnd,
			"resList": resList,
		}
		self.mSystem.NotifyToMaster(residenceConsts.HttpResponseEvent, httpRes)

	def QueryResidenceByStartId(self, startId):
		allResIds = self.mResidenceMap.keys()
		if not allResIds:
			return True, []
		allResIds.sort()
		result = []
		maxResId = 0
		for resId in allResIds:
			if resId <= startId:
				continue
			resInfo = self.mResidenceMap[resId]
			result.append(resInfo)
			maxResId = resId
			if len(result) >= residenceConsts.QueryLimitOnce:
				break
		if maxResId >= allResIds[-1]:
			return True, result
		else:
			return False, result
	# ----------------------------------------------------------------------------------------------
	# 新增一个领地
	def DoAddNewResidence(self, master, resInfo):
		if master:
			uid = master.mUid
		else:
			uid = 0
		print 'DoAddNewResidence uid:%s, resInfo:%s' % (uid, str(resInfo))
		area = util.PosToAeraString(resInfo["minPos"], resInfo["maxPos"])
		bornPoint = util.ListToString(resInfo["bornPos"])
		# 新增领地先在内存中完成，再更新数据库
		resInfo["version"] = int(time.time())
		self.AddOneResidence(resInfo)
		dbApi.CreateNewResidence(uid, resInfo["id"], self.mServerType, resInfo["name"],
			resInfo["dimension"], area, bornPoint, resInfo["resLevel"], resInfo["parentResId"])
		# 给领地增加玩家，再更新数据库
		if master:
			master.JoinResidence(resInfo)
			if master.mPlayerId == residenceConsts.SERVER_PLAYER_PLAYERID:
				userName = residenceConsts.SERVER_PLAYER_NICKNAME
			else:
				userName = lobbyGameApi.GetPlayerNickname(master.mPlayerId)
			dbApi.AddPlayerToResidence(master.mUid, resInfo["id"], self.mServerType, userName)

	def DoAddNewResidenceByUid(self, uid, username, resInfo):
		print 'DoAddNewResidenceByUid uid:%s, resInfo:%s' % (uid, str(resInfo))
		area = util.PosToAeraString(resInfo["minPos"], resInfo["maxPos"])
		bornPoint = util.ListToString(resInfo["bornPos"])
		# 新增领地先在内存中完成，再更新数据库
		resInfo["version"] = int(time.time())
		self.AddOneResidence(resInfo)
		dbApi.CreateNewResidence(uid, resInfo["id"], self.mServerType, resInfo["name"],
			resInfo["dimension"], area, bornPoint, resInfo["resLevel"], resInfo["parentResId"])
		# 给领地增加玩家
		dbApi.AddPlayerToResidence(uid, resInfo["id"], self.mServerType, username)
		# 如果玩家在线，那么更新玩家缓存
		master = util.GetResidenceSystem().GetPlayerMgr().GetPlayerByUid(uid)
		if master:
			master.JoinResidence(resInfo)

	# 修改领地占据的区域		
	def DoChangeResidencePos(self, master, resId, minPos, maxPos):
		if master:
			uid = master.mUid
		else:
			uid = 0
		print 'DoChangeNewResidence uid:%s, minPos:%s, maxPos:%s' % (uid, minPos, maxPos)
		area = util.PosToAeraString(minPos, maxPos)
		resInfo = self.mResidenceMap[resId]
		resInfo["version"] = int(time.time())
		oldMinPos = resInfo["minPos"]
		oldMaxPos = resInfo["minPos"]
		resInfo["minPos"] = minPos
		resInfo["maxPos"] = maxPos
		self.ChangeOneResidencePos(resInfo, oldMinPos, oldMaxPos)
		
		dbApi.ChangeResidencePos(resInfo["id"], self.mServerType, area)
		
		if master:
			master.JoinResidence(resInfo)
		
	
	# 删除领地
	def DoDeleteResidence(self, baseResInfo):
		baseResId = baseResInfo["id"]
		# 遍历所有子领地，查询出所有需要删除的领地ID列表
		allSubResList = set()
		self.FindAllSubResidenceList(baseResId, allSubResList)
		allSubResList.add(baseResId)
		#print "FindAllSubResidenceList baseResId=%s, allSubResList=%s" % (baseResId, str(allSubResList))
		result = []
		finalResIdList = []
		for resId in allSubResList:
			resInfo = self.DelResidenceByResidenceId(resId)
			if resInfo:
				result.append(resInfo)
				finalResIdList.append(resId)
		# 被删除的领地，需要清理玩家的从属关系
		util.GetPlayerMgr().CleanOwnerAndAuthorityByDeleteResidence(finalResIdList)
		dbApi.DeleteResidence(self.mServerType, finalResIdList)
		if baseResInfo["resLevel"] == 0:	# 只有零级领地才有所有者
			dbApi.DeletePlayerResidence(self.mServerType, baseResId)
		dbApi.DeleteOutPlayerAuthority(self.mServerType, finalResIdList)
		self.mSystem.BroadcastToAllClient(residenceConsts.DelResidenceFromServerEvent, {"delResIdList": finalResIdList})
		return result

	# 把一个玩家添加到一个领地的所有者中
	def DoAddPlayerToResidence(self, player, resInfo):
		player.JoinResidence(resInfo)
		userName = lobbyGameApi.GetPlayerNickname(player.mPlayerId)
		dbApi.AddPlayerToResidence(player.mUid, resInfo["id"], self.mServerType, userName)

	# 把一个玩家从一个领地的所有者中剔除
	def DoRemovePlayerFromResidence(self, player, resInfo):
		player.LeaveResidence(resInfo)
		dbApi.RemovePlayerFromResidence(self.mServerType, player.mUid, resInfo["id"])
		#import lobbyGame.netgameApi as lobbyGameApi
		playerId = lobbyGameApi.GetPlayerIdByUid(player.mUid)
		self.mSystem.NotifyToClient(playerId, residenceConsts.RemovePlayerResidentFromServerEvent, {"removePlayerResId": resInfo["id"]})

	# 根据权限修改的信息，生成最终的权限字典
	def DoApplyAuthorityChange(self, authority, actionDict):
		valueChangeDict = {}
		for keyword, action in actionDict.iteritems():
			oldAuValue = authority.get(keyword, None)
			vType = residenceConsts.AuthorityValueType[keyword]
			if vType == bool:
				if action.has_key("del") and authority.has_key(keyword):
					del authority[keyword]
				elif action.has_key("set"):
					authority[keyword] = action["set"]
			elif vType == list:
				if not authority.has_key(keyword):
					authority[keyword] = []
				if action.has_key("set"):
					authority[keyword] = action["set"]
				if action.has_key("add"):
					for v in action["add"]:
						if v not in authority[keyword]:
							authority[keyword].append(v)
				if action.has_key("remove"):
					for v in action["remove"]:
						if v in authority[keyword]:
							authority[keyword].remove(v)
			newAuValue = authority.get(keyword, None)
			valueChangeDict[keyword] = {
				"old": oldAuValue,
				"new": newAuValue,
			}
		return valueChangeDict
	# ----------------------------------------------------------------------------------------------
	# 完整的创建新顶级领地的完整逻辑，包括各种检查和最终的生效和返回
	def ServerTryCreateTopResidenceStart(self, cbFunc, uid, name, dimension, minPos, maxPos, bornPos=None):
		minPos, maxPos = self.FitNewResidenceY(minPos, maxPos)
		def CheckCreateTopResidenceCallback(suc, rcode):
			if not suc:
				dbApi.ReleasePlayerResideneActionLock(uid)
				if rcode == residenceConsts.ResponseCode.SizeOverLimit:
					needSize = util.GetModConfByField("size_limit").get("lv0", None)
					formatData = {
						"x0": needSize["x"][0],
						"x1": needSize["x"][1],
						"y0": needSize["y"][0],
						"y1": needSize["y"][1],
						"z0": needSize["z"][0],
						"z1": needSize["z"][1],
					}
					message = residenceConsts.FMT_CH[rcode].format(formatData)
				else:
					message = residenceConsts.FMT_CH[rcode]
				cbFunc(suc, message)
				return
			username = rcode
			self.ServerTryCreateTopResidenceAfter(cbFunc, uid, username, name, dimension, minPos, maxPos, bornPos)
		self.CheckCreateTopResidenceStep1(CheckCreateTopResidenceCallback, uid, name, dimension, minPos, maxPos, bornPos)

	def ServerTryCreateTopResidenceAfter(self, cbFunc, uid, username, name, dimension, minPos, maxPos, bornPos):
		if not self.mUsableResIds:
			cbFunc(False, residenceConsts.FMT_CH[residenceConsts.ResponseCode.NoUsableResId])
			return
		newResId = self.mUsableResIds.pop(0)
		# 付钱
		tradeSystem = serverApi.GetSystem("neteaseTrade", "neteaseTradeDev")
		if not tradeSystem:
			self.real_createResidence(newResId, uid, name, username, dimension, minPos, maxPos, bornPos)
			cbFunc(True, "创建成功！领地ID是:%s" % newResId)
			return		
		def PurchaseCallback(playerId, rtn, data):
			if not rtn:
				dbApi.ReleasePlayerResideneActionLock(uid)
				cbFunc(False, "请求超时")
				return
			if data['code'] == 1 and data['entity']['groceryId'] == util.GetModConfByField("grocery_id") and \
					data['entity']['goodId'] == "RESIDENCE_OPEN":
				self.ShowCreateTips("购买成功，创建中", playerId)
				self.real_createResidence(newResId, uid, name, username, dimension, minPos, maxPos, bornPos)
				cbFunc(True, "创建成功！领地ID是:%s" % newResId)
			else:
				dbApi.ReleasePlayerResideneActionLock(uid)
				cbFunc(False, "支付失败，无法创建新领地")
		params = {
			'playerId': lobbyGameApi.GetPlayerIdByUid(uid),
			'groceryId': util.GetModConfByField("grocery_id"),
			'goodId': "RESIDENCE_OPEN",
			'forgery': PurchaseCallback,
		}
		tradeSystem.OnPlayerPurchase(params)
		
	def real_createResidence(self, newResId, uid, name, username, dimension, minPos, maxPos, bornPos):
		resInfo = {
			"id": newResId,
			"serverType": self.mServerType,
			"dimension": dimension,
			"name": name,
			"resLevel": 0,
			"parentResId": 0,
			"minPos": minPos,
			"maxPos": maxPos,
			"authority": {},
		}
		if bornPos is None:
			resInfo["bornPos"] = ((minPos[0]+maxPos[0])//2, maxPos[1], (minPos[2]+maxPos[2])//2)
		else:
			resInfo["bornPos"] = bornPos
		self.DoAddNewResidenceByUid(uid, username, resInfo)
		dbApi.ReleasePlayerResideneActionLock(uid)
	
	# 完整的创建子领地的完整逻辑，包括各种检查和最终的生效和返回
	def ServerTryCreateSubResidence(self, name, parentResId, minPos, maxPos, bornPos=None):
		parentResInfo = self.mResidenceMap.get(parentResId, None)
		if not parentResInfo:
			reason = "TryCreateSubResidence fail! parentResId[%s] is not exist" % parentResId
			return False, reason, "无法根据当前选择的两个对角点创建子领地，圈地失败，请重新圈地"
		resLevel = parentResInfo["resLevel"] + 1
		if resLevel > util.GetModConfByField("sub_lv_limit"):
			reason = "TryCreateSubResidence fail! resLevel limit is %s" % util.GetModConfByField("sub_lv_limit")
			return False, reason, "选择的 %s,%s 在自己的领地内，但该领地的子领地层级已达上限，无法创建子领地。"%(str(minPos), str(maxPos))
		topLevelResId = self.GetTopLevelResidenceId(parentResInfo)
		hasNum, limitNum = self.GetSubResidenceNumber(topLevelResId), util.GetModConfByField("sub_num_limit")
		if hasNum >= limitNum:
			reason = "TryCreateSubResidence fail! topLevel[%s] already has %s sub residence, limit is %s" % (topLevelResId, hasNum, limitNum)
			return False, reason, "选择的 %s,%s 在自己的领地内，但该领地的子领地数量已达上限，无法创建子领地。"%(str(minPos), str(maxPos))
		minPos, maxPos = self.FitNewResidenceY(minPos, maxPos)
		suc, reason = self.CheckNewResidenceBase(name, minPos, maxPos)
		if not suc:
			return False, reason, "无法根据当前选择的两个对角点创建子领地，圈地失败，请重新圈地。"
		suc, reason = self.CheckNewResidenceSize(resLevel, minPos, maxPos)
		if not suc:
			needSize = util.GetModConfByField("size_limit").get("lv%d"%resLevel, None)
			return False, reason, "当前选择的子领地区域大小不符合要求，圈地失败；子领地范围要求：东西%s~%s格，南北%s~%s格，高度%s~%s格"%(needSize["x"][0], needSize["x"][1], needSize["z"][0], needSize["z"][1], needSize["y"][0], needSize["y"][1])
		suc, reason, tips = self.ServerCheckSubResidenceArea(parentResInfo, minPos, maxPos)
		if not suc:
			return False, reason, tips
		if not self.mUsableResIds:
			code = residenceConsts.ResponseCode.NoUsableResId
			return False, residenceConsts.FMT_EN[code], residenceConsts.FMT_CH[code]
		newResId = self.mUsableResIds.pop(0)
		resInfo = {
			"id": newResId,
			"serverType": self.mServerType,
			"dimension": parentResInfo["dimension"],
			"name": name,
			"resLevel": resLevel,
			"parentResId": parentResId,
			"minPos": minPos,
			"maxPos": maxPos,
			"authority": {},
		}
		if bornPos is None:
			resInfo["bornPos"] = ((minPos[0]+maxPos[0])//2, maxPos[1], (minPos[2]+maxPos[2])//2)
		else:
			resInfo["bornPos"] = bornPos
		self.DoAddNewResidence(None, resInfo)
		return True, resInfo, "创建成功！子领地ID是:%s"%newResId
	
	def TryCreateTopResidenceStart(self, cbFunc, uid, name, dimension, minPos, maxPos, bornPos=None):
		minPos, maxPos = self.FitNewResidenceY(minPos, maxPos)
		def CheckCreateTopResidenceCallback(suc, rcode):
			if not suc:
				cbFunc(suc, residenceConsts.FMT_EN[rcode])
				return
			username = rcode
			if not self.mUsableResIds:
				code = residenceConsts.ResponseCode.NoUsableResId
				cbFunc(False, residenceConsts.FMT_EN[code])
				return
			newResId = self.mUsableResIds.pop(0)
			resInfo = {
				"id": newResId,
				"serverType": self.mServerType,
				"dimension": dimension,
				"name": name,
				"resLevel": 0,
				"parentResId": 0,
				"minPos": minPos,
				"maxPos": maxPos,
				"authority": {},
			}
			if bornPos is None:
				resInfo["bornPos"] = ((minPos[0]+maxPos[0])//2, maxPos[1], (minPos[2]+maxPos[2])//2)
			else:
				resInfo["bornPos"] = bornPos
			self.DoAddNewResidenceByUid(uid, username, resInfo)
			dbApi.ReleasePlayerResideneActionLock(uid)
			cbFunc(True, resInfo)
		self.CheckCreateTopResidenceStep1(CheckCreateTopResidenceCallback, uid, name, dimension, minPos, maxPos, bornPos)
	
	def CheckCreateTopResidenceStep1(self, cbFunc, uid, name, dimension, minPos, maxPos, bornPos):
		# 玩家是否正在执行某些领地相关操作（并发限制）
		def GetPlayerResidenceActionLockCallback(suc):
			if not suc:
				cbFunc(False, residenceConsts.ResponseCode.GetPlayerActionLockFail)
				return
			self.CheckCreateTopResidenceStep2(cbFunc, uid, name, dimension, minPos, maxPos, bornPos)
		dbApi.GetPlayerResidenceActionLock(uid, GetPlayerResidenceActionLockCallback)

	def CheckCreateTopResidenceStep2(self, cbFunc, uid, name, dimension, minPos, maxPos, bornPos):
		# 系统创建领地不需要查询玩家是否存在
		# 系统创建领地不受领地数量限制
		if uid == residenceConsts.SERVER_PLAYER_UID:
			self.CheckCreateTopResidenceStep4(cbFunc, 0, uid, residenceConsts.SERVER_PLAYER_NICKNAME, name, dimension, minPos, maxPos, bornPos)
			return
		def QueryPlayerDataCallback(records):
			if not records:
				dbApi.ReleasePlayerResideneActionLock(uid)
				cbFunc(False, residenceConsts.ResponseCode.PlayerNotExist)
				return
			username = records[0][1]
			self.CheckCreateTopResidenceStep3(cbFunc, uid, username, name, dimension, minPos, maxPos, bornPos)
		dbApi.QueryPlayerDataByUid(uid, QueryPlayerDataCallback)
	
	def CheckCreateTopResidenceStep3(self, cbFunc, uid, username, name, dimension, minPos, maxPos, bornPos):
		# 玩家拥有的领地数量是否已经到达上限
		def QueryPlayerAllResidenceCallback(records):
			player = util.GetResidenceSystem().GetPlayerMgr().GetPlayerByUid(uid)
			if records:
				hasResNum = len(records)
				if player:
					player.CacheResData(records)
			else:
				hasResNum = 0
				if player:
					player.CacheResData([])
			self.CheckCreateTopResidenceStep4(cbFunc, hasResNum, uid, username, name, dimension, minPos, maxPos, bornPos)
		dbApi.QueryPlayerResidence(uid, QueryPlayerAllResidenceCallback)
	
	def CheckCreateTopResidenceStep4(self, cbFunc, hasResNum, uid, username, name, dimension, minPos, maxPos, bornPos):
		limitNum = util.GetModConfByField("lv0_residence_num_limit")
		if hasResNum >= limitNum:
			dbApi.ReleasePlayerResideneActionLock(uid)
			cbFunc(False, residenceConsts.ResponseCode.ReachResidenceNumLimit)
			return
		# 检查领地名合法性，以及领地输入区域合法性
		suc, reason = self.CheckNewResidenceBase(name, minPos, maxPos)
		if not suc:
			dbApi.ReleasePlayerResideneActionLock(uid)
			cbFunc(False, reason)
			return
		# 检查领地区域大小是否符合配置中的限制
		suc, reason = self.CheckNewResidenceSize(0, minPos, maxPos)
		if not suc:
			dbApi.ReleasePlayerResideneActionLock(uid)
			cbFunc(False, residenceConsts.ResponseCode.SizeOverLimit)
			return
		suc, reason = self.CheckTopLevelResidenceArea(dimension, minPos, maxPos)
		if not suc:
			dbApi.ReleasePlayerResideneActionLock(uid)
			cbFunc(False, residenceConsts.ResponseCode.AreaConflictWithOther)
			return
		cbFunc(True, username)
	
	def TryChangeResidencePos(self, uid, resId, dimension, minPos, maxPos):
		resInfo = self.mResidenceMap.get(resId)
		if not resInfo:
			reason = "TryChangeResidencePos fail! resId[%s] is not exist" % resId
			return False, reason, "领地不存在"
		suc, playerOrReason = self.CheckUpdateResidencePlayer(uid)
		if not suc:
			return False, playerOrReason, "无法根据当前选择的两个对角点创建领地，圈地失败，请重新圈地"
		parentResId = resInfo.get("parentResId", 0)
		if parentResId == 0:
			#是顶层领地
			suc, reason = self.CheckTopLevelResidenceArea(dimension, minPos, maxPos, resId)
			if not suc:  # 失败不要忘记解除互斥锁
				playerOrReason.ReleaseResidenceActionLock()
				return False, reason, "无法根据当前选择的两个对角点创建领地，圈地失败，请重新圈地"
			suc, reason = self.CheckNewResidenceSize(0, minPos, maxPos)
			if not suc:  # 失败不要忘记解除互斥锁
				playerOrReason.ReleaseResidenceActionLock()
				needSize = util.GetModConfByField("size_limit").get("lv0", None)
				return False, reason, "当前选择的领地区域大小不符合要求，圈地失败；领地范围要求：东西%s~%s格，南北%s~%s格，高度%s~%s格。"%(needSize["x"][0], needSize["x"][1], needSize["z"][0], needSize["z"][1], needSize["y"][0], needSize["y"][1])
			#检查是否和其他顶级领地重合
			suc, reason = self.CheckTopLevelResidenceArea(dimension, minPos, maxPos, resId)
			if not suc:  # 失败不要忘记解除互斥锁
				playerOrReason.ReleaseResidenceActionLock()
				return False, reason, "当前选中的领地区域与其他同层级领地有交叉，圈地失败"
			#检查是否和子领地重合
			suc, reason = self.CheckChangeResidence(resId, minPos, maxPos)
			if not suc:  # 失败不要忘记解除互斥锁
				playerOrReason.ReleaseResidenceActionLock()
				return False, reason, " 当前选中的领地区域与子领地有交叉，圈地失败"
			self.DoChangeResidencePos(playerOrReason, resId, minPos, maxPos)
			playerOrReason.ReleaseResidenceActionLock()
			return True, resInfo, " 修改成功"
		else:
			parentResInfo = self.mResidenceMap.get(parentResId, None)
			if not parentResInfo:
				reason = "TryCreateSubResidence fail! parentResId[%s] is not exist" % parentResId
				return False, reason, "父领地不存在"
			resLevel = resInfo["resLevel"]
			# if resLevel > util.GetModConfByField("sub_lv_limit"):
			# 	reason = "TryCreateSubResidence fail! resLevel limit is %s" % util.GetModConfByField("sub_lv_limit")
			# 	return False, reason
			# topLevelResId = self.GetTopLevelResidenceId(parentResInfo)
			# hasNum, limitNum = self.GetSubResidenceNumber(topLevelResId), util.GetModConfByField("sub_num_limit")
			# if hasNum >= limitNum:
			# 	reason = "TryCreateSubResidence fail! topLevel[%s] already has %s sub residence, limit is %s" % (
			# 	topLevelResId, hasNum, limitNum)
			# 	return False, reason
			minPos, maxPos = self.FitNewResidenceY(minPos, maxPos)
			suc, reason = self.CheckNewResidenceBase("", minPos, maxPos)
			if not suc:
				return False, reason, "无法根据当前选择的两个对角点创建子领地，圈地失败，请重新圈地。"
			suc, reason = self.CheckNewResidenceSize(resLevel, minPos, maxPos)
			if not suc:
				needSize = util.GetModConfByField("size_limit").get("lv%d" % resLevel, None)
				return False, reason, "当前选择的子领地区域大小不符合要求，圈地失败；子领地范围要求：东西%s~%s格，南北%s~%s格，高度%s~%s格"%(needSize["x"][0], needSize["x"][1], needSize["z"][0], needSize["z"][1], needSize["y"][0], needSize["y"][1])
			suc, reason, tips = self.ServerCheckSubResidenceArea(parentResInfo, minPos, maxPos, resId)
			if not suc:
				return False, reason, tips
			
			def purchase_cb(playerId, rtn, data):
				if not rtn:
					self.ShowCreateTips("请求超时", playerId)
					return
				if data['code'] == 1 and data['entity']['groceryId'] == util.GetModConfByField("grocery_id") and \
						data['entity']['goodId'] == "RESIDENCE_CHANGE":
					self.ShowCreateTips("购买成功，修改中", playerId)
					self.Real_ChangeResidencePos(playerOrReason, resId, minPos, maxPos)
					self.ShowCreateTips("修改成功！", playerId)
				else:
					self.ShowCreateTips("购买失败", playerId)
			
			tradeSystem = serverApi.GetSystem("neteaseTrade", "neteaseTradeDev")
			if tradeSystem:
				tradeSystem.OnPlayerPurchase({
					'playerId': lobbyGameApi.GetPlayerUid(uid),
					'groceryId': util.GetModConfByField("grocery_id"),
					'goodId': "RESIDENCE_CHANGE",
					'forgery': purchase_cb,
				})
				return True, "", "购买中。。。"
			else:
				self.Real_ChangeResidencePos(playerOrReason, resId, minPos, maxPos)
				return True, reason, "修改成功！"
				
	def Real_ChangeResidencePos(self,playerOrReason, resId, minPos, maxPos):
		self.DoChangeResidencePos(playerOrReason, resId, minPos, maxPos)
		playerOrReason.ReleaseResidenceActionLock()
			
	# 创建新领地（运营指令版）
	def TryCreateSubResidence(self, name, parentResId, minPos, maxPos, bornPos=None):
		parentResInfo = self.mResidenceMap.get(parentResId, None)
		if not parentResInfo:
			reason = "TryCreateSubResidence fail! parentResId[%s] is not exist" % parentResId
			return False, reason
		resLevel = parentResInfo["resLevel"] + 1
		if resLevel > util.GetModConfByField("sub_lv_limit"):
			reason = "TryCreateSubResidence fail! resLevel limit is %s" % util.GetModConfByField("sub_lv_limit")
			return False, reason
		topLevelResId = self.GetTopLevelResidenceId(parentResInfo)
		hasNum, limitNum = self.GetSubResidenceNumber(topLevelResId), util.GetModConfByField("sub_num_limit")
		if hasNum >= limitNum:
			reason = "TryCreateSubResidence fail! topLevel[%s] already has %s sub residence, limit is %s" % (topLevelResId, hasNum, limitNum)
			return False, reason
		minPos, maxPos = self.FitNewResidenceY(minPos, maxPos)
		suc, reason = self.CheckNewResidenceBase(name, minPos, maxPos)
		if not suc:
			return False, reason
		suc, reason = self.CheckNewResidenceSize(resLevel, minPos, maxPos)
		if not suc:
			needSize = util.GetModConfByField("size_limit").get("lv%d"%resLevel, None)
			return False, reason
		suc, reason = self.CheckSubResidenceArea(parentResInfo, minPos, maxPos)
		if not suc:
			return False, reason
		if not self.mUsableResIds:
			code = residenceConsts.ResponseCode.NoUsableResId
			return False, residenceConsts.FMT_EN[code]		
		newResId = self.mUsableResIds.pop(0)
		resInfo = {
			"id": newResId,
			"serverType": self.mServerType,
			"dimension": parentResInfo["dimension"],
			"name": name,
			"resLevel": resLevel,
			"parentResId": parentResId,
			"minPos": minPos,
			"maxPos": maxPos,
			"authority": {},
		}
		if bornPos is None:
			resInfo["bornPos"] = ((minPos[0]+maxPos[0])//2, maxPos[1], (minPos[2]+maxPos[2])//2)
		else:
			resInfo["bornPos"] = bornPos
		self.DoAddNewResidence(None, resInfo)
		return True, resInfo

	def OnSetPlayerResidence(self, data):
		"""
		处理来自master的创建新领地的运营指令
		"""
		def CreateTopResidenceCallback(suc, resDataOrReason):
			if suc:
				self.OnHttpResidenceSuccess(resDataOrReason, data['clientId'])
			else:
				self.OnHttpResidenceFail(resDataOrReason, data['clientId'])
		parentResId = data.get("parentResId", 0)
		if parentResId == 0:
			self.TryCreateTopResidenceStart(CreateTopResidenceCallback, data['uid'], data['name'], data.get("dimension", 0), data['minPos'], data['maxPos'], data.get("bornPos", None))
		else:
			suc, resDataOrReason = self.TryCreateSubResidence(data['name'], parentResId, data['minPos'], data['maxPos'], data.get("bornPos", None))
			CreateTopResidenceCallback(suc, resDataOrReason)

	def OnHttpResidenceSuccess(self, data, clientId):
		httpRes = {
			"clientId": clientId,
			"code": residenceConsts.SuccessCode,
			"message": "",
			"entity": data,
		}
		self.mSystem.NotifyToMaster(residenceConsts.HttpResponseEvent, httpRes)

	def OnHttpResidenceFail(self, reason, clientId):
		httpRes = {
			"clientId": clientId,
			"code": residenceConsts.FailCode,
			"message": reason,
			"entity": None,
		}
		self.mSystem.NotifyToMaster(residenceConsts.HttpResponseEvent, httpRes)

	# 删除已有领地（运营指令版）
	def TryDeleteResidence(self, resId):
		resInfo = self.mResidenceMap.get(resId, None)
		if not resInfo:
			reason = "Create Residence Fail, reason is residence[%s] not exist" % resId
			return False, reason
		resInfoList = self.DoDeleteResidence(resInfo)
		return True, resInfoList

	def OnHttpDelResidence(self, data):
		"""
		处理来自master的删除已有领地的运营指令
		"""
		resId = data.get("resId", -1)
		suc, dataOrReason = self.TryDeleteResidence(resId)
		if suc:
			self.OnHttpResidenceSuccess(dataOrReason, data["clientId"])
		else:
			self.OnHttpResidenceFail(dataOrReason, data["clientId"])

	def TryAddPlayerToResidenceStart(self, cbFunc, uid, resId):
		def CheckAddPlayerToResidenceCallback(suc, reason):
			if not suc:
				cbFunc(False, residenceConsts.FMT_EN[reason])
				return
			username, resInfo = reason["username"], reason["resInfo"]
			player = util.GetResidenceSystem().GetPlayerMgr().GetPlayerByUid(uid)
			if player:
				player.JoinResidence(resInfo)
			dbApi.AddPlayerToResidence(uid, resId, self.mServerType, username)
			dbApi.ReleasePlayerResideneActionLock(uid)
			cbFunc(True, resInfo)
		self.CheckAddPlayerToResidenceStep1(CheckAddPlayerToResidenceCallback, uid, resId)

	def CheckAddPlayerToResidenceStep1(self, cbFunc, uid, resId):
		# 玩家是否正在执行某些领地相关操作（并发限制）
		def GetPlayerResidenceActionLockCallback(suc):
			if not suc:
				cbFunc(False, residenceConsts.ResponseCode.GetPlayerActionLockFail)
				return
			self.CheckAddPlayerToResidenceStep2(cbFunc, uid, resId)
		dbApi.GetPlayerResidenceActionLock(uid, GetPlayerResidenceActionLockCallback)

	def CheckAddPlayerToResidenceStep2(self, cbFunc, uid, resId):
		# 系统获取领地不需要查询玩家是否存在
		if uid == residenceConsts.SERVER_PLAYER_UID:
			self.CheckAddPlayerToResidenceStep3(cbFunc, uid, residenceConsts.SERVER_PLAYER_NICKNAME, resId)
			return
		def QueryPlayerDataCallback(records):
			if not records:
				dbApi.ReleasePlayerResideneActionLock(uid)
				cbFunc(False, residenceConsts.ResponseCode.PlayerNotExist)
				return
			username = records[0][1]
			self.CheckAddPlayerToResidenceStep3(cbFunc, uid, username, resId)
		dbApi.QueryPlayerDataByUid(uid, QueryPlayerDataCallback)
	
	def CheckAddPlayerToResidenceStep3(self, cbFunc, uid, username, resId):
		# 玩家拥有的领地数量是否已经到达上限
		def QueryPlayerAllResidenceCallback(records):
			player = util.GetResidenceSystem().GetPlayerMgr().GetPlayerByUid(uid)
			if records:
				# 顺便检查此玩家是否已经是目标领地的所有者了
				for record in records:
					record = util.UnicodeConvert(record)
					if record[0] == resId:
						dbApi.ReleasePlayerResideneActionLock(uid)
						cbFunc(False, residenceConsts.ResponseCode.AlreadyOwnerOfTarget)
						return
				hasResNum = len(records)
				if player:
					player.CacheResData(records)
			else:
				hasResNum = 0
				if player:
					player.CacheResData([])
			# 系统获取领地不受领地数量限制
			if uid == residenceConsts.SERVER_PLAYER_UID:
				hasResNum = 0
			self.CheckAddPlayerToResidenceStep4(cbFunc, hasResNum, uid, username, resId)
		dbApi.QueryPlayerResidence(uid, QueryPlayerAllResidenceCallback)
	
	def CheckAddPlayerToResidenceStep4(self, cbFunc, hasResNum, uid, username, resId):
		limitNum = util.GetModConfByField("lv0_residence_num_limit")
		if hasResNum >= limitNum:
			dbApi.ReleasePlayerResideneActionLock(uid)
			cbFunc(False, residenceConsts.ResponseCode.ReachResidenceNumLimit)
			return
		resInfo = self.mResidenceMap.get(resId, None)
		if not resInfo:
			dbApi.ReleasePlayerResideneActionLock(uid)
			cbFunc(False, residenceConsts.ResponseCode.TargetResidenceNotExist)
			return
		if resInfo["resLevel"] != 0:
			dbApi.ReleasePlayerResideneActionLock(uid)
			cbFunc(False, residenceConsts.ResponseCode.TargetResidenceNotTopLevel)
			return
		params = {
			"username": username,
			"resInfo": resInfo,
		}
		cbFunc(True, params)

	def OnHttpAddPlayerToResidence(self, data):
		"""
		处理来自master的为已有的领地新增所有者的运营指令
		"""
		uid, resId = data["uid"], data["resId"]
		def AddPlayerToResidenceCallback(suc, dataOrReason):
			if suc:
				self.OnHttpResidenceSuccess(dataOrReason, data["clientId"])
			else:
				self.OnHttpResidenceFail(dataOrReason, data["clientId"])
		self.TryAddPlayerToResidenceStart(AddPlayerToResidenceCallback, uid, resId)

	def CheckCanRemovePlayerResidence(self, resId):
		resInfo = self.mResidenceMap.get(resId, None)
		if not resInfo:
			reason = "CheckCanRemovePlayerResidence fail! residence [%s] not exist" % resId
			return False, reason
		if resInfo["resLevel"] != 0:
			reason = "CheckCanRemovePlayerResidence fail! residence [%s] not toplevel residence" % resId
			return False, reason
		return True, resInfo

	def TryRemovePlayerFromResidence(self, uid, resId):
		suc, playerOrReason = self.CheckUpdateResidencePlayer(uid)
		if not suc:
			return False, playerOrReason
		suc, resInfoOrReason = self.CheckCanRemovePlayerResidence(resId)
		if not suc:
			playerOrReason.ReleaseResidenceActionLock()
			return False, resInfoOrReason
		if not playerOrReason.IsResidenceOwner(resId):
			playerOrReason.ReleaseResidenceActionLock()
			reason = "CheckCanRemovePlayerResidence fail! player [%s] is not owner for residence [%s]" % (uid, resId)
			return False, reason
		self.DoRemovePlayerFromResidence(playerOrReason, resInfoOrReason)
		playerOrReason.ReleaseResidenceActionLock()
		return True, resInfoOrReason

	def OnHttpRemovePlayerFromResidence(self, data):
		"""
		处理来自master的为已有领地移除一个所有者的运营指令
		"""
		uid, resId = data["uid"], data["resId"]
		suc, dataOrReason = self.TryRemovePlayerFromResidence(uid, resId)
		if suc:
			self.OnHttpResidenceSuccess(dataOrReason, data["clientId"])
		else:
			self.OnHttpResidenceFail(dataOrReason, data["clientId"])

	def TryChangeResidenceAuthority(self, resId, authority):
		resInfo = self.mResidenceMap.get(resId, None)
		if not resInfo:
			reason = "ChangeResidenceAuthority fail! residence [%s] not exist" % resId
			return False, reason
		suc, actionOrReason = self.CheckAuthority(authority, False)
		if not suc:
			return False, actionOrReason
		valueChangeDict = self.DoApplyAuthorityChange(resInfo["authority"], actionOrReason)
		self.ApplyFieldAuthorityChange(resInfo, valueChangeDict)
		resInfo["version"] = int(time.time())
		dbApi.ChangeResidenceAuthority(self.mServerType, resId, resInfo["authority"])
		return True, resInfo["authority"]

	def OnHttpChangeResidenceAuthority(self, data):
		"""
		处理来自master的修改已有领地权限设置的运营指令
		"""
		resId, authority = data["resId"], data.get("authority", {})
		suc, dataOrReason = self.TryChangeResidenceAuthority(resId, authority)
		if suc:
			self.OnHttpResidenceSuccess(dataOrReason, data["clientId"])
		else:
			self.OnHttpResidenceFail(dataOrReason, data["clientId"])

	def TryChangePlayerResidenceAuthority(self, uid, resId, authority, mainAuth = None):
		suc, playerOrReason = self.CheckUpdateResidencePlayer(uid)
		if not suc:
			return False, playerOrReason
		resInfo = self.mResidenceMap.get(resId, None)
		if not resInfo:
			playerOrReason.ReleaseResidenceActionLock()
			reason = "ChangePlayerResidenceAuthority fail! residence [%s] not exist" % resId
			return False, reason
		if playerOrReason.IsResidenceOwner(resId):
			playerOrReason.ReleaseResidenceActionLock()
			reason = "ChangePlayerResidenceAuthority fail! player [%s] is owner of residence [%s]" % (uid, resId)
			return False, reason
		suc, actionOrReason = self.CheckAuthority(authority, True)
		if not suc:
			playerOrReason.ReleaseResidenceActionLock()
			return False, actionOrReason
		doInsert = False
		oldAuthority = playerOrReason.GetAllAuthority(resId)
		if not oldAuthority:
			oldAuthority = {}
			doInsert = True
		self.DoApplyAuthorityChange(oldAuthority, actionOrReason)
		playerOrReason.ApplyAuthorityByResId(resId, oldAuthority)
		playerOrReason.ReleaseResidenceActionLock()
		playerId = lobbyGameApi.GetPlayerIdByUid(uid)
		nickname = lobbyGameApi.GetPlayerNickname(playerId)
		if doInsert:
			dbApi.InsertOutPlayerResidenceAuthority(self.mServerType, uid, resId, oldAuthority)
			self.OnInsertAuthority(uid, nickname, resId, mainAuth)
		else:
			dbApi.UpdateOutPlayerResidenceAuthority(self.mServerType, uid, resId, oldAuthority)
		
		return True, oldAuthority
	
	def ServerTryChangePlayerResidenceAuthority(self, uid, resId, authority, mainAuth=None):
		suc, playerOrReason = self.CheckUpdateResidencePlayer(uid)
		if not suc:
			return False, playerOrReason, "玩家不在线！"
		resInfo = self.mResidenceMap.get(resId, None)
		if not resInfo:
			playerOrReason.ReleaseResidenceActionLock()
			reason = "ChangePlayerResidenceAuthority fail! residence [%s] not exist" % resId
			return False, reason, "领地不存在！"
		if playerOrReason.IsResidenceOwner(resId):
			playerOrReason.ReleaseResidenceActionLock()
			reason = "ChangePlayerResidenceAuthority fail! player [%s] is owner of residence [%s]" % (uid, resId)
			return False, reason, "不能给领地主人增加权限！"
		suc, actionOrReason = self.CheckAuthority(authority, True)
		if not suc:
			playerOrReason.ReleaseResidenceActionLock()
			return False, actionOrReason, actionOrReason
		doInsert = False
		oldAuthority = playerOrReason.GetAllAuthority(resId)
		if not oldAuthority:
			oldAuthority = {}
			doInsert = True
		self.DoApplyAuthorityChange(oldAuthority, actionOrReason)
		playerOrReason.ApplyAuthorityByResId(resId, oldAuthority)
		playerOrReason.ReleaseResidenceActionLock()
		playerId = lobbyGameApi.GetPlayerIdByUid(uid)
		nickname = lobbyGameApi.GetPlayerNickname(playerId)
		if doInsert:
			dbApi.InsertOutPlayerResidenceAuthority(self.mServerType, uid, resId, oldAuthority)
			self.OnInsertAuthority(uid, nickname, resId, mainAuth)
		else:
			dbApi.UpdateOutPlayerResidenceAuthority(self.mServerType, uid, resId, oldAuthority)
		
		return True, oldAuthority, "成功！"
	
	def TryDeletePlayerResidenceAuthority(self, clientId, uid, resId):
		suc, playerOrReason = self.CheckUpdateResidencePlayer(uid)
		if suc:
			resInfo = self.mResidenceMap.get(resId, None)
			if not resInfo:
				playerOrReason.ReleaseResidenceActionLock()
				reason = "ChangePlayerResidenceAuthority fail! residence [%s] not exist" % resId
				return False, reason
			if playerOrReason.IsResidenceOwner(resId):
				playerOrReason.ReleaseResidenceActionLock()
				reason = "ChangePlayerResidenceAuthority fail! player [%s] is owner of residence [%s]" % (uid, resId)
				return False, reason
			playerOrReason.DeleteAuthorityByResId(resId)
			playerOrReason.ReleaseResidenceActionLock()
		dbApi.DeleteOutPlayerAuthorityByUid(self.mServerType, [resId], uid)
		self.OnDeleteAuthority(clientId, uid, resId)
		
	def OnDeleteAuthority(self, clientId, uid, resId):
		"""
		删除曾经生效的的外部玩家针对指定领地的简化版权限
		"""
		if self.mResAuthority.has_key(resId) == True:
			if self.mResAuthority[resId].has_key(uid):
				self.mResAuthority[resId].pop(uid)
		dbApi.DeleteOutPlayerResidenceMainAuthority(self.mServerType, uid, resId)
		self.mSystem.NotifyToClient(clientId, "DeleteAuthorityFromServerEvent", {"uid":uid, "resId":resId})
				
	
	def OnInsertAuthority(self, uid, userName, resId, mainAuth):
		"""
		赋予外部玩家针对指定领地的简化版权限
		"""
		if mainAuth is None:
			realAuthority = {
				"PlacedBlock": True,
				"UseDoor": True,
				"Enter": True
			}
		else:
			realAuthority = mainAuth
		if self.mResAuthority.has_key(resId) == False:
			self.mResAuthority[resId] = {}
		self.mResAuthority[resId][uid] = {"uid": uid, "username": userName, "authority": realAuthority}
		dbApi.InsertOutPlayerResidenceMainAuthority(self.mServerType, uid, resId, realAuthority, userName)
		def QueryPlayerResidenceByResIdCb(records):
			playerUid = -1
			for record in records:
				if record:
					playerUid = record[4]
			if playerUid > 0:
				playerId = lobbyGameApi.GetPlayerIdByUid(playerUid)
				if playerId != "":
					myAuthority = {}
					myAuthority[resId] = {}
					myAuthority[resId][uid] = {"uid":uid, "username":userName, "authority":realAuthority}
					self.mSystem.NotifyToClient(playerId, "UpdateAuthorityFromServerEvent", myAuthority)
		dbApi.QueryPlayerResidenceByResId([resId],QueryPlayerResidenceByResIdCb)

	def OnHttpChangePlayerResidenceAuthority(self, data):
		"""
		处理来自master的为已有领地的一个外部玩家设置权限的运营指令
		"""
		uid, resId, authority = data["uid"], data["resId"], data.get("authority", {})
		suc, dataOrReason = self.TryChangePlayerResidenceAuthority(uid, resId, authority)
		if suc:
			self.OnHttpResidenceSuccess(dataOrReason, data["clientId"])
		else:
			self.OnHttpResidenceFail(dataOrReason, data["clientId"])

	def TryChangeResidenceTeleportPos(self, resId, pos):
		resInfo = self.mResidenceMap.get(resId, None)
		if not resInfo:
			reason = "ChangeResidenceTeleportPos fail! residence [%s] not exist" % resId
			return False, reason
		try:
			bornPos = (int(pos[0]), int(pos[1]), int(pos[2]))
		except:
			reason = "ChangeResidenceTeleportPos fail! pos must (int,int,int) but %s" % str(pos)
			return False, reason
		resInfo["bornPos"] = bornPos
		resInfo["version"] = int(time.time())
		dbApi.ChangeResidenceTeleportPos(self.mServerType, resId, util.ListToString(bornPos))
		return True, resInfo

	def OnHttpChangeResidenceBornPos(self, data):
		"""
		处理来自master的为已有领地修改传送点的运营指令
		"""
		suc, dataOrReason = self.TryChangeResidenceTeleportPos(data["resId"], data["pos"])
		if suc:
			self.OnHttpResidenceSuccess(dataOrReason, data["clientId"])
		else:
			self.OnHttpResidenceFail(dataOrReason, data["clientId"])

	def TryReleasePlayerResidenceLock(self, uid):
		player = util.GetResidenceSystem().GetPlayerMgr().GetPlayerByUid(uid)
		if not player:
			return False, "ReleasePlayerResidenceLock fail! player [%s] is not online" % uid
		player.ReleaseResidenceActionLock()
		return True, {}

	def OnHttpReleasePlayerResidenceLock(self, data):
		"""
		处理来自master的为指定玩家解除领地操作并发锁（用于限制并发）的运营指令（此指令是为了解除某些不可预知的原因导致的某个玩家被锁定在操作中，无法执行领地相关操作的状态）
		"""
		suc, dataOrReason = self.TryReleasePlayerResidenceLock(data["uid"])
		if suc:
			self.OnHttpResidenceSuccess(dataOrReason, data["clientId"])
		else:
			self.OnHttpResidenceFail(dataOrReason, data["clientId"])

	# 尝试把指定玩家传送到指定领地（需要拥有外部玩家特殊权限，或者是领地的所有者）
	def TryTeleportPlayerToResidence(self, resId, uid):
		resInfo = self.mResidenceMap.get(resId, None)
		if not resInfo:
			return False, "teleport player to residence fail! residence [%s] not exist" % resId
		player = util.GetResidenceSystem().GetPlayerMgr().GetPlayerByUid(uid)
		if not player:
			return False, "teleport player to residence fail! player [%s] not exist" % uid
		playerId = player.mPlayerId
		if player.IsResidenceOwner(resId):
			canPlayerTeleport = True
		else:
			canPlayerTeleport = player.FindPlayerAuthority("can_other_player_teleport", resInfo["id"])
			if canPlayerTeleport is None:
				canPlayerTeleport = resInfo["authority"].get("can_other_player_teleport", None)
				if canPlayerTeleport is None:
					canPlayerTeleport = util.GetModConfByField("can_other_player_teleport")
		if not canPlayerTeleport:
			return False, "teleport player to residence fail! player cannot teleport by authority limit"
		oldDim = util.GetEntityDimensionId(player.mPlayerId)
		if oldDim == resInfo["dimension"]:
			util.ChangeEntityPos(playerId, resInfo["bornPos"])
		else:
			util.ChangePlayerDimension(playerId, resInfo["dimension"], resInfo["bornPos"])
		return True, resInfo
	# ---------------------------------------------------------------------------------------------
	def SyncResidenceToAllPlayer(self):
		pass

	def Destroy(self):
		if not self.mQueryIdTimer is None:
			comp = serverApi.CreateComponent(serverApi.GetLevelId(), "Minecraft", "game")
			comp.CancelTimer(self.mQueryIdTimer)
			self.mQueryIdTimer = None
		self.mSystem.UnListenForEvent(residenceConsts.ModNameSpace, residenceConsts.MasterSystemName,
									residenceConsts.QueryServerResidenceEvent, self, self.OnQueryServerResidence)
		self.mSystem.UnListenForEvent(residenceConsts.ModNameSpace, residenceConsts.MasterSystemName,
									residenceConsts.SetPlayerResidenceEvent, self, self.OnSetPlayerResidence)
		self.mSystem.UnListenForEvent(residenceConsts.ModNameSpace, residenceConsts.MasterSystemName,
									residenceConsts.HttpDelResidenceEvent, self, self.OnHttpDelResidence)
		self.mSystem.UnListenForEvent(residenceConsts.ModNameSpace, residenceConsts.MasterSystemName,
									residenceConsts.AddPlayerToResidenceEvent, self, self.OnHttpAddPlayerToResidence)
		self.mSystem.UnListenForEvent(residenceConsts.ModNameSpace, residenceConsts.MasterSystemName,
									residenceConsts.RemovePlayerFromResidenceEvent, self,
									self.OnHttpRemovePlayerFromResidence)
		self.mSystem.UnListenForEvent(residenceConsts.ModNameSpace, residenceConsts.MasterSystemName,
									residenceConsts.ChangeResidenceAuthorityEvent, self,
									self.OnHttpChangeResidenceAuthority)
		self.mSystem.UnListenForEvent(residenceConsts.ModNameSpace, residenceConsts.MasterSystemName,
									residenceConsts.ChangePlayerResidenceAuthorityEvent, self,
									self.OnHttpChangePlayerResidenceAuthority)
		self.mSystem.UnListenForEvent(residenceConsts.ModNameSpace, residenceConsts.MasterSystemName,
									residenceConsts.ChangeResidenceBornPosEvent, self,
									self.OnHttpChangeResidenceBornPos)
		self.mSystem.UnListenForEvent(residenceConsts.ModNameSpace, residenceConsts.MasterSystemName,
									residenceConsts.ReleasePlayerResidenceLockEvent, self,
									self.OnHttpReleasePlayerResidenceLock)
		self.mSystem = None
