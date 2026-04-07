# -*- coding: utf-8 -*-
import server.extraMasterApi as extraMasterApi
MasterSystem = extraMasterApi.GetMasterSystemCls()

class SimpleMasterSystem(MasterSystem):
	def __init__(self, namespace, systemName):
		MasterSystem.__init__(self, namespace, systemName)
		
	def Destroy(self):
		pass