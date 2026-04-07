插件介绍：
副本管理插件，该插件用于管理副本的进入、退出、排队，以及单地图多副本功能。服主使用该插件后：
（1） 如果副本承载人数达到上限，会有等待界面提示玩家等待；
（2） 服主只需关心副本内部的逻辑，无需关心如何分配玩家到哪个game，无需关心优化副本承载的逻辑；
（3） 可以很方便的管理一个地图多个副本的情况（这么做是为了避免开太多game服）
（4） 不同副本中的聊天互相不可见，同一副本内的玩家聊天互相可见。
实战实例1：
开发者制作了单人新手副本，在一个地图中有20个新手副本区域，然后部署了10个game。那么就支持同时有200个人玩新手副本。使用副本管理插件后，会自动将新手分配到空闲的副本区域，如当前第20个game服的副本区域5空闲，第1个game服中的副本区域1空闲，那么新的想进入副本的玩家会被分配到这两个中的一个。当所有副本区域都满了之后，后续进入的新玩家会出现排队界面。
实战实例2：
设计了两个副本，一个是中午时段开放的副本A，一个是晚上时段开放的副本B；假设人数有200人，一个game可承载20人，如果两个副本分别放在不同的不同的地图，就需要开20个game，副本A10个，副本B10个；由于这两个副本的时段是错开的，用了副本管理插件后：服主可以在一张地图上做副本A和副本B，这样只需开10个game就可以了。


插件构成：
（1）neteaseDungeonGame: 部署于游戏服。
（2）neteaseDungeonLobby: 部署于大厅服。
（3）neteaseDungeonMaster: 部署于控制服。
（4）neteaseDungeonService: 部署于功能服。

使用步骤：
（1）配置lobby、game、service中mod.json，请按照文件mod.json中"_comment"注释配置对应内容。
（2）MCStudio把neteaseDungeonGame添加到游戏服，把neteaseDungeonLobby添加到大厅服，把neteaseDungeonMaster添加到控制服，把neteaseDungeonService添加到功能服。若不是MCStudio添加neteaseDungeonService，则需要手动将字符串"neteaseDungeon"添加到deploy.json中service下的module_names属性中。
（3）使用本插件提供的event和api完成游戏功能。

插件api：
（1）将玩家转入某个副本类型的game中
适用服务器：lobby
函数：TransferToDungeon(playerId, dungeonType)
参数：
    playerId: str, 玩家对象的entityId
    dungeonType：str, 副本类型，对应mod.json文件中game_dungeon_list中的dungeon_type配置
示例：
    import server.extraServerApi as serverApi
    dungeonSystem = serverApi.GetSystem("neteaseDungeon", "neteaseDungeonLobbyServer")
    dungeonSystem.TransferToDungeon('1234455', 'dungeonA')

（2）获取玩家上一次进入副本信息。
适用服务器：lobby
函数：GetPreDungeonInfoByUid(uid, cb)
参数：
    uid: int，玩家uid
    cb: function，异步回调函数。回调函数包含三个参数：uid, preServerId, preDungenoId。uid：int，是玩家uid。preServerId：int，是上次副本所在服务器id。preDungenoId：int，是上次副本的副本id。若上次副本不存在或战斗结束，则preServerId和preDungenoId为-1
返回：
    无
示例：
    def testCb1(uid, serverId, dungenoId):
        print 'testCb1', uid, serverId, dungenoId
    import server.extraServerApi as serverApi
    dungeonSystem = serverApi.GetSystem("neteaseDungeon", "neteaseDungeonLobbyServer")
    dungeonSystem.GetPreDungeonInfoByUid(123, testCb1)

（3）进入指定副本
适用服务器：lobby
函数：TransferToDungeonById(uid, serverId, dungeonId, cb)
参数：
    uid: int，玩家uid
    serverId：int，副本所在服务器id
    dungeonId：int，副本id
    cb：function，异步回调函数。回调函数包含一个参数：bCanJoin。bCanJoin：bool，是否能进入副本。若为True，则玩家会切服到指定副本，否则不做处理。
示例：
    def testCb2(bCanJoin):
        print 'testCb2', bCanJoin
    import server.extraServerApi as serverApi
    dungeonSystem = serverApi.GetSystem("neteaseDungeon", "neteaseDungeonLobbyServer")
    dungeonSystem.TransferToDungeonById(123, 3000000, 0, testCb2)

