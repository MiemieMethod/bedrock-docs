# -*- coding: utf-8 -*-
import apolloCommon.mongoPool as mongoPool
import logout
import lobbyGame.netgameApi as netgameApi

#-----------------------------------------------------------------------------------
PLAYER_COLLECTION = 'player_col' #mongo中，存储玩家数据的集合
#-----------------------------------------------------------------------------------

def QuerySinglePlayer(collection, uid):
	'''
	查询uid对应玩家数据。它会在异步线程执行，这里不能调用mod api
	'''
	document = collection.find_one({"_id":uid})
	if not document:
		return None
	return document

def InsertSinglePlayer(collection, uid, base):
	'''
	插入玩家数据它会在异步线程执行，这里不能调用mod api
	'''
	ret = collection.insert_one(base)
	return ret

def SaveSinglePlayer(collection, uid, base):
	try:
		ret = collection.replace_one({"_id": uid}, base)
	except Exception, e:
		logout.error('save exception:%s. save info:%s' % (str(e), str(base)))
		ret = None
	return (uid, ret)

class MongoOperation(object):
	
	def InitMongoDb(self):
		exist, host, user, password, database, port = netgameApi.GetMongoConfig()
		if exist:
			mongoPool.Init(host, port, user, password, database, 20)
		else:
			logout.error("[DATABASE_ERROR] mongo db not exist!")
		return exist
	
	def QueryPlayerData(self,player_id,uid,cb = None):
		mongoPool.AsyncExecuteWithOrderKey(
			PLAYER_COLLECTION, QuerySinglePlayer,
		    "%s_%s" % (PLAYER_COLLECTION, uid),
		    cb,uid)
	
	def InsertPlayerData(self, player_id, uid,player_data,cb = None):
		mongoPool.AsyncExecuteWithOrderKey(PLAYER_COLLECTION,
		                                      InsertSinglePlayer,
		                                      "%s_%s" % (PLAYER_COLLECTION, uid),
		                                      cb,uid, player_data)
	
	def SavePlayerByUid(self, uid, player_data,cb = None):
		mongoPool.AsyncExecuteWithOrderKey(PLAYER_COLLECTION,
		                                      SaveSinglePlayer,
		                                      "%s_%s" % (PLAYER_COLLECTION, uid),
		                                      cb,uid, player_data)
			
	def Destroy(self):
		mongoPool.Finish()