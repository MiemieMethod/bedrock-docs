# -*- coding: utf-8 -*-

#---------------------------------------------------------------------------------------
# 整个Mod的一些绑定配置
ModVersion = "1.0.0"
ModNameSpace = "neteaseCloud"
ServerSystemName = "neteaseCloudDev"
ClientSystemName = "neteaseCloudBeh"
ServerSystemClsPath = "neteaseCloudScript.cloudServerSystem.CloudServerSystem"
ClientSystemClsPath = "neteaseCloudScript.cloudClientSystem.CloudClientSystem"
#---------------------------------------------------------------------------------------
SyncRightHandSlotEvent = 'SyncRightHandSlotEvent'
LoginCloudServerEvent = 'LoginCloudServerEvent'
#---------------------------------------------------------------------------------------
class CloudItemType(object):
    INVENTORY = 'inventory'
    ARMOR = 'armor'
    HANDS = 'hands'
    EFFECT = 'effect'

class ProcessType(object):
    NO_ACTION = 0
    FILTER_ACTION = 1
    CLOUD_ACTION = 2
