# -*- coding: utf-8 -*-
import client.extraClientApi as clientApi
ViewBinder = clientApi.GetViewBinderCls()
ViewRequest = clientApi.GetViewViewRequestCls()
ScreenNode = clientApi.GetScreenNodeCls()

from functools import wraps

def touch_filter(touchType):
	def touchFilter(func):
		@wraps(func)
		def decorated(*args, **kwargs):
			touchEventEnum = clientApi.GetMinecraftEnum().TouchEvent
			touchEvent = args[1]["TouchEvent"]
			if touchType == "up":
				if touchEvent == touchEventEnum.TouchUp:
					value = func(*args, **kwargs)
					return value
			if touchType == "down":
				if touchEvent == touchEventEnum.TouchDown:
					value = func(*args, **kwargs)
					return value
			if touchType == "cancel":
				if touchEvent == touchEventEnum.TouchCancel:
					value = func(*args, **kwargs)
					return value
			if touchType == "move":
				if touchEvent == touchEventEnum.TouchMove:
					value = func(*args, **kwargs)
					return value
		return decorated
	return touchFilter


class PushScreenDemo(ScreenNode):
	def __init__(self, namespace, name, param):
		ScreenNode.__init__(self, namespace, name, param)
		#PopScreen按钮
		self.PopBtnPath = "/pushScreenPanel/closeBtn"
		# 文本+文本输入框示例
		self.mLabelText_label = "/pushScreenPanel/newlabel"
		self.mLabelText_textEditor = "/pushScreenPanel/text_edit_box1"
		self.mText = ""
		self.initText = "I am datiangou!"
		self.textColor1 = (0.8, 1, 0, 0.8)
		self.textColor2 = (1, 1, 1, 1)
		#paperDoll
		self.paperdollPath = "/pushScreenPanel/paper_doll0"
		self.addBtnPath = "/pushScreenPanel/addBtn"
		self.reduceBtnPath = "/pushScreenPanel/reduceBtn"
		self.ensureBtnPath = "/pushScreenPanel/ensureBtn"
		self.mScale = 1
		print("===== PushScreenDemo __init__ =====")

	def Create(self):
		self.AddTouchEventHandler(self.PopBtnPath, self.OnPopScreenBtnClick, {"isSwallow": True})
		self.AddTouchEventHandler(self.addBtnPath, self.OnAddBtnClick, {"isSwallow": True})
		self.AddTouchEventHandler(self.reduceBtnPath, self.OnReduceBtnClick, {"isSwallow": True})
		self.AddTouchEventHandler(self.ensureBtnPath, self.OnEnsureBtnClick, {"isSwallow": True})
		print("===== MainScreen Create =====")
		
	@touch_filter("up")
	def OnPopScreenBtnClick(self, args):
		self.SetTextColor(self.mLabelText_label, self.textColor2)
		self.SetText(self.mLabelText_label, self.initText)
		clientApi.PopScreen()
	
	@touch_filter("up")
	def OnAddBtnClick(self, args):
		self.mScale += 0.2
		self.mScale = 3 if self.mScale > 3 else self.mScale
		self.SetUiModelScale(self.paperdollPath, self.mScale)

	@touch_filter("up")
	def OnReduceBtnClick(self, args):
		self.mScale -= 0.2
		self.mScale = 0 if self.mScale < 0 else self.mScale
		self.SetUiModelScale(self.paperdollPath, self.mScale)

	@touch_filter("up")
	def OnEnsureBtnClick(self, args):
		if self.mText:
			self.SetText(self.mLabelText_label, self.mText)
			self.SetTextColor(self.mLabelText_label, self.textColor1)

	# 文本-文本输入框示例
	@ViewBinder.binding(ViewBinder.BF_EditChanged | ViewBinder.BF_EditFinished)
	def OnTextEditCallback(self,args):
		self.mText = args["Text"]
		return ViewRequest.Refresh

	@ViewBinder.binding(ViewBinder.BF_BindString)
	def ReturnTextFunc(self):
		return self.mText

	def Destroy(self):
		print("===== MainScreen Destroy =====")