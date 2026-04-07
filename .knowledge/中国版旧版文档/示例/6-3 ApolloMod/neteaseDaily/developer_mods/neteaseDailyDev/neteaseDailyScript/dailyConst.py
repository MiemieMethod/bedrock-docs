# -*- coding: utf-8 -*-

# 整个Mod的一些绑定配置
ModVersion = "1.0.0"
ModName = "neteaseDaily"
ClientSystemName = "neteaseDailyBeh"
ClientSystemClsPath = "neteaseDailyScript.dailyClientSystem.DailyClientSystem"
ServerSystemName = "neteaseDailyDev"
ServerSystemClsPath = "neteaseDailyScript.dailyServerSystem.DailyServerSystem"
ServiceSystemName = "neteaseDailyService"
ServiceSystemClsPath = "neteaseDailyScript.dailyServiceSystem.DailyServiceSystem"
MasterSystemName = "neteaseDailyMaster"
MasterSystemClsPath = "neteaseDailyScript.dailyMasterSystem.DailyMasterSystem"

# UI
dailyUIName = "dailyUI"
dailyUIClsPath = "neteaseDailyScript.dailyClientUI.DailyScreen"
dailyUIScreenDef = "dailyUI.main"

# 配置名称
CfgKeyRewards = 'Rewards'

# 数据库表名
# 玩家每日登录奖励领取信息表
TableDailyReward = "neteaseDailyRewardInfo"

# 引擎事件
UiInitFinishedEvent = "UiInitFinished"

# 事件
QueryPlayerRecvEvent = 'QueryPlayerRecvEvent'
DisplayDailyRewardEvent = 'DisplayDailyRewardEvent'
PlayerRecvEvent = 'PlayerRecvEvent'


# 指令
class DailyRequestMapping(object):
	Query = "/query-player-recv"


# 错误码
RespCodeSuccess = 1  # 请求成功
RespCodeInvalidParameter = 4  # 请求参数有误
RespCodeInvalidUser = 2  # 用户不存在或不在线
RespCodeTimeout = 2  # 请求超时
RespCodeDBError = 3  # 数据库操作失败
