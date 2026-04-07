# -*- coding: utf-8 -*-

from common.mod import Mod
import server.extraServiceApi as serviceApi
import neteaseMatchScript.serviceConsts as serviceConsts

@Mod.Binding(name = serviceConsts.ModName, version = serviceConsts.ModVersion)
class MatchServiceMod(object):
	@Mod.InitService()
	def MatchServiceInit(self):
		print '===========================neteaseMatch initService==============================='
		serviceApi.RegisterSystem(serviceConsts.ModName, serviceConsts.ServiceSystemName, serviceConsts.ServiceSystemClsPath)

	@Mod.DestroyService()
	def MatchServiceDestroy(self):
		print '===========================neteaseMatch destroyService==============================='
