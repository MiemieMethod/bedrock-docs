# -*- coding: utf-8 -*-

#整个Mod的一些绑定配置
ModVersion = "1.0.1"
ModNameSpace = "neteaseDungeon"
ServiceSystemName = "neteaseDungeonService"
LobbyServerSystemName = "neteaseDungeonLobbyServer"
GameServerSystemName = "neteaseDungeonGameServer"
ServiceSystemClsPath = "neteaseDungeonScript.dungeonServiceSystem.DungeonServiceSystem"
LobbySystemClsPath = "neteaseDungeonScript.dungeonLobbyServerSys.DungeonLobbySys"
GameSystemClsPath = "neteaseDungeonScript.dungeonGameServerSys.DungeonGameSys"
ServiceModuleName = "neteaseDungeon"

#event
RegisterGameDungeonsEvent = 'RegisterGameDungeonsEvent' #game向service注册副本id
TransferToDungeonByDungeonTypeEvent = 'TransferToDungeonByDungeonType' #请求切服到指定类型的副本
PlayerJoinDungeonEvent = 'PlayerJoinDungeonEvent' #玩家加入副本事件
PlayerQuitDungeonEvent = 'PlayerQuitDungeonEvent' #玩家退出副本事件
ServerDisconnectEvent = 'ServerDisconnectEvent' #服务器同service断开连接事件
UpdateServerStatusEvent = 'UpdateServerStatusEvent'#更新服务器状态事件，处理未就绪服务器。
PlayerLoginDungeonEvent = 'PlayerLoginDungeonEvent' #game服务器，玩家加入副本事件
PlayerLogoutDungeonEvent = 'PlayerLogoutDungeonEvent' #game服务器，玩家退出副本事件
ServiceConnectEvent = 'ServiceRegisterModuleEvent'#开始注册service module事件
AddServerPlayerEvent = 'AddServerPlayerEvent' #玩家登录到lobby/game事件
DelServerPlayerEvent = 'DelServerPlayerEvent' #玩家离开到lobby/game事件
ServerChatEvent = 'ServerChatEvent'
ResetDungeonEvent = 'ResetDungeonEvent' #重置副本事件

#时间常量
DungeonTransferTimeout = 360 #切服到副本超时时间为6min
ReDungeonTransferTime = 10 #两次申请切服到副本之间时间