# -*- coding: utf-8 -*-

from common.mod import Mod
import rankConsts as rankConsts


@Mod.Binding(name=rankConsts.ModNameSpace, version=rankConsts.ModVersion)
class NeteaseRankServer(object):
	def __init__(self):
		pass
	
	@Mod.InitServer()
	def initServer(self):
		print '===========================neteaseRank initServer==============================='
		import server.extraServerApi as serverApi
		self.mServerSystem = serverApi.RegisterSystem(rankConsts.ModNameSpace, rankConsts.ServerSystemName,
		                                              rankConsts.ServerSystemClsPath)
	
	@Mod.DestroyServer()
	def destroyServer(self):
		print '===========================neteaseRank destroyServer==============================='