# -*- coding:utf-8 -*-
import Queue
from guildConsts import GuildAttrType
from guildConsts import PlayerAttrType
from guildConsts import DutyType
import guildConsts as guildConsts
import time
import logout

class GuildGas(object):
	'''
	单个公会的信息
	'''
	def __init__(self, param):
		self.mFrame = 0
		# self.mLastSaveTime = 0
		# self.mIsDirty = False
		
		self.mAttrsToSync = {}  # 待同步至客户端的属性
		self.mAttrsDictCurrent = {}  # 公会属性
		self.mNeedsUpdateAttrs = []  # 需要被更新到客户端的属性
		self.mNeedsSaveAttrs = [] #需要保存的属性
		self.mAttrsToSave = {}  #待保存的属性
		
		#self.ApplicationQueue = Queue.Queue()
		self.InitGuild(param)
		
	def InitGuild(self, param):
		self.mNeedsUpdateAttrs.append(GuildAttrType.GuildId)
		self.mNeedsUpdateAttrs.append(GuildAttrType.Name)
		self.mNeedsUpdateAttrs.append(GuildAttrType.Activity)
		self.mNeedsUpdateAttrs.append(GuildAttrType.ApplicationQueue)
		self.mNeedsUpdateAttrs.append(GuildAttrType.PresidentPlayerDict)
		self.mNeedsUpdateAttrs.append(GuildAttrType.ElderPlayerDict)
		self.mNeedsUpdateAttrs.append(GuildAttrType.CommonPlayerDict)
		self.mNeedsUpdateAttrs.append(GuildAttrType.MaxNum)
		self.mNeedsUpdateAttrs.append(GuildAttrType.MapId)
		self.mNeedsUpdateAttrs = list(set(self.mNeedsUpdateAttrs))
		
		# 只有几个属性需要保存
		self.mNeedsSaveAttrs.append(GuildAttrType.GuildId)
		self.mNeedsSaveAttrs.append(GuildAttrType.Name)
		self.mNeedsSaveAttrs.append(GuildAttrType.Activity)
		self.mNeedsSaveAttrs.append(GuildAttrType.MaxNum)
		self.mNeedsSaveAttrs.append(GuildAttrType.UnActivityDay)
		self.mNeedsSaveAttrs.append(GuildAttrType.MapId)
		self.mNeedsSaveAttrs = list(set(self.mNeedsSaveAttrs))
		
		self.SetAttrCurrent(GuildAttrType.GuildId, param.get(GuildAttrType.GuildId))
		self.SetAttrCurrent(GuildAttrType.Name, param.get(GuildAttrType.Name))
		self.SetAttrCurrent(GuildAttrType.Activity, param.get(GuildAttrType.Activity))
		self.SetAttrCurrent(GuildAttrType.ApplicationQueue, {})
		self.SetAttrCurrent(GuildAttrType.PresidentPlayerDict, {})
		self.SetAttrCurrent(GuildAttrType.ElderPlayerDict, {})
		self.SetAttrCurrent(GuildAttrType.CommonPlayerDict, {})
		self.SetAttrCurrent(GuildAttrType.MaxNum, param.get(GuildAttrType.MaxNum))
		self.SetAttrCurrent(GuildAttrType.MapId, param.get(GuildAttrType.MapId))
		self.SetAttrCurrent(GuildAttrType.UnActivityDay, param.get(GuildAttrType.UnActivityDay))
		
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
	
	def GetAttr(self, attrType):
		'''
		查询属性
		'''
		return self.mAttrsDictCurrent.get(attrType, None)
	
	def GetAttrsToSync(self):
		'''
		获取同步属性
		'''
		return self.mAttrsToSync
	
	def ResetAttrs(self):
		'''
		重置待同步属性
		'''
		self.mAttrsToSync = {}
		
	def ResetAttrsToSave(self):
		self.mAttrsToSave = {}
		
	def GetAttrsToSyncWhenAddPlayer(self):
		'''
		登陆时，推一下信息
		'''
		attrsToSync = {}
		for attrType, attrValue in self.mAttrsDictCurrent.items():
			if attrType in self.mNeedsUpdateAttrs:
				attrsToSync[attrType] = attrValue
		return attrsToSync
		
	def GetGuildBrief(self):
		'''
		获取简略信息
		'''
		attrsBriefDict = self.mAttrsDictCurrent.copy()
		attrsBriefDict.pop(GuildAttrType.GuildId)
		attrsBriefDict.pop(GuildAttrType.ApplicationQueue)
		attrsBriefDict.pop(GuildAttrType.ElderPlayerDict)
		attrsBriefDict.pop(GuildAttrType.CommonPlayerDict)
		attrsBriefDict.pop(GuildAttrType.MapId)
		attrsBriefDict.pop(GuildAttrType.UnActivityDay)
		attrsBriefDict[GuildAttrType.CurrentNum] = len(self.GetAttr(GuildAttrType.PresidentPlayerDict)) + \
		                                           len(self.GetAttr(GuildAttrType.ElderPlayerDict)) + \
		                                           len(self.GetAttr(GuildAttrType.CommonPlayerDict))
		attrsBriefDict['PresidentName'] = list(self.GetAttr(GuildAttrType.PresidentPlayerDict).values())[0].get(PlayerAttrType.Name)
		return attrsBriefDict
	
	def AddPlayer(self, uid, playerData, duty):
		"""
		玩家加入公会
		"""
		attrType = guildConsts.DutyTypeToGuildDict.get(duty, None)
		if attrType not in (GuildAttrType.PresidentPlayerDict, GuildAttrType.ElderPlayerDict, GuildAttrType.CommonPlayerDict):
			return
		self.mAttrsDictCurrent[attrType][uid] = playerData
		#新加入的玩家把公会所有信息同步过去
		self.SetAllSync()
	
	def SetAllSync(self):
		for attrType, attrValue in self.mAttrsDictCurrent.items():
			if attrType in self.mNeedsUpdateAttrs:
				self.mAttrsToSync[attrType] = attrValue
	
	def RemovePlayer(self, uid, duty):
		"""
		玩家离开公会
		"""
		attrType = guildConsts.DutyTypeToGuildDict.get(duty, None)
		if attrType not in (GuildAttrType.PresidentPlayerDict, GuildAttrType.ElderPlayerDict, GuildAttrType.CommonPlayerDict):
			return
		if self.mAttrsDictCurrent[attrType].has_key(uid):
			self.mAttrsDictCurrent[attrType].pop(uid)
			self.mAttrsToSync[attrType] = self.mAttrsDictCurrent[attrType]
		
	def ChangePlayerDuty(self, uid, fromDuty, toDuty):
		"""
		修改玩家职务
		"""
		fromAttrType = guildConsts.DutyTypeToGuildDict.get(fromDuty, None)
		toAttrType = guildConsts.DutyTypeToGuildDict.get(toDuty, None)
		if fromAttrType not in (GuildAttrType.PresidentPlayerDict, GuildAttrType.ElderPlayerDict, GuildAttrType.CommonPlayerDict):
			return
		if toAttrType not in (GuildAttrType.PresidentPlayerDict, GuildAttrType.ElderPlayerDict, GuildAttrType.CommonPlayerDict):
			return
		if self.mAttrsDictCurrent[fromAttrType].has_key(uid):
			playerData = self.mAttrsDictCurrent[fromAttrType].get(uid)
			self.mAttrsDictCurrent[fromAttrType].pop(uid)
			self.mAttrsDictCurrent[toAttrType][uid] = playerData
			
			self.mAttrsToSync[fromAttrType] = self.mAttrsDictCurrent[fromAttrType]
			self.mAttrsToSync[toAttrType] = self.mAttrsDictCurrent[toAttrType]
			
	def ChangePlayerAttr(self, uid, duty, attrType, attrValue):
		"""
		修改玩家的公会成员属性
		"""
		group =  guildConsts.DutyTypeToGuildDict.get(duty, None)
		if group not in (GuildAttrType.PresidentPlayerDict, GuildAttrType.ElderPlayerDict, GuildAttrType.CommonPlayerDict):
			return
		if self.mAttrsDictCurrent[group].has_key(uid):
			self.mAttrsDictCurrent[group][uid][attrType] = attrValue
			self.mAttrsToSync[group] = self.mAttrsDictCurrent[group]
			
	def PutUidToApplicationQueue(self, args):
		'''
		把玩家放到申请队列里
		'''
		uid = args.get('uid')
		level = args.get('level')
		name = args.get('name')
		applicationTime = args.get('applicationTime', None)
		needSave = args.get('needSave', True)
		if self.mAttrsDictCurrent[GuildAttrType.ApplicationQueue].has_key(uid):
			return
		if applicationTime == None:
			applicationTime = time.time()
		data = {'applicationTime': applicationTime, 'level': level, 'name': name}
		self.mAttrsDictCurrent[GuildAttrType.ApplicationQueue][uid] = data
		self.mAttrsToSync[GuildAttrType.ApplicationQueue] = self.mAttrsDictCurrent[GuildAttrType.ApplicationQueue]
		print "PutUidToApplicationQueue", self.mAttrsDictCurrent[GuildAttrType.ApplicationQueue]
		if needSave:
			guildId = self.GetAttr(GuildAttrType.GuildId)
			saveData = {'applicationTime': applicationTime, 'uid': uid, 'guildId': guildId}
			def saveApplicationCb(suc):
				if suc:
					logout.info(saveData, " 申请队列插入成功")
			guildConsts.GetServiceModSystem().GetMysqlMgr().SaveGuildApplication(saveData, saveApplicationCb)
		
	def GetPlayerNum(self):
		"""
		返回当前公会成员总数
		"""
		totalNum = len(self.GetAttr(GuildAttrType.PresidentPlayerDict)) + \
		           len(self.GetAttr(GuildAttrType.ElderPlayerDict)) +\
		           len(self.GetAttr(GuildAttrType.CommonPlayerDict))
		return totalNum
	
	def KickPlayer(self, uid):
		"""
		把玩家踢出公会
		"""
		print "KickPlayer", uid
		for dictType in (GuildAttrType.PresidentPlayerDict, GuildAttrType.ElderPlayerDict, GuildAttrType.CommonPlayerDict):
			if self.mAttrsDictCurrent[dictType].has_key(uid):
				self.mAttrsDictCurrent[dictType].pop(uid)
				self.mAttrsToSync[dictType] = self.mAttrsDictCurrent[dictType]
				print "KickPlayer", self.mAttrsToSync
				
	def AddPlayerToGuildPlayerList(self, uid, playerAttrs, duty, isAdd):
		"""
		同意申请列表中的玩家成为公会的正式成员
		"""
		if self.mAttrsDictCurrent[GuildAttrType.ApplicationQueue].has_key(uid):
			self.mAttrsDictCurrent[GuildAttrType.ApplicationQueue].pop(uid)
			self.mAttrsToSync[GuildAttrType.ApplicationQueue] = self.mAttrsDictCurrent[GuildAttrType.ApplicationQueue]
			def deleteApplicationCb(suc):
				if suc:
					logout.info(guildId, "application", uid, " 申请队列删除成功")
			guildId = self.GetAttr(GuildAttrType.GuildId)
			guildConsts.GetServiceModSystem().GetMysqlMgr().DeleteGuildApplication(guildId, uid, deleteApplicationCb)
		if isAdd:
			self.AddPlayer(uid, playerAttrs, duty)
	
	# def DoAutoSave(self):
	# 	'''
	# 	执行定时存档
	# 	'''
	# 	if self.IsNeedSave(int(time.time())) == False:
	# 		return
	# 	self.DoSave()
	
	def DoSave(self):
		'''
		存档所有数据
		'''
		def SaveCb(args, mAttrsDictCurrent):
			if args is None:
				logout.error("save guild[%s:%s] fail" % (mAttrsDictCurrent.get(GuildAttrType.GuildId), mAttrsDictCurrent.get(GuildAttrType.Name)))
		callback = lambda args: SaveCb(args, self.mAttrsDictCurrent)
		guildConsts.GetServiceModSystem().GetMysqlMgr().SaveGuildByGuildId(self.mAttrsDictCurrent, callback)
		
	def SaveAttrsToSave(self):
		'''
		存档已改变的属性
		'''
		def SaveCb(args, mAttrsDictCurrent):
			if args is None:
				logout.error("save guild[%s:%s] fail"%(mAttrsDictCurrent.get(GuildAttrType.GuildId), mAttrsDictCurrent.get(GuildAttrType.Name)))
		callback = lambda args: SaveCb(args, self.mAttrsDictCurrent)
		guildConsts.GetServiceModSystem().GetMysqlMgr().SaveGuildPartByGuildId(self.mAttrsToSave, callback)
	
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
	
	def Tick(self):
		self.mFrame += 1
		if self.mAttrsToSave:
			self.mAttrsToSave[GuildAttrType.GuildId] = self.GetAttr(GuildAttrType.GuildId)
			self.SaveAttrsToSave()
			self.ResetAttrsToSave()
		# if self.mFrame % self.CHECK_SAVE_FRAME == 0:
		# 	self.DoAutoSave()