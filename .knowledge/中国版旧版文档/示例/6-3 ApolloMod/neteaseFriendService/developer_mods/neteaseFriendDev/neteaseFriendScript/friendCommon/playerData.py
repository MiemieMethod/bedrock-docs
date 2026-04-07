# -*- coding: utf-8 -*-
import time
class PlayerData(object):
	def __init__(self):
		self.mUid = 0
		self.mNickName = ""
		self.mHeadImage = ""
		#self.mOnline = False
		self.UpdateTimestamp()
		
	def GetPlayerData(self):
		self.UpdateTimestamp()
		dict = {}
		dict["uid"] = self.mUid
		dict["nickname"] = self.mNickName
		dict["head_image"] = self.mHeadImage
		#dict["online"] = self.mOnline
		return dict
	
	def GetPlayerUid(self):
		return self.mUid
	
	# def GetPlayerOnline(self):
	# 	self.UpdateTimestamp()
	# 	return self.mOnline
	
	def GetNickName(self):
		self.UpdateTimestamp()
		return self.mNickName
	
	def SetUid(self, uid):
		self.UpdateTimestamp()
		self.mUid = uid
		
	def SetPlayerData(self, uid, nickname, head_image = None):
		self.UpdateTimestamp()
		self.mUid = uid
		self.mNickName = nickname
		if head_image is not None:
			self.mHeadImage = head_image
		
	def SetNickName(self, nickname):
		self.UpdateTimestamp()
		self.mNickName = nickname
		
	def SetHeadImage(self, head_image):
		self.UpdateTimestamp()
		self.mHeadImage = head_image
		
	# def SetOnline(self, online):
	# 	self.UpdateTimestamp()
	# 	self.mOnline = online
	
	def UpdateTimestamp(self):
		self.mTimeStamp = time.time()
	
	def GetLastUpdateTimestamp(self):
		return self.mTimeStamp
		
	