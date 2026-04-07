# -*- coding: utf-8 -*-

# 获取引擎服务端API的模块
import server.extraServerApi as serverApi
import npcManager
import lobbyGame.netgameApi as netgameApi
# 获取引擎服务端System的基类，System都要继承于ServerSystem来调用相关函数
ServerSystem = serverApi.GetServerSystemCls()

# 在modMain中注册的Server System类
class gameServerSystem(ServerSystem):

    # ServerSystem的初始化函数
    def __init__(self, namespace, systemName):
        # 首先调用父类的初始化函数
        super(gameServerSystem, self).__init__(namespace, systemName)
        print "===== gameServerSystem init ====="
        
        self.mNpcMgr = npcManager.NpcManager(self)
        # 玩家player id到uid的映射
        self.mPlayerid2uid = {}
        # 初始时调用监听函数监听事件
        self.ListenEvent()
        # 设置为创造模式 0生存模式，1创造模式，2冒险模式
        netgameApi.SetLevelGameType(2)

    def ListenEvent(self):
        #玩家加入时触发该事件
        self.ListenForEvent(serverApi.GetEngineNamespace(), serverApi.GetEngineSystemName(), 'AddServerPlayerEvent',self, self.OnAddServerPlayer)
        #entity被敲击触发该事件
        self.ListenForEvent(serverApi.GetEngineNamespace(), serverApi.GetEngineSystemName(), 'EntityBeKnockEvent', self,self.OnNpcTouched)

    def UnListenEvent(self):
        self.UnListenForEvent(serverApi.GetEngineNamespace(), serverApi.GetEngineSystemName(), 'AddServerPlayerEvent',self, self.OnAddServerPlayer)
        self.UnListenForEvent(serverApi.GetEngineNamespace(), serverApi.GetEngineSystemName(), 'EntityBeKnockEvent', self,self.OnNpcTouched)

    def OnAddServerPlayer(self, args):
        '''
        添加玩家的监听函数
        '''
        playerId = args.get('id','-1')
        if playerId == "-1":
            return
        uid = netgameApi.GetPlayerUid(playerId)
        self.mPlayerid2uid[playerId] = uid
        print 'player login.uid:', uid

    def OnNpcTouched(self, args):
        '''
        点击npc回调函数。
        '''
        npcEntityId = args['entityId']
        npcData = self.mNpcMgr.GetNpcData(npcEntityId)
        if not npcData:
            return
        player_entity_id = args['srcId']
        if npcData.name == 'lobby':
            netgameApi.TransferToOtherServer(player_entity_id, "lobby")

    # 函数名为Destroy才会被调用，在这个System被引擎回收的时候会调这个函数来销毁一些内容
    def Destroy(self):
        print "===== TutorialServerSystem Destroy ====="
        # 调用上面的反监听函数来销毁
        self.UnListenEvent()