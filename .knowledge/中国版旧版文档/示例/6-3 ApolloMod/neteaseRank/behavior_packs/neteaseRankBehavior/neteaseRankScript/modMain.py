# -*- coding: utf-8 -*-

from common.mod import Mod
import rankConsts as rankConsts


@Mod.Binding(name=rankConsts.ModNameSpace, version=rankConsts.ModVersion)
class NeteaseRankClient(object):
	def __init__(self):
		pass
	
	@Mod.InitClient()
	def initClient(self):
		print '===========================neteaseRank initClient==============================='
		import client.extraClientApi as clientApi
		self.mClentSystem = clientApi.RegisterSystem(rankConsts.ModNameSpace, rankConsts.ClientSystemName,
		                                             rankConsts.ClientSystemClsPath)
	
	@Mod.DestroyClient()
	def destroyClient(self):
		print '===========================neteaseRank destroyClient==============================='