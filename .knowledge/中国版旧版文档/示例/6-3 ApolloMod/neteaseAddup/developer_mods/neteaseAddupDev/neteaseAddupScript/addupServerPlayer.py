# -*- coding: utf-8 -*-

import neteaseAddupScript.addupConsts as addupConsts

class Player(object):
	def __init__(self, playerId, uid):
		super(Player, self).__init__()
		self.mPlayerId = playerId
		self.mUid = uid
		self.mDirty = False
		self.mDbLoaded = False
		self.mClientReady = False
		self.mNeedInsert = False
		#
		self.mAddupInfo = None

	def IsDirty(self):
		return self.mDirty
	
	def DataReady(self):
		return self.mDbLoaded
	
	def NeedInsert(self):
		return self.mNeedInsert

	def GetSaveData(self):
		return self.mPlayerId, self.mUid, self.mAddupInfo
	#-----------------------------------------------------------------------------------------------------------------------------------------
	def SetSaved(self):
		self.mDirty = False
	
	def SetDirty(self):
		self.mDirty = True
	
	def SetNotNeedInsert(self):
		self.mNeedInsert = False
	
	def SetClientReady(self):
		self.mClientReady = True
	#-----------------------------------------------------------------------------------------------------------------------------------------
	def OnQueryCallback(self, addupInfo):
		self.mDirty = False
		self.mDbLoaded = True
		self.mNeedInsert = False
		self.mAddupInfo = addupInfo
	
	def OnCreateByNew(self):
		self.mDirty = True
		self.mDbLoaded = True
		self.mNeedInsert = True
		self.mAddupInfo = {}
	#-----------------------------------------------------------------------------------------------------------------------------------------
	def GetAddupInfoByKey(self, actKey):
		return self.mAddupInfo.get(actKey, {})
	
	def IsReachProcess(self, addupInfo, targetProcess):
		process = addupInfo.get("process", 0)
		return process >= targetProcess
	
	def IsAlreadyGetBonus(self, addupInfo, bonusKey):
		bonusList = addupInfo.get("bonusList", [])
		return bonusKey in bonusList

	def SetAlreadyGetBonus(self, addupInfo, bonusKey):
		if not addupInfo.has_key("bonusList"):
			addupInfo["bonusList"] = []
		if not bonusKey in addupInfo["bonusList"]:
			addupInfo["bonusList"].append(bonusKey)

	def SaveAddupInfoByKey(self, actKey, addupInfo):
		self.mAddupInfo[actKey] = addupInfo
		self.mDirty = True
	
	def CleanAddupInfoByKey(self, actKey):
		if self.mAddupInfo.has_key(actKey):
			del self.mAddupInfo[actKey]
			self.mDirty = True

	def IsAlreadyNotes(self, addupInfo, orderId):
		notes = addupInfo.get("notes", [])
		return orderId in notes
	
	def SetAlreadyNotes(self, addupInfo, orderId, plusProcess):
		if not addupInfo.has_key("notes"):
			addupInfo["notes"] = []
		if not addupInfo.has_key("process"):
			addupInfo["process"] = 0
		if not orderId in addupInfo["notes"]:
			addupInfo["notes"].append(orderId)
		addupInfo["process"] += plusProcess
	
	def ChangeAddupProcess(self, addupInfo, targetProcess):
		addupInfo["process"] = targetProcess
	
	def ChangeAddupBonusState(self, addupInfo, bonusKey, alreadyGet):
		if not addupInfo.has_key("bonusList"):
			addupInfo["bonusList"] = []
		if alreadyGet:
			if bonusKey not in addupInfo["bonusList"]:
				addupInfo["bonusList"].append(bonusKey)
		else:
			if bonusKey in addupInfo["bonusList"]:
				addupInfo["bonusList"].remove(bonusKey)

	def UpdateByOrders(self, activeKey, actConfig, orderList):
		changed = False
		addupInfo = self.GetAddupInfoByKey(activeKey)
		startTp, endTp = actConfig["startTp"], actConfig["endTp"]
		#
		for order in orderList:
			plusProcess = addupConsts.Item2ProcessMap.get(order["item_id"], 0)
			if plusProcess <= 0:
				continue
			if self.IsAlreadyNotes(addupInfo, order["orderid"]):
				continue
			buy_time = int(order.get("buy_time", 0))
			if buy_time < startTp or buy_time >= endTp:
				continue
			changed = True
			self.SetAlreadyNotes(addupInfo, order["orderid"], plusProcess*order["item_num"])
		if changed:
			self.SaveAddupInfoByKey(activeKey, addupInfo)
		return changed
	#-----------------------------------------------------------------------------------------------------------------------------------------

