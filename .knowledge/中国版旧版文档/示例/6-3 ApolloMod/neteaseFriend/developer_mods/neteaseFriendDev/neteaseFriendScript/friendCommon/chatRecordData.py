# -*- coding: utf-8 -*-
import time
class ChatData(object):
	"""
	单个玩家的聊天记录的内存缓存
	"""
	def __init__(self):
		self.mUid = 0
		self.mChatRecords = None
		self.mHasChatIndex = set()
		self.UpdateTimestamp()
		
	def SetUid(self, uid):
		self.mUid = uid
		
	def UpdateTimestamp(self):
		self.mTimeStamp = time.time()
		
	def GetLastUpdateTimestamp(self):
		return self.mTimeStamp
	
	def InsertChatRecord(self, friendUid, record):
		self.UpdateTimestamp()
		if self.mChatRecords is None:
			self.mChatRecords = {}
		records = self.mChatRecords.get(friendUid, None)
		chatIndex = record.get("chatIndex")
		if chatIndex in self.mHasChatIndex:
			return
		if not records:
			records = []
			self.mChatRecords[friendUid] = records
		self.mChatRecords[friendUid].append(record)
		self.mHasChatIndex.add(chatIndex)
	
	def PopChatRecord(self, friendUid):
		self.UpdateTimestamp()
		records = self.mChatRecords.get(friendUid, [])
		if len(records) == 0:
			return
		records.pop(0)
		
	def GetChatRecord(self, friendUid):
		if self.mChatRecords is None:
			return None
		return self.mChatRecords.get(friendUid, None)
	
	def SetChatRecord(self, friendUid, records):
		self.UpdateTimestamp()
		if self.mChatRecords is None:
			self.mChatRecords = {}
		self.mChatRecords[friendUid] = records
	
	def DelChatRecord(self, friendUid):
		self.UpdateTimestamp()
		if friendUid in self.mChatRecords:
			for sigleChat in self.mChatRecords[friendUid]:
				chatIndex = sigleChat.get("chatIndex")
				if chatIndex in self.mHasChatIndex:
					self.mHasChatIndex.remove(chatIndex)
			del self.mChatRecords[friendUid]