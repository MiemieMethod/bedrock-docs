# -*- coding: utf-8 -*-

from common.mod import Mod
import server.extraServiceApi as serviceApi
from neteaseQuestScript.questConst import ModVersion, ModName, ServiceSystemName, ServiceSystemClsPath


@Mod.Binding(name=ModName, version=ModVersion)
class NeteaseQuestService(object):
	@Mod.InitService()
	def QuestServiceInit(self):
		print '==== neteaseQuest initService ===='
		serviceApi.RegisterSystem(ModName, ServiceSystemName, ServiceSystemClsPath)

	@Mod.DestroyService()
	def QuestServiceDestroy(self):
		print '==== neteaseQuest destroyService ===='
