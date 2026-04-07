# -*- coding: utf-8 -*-
import weakref

import server.extraServerApi as serverApi
import timer
import netgame.apolloCommon.commonNetgameApi as commonNetgameApi

def strCamp(str, maxLength):
	if len(str) <= maxLength:
		return str
	else:
		return str[0:maxLength]
		
class NpcData(object):
	'''
	记录npc的数据
	'''
	def __init__(self, identifier, name, pos, orientations, isTalk, talkContent, transferServerArgs, dimensionId):
		super(NpcData, self).__init__()
		self.mIdentifier = identifier
		self.mEntityId = None #实体Id
		self.mPos = tuple(pos) #坐标
		self.mInited = False #是否初始化
		self.mName = name #名字
		self.mOrientations = tuple(orientations) #朝向
		self.mIsTalk = isTalk #是否显示对话框
		self.mTalkContent = talkContent #对话框内容
		self.mTransferServerArgs = transferServerArgs #转服参数
		self.mDimensionId = dimensionId #维度
		#
		self.mKnockStyle = "transfer"
		self.mDefinedCallback = None
		self.mDefinedModName = ""
		self.mDefinedSystemName = ""
		self.mDefinedFuncName = ""
		self.mDefinedFuncArgs = []
	
	def InitSuccess(self, id):
		'''
		npc初始化成功
		'''
		self.mEntityId = id
		self.mInited = True
	
	def SetTouchedCallback(self, func):
		self.mKnockStyle = "onlyFunc"
		self.mDefinedCallback = func
	
	def SetSystemCallback(self, modName, systemName, funcName, funcArgs):
		self.mKnockStyle = "systemFunc"
		self.mDefinedModName = modName
		self.mDefinedSystemName = systemName
		self.mDefinedFuncName = funcName
		self.mDefinedFuncArgs = funcArgs

class NpcManager(object):
	'''
	管理所有npc
	'''
	def __init__(self, server):
		super(NpcManager, self).__init__()
		self.mServer = weakref.proxy(server)
		self.mWaitingNpc = []  # 需要注册的npc列表
		self.mActiveNpcDict = {}  # entity id => NpcData
		
		modConfig = commonNetgameApi.GetModJsonConfig('neteaseNpcScript')
		NPCS_TYPE = modConfig["NPCS_TYPE"]
		NPCS_DISTRIBUTE = modConfig["NPCS_DISTRIBUTE"]
		
		for NPC in NPCS_DISTRIBUTE:
			if NPC["server"] == commonNetgameApi.GetServerType():
				typeId = NPC.get("typeId", "")
				pos = NPC.get("pos", (0,0,0))
				orientations = NPC.get("orientations", (0,180))
				dimensionId = NPC.get("dimensionId", 0)
				if NPCS_TYPE.has_key(typeId):
					identifier = NPCS_TYPE[typeId].get("identifier", "minecraft:npc")
					name = strCamp(NPCS_TYPE[typeId].get("name", "steve").encode('utf-8'),45)
					isTalk = NPCS_TYPE[typeId].get("isTalk", True)
					talkContent = strCamp(NPCS_TYPE[typeId].get("talkContent", "").encode('utf-8'), 210)
					if not talkContent:
						talkContent = "是否前往？"
					transferServerArgs = NPCS_TYPE[typeId].get("transferServerArgs", "lobby").encode('utf-8')
					simpleStyle = NPCS_TYPE[typeId].get("simpleStyle", True)
					if not simpleStyle:
						modName = NPCS_TYPE[typeId].get("modName", "")
						systemName = NPCS_TYPE[typeId].get("systemName", "")
						funcName = NPCS_TYPE[typeId].get("funcName", "")
						funcArgs = NPCS_TYPE[typeId].get("funcArgs", [])
				else:
					identifier = "minecraft:npc"
					name = "steve"
					isTalk = True
					talkContent = "是否前往？"
					transferServerArgs = ""
					simpleStyle = True
				npcData = NpcData(identifier, name, pos, orientations, isTalk, talkContent, transferServerArgs, dimensionId)
				if not simpleStyle:
					npcData.SetSystemCallback(modName, systemName, funcName, funcArgs)
				self.mWaitingNpc.append(npcData)
		comp = self.mServer.CreateComponent(serverApi.GetLevelId(), "Minecraft", "game")
		self.mRegisterNpcTimer = comp.AddRepeatedTimer(5.0, self.TryCreateNpcs)
		print "mWaitingNpc = {}".format(len(self.mWaitingNpc))

	def RegisterExtraNpc(self, identifier, name, dimensionId, pos, rot, callbackFunc):
		npcData = NpcData(identifier, name, pos, rot, False, "", "", dimensionId)
		npcData.SetTouchedCallback(callbackFunc)
		self.mWaitingNpc.append(npcData)
	
	def TryCreateNpcs(self):
		'''
		尝试创建npc
		'''
		if not self.mWaitingNpc:
			return
		npcNum = len(self.mWaitingNpc)
		for id in xrange(npcNum):
			if self._CreateSingleNpc(id):
				npcData = self.mWaitingNpc[id]
				self.mActiveNpcDict[npcData.mEntityId] = npcData
				self.mWaitingNpc[id] = None
		self.mWaitingNpc = [one for one in self.mWaitingNpc if one]
	
	def _CreateSingleNpc(self, id):
		'''
		创建一个npc
		'''
		npcData = self.mWaitingNpc[id]
		# 检查引擎是否已经加载了chunk。只有先加载chunk，然后才创建npc。
		#exist = serverlevel.check_chunk_state((npcData.mPos[0], npcData.mPos[1], npcData.mPos[2]))
		dimensionComp = self.mServer.CreateComponent(serverApi.GetLevelId(), "Minecraft", "dimension")
		suc = dimensionComp.CreateDimension(npcData.mDimensionId)
		if suc == False:
			return False
		chunkComp = self.mServer.CreateComponent(serverApi.GetLevelId(), "Minecraft", "chunkSource")
		exist = chunkComp.CheckChunkState(npcData.mDimensionId, (npcData.mPos[0], npcData.mPos[1], npcData.mPos[2]))
		if (not exist) or (int(exist) == -1):
			return False
		# 创建npc，并设置属性。
		entityId = self.mServer.CreateEngineEntityByTypeStr(npcData.mIdentifier, npcData.mPos, npcData.mOrientations, npcData.mDimensionId, True)
		# 检查npc是否成功创建。
		if (not entityId) or (int(entityId) == -1):
			return False
		npcData.InitSuccess(entityId)
		nameComp = self.mServer.CreateComponent(entityId, 'Minecraft', 'name')
		print npcData.mName
		setnamesuccess = nameComp.SetName(npcData.mName)
		print 'setnamesuccess',setnamesuccess
		print 'create npc success.entity id:', entityId
		return True
	
	def Destroy(self):
		'''
		清理工作。包括停止定时器。
		'''
		if self.mRegisterNpcTimer:
			comp = serverApi.CreateComponent(serverApi.GetLevelId(), "Minecraft", "game")
			comp.CancelTimer(self.mRegisterNpcTimer)
			self.mRegisterNpcTimer = None
	
	def GetNpcData(self, entity_id):
		return self.mActiveNpcDict.get(entity_id, None)


