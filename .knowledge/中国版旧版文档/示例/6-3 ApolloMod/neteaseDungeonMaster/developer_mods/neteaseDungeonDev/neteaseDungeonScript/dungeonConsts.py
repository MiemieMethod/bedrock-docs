# -*- coding: utf-8 -*-

# 整个Mod的一些绑定配置
ModVersion = "1.0.1"
ModNameSpace = "neteaseDungeon"
ServiceSystemName = "neteaseDungeonService"
MasterSystemName = "neteaseDungeonMaster"
LobbyServerSystemName = "neteaseDungeonLobbyServer"
ServiceSystemClsPath = "neteaseDungeonScript.dungeonServiceSystem.DungeonServiceSystem"
MasterSystemClsPath = "neteaseDungeonScript.dungeonMasterSystem.DungeonMasterSystem"
ServiceModuleName = "neteaseDungeon"

#event
RegisterGameDungeonsEvent = 'RegisterGameDungeonsEvent' #game向service注册副本id
TransferToDungeonByDungeonTypeEvent = 'TransferToDungeonByDungeonType' #请求切服到指定类型的副本
PlayerJoinDungeonEvent = 'PlayerJoinDungeonEvent' #玩家加入副本事件
PlayerQuitDungeonEvent = 'PlayerQuitDungeonEvent' #玩家退出副本事件
ServerDisconnectEvent = 'ServerDisconnectEvent' #服务器同service断开连接事件
UpdateServerStatusEvent = 'UpdateServerStatusEvent'#更新服务器状态事件，处理未就绪服务器。
HttpRequestJoinDungeonEvent = 'HttpRequestJoinDungeonEvent' #处理http指令，请求进入副本事件
HttpGetDungeonNumInfoEvent = 'HttpGetDungeonNumInfoEvent' #处理http指令，查询某个副本类型当前的占用数量和闲置数量

#http url地址
TransferToDungeonUrl = '/dungeon/transfer-by-dungeon-type'
GetDungeonNumInfoByTypeUrl = '/dungeon/get-dungeon-num-info-by-dungeon-type'

#时间配置
DungeonTransferTimeout = 360 #切服到副本超时时间为6min
ReDungeonTransferTime = 10 #两次申请切服到副本之间时间

#http错误码
SuccessCode = 1
FailCode = 2