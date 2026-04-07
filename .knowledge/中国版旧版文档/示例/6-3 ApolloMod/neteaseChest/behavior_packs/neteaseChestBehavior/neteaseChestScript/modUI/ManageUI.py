# -*- coding: utf-8 -*-
import client.extraClientApi as clientApi
ViewBinder = clientApi.GetViewBinderCls()
ViewRequest = clientApi.GetViewViewRequestCls()
ScreenNode = clientApi.GetScreenNodeCls()
import time
import chestConsts as chestConsts
from chestConsts import UIDef

class ManageScreen(ScreenNode):
	def __init__(self,namespace,name,param):
		ScreenNode.__init__(self, namespace, name, param)
		print "===%s===" % "init ManageScreen"
		
		self.mManagePanel = "/ManagePanel"
		self.mManageImg = self.mManagePanel + "/apply_img"
		self.mUserListImg = self.mManageImg + "/userlist_img"
		self.mApplicatorlistImg = self.mManageImg + "/applicatorlist_img"
		
		self.mTitleLbl = self.mManageImg + "/manage_title_lbl"
		self.mOwnerLbl = self.mManageImg + "/gamer_title_lbl"
		self.mCloseBtn = self.mManageImg + "/close_btn"
		self.mPlayerId = clientApi.GetLocalPlayerId()  # 获取客户端本地玩家的playerId
		
		self.userIdList = []
		self.applicatorIdList = []
		
		self.mCid = -1
		self.mPos = None
		self.blockText = "容器"
	
	def InitScreen(self):
		print "InitScreen ManageScreen"
		self.SetVisible(self.mManagePanel, False)
		chestConsts.GetClientModSystem().ListenForEvent(chestConsts.ModNameSpace, chestConsts.ServerSystemName,chestConsts.ShowChestManageFromServerEvent, self,self.OnShowChestManage)
		
	def OnShowChestManage(self, args):
		clientApi.SetInputMode(1)
		ownerList = args.get("ownerList")
		userList = args.get("userList")
		applicatorList = args.get("applicatorList")
		if args.has_key("blockText"):
			self.blockText = args["blockText"]
		self.SetText(self.mOwnerLbl, "你是当前%s拥有者"%self.blockText)
		self.SetText(self.mTitleLbl, "%s管理"%self.blockText)
		self.mCid = args.get("cid")
		if args.has_key("pos"):
			self.mPos = args["pos"]
		self.ShowUserList(userList)
		self.ShowApplicatorList(applicatorList)
		self.SetVisible(self.mManagePanel, True)
		clientApi.HideSlotBarGui(True)
	
	def ShowUserList(self, userList):
		print "ShowUserList", userList
		userNum = len(userList)
		self.SetText(self.mUserListLbl, "其他%s的使用者（%s / 5）" % (self.blockText, str(userNum)))
		if userNum <= 0:
			self.SetVisible(self.mUserImg, False)
		else:
			self.SetVisible(self.mUserImg, True)
		deltaNum = userNum - len(self.mUserImgs)
		if deltaNum > 0:
			for i in xrange(len(self.mUserImgs) + 1, userNum + 1):
				userImg = "user_img_%s" % i
				userImgPath = '%s/%s' % (self.mUserListPanel, userImg)
				userNameLabelPath = '%s/%s' % (userImgPath, self.mUserNameLabel)
				deleteBtnPath = '%s/%s' % (userImgPath, self.mUserDeleteBtn)
				self.Clone(self.mUserImg, self.mUserListPanel, userImg)
				self.mUserImgs.append(userImgPath)
				self.mUserNameLabels.append(userNameLabelPath)
				self.mUserDeleteBtns.append(deleteBtnPath)
		elif deltaNum < 0:
			for i in xrange(userNum + 1, len(self.mUserImgs) + 1):
				if i == 1:
					continue
				print 'removing user ', i
				userImg = "user_img_%s" % i
				userImgPath = '%s/%s' % (self.mUserListPanel, userImg)
				userNameLabelPath = '%s/%s' % (userImgPath, self.mUserNameLabel)
				deleteBtnPath = '%s/%s' % (userImgPath, self.mUserDeleteBtn)
				self.RemoveComponent(userImgPath, self.mUserListPanel)
				self.mUserImgs.remove(userImgPath)
				self.mUserNameLabels.remove(userNameLabelPath)
				self.mUserDeleteBtns.remove(deleteBtnPath)
				# 其余情况，正常显示
		d = self.GetSize(self.mUserImg)[1]
		for i, userImg in enumerate(self.mUserImgs):
			self.SetPosition(userImg, (self.mUserImgPos[0], self.mUserImgPos[1] + d * i))
		i = 0
		self.userIdList = []
		for uid, nickName in userList.items():
			self.userIdList.append(uid)
			self.SetText(self.mUserNameLabels[i], nickName.encode('utf-8'))
			i = i + 1
		
		height = 10 + i * (10 + d)
		height = max(height, self.mUserListPanelSize[1])
		self.SetSize(self.mUserListPanel, (self.mUserListPanelSize[0], height))
		
	def ShowApplicatorList(self, applicatorList):
		print "ShowApplicatorList", applicatorList
		self.SetText(self.mApplicatorListLbl, "申请使用%s的玩家" % (self.blockText))
		applicatorNum = len(applicatorList)
		if applicatorNum <= 0:
			print "ShowApplicatorList2 ", self.mApplicatorImg
			self.SetVisible(self.mApplicatorImg, False)
		else:
			self.SetVisible(self.mApplicatorImg, True)
		deltaNum = applicatorNum - len(self.mApplicatorImgs)
		print "deltaNum", deltaNum, self.mApplicatorImgs
		if deltaNum > 0:
			for i in xrange(len(self.mApplicatorImgs) + 1, applicatorNum + 1):
				applyImg = "apply_img_%s" % i
				applyImgPath = '%s/%s' % (self.mApplicatorListPanel, applyImg)
				applicatorNameLabelPath = '%s/%s' % (applyImgPath, self.mApplicatorNameLabel)
				acceptBtnPath = '%s/%s' % (applyImgPath, self.mApplicatorAcceptBtn)
				refuseBtnPath = '%s/%s' % (applyImgPath, self.mApplicatorRefuseBtn)
				self.Clone(self.mApplicatorImg, self.mApplicatorListPanel, applyImg)
				self.mApplicatorImgs.append(applyImgPath)
				self.mApplicatorNameLabels.append(applicatorNameLabelPath)
				self.mApplicatorAcceptBtns.append(acceptBtnPath)
				self.mApplicatorRefuseBtns.append(refuseBtnPath)
		elif deltaNum < 0:
			for i in xrange(applicatorNum + 1, len(self.mApplicatorImgs) + 1):
				if i == 1:
					continue
				print 'removing applicator ', i
				applyImg = "apply_img_%s" % i
				applyImgPath = '%s/%s' % (self.mApplicatorListPanel, applyImg)
				applicatorNameLabelPath = '%s/%s' % (applyImgPath, self.mApplicatorNameLabel)
				acceptBtnPath = '%s/%s' % (applyImgPath, self.mApplicatorAcceptBtn)
				refuseBtnPath = '%s/%s' % (applyImgPath, self.mApplicatorRefuseBtn)
				self.RemoveComponent(applyImgPath, self.mApplicatorListPanel)
				self.mApplicatorImgs.remove(applyImgPath)
				self.mApplicatorNameLabels.remove(applicatorNameLabelPath)
				self.mApplicatorAcceptBtns.remove(acceptBtnPath)
				self.mApplicatorRefuseBtns.remove(refuseBtnPath)
		# 其余情况，正常显示
		d = self.GetSize(self.mApplicatorImg)[1]
		for i, applicatorImg in enumerate(self.mApplicatorImgs):
			self.SetPosition(applicatorImg, (self.mApplicatorImgPos[0], self.mApplicatorImgPos[1] + d * i))
		i = 0
		self.applicatorIdList = []
		for uid, nickName in applicatorList.items():
			self.applicatorIdList.append(uid)
			self.SetText(self.mApplicatorNameLabels[i], nickName.encode('utf-8'))
			i = i + 1
		
		height = 10 + i * (10 + d)
		height = max(height, self.mUserListPanelSize[1])
		self.SetSize(self.mApplicatorListPanel, (self.mApplicatorListPanelSize[0], height))
		
	def Create(self):
		pass
		#==================================== 使用者列表
		userlist_scrollBase = self.mUserListImg + "/userlist_scroll_base"
		userlist_scrollBaseTouch = userlist_scrollBase + "/scroll_touch/scroll_view/panel/background_and_viewport/scrolling_view_port/scrolling_content"
		userlist_size = self.GetSize(userlist_scrollBaseTouch)
		if userlist_size:
			self.mUserListPanel = userlist_scrollBaseTouch
			self.mUserListPanelSize = userlist_size
		else:
			userlist_scrollBaseMouse = userlist_scrollBase + "/scroll_mouse/scroll_view/stack_panel/background_and_viewport/scrolling_view_port/scrolling_content"
			userlist_size = self.GetSize(userlist_scrollBaseMouse)
			self.mUserListPanel = userlist_scrollBaseMouse
			self.mUserListPanelSize = userlist_size
		
		self.mApplicatorListLbl = self.mApplicatorlistImg + "/applicatorlist_lbl"
		self.mUserNameLabel = "user_lbl_1"
		self.mUserDeleteBtn = "delete_btn_1"
		self.mUserImg = self.mUserListPanel + "/user_img_1"
		self.mUserImgs = [
			self.mUserImg
		]
		self.mUserNameLabels = [
			self.mUserImg + "/" + self.mUserNameLabel
		]
		self.mUserDeleteBtns = [
			self.mUserImg + "/" + self.mUserDeleteBtn
		]
		self.mUserImgPos = self.GetPosition(self.mUserImg)
		#============================================================= 申请者列表
		applicatorlist_scrollBase = self.mApplicatorlistImg + "/applicatorlist_scroll_base"
		applicatorlist_scrollBaseTouch = applicatorlist_scrollBase + "/scroll_touch/scroll_view/panel/background_and_viewport/scrolling_view_port/scrolling_content"
		applicatorlist_size = self.GetSize(applicatorlist_scrollBaseTouch)
		if applicatorlist_size:
			self.mApplicatorListPanel = applicatorlist_scrollBaseTouch
			self.mApplicatorListPanelSize = applicatorlist_size
		else:
			applicatorlist_scrollBaseMouse = applicatorlist_scrollBase + "/scroll_mouse/scroll_view/stack_panel/background_and_viewport/scrolling_view_port/scrolling_content"
			applicatorlist_size = self.GetSize(applicatorlist_scrollBaseMouse)
			self.mApplicatorListPanel = applicatorlist_scrollBaseMouse
			self.mApplicatorListPanelSize = applicatorlist_size
		self.mUserListLbl = self.mUserListImg + "/userlist_lbl"
		self.mApplicatorNameLabel = "applicator_lbl_1"
		self.mApplicatorAcceptBtn = "accept_btn_1"
		self.mApplicatorRefuseBtn = "refuse_btn_1"
		self.mApplicatorImg = self.mApplicatorListPanel + "/apply_img_1"
		self.mApplicatorImgs = [
			self.mApplicatorImg
		]
		self.mApplicatorNameLabels = [
			self.mApplicatorImg + "/" + self.mApplicatorNameLabel
		]
		self.mApplicatorAcceptBtns = [
			self.mApplicatorImg + "/" + self.mApplicatorAcceptBtn
		]
		self.mApplicatorRefuseBtns = [
			self.mApplicatorImg + "/" + self.mApplicatorRefuseBtn
		]
		self.mApplicatorImgPos = self.GetPosition(self.mApplicatorImg)
		self.AddTouchEventHandler(self.mCloseBtn, self.ClosePanel)
		for index, deleteBtnPath in enumerate(self.mUserDeleteBtns):
			self.AddTouchEventHandler(deleteBtnPath, self.DeleteUser)

		for index, acceptBtnPath in enumerate(self.mApplicatorAcceptBtns):
			self.AddTouchEventHandler(acceptBtnPath, self.AcceptUser)

		for index, refuseBtnPath in enumerate(self.mApplicatorRefuseBtns):
			self.AddTouchEventHandler(refuseBtnPath, self.RefuseUser)
			
	def ClosePanel(self, args=None):
		print "======%s========" % "ClosePanel"
		self.SetVisible(self.mManagePanel, False)
		clientApi.SetInputMode(0)
		clientApi.HideSlotBarGui(False)
			
	def DeleteUser(self, args):
		touchEvent = args["TouchEvent"]
		touch_event_enum = clientApi.GetMinecraftEnum().TouchEvent
		if touchEvent == touch_event_enum.TouchUp:
			self.SetSprite(args["ButtonPath"] + '/default', "textures/ui/netease_chest/btn02@3x.png")
			self.SetSprite(args["ButtonPath"] + '/hover', "textures/ui/netease_chest/btn02@3x.png")
			self.SetSprite(args["ButtonPath"] + '/pressed', "textures/ui/netease_chest/btn02@3x.png")
			uidIndex = self.GetDeleteUidIndex(args["ButtonPath"])
			uid = self.userIdList[uidIndex]
			data = {'opPlayerId':self.mPlayerId, "pos":self.mPos, 'uid': uid, 'cid': self.mCid}
			chestConsts.GetClientModSystem().NotifyToServer(chestConsts.DeletUserFromClientEvent, data)
		elif touchEvent == touch_event_enum.TouchDown:
			self.SetSprite(args["ButtonPath"] + '/default', "textures/ui/netease_chest/btn02_click@3x.png")
			self.SetSprite(args["ButtonPath"] + '/hover', "textures/ui/netease_chest/btn02_click@3x.png")
			self.SetSprite(args["ButtonPath"] + '/pressed', "textures/ui/netease_chest/btn02_click@3x.png")
		elif touchEvent == touch_event_enum.TouchCancel:
			self.SetSprite(args["ButtonPath"] + '/default', "textures/ui/netease_chest/btn02@3x.png")
			self.SetSprite(args["ButtonPath"] + '/hover', "textures/ui/netease_chest/btn02@3x.png")
			self.SetSprite(args["ButtonPath"] + '/pressed', "textures/ui/netease_chest/btn02@3x.png")
		elif touchEvent == touch_event_enum.TouchMove:
			self.SetSprite(args["ButtonPath"] + '/default', "textures/ui/netease_chest/btn02@3x.png")
			self.SetSprite(args["ButtonPath"] + '/hover', "textures/ui/netease_chest/btn02@3x.png")
			self.SetSprite(args["ButtonPath"] + '/pressed', "textures/ui/netease_chest/btn02@3x.png")
		else:
			self.SetSprite(args["ButtonPath"] + '/default', "textures/ui/netease_chest/btn02@3x.png")
			self.SetSprite(args["ButtonPath"] + '/hover', "textures/ui/netease_chest/btn02@3x.png")
			self.SetSprite(args["ButtonPath"] + '/pressed', "textures/ui/netease_chest/btn02@3x.png")
			
	def AcceptUser(self, args):
		touchEvent = args["TouchEvent"]
		touch_event_enum = clientApi.GetMinecraftEnum().TouchEvent
		if touchEvent == touch_event_enum.TouchUp:
			self.SetSprite(args["ButtonPath"] + '/default', "textures/ui/netease_chest/btn02@3x.png")
			self.SetSprite(args["ButtonPath"] + '/hover', "textures/ui/netease_chest/btn02@3x.png")
			self.SetSprite(args["ButtonPath"] + '/pressed', "textures/ui/netease_chest/btn02@3x.png")
			uidIndex = self.GetAcceptUidIndex(args["ButtonPath"])
			uid = self.applicatorIdList[uidIndex]
			data = {'opPlayerId':self.mPlayerId, "pos":self.mPos, 'uid': uid, 'cid': self.mCid}
			chestConsts.GetClientModSystem().NotifyToServer(chestConsts.AcceptUserFromClientEvent, data)
		elif touchEvent == touch_event_enum.TouchDown:
			self.SetSprite(args["ButtonPath"] + '/default', "textures/ui/netease_chest/btn02_click@3x.png")
			self.SetSprite(args["ButtonPath"] + '/hover', "textures/ui/netease_chest/btn02_click@3x.png")
			self.SetSprite(args["ButtonPath"] + '/pressed', "textures/ui/netease_chest/btn02_click@3x.png")
		elif touchEvent == touch_event_enum.TouchCancel:
			self.SetSprite(args["ButtonPath"] + '/default', "textures/ui/netease_chest/btn02@3x.png")
			self.SetSprite(args["ButtonPath"] + '/hover', "textures/ui/netease_chest/btn02@3x.png")
			self.SetSprite(args["ButtonPath"] + '/pressed', "textures/ui/netease_chest/btn02@3x.png")
		elif touchEvent == touch_event_enum.TouchMove:
			self.SetSprite(args["ButtonPath"] + '/default', "textures/ui/netease_chest/btn02@3x.png")
			self.SetSprite(args["ButtonPath"] + '/hover', "textures/ui/netease_chest/btn02@3x.png")
			self.SetSprite(args["ButtonPath"] + '/pressed', "textures/ui/netease_chest/btn02@3x.png")
		else:
			self.SetSprite(args["ButtonPath"] + '/default', "textures/ui/netease_chest/btn02@3x.png")
			self.SetSprite(args["ButtonPath"] + '/hover', "textures/ui/netease_chest/btn02@3x.png")
			self.SetSprite(args["ButtonPath"] + '/pressed', "textures/ui/netease_chest/btn02@3x.png")
			
	def RefuseUser(self, args):
		touchEvent = args["TouchEvent"]
		touch_event_enum = clientApi.GetMinecraftEnum().TouchEvent
		if touchEvent == touch_event_enum.TouchUp:
			self.SetSprite(args["ButtonPath"] + '/default', "textures/ui/netease_chest/btn02@3x.png")
			self.SetSprite(args["ButtonPath"] + '/hover', "textures/ui/netease_chest/btn02@3x.png")
			self.SetSprite(args["ButtonPath"] + '/pressed', "textures/ui/netease_chest/btn02@3x.png")
			uidIndex = self.GetRefuseUidIndex(args["ButtonPath"])
			uid = self.applicatorIdList[uidIndex]
			data = {'opPlayerId':self.mPlayerId, "pos":self.mPos, 'uid': uid, 'cid': self.mCid}
			chestConsts.GetClientModSystem().NotifyToServer(chestConsts.RefuseUserFromClientEvent, data)
		elif touchEvent == touch_event_enum.TouchDown:
			self.SetSprite(args["ButtonPath"] + '/default', "textures/ui/netease_chest/btn02_click@3x.png")
			self.SetSprite(args["ButtonPath"] + '/hover', "textures/ui/netease_chest/btn02_click@3x.png")
			self.SetSprite(args["ButtonPath"] + '/pressed', "textures/ui/netease_chest/btn02_click@3x.png")
		elif touchEvent == touch_event_enum.TouchCancel:
			self.SetSprite(args["ButtonPath"] + '/default', "textures/ui/netease_chest/btn02@3x.png")
			self.SetSprite(args["ButtonPath"] + '/hover', "textures/ui/netease_chest/btn02@3x.png")
			self.SetSprite(args["ButtonPath"] + '/pressed', "textures/ui/netease_chest/btn02@3x.png")
		elif touchEvent == touch_event_enum.TouchMove:
			self.SetSprite(args["ButtonPath"] + '/default', "textures/ui/netease_chest/btn02@3x.png")
			self.SetSprite(args["ButtonPath"] + '/hover', "textures/ui/netease_chest/btn02@3x.png")
			self.SetSprite(args["ButtonPath"] + '/pressed', "textures/ui/netease_chest/btn02@3x.png")
		else:
			self.SetSprite(args["ButtonPath"] + '/default', "textures/ui/netease_chest/btn02@3x.png")
			self.SetSprite(args["ButtonPath"] + '/hover', "textures/ui/netease_chest/btn02@3x.png")
			self.SetSprite(args["ButtonPath"] + '/pressed', "textures/ui/netease_chest/btn02@3x.png")
			
	def GetDeleteUidIndex(self, path):
		for index, btnPath in enumerate(self.mUserDeleteBtns):
			if btnPath == path:
				return index
		return -1
	
	def GetAcceptUidIndex(self, path):
		for index, btnPath in enumerate(self.mApplicatorAcceptBtns):
			if btnPath == path:
				return index
		return -1
	
	def GetRefuseUidIndex(self, path):
		for index, btnPath in enumerate(self.mApplicatorRefuseBtns):
			if btnPath == path:
				return index
		return -1
		
		
		