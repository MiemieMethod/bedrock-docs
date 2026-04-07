# -*- coding:utf-8 -*-

# 整个Mod的一些绑定配置
ModVersion = "1.0.0"
ModNameSpace = "neteaseGuild"
ClientSystemName = "neteaseGuildBehavior"
ClientSystemClsPath = "neteaseGuildScript.neteaseGuildClientSystem.GuildClientSystem"
GameClientSystemName = "neteaseGuildGameClient"
GameClientSystemClsPath = "neteaseGuildGameScript.neteaseGuildGameClientSystem.GuildGameClientSystem"
GameServerSystemName = "neteaseGuildGameDev"
GameServerSystemClsPath = "neteaseGuildGameScript.neteaseGuildGameSystem.GuildGameSystem"
ServerSystemName = "neteaseGuildDev"
ServerSystemClsPath = "neteaseGuildScript.neteaseGuildServerSystem.GuildServerSystem"
ServiceSystemName = "neteaseGuildService"
ServiceSystemClsPath = "neteaseGuildScript.neteaseGuildServiceSystem.GuildServiceSystem"

import server.extraServerApi as serverApi
_serverModSystem = None

def GetServerModSystem():
	"""
	返回服务端系统对象，缓存实例提高性能。
	"""
	global _serverModSystem
	if not _serverModSystem:
		#print "GetServerModSystem", serverApi.GetSystem(ModNameSpace, GameServerSystemName)
		_serverModSystem = serverApi.GetSystem(ModNameSpace, GameServerSystemName)
	return _serverModSystem

def Destroy():
	"""
	释放对服务端系统对象的引用
	"""
	global _serverModSystem
	_serverModSystem = None

#"============================================================================================="
class GuildAttrType(object):
	"""
	公会的信息存储字段宏定义
	"""
	GuildId = 0 		# 公会的ID
	Name = 1 			# 名字
	Activity = 2		# 总活跃度
	ApplicationQueue = 3	# 申请列表
	PresidentPlayerDict = 4	# 会长玩家列表
	ElderPlayerDict = 5		# 长老玩家列表
	CommonPlayerDict = 6	# 平民玩家列表
	MapId = 7			# 地图标识
	MaxNum = 8			# 公会上限人数
	UnActivityDay = 9	# 不活跃的天数
	CurrentNum = 10		# 当前人数

class PlayerAttrType(object):
	"""
	单个公会成员的信息存储字段宏定义
	"""
	Uid = 0		# uid
	Name = 1 	# 名字
	Activity = 2	# 活跃度
	GuildId = 3		# 所在公会的ID
	Duty = 4		# 职务：普通，会长，长老
	Online = 5		# 是否在线
	ServerId = 6	# 所在服务器ID
	Level = 7		# 等级
	LastLoginTime = 8	# 上次登录时间

# =======================================================================================================
# 一些事件
SyncGuildAttrsFromServiceEvent = "SyncGuildAttrsFromServiceEvent"		# service向server同步公会信息
SyncPlayerAttrsFromServiceEvent = "SyncPlayerAttrsFromServiceEvent"		# service向server同步公会成员信息
AddServerPlayerEvent = "AddServerPlayerEvent"		# 引擎事件
DelServerPlayerEvent = "DelServerPlayerEvent"		# 引擎事件
AddPlayerFromServerEvent = "AddPlayerFromServerEvent"		# server向client、service通知有玩家上线
DelPlayerFromServerEvent = "DelPlayerFromServerEvent"		# server向client、service通知有玩家下线
SyncGuildAttrsFromServerEvent = "SyncGuildAttrsFromServerEvent"		# server向client同步公会信息
SyncPlayerAttrsFromServerEvent = "SyncPlayerAttrsFromServerEvent"	# server向client同步公会成员信息
CreateGuildFromClientEvent = "CreateGuildFromClientEvent"			# client向lobby请求创建新的公会
CreateGuildFromServerEvent = "CreateGuildFromServerEvent"			# server向service请求创建新公会
CreateGuildSuccessFromServerEvent = "CreateGuildSuccessFromServerEvent"	# server向service发送创建新公会完毕（扣除代币成功）
GetGuildBriefFromServerEvent = "GetGuildBriefFromServerEvent"		# client向server，或者server向service请求公会的快照信息
GetGuildBriefFromServiceEvent = "GetGuildBriefFromServiceEvent"		# service向server同步公会快照信息
GetGuildBriefFromClientEvent = "GetGuildBriefFromClientEvent"		# client向server，或者server向service同步公会信息
AddPlayerFromServerToClientEvent = "AddPlayerFromServerToClientEvent"	# 已废弃事件
JoinGuildFromClientEvent = "JoinGuildFromClientEvent"				# client向server请求加入指定公会
JoinGuildFromServerEvent = "JoinGuildFromServerEvent"				# server向service请求加入指定公会
AgreePlayerFromClientEvent = "AgreePlayerFromClientEvent"			# client向server发送同意玩家的加入公会请求
AgreePlayerFromServerEvent = "AgreePlayerFromServerEvent"			# server向service发送同意玩家的加入公会请求
AppointPlayerFromClientEvent = "AppointPlayerFromClientEvent"		# client向server请求调整公会成员的职务
AppointPlayerFromServerEvent = "AppointPlayerFromServerEvent"		# server向service请求调整公会成员的职务
KickPlayerFromClientEvent = "KickPlayerFromClientEvent"				# client向server请求踢掉指定公会成员
KickPlayerFromServerEvent = "KickPlayerFromServerEvent"				# server向service请求踢掉指定公会成员
ExitGuildFromClientEvent = "ExitGuildFromClientEvent"				# client向server请求离开公会
ExitGuildFromServerEvent = "ExitGuildFromServerEvent"				# server向service请求离开公会
ShowTipsFromServiceEvent = "ShowTipsFromServiceEvent"				# service向server发送弹出提示
ShowTipsFromServerEvent = "ShowTipsFromServerEvent"					# server向client发送弹出提示
ReturnLobbyFromClientEvent = "ReturnLobbyFromClientEvent"			# client向server请求返回公会驻地
LoginRequestEvent = "LoginRequestEvent"					# 初始化完成时，client向server发送此事件
LoginResponseEvent = "LoginResponseEvent"				# server向client回应【LoginRequestEvent】事件
UnShowUIFromServerEvent = "UnShowUIFromServerEvent"		# server向client发送强制关闭全部UI的事件


