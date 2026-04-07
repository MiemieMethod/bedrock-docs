# -*- coding: utf-8 -*-
import server.extraServerApi as serverApi
ServerSystem = serverApi.GetServerSystemCls()

class SimpleServerSys(ServerSystem):
	def __init__(self, namespace, systemName):
		ServerSystem.__init__(self, namespace, systemName)

	def Destroy(self):
		pass