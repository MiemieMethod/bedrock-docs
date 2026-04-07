# -*- coding: utf-8 -*-
import client.extraClientApi as clientApi
ViewBinder = clientApi.GetViewBinderCls()
ViewRequest = clientApi.GetViewViewRequestCls()
ScreenNode = clientApi.GetScreenNodeCls()
import time
import chestConsts as chestConsts
from chestConsts import UIDef
import Queue

class TipsScreen(ScreenNode):
	def __init__(self,namespace,name,param):
		ScreenNode.__init__(self, namespace, name, param)
		print "===%s===" % "init TipsScreen"
		self.mTipsPanel = "/TipsPanel"
		self.mTipImg = self.mTipsPanel + "/tip_img"
		self.mTitle = self.mTipImg + "/tip_title_lbl"
		self.mMessage = self.mTipImg + "/text_lbl"
		self.mCancelBtn = self.mTipImg + "/cancel_btn"
		self.mConfirmBtn = self.mTipImg + "/confirm_btn"
		self.mCloseBtn = self.mTipImg + "/close_btn"
		
		self.mRequestQueue = Queue.Queue()
		
		self.mCnt = 0
		self.mIsShowing = False
		self.mCurrentConfirmFunc = None
		self.mCurrentCancelFunc = None
	
	def InitScreen(self):
		print "====%s====" % "NotifyScreen Init"
		self.SetVisible(self.mTipsPanel, False)
		
		# 按钮监听
		self.AddTouchEventHandler(self.mConfirmBtn, self.OnConfirm)
		self.AddTouchEventHandler(self.mCancelBtn, self.OnCancel)
		self.AddTouchEventHandler(self.mCloseBtn, self.ClosePanel)
	
	def Destory(self):
		print "====%s======" % "NotifyScreen Destroy"
	
	def Update(self):
		if self.mCnt > 0:
			self.ShowPanel()
	
	# endregion
	
	# region 功能函数
	def SetNotifyPanel(self, notifyData, confirmFunc, cancelFunc, messageData=None):
		type = notifyData.get('notify_type')
		title = notifyData.get('title')
		message = None
		if messageData:
			message = messageData
		else:
			message = notifyData.get('message')
		confirm = notifyData.get('confirm')
		cancel = notifyData.get('cancel')
		requestDict = {
			'type': type,
			'title': title,
			'message': message,
			'confirm': confirm,
			'cancel': cancel,
			'confirmFunc': confirmFunc,
			'cancelFunc': cancelFunc
		}
		self.mRequestQueue.put(requestDict)
		self.mCnt += 1
	
	def ShowPanel(self, args=None):
		if self.mIsShowing:
			clientApi.SetInputMode(1)
		else:
			clientApi.SetInputMode(0)
		if self.mIsShowing:
			return
		request = self.mRequestQueue.get()
		if request:
			title = request.get('title')
			message = request.get('message')
			confirm = request.get('confirm')
			cancel = request.get('cancel')
			self.SetText(self.mTitle, title)
			self.SetText(self.mMessage, message)
			self.SetText(self.mConfirmBtn, confirm)
			self.SetText(self.mCancelBtn, cancel)
			
			self.mCurrentConfirmFunc = request.get('confirmFunc')
			self.mCurrentCancelFunc = request.get('cancelFunc')
		self.SetVisible(self.mTipsPanel, True)
		self.mIsShowing = True
	
	def ClosePanel(self, args=None):
		print "======%s========" % "ClosePanel"
		self.SetVisible(self.mTipsPanel, False)
		clientApi.SetInputMode(0)
		self.mCnt -= 1
		self.mIsShowing = False
	
	def HandleConfirm(self):
		print "======%s========" % "HandleConfirm"
		func = self.mCurrentConfirmFunc
		self.ClosePanel()
		clientApi.SetInputMode(0)
		if func != None:
			func()
	
	def HandleCancel(self):
		print "======%s========" % "HandleCancel"
		func = self.mCurrentCancelFunc
		self.ClosePanel()
		clientApi.SetInputMode(0)
		if func != None:
			func()
	
	# endregion
	
	# region UI响应函数
	def OnConfirm(self, args):
		print "======%s========" % "OnConfirm touch down"
		touchEvent = args["TouchEvent"]
		touch_event_enum = clientApi.GetMinecraftEnum().TouchEvent
		if touchEvent == touchEvent == touch_event_enum.TouchUp or touchEvent == touch_event_enum.TouchCancel:
			self.HandleConfirm()
		else:
			pass
	
	def OnCancel(self, args):
		print "======%s========" % "OnCancel touch down"
		touchEvent = args["TouchEvent"]
		touch_event_enum = clientApi.GetMinecraftEnum().TouchEvent
		if touchEvent == touchEvent == touch_event_enum.TouchUp or touchEvent == touch_event_enum.TouchCancel:
			self.HandleCancel()
		else:
			pass