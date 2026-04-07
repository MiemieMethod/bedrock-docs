# -*- coding: utf-8 -*-
#
import server.extraServerApi as serverApi
ServerSystem = serverApi.GetServerSystemCls()
import npcManager
import lobbyGame.netgameApi as netgameApi

#-----------------------------------------------------------------------------------
class NpcServerSystem(ServerSystem):
	def __init__(self, namespace, systemName):
		ServerSystem.__init__(self, namespace, systemName)
		print '--------NpcServer====start!!!!!~~~~~'
		self.mNpcMgr = npcManager.NpcManager(self)
		self.ListenForEvent(serverApi.GetEngineNamespace(), serverApi.GetEngineSystemName(), "EntityBeKnockEvent", self, self.OnNpcTouched)
		self.ListenForEvent(serverApi.GetEngineNamespace(), serverApi.GetEngineSystemName(), "PlayerDieEvent", self, self.OnPlayerDie)
		self.ListenForEvent("neteaseNpc", "npcClient", "ClickSureFromClientEvent", self, self.OnClickSureGame)
		
	def OnPlayerDie(self, args):
		'''
		玩家死亡，对话框消失
		'''
		playerId = args['id']
		data = {"playerId" : playerId}
		self.NotifyToClient(playerId, "PlayerDieFromServerEvent", data)

	def OnNpcBeKnocked(self, entityId, playerId, gameType):
		print "OnNpcBeKnocked entityId={} playerId={} gameType={}".format(entityId, playerId, gameType)

	def RegisterExtraNpc(self, identifier, name, dimensionId, pos, rot, callbackFunc):
		self.mNpcMgr.RegisterExtraNpc(identifier, name, dimensionId, pos, rot, callbackFunc)
	
	def DeleteExtraNpc(self, entityId):
		npcData = self.mNpcMgr.GetNpcData(entityId)
		if not npcData:
			return
		self.DestroyEntity(entityId)
		
	def OnNpcTouched(self, args):
		'''
		点击npc回调函数。
		'''
		npcEntityId = args.get('entityId')
		npcData = self.mNpcMgr.GetNpcData(npcEntityId)
		playerId = args.get('srcId')
		if not npcData:
			return
		# 使用API注册的NPC
		if npcData.mKnockStyle == "onlyFunc":
			npcData.mDefinedCallback(npcData.mEntityId, playerId)
			return
		# 配置了回调指定mod的函数的NPC
		if npcData.mKnockStyle == "systemFunc":
			tarSystem = serverApi.GetSystem(npcData.mDefinedModName, npcData.mDefinedSystemName)
			if not tarSystem:
				return
			tarFunc = getattr(tarSystem, npcData.mDefinedFuncName, None)
			if not tarFunc or not callable(tarFunc):
				return
			args = [npcData.mEntityId, playerId]
			if npcData.mDefinedFuncArgs:
				args.extend(npcData.mDefinedFuncArgs)
			apply(tarFunc, args)
			return
		# 默认的实现转服逻辑的NPC
		if npcData.mIsTalk == True:
			data = {'aimServer': npcData.mTransferServerArgs,'playerId': playerId,'talkContent': npcData.mTalkContent,"npcName": npcData.mName}
			self.NotifyToClient(playerId, "CheckSureFromServerEvent", data)
		else:
			netgameApi.TransferToOtherServer(playerId, npcData.mTransferServerArgs)
	
	def OnClickSureGame(self, args):
		'''
		客户端点击确定，切服
		'''
		server = args["aimServer"]
		netgameApi.TransferToOtherServer(args['playerId'], server)

	def Destroy(self):
		self.UnListenForEvent(serverApi.GetEngineNamespace(), serverApi.GetEngineSystemName(), "EntityBeKnockEvent", self, self.OnNpcTouched)
		self.UnListenForEvent(serverApi.GetEngineNamespace(), serverApi.GetEngineSystemName(), "PlayerDieEvent", self, self.OnPlayerDie)
		self.UnListenForEvent("neteaseNpc", "npcClient", "ClickSureFromClientEvent", self, self.OnClickSureGame)
