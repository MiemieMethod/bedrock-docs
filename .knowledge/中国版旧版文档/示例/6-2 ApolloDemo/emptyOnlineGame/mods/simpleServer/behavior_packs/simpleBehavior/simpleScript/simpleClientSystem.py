# -*- coding: utf-8 -*-
import client.extraClientApi as extraClientApi
ClientSystem = extraClientApi.GetClientSystemCls()

class SimpleClientSystem(ClientSystem):
	def __init__(self, namespace, systemName):
		ClientSystem.__init__(self,namespace,systemName)

	def Destroy(self):
		pass