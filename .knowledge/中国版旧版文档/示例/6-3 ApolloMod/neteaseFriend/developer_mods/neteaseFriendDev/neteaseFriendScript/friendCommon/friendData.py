# -*- coding: utf-8 -*-
import time
class CFriendData(object):
	"""
	单个玩家的好友相关信息缓存
	包括了好友、黑名单、还有申请、RN好友、未读聊天标识等
	"""
	def __init__(self):
		self.mUid = 0
		self.mFriendUids = None
		self.mFriendRequests = None
		self.mBlackList = None
		self.mUnReadFriendList = None
		self.mRNFriendUids = set()
		self.mTempFriendUids = None
		self.UpdateTimestamp()

	def AddUnReadFriendList(self, uid):
		if self.mUnReadFriendList is None:
			self.mUnReadFriendList = []
		if uid not in self.mUnReadFriendList:
			self.mUnReadFriendList.append(uid)

	def DelUnReadFriendList(self, uid):
		if self.mUnReadFriendList is not None and uid in self.mUnReadFriendList:
			self.mUnReadFriendList.remove(uid)

	def GetUnReadFriendList(self):
		return self.mUnReadFriendList

	def SetUnReadFriend(self, uids):
		self.mUnReadFriendList = uids

	def AddRNFriend(self, uid):
		self.mRNFriendUids.add(uid)
	
	def AddTempFriend(self, uid):
		self.UpdateTimestamp()
		if self.mTempFriendUids is None:
			self.mTempFriendUids = []
		if uid in self.mTempFriendUids:
			return
		self.mTempFriendUids.append(uid)
		
	def SetTempFriend(self, tempFriends):
		self.UpdateTimestamp()
		self.mTempFriendUids = tempFriends
	
	def DelTempFriend(self, uid):
		self.UpdateTimestamp()
		if self.mTempFriendUids is not None and uid in self.mTempFriendUids:
			self.mTempFriendUids.remove(uid)
	
	def GetTempFriends(self):
		return self.mTempFriendUids
		
	def DelRNFriend(self, uid):
		if uid in self.mRNFriendUids:
			self.mRNFriendUids.remove(uid)
	
	def SetRNFriend(self, RNfriendUids):
		self.UpdateTimestamp()
		self.mRNFriendUids = RNfriendUids
			
	def ClearRNFriend(self):
		self.mRNFriendUids.clear()
		
	def GetRNFriend(self):
		return self.mRNFriendUids
	
	def GetUid(self):
		return self.mUid
	
	def SetUid(self, uid):
		self.mUid = uid
	
	def GetFriends(self):
		return self.mFriendUids
	
	def AddFriend(self, uid):
		self.UpdateTimestamp()
		if self.mFriendUids is None:
			self.mFriendUids = []
		if uid in self.mFriendUids:
			return
		self.mFriendUids.append(uid)
		
		
	def SetFriends(self, friendUids):
		'''
		用于lobby/game直接设置friends
		'''
		self.UpdateTimestamp()
		self.mFriendUids = friendUids
	
	def DelFriend(self, uid):
		self.UpdateTimestamp()
		if self.mFriendUids and uid in self.mFriendUids:
			self.mFriendUids.remove(uid)
	
	def GetFriendRequests(self):
		return self.mFriendRequests
	
	def AddFriendRequest(self, request):
		self.UpdateTimestamp()
		if self.mFriendRequests is None:
			self.mFriendRequests = {}
		self.mFriendRequests[request["auid"]] = request
		
	def SetRequest(self, requestDict):
		self.UpdateTimestamp()
		if self.mFriendRequests is None:
			self.mFriendRequests = {}
		self.mFriendRequests = requestDict
	
	def DelFriendRequest(self, uid):
		self.UpdateTimestamp()
		if self.mFriendRequests and uid in self.mFriendRequests:
			del self.mFriendRequests[uid]
	
	def GetBlackList(self):
		return self.mBlackList
	
	def AddblackList(self, uid):
		self.UpdateTimestamp()
		if self.mBlackList is None:
			self.mBlackList = []
		if uid not in self.mBlackList:
			self.mBlackList.append(uid)
			
	def SetBlackList(self, blackUids):
		'''
		用于lobby/game直接设置friends
		'''
		self.UpdateTimestamp()
		self.mBlackList = blackUids
	
	def DelBlackList(self, uid):
		self.UpdateTimestamp()
		if self.mBlackList and uid in self.mBlackList:
			self.mBlackList.remove(uid)
			
	def UpdateTimestamp(self):
		self.mTimeStamp = time.time()
		
	def GetLastUpdateTimestamp(self):
		return self.mTimeStamp
		
	