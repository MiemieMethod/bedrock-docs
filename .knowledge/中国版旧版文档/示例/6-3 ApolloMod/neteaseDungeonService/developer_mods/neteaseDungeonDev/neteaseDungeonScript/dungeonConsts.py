# -*- coding: utf-8 -*-

# 整个Mod的一些绑定配置
ModVersion = "1.0.1"
ModNameSpace = "neteaseDungeon"
ServiceSystemName = "neteaseDungeonService"
ServiceSystemClsPath = "neteaseDungeonScript.dungeonServiceSystem.DungeonServiceSystem"
ServiceModuleName = "neteaseDungeon"

#event
RegisterGameDungeonsEvent = 'RegisterGameDungeonsEvent' #game向service注册副本id
TransferToDungeonByDungeonTypeEvent = 'TransferToDungeonByDungeonType' #请求切服到指定类型的副本
AskAndLockForDungeonByTypeEvent = 'AskAndLockForDungeonByTypeEvent'     # 申请并锁定一个指定类型的副本
UnlockDungeonEvent = 'UnlockDungeonEvent'       # 解锁一个使用【AskAndLockForDungeonByTypeEvent】申请的副本
PlayerJoinDungeonEvent = 'PlayerJoinDungeonEvent' #玩家加入副本事件
PlayerQuitDungeonEvent = 'PlayerQuitDungeonEvent' #玩家退出副本事件
ServerDisconnectEvent = 'ServerDisconnectEvent' #服务器同service断开连接事件
UpdateServerStatusEvent = 'UpdateServerStatusEvent'#更新服务器状态事件，处理未就绪服务器。
HttpRequestJoinDungeonEvent = 'HttpRequestJoinDungeonEvent' #处理http指令，请求进入副本事件
PlayerTransferToDungeonEvent = 'PlayerTransferToDungeonEvent'#玩家准备进入副本事件
HttpGetDungeonNumInfoEvent = 'HttpGetDungeonNumInfoEvent' #处理http指令，查询某个副本类型当前的占用数量和闲置数量
ResetDungeonEvent = 'ResetDungeonEvent' #重置副本事件
GetPreDungeonInfoEvent = 'GetPreDungeonInfoEvent' #获取玩家上一次进入副本信息的事件，要求上一次副本战斗还未结束。
ApplyToDungeonIdEvent = 'ApplyToDungeonIdEvent' #申请进入某副本
#时间
DungeonTransferTimeout = 360 #切服到副本超时时间为6min
ReDungeonTransferTime = 10 #两次申请切服到副本之间时间

#http错误码
SuccessCode = 1
FailCode = 2