#返回码，和返回消息
ResponseText = {}
CodeSuc = 0
ResponseText[CodeSuc] = "成功!"

CodeServiceGuildNumOutOfLimit = 1
ResponseText[CodeServiceGuildNumOutOfLimit] = "服务器公会数量已经达到最大"
CodePlayerNone = 2
ResponseText[CodePlayerNone] = "玩家不存在"
CodePlayerHasGuild = 3
ResponseText[CodePlayerHasGuild] = "玩家已有公会"
CodeCreateSuccess = 4
ResponseText[CodeCreateSuccess] = "创建成功"
CodeParamError = 5
ResponseText[CodeParamError] = "参数错误"
CodeDutyNotEnough = 6
ResponseText[CodeDutyNotEnough] = "权限不足"
CodeGuildDiff = 7
ResponseText[CodeGuildDiff] = "公会不同"
CodeGuildNone = 8
ResponseText[CodeGuildNone] = "公会不存在"
CodeGuildPeopleMaxNum = 9
ResponseText[CodeGuildPeopleMaxNum] = "公会已达最大人数"
CodePlayerNotInGuild = 10
ResponseText[CodePlayerNotInGuild] = "玩家不在公会"
CodePresidentCannotLeaveGuild = 11
ResponseText[CodePresidentCannotLeaveGuild] = "会长无法退出公会，请转让会长后再退出公会。"
CodeGuildDisMiss = 12
ResponseText[CodeGuildDisMiss] = "公会解散"
CodeDBError = 13
ResponseText[CodeDBError] = "数据库操作失败"
CodeGuildNameNotLegal = 14
ResponseText[CodeGuildNameNotLegal] = "名字不合法"
CodeDiamondNotEnough = 15
ResponseText[CodeDiamondNotEnough] = "砖石数量不足"
CodeOutOfTime = 16
ResponseText[CodeOutOfTime] = "请求超时"
CodeKick = 17
ResponseText[CodeKick] = "你已经离开公会"
CodeAddSuccess = 18
ResponseText[CodeAddSuccess] = "你已经加入公会"
CodeApplicationMaxNum = 19
ResponseText[CodeApplicationMaxNum] = "该公会人数已满，看看其他公会吧"
CodeApplicationSuccess = 20
ResponseText[CodeApplicationSuccess] = "申请成功，请等待公会审批"
CodeGuildNameRepeated = 21
ResponseText[CodeGuildNameRepeated] = "名字重复"
#===========================================================================================================
#一些变量
# lobby默认的出生点坐标
DEFAULT_LOBBY_BORN_POS = [1393, 70, 40]

# 原始背包格子数
INV_SLOT_NUM = 36

#获取玩家背包物品信息
def GetPlayerItem(playerId, slotPos):
	print "GetPlayerItem", GetServerModSystem()
	_itemComp = GetServerModSystem().CreateComponent(playerId, 'Minecraft', 'item')
	return _itemComp.GetPlayerItem(serverApi.GetMinecraftEnum().ItemPosType.INVENTORY, slotPos)

# 获取玩家背包中钻石的数量
def GetPlayerDimondNum(playerId):
	diamondCount = 0
	for i in range(INV_SLOT_NUM):
		itemDict = GetPlayerItem(playerId, i)
		if itemDict == None:
			continue
		if itemDict['itemName'] == 'minecraft:diamond':
			diamondCount += itemDict['count']
	return diamondCount

# 设置玩家背包中指定格子的钻石数量
def SetDiamodDict(playerId, count, i):
	itemDict = {
		'itemName': 'minecraft:diamond',
		'count': count,
		'auxValue': 0,
	}
	comp = serverApi.CreateComponent(playerId, 'Minecraft', 'item')
	comp.SpawnItemToPlayerInv(itemDict, playerId, i)

# 从玩家背包中扣除指定数量的钻石	
def ConsumeDiamond(playerId, cost):
	remainCost = cost
	for i in range(INV_SLOT_NUM):
		if remainCost <= 0:
			return
		itemDict = GetPlayerItem(playerId, i)
		if itemDict == None:
			continue
		if itemDict['itemName'] == 'minecraft:diamond':
			if itemDict['count'] <= remainCost:
				SetDiamodDict(playerId, 0, i)
				remainCost = remainCost - itemDict['count']
			else:
				SetDiamodDict(playerId, itemDict['count'] - remainCost, i)
				remainCost = 0
