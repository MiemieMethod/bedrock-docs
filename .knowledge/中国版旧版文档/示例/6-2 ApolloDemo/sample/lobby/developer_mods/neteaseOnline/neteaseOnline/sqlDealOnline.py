#coding:utf-8

import logout
#--------------------------------------------------------------------------------------------------
# 设置玩家在线标识
def redis_get_player_lock(db, idx, uid, serverid, proxyid):
	# 使用hash形式存储
	# serverid为玩家当前所在服务器进程的serverid
	# proxyid为玩家客户端当前保持连接的proxy进程的serverid
	key_player = "online_user_%d" % uid
	data = {"serverid":serverid, "proxyid":proxyid}
	ret = db.hmset(key_player, data)
	if not ret:
		logout.error("redis_get_player_lock fail by ret=%s" % ret)
		return (idx, uid, False)
	return (idx, uid, True)

# 释放玩家在线标识	
def redis_release_player_lock(db, idx, uid):
	# 这里只删除了玩家所在服务器进程的信息
	# 玩家客户端连接的proxy进程信息，还是保留，用于可能存在的聊天等业务需求
	key_player = "online_user_%d" % uid
	ret = db.hdel(key_player, "serverid")
	if ret is False:
		logout.error("redis_release_player_lock fail by ret=%s" % ret)
		return (idx, uid, False)
	return (idx, uid, True)
	
	

	
