# -*- coding: utf-8 -*-
import json

import apolloCommon.mysqlPool as mysqlPool

# 辅助函数 -- 把unicode编码的字符串、字典或列表转换成utf8编码
def UnicodeConvert(input):
	if isinstance(input, dict):
		return {UnicodeConvert(key): UnicodeConvert(value) for key, value in input.iteritems()}
	elif isinstance(input, list):
		return [UnicodeConvert(element) for element in input]
	elif isinstance(input, tuple):
		tmp = [UnicodeConvert(element) for element in input]
		return tuple(tmp)
	elif isinstance(input, unicode):
		return input.encode('utf-8')
	else:
		return input

def Init():
	mysqlPool.InitDB(10)

def Destroy():
	mysqlPool.Finish()

# 查询指定玩家的外观存档信息
def QueryPlayerData(uid, cbFunc):
	sql = "SELECT uid, addupData FROM neteaseAddupData WHERE uid=%s"
	params = (uid, )
	def queryCallback(data):
		if not data:
			cbFunc(None)
			return
		_, addupData = data[0]
		addupData = UnicodeConvert(json.loads(addupData))
		cbFunc(addupData)
	mysqlPool.AsyncQueryWithOrderKey("pl%s" % uid, sql, params, queryCallback)

# 插入一条新的外观存档数据
def InsertPlayerData(uid, addupData, cbFunc=None):
	sql = "INSERT INTO neteaseAddupData (uid, addupData) VALUES (%s, %s)"
	params = (uid, json.dumps(addupData, ensure_ascii=False))
	def insertCallback(suc):
		if not cbFunc or not callable(cbFunc):
			return
		cbFunc(suc)
	mysqlPool.AsyncExecuteWithOrderKey("pl%s" % uid, sql, params, insertCallback)

# 更新指定玩家的外观存储信息
def UpdatePlayerData(uid, addupData, cbFunc=None):
	sql = "UPDATE neteaseAddupData SET addupData=%s WHERE uid=%s"
	params = (json.dumps(addupData, ensure_ascii=False), uid)
	def updateCallback(suc):
		if not cbFunc or not callable(cbFunc):
			return
		cbFunc(suc)
	mysqlPool.AsyncExecuteWithOrderKey("pl%s" % uid, sql, params, updateCallback)
	