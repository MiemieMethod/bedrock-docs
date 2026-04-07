# -*- coding:utf-8 -*-

# 整个Mod的一些绑定配置
ModVersion = "1.0.0"
ModNameSpace = "neteaseFriend"
ClientSystemName = "neteaseFriendBehavior"
ClientSystemClsPath = "neteaseFriendScript.neteaseFriendClientSystem.FriendClientSystem"
ServerSystemName = "neteaseFriendDev"
ServerSystemClsPath = "neteaseFriendScript.neteaseFriendServerSystem.FriendServerSystem"
ServiceSystemName = "neteaseFriendService"
ServiceSystemClsPath = "neteaseFriendScript.neteaseFriendServiceSystem.FriendServiceSystem"

import server.extraServiceApi as serviceApi

_serviceModSystem = None

def GetServiceModSystem():
	"""
	获取服务端系统，全局一个单例。
	"""
	global _serviceModSystem
	if not _serviceModSystem:
		_serviceModSystem = serviceApi.GetSystem(ModNameSpace, ServiceSystemName)
	return _serviceModSystem

def Destroy():
	global _serviceModSystem
	_serviceModSystem = None

# =======================================================================================================
# 一些事件
AddFriendFromServerEvent = "AddFriendFromServerEvent"
AcceptFriendFromServerEvent = "AcceptFriendFromServerEvent"
RefuseFriendFromServerEvent = "RefuseFriendFromServerEvent"
DeleteFriendFromServerEvent = "DeleteFriendFromServerEvent"
AddBlackFromServerEvent = "AddBlackFromServerEvent"
DeleteBlackFromServerEvent = "DeleteBlackFromServerEvent"

AddFriendResultFromServiceEvent = "AddFriendResultFromServiceEvent"
AddFriendNotifyFromServiceEvent = "AddFriendNotifyFromServiceEvent"

AcceptFriendResultFromServiceEvent = "AcceptFriendResultFromServiceEvent"
AcceptFriendNotifyFromServiceEvent = "AcceptFriendNotifyFromServiceEvent"

RefuseFriendResultFromServiceEvent = "RefuseFriendResultFromServiceEvent"

DeleteFriendResultFromServiceEvent = "DeleteFriendResultFromServiceEvent"
DeleteFriendNotifyFromServiceEvent = "DeleteFriendNotifyFromServiceEvent"

DeleteBlackListResultFromServiceEvent = "DeleteBlackListResultFromServiceEvent"

AddBlackListResultFromServiceEvent = "AddBlackListResultFromServiceEvent"
AddBlackListRNotifyFromServiceEvent = "AddBlackListRNotifyFromServiceEvent"

AddPlayerFromServerEvent = "AddPlayerFromServerEvent"
DelPlayerFromServerEvent = "DelPlayerFromServerEvent"

ChatFromServerEvent = "ChatFromServerEvent"
ChatFromClientEvent = "ChatFromClientEvent"
ChatResultFromServiceEvent = "ChatResultFromServiceEvent"
NewChatFromServiceEvent = "NewChatFromServiceEvent"

UpdatePlayerDataFromServiceEvent = "UpdatePlayerDataFromServiceEvent"
FriendStateResponseFromServiceEvent = "FriendStateResponseFromServiceEvent"

RNFriendsUpdateFromServiceEvent = "RNFriendsUpdateFromServiceEvent"

SyncRNFriendFromServerEvent = "SyncRNFriendFromServerEvent"

# UpdateRoleDigest
# =======================================================================================================
#========================================================================================================
#一些常量
FRIENDS_MAX_NUM = 200
BLACK_MAX_NUM = 200
#========================================================================================================
# 返回码，和返回消息
# 返回码，和返回消息
ResponseText = {}
CodeSuc = 0
ResponseText[CodeSuc] = "成功!"

AlreadyFriend = 1
ResponseText[AlreadyFriend] = "该玩家已经是您的好友了!"

FriendInYourBlack = 2
ResponseText[FriendInYourBlack] = "该玩家在你的黑名单列表内，请移除黑名单后重试!"

YouInFriendBlack = 3
ResponseText[YouInFriendBlack] = "该玩家已将你拉黑!"

YourFriendsMax = 4
ResponseText[YourFriendsMax] = "你的玩家数量已经达到上限!"

HisFriendsMax = 5
ResponseText[HisFriendsMax] = "该玩家的玩家数量已经达到上限!"

AlreadyInRequest = 6
ResponseText[AlreadyInRequest] = "您已经向该玩家发送好友邀请了!"

NotInRequest = 7
ResponseText[NotInRequest] = "该好友不在申请列表内!"

IsFriend = 8
ResponseText[IsFriend] = "是好友!"

IsNotFriend = 9
ResponseText[IsFriend] = "不是好友!"

CodeFailed = 10
ResponseText[CodeFailed] = "失败!"

FriendIsYou = 11
ResponseText[FriendIsYou] = "你不能加自己为好友"

FriendNone = 12
ResponseText[FriendNone] = "好友不存在"

YourTempFriendsMax = 13
ResponseText[YourFriendsMax] = "你的临时好友数量已经达到上限!"

HisTempFriendsMax = 14
ResponseText[HisFriendsMax] = "该玩家的临时好友数量已经达到上限!"

AlreadyInTempFriends = 15
ResponseText[AlreadyInTempFriends] = "已经加了临时好友！"
