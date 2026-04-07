# -*- coding: utf-8 -*-
import client.extraClientApi as extraClientApi
from neteaseBattleScript.battleCommon.battleConsts import ModNameSpace
import neteaseBattleScript.ui.uiDef as uiDef

class UIMgr(object):
	"""
	UI管理器
	"""
	def __init__(self):
		super(UIMgr, self).__init__()
		self.mOpenedUI = set()
		self.mInputMode = 0
		self.mUIDict = {}

	def Destroy(self):
		pass

	def Init(self):
		for uiKey, config in uiDef.UIData.iteritems():
			self.InitSingleUI(uiKey, config)

	def InitSingleUI(self, uiKey, config):
		# 初始化UI，就和MODSDK教程一模一样只是写到了这里，单独抽离逻辑
		cls, screen = config["cls"], config["screen"]
		extraClientApi.RegisterUI(ModNameSpace, uiKey, cls, screen)
		extraParam = {}
		if config.has_key("isHud"):
			extraParam["isHud"] = config["isHud"]
		ui = extraClientApi.CreateUI(ModNameSpace, uiKey, extraParam)
		if not ui:
			print "InitSingleUI %s fail" % uiKey
			return
		layer = config.get("layer", None)
		if not layer is None:
			ui.SetLayer("", layer)
		ui.InitScreen()
		self.mUIDict[uiKey] = ui

	def GetUI(self, uiKey):
		return self.mUIDict.get(uiKey, None)

	def RemoveUI(self, uiKey):
		ui = self.mUIDict.get(uiKey, None)
		if ui:
			del self.mUIDict[uiKey]
			ui.SetRemove()
			return True
		return False

	def RegisterUIOpen(self, uiKey):
		# 告知UI管理器某界面处于打开中，可再次扩展“打开一个界面关闭前一个打开的界面”的逻辑
		self.mOpenedUI.add(uiKey)
		# extraClientApi.SetResponse(False)
		extraClientApi.SetInputMode(1)
		extraClientApi.HideHudGUI(True)
		# extraClientApi.SetInputEnable(False)

	def RegisterUIClose(self, uiKey):
		# 告知UI管理器界面关闭
		self.mOpenedUI.discard(uiKey)
		if not self.mOpenedUI:
			# 暂时需求为“只要还有打开着的界面inputmode就保持为1”
			# extraClientApi.SetResponse(True)
			extraClientApi.SetInputMode(0)
			extraClientApi.HideHudGUI(False)
			# extraClientApi.SetInputEnable(True)

	def SetInputMode(self, v):
		inputMode = 0
		if v:
			if not self.mInputMode:
				inputMode = 1
			self.mInputMode += 1
		elif self.mInputMode:
			self.mInputMode -= 1
			if not self.mInputMode:
				inputMode = -1
		if inputMode > 0:
			extraClientApi.SetInputMode(1)
		elif inputMode < 0:
			extraClientApi.SetInputMode(0)

