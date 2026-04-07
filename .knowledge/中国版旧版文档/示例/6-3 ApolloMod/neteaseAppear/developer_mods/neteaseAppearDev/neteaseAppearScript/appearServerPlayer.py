# -*- coding: utf-8 -*-

import neteaseAppearScript.appearConst as appearConst

class PlayerAppear(object):
	def __init__(self, playerId, uid):
		super(PlayerAppear, self).__init__()
		self.mPlayerId = playerId
		self.mUid = uid
		self.mDirty = False
		self.mDbLoaded = False
		self.mClientReady = False
		self.mNeedInsert = False
		#
		self.mAppearInfo = None
		self.mMountId = None
		#
		self.mMoneyData = None

	def IsDirty(self):
		return self.mDirty
	
	def DataReady(self):
		return self.mDbLoaded
	
	def NeedInsert(self):
		return self.mNeedInsert

	def GetSaveData(self):
		return self.mPlayerId, self.mUid, self.mAppearInfo
	
	def GetUseAppearData(self):
		return {
			"mountId": self.mMountId,
			"useData": self.mAppearInfo["useData"],
			"playerId": self.mPlayerId,
		}
	#-----------------------------------------------------------------------------------------------------------------------------------------
	def CacheMoneyData(self, moneyData):
		self.mMoneyData = moneyData
	
	def ChangeMoneydata(self, moneyType, moneyValue):
		if self.mMoneyData is None:
			return
		if self.mMoneyData.has_key(moneyType):
			self.mMoneyData[moneyType] += moneyValue
		else:
			self.mMoneyData[moneyType] = moneyValue
	
	def CheckMoneyEnough(self, moneyType, moneyValue):
		if self.mMoneyData is None:
			return False
		hasMoney = self.mMoneyData.get(moneyType, 0)
		return hasMoney >= moneyValue

	def SetSaved(self):
		self.mDirty = False
	
	def SetDirty(self):
		self.mDirty = True
	
	def SetNotNeedInsert(self):
		self.mNeedInsert = False
	
	def SetClientReady(self):
		self.mClientReady = True
	#-----------------------------------------------------------------------------------------------------------------------------------------
	def OnQueryCallback(self, appearInfo):
		self.mDirty = False
		self.mDbLoaded = True
		self.mNeedInsert = False
		self.mAppearInfo = appearInfo
	
	def OnCreateByNew(self):
		self.mDirty = True
		self.mDbLoaded = True
		self.mNeedInsert = True
		self.mAppearInfo = {
			"unlockData": appearConst.FreeAppears,
			"useData": {
				appearConst.AppearType.Body: appearConst.DefaultBody,
			},
		}
	
	def OnBuyAppearSuccess(self, appearKey):
		self.mDirty = True
		if appearKey not in self.mAppearInfo["unlockData"]:
			self.mAppearInfo["unlockData"].append(appearKey)
	#-----------------------------------------------------------------------------------------------------------------------------------------
	def GetUseBody(self):
		return self.mAppearInfo["useData"].get(appearConst.AppearType.Body, None)

	def GetUseMount(self):
		return self.mAppearInfo["useData"].get(appearConst.AppearType.Mount, None)

	def SetUseMount(self, appearKey):
		self.mAppearInfo["useData"][appearConst.AppearType.Mount] = appearKey
		self.mDirty = True

	def SaveMountId(self, entityId):
		self.mMountId = entityId
	
	def StopRideing(self):
		self.mMountId = None 
		self.SetUseMount(None)

	def AppearUnlocked(self, appearKey):
		if not appearKey:
			return True
		if not self.mAppearInfo:
			return False
		if not appearKey:
			return True
		return appearKey in self.mAppearInfo["unlockData"]
	
	def AppearAlreadyUsed(self, appearType, appearKey):
		old = self.mAppearInfo["useData"].get(appearType, None)
		if old == appearKey:
			return True
		return False
	
	def DoChangeUseAppear(self, appearType, appearKey):
		if not appearKey:
			appearKey = None
		if appearType == appearConst.AppearType.Mount:
			self.SetUseMount(appearKey)
		else:
			self.mAppearInfo["useData"][appearType] = appearKey
		self.mDirty = True

