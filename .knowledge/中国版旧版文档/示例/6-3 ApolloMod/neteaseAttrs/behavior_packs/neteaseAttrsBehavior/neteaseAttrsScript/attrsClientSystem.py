# -*- coding: utf-8 -*-

import neteaseAttrsScript.attrsConst as attrsConst
import client.extraClientApi as clientApi

ClientSystem = clientApi.GetClientSystemCls()


class AttrsClientSystem(ClientSystem):
	def __init__(self, namespace, systemName):
		ClientSystem.__init__(self, namespace, systemName)
		self.mAttrsUINode = None

		self.ListenForEvent(clientApi.GetEngineNamespace(), clientApi.GetEngineSystemName(), attrsConst.UiInitFinishedEvent, self, self.OnUiInitFinished)

	def Destroy(self):
		self.mAttrsUINode = None

		self.UnListenForEvent(clientApi.GetEngineNamespace(), clientApi.GetEngineSystemName(), attrsConst.UiInitFinishedEvent, self, self.OnUiInitFinished)

	def OnUiInitFinished(self, *args):
		# 注册UI 详细解释参照《UI API》
		clientApi.RegisterUI(
			attrsConst.ModName, attrsConst.attrsUIName, attrsConst.attrsUIClsPath, attrsConst.attrsUIScreenDef)
		# 创建UI 详细解释参照《UI API》
		clientApi.CreateUI(attrsConst.ModName, attrsConst.attrsUIName, {"isHud": 1})
		self.mAttrsUINode = clientApi.GetUI(attrsConst.ModName, attrsConst.attrsUIName)
		if self.mAttrsUINode:
			self.mAttrsUINode.InitScreen()
		else:
			print '==== %s ====' % 'create UI: %s failed' % attrsConst.attrsUIScreenDef

	def Detail(self, detail, x, y):
		if self.mAttrsUINode:
			self.mAttrsUINode.detail(detail, x, y)
