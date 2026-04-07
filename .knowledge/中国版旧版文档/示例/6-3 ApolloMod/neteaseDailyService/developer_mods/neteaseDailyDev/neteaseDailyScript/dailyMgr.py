# -*- coding: utf-8 -*-

import apolloCommon.mysqlPool as mysqlPool
# import apolloCommon.redisPool as redisPool
import logout
import neteaseDailyScript.dailyConst as dailyConst
# import neteaseDailyScript.timermanager as timermanager
import time
import weakref
import json


class DailyMgr(object):
	"""
	该mod的service逻辑类
	接收并处理外部请求
	"""

	def __init__(self, system, moduleName):
		super(DailyMgr, self).__init__()
		self.mSystem = weakref.proxy(system)
		self.mModuleName = moduleName

		self.mSystem.RegisterRpcMethod(moduleName, dailyConst.DisplayDailyRewardEvent, self.OnDisplayDailyRewardReq)  # 打开界面
		self.mSystem.RegisterRpcMethod(moduleName, dailyConst.PlayerRecvEvent, self.OnPlayerRecvReq)  # 领取每日登录奖励
		self.mSystem.RegisterRpcMethod(moduleName, dailyConst.QueryPlayerRecvEvent, self.OnQueryPlayerRecvReq)  # master查询领取情况
		self.mSystem.RegisterRpcMethod(moduleName, 'DailyRollback', self.OnDailyRollbackReq)  # 领取回滚

	def Destroy(self):
		self.mSystem = None

	def DailyMgrRender(self, serverId, callbackId, data):
		respData = {
			'code': data['code'],
			'message': data.get('message', ''),
			'entity': data.get('entity', {})
		}
		self.mSystem.ResponseToServer(serverId, callbackId, respData)

	def OnDailyRollbackReq(self, serverId, callbackId, data):
		# 领取失败，领取返回时玩家空格不足，没有发放奖励
		uid = data.get('uid')
		date = data.get('date')
		if not uid or not date:
			self.mSystem.ResponseToServer(serverId, callbackId, {
				'code': dailyConst.RespCodeInvalidParameter,
				'message': 'OnDailyRollbackReq 参数有误 data: {}'.format(data)
			})
			return
		sql = 'DELETE FROM {} WHERE uid=%s AND recv_date=%s'.format(dailyConst.TableDailyReward)
		mysqlPool.AsyncExecuteWithOrderKey(
			'PLAYER_{}_ROLLBACK_DAILY_REWARD'.format(uid), sql, (uid, date),
			lambda rtn: self.OnDailyRollback(rtn, uid, date, serverId, callbackId))

	def OnDailyRollback(self, rtn, uid, date, serverId, callbackId):
		respData = {
			'code': dailyConst.RespCodeSuccess,
			'message': '请求成功',
			'entity': {'date': date}
		}
		if not rtn:
			# 回滚失败
			# 需要手动删除
			logout.error('玩家 {} 于日期 {} 领取每日签到奖励回滚失败'.format(uid, date))
			respData['code'] = dailyConst.RespCodeDBError
			respData['message'] = '数据库操作失败'
		else:
			logout.info('玩家 {} 于日期 {} 领取每日签到奖励回滚成功'.format(uid, date))
		self.mSystem.ResponseToServer(serverId, callbackId, respData)

	def OnQueryPlayerRecvReq(self, serverId, callbackId, data):
		"""
		查询玩家本周每日登录奖励领取情况
		"""
		uid = data.get('uid')
		if not uid:
			self.mSystem.ResponseToServer(serverId, callbackId, {
				'code': dailyConst.RespCodeInvalidParameter,
				'message': ''
			})
			return
		self.OnDisplayDailyRewardReq(serverId, callbackId, {'uid': uid, 'stamp': time.time()})  # 复用打开界面的逻辑

	def OnDisplayDailyRewardReq(self, serverId, callbackId, data):
		uid = data.get('uid')
		stamp = data.get('stamp')  # 服务端发来的日期，例如'1970-01-01'
		if not uid or not stamp:
			self.mSystem.ResponseToServer(serverId, callbackId, {
				'code': dailyConst.RespCodeInvalidParameter,
				'message': 'OnDisplayDailyRewardReq 参数有误 data: {}'.format(data)
			})
			return
		tm = time.localtime(stamp)
		w = tm.tm_wday + 1
		head, tail = (time.strftime('%Y-%m-%d', time.localtime(stamp - 86400 * (w - 1))), time.strftime('%Y-%m-%d', time.localtime(stamp + 86400 * (7 - w))))  # 本周的起止
		sql = 'SELECT recv_date FROM {} WHERE uid=%s AND (recv_date BETWEEN %s AND %s)'.format(dailyConst.TableDailyReward)
		mysqlPool.AsyncQueryWithOrderKey(
			'DISPLAY_PLAYER_{}_DAILY_REWARD'.format(uid), sql, (uid, head, tail),
			lambda resultSet: self.DisplayDailyReward(resultSet, uid, stamp, serverId, callbackId))

	def OnPlayerRecvReq(self, serverId, callbackId, data):
		uid = data.get('uid')
		date = data.get('date')
		if not uid or not date:
			self.mSystem.ResponseToServer(serverId, callbackId, {
				'code': dailyConst.RespCodeInvalidParameter,
				'message': 'OnPlayerRecvReq 参数有误 data: {}'.format(data)
			})
			return
		sql = 'SELECT recv_date FROM {} WHERE uid=%s AND recv_date=%s'.format(dailyConst.TableDailyReward)
		mysqlPool.AsyncQueryWithOrderKey(
			'PLAYER_{}_RECV_DAILY_REWARD'.format(uid), sql, (uid, date),
			lambda resultSet: self.OnGuaranteePlayerRecv(resultSet, uid, date, serverId, callbackId))

	def OnGuaranteePlayerRecv(self, resultSet, uid, date, serverId, callbackId):
		if resultSet is None:
			logout.error('玩家 uid: {} 于日期 {} 签到失败'.format(uid, date))
			self.mSystem.ResponseToServer(serverId, callbackId, {'code': dailyConst.RespCodeDBError, 'message': '数据库操作失败'})
			return
		if resultSet:
			logout.error('玩家 uid: {} 于日期 {} 签到失败'.format(uid, date))
			self.mSystem.ResponseToServer(serverId, callbackId, {
				'code': dailyConst.RespCodeDBError,
				'message': '已领取',
				'entity': {'date': date}
			})
			return
		sql = 'INSERT INTO {} (uid, recv_date) VALUES (%s, %s)'.format(dailyConst.TableDailyReward)
		mysqlPool.AsyncExecuteWithOrderKey(
			'PLAYER_{}_RECV_DAILY_REWARD'.format(uid), sql, (uid, date),
			lambda rtn: self.OnPlayerRecv(rtn, uid, date, serverId, callbackId))

	def OnPlayerRecv(self, rtn, uid, date, serverId, callbackId):
		respData = {
			'code': dailyConst.RespCodeSuccess,
			'message': '请求成功',
			'entity': {'date': date}
		}
		if not rtn:
			# 签到失败
			logout.error('玩家 uid: {} 于日期 {} 签到失败'.format(uid, date))
			respData['code'] = dailyConst.RespCodeDBError
			respData['message'] = '已领取'
			sql = 'SELECT recv_date FROM {} WHERE uid=%s AND recv_date=%s'.format(dailyConst.TableDailyReward)
			mysqlPool.AsyncQueryWithOrderKey(
				'PLAYER_{}_RECV_DAILY_REWARD'.format(uid), sql, (uid, date),
				lambda resultSet: (self.mSystem.ResponseToServer(serverId, callbackId, respData) if resultSet else self.mSystem.ResponseToServer(serverId, callbackId, {'code': dailyConst.RespCodeDBError, 'message': '数据库操作失败'})))
		else:
			self.mSystem.ResponseToServer(serverId, callbackId, respData)

	def DisplayDailyReward(self, resultSet, uid, stamp, serverId, callbackId):
		respData = {
			'code': dailyConst.RespCodeSuccess,
			'message': '请求成功',
		}
		data = self.OnDisplayDailyReward(resultSet)
		if data is None:
			respData['code'] = dailyConst.RespCodeDBError
			respData['message'] = '数据库操作失败'
		else:
			respData['entity'] = {
				'stamp': stamp,  # 要发回去当验证标识
				'recv': data
			}
		self.mSystem.ResponseToServer(serverId, callbackId, respData)

	def OnDisplayDailyReward(self, resultSet):
		if resultSet is None:
			logout.error('DisplayDailyReward failed')
			return
		raw = {i: 0 for i in range(7)}
		for row in resultSet:
			raw[(time.strptime(row[0], '%Y-%m-%d').tm_wday + 1) % 7] = 1  # 领取了的日期设置为1
		return raw
