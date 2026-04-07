# -*- coding: utf-8 -*-
import neteaseResidenceScript.residenceBaseMgr as residenceBaseMgr
import neteaseResidenceScript.residenceConsts as residenceConsts
import neteaseResidenceScript.util as util
import neteaseResidenceScript.effect.effectFunc as effectFunc
import neteaseResidenceScript.ui.uiDef as uiDef

class ResidenceGacMgr(residenceBaseMgr.ResidenceBaseMgr):
	"""
	客户端领地管理类
	"""
	def __init__(self, system):
		import weakref
		self.SHOW_RES_EFFECT = True
		self.mSystem = weakref.proxy(system)
		residenceBaseMgr.ResidenceBaseMgr.__init__(self, system)
		self.mSystem.ListenForEvent(residenceConsts.ModNameSpace, residenceConsts.ServerSystemName,
							residenceConsts.SyncResidenceDataEvent, self, self.OnSyncResidenceData)
		self.mSystem.ListenForEvent(residenceConsts.ModNameSpace, residenceConsts.ServerSystemName,
		                            residenceConsts.DelResidenceFromServerEvent, self, self.OnDelResidenceFromServerEvent)
		self.mSystem.ListenForEvent(residenceConsts.ModNameSpace, residenceConsts.ServerSystemName,
		                    residenceConsts.RemovePlayerResidentFromServerEvent, self, self.OnRemovePlayerResidentFromServerEvent)
		self.mSystem.ListenForEvent(residenceConsts.ModNameSpace, residenceConsts.ServerSystemName,"UpdateApplicationFromServerEvent", self,
		                            self.OnUpdateApplicationFromServerEvent)
		self.mSystem.ListenForEvent(residenceConsts.ModNameSpace, residenceConsts.ServerSystemName,"UpdateAuthorityFromServerEvent", self,
		                            self.OnUpdateAuthorityFromServerEvent)
		self.mSystem.ListenForEvent(residenceConsts.ModNameSpace, residenceConsts.ServerSystemName,"RemoveApplicationFromServerEvent", self, self.OnRemoveApplicationFromServerEvent)
		self.mSystem.ListenForEvent(residenceConsts.ModNameSpace, residenceConsts.ServerSystemName,"ChangeAuthFromServerEvent", self, self.OnChangeAuthFromServerEvent)
		self.mSystem.ListenForEvent(residenceConsts.ModNameSpace, residenceConsts.ServerSystemName,"DeleteAuthorityFromServerEvent", self, self.OnDeleteAuthorityFromServerEvent)
		self.mSystem.ListenForEvent(residenceConsts.ModNameSpace, residenceConsts.ServerSystemName,"SureDeleteAuthFromServerEvent", self, self.OnSureDeleteAuthFromServerEvent)
		self.mSystem.ListenForEvent(residenceConsts.ModNameSpace, residenceConsts.ServerSystemName,"updateNewEnterAuthFromServerEvent", self, self.OnUpdateNewEnterAuthFromServerEvent)
		self.mSystem.ListenForEvent(residenceConsts.ModNameSpace, residenceConsts.ServerSystemName,"UpdateNewApplicationFromServerEvent", self, self.OnUpdateNewApplicationFromServerEvent)
		self.mSystem.ListenForEvent(residenceConsts.ModNameSpace, residenceConsts.ServerSystemName,"UpdateTransferUnreadFromServerEvent", self, self.OnUpdateTransferUnreadFromServerEvent)
		self.mSystem.ListenForEvent(residenceConsts.ModNameSpace, residenceConsts.ServerSystemName,"UpdateApplicatorUnreadFromServerEvent", self, self.OnUpdateApplicatorUnreadFromServerEvent)
		
		self.mHasDrawResidence = {} #resId, resInfo
		
		self.mResApplication = {}
		self.mResAuthority = {}
		
		self.mTransferResIdUnRead = set()
		self.mApplicatorUidUnRead = {}
		
	def OnUpdateTransferUnreadFromServerEvent(self, args):
		"""
		更新未读的传动到领地申请提示（小红点）
		"""
		unRead = args.get("unRead")
		for keys in uiDef.UIData.keys():
			ui = self.mSystem.mUIMgr.GetUI(keys)
			print keys, ui
			ui.ShowTransferMainNewImg( len(unRead) > 0 )
		self.mTransferResIdUnRead = set(unRead)
		
	def OnUpdateApplicatorUnreadFromServerEvent(self, args):
		"""
		更新未读的权限申请提示（小红点）
		"""
		unRead = args.get("unRead")
		for keys in uiDef.UIData.keys():
			ui = self.mSystem.mUIMgr.GetUI(keys)
			print keys, ui
			ui.ShowManageMainNewImg( len(unRead) > 0 )
		self.mApplicatorUidUnRead = unRead
		

	def OnUpdateNewEnterAuthFromServerEvent(self, args):
		"""
		发出的传送到领地申请通过了
		"""
		resId = args.get("resId")
		self.mTransferResIdUnRead.add(resId)
		#新的请求到来了
		# TransferUi = self.mSystem.mUIMgr.GetUI(uiDef.UIDef.UIResidenceTransfer)
		# if TransferUi:
		# 	if TransferUi.mIsShow == True:
		# 		return
		for keys in uiDef.UIData.keys():
			ui =  self.mSystem.mUIMgr.GetUI(keys)
			ui.ShowTransferMainNewImg(True)
		
	def OnUpdateNewApplicationFromServerEvent(self, args):
		"""
		发出的权限申请通过了
		"""
		resId = args.get("resId")
		applicatorUid = args.get("applicatorUid")
		if resId not in self.mApplicatorUidUnRead:
			self.mApplicatorUidUnRead[resId] = []
		if applicatorUid not in self.mApplicatorUidUnRead:
			self.mApplicatorUidUnRead[resId].append(applicatorUid)
			
		for keys in uiDef.UIData.keys():
			ui =  self.mSystem.mUIMgr.GetUI(keys)
			ui.ShowManageMainNewImg(True)
		
		
	def UpdateTransferResIdListState(self, resList, isShow):
		"""
		更新传送申请状态为已读
		"""
		if isShow:
			for resData in resList:
				resId = resData["resId"]
				self.mTransferResIdUnRead.discard(resId)
			for keys in uiDef.UIData.keys():
				ui =  self.mSystem.mUIMgr.GetUI(keys)
				ui.ShowTransferMainNewImg(False)
				
	def UpdateApplicatorListState(self, chosenResId, isShow):
		"""
		更新权限申请状态为已读
		"""
		if isShow:
			if self.mApplicatorUidUnRead.has_key(chosenResId):
				self.mApplicatorUidUnRead.pop(chosenResId)
			for keys in uiDef.UIData.keys():
				ui =  self.mSystem.mUIMgr.GetUI(keys)
				print "UpdateApplicatorListState", self.mApplicatorUidUnRead
				ui.ShowManageMainNewImg(len(self.mApplicatorUidUnRead) > 0)
				
		
	def OnDeleteAuthorityFromServerEvent(self, args):
		"""
		针对特定领地的简化版权限被删除了
		"""
		resId = args.get("resId")
		uid = args.get("uid")
		if self.mResAuthority.has_key(resId) == True:
			if self.mResAuthority[resId].has_key(uid):
				self.mResAuthority[resId].pop(uid)
				ui = self.mSystem.mUIMgr.GetUI(uiDef.UIDef.UIResidenceManage)
				if ui:
					ui.RefreshUser()
	
	def OnChangeAuthFromServerEvent(self, args):
		"""
		针对特定领地的简化版权限被修改了
		"""
		resId = args.get("resId")
		uid = args.get("uid")
		changeAuth = args.get("changeAuth")
		state = args.get("state")
		if self.mResAuthority.has_key(resId) == False:
			return
		if self.mResAuthority[resId].has_key(uid) == False:
			return
		self.mResAuthority[resId][uid]["authority"][changeAuth] = state
		manageUi = self.mSystem.mUIMgr.GetUI(uiDef.UIDef.UIResidenceManage)
		if manageUi:
			manageUi.ShowBtnImgs(uid, changeAuth, state)
			
			
	def OnSureDeleteAuthFromServerEvent(self, args):
		"""
		针对特定领地的简化版权限被修改后，所有权限都丢失了（等价于被删除）
		"""
		manageUi = self.mSystem.mUIMgr.GetUI(uiDef.UIDef.UIResidenceManage)
		if manageUi:
			manageUi.OnShowSurePanel(args)
		
	def OnUpdateApplicationFromServerEvent(self, args):
		'''
		更新特殊权限申请列表
		'''
		myApplication = args
		for resId, oneResApply in myApplication.iteritems():
			if self.mResApplication.has_key(resId) == False:
				self.mResApplication[resId] = {}
			for uid, oneUidApply in oneResApply.iteritems():
				self.mResApplication[resId][uid] = oneUidApply
		
		ui =  self.mSystem.mUIMgr.GetUI(uiDef.UIDef.UIResidenceManage)
		if ui:
			ui.RefreshApplicator()
				
	def OnRemoveApplicationFromServerEvent(self, args):
		"""
		特殊权限申请处理完毕
		"""
		applicatorUid = args.get("applicatorUid")
		resId = args.get("resId")
		if self.mResApplication.has_key(resId):
			if self.mResApplication[resId].has_key(applicatorUid):
				self.mResApplication[resId].pop(applicatorUid)
		
		ui = self.mSystem.mUIMgr.GetUI(uiDef.UIDef.UIResidenceManage)
		if ui:
			ui.RefreshApplicator()
		
				
	def OnUpdateAuthorityFromServerEvent(self, args):
		'''
		更新权限列表
		'''
		print "OnUpdateAuthorityFromServerEvent", args
		myAuthority = args
		for resId, oneAuthority in myAuthority.iteritems():
			if self.mResAuthority.has_key(resId) == False:
				self.mResAuthority[resId] = {}
			for uid, oneUidAuthority in oneAuthority.iteritems():
				self.mResAuthority[resId][uid] = oneUidAuthority
		ui = self.mSystem.mUIMgr.GetUI(uiDef.UIDef.UIResidenceManage)
		if ui:
			ui.RefreshUser()
				
		
	def OnDelResidenceFromServerEvent(self, data):
		"""
		有领地被删除了
		"""
		delResIdList = data.get("delResIdList")
		for delid in  delResIdList:
			if self.mHasDrawResidence.has_key(delid):
				resFrameList = self.mHasDrawResidence[delid]["resFrameList"]
				effectFunc.StopResidenceBox(resFrameList)
				self.mHasDrawResidence.pop(delid)
				self.DelResidenceByResidenceId(delid)
				
	def OnRemovePlayerResidentFromServerEvent(self, data):
		"""
		玩家从领地中被移除
		"""
		print "OnRemovePlayerResidentFromServerEvent", data
		removePlayerResId = data["removePlayerResId"]
		self.mSystem.GetPlayerGac().LeaveResidence(removePlayerResId)

	def OnSyncResidenceData(self, data):
		"""
		领地数据同步
		"""
		print 'OnSyncResidenceData', data["needSyncList"]
		for resInfo in data["needSyncList"]:
			self.AddOneResidence(resInfo)
			resId = resInfo["id"]
			if self.mHasDrawResidence.has_key(resId):
				if self.mHasDrawResidence[resId]["minPos"] == resInfo.get("minPos") and self.mHasDrawResidence[resId]["maxPos"] == resInfo.get("maxPos"):
					continue
				else:
					resFrameList = self.mHasDrawResidence[resId]["resFrameList"]
					effectFunc.StopResidenceBox(resFrameList)
			print "OnSyncResidenceData", resId, self.SHOW_RES_EFFECT
			resInfo["resFrameList"] = effectFunc.DrawResidenceBox(resInfo.get("minPos"), resInfo.get("maxPos"), show = self.SHOW_RES_EFFECT)
			self.mHasDrawResidence[resId] = resInfo
	
	def set_show_res_effect(self, isShow):
		self.SHOW_RES_EFFECT = isShow
		for resId in self.mHasDrawResidence.keys():
			resInfo = self.mHasDrawResidence[resId]
			resFrameList = self.mHasDrawResidence[resId]["resFrameList"]
			effectFunc.StopResidenceBox(resFrameList)
			resInfo["resFrameList"] = effectFunc.DrawResidenceBox(resInfo.get("minPos"), resInfo.get("maxPos"), show=self.SHOW_RES_EFFECT)
			self.mHasDrawResidence[resId] = resInfo
			
			
			
			
	# 指定玩家在当前位置是否行为受限，返回是否受限，或具体权限信息
	# 非领地玩家行为不受限
	# 玩家是领地所有者，行为不受限
	# 玩家是领地外部人员，根据具体情况返回配置的结果，最终使用mod.json保底
	def GetLimitAndAuthorityByResidence(self, player, dim, pos, aukey):
		resInfoList = self.FindResidenceByPos(dim, pos)
		if not resInfoList:  # 非领地玩家行为不受限
			return False, None
		topLevelResId = resInfoList[-1]["id"]
		if player.IsResidenceOwner(topLevelResId):  # 玩家是领地所有者，行为不受限
			return False, None
		# 对于领地外部人员的限制，部分权限需要考虑玩家个体限制，部分权限不需要考虑
		auValue = self.GetAuthorityMutex(aukey, resInfoList, player)
		return None, auValue

	def GetAuthorityMutex(self, aukey, resInfoList, player):
		usePlayer = residenceConsts.AuthorityForPlayer.get(aukey, False)
		if usePlayer:
			auValue = self.GetAuthorityWithPlayer(aukey, resInfoList, player)
		else:
			auValue = self.GetAuthorityWithoutPlayer(aukey, resInfoList)
		return auValue

	def GetAuthorityWithPlayer(self, aukey, resInfoList, player):
		for resInfo in resInfoList:
			# 如果玩家独立配置了领地权限
			# 那么玩家自身的权限配置拥有最高的优先级
			ret = player.FindPlayerAuthority(aukey, resInfo["id"])
			if not ret is None:
				return ret
			# 否则查看子领地权限
			ret = resInfo["authority"].get(aukey, None)
			if not ret is None:
				return ret
		# 最终保底还是返回mod.json的默认值
		return util.GetModConfByField(aukey)

	def GetAuthorityWithoutPlayer(self, aukey, resInfoList):
		for resInfo in resInfoList:
			ret = resInfo["authority"].get(aukey, None)
			if not ret is None:
				return ret
		# 最终保底还是返回mod.json的默认值
		return util.GetModConfByField(aukey)
