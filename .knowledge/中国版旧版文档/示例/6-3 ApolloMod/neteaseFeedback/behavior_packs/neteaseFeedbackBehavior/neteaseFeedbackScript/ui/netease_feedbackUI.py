# -*- coding: utf-8 -*-

import client.extraClientApi as extraClientApi

ViewBinder = extraClientApi.GetViewBinderCls()
ViewRequest = extraClientApi.GetViewViewRequestCls()
ScreenNode = extraClientApi.GetScreenNodeCls()
TouchEvent = extraClientApi.GetMinecraftEnum().TouchEvent
import weakref

class FeedBackMainScreen(ScreenNode):
	def __init__(self, namespace, name, param):
		ScreenNode.__init__(self, namespace, name, param)
		print "FeedBackMainScreen", namespace, name, param
		#self.mUiKey = UIDef.UIChatDesk
		self.mSelectedTags = []
		self.mFeedBackMes = ""
		self.mSuredTags = []
		self.mSuredTagIndexes = []
		#UI 路径
		#反馈页面
  
	# Create函数是继承自ScreenNode，会在UI创建完成后被调用
	def Create(self):
		print "FeedBackMainScreen Create"

		self.mMainPanel = self.GetBaseUIControl("/main_pnl")
		
		self.mImgBaseDialoge = self.mMainPanel.GetChildByPath("/img_base_dialoge").asImage()
		self.mDialogeCloseBtn = self.mImgBaseDialoge.GetChildByPath("/btn_close").asButton()
		self.mLbTypeSelect = self.mImgBaseDialoge.GetChildByPath("/lb_Type_select").asLabel()
		self.mLbTypeSelectTags = []
		self.mLbSelectTags = []
		for i in range(1, 6):
			self.mLbTypeSelectTags.append(self.mLbTypeSelect.GetChildByPath("/img_tag" + str(i)).asImage())
			self.mLbSelectTags.append(self.mLbTypeSelect.GetChildByPath("/img_tag" + str(i) + "/lb_tag" + str(i)).asLabel())
		self.mChangeTypeBtn = self.mImgBaseDialoge.GetChildByPath("/btn_changeType").asButton()
		self.mLbChooseType = self.mChangeTypeBtn.GetChildByPath("/lb_chooseType").asLabel()
		self.mLbChangeType = self.mChangeTypeBtn.GetChildByPath("/lb_changeType").asLabel()
		self.mTextEditFeedback = self.mImgBaseDialoge.GetChildByPath("/text_edit_feedback").asTextEditBox()
		self.mReleaseBtn = self.mImgBaseDialoge.GetChildByPath("/btn_release").asButton()
		self.mReleaseBtnUseImg = self.mReleaseBtn.GetChildByPath("/img_release_unuse").asImage()
		
		#Tag选择
		self.mBtnMaskWindow = self.GetBaseUIControl("/btn_mask_window")
		self.mImgWindowTypes = self.mBtnMaskWindow.GetChildByPath("/img_window_types").asImage()
		self.mCloseWindowBtn = self.mImgWindowTypes.GetChildByPath("/btn_closeWindow").asButton()
		self.mConfirmBtn = self.mImgWindowTypes.GetChildByPath("/btn_confirm").asButton()
		self.mConfirmBtnImg = self.mConfirmBtn.GetChildByPath("/img_confirm_unuse").asImage()
		
		self.mAllTagsRadios = []
		self.mTagImgRadiosActive = []
		self.mTagLbRadios = []
		self.mTagSelectBtns = []
		for i in range(1, 11):
			self.mAllTagsRadios.append(self.mImgWindowTypes.GetChildByPath("/img_radio" + str(i)).asImage())
			self.mTagImgRadiosActive.append(self.mImgWindowTypes.GetChildByPath("/img_radio" + str(i) + "/img_radio" + str(i) + "_active").asImage())
			self.mTagLbRadios.append(self.mImgWindowTypes.GetChildByPath("/img_radio" + str(i) + "/lb_radio" + str(i)).asLabel())
			self.mTagSelectBtns.append(self.mImgWindowTypes.GetChildByPath("/img_radio" + str(i) + "/tag_button" + str(i)).asButton())

	def InitScreen(self):
		self.ChangeScreenVisible(False)

	def ChangeScreenVisible(self, flag):
		self.SetScreenVisible(flag)
		OpeComp = extraClientApi.GetEngineCompFactory().CreateOperation(extraClientApi.GetLevelId())
		if flag:
			self.SetIsHud(0)
			OpeComp.SetCanPause(False)
			OpeComp.SetCanChat(False)
		else:
			self.SetIsHud(1)
			OpeComp.SetCanPause(True)
			OpeComp.SetCanChat(True)
	
	def Show(self, flag):
		self.ChangeScreenVisible(flag)
		self.mBtnMaskWindow.SetVisible(not flag)
		self.mImgBaseDialoge.SetVisible(flag)
		self.DealDialogeSelectedUITags()
		
	def InitSystem(self, system):
		self.mClientSystem = weakref.proxy(system)
		
		self.mCloseWindowBtn.AddTouchEventParams({"isSwallow":True})
		self.mCloseWindowBtn.SetButtonTouchUpCallback(self.OnCloseWindowBtn)

		self.mDialogeCloseBtn.AddTouchEventParams({"isSwallow":True})
		self.mDialogeCloseBtn.SetButtonTouchUpCallback(self.OnDialogeCloseBtn)

		self.mConfirmBtn.AddTouchEventParams({"isSwallow":True})
		self.mConfirmBtn.SetButtonTouchUpCallback(self.OnSureFeedbackTags)

		self.mChangeTypeBtn.AddTouchEventParams({"isSwallow":True})
		self.mChangeTypeBtn.SetButtonTouchUpCallback(self.OnChangeTypeBtn)

		self.mReleaseBtn.AddTouchEventParams({"isSwallow":True})
		self.mReleaseBtn.SetButtonTouchUpCallback(self.OnSureFeedbackTagsAndMessage)

		for radioBtn in self.mTagSelectBtns:
			radioBtn.AddTouchEventParams({"isSwallow":True})
			radioBtn.SetButtonTouchUpCallback(self.OnSelectedTagBtn)
	
	def OnChangeTypeBtn(self, args):
		self.mBtnMaskWindow.SetVisible(True)
	
	def InitFeedbackTags(self, tags):
		self.mUIFeedbackTags = tags.keys()
		for i in range(0, len(self.mUIFeedbackTags)):
			self.mTagImgRadiosActive[i].SetVisible(False)
			self.mTagLbRadios[i].SetText(self.mUIFeedbackTags[i])
		
		for i in range(len(self.mUIFeedbackTags), len(self.mAllTagsRadios)):
			self.mAllTagsRadios[i].SetVisible(False)
		
		self.DealDialogeSelectedUITags()
		
	def OnSelectedTagBtn(self, args):
		tagIndex = self.GeTagIndex(args["ButtonPath"])
		if self.mUIFeedbackTags[tagIndex] not in self.mSuredTags:
			self.mTagImgRadiosActive[tagIndex].SetVisible(True)
			self.mSuredTags.append(self.mUIFeedbackTags[tagIndex])
			self.mSuredTagIndexes.append(tagIndex)
		else:
			self.mTagImgRadiosActive[tagIndex].SetVisible(False)
			self.mSuredTags.remove(self.mUIFeedbackTags[tagIndex])
			self.mSuredTagIndexes.remove(tagIndex)
		self.ShowSureTagsButton()
		if len(self.mSuredTags) in (4, 5):
			self.ShowTagsButton()
			
	def GeTagIndex(self, path):
		# skip "tag_button"
		tag_id = int(path.split("/")[-1][10:])
		return (tag_id-1) if (tag_id > 0) else -1

	
	def OnSureFeedbackTags(self, args):
		self.mSelectedTags = self.mSuredTags
		self.mBtnMaskWindow.SetVisible(False)
		self.DealDialogeSelectedUITags()
	
	def DealDialogeSelectedUITags(self):
		self.mLbChooseType.SetVisible(len(self.mSelectedTags) <= 0)
		self.mLbChangeType.SetVisible(len(self.mSelectedTags) > 0)
		for i in range(0, len(self.mSelectedTags)):
			self.mLbTypeSelectTags[i].SetVisible(True)
			self.mLbSelectTags[i].SetText(self.mSelectedTags[i])
		
		for i in range(len(self.mSelectedTags), len(self.mLbTypeSelectTags)):
			self.mLbTypeSelectTags[i].SetVisible(False)
		
	def OnCloseWindowBtn(self, args):
		self.mBtnMaskWindow.SetVisible(False)
		
	def OnDialogeCloseBtn(self, args):
		self.ChangeScreenVisible(False)
		
	def OnSureFeedbackTagsAndMessage(self, args):
		import client.extraClientApi as clientApi
		comp = clientApi.GetEngineCompFactory().CreateGame(clientApi.GetLevelId())
		self.mFeedBackText = (self.mTextEditFeedback.GetEditText() or '').strip()
		isValid = comp.CheckWordsValid(self.mFeedBackText)
		if isValid:
			self.mClientSystem.NotifyToServer("CommitFeedbackFromClientEvent", {"message":self.mFeedBackText, "playerId":self.mClientSystem.mLocalPlayerId, "tags":self.mSelectedTags})
			self.mTextEditFeedback.SetEditText("")
			self.ReSetTags()
			self.ChangeScreenVisible(False)
		else:
			self.mClientSystem.NotifyToServer("ShowTipsFromClientEvent", {"playerId":extraClientApi.GetLocalPlayerId(), "message":"文字拥有屏蔽字"})
	
	def ReSetTags(self):
		self.mSelectedTags = []
		self.mSuredTags = []
		self.mSuredTagIndexes = []
		for tagIndex in range(0, len(self.mTagImgRadiosActive)):
			self.mTagImgRadiosActive[tagIndex].SetVisible(False)
		self.ShowSureTagsButton()
		
	def ShowSureTagsButton(self):
		self.mConfirmBtnImg.SetVisible((len(self.mSuredTags) <= 0))
		self.mConfirmBtnImg.SetTouchEnable((len(self.mSuredTags) <= 0))
	
	def ShowTagsButton(self):
		if len(self.mSuredTags) < 5:
			for i in range(0, len(self.mUIFeedbackTags)):
				self.mTagLbRadios[i].SetText("§f" + self.mUIFeedbackTags[i])
				self.mTagSelectBtns[i].SetTouchEnable(True)
		else:
			for i in range(0, len(self.mUIFeedbackTags)):
				if i not in self.mSuredTagIndexes:
					self.mTagLbRadios[i].SetText("§0" + self.mUIFeedbackTags[i])
					self.mTagSelectBtns[i].SetTouchEnable(False)
		
	@ViewBinder.binding(ViewBinder.BF_EditChanged | ViewBinder.BF_EditFinished)
	def message_text_edit_box0(self, args):
		self.DrawSendButton()
		return ViewRequest.Refresh
	
	def DrawSendButton(self, enable=None):
		self.mFeedBackText = (self.mTextEditFeedback.GetEditText() or '').strip()
		self.mReleaseBtn.SetTouchEnable(self.mFeedBackText != "")
		self.mReleaseBtnUseImg.SetVisible(self.mFeedBackText == "")
	
	def Destroy(self):
		pass

	# 继承自ScreenNode的方法，会被引擎自动调用，1秒钟30帧
	def Update(self):
		pass
		