（4）获取当前位置的副本类型及各项配置项
适用服务器：game
函数：GetDungeonConfByPos(position)
参数：
    position: list(float, float, float)，位置坐标
返回：
    None/dict, 若位置不在任何副本中，则返回None，否则返回副本配置信息。
    返回dict中包含的key和对应值说明如下：
        "offset": list(float, float, float)， 副本区域偏移量，对应mod.json文件中game_dungeon_list中area_offset配置
        "type": str，副本类型，对应mod.json文件中game_dungeon_list中的dungeon_type配置
        "name": str，副本名字，对应mod.json文件中dungeon_type_list中的name配置
        "maxNum": int, 单个副本可以容纳的人数，对应mod.json文件中dungeon_type_list中的max_players配置
        "minPos": list(float, float, float)，立方区域顶点，为立方区域的最小值，对应mod.json文件中dungeon_type_list中的area_min_vertex配置
        "maxPos": list(float, float, float)，立方区域顶点，为立方区域的最大值，对应mod.json文件中dungeon_type_list中的area_max_vertex配置
        "bornPos": list(float, float, float)，玩家出生点，对应mod.json文件中dungeon_type_list中的born_pos配置
        "dungeonId": int, 副本id，表示mod.json文件中game_dungeon_list中某类型game的第几个副本配置，id从0开始。
示例：
    import server.extraServerApi as serverApi
    dungeonSystem = serverApi.GetSystem("neteaseDungeon", "neteaseDungeonGameServer")
    pos = (1384.009, 52, 24.437)
    conf = dungeonSystem.GetDungeonConfByPos(pos)
    '''
    执行结果示例：
    {'maxNum': 2, 'name': u'dungeonNameB', 'dungeonId': 1, 'bornPos': [1454.701, 72, 64.195], 'offset': [0, 0, 0], 'minPos': [1444, 68, 54], 'maxPos': [1464, 88, 74], 'type': u'dungeonB'}
    '''

（5）获取当前所在副本区域的位置偏移
适用服务器：game
函数：GetDungeonOffsetByPos(position)
参数：
    position: list(float, float, float)，位置坐标
返回：
    list(float, float, float)， 若位置不在任何副本中，则返回[0, 0, 0]，否则返回副本的偏移量。它对应对应mod.json文件中game_dungeon_list中area_offset配置
示例：
    import server.extraServerApi as serverApi
    dungeonSystem = serverApi.GetSystem("neteaseDungeon", "neteaseDungeonGameServer")
    pos = [1384.009, 52, 24.437]
    conf = dungeonSystem.GetDungeonOffsetByPos(pos)

（6）获取当前副本的玩家列表
适用服务器：game
函数：GetPlayerUidsByDungeonId(dungeonId)
参数：
    dungeonId：int，副本id
返回：
    list(int), 玩家uid列表
示例：
    import server.extraServerApi as serverApi
    dungeonSystem = serverApi.GetSystem("neteaseDungeon", "neteaseDungeonGameServer")
    uidList = dungeonSystem.GetPlayerUidsByDungeonId(0)

（7）重置副本，副本会转为空闲状态，强制将副本中玩家转移到大厅服。通常副本战斗结束后，调用本api，告知本次战斗结束，开启了下次战斗。
适用服务器：game
函数：ResetDungeon(dungeonId)
参数：
    dungeonId：int，副本id
返回：
    无
示例：
    import server.extraServerApi as serverApi
    dungeonSystem = serverApi.GetSystem("neteaseDungeon", "neteaseDungeonGameServer")
    dungeonSystem.ResetDungeon(0) #重置这个game的0号副本，其他玩家可以进入0号副本了。
注意：结束战斗后一定要调用本api重置副本，否则副本会一直被占用，其他玩家一直无法进入。

