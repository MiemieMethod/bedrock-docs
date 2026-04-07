#coding:utf-8

import logout
#--------------------------------------------------------------------------------------------------
# 读取并缓存redis数据库的连接参数
redis_config = None
def read_redis_config():
	global redis_config
	import netgame_api
	exist, host, port, password = netgame_api.get_redis_config()
	if exist:
		redis_config = {"host":host, "port":port, "password":password}
	logout.info("read_redis_config %s %s %s %s" % (exist, host, port, password))

# 生成一个临时的redis连接
def get_redis_db():
	global redis_config
	if redis_config is None:
		return None
	import redis
	return redis.StrictRedis(host=redis_config["host"], port=redis_config["port"], password=redis_config["password"])
#--------------------------------------------------------------------------------------------------
# 读取并缓存mysql数据库的连接参数
mysql_config = None
def read_mysql_config():
	global mysql_config
	import netgame_api
	exist, host, user, password, database, port = netgame_api.get_mysql_config()
	if exist:
		mysql_config = {"host":host, "user":user, "password":password, "database":database, "port":port}
	logout.info("read_mysql_config %s %s %s %s %s %s" % (exist, host, user, password, database, port))

# 生成一个临时的mysql数据库连接
def get_mysql_db():
	global mysql_config
	if mysql_config is None:
		return None
	import MySQLdb
	return MySQLdb.connect(host=mysql_config["host"],
		port=mysql_config["port"],
		user=mysql_config["user"],
		passwd=mysql_config["password"],
		db=mysql_config["database"]
		)
#--------------------------------------------------------------------------------------------------
'''
示例使用mysql数据库存取玩家原始存档
仅为示例，不建议使用mysql直接存取玩家原始存档
二进制字符串太长，且完全没有可读性

建表语句
CREATE TABLE `netgame_player` (
  `pkey` varchar(30) NOT NULL,
  `data_str` mediumblob,
  PRIMARY KEY (`pkey`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;
'''
# 从mysql读取玩家二进制字符串存档
def mysql_query_playerdata(idx, playerkey):
	import cPickle
	db = get_mysql_db()
	if not db:
		logout.error("mysql_query_playerdata fail by no db")
		return idx, False, ""
	cursor = db.cursor()
	sql = "SELECT pkey, data_str FROM netgame_player where pkey='%s' LIMIT 1" % playerkey
	cursor.execute(sql)
	result = cursor.fetchone()
	if not result:	#查询不到，新建记录
		sql = "INSERT INTO netgame_player (pkey, data_str) VALUES ('%s', '')" % playerkey
		try:
			cursor.execute(sql)
			db.commit()
		except:
			db.rollback()
		suc = False
		data = ""
	else:
		suc = True
		data = cPickle.loads(result[1])
	db.close()
	return idx, suc, data

# 使用mysql数据库存储玩家二进制字符串存档
def mysql_save_playerdata(idx, playerkey, playerdata):
	import MySQLdb
	import cPickle
	db = get_mysql_db()
	if not db:
		logout.error("mysql_save_playerdata fail by no db")
		return idx, False
	cursor = db.cursor()
	sql = "UPDATE netgame_player SET data_str=%s where pkey=%s"
	try:
		# 这里使用cPickle对存档字符串进程二次打包
		# 因为总有各种难以描述的特殊字符串，可能导致存档字符串被自动截断
		# 也是不建议使用mysql存取二进制存档的原因之一
		cursor.execute(sql, (MySQLdb.Binary(cPickle.dumps(playerdata)), playerkey))
		db.commit()
		suc = True
	except:
		db.rollback()
		suc = False
	db.close()
	return idx, suc
#-----------------------------------------------------------------------------------------------
# 从redis读取玩家二进制字符串存档
def redis_query_playerdata(idx, playerkey):
	db = get_redis_db()
	if db is None:
		logout.error("redis_query_playerdata fail by no db")
		return idx, False, ""
	#
	data = db.get(playerkey)
	if not data:
		data = ""
		suc = False
	else:
		suc = True
	return idx, suc, data

# 使用redis数据库存储玩家二进制字符串存档
def redis_save_playerdata(idx, playerkey, playerdata):
	db = get_redis_db()
	if db is None:
		logout.error("redis_query_playerdata fail by no db")
		return idx, False
	#
	suc = db.set(playerkey, playerdata)
	if not suc:
		suc = False
	else:
		suc = True
	return idx, suc
	
