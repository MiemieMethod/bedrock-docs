# -*- coding: utf-8 -*-
import client.extraClientApi as extraClientApi
from neteaseSquadScript.squadConst import ModName
import neteaseSquadScript.ui.uiDef as uiDef
import weakref

class UIMgr(object):
	def __init__(self):
		super(UIMgr, self).__init__()
		self.mOpenedUI = set()
		self.mUIDict = {}
		self.mClientSystem = None

	def Destroy(self):
		pass

	def Init(self, system):
		self.mClientSystem = system
		for uiKey, config in uiDef.UIData.iteritems():
			self.InitSingleUI(uiKey, config)

	def InitSingleUI(self, uiKey, config):
		cls, screen = config["cls"], config["screen"]
		extraClientApi.RegisterUI(ModName, uiKey, cls, screen)
		extraParam = {}
		if config.has_key("isHud"):
			extraParam["isHud"] = config["isHud"]
		ui = extraClientApi.CreateUI(ModName, uiKey, extraParam)
		if not ui:
			print "InitSingleUI %s fail" % uiKey
			return
		layer = config.get("layer", None)
		if not layer is None:
			ui.SetLayer("", layer)
		ui.InitScreen()
		try:
			ui.InitSystem(self.mClientSystem)
		except Exception as e:
			print e.message
			print "ui %s do not has InitSystem method" % uiKey
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
		self.mOpenedUI.add(uiKey)
		extraClientApi.SetResponse(False)
		extraClientApi.SetInputMode(1)
		#extraClientApi.SetInputEnable(False)

	def RegisterUIClose(self, uiKey):
		self.mOpenedUI.discard(uiKey)
		if not self.mOpenedUI:
			extraClientApi.SetResponse(True)
			extraClientApi.SetInputMode(0)
			#extraClientApi.SetInputEnable(True)

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
		elif inputMode <= 0:
			extraClientApi.SetInputMode(0)

