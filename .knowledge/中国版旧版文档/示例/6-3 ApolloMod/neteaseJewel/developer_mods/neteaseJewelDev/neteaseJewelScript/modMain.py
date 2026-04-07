# -*- coding: utf-8 -*-

from common.mod import Mod
import server.extraServerApi as serverApi
from neteaseJewelScript.jewelConst import ModVersion, ModName, ServerSystemName, ServerSystemClsPath


@Mod.Binding(name=ModName, version=ModVersion)
class NeteaseJewelServer(object):
	"""
	整个插件有三个system，jewel处理宝石镶嵌逻辑，bag处理背包信息的同步，calc计算装备镶嵌后属性
	"""
	@Mod.InitServer()
	def JewelServerInit(self):
		print '==== neteaseJewel initServer ===='
		serverApi.RegisterSystem(ModName, ServerSystemName, ServerSystemClsPath)
		serverApi.RegisterSystem(ModName, 'bag', "neteaseJewelScript.bagServerSystem.BagServerSystem")
		serverApi.RegisterSystem(ModName, 'calc', "neteaseJewelScript.calcServerSystem.CalcServerSystem")

	@Mod.DestroyServer()
	def JewelServerDestroy(self):
		print '==== neteaseJewel destroyServer ===='
