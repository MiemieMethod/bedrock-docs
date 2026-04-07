# -*- coding: utf-8 -*-

# 整个Mod的一些绑定配置
ModVersion = "1.0.2"
ModName = "neteaseJewel"
ClientSystemName = "neteaseJewelBeh"
ClientSystemClsPath = "neteaseJewelScript.jewelClientSystem.JewelClientSystem"
ServerSystemName = "neteaseJewelDev"
ServerSystemClsPath = "neteaseJewelScript.jewelServerSystem.JewelServerSystem"
ServiceSystemName = "neteaseJewelService"
ServiceSystemClsPath = "neteaseJewelScript.jewelServiceSystem.JewelServiceSystem"
MasterSystemName = "neteaseJewelMaster"
MasterSystemClsPath = "neteaseJewelScript.jewelMasterSystem.JewelMasterSystem"

# UI
jewelUIName = "jewelUI"
jewelUIClsPath = "neteaseJewelScript.netease_jewel_UI.JewelScreen"
jewelUIScreenDef = "netease_jewel_UI.main"

# 引擎事件
UiInitFinishedEvent = "UiInitFinished"
OnLocalPlayerStopLoading = "OnLocalPlayerStopLoading"

# 事件
DisplayJewelBoardEvent = 'DisplayJewelBoardEvent'
PlayerOfferArmEvent = 'PlayerOfferArmEvent'
PlayerClaimArmEvent = 'PlayerClaimArmEvent'
PlayerOfferGemEvent = 'PlayerOfferGemEvent'
PlayerClaimGemEvent = 'PlayerClaimGemEvent'
PlayerEnterEvent = 'PlayerEnterEvent'
SyncJewelConfigEvent = 'SyncJewelConfigEvent'
