# -*- coding: utf-8 -*-

# --------------------------------------------------------------------------------------------------------
# 命名空间
ModVersion = "1.0.0"
ModName = "neteaseAddup"
ClientSystemName = "neteaseAddupBeh"
ClientSystemClsPath = "neteaseAddupScript.addupClientSystem.AddupClientSystem"
ServerSystemName = "neteaseAddupDev"
ServerSystemClsPath = "neteaseAddupScript.addupServerSystem.AddupServerSystem"
MasterSystemName = "neteaseAddupMaster"
MasterSystemClsPath = "neteaseAddupScript.addupMasterSystem.AddupMasterSystem"
# --------------------------------------------------------------------------------------------------------
# 可配置参数
# 
ActivityExpireTime = 3600 * 24 * 30
AllActivityData = {}
Item2ProcessMap = {}
# --------------------------------------------------------------------------------------------------------
# 事件配置
class ClientEvent(object):
    ClientEnter = "ClientEnter"
    GetAddupBonus = "GetAddupBonus"
    OpenNeteaseShop = "OpenNeteaseShop"

class ServerEvent(object):
    ServerReady = "ServerReady"
    SyncAddupInfo = "SyncAddupInfo"
    UpdateActiveAddup = "UpdateActiveAddup"
    GetAddupBonusRet = "GetAddupBonusRet"
    OpenBonusUI = "OpenBonusUI"
    HttpResponse = "HttpResponse"

class MasterRequest(object):
    GetAddupCharge = "/addup/get-pay"
    SetAddupCharge = "/addup/set-pay"
    SetAddupBonusState = "/addup/set-bonus-state"

class MasterEvent(object):
    GetAddupCharge = "GetAddupCharge"
    SetAddupCharge = "SetAddupCharge"
    SetAddupBonusState = "SetAddupBonusState"
