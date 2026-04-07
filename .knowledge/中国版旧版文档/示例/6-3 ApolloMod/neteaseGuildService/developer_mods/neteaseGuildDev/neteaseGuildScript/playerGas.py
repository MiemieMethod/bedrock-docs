# -*- coding:utf-8 -*-
from guildConsts import PlayerAttrType
import guildConsts as guildConsts
import logout
import time

class PlayerGas(object):
	'''
	玩家属性类
	'''
	def __init__(self, param):
		self.mFrame = 0
		#self.mLastSaveTime = 0
		#self.mIsDirty = False
		
		
		self.mAttrsToSync = {} #待同步至客户端的属性
		self.mAttrsDictCurrent = {} #玩家属性
		self.mNeedsUpdateAttrs = [] #需要被更新到客户端的属性
		self.mNeedsSaveAttrs = [] #需要保存的属性
		self.mAttrsToSave = {} #待保存的属性
		
		self.InitPlayer(param)
		
	def InitPlayer(self, param):
		'''
		初始化玩家
		'''
		#只有几个属性需要同步至客户端
		self.mNeedsUpdateAttrs.append(PlayerAttrType.Uid)
		self.mNeedsUpdateAttrs.append(PlayerAttrType.Name)
		self.mNeedsUpdateAttrs.append(PlayerAttrType.Activity)
		self.mNeedsUpdateAttrs.append(PlayerAttrType.Online)
		self.mNeedsUpdateAttrs.append(PlayerAttrType.GuildId)
		self.mNeedsUpdateAttrs.append(PlayerAttrType.Duty)
		self.mNeedsUpdateAttrs.append(PlayerAttrType.Level)
		self.mNeedsUpdateAttrs = list(set(self.mNeedsUpdateAttrs))
		#只有几个属性需要保存
		self.mNeedsSaveAttrs.append(PlayerAttrType.Uid)
		self.mNeedsSaveAttrs.append(PlayerAttrType.Name)
		self.mNeedsSaveAttrs.append(PlayerAttrType.Activity)
		self.mNeedsSaveAttrs.append(PlayerAttrType.GuildId)
		self.mNeedsSaveAttrs.append(PlayerAttrType.Duty)
		self.mNeedsSaveAttrs.append(PlayerAttrType.Level)
		self.mNeedsSaveAttrs.append(PlayerAttrType.LastLoginTime)
		self.mNeedsSaveAttrs = list(set(self.mNeedsSaveAttrs))
		# for attrType, attrValue in param.items():
		# 	self.SetAttrCurrent(attrType, attrValue)
		self.SetAttrCurrent(PlayerAttrType.Uid, param.get(PlayerAttrType.Uid))
		self.SetAttrCurrent(PlayerAttrType.Name, param.get(PlayerAttrType.Name))
		self.SetAttrCurrent(PlayerAttrType.Activity, param.get(PlayerAttrType.Activity))
		self.SetAttrCurrent(PlayerAttrType.GuildId, param.get(PlayerAttrType.GuildId))
		self.SetAttrCurrent(PlayerAttrType.Duty, param.get(PlayerAttrType.Duty))
		self.SetAttrCurrent(PlayerAttrType.Online, param.get(PlayerAttrType.Online))
		self.SetAttrCurrent(PlayerAttrType.ServerId, param.get(PlayerAttrType.ServerId))
		self.SetAttrCurrent(PlayerAttrType.Level, param.get(PlayerAttrType.Level))
		self.SetAttrCurrent(PlayerAttrType.LastLoginTime, param.get(PlayerAttrType.LastLoginTime))
		print "InitPlayer", self.mAttrsDictCurrent
		
	def SetAttrCurrent(self, attrType, attrValue, needToSave = False):
		'''
		设置属性
		'''
		oldValue = self.mAttrsDictCurrent.get(attrType, None)
		self.mAttrsDictCurrent[attrType] = attrValue
		if oldValue != attrValue and attrType in self.mNeedsUpdateAttrs:
			self.mAttrsToSync[attrType] = attrValue
		if oldValue != attrValue and attrType in self.mNeedsSaveAttrs and needToSave == True:
			self.mAttrsToSave[attrType] = attrValue
			
	def AddPlayerSync(self):
		for attrType, attrValue in self.mAttrsDictCurrent.items():
			if attrType in self.mNeedsUpdateAttrs:
				self.mAttrsToSync[attrType] = attrValue
	
	def GetAttr(self, attrType):
		return self.mAttrsDictCurrent.get(attrType, None)
	
	def GetAttrsSaveInGuild(self):
		'''
		获取需要存在公会的属性
		'''
		attrsSaveInGuildDict = self.mAttrsDictCurrent.copy()
		attrsSaveInGuildDict.pop(PlayerAttrType.Duty)
		attrsSaveInGuildDict.pop(PlayerAttrType.ServerId)
		return attrsSaveInGuildDict
	
	def SyncAttrsToClient(self, attrsToSync):
		'''
		同步至客户端
		'''
		serverId = self.GetAttr(PlayerAttrType.ServerId)
		uid = self.GetAttr(PlayerAttrType.Uid)
		if serverId != None and uid != None:
			attrsToSync[PlayerAttrType.Uid] = uid
			guildConsts.GetServiceModSystem().NotifyToServerNode(serverId, guildConsts.SyncPlayerAttrsFromServiceEvent, attrsToSync)
	
	def ResetAttrs(self):
		self.mAttrsToSync = {}
	
	def ResetAttrsToSave(self):
		self.mAttrsToSave = {}
	
	# def DoAutoSave(self):
	# 	'''
	# 	执行定时存档
	# 	'''
	# 	if self.IsNeedSave(int(time.time())) == False or self.GetAttr(PlayerAttrType.Online) == False:
	# 		return
	# 	self.DoSave()
		
	def DoSave(self):
		'''
		存档所有属性
		'''
		def SaveCb(args, mAttrsDictCurrent):
			if args is None:
				logout.error("save player[%s:%s] fail"%(mAttrsDictCurrent.get(PlayerAttrType.Uid), mAttrsDictCurrent.get(PlayerAttrType.Name)))
		callback = lambda args: SaveCb(args, self.mAttrsDictCurrent)
		guildConsts.GetServiceModSystem().GetMysqlMgr().SavePlayerByUid(self.mAttrsDictCurrent, callback)
	
	# def IsNeedSave(self, timestamp):
	# 	'''
	# 	判断是否需要定时存档
	# 	'''
	# 	if not self.mIsDirty:
	# 		return False
	# 	if timestamp - self.mLastSaveTime < self.AUTO_SAVE_TIME:
	# 		return False
	# 	return True
	
	# def OnSaveDone(self, timestamp):
	# 	'''
	# 	存档完成
	# 	'''
	# 	self.mFrame = 0
	# 	#self.mIsDirty = False
	# 	self.mLastSaveTime = timestamp
	
	# def SetDirty(self, dirty):
	# 	'''
	# 	设置是否开启定时存档
	# 	'''
	# 	self.mIsDirty = dirty
	
	def SaveAttrsToSave(self):
		'''
		存档已改变的属性
		'''
		def SaveCb(args, mAttrsDictCurrent):
			if args is None:
				logout.error("save player[%s:%s] fail"%(mAttrsDictCurrent.get(PlayerAttrType.Uid), mAttrsDictCurrent.get(PlayerAttrType.Name)))
		callback = lambda args: SaveCb(args, self.mAttrsDictCurrent)
		guildConsts.GetServiceModSystem().GetMysqlMgr().SavePlayerPartByUid(self.mAttrsToSave, callback)
	
	
	def Tick(self):
		self.mFrame += 1
		if self.mAttrsToSync:
			self.SyncAttrsToClient(self.mAttrsToSync)
			self.ResetAttrs()
		if self.mAttrsToSave:
			self.mAttrsToSave[PlayerAttrType.Uid] = self.GetAttr(PlayerAttrType.Uid)
			self.SaveAttrsToSave()
			self.ResetAttrsToSave()
		# if self.mFrame % self.CHECK_SAVE_FRAME == 0:
		# 	self.DoAutoSave()
			
		