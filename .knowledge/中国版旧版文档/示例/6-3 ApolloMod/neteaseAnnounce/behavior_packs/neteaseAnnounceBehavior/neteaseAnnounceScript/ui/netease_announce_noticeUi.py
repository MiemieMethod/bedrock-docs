# -*- coding: utf-8 -*-
import client.extraClientApi as extraClientApi
ViewBinder = extraClientApi.GetViewBinderCls()
ViewRequest = extraClientApi.GetViewViewRequestCls()
ScreenNode = extraClientApi.GetScreenNodeCls()
TouchEvent = extraClientApi.GetMinecraftEnum().TouchEvent
import neteaseAnnounceScript.apiUtil as apiUtil
from neteaseAnnounceScript.ui.uiDef import UIDef


class LoginPopupScreen(ScreenNode):
	def __init__(self, namespace, name, param):
		ScreenNode.__init__(self, namespace, name, param)
		self.mUiKey = UIDef.UILogin
		self.mDataList = []
		self.mRecentIndex = 0

	def ChangeScreenVisible(self, flag):
		self.mBShow = flag
		if flag:
			apiUtil.GetUiMgr().RegisterUIOpen(self.mUiKey)
		else:
			apiUtil.GetUiMgr().RegisterUIClose(self.mUiKey)
		self.SetVisible("", flag)

	# Create函数是继承自ScreenNode，会在UI创建完成后被调用
	def Create(self):
		pass

	def InitScreen(self):
		self.AddTouchEventHandler("/notice_pnl/notice_image_bg/notice_image_btn", self.OnNext)
		self.AddTouchEventHandler("/notice_pnl/notice_text_bg/notice_text_btn", self.OnNext)
		self.ChangeScreenVisible(False)

	def Destroy(self):
		pass

	# 继承自ScreenNode的方法，会被引擎自动调用，1秒钟30帧
	def Update(self):
		pass

	def CmpRecord(self, a, b):
		if a["priority"] == b["priority"]:
			return cmp(a["_id"], b["_id"])
		return cmp(b["priority"], a["priority"])

	def Show(self, data):
		self.ChangeScreenVisible(True)
		version = data["version"]
		# print "LoginPopupScreen", version
		self.mDataList = data["dataList"]
		self.mDataList.sort(self.CmpRecord)
		self.mRecentIndex = -1
		self.DrawNext()

	def DrawNext(self):
		self.mRecentIndex += 1
		length = len(self.mDataList)
		if self.mRecentIndex >= length:
			self.ChangeScreenVisible(False)
			return
		data = self.mDataList[self.mRecentIndex]
		if data["pic"]:
			self.DrawPic(data, length)
		else:
			self.DrawNoPic(data, length)

	def DrawPic(self, data, length):
		head = "/notice_pnl/notice_image_bg"
		self.SetVisible(head, True)
		self.SetVisible("/notice_pnl/notice_text_bg", False)
		title = "%s(%d/%d)" % (data["title"], self.mRecentIndex+1, length)
		self.SetText(head+"/notice_image_title", title)
		scrollBase = head+"/scroll_notice_image_main"
		scrollBaseTouch = scrollBase + "/scroll_touch/scroll_view/panel/background_and_viewport/scrolling_view_port/scrolling_content/lb_notice"
		self.SetText(scrollBaseTouch, data["content"])
		scrollBaseMouse = scrollBase + "/scroll_mouse/scroll_view/stack_panel/background_and_viewport/scrolling_view_port/scrolling_content/lb_notice"
		self.SetText(scrollBaseMouse, data["content"])
		if self.mRecentIndex == (length-1):
			self.SetText(head+"/notice_image_btn/button_label", "关闭")
		else:
			self.SetText(head+"/notice_image_btn/button_label", "继续")
		self.SetSprite(head+"/notice_image_banner", data["pic"])

	def DrawNoPic(self, data, length):
		head = "/notice_pnl/notice_text_bg"
		self.SetVisible(head, True)
		self.SetVisible("/notice_pnl/notice_image_bg", False)
		title = "%s(%d/%d)" % (data["title"], self.mRecentIndex + 1, length)
		self.SetText(head + "/notice_text_title", title)
		scrollBase = head+"/scroll_notice_text_main"
		scrollBaseTouch = scrollBase + "/scroll_touch/scroll_view/panel/background_and_viewport/scrolling_view_port/scrolling_content/lb_notice"
		self.SetText(scrollBaseTouch, data["content"])
		scrollBaseMouse = scrollBase + "/scroll_mouse/scroll_view/stack_panel/background_and_viewport/scrolling_view_port/scrolling_content/lb_notice"
		self.SetText(scrollBaseMouse, data["content"])
		if self.mRecentIndex == (length-1):
			self.SetText(head+"/notice_text_btn/button_label", "关闭")
		else:
			self.SetText(head+"/notice_text_btn/button_label", "继续")

	def OnNext(self, args):
		event = args["TouchEvent"]
		if event == TouchEvent.TouchUp:
			extraClientApi.SetResponse(True)
			self.DrawNext()
		elif event == TouchEvent.TouchDown:
			extraClientApi.SetResponse(False)
		elif event == TouchEvent.TouchMove:
			pass
		elif event == TouchEvent.TouchCancel:
			extraClientApi.SetResponse(True)

