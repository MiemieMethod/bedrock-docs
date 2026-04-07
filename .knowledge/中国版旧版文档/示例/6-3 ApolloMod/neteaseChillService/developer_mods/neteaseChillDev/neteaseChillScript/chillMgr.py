# -*- coding: utf-8 -*-

import apolloCommon.mysqlPool as mysqlPool
# import apolloCommon.redisPool as redisPool
import logout
import neteaseChillScript.chillConst as chillConst
# import neteaseChillScript.timermanager as timermanager
import time
import weakref
import json


class ChillMgr(object):
	"""
	该mod的service逻辑处理类
	"""
	def __init__(self, system, moduleName):
		super(ChillMgr, self).__init__()
		self.mSystem = weakref.proxy(system)
		self.mModuleName = moduleName

		self.mSystem.RegisterRpcMethod(moduleName, chillConst.DisplayChillRewardEvent, self.OnDisplayChillRewardReq)  # 大厅服发过来查询是否已经领取了奖励，领或者没领有不同的显示状态
		self.mSystem.RegisterRpcMethod(moduleName, chillConst.PlayerRecvChillRewardEvent, self.OnPlayerRecvReq)  # 大厅服发过来表示某玩家要领取活动奖励
		self.mSystem.RegisterRpcMethod(moduleName, chillConst.PlayerAchvChillRewardEvent, self.OnPlayerAchvReq)  # 大厅服发过来表示某玩家达成了活动奖励的领取条件
		self.mSystem.RegisterRpcMethod(moduleName, chillConst.QueryPlayerChillEvent, self.OnQueryPlayerChillReq)  # master发过来查询玩家的活动奖励领取情况
		self.mSystem.RegisterRpcMethod(moduleName, 'ChillRollback', self.OnChillRollbackReq)  # 领取回滚，例如一瞬间玩家背包满了

	def Destroy(self):
		self.mSystem = None

	def ChillMgrRender(self, serverId, callbackId, data):
		respData = {
			'code': data['code'],
			'message': data.get('message', ''),
			'entity': data.get('entity', {})
		}
		self.mSystem.ResponseToServer(serverId, callbackId, respData)

	def OnChillRollbackReq(self, serverId, callbackId, data):
		"""
		来自server的回滚奖励领取状态的事件，目前在玩家背包满了的时候会触发
		"""
		uid = data.get('uid')
		if not uid:
			self.mSystem.ResponseToServer(serverId, callbackId, {
				'code': chillConst.RespCodeInvalidParameter,
				'message': 'OnChillRollbackReq 参数有误 data: {}'.format(data)
			})
			return
		sql = 'UPDATE {} SET recv_date = %s WHERE uid=%s'.format(chillConst.TableChillReward)
		mysqlPool.AsyncExecuteWithOrderKey(
			'PLAYER_{}_ROLLBACK_CHILL_REWARD'.format(uid), sql, ('-1', uid),
			lambda rtn: self.OnChillRollback(rtn, uid, serverId, callbackId))

	def OnChillRollback(self, rtn, uid, serverId, callbackId):
		respData = {
			'code': chillConst.RespCodeSuccess,
			'message': '请求成功',
		}
		if not rtn:
			# 回滚失败
			# 需要手动删除
			logout.error('玩家 {} 领取活动奖励回滚失败'.format(uid))
			respData['code'] = chillConst.RespCodeDBError
			respData['message'] = '数据库操作失败'
		else:
			logout.info('玩家 {} 领取活动奖励回滚成功'.format(uid))
		self.mSystem.ResponseToServer(serverId, callbackId, respData)

	def OnQueryPlayerChillReq(self, serverId, callbackId, data):
		"""
		查询玩家活动奖励领取情况
		"""
		uid = data.get('uid')
		if not uid:
			self.mSystem.ResponseToServer(serverId, callbackId, {
				'code': chillConst.RespCodeInvalidParameter,
				'message': ''
			})
			return
		self.OnDisplayChillRewardReq(serverId, callbackId, {'uid': uid})

	def OnDisplayChillRewardReq(self, serverId, callbackId, data):
		"""
		来自server的查询奖励领取状态的请求
		"""
		# 在数据库中查询领取情况
		uid = data.get('uid')
		if not uid:
			self.mSystem.ResponseToServer(serverId, callbackId, {
				'code': chillConst.RespCodeInvalidParameter,
				'message': 'OnDisplayChillRewardReq 参数有误 data: {}'.format(data)
			})
			return
		sql = 'SELECT achv_date, recv_date FROM {} WHERE uid=%s'.format(chillConst.TableChillReward)
		mysqlPool.AsyncQueryWithOrderKey(
			'DISPLAY_PLAYER_{}_CHILL_REWARD'.format(uid), sql, (uid,),
			lambda resultSet: self.DisplayChillReward(resultSet, uid, serverId, callbackId))

	def OnPlayerAchvReq(self, serverId, callbackId, data):
		"""
		来自server的指定uid的玩家，达成指定奖励领取条件的事件
		"""
		# 玩家达成领取条件
		uid = data.get('uid')
		if not uid:
			self.mSystem.ResponseToServer(serverId, callbackId, {
				'code': chillConst.RespCodeInvalidParameter,
				'message': 'OnPlayerAchvReq 参数有误 data: {}'.format(data)
			})
			return
		sql = 'SELECT achv_date, recv_date FROM {} WHERE uid=%s'.format(chillConst.TableChillReward)  # 先查一下是否已经获得了资格
		mysqlPool.AsyncQueryWithOrderKey(
			'PLAYER_{}_ACHV_CHILL_REWARD'.format(uid), sql, (uid,),
			lambda resultSet: self.OnPlayerAchv(resultSet, uid, serverId, callbackId))

	def OnPlayerAchv(self, resultSet, uid, serverId, callbackId):
		respData = {
			'code': chillConst.RespCodeSuccess,
			'message': '请求成功',
			'entity': {'uid': uid, 'qualified': 1}
		}
		if resultSet is None:
			logout.error('PLAYER_{}_ACHV_CHILL_REWARD failed'.format(uid))
			return
		if resultSet:
			for row in resultSet:
				if row[-1] != '-1':
					respData['entity']['qualified'] = -1  # 已经获得了资格，激活过了，不可以重复激活
			self.mSystem.ResponseToServer(serverId, callbackId, respData)
			return
		timestamp = str(time.time())
		sql = 'INSERT INTO {} (uid, achv_date) VALUES (%s, %s)'.format(chillConst.TableChillReward)  # 正常插入，achv_date的默认值就是字符串"-1"
		mysqlPool.AsyncExecuteWithOrderKey(
			'PLAYER_{}_ACHV_CHILL_REWARD'.format(uid), sql, (uid, timestamp),
			lambda rtn: rtn and self.mSystem.ResponseToServer(serverId, callbackId, respData))  # 成功则一定有领取权

	def OnPlayerRecvReq(self, serverId, callbackId, data):
		"""
		client通过server转发过来的指定uid玩家领取活动奖励的请求
		"""
		# 玩家领取活动奖励
		uid = data.get('uid')
		if not uid:
			self.mSystem.ResponseToServer(serverId, callbackId, {
				'code': chillConst.RespCodeInvalidParameter,
				'message': 'OnPlayerRecvReq 参数有误 data: {}'.format(data)
			})
			return
		timestamp = str(time.time())
		sql = 'UPDATE {} SET recv_date = %s WHERE uid=%s AND recv_date=%s'.format(chillConst.TableChillReward)
		mysqlPool.AsyncExecuteWithOrderKey(
			'PLAYER_{}_RECV_CHILL_REWARD'.format(uid), sql, (timestamp, uid, '-1'),  # 数据库是有行级锁的，所以只要保证achv_date是字符串"-1"即可成功领取
			lambda rtn: self.OnPlayerRecv(rtn, uid, timestamp, serverId, callbackId))

	def OnPlayerRecv(self, rtn, uid, timestamp, serverId, callbackId):
		if not rtn:
			# 领取失败
			logout.error('玩家 uid: {} 于时间 {} 领取活动奖励失败'.format(uid, timestamp))
			return
		sql = 'SELECT achv_date, recv_date FROM {} WHERE uid=%s'.format(chillConst.TableChillReward)  # 查询一下是否操作成功，即检查传入的时间戳为本次请求时入参的时间戳，即141行的timestamp
		mysqlPool.AsyncQueryWithOrderKey(
			'PLAYER_{}_RECV_CHILL_REWARD'.format(uid), sql, (uid,),
			lambda resultSet: self.OnGuaranteePlayerRecv(resultSet, uid, timestamp, serverId, callbackId))

	def OnGuaranteePlayerRecv(self, resultSet, uid, timestamp, serverId, callbackId):
		if resultSet is None:
			logout.error('GuaranteePlayerRecv failed')
			self.mSystem.ResponseToServer(serverId, callbackId, {
				'code': chillConst.RespCodeDBError,
				'message': '数据库操作失败',
			})
			return
		for row in resultSet:
			if row[-1] == timestamp:
				self.mSystem.ResponseToServer(serverId, callbackId, {
					'code': chillConst.RespCodeSuccess,
					'message': '请求成功',
				})
				return
			elif row[-1] == '-1':
				self.mSystem.ResponseToServer(serverId, callbackId, {
					'code': chillConst.RespCodeDBError,
					'message': '领取异常',
					'entity': {'uid': uid, 'qualified': 1}
				})
				return
			else:
				self.mSystem.ResponseToServer(serverId, callbackId, {
					'code': chillConst.RespCodeDBError,
					'message': '已领取',
					'entity': {'uid': uid, 'qualified': -1}
				})
				return
		self.mSystem.ResponseToServer(serverId, callbackId, {
			'code': chillConst.RespCodeDBError,
			'message': '无领取资格',
			'entity': {'uid': uid, 'qualified': 0}
		})

	def DisplayChillReward(self, resultSet, uid, serverId, callbackId):
		respData = {
			'code': chillConst.RespCodeSuccess,
			'message': '请求成功',
		}
		data = self.OnDisplayChillReward(resultSet)
		if data is None:
			respData['code'] = chillConst.RespCodeDBError
			respData['message'] = '数据库操作失败'
		else:
			respData['entity'] = data
		self.mSystem.ResponseToServer(serverId, callbackId, respData)

	def OnDisplayChillReward(self, resultSet):
		if resultSet is None:
			logout.error('DisplayChillReward failed')
			return
		raw = {
			'qualified': 0,
			'achv': '',
			'recv': ''
		}
		for row in resultSet:  # 如果是空记录则表示不会走进来，是上行的结构，表示未触发奖励
			raw['achv'] = row[0]
			raw['recv'] = row[-1]
			if raw['recv'] == '-1':  # 字符串"-1"表示有资格未领取
				raw['qualified'] = 1
			else:
				raw['qualified'] = -1  # 已领取
		return raw
