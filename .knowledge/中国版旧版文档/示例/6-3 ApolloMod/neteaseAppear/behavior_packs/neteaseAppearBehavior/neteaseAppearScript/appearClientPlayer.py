# -*- coding: utf-8 -*-

import neteaseAppearScript.appearConst as appearConst

class PlayerAppear(object):
	def __init__(self, playerId):
		super(PlayerAppear, self).__init__()
		self.mPlayerId = playerId
		self.mUid = None
		#
		self.mUseAppear = None 
		self.mUnlockAppear = None
		self.mMountId = None
		self.mBodyModelConfig = None
		self.mMountModelConfig = None
		#
		self.mActiveAppear = {}
		self.mActiveAppearInstance = {}
	
	def OnServerReady(self, uid):
		self.mUid = uid

	def OnSyncAppearInfo(self, appearInfo):
		self.mUnlockAppear = appearInfo.get("unlockData", [])
		self.mUseAppear = appearInfo.get("useData", {})
	
	def OnUpdateUseAppear(self, useData, mountId):
		self.mUseAppear = useData
		self.mMountId = mountId

	def GetUseAppear(self, appearType):
		appearKey = self.mUseAppear.get(appearType, None)
		if not appearKey:
			return "empty"
		else:
			return appearKey
	
	def CheckAppearOpen(self, appearValue):
		if (not appearValue) or (appearValue == "empty"):
			return True
		return appearValue in self.mUnlockAppear

	def CleanActiveAppear(self, appearType):
		self.mActiveAppear[appearType] = None 
		self.mActiveAppearInstance[appearType] = []
		if appearType == appearConst.AppearType.Body:
			self.mBodyModelConfig = None 
		elif appearType == appearConst.AppearType.Mount:
			self.mMountModelConfig = None

	def CacheActiveBody(self, appearValue, modelConfig):
		self.CacheActiveAppear(appearConst.AppearType.Body, appearValue)
		self.mBodyModelConfig = modelConfig
	
	def CacheActiveMount(self, appearValue, modelConfig):
		self.CacheActiveAppear(appearConst.AppearType.Mount, appearValue)
		self.mMountModelConfig = modelConfig

	def GetAnimateName(self, isMount, action):
		if isMount:
			config = self.mMountModelConfig
		else:
			config = self.mBodyModelConfig
		return config.get(action, "idle")

	def CacheActiveAppear(self, appearType, appearValue):
		self.mActiveAppear[appearType] = appearValue
	
	def GetAppearInstance(self, appearType):
		return self.mActiveAppearInstance.get(appearType, [])
	
	def CacheAppearInstance(self, appearType, effectId):
		if appearType not in self.mActiveAppearInstance:
			self.mActiveAppearInstance[appearType] = []
		self.mActiveAppearInstance[appearType].append(effectId)
	
	def CheckDirtyAppear(self, appearType):
		use = self.mUseAppear.get(appearType, None)
		active = self.mActiveAppear.get(appearType, None)
		if use == active:
			return False, active, use
		else:
			return True, active, use
	
	