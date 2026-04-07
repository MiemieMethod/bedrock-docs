# -*- coding: utf-8 -*-

# 整个Mod的一些绑定配置
ModVersion = "1.0.0"
ModName = "neteaseQuest"
ServiceSystemName = "neteaseQuestService"
ServiceSystemClsPath = "neteaseQuestScript.questServiceSystem.QuestServiceSystem"
MasterSystemName = "neteaseQuestMaster"
MasterSystemClsPath = "neteaseQuestScript.questMasterSystem.QuestMasterSystem"

QUEST_KILL_MONSTER = 'KM'
QUEST_COLLECT_ITEM = 'CI'
QUEST_ARRIVE_PLACE = 'AP'
QUEST_PLAYER_LEVEL = 'PL'

# 数据库表名
# 任务数据信息表
TableQuestData = "neteaseQuestDataInfo"

# 引擎事件
UiInitFinishedEvent = "UiInitFinished"
AddServerPlayerEvent = 'AddServerPlayerEvent'
DelServerPlayerEvent = 'DelServerPlayerEvent'

# 事件
PushQuestDataEvent = 'PushQuestDataEvent'
PullQuestDataEvent = 'PullQuestDataEvent'
QueryQuestDataEvent = 'QueryQuestDataEvent'
UpdateQuestDataEvent = 'UpdateQuestDataEvent'


# 玩家货币指令
class QuestRequestMapping(object):
	Query = "/query-quest-data"
	Update = "/update-quest-data"


# 错误码
RespCodeSuccess = 1  # 请求成功
RespCodeInvalidParameter = 4  # 请求参数有误
RespCodeInvalidUser = 2  # 用户不存在或不在线
RespCodeTimeout = 2  # 请求超时
RespCodeDBError = 3  # 数据库操作失败
