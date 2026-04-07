# -*- coding: utf-8 -*-

import client.extraClientApi as clientApi
import neteaseTransactionScript.apiUtil as apiUtil
import neteaseTransactionScript.transactionClientConsts as transactionConsts


ViewBinder = clientApi.GetViewBinderCls()
ViewRequest = clientApi.GetViewViewRequestCls()
ScreenNode = clientApi.GetScreenNodeCls()


class TransactionHudUI(ScreenNode):
	def __init__(self, namespace, name, param):
		ScreenNode.__init__(self, namespace, name, param)
		self.mTipsAlpha = 0
		self.mConfirmTimeOut = -1
		self.mTipsPanelPath = "/tipsPanel"
		self.mConfirmPanelPath = "/confirmPanel"
		self.mRefuseBtnPath = "/confirmPanel/refuseBtn"
		self.mConfirmBtnPath = "/confirmPanel/confirmBtn"
		self.mConfirmEventData = {
			"fromPlayerId": None,
			"toPlayerId": None,
			"isConfirmed": False
		}
		self.mBShow = None

	def ChangeScreenVisible(self, flag):
		self.mBShow = flag
		self.SetVisible("", flag)

	def InitScreen(self):
		self.ChangeScreenVisible(False)

	# Create函数是继承自ScreenNode，会在UI创建完成后被调用
	def Create(self):
		self.RegisterButtonEvent()

	def RegisterButtonEvent(self):
		self.AddTouchEventHandler(self.mRefuseBtnPath, self.OnRefuseBtnClick, {"isSwallow": True})
		self.AddTouchEventHandler(self.mConfirmBtnPath, self.OnConfirmBtnClick, {"isSwallow": True})

	@apiUtil.touch_filter("up")
	def OnConfirmBtnClick(self, args):
		self.mConfirmTimeOut = -1
		self.SetVisible(self.mConfirmPanelPath, False)
		self.mConfirmEventData["isConfirmed"] = True
		apiUtil.GetTransactionClientSystem().NotifyToServer(transactionConsts.ConfirmRequestEvent, self.mConfirmEventData)

	@apiUtil.touch_filter("up")
	def OnRefuseBtnClick(self, args):
		self.mConfirmTimeOut = -1
		self.SetVisible(self.mConfirmPanelPath, False)
		self.mConfirmEventData["isConfirmed"] = False
		apiUtil.GetTransactionClientSystem().NotifyToServer(transactionConsts.ConfirmRequestEvent, self.mConfirmEventData)

	def Destroy(self):
		pass

	@ViewBinder.binding(ViewBinder.BF_BindFloat, "#tipsAlpha")
	def OnDetailShow(self):
		if self.mTipsAlpha > 1:
			return 1.0
		return self.mTipsAlpha

	# 继承自ScreenNode的方法，会被引擎自动调用，1秒钟30帧
	def Update(self):
		if self.mTipsAlpha > 0:
			self.mTipsAlpha -= 0.04
		if self.mConfirmTimeOut > 0:
			self.mConfirmTimeOut -= 1
			if self.mConfirmTimeOut == 0:
				self.OnRefuseBtnClick({ "TouchEvent": 0 })
				self.ShowTips("长时间未确认，已取消")
		if self.mTipsAlpha <= 0 and self.mConfirmTimeOut <= 0:
			if self.mBShow != False:
				self.ChangeScreenVisible(False)

	#-------------------------------------------  API  ----------------------------------------------
	def ShowConfirmPanel(self, args):
		self.ChangeScreenVisible(True)
		self.mConfirmEventData["fromPlayerId"] = args["fromPlayerId"]
		self.mConfirmEventData["toPlayerId"] = args["toPlayerId"]
		self.mConfirmTimeOut = 900
		nickName = args["nickName"]
		self.SetVisible(self.mConfirmPanelPath, True)
		self.SetText(self.mConfirmPanelPath + "/confirmInfo/confirmImg/confirmLabel", nickName + "向你发起面对面交易，是否同意？")

	def ShowTips(self, msg):
		self.ChangeScreenVisible(True)
		print "On Show Tips [{}]".format(msg)
		self.SetVisible(self.mTipsPanelPath, True)
		self.SetText(self.mTipsPanelPath + "/tipsText", msg)
		self.mTipsAlpha = 3.0
