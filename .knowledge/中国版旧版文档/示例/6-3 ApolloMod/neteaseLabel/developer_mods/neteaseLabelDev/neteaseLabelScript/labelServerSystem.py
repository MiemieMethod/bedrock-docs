# -*- coding: utf-8 -*-

from collections import Counter
import datetime
import lobbyGame.netgameApi as netgameApi
import apolloCommon.commonNetgameApi as commonNetgameApi
import logout
import neteaseLabelScript.labelConst as labelConst
import apolloCommon.mysqlPool as mysqlPool
import server.extraServerApi as serverApi

ServerSystem = serverApi.GetServerSystemCls()


def drop_comments(p_object):
	if isinstance(p_object, dict):
		return {drop_comments(key): drop_comments(value) for key, value in p_object.iteritems() if key != '_comment'}
	elif isinstance(p_object, list):
		return [drop_comments(item) for item in p_object]
	elif isinstance(p_object, unicode):
		return p_object.encode('utf-8')
	else:
		return p_object


class LabelServerSystem(ServerSystem):
	def __init__(self, namespace, systemName):
		ServerSystem.__init__(self, namespace, systemName)
		self.mLabelOnlinePlayers = set()
		self.mPlayerId2LabelFrontBack = {}
		self.mPlayerId2LabelHead = {}
		self.mPlayerId2LabelInfo = {}
		self.mPlayerAoiMonitor = 0
		if not self.InitMysqlPool():
			return
		if not self.InitLabelCfg():
			return

		self.ListenForEvent(serverApi.GetEngineNamespace(), serverApi.GetEngineSystemName(), labelConst.AddServerPlayerEvent, self, self.OnAddServerPlayer)
		self.ListenForEvent(serverApi.GetEngineNamespace(), serverApi.GetEngineSystemName(), labelConst.DelServerPlayerEvent, self, self.OnDelServerPlayer)
		self.ListenForEvent(labelConst.ModName, labelConst.ClientSystemName, labelConst.QueryAllLabelsInUseEvent, self, self.OnQueryAllLabelsInUse)
		self.ListenForEvent(labelConst.ModName, labelConst.ClientSystemName, labelConst.PlayerPutOnLabelEvent, self, self.OnPlayerPutOnLabel)
		self.ListenForEvent(labelConst.ModName, labelConst.ClientSystemName, labelConst.PlayerTakeOffLabelEvent, self, self.OnPlayerTakeOffLabel)
		self.ListenForEvent(labelConst.ModName, labelConst.ClientSystemName, 'ResumeDisplayEvent', self, self.OnResumeDisplay)

	def InitMysqlPool(self):
		try:
			mysqlPool.InitDB(20)
		except:
			logout.error("Exception in InitMysqlPool")
			return False
		return True

	def InitLabelCfg(self):
		cfg = commonNetgameApi.GetModJsonConfig("neteaseLabelScript")
		if not cfg:
			logout.error("nothing in InitLabelCfg")
			return False
		self.mLabels = drop_comments(cfg['Labels'])
		for labelId, config in self.mLabels.items():
			part = config['part']
			if not (isinstance(part, int) and part in (0, 1, 2)):
				self.mLabels.pop(labelId)
		return True

	def Update(self):
		self.mPlayerAoiMonitor += 1
		if self.mPlayerAoiMonitor % 44:
			self.mPlayerAoiMonitor = 0
			self.DetectPlayerAoi()

	def DetectPlayerAoi(self):
		"""
		每隔一定时间，根据AOI向客户端同步可见范围内的称号信息
		"""
		for playerId in self.mLabelOnlinePlayers.copy():
			comp = self.CreateComponent(playerId, 'Minecraft', 'game')
			try:
				entityIdList = comp.GetEntitiesAround(playerId, 100, {})
				labels = {entityId: self.mPlayerId2LabelHead[entityId] for entityId in entityIdList if entityId != playerId and entityId in self.mPlayerId2LabelHead}
				if playerId in self.mPlayerId2LabelHead:
					labels[playerId] = self.mPlayerId2LabelHead[playerId]
				self.NotifyToClient(playerId, 'HighlightEvent', {'labels': labels})
			except:
				import traceback
				traceback.print_exc()
				print 'Exception in DetectPlayerAoi playerId: {}'.format(playerId)

	def Destroy(self):
		self.UnListenForEvent(serverApi.GetEngineNamespace(), serverApi.GetEngineSystemName(), labelConst.AddServerPlayerEvent, self, self.OnAddServerPlayer)
		self.UnListenForEvent(serverApi.GetEngineNamespace(), serverApi.GetEngineSystemName(), labelConst.DelServerPlayerEvent, self, self.OnDelServerPlayer)
		self.UnListenForEvent(labelConst.ModName, labelConst.ClientSystemName, labelConst.QueryAllLabelsInUseEvent, self, self.OnQueryAllLabelsInUse)
		self.UnListenForEvent(labelConst.ModName, labelConst.ClientSystemName, labelConst.PlayerPutOnLabelEvent, self, self.OnPlayerPutOnLabel)
		self.UnListenForEvent(labelConst.ModName, labelConst.ClientSystemName, labelConst.PlayerTakeOffLabelEvent, self, self.OnPlayerTakeOffLabel)
		self.UnListenForEvent(labelConst.ModName, labelConst.ClientSystemName, 'ResumeDisplayEvent', self, self.OnResumeDisplay)
		mysqlPool.Finish()

	def OnResumeDisplay(self, data):
		"""
		设置前缀型称号和后缀型称号
		"""
		playerId = data["playerId"]
		if playerId in self.mPlayerId2LabelFrontBack:
			front, back = self.mPlayerId2LabelFrontBack[playerId]
			comp = self.CreateComponent(playerId, "Minecraft", "name")
			if comp:
				comp.SetPlayerPrefixAndSuffixName(front, '', back, '')

	def OnAddServerPlayer(self, data):
		"""
		玩家上线
		"""
		playerId = data.get("id", "-1")
		self.mLabelOnlinePlayers.add(playerId)

	def OnDelServerPlayer(self, data):
		"""
		玩家离线
		"""
		playerId = data.get("id", "-1")
		self.mLabelOnlinePlayers.discard(playerId)
		self.mPlayerId2LabelInfo.pop(playerId, -1)
		self.mPlayerId2LabelHead.pop(playerId, -1)
		self.mPlayerId2LabelFrontBack.pop(playerId, -1)

	def OnQueryAllLabelsInUse(self, data):
		"""
		客户端初始化完毕，向服务器发送的第一条消息，去数据库查询称号的存档信息
		"""
		playerId = data.get("playerId", "-1")
		uid = netgameApi.GetPlayerUid(playerId)
		if not uid:
			print 'can not get uid by playerId: %s' % playerId
			return
		sql = 'SELECT label_id, part, in_use FROM {} WHERE uid=%s'.format(labelConst.TableLabelData)
		mysqlPool.AsyncQueryWithOrderKey(
			'QUERY_PLAYER_{}_ALL_LABELS_IN_USE'.format(uid), sql, (uid,),
			lambda resultSet: self.PostQueryAllLabelsInUse(resultSet, uid))

	def PostQueryAllLabelsInUse(self, resultSet, uid):
		"""
		从数据库读取存档信息返回
		"""
		if resultSet is None:
			logout.error('QUERY_PLAYER_{}_ALL_LABELS_IN_USE failed'.format(uid))
			return
		playerId = netgameApi.GetPlayerIdByUid(uid)
		if not playerId:
			print 'can not get playerId by uid: %s' % uid
			return
		if playerId in self.mLabelOnlinePlayers:
			self.mPlayerId2LabelInfo[playerId] = {row[0]: {'labelId': row[0], 'part': self.mLabels[row[0]]['part'], 'inUse': row[2]} for row in resultSet if row[0] in self.mLabels}
			self.NotifyToClient(playerId, 'CacheEvent', {'cache': self.mPlayerId2LabelInfo[playerId]})
		front, back = '', ''
		for row in resultSet:
			labelId, part, inUse = row
			if not inUse:
				continue
			if labelId in self.mLabels and part == self.mLabels[labelId]['part']:
				if not part:
					front = self.mLabels[labelId]['text']
				elif part % 2:
					back = self.mLabels[labelId]['text']
				else:
					label = self.mLabels[labelId]
					if playerId in self.mLabelOnlinePlayers:
						self.mPlayerId2LabelHead[playerId] = label
		comp = self.CreateComponent(playerId, "Minecraft", "name")
		if comp:
			comp.SetPlayerPrefixAndSuffixName(front, '', back, '')
		if playerId in self.mLabelOnlinePlayers:
			self.mPlayerId2LabelFrontBack[playerId] = (front, back)

	def PrePutOnLabel(self, conn, uid, labelId, part):
		"""
		1、查询想要佩戴的称号是否解锁
		2、更新目标称号，以及同类的其他已解锁称号的佩戴状态
		"""
		try:
			c = conn.cursor()
			c.execute('SELECT * FROM {} WHERE uid=%s AND label_id=%s'.format(labelConst.TableLabelData), (uid, labelId))
			rows = c.fetchall()
			if rows:
				c.execute(
					'UPDATE {} t SET t.in_use = CASE t.label_id WHEN %s THEN 1 ELSE 0 END, t.part = CASE t.label_id WHEN %s THEN %s ELSE t.part END WHERE t.uid=%s AND (t.label_id=%s OR t.part=%s)'.format(labelConst.TableLabelData),
					(labelId, labelId, part, uid, labelId, part)
				)
				conn.commit()
				c.execute('SELECT label_id, part, in_use FROM {} WHERE uid=%s'.format(labelConst.TableLabelData), (uid,))
				return c.fetchall()
			else:
				return False
		except Exception as e:
			conn.rollback()
			logout.error('Exception in PrePutOnLabel e: {}'.format(e))
			return False

	def OnPlayerPutOnLabel(self, data):
		"""
		client界面触发：【佩戴某个称号】的行为
		"""
		playerId = data.get("playerId", "-1")
		uid = netgameApi.GetPlayerUid(playerId)
		if not uid:
			print 'can not get uid by playerId: %s' % playerId
			return
		labelId = data['labelId']
		if labelId not in self.mLabels:
			return
		mysqlPool.AsyncExecuteFunctionWithOrderKey(
			self.PrePutOnLabel,
			'PLAYER_%s_PUT_ON_LABEL' % uid,
			lambda rows: self.PostManipulateOneLabel(rows, uid),
			uid, labelId, self.mLabels[labelId]['part']
		)

	def PreTakeOffLabel(self, conn, uid, labelId, part):
		"""
		1、查询想要卸下的称号是否解锁
		2、更新目标称号的佩戴状态
		"""
		try:
			c = conn.cursor()
			c.execute('SELECT * FROM {} WHERE uid=%s AND label_id=%s'.format(labelConst.TableLabelData), (uid, labelId))
			rows = c.fetchall()
			if rows:
				c.execute(
					'UPDATE {} t SET t.in_use = 0, t.part = %s WHERE t.uid=%s AND t.label_id=%s'.format(labelConst.TableLabelData),
					(part, uid, labelId)
				)
				conn.commit()
				c.execute('SELECT label_id, part, in_use FROM {} WHERE uid=%s'.format(labelConst.TableLabelData), (uid,))
				return c.fetchall()
			else:
				return False
		except Exception as e:
			conn.rollback()
			logout.error('Exception in PreTakeOffLabel e: {}'.format(e))
			return False

	def PostManipulateOneLabel(self, rows, uid):
		"""
		更新内存中缓存的称号的佩戴状态
		"""
		if not rows:
			return
		playerId = netgameApi.GetPlayerIdByUid(uid)
		if not playerId:
			print 'can not get playerId by uid: %s' % uid
			return
		if playerId in self.mLabelOnlinePlayers:
			self.mPlayerId2LabelInfo[playerId] = {row[0]: {'labelId': row[0], 'part': self.mLabels[row[0]]['part'], 'inUse': row[2]} for row in rows if row[0] in self.mLabels}
			self.NotifyToClient(playerId, 'CacheEvent', {'cache': self.mPlayerId2LabelInfo[playerId]})
		front, back = '', ''
		flag = True
		for row in rows:
			labelId, part, inUse = row
			if inUse and labelId in self.mLabels and part == self.mLabels[labelId]['part']:
				if not part:
					front = self.mLabels[labelId]['text']
				elif part % 2:
					back = self.mLabels[labelId]['text']
				else:
					flag = False
					label = self.mLabels[labelId]
					if playerId in self.mLabelOnlinePlayers:
						self.mPlayerId2LabelHead[playerId] = label
		if flag:
			self.mPlayerId2LabelHead.pop(playerId, -1)
		comp = self.CreateComponent(playerId, "Minecraft", "name")
		if comp:
			comp.SetPlayerPrefixAndSuffixName(front, '', back, '')
		if playerId in self.mLabelOnlinePlayers:
			self.mPlayerId2LabelFrontBack[playerId] = (front, back)

	def OnPlayerTakeOffLabel(self, data):
		"""
		client界面触发：【卸下某个称号】的行为
		"""
		playerId = data.get("playerId", "-1")
		uid = netgameApi.GetPlayerUid(playerId)
		if not uid:
			print 'can not get uid by playerId: %s' % playerId
			return
		labelId = data['labelId']
		if labelId not in self.mLabels:
			return
		mysqlPool.AsyncExecuteFunctionWithOrderKey(
			self.PreTakeOffLabel,
			'PLAYER_%s_TAKE_OFF_LABEL' % uid,
			lambda rows: self.PostManipulateOneLabel(rows, uid),
			uid, labelId, self.mLabels[labelId]['part']
		)

	def PreOpenLabelBoard(self, conn, uid):
		"""
		查询指定ui的玩家的已经解锁的称号信息
		"""
		try:
			c = conn.cursor()
			c.execute('SELECT label_id, part, in_use FROM {} WHERE uid=%s'.format(labelConst.TableLabelData), (uid,))
			return c.fetchall()
		except Exception as e:
			conn.rollback()
			logout.error('Exception in PreOpenLabelBoard e: {}'.format(e))
			return False

	def OpenLabelBoard(self, uid, **kwargs):
		"""
		指定uid的玩家，显示称号界面
		假如内存缓存中，已经有对应玩家的称号信息了，直接通知客户端显示称号界面
		否则就从需要先从数据库查询已经解锁的称号信息
		"""
		print 'OpenLabelBoard', uid
		playerId = netgameApi.GetPlayerIdByUid(uid)
		if not playerId:
			print 'can not get playerId by uid: %s' % uid
			return
		if 'rows' in kwargs:
			rows = kwargs['rows'] or []
			if playerId in self.mLabelOnlinePlayers:
				self.mPlayerId2LabelInfo[playerId] = {row[0]: {'labelId': row[0], 'part': self.mLabels[row[0]]['part'], 'inUse': row[2]} for row in rows if row[0] in self.mLabels}
				self.NotifyToClient(playerId, 'CacheEvent', {'cache': self.mPlayerId2LabelInfo[playerId]})
			self.NotifyToClient(playerId, labelConst.DisplayLabelBoardEvent, {
				'cfg': self.mLabels,
				'info': self.mPlayerId2LabelInfo[playerId]
			})
			return
		else:
			mysqlPool.AsyncExecuteFunctionWithOrderKey(
				self.PreOpenLabelBoard,
				'PLAYER_%s_OPEN_LABEL_BOARD' % uid,
				lambda rows: self.OpenLabelBoard(uid, rows=rows),
				uid
			)

	def PreUnlockLabelsForPlayer(self, conn, operation, parameters):
		"""
		数据库操作，通过插入记录的方式，为指定uid的玩家解锁一些称号
		"""
		try:
			c = conn.cursor()
			c.executemany(operation, parameters)
			rowcount = c.rowcount
			conn.commit()
		except Exception as e:
			conn.rollback()
			logout.error('Exception in PreUnlockLabelsForPlayer e: {} operation: {} parameters: {}'.format(e, operation, parameters))
			return False
		return rowcount

	def UnlockLabelsForPlayer(self, uid, labelIdList):
		"""
		为指定uid的玩家解锁一些称号
		"""
		print 'UnlockLabelsForPlayer', uid, labelIdList
		playerId = netgameApi.GetPlayerIdByUid(uid)
		if not playerId:
			print 'can not get playerId by uid: %s' % uid
			return
		s = set(labelIdList)
		for labelId in s:
			if labelId not in self.mLabels:
				return
		date = datetime.datetime.now().isoformat()
		mysqlPool.AsyncExecuteFunctionWithOrderKey(
			self.PreUnlockLabelsForPlayer,
			'UNLOCK_LABELS_FOR_PLAYER_%s' % uid,
			lambda rowcount: rowcount,
			'INSERT INTO {} (uid, label_id, recv_date, part, in_use) VALUES (%s, %s, %s, %s, %s) ON DUPLICATE KEY UPDATE uid = uid'.format(labelConst.TableLabelData),
			[(uid, labelId, date, self.mLabels[labelId]['part'], 0) for labelId in s]
		)

	def GetLabelInfoByPlayerId(self, playerId):
		return self.mPlayerId2LabelInfo.get(playerId, {})

	def GetAttrInfoByPlayerId(self, playerId):
		"""
		返回称号佩戴后的额外附加属性
		"""
		c = Counter()
		s = serverApi.GetSystem("neteaseBattle", "neteaseBattleDev")
		if not s:
			return {}
		if playerId not in self.mPlayerId2LabelInfo:
			return {}
		for k, v in self.mPlayerId2LabelInfo[playerId].iteritems():
			if v['inUse']:
				c.update(s.GetEquipAttrDict('netease_label:{}'.format(k), 0))
		return dict(c)
