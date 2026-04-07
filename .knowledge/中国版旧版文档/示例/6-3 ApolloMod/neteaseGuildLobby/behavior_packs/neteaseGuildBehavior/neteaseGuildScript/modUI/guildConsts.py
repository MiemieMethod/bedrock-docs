# -*- coding:utf-8 -*-

# 整个Mod的一些绑定配置
ModVersion = "1.0.0"
ModNameSpace = "neteaseGuild"
ClientSystemName = "neteaseGuildBehavior"
ClientSystemClsPath = "neteaseGuildScript.neteaseGuildClientSystem.GuildClientSystem"
ServerSystemName = "neteaseGuildDev"
ServerSystemClsPath = "neteaseGuildScript.neteaseGuildServerSystem.GuildServerSystem"
ServiceSystemName = "neteaseGuildService"
ServiceSystemClsPath = "neteaseGuildScript.neteaseGuildServiceSystem.GuildServiceSystem"

import client.extraClientApi as clientApi
_clientModSystem = None
def GetClientModSystem():
	"""
	返回客户端系统对象，缓存实例提高性能。
	"""
	global _clientModSystem
	if not _clientModSystem:
		_clientModSystem = clientApi.GetSystem(ModNameSpace, ClientSystemName)
	return _clientModSystem


def Destroy():
	"""
	释放对客户端系统对象的引用
	"""
	global _clientModSystem
	_clientModSystem = None

# "============================================================================================="
class DutyType(object):
	"""
	公会的职务宏定义
	"""
	President = 2	# 会长
	Elder = 1		# 长老
	Common = 0		# 普通会员

class GuildAttrType(object):
	"""
	公会的信息存储字段宏定义
	"""
	GuildId = 0 	# 公会的ID
	Name = 1 		# 名字
	Activity = 2	# 总活跃度
	ApplicationQueue = 3	# 申请列表
	PresidentPlayerDict = 4	# 会长玩家列表
	ElderPlayerDict = 5		# 长老玩家列表
	CommonPlayerDict = 6	# 平民玩家列表
	MapId = 7				# 地图标识
	MaxNum = 8				# 公会上限人数
	UnActivityDay = 9		# 不活跃的天数
	CurrentNum = 10			# 当前人数

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
	
class UIDef:
	"""
	公会相关的UI界面
	"""
	# 处理加入申请的界面
	UI_APPLY = {
		'ui_key': 'ApplyUI',
		'ui_cls_path': 'neteaseGuildScript.modUI.applyUI.ApplyScreen',
		'ui_def': 'ApplyUI.main'
	}
	# 创建公会界面
	UI_CREATEGUILD = {
		'ui_key': 'CreateGuildUI',
		'ui_cls_path': 'neteaseGuildScript.modUI.createGuildUI.CreateGuildScreen',
		'ui_def': 'CreateGuildUI.main'
	}
	# 加入公会界面
	UI_JOIN = {
		'ui_key': 'JoinUI',
		'ui_cls_path': 'neteaseGuildScript.modUI.joinUI.JoinScreen',
		'ui_def': 'JoinUI.main'
	}
	# 我的公会状态界面
	UI_MYGUILD = {
		'ui_key': 'MyGuildUI',
		'ui_cls_path': 'neteaseGuildScript.modUI.myGuildUI.MyGuildScreen',
		'ui_def': 'MyGuildUI.main'
	}
	# 退出公会弹出
	UI_QUIT = {
		'ui_key': 'QuitUI',
		'ui_cls_path': 'neteaseGuildScript.modUI.quitUI.QuitScreen',
		'ui_def': 'QuitUI.main'
	}

class NotifyDef:
	EXIT_GUILD = {
		'notify_type': '退出公会',
		'title': '退出公会',
		'message': '确定退出%s公会吗？',
		'confirm': '确定',
		'cancel': '取消'
	}

# =======================================================================================================
# 一些事件
SyncGuildAttrsFromServiceEvent = "SyncGuildAttrsFromServiceEvent"		# service向server同步公会信息
SyncPlayerAttrsFromServiceEvent = "SyncPlayerAttrsFromServiceEvent"		# service向server同步公会成员信息
AddServerPlayerEvent = "AddServerPlayerEvent"		# 引擎事件
DelServerPlayerEvent = "DelServerPlayerEvent"		# 引擎事件
AddPlayerFromServerEvent = "AddPlayerFromServerEvent"				# server向client、service通知有玩家上线
DelPlayerFromServerEvent = "DelPlayerFromServerEvent"				# server向client、service通知有玩家下线
SyncGuildAttrsFromServerEvent = "SyncGuildAttrsFromServerEvent"		# server向client同步公会信息
SyncPlayerAttrsFromServerEvent = "SyncPlayerAttrsFromServerEvent"	# server向client同步公会成员信息
UiInitFinishedEvent = 'UiInitFinished'				# 引擎事件
CreateGuildFromClientEvent = "CreateGuildFromClientEvent"			# client向lobby请求创建新的公会
GetGuildBriefFromServerEvent = "GetGuildBriefFromServerEvent"		# client向server，或者server向service请求公会的快照信息
GetGuildBriefFromServiceEvent = "GetGuildBriefFromServiceEvent"		# service向server同步公会快照信息
GetGuildBriefFromClientEvent = "GetGuildBriefFromClientEvent"		# client向server，或者server向service同步公会信息
AddPlayerFromServerToClientEvent = "AddPlayerFromServerToClientEvent"	# 已废弃事件
ShowUIFromClientEvent = "ShowUIFromClientEvent"				# client内部事件，显示指定UI
JoinGuildFromClientEvent = "JoinGuildFromClientEvent"		# client向server请求加入指定公会
AgreePlayerFromClientEvent = "AgreePlayerFromClientEvent"		# client向server发送同意玩家的加入公会请求
AppointPlayerFromClientEvent = "AppointPlayerFromClientEvent"	# client向server请求调整公会成员的职务
KickPlayerFromClientEvent = "KickPlayerFromClientEvent"		# client向server请求踢掉指定公会成员
ExitGuildFromClientEvent = "ExitGuildFromClientEvent"		# client向server请求离开公会
ReturnGuildMapFromClientEvent = "ReturnGuildMapFromClientEvent"		# client向server请求返回公会驻地
ShowCreateGuildUIFromClientEvent = "ShowCreateGuildUIFromClientEvent"		# client向server请求打开创建公会界面
ShowCreateGuildUIFromServerEvent = "ShowCreateGuildUIFromServerEvent"		# server向client通知打开创建公会界面
