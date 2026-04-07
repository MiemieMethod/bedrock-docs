# -*- coding: utf-8 -*-
from mod.common.mod import Mod

import mod.client.extraClientApi as clientApi
import mod.server.extraServerApi as serverApi


@Mod.Binding(name='protalGate', version='1.0.0')
class Main(object):

    def __init__(self):
        pass

    @Mod.InitClient()
    def init_client(self):
        clientApi.RegisterSystem("customMusic","Music","customMusicDemoScripts.client.Music.Main")
        pass
        
    @Mod.InitServer()
    def init_server(self):
        pass

    @Mod.DestroyClient()
    def destroy_client(self):
        pass

    @Mod.DestroyServer()
    def destroy_server(self):
        pass
