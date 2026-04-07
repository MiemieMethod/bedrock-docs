# -*- coding:utf-8 -*-

# =========================================================================================
baseGetUrl = "/get-mc-item-order-list"
baseShipUrl = "/ship-mc-item-order"
testGasUrl = "http://gasproxy.mc.netease.com:60001"
obtGasUrl = "http://gasproxy.mc.netease.com:60002"
# =========================================================================================
# 整个Mod的一些绑定配置
ModVersion = "1.0.0"
ModNameSpace = "neteaseShop"
ClientSystemName = "neteaseShopBeh"
ClientSystemClsPath = "neteaseShopScript.neteaseShopClientSystem.ShopClientSystem"
ServerSystemName = "neteaseShopDev"
ServerSystemClsPath = "neteaseShopScript.neteaseShopServerSystem.ShopServerSystem"
MasterSystemName = "neteaseShopMaster"
MasterSystemClsPath = "neteaseShopScript.neteaseShopMasterSystem.ShopMasterSystem"
# ===========================================================================================
import server.extraServerApi as serverApi
_masterModSystem = None
def GetMasterModSystem():
	"""
	获取服务端系统，全局一个单例。
	:return:
	:rtype: RPGBattleScripts.modServer.serverSystem.rpgBattleServerSystem.RPGBattleServerSystem
	"""
	global _masterModSystem
	if not _masterModSystem:
		_masterModSystem = serverApi.GetSystem(ModNameSpace, MasterSystemName)
	return _masterModSystem

def Destroy():
	global _masterModSystem
	_masterModSystem = None