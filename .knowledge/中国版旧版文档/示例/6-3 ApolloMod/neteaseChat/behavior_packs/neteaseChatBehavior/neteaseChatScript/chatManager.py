# -*- coding:utf-8 -*-
import chatConsts as chatConsts
import logout
import client.extraClientApi as clientApi
import neteaseChatScript.ui.uiDef as uiDef

class ChatManager(object):
	def __init__(self, system, channel):
		import weakref
		self.system = weakref.proxy(system)
		self.mChatChannel = channel
		self.mScreenUids = []
		self.mUnReadChatRecords = []
		self.mAllChatRecords = []
		self.mDirty = False
		#self.mRepeatedTellClientNewChatTimer = timer.TimerManager.addRepeatTimer(1.5, self.RepeatedTellClientNewChat)
		self.mTimerComp = clientApi.CreateComponent(clientApi.GetLevelId(), "Minecraft", "game")
		self.mTimerComp.AddRepeatedTimer(1, self.RepeatedTellClientNewChat)
		
	def RepeatedTellClientNewChat(self):
		if self.mDirty == True:
			self.system.BroadcastEvent('LocalNewChatRecord', {"chatChannel":self.mChatChannel})
			self.mDirty = False
		
	def SetScreenUids(self, screenUids):
		self.mScreenUids = screenUids
		
	def InsertChatMes(self, chatDict):
		print "ClientInsertChatMes", chatDict
		playerUid = chatDict["playerUid"]
		# if self.mChatRecords.has_key(playerUid) == False:
		# 	self.mChatRecords[playerUid] = []
		self.mUnReadChatRecords.append(chatDict)
		if len(self.mUnReadChatRecords) > chatConsts.MAX_CHAT_LEN:
			self.mUnReadChatRecords.pop(0)
		self.mAllChatRecords.append(chatDict)
		if len(self.mAllChatRecords) > chatConsts.MAX_CHAT_LEN:
			self.mAllChatRecords.pop(0)
		self.mDirty = True
		#self.system.BroadcastEvent('LocalNewChatRecord', {"chatChannel":self.mChatChannel})
		#TODO 显示
	
	def GetUnReadChatRecords(self):
		unReadChatRecords = self.mUnReadChatRecords
		self.mUnReadChatRecords = []
		return unReadChatRecords
	
	def GetAllChatRecords(self):
		return self.mAllChatRecords