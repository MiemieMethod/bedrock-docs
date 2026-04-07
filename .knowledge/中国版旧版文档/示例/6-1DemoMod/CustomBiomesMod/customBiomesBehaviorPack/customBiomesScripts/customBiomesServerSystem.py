# -*- coding: utf-8 -*-
import random
import mod.server.extraServerApi as serverApi
ServerSystem = serverApi.GetServerSystemCls()
compFactory = serverApi.GetEngineCompFactory()

class CustomBiomesServerSystem(ServerSystem):

    def __init__(self, namespace, systemName):
        super(CustomBiomesServerSystem, self).__init__(namespace, systemName)
        print "===== CustomBiomesServerSystem init ====="

        self.ListenEvent()

    def ListenEvent(self):
        self.ListenForEvent(serverApi.GetEngineNamespace(), serverApi.GetEngineSystemName(), 'LoadServerAddonScriptsAfter', self, self.LoadServerAddonScriptsAfter)
        self.ListenForEvent(serverApi.GetEngineNamespace(), serverApi.GetEngineSystemName(), 'PlaceNeteaseStructureFeatureEvent', self, self.PlaceNeteaseStructureFeatureEvent)
        self.ListenForEvent(serverApi.GetEngineNamespace(), serverApi.GetEngineSystemName(), "ServerChatEvent", self, self.ServerChatEvent)

    def LoadServerAddonScriptsAfter(self, args):
        self.ListenForFeature()

    def ListenForFeature(self):
        comp = compFactory.CreateFeature(serverApi.GetLevelId())
        comp.AddNeteaseFeatureWhiteList("test:pumpkins")

    def PlaceNeteaseStructureFeatureEvent(self, args):
        print 'place structure {} place at {}, {}, {}, biomeType = {}, biomeName = {}'.format(
            args['structureName'], args['x'], args['y'], args['z'], args['biomeType'], args['biomeName'])
        if random.random() > 0.5:
            args['cancel'] = True
            print 'cancel structure {} place at {}, {}, {}, biomeType = {}, biomeName = {}'.format(
                args['structureName'], args['x'], args['y'], args['z'], args['biomeType'], args['biomeName'])

    def ServerChatEvent(self, args):
        print "==== OnServerChat ==== ", args
        playerId = args["playerId"]
        if args["message"] == "overworld":
            comp = compFactory.CreatePos(playerId)
            pos = comp.GetPos()
            comp = compFactory.CreateDimension(playerId)
            comp.ChangePlayerDimension(0, pos)
        elif args["message"] == "nether":
            comp = compFactory.CreatePos(playerId)
            pos = comp.GetPos()
            comp = compFactory.CreateDimension(playerId)
            comp.ChangePlayerDimension(1, pos)
        elif args["message"] == "theend":
            comp = compFactory.CreatePos(playerId)
            pos = comp.GetPos()
            comp = compFactory.CreateDimension(playerId)
            comp.ChangePlayerDimension(2, pos)
        elif args["message"] == "dm3":
            comp = compFactory.CreatePos(playerId)
            pos = comp.GetPos()
            comp = compFactory.CreateDimension(playerId)
            comp.ChangePlayerDimension(3, pos)
        elif args["message"] == "dm4":
            comp = compFactory.CreatePos(playerId)
            pos = comp.GetPos()
            comp = compFactory.CreateDimension(playerId)
            comp.ChangePlayerDimension(4, pos)
        elif args["message"] == "dm5":
            comp = compFactory.CreatePos(playerId)
            pos = comp.GetPos()
            comp = compFactory.CreateDimension(playerId)
            comp.ChangePlayerDimension(5, pos)
        elif args["message"] == "dm559":
            comp = compFactory.CreateDimension(playerId)
            comp.ChangePlayerDimension(559, (0,64,0))
        elif args["message"] == "dm22779":
            comp = compFactory.CreatePos(playerId)
            pos = comp.GetPos()
            comp = compFactory.CreateDimension(playerId)
            comp.ChangePlayerDimension(22779, pos)
        elif args["message"] == "dm23333":
            comp = compFactory.CreatePos(playerId)
            pos = comp.GetPos()
            comp = compFactory.CreateDimension(playerId)
            comp.ChangePlayerDimension(23333, pos)

    def Destroy(self):
        print "===== CustomBiomesClientSystem Destroy ====="
        comp = compFactory.CreateFeature(serverApi.GetLevelId())
        comp.ClearAllNeteaseFeatureWhiteList()
