# -*- coding: utf-8 -*-
import apolloCommon.mongoPool as mongoPool
import logout
import lobbyGame.netgameApi as netgameApi

#-----------------------------------------------------------------------------------
PLAYER_COLLECTION = 'player_TutotialMod' #mongo中，存储玩家数据的集合
#-----------------------------------------------------------------------------------
def SaveSinglePlayer(collection, uid, base):
	try:
		ret = collection.replace_one({"_id": uid}, base)
	except Exception, e:
		logout.error('save exception:%s. save info:%s' % (str(e), str(base)))
		ret = None
	return (uid, ret)


def QuerySinglePlayer(collection, uid):
	document = collection.find_one({"_id": uid})
	if not document:
		return None
	return document


def InsertSinglePlayer(collection, uid, base):
	ret = collection.insert_one(base)
	return ret

class MongoOperation(object):
	
	def InitMongoDb(self):
		exist, host, user, password, database, port = netgameApi.GetMongoConfig()
		if exist:
			mongoPool.Init(host, port, user, password, database, 20)
		else:
			logout.error("[DATABASE_ERROR] mongo db not exist!")
		return exist
	
	def AddDiamondSword(self, playerId):
		'''
		玩家钻石剑数量加1
		'''
		uid = netgameApi.GetPlayerUid(playerId)
		mongoPool.AsyncExecuteWithOrderKey(PLAYER_COLLECTION, QuerySinglePlayer,
		                                      "%s_%s" % (PLAYER_COLLECTION, uid),
		                                      lambda data: self.AddOneDiamondSword(uid, data),
		                                      uid)
		
	def AddOneDiamondSword(self, uid, data):
		if data:
			player_dict = data
			player_dict["_id"] = uid
			if data.has_key("DiamondSwordNum"):
				player_dict["DiamondSwordNum"] = player_dict["DiamondSwordNum"] + 1
			else:
				player_dict["DiamondSwordNum"] = 1
			mongoPool.AsyncExecuteWithOrderKey(PLAYER_COLLECTION, SaveSinglePlayer,
			                                      "%s_%s" % (PLAYER_COLLECTION, uid),
			                                      None,
			                                      uid, player_dict)
		else:
			player_dict = {'_id': uid, 'DiamondSwordNum': 1}
			mongoPool.AsyncExecuteWithOrderKey(PLAYER_COLLECTION, InsertSinglePlayer,
			                                      "%s_%s" % (PLAYER_COLLECTION, uid),
			                                      None,
			                                      uid, player_dict)
			
	def Destroy(self):
		mongoPool.Finish()