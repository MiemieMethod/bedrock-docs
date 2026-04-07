# -*- coding: utf-8 -*-

from common.mod import Mod
import rankConsts as rankConsts


@Mod.Binding(name=rankConsts.ModNameSpace, version=rankConsts.ModVersion)
class NeteaseRankService(object):
	def __init__(self):
		pass
	
	@Mod.InitService()
	def initService(self):
		print '===========================neteaseRank initService==============================='
		import server.extraServiceApi as serviceApi
		self.mServiceSystem = serviceApi.RegisterSystem(rankConsts.ModNameSpace, rankConsts.ServiceSystemName,
		                                                rankConsts.ServiceSystemClsPath)
	
	@Mod.DestroyService()
	def destroyService(self):
		print '===========================neteaseRank destroyService==============================='