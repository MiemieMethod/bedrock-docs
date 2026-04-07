# -*- coding: utf-8 -*-
import client.extraClientApi as extraClientApi
import neteaseDungeonScript.ui.uiDef as uiDef
import neteaseDungeonScript.dungeonConsts as dungeonConsts
class UIMgr(object):
	def __init__(self):
		super(UIMgr, self).__init__()
		self.mInputMode = 0
		self.mUIDict = {}

	def Destroy(self):
		pass

	def Init(self):
		for uiKey, config in uiDef.UIData.iteritems():
			self.InitSingleUI(uiKey, config)

	def InitSingleUI(self, uiKey, config):
		cls, screen = config["cls"], config["screen"]
		extraClientApi.RegisterUI(dungeonConsts.ModNameSpace, uiKey, cls, screen)
		extraParam = {}
		if config.has_key("isHud"):
			extraParam["isHud"] = config["isHud"]
		ui = extraClientApi.CreateUI(dungeonConsts.ModNameSpace, uiKey, extraParam)
		if not ui:
			print "InitSingleUI %s fail" % uiKey
			return
		ui.SetLayer("", config["layer"]*1000)
		ui.InitScreen()
		self.mUIDict[uiKey] = ui

	def GetUI(self, uiKey):
		return self.mUIDict.get(uiKey, None)

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