 # -*- coding: utf-8 -*-

from common.mod import Mod
import neteaseResidenceScript.residenceConsts as residenceConsts

@Mod.Binding(name = residenceConsts.ModNameSpace, version = residenceConsts.ModVersion)
class NeteaseResidenceClient(object):
	def __init__(self):
		pass

	@Mod.InitClient()
	def initClient(self):
		print '===========================NeteaseResidenceClient initClient==============================='
		import client.extraClientApi as extraClientApi
		self.mClientSystem = extraClientApi.RegisterSystem(residenceConsts.ModNameSpace,
				residenceConsts.ClientSystemName, residenceConsts.ClientSystemClsPath)

	@Mod.DestroyClient()
	def destroyClient(self):
		print '===========================NeteaseResidenceClient destroyClient==============================='