（8）申请并锁定一个指定类型的副本。
适用服务器：lobby
函数：AskAndLockDungeonByType(dungeonType, uidList, overtime, cbFunc)
参数：
    dungeonType：str, 副本类型，对应mod.json文件中game_dungeon_list中的dungeon_type配置
    uidList: list(int), 参与这个副本的玩家uid列表
    overtime: int，需要锁定这个副本多久，单位秒，锁定期间副本不会被分配出去
    cbFunc: function，异步回调函数。回调函数包含三个参数：suc, serverid, dungeonId。suc：bool，当uidList中已经有uid申请了锁定副本，并且尚未解锁，那么会返回False；serverid：int，副本所在的服务器进程id（负数代表没有可用的副本）。dungeonId：int，目标服务器进程中的副本的唯一id（负数代表没有可用的副本）。
返回：
    无
示例：
    def testCb1(suc, serverId, dungenoId):id
        print 'testCb1 suc={} serverId={} dungenoId={}'.format(suc, serverId, dungenoId)
    import server.extraServerApi as serverApi
    dungeonSystem = serverApi.GetSystem("neteaseDungeon", "neteaseDungeonLobbyServer")
    dungeonSystem.AskAndLockDungeonByType("dungeonA", [123, 345], 600, testCb1)

（9）解除使用【AskAndLockDungeonByType】申请的副本的锁定。
适用服务器：lobby
函数：ReleaseLockedDungeon(serverId, dungeonId, cbFunc=None)
参数：
    serverId：int，副本所在的服务器进程id
    dungeonId：int，目标服务器进程中的副本的唯一id
    cbFunc: function，异步回调函数。回调函数包含两个参数：find, suc。find：bool，满足条件的副本是否存在（副本没有被锁定或者锁定已经超时也会返回False）。suc：bool，解除锁定是否成功，当副本中还存在玩家时，结束锁定会失败。
返回：
    无
示例：
    def testCb1(find, suc):
        print 'testCb1 find={} suc={}'.format(find, suc)
    import server.extraServerApi as serverApi
    dungeonSystem = serverApi.GetSystem("neteaseDungeon", "neteaseDungeonLobbyServer")
    dungeonSystem.ReleaseLockedDungeon(123, 0, testCb1)

插件event：
（1）PlayerLoginDungeonEvent
适用服务器：game
命名空间：namespace = 'neteaseDungeon',systemname = 'neteaseDungeonGameServer'
描述：玩家进入副本事件，玩家进入副本所在游戏会触发本事件。本事件在AddServerPlayerEvent事件之后触发。
参数：
    uid：int，玩家uid
    dungeonId：int，副本id

（2）PlayerLogoutDungeonEvent
适用服务器：game
命名空间：namespace = 'neteaseDungeon',systemname = 'neteaseDungeonGameServer'
描述：玩家退出副本事件，玩家离开副本游戏会触发本事件。本事件在DelServerPlayerEvent事件之后触发。注意玩家退出，副本不会空余一个玩家额度，只能调用ResetDungeon重置副本，才能清空占用配额。例如：副本最多允许2个玩家，若玩家A和B都进入本副本，B中途退出，则调用ResetDungeon之前，是不会有新玩家分配到这个副本的。
参数：
    uid：int，玩家uid
    dungeonId：int，副本id

运营指令：
（1）将某个玩家转入到指定的副本类型
post url: http:masterip:masterport/dungeon/transfer-by-dungeon-type
post body:{
    "uid" : 123  #玩家uid
    "dungeonType" : "dungeonNameB" #副本类型
}
response:
 {
     "code": 1, #1表示成功，0表示失败
     "entity": {
         "uid" : 123  #玩家uid
         "descServerId" : 3000000 #副本所在服务器的id
         "descDungeonId" : 0 #副本id
       },
       "message": ""
 }

（2）查询某个副本类型当前的占用数量和闲置数量（一个副本区域算1个）
post url: http:masterip:masterport/dungeon/get-dungeon-num-info-by-dungeon-type
post body:{
    "dungeonType" : "dungeonNameB" #副本类型
}
response:
 {
     "code": 1, #1表示成功，0表示失败
     "entity": {
         "free" : 1  #空闲副本数量
         "occupied" : 1 #被占用副本数量
       },
       "message": ""
 }

 更新列表：
1.0.0版本：
初始版本
1.0.1版本：
新增API：
    （8）申请并锁定一个指定类型的副本。
    （9）解除使用【AskAndLockDungeonByType】申请的副本的锁定。
1.0.2版本：
1、使用公开稳定的API：SetLayer和SetVisible替换set_visible和set_layer，避免有时候出现UI错乱问题
    