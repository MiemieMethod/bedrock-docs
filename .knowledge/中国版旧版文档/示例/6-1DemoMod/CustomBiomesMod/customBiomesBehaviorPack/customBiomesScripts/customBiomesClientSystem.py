# -*- coding: utf-8 -*-

import mod.client.extraClientApi as clientApi
ClientSystem = clientApi.GetClientSystemCls()

class CustomBiomesClientSystem(ClientSystem):

    def __init__(self, namespace, systemName):
        super(CustomBiomesClientSystem, self).__init__(namespace, systemName)
        print "==== CustomBiomesClientSystem Init ===="

    def Destroy(self):
        pass