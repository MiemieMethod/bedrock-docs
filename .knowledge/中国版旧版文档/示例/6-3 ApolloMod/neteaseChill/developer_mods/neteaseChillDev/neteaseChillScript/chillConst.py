# -*- coding: utf-8 -*-

# 整个Mod的一些绑定配置
ModVersion = "1.0.0"
ModName = "neteaseChill"
ClientSystemName = "neteaseChillBeh"
ClientSystemClsPath = "neteaseChillScript.chillClientSystem.ChillClientSystem"
ServerSystemName = "neteaseChillDev"
ServerSystemClsPath = "neteaseChillScript.chillServerSystem.ChillServerSystem"
ServiceSystemName = "neteaseChillService"
ServiceSystemClsPath = "neteaseChillScript.chillServiceSystem.ChillServiceSystem"
MasterSystemName = "neteaseChillMaster"
MasterSystemClsPath = "neteaseChillScript.chillMasterSystem.ChillMasterSystem"

# UI
chillUIName = "moneyUI"
chillUIClsPath = "neteaseChillScript.chillClientUI.ChillScreen"
chillUIScreenDef = "moneyUI.main"

# 配置名称
CfgKeyRewards = 'Rewards'

# 数据库表名
# 玩家活动奖励领取信息表
TableChillReward = "neteaseChillRewardInfo"

# 引擎事件
UiInitFinishedEvent = "UiInitFinished"
AddServerPlayerEvent = 'AddServerPlayerEvent'
DelServerPlayerEvent = 'DelServerPlayerEvent'

# 事件
QueryPlayerChillEvent = 'QueryPlayerChillEvent'
DisplayChillRewardEvent = 'DisplayChillRewardEvent'
PlayerRecvChillRewardEvent = 'PlayerRecvChillRewardEvent'
PlayerAchvChillRewardEvent = 'PlayerAchvChillRewardEvent'
NavigateToShopEvent = 'NavigateToShopEvent'


# 指令
class ChillRequestMapping(object):
	Query = "/query-player-chill"


# 错误码
RespCodeSuccess = 1  # 请求成功
RespCodeInvalidParameter = 4  # 请求参数有误
RespCodeInvalidUser = 2  # 用户不存在或不在线
RespCodeTimeout = 2  # 请求超时
RespCodeDBError = 3  # 数据库操作失败
