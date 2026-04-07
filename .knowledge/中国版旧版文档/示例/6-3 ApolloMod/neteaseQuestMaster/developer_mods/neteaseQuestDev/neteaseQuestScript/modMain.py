# -*- coding: utf-8 -*-

from common.mod import Mod
import server.extraMasterApi as masterApi
from neteaseQuestScript.questConst import ModVersion, ModName, MasterSystemName, MasterSystemClsPath


@Mod.Binding(name=ModName, version=ModVersion)
class NeteaseQuestMaster(object):
	@Mod.InitMaster()
	def QuestMasterInit(self):
		print '==== neteaseQuest initMaster ===='
		masterApi.RegisterSystem(ModName, MasterSystemName, MasterSystemClsPath)

	@Mod.DestroyMaster()
	def QuestMasterDestroy(self):
		print '==== neteaseQuest destroyMaster ===='
