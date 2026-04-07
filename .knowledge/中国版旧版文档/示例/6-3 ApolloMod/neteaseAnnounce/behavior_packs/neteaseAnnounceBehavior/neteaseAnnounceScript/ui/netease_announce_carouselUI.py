# -*- coding: utf-8 -*-
import time
import client.extraClientApi as extraClientApi
ViewBinder = extraClientApi.GetViewBinderCls()
ViewRequest = extraClientApi.GetViewViewRequestCls()
ScreenNode = extraClientApi.GetScreenNodeCls()

class FloatingWindowScreen(ScreenNode):
	def __init__(self, namespace, name, param):
		ScreenNode.__init__(self, namespace, name, param)
		self.mHadInQueue = []
		self.mQueue = []
		self.mRecentData = None
		self.mFrame = 0
		self.mStartTimestamp = 0

	def ChangeScreenVisible(self, flag):
		self.mBShow = flag
		self.SetVisible("", flag)

	# Create函数是继承自ScreenNode，会在UI创建完成后被调用
	def Create(self):
		pass

	def InitScreen(self):
		self.ChangeScreenVisible(False)

	def Destroy(self):
		pass

	# 继承自ScreenNode的方法，会被引擎自动调用，1秒钟30帧
	def Update(self):
		if not self.mBShow:
			return
		self.mFrame += 1
		if self.mFrame % 30 == 0:
			self.CheckDisplayTime()

	def CmpRecord(self, a, b):
		return cmp(a["_id"], b["_id"])

	def Show(self, data):
		version = data["version"]
		print "FloatingWindowScreen", version
		for record in data["dataList"]:
			if record["_id"] in self.mHadInQueue:
				continue
			self.mQueue.append(record)
			self.mHadInQueue.append(record["_id"])
		self.mQueue.sort(self.CmpRecord)
		if self.mBShow:
			return
		self.ChangeScreenVisible(True)
		self.DrawNext()

	def DrawNext(self):
		if not self.mQueue:
			self.ChangeScreenVisible(False)
			return
		self.mRecentData = self.mQueue.pop(0)
		self.mStartTimestamp = int(time.time()) + self.mRecentData["displayTime"]
		self.SetText("/main_pnl/img_base_carousel/lb_carousel", self.mRecentData["content"])

	def CheckDisplayTime(self):
		now = int(time.time())
		if now < self.mStartTimestamp:
			return
		self.DrawNext()