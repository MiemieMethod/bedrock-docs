# -*- coding: utf-8 -*-
import server.extraMasterApi as masterApi
MasterSystem = masterApi.GetMasterSystemCls()
import netease_server.mysqlpool as mysqlpool
'''
排行榜功能。
demo展示了：
	lobby/game与master通信。
	mysql线程池使用。
'''
class SyncRankSystem(MasterSystem):
	def __init__(self, namespace, systemName):
		MasterSystem.__init__(self, namespace, systemName)
		print 'init SyncRankSystem'
		#最多给1000个玩家排序，之后玩家没有排序。
		self.max_rank = 1000
		#必须大于min_value才可以进行排序。
		self.min_value = -1
		#记录玩家积分
		self.player_map  = {}#uid => {uid, score, rank, loadTime, nickname}
		#排名前1000的玩家
		self.rank_map = {} #rank id => player id
		#加载排名前1000的玩家。
		self.loadRank()
		#需要异步存档的玩家id。
		self.need_save_uids = []
		# 【自定义事件，向lobby/game发送排行榜信息】
		self.DefineEvent('RankingResponseEvent')
		# 【积分发生变化事件，这个事件在demo不会触发】，最后需要UnListenForEvent()
		self.ListenForEvent('idv', 'masterMatch', 'ChangeScoreEvent', self, self.addScore)
		# 【请求获取排行榜事件，lobby/game向master请求排行榜信息】，最后需要UnListenForEvent()
		self.ListenForEvent('Minecraft', 'SampleServer', 'RankingRequestEvent', self, self.requestRanking)
		#test
		# self.ListenForEvent(masterApi.GetEngineNamespace(), masterApi.GetEngineSystemName(), 'OnScriptTickClient', self,
	     #                self.test)
		# self.testCnt = 0#test

	#test
	# def test(self):
	# 	self.testCnt = self.testCnt + 1
	# 	if 50 == self.testCnt or 51 == self.testCnt or 52 == self.testCnt or 53 == self.testCnt:
	# 		import time
	# 		data = {}
	# 		data['uid'] = self.testCnt
	# 		data['score'] = 2
	# 		data['nickname'] = 'nickname' + str(data['uid'])
	# 		self.addScore(data)
	# 请求获取排行榜
	def requestRanking(self, data):
		serverId = data['serverId']
		rankNum = len(self.rank_map)
		#一次只获取前10名信息。
		requestNum = 10
		playerNum = requestNum if requestNum < rankNum else rankNum
		responseData = self.CreateEventData()#等价于 responseData = {}
		responseData['players'] = []
		for i in xrange(playerNum):
			onePlayer = {}
			uid = self.rank_map[i + 1]
			playerData = self.player_map[uid]
			onePlayer['id'] = uid
			onePlayer['score'] = playerData['score']
			onePlayer['nickname'] =  playerData['nickname']
			responseData['players'].append(onePlayer)
			#给"serverId"所在服发送事件，内容是responseData
		self.NotifyToServerNode(serverId, "RankingResponseEvent", responseData)
	#master tick每帧执行。
	def Update(self):
		#存档脏数据
		if self.need_save_uids:
			uid = self.need_save_uids[0]
			if uid in self.player_map:
				self.replacePlayerData(self.player_map[uid])
			self.need_save_uids.remove(uid)
		#若内存记录玩家信息太多，则从内存中删除一部分玩家信息，删除20min前加载玩家信息，每次最多删除100个。
		if len(self.player_map) >= 10000:#避免占太多内存
			import time
			expireTime = int(time.time()) - 1200
			deleteKeys = []
			deleteNum = 0
			for uid in self.player_map:
				playerData = self.player_map[uid]
				#前1000名一直在内存，其他的玩家rank值为-1.
				if playerData['rank'] >= 0:
					continue
				#需要存档的玩家，不能删除内存数据，因为需要存档。
				if playerData['id'] in self.need_save_uids:
					continue
				if playerData['loadTime'] < expireTime:
					deleteKeys.append(uid)
					deleteNum = deleteNum + 1
				if deleteNum >= 100:
					break
			for key in deleteKeys:
				del self.player_map[key]
	#replace记录玩家信息。mysql replace操作：若存在则update，若不存在则insert。
	def replacePlayerData(self, player_data):
		sql = 'replace into score_rank (rank_id, score, uid, nickname) values (%s, %s, %s, %s)'
		params = (player_data['rank'], player_data['score'], player_data['uid'], player_data['nickname'])
		#使用线程池执行mysql操作，这是个异步操作，不阻塞主线程。
		#第一个参数是mysql的table name；第二个参数时sql语句，第三个参数是个元组，对应sql参数的值。
		#线程池会将所有对score_rank表的操作排队，按照顺序执行。
		#注意，mysql线程池执行错误会重试3次，若都失败则返回None。
		mysqlpool.async_execute('score_rank', sql, params)

	#加载排名前1000的玩家。
	def loadRank(self):
		sql = 'select uid, rank_id, score,nickname from score_rank where rank_id <= %s'
		params = (self.max_rank, )
		#线程池，支持异步回调。在线程池中执行mysql查询操作，执行完成后，在主线程执行回调函数。
		#回调函数支持多个参数，最后一个参数必须是mysql执行结果。
		mysqlpool.async_query('score_rank', sql, params, lambda records : self.loadRankCb(records))

	#加载一个玩家的积分。callback为异步回调。
	def loadPlayerRank(self, uid, callback):
		sql = 'select uid, rank_id, score,nickname from score_rank where uid = %s'
		params = (uid, )
		#线程池，支持异步回调。在线程池中执行mysql查询操作，执行完成后，在主线程执行回调函数。
		mysqlpool.async_query('score_rank', sql, params, callback)

	#loadPlayerRank的回调函数，它会在主线程执行。record为查询结果，None表示错误，这里忽略了错误情况，
	#若只查到一条记录，record是个二维数组，可以通过record[0]返回记录。
	def getPlayerRankCb(self, uid, changeScore, nickname, record):
		nickname = nickname.encode('utf-8')
		if record:
			curScore = record[0][2] + changeScore
			self.changeRank(uid, curScore, nickname)
		else:
			self.changeRank(uid, changeScore, nickname)

	#loadRank的回调。records是二维数组。将所有字符串转出utf8格式，保证集群字符串格式的一致性。
	def loadRankCb(self, records):
		if records is None:
			print 'Load rank failed!'
			return
		for record in records:
			nickname = record[3].encode('utf-8')
			self.initPlayerRank(record[0], record[1], record[2], nickname)
	#处理积分变化事件。
	def addScore(self, data):
		uid = data['uid']
		changeScore = data['score']
		nickname = data['nickname']
		if uid in self.player_map:
			curScore = self.player_map[uid]['score'] + changeScore
			self.changeRank(uid, curScore, nickname)
		else:
			self.loadPlayerRank(uid, lambda record : self.getPlayerRankCb(uid, changeScore, nickname, record))
	#更新排名
	def changeRank(self, uid, score, nickname):
		self.add_save_uid(uid)
		if score < self.min_value:
			self.initPlayerRank(uid, -1, score, nickname)
			return
		rank_num = len(self.rank_map)
		if uid not in self.rank_map.values():
			next_max_rank = rank_num + 1
			cur_rank = next_max_rank
			if self.max_rank > next_max_rank:
				self.initPlayerRank(uid, next_max_rank, score, nickname)
			else:
				pre_last_uid = self.rank_map[self.max_rank]
				self.player_map[pre_last_uid]['rank'] = -1
				self.add_save_uid(pre_last_uid)
				self.initPlayerRank(uid, self.max_rank, score, nickname)
				cur_rank = self.max_rank
			self._upRank(cur_rank - 1, score)
		else:
			player_data = self.player_map[uid]
			pre_score = player_data['score']
			player_data['score'] = score
			if pre_score > score:
				self._downRank(player_data['rank'] + 1, score)
			else:
				self._upRank(player_data['rank'] - 1, score)
		self.updateMinvalue()
	#更新self.min_value
	def updateMinvalue(self):
		rank_num = len(self.rank_map)
		if rank_num < self.max_rank:
			self.min_value = -1
		else:
			uid = self.rank_map[self.max_rank]
			self.min_value = self.player_map[uid]['score']
	#提升排名。
	def _upRank(self, begin_rank, score):
		check_rank = begin_rank
		while check_rank >= 1:
			check_uid = self.rank_map[check_rank]
			check_data = self.player_map[check_uid]
			if score < check_data['score']:
				break
			self.swapRank(check_rank, check_rank + 1)
			check_rank = check_rank - 1
	#降低排名
	def _downRank(self, begin_rank, score):
		player_num = len(self.player_map)
		check_rank = begin_rank
		while check_rank <= player_num:
			check_uid = self.rank_map[check_rank]
			check_data = self.player_map[check_uid]
			if score >= check_data['score']:
				break
			self.swapRank(check_rank, check_rank - 1)
			check_rank = check_rank + 1
	#交换排名
	def swapRank(self, first_rank, second_rank):
		first_uid = self.rank_map[first_rank]
		second_uid = self.rank_map[second_rank]
		first_data = self.player_map[first_uid]
		second_data = self.player_map[second_uid]
		first_data['rank'], second_data['rank'] = second_data['rank'], first_data['rank']
		self.rank_map[first_data['rank']] = first_uid
		self.rank_map[second_data['rank']] = second_uid
		self.add_save_uid(first_uid)
		self.add_save_uid(second_uid)
	#添加需要异步存档的玩家id。
	def add_save_uid(self, uid):
		if uid not in self.need_save_uids:
			self.need_save_uids.append(uid)
	#初始化玩家信息。
	def initPlayerRank(self, uid, rank, score, nickname):
		import time
		player_data = {}
		player_data['score'] = score
		player_data['rank'] = rank
		player_data['uid'] = uid
		player_data['nickname'] = nickname
		player_data['loadTime'] = int(time.time())
		self.player_map[uid] = player_data
		if rank > 0:
			self.rank_map[rank] = uid

	def Destroy(self):
		print 'Destroy #########yyyyyyyyyyyyyyyyyyyyyyyyyyy#######SyncRankSystem################'
		self.UnListenForEvent('idv', 'masterMatch', 'ChangeScoreEvent', self, self.addScore)
		#结束前需要存档所有脏数据。
		for uid in self.need_save_uids:
			self.replacePlayerData(self.player_map[uid])
		self.need_save_uids = []