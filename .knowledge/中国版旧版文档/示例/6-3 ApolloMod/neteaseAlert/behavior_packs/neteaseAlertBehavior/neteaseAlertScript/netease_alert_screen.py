# -*- coding: utf-8 -*-

import neteaseAlertScript.alertConst as alertConst
import client.extraClientApi as clientApi

ScreenNode = clientApi.GetScreenNodeCls()  # MODSDK提供的UI基类


class AlertScreen(ScreenNode):
	def __init__(self, namespace, name, param):
		ScreenNode.__init__(self, namespace, name, param)
		print '==== %s ====' % 'init AlertScreen'


		self.producer = None  # 客户端类的一个引用

	# Create函数是继承自ScreenNode，会在UI创建完成后被调用
	def Create(self):
		print '==== %s ====' % 'AlertScreen Create'
		self.mMainPanel = self.GetBaseUIControl("/main_pnl")
		self.mBg = self.mMainPanel.GetChildByPath("/img_alert").asImage()
		self.mText = self.mBg.GetChildByPath("/lb_alert").asLabel()

	def InitScreen(self):
		print '==== %s ====' % 'AlertScreen Init'

	# 继承自ScreenNode的方法，会被引擎自动调用，1秒钟30帧
	def Update(self):
		if not self.producer:
			self.producer = clientApi.GetSystem(alertConst.ModName, alertConst.ClientSystemName)  # 取得该Mod的客户端类对象
		if self.producer:
			task = self.producer.task  # 对应了封装的弹出提示任务对象
			if task:
				task.tick(self)  # 执行每一帧该任务对象预设好的“事情”
