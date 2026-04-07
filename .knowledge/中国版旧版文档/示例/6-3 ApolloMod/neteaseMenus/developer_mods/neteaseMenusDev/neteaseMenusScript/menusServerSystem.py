# -*- coding: utf-8 -*-

import lobbyGame.netgameApi as netgameApi
import apolloCommon.commonNetgameApi as commonNetgameApi
import neteaseMenusScript.menusConst as menusConst
import server.extraServerApi as serverApi
from mod_log import engine_logger as logger

ServerSystem = serverApi.GetServerSystemCls()

def CleanDictOrList(_dictOrList, exKey):
	if type(_dictOrList) == list:
		for v in _dictOrList:
			if type(v) == list or type(v) == dict:
				CleanDictOrList(v, exKey)
	elif type(_dictOrList) == dict:
		if exKey in _dictOrList:
			del _dictOrList[exKey]
		for v in _dictOrList.values():
			if type(v) == dict or type(v) == list:
				CleanDictOrList(v, exKey)

class MenusServerSystem(ServerSystem):
	"""
	该mod的服务端类
	将mod.json的配置推到客户端用以显示主菜单栏
	"""

	def __init__(self, namespace, systemName):
		ServerSystem.__init__(self, namespace, systemName)

		# 加载配置信息
		self.ReloadConfig()

		# 注册事件
		self.ListenForEvent(menusConst.ModName, menusConst.ClientSystemName, menusConst.DisplayMenusEvent, self, self.OnDisplayMenus)

	def Destroy(self):
		self.UnListenForEvent(menusConst.ModName, menusConst.ClientSystemName, menusConst.DisplayMenusEvent, self, self.OnDisplayMenus)

	def ReloadConfig(self):
		# 读取mod.json配置文件
		cfg = commonNetgameApi.GetModJsonConfig("neteaseMenusScript")
		if not cfg:
			logger.error("==== neteaseMenus ReloadConfig: read config failed")
			return False

		menusConst.ConfigParams.update(cfg["configParams"])
		CleanDictOrList(menusConst.ConfigParams, "_comment")
		logger.info("==== neteaseMenus ReloadConfig: finished, new config: {}".format(menusConst.ConfigParams))

	def OnDisplayMenus(self, args):
		logger.info("==== neteaseMenus OnDisplayMenus: {}".format(args))
		playerId = args["id"]
		uid = netgameApi.GetPlayerUid(playerId)
		if not uid:
			logger.error("==== neteaseMenus OnDisplayMenus: uid not found, playerId={}".format(playerId))
			return
		# 这里可以针对具体用户情况下发不同的配置，要小心不要改到公共配置
		data = menusConst.ConfigParams
		self.NotifyToClient(playerId, menusConst.DisplayMenusEvent, data)
