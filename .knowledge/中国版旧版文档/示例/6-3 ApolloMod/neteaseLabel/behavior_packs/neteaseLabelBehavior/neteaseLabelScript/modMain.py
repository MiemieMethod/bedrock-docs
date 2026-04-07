# -*- coding: utf-8 -*-

from common.mod import Mod
import client.extraClientApi as clientApi
from neteaseLabelScript.labelConst import ModVersion, ModName, ClientSystemName, ClientSystemClsPath


@Mod.Binding(name=ModName, version=ModVersion)
class NeteaseLabelClient(object):
	@Mod.InitClient()
	def LabelClientInit(self):
		print '==== neteaseLabel initClient ===='
		clientApi.RegisterSystem(ModName, ClientSystemName, ClientSystemClsPath)

	@Mod.DestroyClient()
	def LabelClientDestroy(self):
		print '==== neteaseLabel destroyClient ===='
