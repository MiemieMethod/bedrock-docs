# -*- coding: utf-8 -*-

# 获取引擎服务端API的模块
import server.extraServerApi as serverApi
import npcManager
import lobbyGame.netgameApi as netgameApi
from tutorialScripts.mongoOperation import MongoOperation
from tutorialScripts.mysqlOperation import MysqlOperation
import logout
# 获取引擎服务端System的基类，System都要继承于ServerSystem来调用相关函数
ServerSystem = serverApi.GetServerSystemCls()

class DbType(object):
    #使用的数据库种类
    Mongo = 1
    Mysql = 2

# 在modMain中注册的Server System类
class TutorialServerSystem(ServerSystem):

    # ServerSystem的初始化函数
    def __init__(self, namespace, systemName):
        # 首先调用父类的初始化函数
        super(TutorialServerSystem, self).__init__(namespace, systemName)
        print "===== TutorialServerSystem init ====="
        
        self.mMongoMgr = MongoOperation()
        self.mMysqlMgr = MysqlOperation()
        self.mDbType = 0
        if self.mMongoMgr.InitMongoDb() == True:
            self.mDbType = DbType.Mongo
        elif self.mMysqlMgr.InitMysqlDb() == True:
            self.mDbType = DbType.Mysql
        else:
            logout.error("[DATABASE_ERROR]db not exist!")
        self.mNpcMgr = npcManager.NpcManager(self)
        # 玩家player id到uid的映射
        self.mPlayerid2uid = {}
        # 初始时调用监听函数监听事件
        self.ListenEvent()
        # 设置为创造模式 0生存模式，1创造模式，2冒险模式
        netgameApi.SetLevelGameType(2)

    def ListenEvent(self):
        #玩家发送聊天信息时触发
        self.ListenForEvent(serverApi.GetEngineNamespace(), serverApi.GetEngineSystemName(), "ServerChatEvent", self, self.OnServerChat)
        #玩家加入时触发该事件
        self.ListenForEvent(serverApi.GetEngineNamespace(), serverApi.GetEngineSystemName(), 'AddServerPlayerEvent',self, self.OnAddServerPlayer)
        #entity被敲击时触发
        self.ListenForEvent(serverApi.GetEngineNamespace(), serverApi.GetEngineSystemName(), 'EntityBeKnockEvent', self,self.OnNpcTouched)
        #游戏内自动生成怪物时触发
        self.ListenForEvent(serverApi.GetEngineNamespace(), serverApi.GetEngineSystemName(), 'ServerSpawnMobEvent', self,self.OnServerSpawn)

    def UnListenEvent(self):
        self.UnListenForEvent(serverApi.GetEngineNamespace(), serverApi.GetEngineSystemName(), "ServerChatEvent", self, self.OnServerChat)
        self.UnListenForEvent(serverApi.GetEngineNamespace(), serverApi.GetEngineSystemName(), 'AddServerPlayerEvent',self, self.OnAddServerPlayer)
        self.UnListenForEvent(serverApi.GetEngineNamespace(), serverApi.GetEngineSystemName(), 'EntityBeKnockEvent', self,self.OnNpcTouched)

    # 监听ServerChatEvent的回调函数
    def OnServerChat(self, args):
        print "==== OnServerChat ==== ", args
        # 生成掉落物品
        # 当我们输入的信息等于右边这个值时，创建相应的物品
        if args["message"] == "钻石剑":
            # 创建Component，用来完成特定的功能，这里是为了创建Item物品
            comp = serverApi.CreateComponent(serverApi.GetLevelId(), "Minecraft", "item")
            # 给这个Component赋值，参数参考《MODSDK文档》
            comp.addItems = [("minecraft:diamond_sword", 1, 0, True, {"to": "inventory", "playerId": args["playerId"]})]
            # 这一步很重要，它告诉系统需要更新这个Component，继而完成响应的功能
            self.NeedsUpdate(comp)
            #记录玩家钻石剑数量
            self.AddDiamondSword(args["playerId"])
        elif args["message"] == "钻石镐":
            comp = serverApi.CreateComponent(serverApi.GetLevelId(), "Minecraft", "item")
            comp.addItems = [("minecraft:diamond_pickaxe", 1, 0, True, {"to": "inventory", "playerId": args["playerId"]})]
            self.NeedsUpdate(comp)
        elif args["message"] == "钻石头盔":
            comp = serverApi.CreateComponent(serverApi.GetLevelId(), "Minecraft", "item")
            comp.addItems = [("minecraft:diamond_helmet", 1, 0, True, {"to": "inventory", "playerId": args["playerId"]})]
            self.NeedsUpdate(comp)
        elif args["message"] == "钻石胸甲":
            comp = serverApi.CreateComponent(serverApi.GetLevelId(), "Minecraft", "item")
            comp.addItems = [("minecraft:diamond_chestplate", 1, 0, True, {"to": "inventory", "playerId": args["playerId"]})]
            self.NeedsUpdate(comp)
        elif args["message"] == "钻石护腿":
            comp = serverApi.CreateComponent(serverApi.GetLevelId(), "Minecraft", "item")
            comp.addItems = [("minecraft:diamond_leggings", 1, 0, True, {"to": "inventory", "playerId": args["playerId"]})]
            self.NeedsUpdate(comp)
        elif args["message"] == "钻石靴子":
            comp = serverApi.CreateComponent(serverApi.GetLevelId(), "Minecraft", "item")
            comp.addItems = [("minecraft:diamond_boots", 1, 0, True, {"to": "inventory", "playerId": args["playerId"]})]
            self.NeedsUpdate(comp)
        else:
            print "==== Sorry man ===="

    def AddDiamondSword(self,playerId):
        '''
        插入一件钻石剑记录到数据库
        :param playerId:
        :return:
        '''
        if playerId == "-1":
            return
        if self.mDbType == DbType.Mongo:
            self.mMongoMgr.AddDiamondSword(playerId)
        elif self.mDbType == DbType.Mysql:
            self.mMysqlMgr.AddDiamondSword(playerId)

    def OnServerSpawn(self,args):
        args["cancel"] = False

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
        npc_entity_id = args['entityId']
        npc_data = self.mNpcMgr.GetNpcData(npc_entity_id)
        if not npc_data:
            return
        player_entity_id = args['srcId']
        uid = self.mPlayerid2uid[player_entity_id]
        if npc_data.name == 'lobby':
            # request_data = {'uid': uid, 'player_id': player_entity_id}
            # self.RequestToService('AwesomeMatch', 'RequestLobby', request_data)
            netgameApi.TransferToOtherServer(player_entity_id, "lobby")

    # 函数名为Destroy才会被调用，在这个System被引擎回收的时候会调这个函数来销毁一些内容
    def Destroy(self):
        print "===== TutorialServerSystem Destroy ====="
        # 调用上面的反监听函数来销毁
        self.UnListenEvent()
        # 结束数据库线程池，确保相关异步任务全部执行完。
        if self.mDbType == DbType.Mongo:
            self.mMongoMgr.Destroy()
        elif self.mDbType == DbType.Mysql:
            self.mMysqlMgr.Destroy()