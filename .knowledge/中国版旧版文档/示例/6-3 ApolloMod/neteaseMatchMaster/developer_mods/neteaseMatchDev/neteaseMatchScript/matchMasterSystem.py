# -*- coding: utf-8 -*-
import server.extraMasterApi as masterApi
MasterSystem = masterApi.GetMasterSystemCls()
import neteaseMatchScript.masterConsts as masterConsts

class MatchMasterSystem(MasterSystem):
	def __init__(self, namespace, systemName):
		MasterSystem.__init__(self, namespace, systemName)
		self.mMatchServerIdMap = {}
		self.mMatchedUIDMap = {}
		self.ListenForEvent(masterApi.GetEngineNamespace(), masterApi.GetEngineSystemName(),
				'NetGameCommonConfChangeEvent', self, self.OnNetGameCommonConfChange)
		self.ListenForEvent(masterApi.GetEngineNamespace(), masterApi.GetEngineSystemName(),
				'PlayerLogoutServerEvent', self, self.OnPlayerLogoutServer)
		self.ListenForEvent(masterApi.GetEngineNamespace(), masterApi.GetEngineSystemName(),
				'PlayerLoginServerEvent', self, self.OnPlayerLoginServer)

	def OnNetGameCommonConfChange(self, args):
		'''
		获取使用了本插件的所有lobby/game
		'''
		import master.masterConf as masterConf
		serverConfList = masterConf.netgameConf["serverlist"]
		self.mMatchServerIdMap = {}
		for conf in serverConfList:
			modsStr = conf["mods"]
			mods = [mod.strip() for mod in modsStr.split(',')]
			if masterConsts.ModName in mods:
				self.mMatchServerIdMap[conf["serverid"]] = True

	def OnPlayerLogoutServer(self, args):
		'''
		处理玩家登陆事件，清除匹配相关缓存
		'''
		if args['isTransfer']:
			return
		uid = args['uid']
		if uid not in self.mMatchedUIDMap:
			return
		del self.mMatchedUIDMap[uid]
		data = {'uid' : uid}
		self.RequestToService(masterConsts.ModName, masterConsts.MatchPlayerLogoutEvent, data)

	def OnPlayerLoginServer(self, args):
		serverId = args['serverId']
		if serverId not in self.mMatchServerIdMap:
			return
		uid = args['uid']
		self.mMatchedUIDMap[uid] = True



