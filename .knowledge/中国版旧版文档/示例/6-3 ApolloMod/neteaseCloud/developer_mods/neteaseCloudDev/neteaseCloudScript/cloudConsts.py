# -*- coding: utf-8 -*-

#---------------------------------------------------------------------------------------
# 整个Mod的一些绑定配置
#---------------------------------------------------------------------------------------
# 整个Mod的一些绑定配置
ModVersion = "1.0.0"
ModNameSpace = "neteaseCloud"
ServerSystemName = "neteaseCloudDev"
ClientSystemName = "neteaseCloudBeh"
MasterSystemName = "neteaseCloudMaster"
ServerSystemClsPath = "neteaseCloudScript.cloudServerSystem.CloudServerSystem"
ClientSystemClsPath = "neteaseCloudScript.cloudClientSystem.CloudClientSystem"
MasterSystemClsPath = "neteaseCloudScript.cloudMasterSystem.CloudMasterSystem"
#---------------------------------------------------------------------------------------
SyncRightHandSlotEvent = 'SyncRightHandSlotEvent'
SetUserInventoryEvent = 'SetUserInventoryEvent'
SetUserInventoryResultEvent = 'SetUserInventoryResultEvent'
LoginCloudServerEvent = 'LoginCloudServerEvent'
FinishSyncCloudItemEvent = 'FinishSyncCloudItemEvent' #完成云端玩家信息同步事件
#---------------------------------------------------------------------------------------
class CloudItemType(object):
    INVENTORY = 'inventory'  # 存在数据库json格式的key
    ARMOR = 'armor'  # 存在数据库json格式的key
    HANDS = 'hands'  # 存在数据库json格式的key
    EFFECT = 'effect'  # 存在数据库json格式的key
    EXTRA_DATA = 'extraData'  # 存在数据库json格式的key

class ProcessType(object):
    """
    信息处理方式包含三种
    0表示不做任何处理
    1表示不使用和同步云端玩家信息，且进入服务器时清空本地信息（可配置清空的信息类型），离开服务器时特定类型的物品通过邮件发送给玩家
    2表示使用云端玩家信息，可配置要使用的云端信息类型，进入服务器（包括登录和切换）时会同步云端信息到本地，而且信息变化时会同步到云端
    """
    NO_ACTION = 0
    FILTER_ACTION = 1
    CLOUD_ACTION = 2
