# -*- coding:utf-8 -*-
import feedbackConsts as feedbackConsts
import logout
import lobbyGame.netgameApi as netgameApi
import netgame.apolloCommon.commonNetgameApi as commonNetgameApi
import server.extraServerApi as serverApi
import apolloCommon.mysqlPool as mysqlPool
import time
import dbApi

class FeedbackManager(object):
	def __init__(self, system):
		import weakref
		self.system = weakref.proxy(system)
		self.system.ListenForEvent(feedbackConsts.ModNameSpace, feedbackConsts.ClientSystemName, 'CommitFeedbackFromClientEvent', self, self.OnCommitFeedbackFromClientEvent)
		self.mAllFeedback = {}
		
	def Init(self):
		dbApi.Init()
		self.modConfig = commonNetgameApi.GetModJsonConfig('neteaseFeedbackScript')
		configTags = self.modConfig["tags"]
		feedbackTags = []
		for one in configTags:
			#print "FeedbackManager", len(one)
			if len(one) > 5:
				one = one[0:5]
			if len(feedbackTags) < 10:
				if one not in feedbackTags:
					feedbackTags.append(one)
			else:
				break
		#初始化tag，并读需要的tag
		dbApi.InitTagType(feedbackTags)
		dbFeedbackTags = dbApi.SelectAllTagType()
		self.mDbFeedbackTags = dbFeedbackTags
		self.mFeedbackTags = {}
		for tagName in feedbackTags:
			tagName = tagName.encode("utf-8")
			#print "Init", tagName, tagName in dbFeedbackTags
			if tagName in dbFeedbackTags:
				self.mFeedbackTags[tagName] = dbFeedbackTags[tagName]
		#print "Init feedbackTags", feedbackTags, dbFeedbackTags, self.mFeedbackTags
		# for tagName in self.mFeedbackTags.copy():
		# 	if tagName not in feedbackTags:
		# 		self.mFeedbackTags.pop(tagName)
		
	def GetAllFeedbackTags(self):
		return  self.mFeedbackTags
	
	def OnCommitFeedbackFromClientEvent(self, args):
		print "OnCommitFeedbackFromClientEvent", args, self.mFeedbackTags
		message = args.get("message", "")
		tags = args.get("tags", [])
		playerId = args.get("playerId", "")
		playerUid = netgameApi.GetPlayerUid(playerId)
		nickname = netgameApi.GetPlayerNickname(playerId)
		if len(tags) >= 5 or len(message) <= 0:
			feedbackConsts.ShowAlert(playerId, "文字长度超过限制")
			return
		gcomp = serverApi.CreateComponent(serverApi.GetLevelId(), "Minecraft", "game")
		if not gcomp.CheckWordsValid(message):
			print '屏蔽字'
			feedbackConsts.ShowAlert(playerId, "文字拥有屏蔽字")
			return
		tagIds = []
		for tagOne in tags:
			tagId = self.mFeedbackTags.get(tagOne)
			if tagId is not None:
				tagIds.append(tagId)
		def InsertFeedbackToDbCb(messageId):
			if messageId is not None:
				# 不管结果
				dbApi.InsertFeedbackHasTagToDb(messageId, tagIds)
				self.mAllFeedback[messageId] = {
					"message": message,
					"tags": tags,
					"tagIds": tagIds,
					"playerUid": playerUid,
					"nickname": nickname
				}
				feedbackConsts.ShowAlert(playerId, "反馈成功")
				return
		dbApi.InsertFeedbackToDb(message, playerUid, nickname, InsertFeedbackToDbCb)
		
	def GetFeedbackByCond(self, args, cb):
		'''
		根据Tag类型获取反馈
		'''
		tags = args.get("tags")
		needQueryUids = args.get("needQueryUids")
		startTime = args.get("startTime")
		endTime = args.get("endTime")
		needsTagIds = {}
		#print "GetFeedbackByCond", tags, self.mFeedbackTags
		for tagOneName in tags:
			if self.mDbFeedbackTags.has_key(tagOneName):
				needsTagIds[self.mDbFeedbackTags[tagOneName]] = tagOneName
		messageResult = []
		if len(needsTagIds.keys()) <= 0:
			cb({"messageResult": messageResult})
			return
		def SelectFeedbackByTagIdsCb(records):
			for record in records:
				if record:
					messageId = record[0]
					message = record[1]
					uid = record[2]
					if needQueryUids is not None and uid not in needQueryUids:
						continue
					userName = record[3]
					createTime = record[4]
					if startTime is not None and createTime < startTime:
						continue
					if endTime is not None and createTime > endTime:
						continue
					tagId = record[7]
					tagName = needsTagIds[tagId]
					messageResult.append({"messageId":messageId, "message":message, "uid":uid, "userName":userName, "createTime":createTime, "tagName":tagName})
			cb({"messageResult":messageResult})
		dbApi.SelectFeedbackByTagIds(needsTagIds.keys(), SelectFeedbackByTagIdsCb)
		
		
	
	
	
	
	
	