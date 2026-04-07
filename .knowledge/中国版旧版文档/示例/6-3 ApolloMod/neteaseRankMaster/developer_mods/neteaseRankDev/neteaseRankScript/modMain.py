# -*- coding: utf-8 -*-

from common.mod import Mod
import rankConsts as rankConsts


@Mod.Binding(name=rankConsts.ModNameSpace, version=rankConsts.ModVersion)
class NeteaseRankMaster(object):
	def __init__(self):
		pass
	
	@Mod.InitMaster()
	def initMaster(self):
		print '===========================neteaseRank initMaster==============================='
		import server.extraMasterApi as extraMasterApi
		self.mMasterSystem = extraMasterApi.RegisterSystem(rankConsts.ModNameSpace, rankConsts.MasterSystemName,
		                                                rankConsts.MasterSystemClsPath)
	
	@Mod.DestroyMaster()
	def destroyMaster(self):
		print '===========================neteaseRank destroyMaster==============================='