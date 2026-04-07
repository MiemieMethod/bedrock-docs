# -*- coding: utf-8 -*-
import server.extraServiceApi as serviceApi
ServiceSystem = serviceApi.GetServiceSystemCls()

class SimpleServiceSystem(ServiceSystem):
	def __init__(self, namespace, systemName):
		ServiceSystem.__init__(self, namespace, systemName)

	def Destroy(self):
		pass