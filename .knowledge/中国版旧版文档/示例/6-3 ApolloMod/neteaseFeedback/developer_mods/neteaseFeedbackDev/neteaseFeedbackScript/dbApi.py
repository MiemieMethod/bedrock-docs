# -*- coding: utf-8 -*-
import json
import apolloCommon.mysqlPool as mysqlPool
import time

def Init():
	mysqlPool.InitDB(30)
	
def InitTagType(tags):
	for tagOne in tags:
		sql = "insert into neteaseFeedbackTagType(type) values (%s) on duplicate key update type = %s"
		params = (tagOne, tagOne, )
		mysqlPool.SyncInsert(sql, params)
		
def SelectAllTagType():
	tagsDict = {}
	minId = 0
	while True:
		sql = 'select id, type from neteaseFeedbackTagType where id > %s ORDER BY id LIMIT %s'
		records = mysqlPool.SyncFetchAll(sql, (minId, 100))
		if not records:
			break
		for record in records:
			tagId = record[0]
			tagName = record[1].encode("utf-8")
			#print "tagName", tagName
			tagsDict[tagName] = tagId
		minId = records[-1][0]
	print "tagsDict", tagsDict
	return tagsDict

def InsertFeedbackToDb(message, uid, userName, cb = None):
	cuurentTime = time.time()
	sql = "insert into neteaseFeedbackMessage(message, uid, userName, createTime) values (%s, %s, %s, %s)"
	params = (message, uid, userName, cuurentTime, )
	mysqlPool.AsyncInsertOneWithOrderKey(uid, sql, params, cb)
	
def InsertFeedbackHasTagToDb(messageId, tagsId):
	for tagId in tagsId:
		sql = "insert into neteaseFeedbackHasTag(messageId, tagId) values (%s, %s) on duplicate key update messageId = %s and tagId = %s"
		params = (messageId, tagId, messageId, tagId, )
		mysqlPool.AsyncInsertOneWithOrderKey(messageId, sql, params)
		
def SelectFeedbackByTagIds(tagIds, cb):
	sql = "select * from neteaseFeedbackMessage a left join neteaseFeedbackHasTag b on a.id = b.messageId where b.tagId in %s"
	params = (tagIds, )
	mysqlPool.AsyncQueryWithOrderKey("pl%s" % str(tagIds), sql, params, cb)
