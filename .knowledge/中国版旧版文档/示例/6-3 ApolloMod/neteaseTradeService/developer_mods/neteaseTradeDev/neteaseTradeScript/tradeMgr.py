# -*- coding: utf-8 -*-

import apolloCommon.mysqlPool as mysqlPool
# import apolloCommon.mongoPool as mongoPool
import logout
import neteaseTradeScript.tradeConst as tradeConst
import neteaseTradeScript.timermanager as timermanager
import apolloCommon.commonNetgameApi as commonNetgameApi
import time
import calendar
import weakref
import json

REFRESH_MODE_DAY = 1
REFRESH_MODE_WEEK = 2
REFRESH_MODE_MONTH = 3


class Doughs(dict):
	def __init__(self, uid, _system, server_list):
		self.uid = uid
		self._system = _system
		self.server_list = server_list
		super(Doughs, self).__init__(**{})

	def __setitem__(self, k, v):
		if k in self:
			for sid in self.server_list.copy():
				self._system.NotifyToServerNode(sid, 'PlayerDoughsUpdateEvent', {
					'uid': self.uid,
					'k': k,
					'dt': v - self[k]
				})
		super(Doughs, self).__setitem__(k, v)


class TradeMgr(object):
	def __init__(self, system, moduleName):
		super(TradeMgr, self).__init__()
		self.mSystem = weakref.proxy(system)
		self.mModuleName = moduleName
		self.mTradeInvolvedServers = set()
		self.mTradeData = {
			tradeConst.CfgKeyDoughs: {},
			tradeConst.CfgKeyGroceries: {},
			tradeConst.CfgKeyRefreshGroceries: {},
		}
		self.mAvailable = False
		self.mGroceryResetFlag = ()
		self.mGroceryRecentCustomers = set()
		# 检查刷新商店
		self.mRefreshGroceriesTimer = timermanager.timerManager.addTimer(4, self.CheckRefreshGroceries)
		# 保存购买记录
		self.mUpdateDealsTimer = timermanager.timerManager.addRepeatTimer(444, self.CheckUpdateDeals)

		self.mSystem.RegisterRpcMethod(moduleName, tradeConst.QueryPlayerDoughsEvent, self.OnQueryPlayerDoughsReq)
		self.mSystem.RegisterRpcMethod(moduleName, tradeConst.UpdatePlayerDoughsEvent, self.OnUpdatePlayerDoughsReq)
		self.mSystem.RegisterRpcMethod(moduleName, tradeConst.DisplayGroceryEvent, self.OnDisplayGroceryReq)
		self.mSystem.RegisterRpcMethod(moduleName, tradeConst.PlayerPurchaseEvent, self.OnPlayerPurchaseReq)
		self.mSystem.RegisterRpcMethod(moduleName, 'TradeRollback', self.OnTradeRollbackReq)

		self.mSaleData = {
			tradeConst.CfgKeyDealers: {},
			tradeConst.CfgKeySales: {}
		}
		self.mDeadlines = {}
		self.mSecondHand = 0
		self.mExpireStallsTimer = timermanager.timerManager.addRepeatTimer(1, self.CheckExpireStalls)

		self.mSystem.RegisterRpcMethod(moduleName, tradeConst.PlayerOpenStallEvent, self.OnPlayerOpenStallReq)
		self.mSystem.RegisterRpcMethod(moduleName, tradeConst.PlayerCloseStallEvent, self.OnPlayerCloseStallReq)
		self.mSystem.RegisterRpcMethod(moduleName, tradeConst.MerchOnSaleEvent, self.OnMerchOnSaleReq)
		self.mSystem.RegisterRpcMethod(moduleName, tradeConst.StallSaleUpdateEvent, self.OnStallSaleUpdateReq)
		self.mSystem.RegisterRpcMethod(moduleName, tradeConst.PlayerSpotMerchEvent, self.OnPlayerSpotMerchReq)
		self.mSystem.RegisterRpcMethod(moduleName, tradeConst.DisplayStallEvent, self.OnDisplayStallReq)
		self.mSystem.RegisterRpcMethod(moduleName, 'TradeSaleRollback', self.OnTradeSaleRollbackReq)
		self.mSystem.RegisterRpcMethod(moduleName, 'CountStallsEvent', self.OnCountStallsReq)
		self.mSystem.RegisterRpcMethod(moduleName, 'BatchCheckEvent', self.OnBatchCheckReq)

	def CheckExpireStalls(self):
		if not self.mDeadlines:
			return
		now = time.time()
		self.mSecondHand += 1
		outcasts = set()
		for uid in self.mDeadlines.pop(self.mSecondHand, []):
			deadline = self.mSaleData[tradeConst.CfgKeySales].get(uid, {}).get('deadline')
			if deadline:
				if now < deadline:
					self.mDeadlines.setdefault(self.mSecondHand + 1, []).append(uid)
				else:
					outcasts.add(uid)
					self.mSaleData[tradeConst.CfgKeySales].pop(uid, -1)
		if outcasts:
			for serverId in self.mTradeInvolvedServers.copy():
				self.mSystem.NotifyToServerNode(serverId, tradeConst.PlayerCloseStallEvent, {'outcasts': list(outcasts)})

	def Destroy(self):
		if self.mExpireStallsTimer:
			timermanager.timerManager.delTimer(self.mExpireStallsTimer)
			self.mExpireStallsTimer = None
		if self.mUpdateDealsTimer:
			timermanager.timerManager.delTimer(self.mUpdateDealsTimer)
			self.mUpdateDealsTimer = None
		if self.mRefreshGroceriesTimer:
			timermanager.timerManager.delTimer(self.mRefreshGroceriesTimer)
			self.mRefreshGroceriesTimer = None
		self.mSystem = None
		self.mTradeData.clear()
		self.mTradeData = None
		self.mGroceryRecentCustomers.clear()
		self.mGroceryRecentCustomers = None

	def TradeMgrRender(self, serverId, callbackId, data):
		respData = {
			'code': data['code'],
			'message': data.get('message', ''),
			'entity': data.get('entity', {})
		}
		self.mSystem.ResponseToServer(serverId, callbackId, respData)

	def OnTradeRollbackReq(self, serverId, callbackId, data):
		uid = data.get('uid')
		groceryId = data.get('groceryId')
		goodId = data.get('goodId')
		qty = data['qty']
		if not uid or not groceryId or not goodId:
			self.mSystem.ResponseToServer(serverId, callbackId, {
				'code': tradeConst.RespCodeInvalidParameter,
				'message': 'OnTradeRollbackReq 参数有误 data: {}'.format(data)
			})
			return
		grocery = self.mSystem.GetTradeCfg()[-1].get(groceryId)
		good = {good['good_id']: good for good in grocery['grocery_goods']}.get(goodId)

		mapping = {}
		for dough_id, demand in good['good_cost'].iteritems():
			if demand:
				mapping[dough_id] = demand

		if mapping:
			# self.mTradeData[tradeConst.CfgKeyDoughs][uid][good['good_dough']] += good['good_price']
			# self.UpdatePlayerDoughs(uid, {good['good_dough']: self.mTradeData[tradeConst.CfgKeyDoughs][uid][good['good_dough']]})
			doughs = self.mSystem.GetTradeCfg()[0]
			# doughId = good['good_dough']
			# if good['good_price'] < 0:
			# 	self.mTradeData[tradeConst.CfgKeyDoughs][uid][doughId] += good['good_price']
			# 	self.UpdatePlayerDoughs(uid, {doughId: self.mTradeData[tradeConst.CfgKeyDoughs][uid][doughId]})
			# elif self.mTradeData[tradeConst.CfgKeyDoughs][uid][doughId] < doughs[doughId]['dough_limit']:
			# 	if self.mTradeData[tradeConst.CfgKeyDoughs][uid][doughId] > doughs[doughId]['dough_limit'] - good['good_price']:
			# 		self.mTradeData[tradeConst.CfgKeyDoughs][uid][doughId] = doughs[doughId]['dough_limit']
			# 	else:
			# 		self.mTradeData[tradeConst.CfgKeyDoughs][uid][doughId] += good['good_price']
			# 	self.UpdatePlayerDoughs(uid, {doughId: self.mTradeData[tradeConst.CfgKeyDoughs][uid][doughId]})

			for doughId, demand in mapping.iteritems():
				if demand < 0:
					self.mTradeData[tradeConst.CfgKeyDoughs][uid][doughId] += demand
				elif self.mTradeData[tradeConst.CfgKeyDoughs][uid][doughId] < doughs[doughId]['dough_limit']:
					if self.mTradeData[tradeConst.CfgKeyDoughs][uid][doughId] > doughs[doughId]['dough_limit'] - demand:
						self.mTradeData[tradeConst.CfgKeyDoughs][uid][doughId] = doughs[doughId]['dough_limit']
					else:
						self.mTradeData[tradeConst.CfgKeyDoughs][uid][doughId] += demand
			self.UpdatePlayerDoughs(uid, {doughId: self.mTradeData[tradeConst.CfgKeyDoughs][uid][doughId] for doughId in mapping})
		if self.mGroceryResetFlag in self.mTradeData[tradeConst.CfgKeyGroceries].get(uid, {}).get(groceryId, {}):
			self.mTradeData[tradeConst.CfgKeyGroceries].setdefault(uid, {})[groceryId] = {}
		else:
			bought = self.mTradeData[tradeConst.CfgKeyGroceries].setdefault(uid, {}).setdefault(groceryId, {})
			bought[goodId] = bought.setdefault(goodId, 0) - qty
		# 回滚成功
		# 除非货币更新失败
		respData = {
			'code': tradeConst.RespCodeSuccess,
			'message': '请求成功',
		}
		self.mSystem.ResponseToServer(serverId, callbackId, respData)

	def OnQueryPlayerDoughsReq(self, serverId, callbackId, data):
		"""
		查询玩家所有持有的货币信息
		"""
		uid = data.get('uid')
		void = bool(data.get('void'))  # 不需要返回数据
		if not uid:
			self.mSystem.ResponseToServer(serverId, callbackId, {
				'code': tradeConst.RespCodeInvalidParameter,
				'message': ''
			})
			return
		self.mTradeInvolvedServers.add(serverId)
		if uid not in self.mTradeData[tradeConst.CfgKeyDoughs]:
			if not data.get('activate'):
				self.mSystem.ResponseToServer(serverId, callbackId, {
					'code': tradeConst.RespCodeInvalidUser,
					'message': '用户不存在或不在线'
				})
				return
			# 查数据库
			self.PreQueryPlayerDoughs(uid, serverId, callbackId, void)
		else:
			# 内存为准
			respData = {
				'code': tradeConst.RespCodeSuccess,
				'message': '请求成功',
			}
			if not void:
				respData['entity'] = dict(self.mTradeData[tradeConst.CfgKeyDoughs][uid])
			self.mSystem.ResponseToServer(serverId, callbackId, respData)

	def OnUpdatePlayerDoughsReq(self, serverId, callbackId, data):
		uid = data.get('uid')
		mod = data.get('mod')
		if not uid or not mod or not isinstance(mod, dict):
			self.mSystem.ResponseToServer(serverId, callbackId, {
				'code': tradeConst.RespCodeInvalidParameter,
				'message': ''
			})
			return
		if uid not in self.mTradeData[tradeConst.CfgKeyDoughs]:
			self.mSystem.ResponseToServer(serverId, callbackId, {
				'code': tradeConst.RespCodeInvalidUser,
				'message': '用户不存在或不在线'
			})
			return
		respData = {
			'code': tradeConst.RespCodeSuccess,
			'message': '请求成功',
		}
		doughs = self.mSystem.GetTradeCfg()[0]
		for doughId, v in mod.iteritems():
			if doughId not in doughs:
				respData['code'] = tradeConst.RespCodeInvalidParameter
				respData['message'] = '货币类型 {} 无效'.format(doughId)
				self.mSystem.ResponseToServer(serverId, callbackId, respData)
				return
			if not isinstance(v, int):
				respData['code'] = tradeConst.RespCodeInvalidParameter
				respData['message'] = '数据 {}: {} 不合法'.format(doughId, v)
				self.mSystem.ResponseToServer(serverId, callbackId, respData)
				return
			if doughId not in self.mTradeData[tradeConst.CfgKeyDoughs][uid]:
				logout.error('玩家 uid: {} 的货币数据 {} 中没有货币类型 {} 的值'.format(uid, self.mTradeData[tradeConst.CfgKeyDoughs], doughId))  # TODO
				return
		changes = []
		for doughId, v in mod.iteritems():
			# if self.mTradeData[tradeConst.CfgKeyDoughs][uid][doughId] < doughs[doughId]['dough_limit'] or v < 0:
			# 	changes.append(doughId)
			# 	self.mTradeData[tradeConst.CfgKeyDoughs][uid][doughId] += v
			# 	if self.mTradeData[tradeConst.CfgKeyDoughs][uid][doughId] > doughs[doughId]['dough_limit']:
			# 		self.mTradeData[tradeConst.CfgKeyDoughs][uid][doughId] = doughs[doughId]['dough_limit']
			if v < 0:
				changes.append(doughId)
				self.mTradeData[tradeConst.CfgKeyDoughs][uid][doughId] += v
			elif v > 0 and self.mTradeData[tradeConst.CfgKeyDoughs][uid][doughId] < doughs[doughId]['dough_limit']:
				changes.append(doughId)
				if self.mTradeData[tradeConst.CfgKeyDoughs][uid][doughId] > doughs[doughId]['dough_limit'] - v:
					self.mTradeData[tradeConst.CfgKeyDoughs][uid][doughId] = doughs[doughId]['dough_limit']
				else:
					self.mTradeData[tradeConst.CfgKeyDoughs][uid][doughId] += v
		respData['entity'] = dict(self.mTradeData[tradeConst.CfgKeyDoughs][uid])
		self.mSystem.ResponseToServer(serverId, callbackId, respData)
		if changes:
			self.UpdatePlayerDoughs(uid, {doughId: self.mTradeData[tradeConst.CfgKeyDoughs][uid][doughId] for doughId in changes})

	def OnDisplayGroceryReq(self, serverId, callbackId, data):
		uid = data.get('uid')
		groceryId = data.get('groceryId')
		if not uid or not groceryId:
			self.mSystem.ResponseToServer(serverId, callbackId, {
				'code': tradeConst.RespCodeInvalidParameter,
				'message': 'OnDisplayGroceryReq 参数有误 data: {}'.format(data)
			})
			return
		grocery = self.mSystem.GetTradeCfg()[-1].get(groceryId)
		if not grocery:
			self.mSystem.ResponseToServer(serverId, callbackId, {
				'code': tradeConst.RespCodeInvalidParameter,
				'message': 'OnDisplayGroceryReq 不存在的商店 groceryId: {}'.format(groceryId)
			})
			return
		if groceryId not in self.mTradeData[tradeConst.CfgKeyGroceries].get(uid, {}):
			self.PreDisplayGrocery(uid, groceryId, serverId, callbackId)
		else:
			if self.mGroceryResetFlag in self.mTradeData[tradeConst.CfgKeyGroceries][uid][groceryId]:
				self.mTradeData[tradeConst.CfgKeyGroceries][uid][groceryId] = {}
			# 内存为准
			respData = {
				'code': tradeConst.RespCodeSuccess,
				'message': '请求成功',
				'entity': {
					'grocery': grocery,
					'bought': self.mTradeData[tradeConst.CfgKeyGroceries][uid][groceryId],
					'doughs': {doughId: self.mTradeData[tradeConst.CfgKeyDoughs].get(uid, {}).get(doughId) for doughId in grocery['grocery_doughs']},
					'icons': {doughId: self.mSystem.GetTradeCfg()[0].get(doughId, {}).get('dough_icon') for doughId in grocery['grocery_doughs']}
				}
			}
			self.mSystem.ResponseToServer(serverId, callbackId, respData)

	def OnPlayerPurchaseReq(self, serverId, callbackId, data):
		uid = data.get('uid')
		groceryId = data.get('groceryId')
		goodId = data.get('goodId')
		qty = data['qty']
		if not uid or not groceryId or not goodId:
			self.mSystem.ResponseToServer(serverId, callbackId, {
				'code': tradeConst.RespCodeInvalidParameter,
				'message': 'OnPlayerPurchaseReq 参数有误 data: {}'.format(data)
			})
			return
		grocery = self.mSystem.GetTradeCfg()[-1].get(groceryId)
		if not grocery:
			self.mSystem.ResponseToServer(serverId, callbackId, {
				'code': tradeConst.RespCodeInvalidParameter,
				'message': 'OnPlayerPurchaseReq 不存在的商店 groceryId: {}'.format(groceryId)
			})
			return
		good = {good['good_id']: good for good in grocery['grocery_goods']}.get(goodId)
		if not good:
			self.mSystem.ResponseToServer(serverId, callbackId, {
				'code': tradeConst.RespCodeInvalidParameter,
				'message': 'OnPlayerPurchaseReq 不存在的商品 {}-{}'.format(groceryId, goodId)
			})
			return
		if self.mGroceryResetFlag in self.mTradeData[tradeConst.CfgKeyGroceries].get(uid, {}).get(groceryId, {}):
			self.mTradeData[tradeConst.CfgKeyGroceries].setdefault(uid, {})[groceryId] = {}
		if self.mTradeData[tradeConst.CfgKeyGroceries].get(uid, {}).get(groceryId, {}).get(goodId, 0) >= good.get('good_limit', float('nan')):
			logout.warning('玩家 uid: {} 购买商品 {}-{} 次数 {} 达到上限 {} 次数'.format(uid, groceryId, goodId, self.mTradeData[tradeConst.CfgKeyGroceries].get(uid, {}).get(groceryId, {}).get(goodId, 0), good['good_limit']))
			return

		mapping = {}
		for dough_id, demand in good['good_cost'].iteritems():
			if demand:
				if qty > 1:
					demand *= qty
				balance = self.mTradeData[tradeConst.CfgKeyDoughs].get(uid, {}).get(dough_id)
				if balance is None:
					logout.error('玩家 uid: {} 购买商品 {}-{} 货币 {} 异常'.format(uid, groceryId, goodId, dough_id))
					return
				if balance < demand:
					logout.warning(
						'玩家 uid: {} 购买商品 {}-{} 货币 {} 售价 {} 余额 {} 不足'.format(uid, groceryId, goodId, dough_id, demand, balance))
					self.mSystem.ResponseToServer(serverId, callbackId, {
						'code': tradeConst.RespCodeInvalidUser,
						'message': '余额不足'
					})
					return
				mapping[dough_id] = demand

		# balance = self.mTradeData[tradeConst.CfgKeyDoughs].get(uid, {}).get(good['good_dough'])
		# if balance is None:
		# 	logout.error('玩家 uid: {} 购买商品 {}-{} 货币 {} 异常'.format(uid, groceryId, goodId, good['good_dough']))
		# 	return
		# if balance < good['good_price']:
		# 	logout.warning('玩家 uid: {} 购买商品 {}-{} 货币 {} 售价 {} 余额 {} 不足'.format(uid, groceryId, goodId, good['good_dough'], good['good_price'], balance))
		# 	self.mSystem.ResponseToServer(serverId, callbackId, {
		# 		'code': tradeConst.RespCodeInvalidUser,
		# 		'message': '余额不足'
		# 	})
		# 	return
		# 至此应该是可以购买了
		# if good['good_price']:
		if mapping:
			# self.mTradeData[tradeConst.CfgKeyDoughs][uid][good['good_dough']] -= good['good_price']
			# self.UpdatePlayerDoughs(uid, {good['good_dough']: self.mTradeData[tradeConst.CfgKeyDoughs][uid][good['good_dough']]})
			doughs = self.mSystem.GetTradeCfg()[0]
			# doughId = good['good_dough']
			for doughId, demand in mapping.iteritems():
				if demand > 0:
					self.mTradeData[tradeConst.CfgKeyDoughs][uid][doughId] -= demand
				elif self.mTradeData[tradeConst.CfgKeyDoughs][uid][doughId] < doughs[doughId]['dough_limit']:
					if self.mTradeData[tradeConst.CfgKeyDoughs][uid][doughId] > doughs[doughId]['dough_limit'] + demand:
						self.mTradeData[tradeConst.CfgKeyDoughs][uid][doughId] = doughs[doughId]['dough_limit']
					else:
						self.mTradeData[tradeConst.CfgKeyDoughs][uid][doughId] -= demand
			self.UpdatePlayerDoughs(uid, {doughId: self.mTradeData[tradeConst.CfgKeyDoughs][uid][doughId] for doughId in mapping})
		bought = self.mTradeData[tradeConst.CfgKeyGroceries].setdefault(uid, {}).setdefault(groceryId, {})
		bought[goodId] = bought.setdefault(goodId, 0) + qty
		self.mGroceryRecentCustomers.add(uid)
		# self.DisplayGrocery(uid, groceryId, serverId, callbackId)
		if self.mGroceryResetFlag in self.mTradeData[tradeConst.CfgKeyGroceries].get(uid, {}).get(groceryId, {}):
			self.mTradeData[tradeConst.CfgKeyGroceries].setdefault(uid, {})[groceryId] = {}
		# 内存为准
		respData = {
			'code': tradeConst.RespCodeSuccess,
			'message': '请求成功',
			'entity': {
				'bought': self.mTradeData[tradeConst.CfgKeyGroceries][uid][groceryId],
				'doughs': {doughId: self.mTradeData[tradeConst.CfgKeyDoughs].get(uid, {}).get(doughId) for doughId in grocery['grocery_doughs']},
				'item': {good['good_item_id']: good['good_item_count']},
				'groceryId': groceryId,
				'goodId': goodId,
				'qty': qty
			}
		}
		self.mSystem.ResponseToServer(serverId, callbackId, respData)
		logout.info('玩家 uid: {} 购买商品 {}-{} 成功'.format(uid, groceryId, goodId))  # TODO

	def PreQueryPlayerDoughs(self, uid, serverId, callbackId, void=False):
		sql = 'SELECT dough_id, balance FROM {} WHERE uid=%s'.format(tradeConst.TableTradeDough)
		mysqlPool.AsyncQueryWithOrderKey(
			'QUERY_PLAYER_%s_DOUGHS' % uid, sql, (uid,), lambda resultSet: self.QueryPlayerDoughs(resultSet, uid, serverId, callbackId, void))

	def QueryPlayerDoughs(self, resultSet, uid, serverId, callbackId, void=False):
		respData = {
			'code': tradeConst.RespCodeSuccess,
			'message': '请求成功',
		}
		data = self.OnQueryPlayerDoughs(resultSet, uid)
		if data is None:
			respData['code'] = tradeConst.RespCodeDBError
			respData['message'] = '数据库操作失败'
		elif not void:
			respData['entity'] = data
		self.mSystem.ResponseToServer(serverId, callbackId, respData)

	def OnQueryPlayerDoughs(self, resultSet, uid):
		if resultSet is None:
			logout.error('QueryPlayerDoughs failed')
			return
		doughs = self.mSystem.GetTradeCfg()[0].copy()
		for row in resultSet:
			doughId = row[0]
			if doughId in doughs:
				if doughId not in self.mTradeData[tradeConst.CfgKeyDoughs].setdefault(uid, Doughs(uid, self.mSystem, self.mTradeInvolvedServers)):
					# 当前配置有效且内存没有才更新
					self.mTradeData[tradeConst.CfgKeyDoughs][uid][doughId] = int(row[-1])
				doughs.pop(doughId)
		for k, v in doughs.iteritems():
			# 可能有新的种类
			if k not in self.mTradeData[tradeConst.CfgKeyDoughs].setdefault(uid, Doughs(uid, self.mSystem, self.mTradeInvolvedServers)):
				self.mTradeData[tradeConst.CfgKeyDoughs][uid][k] = v['dough_default']
		return self.mTradeData[tradeConst.CfgKeyDoughs].setdefault(uid, Doughs(uid, self.mSystem, self.mTradeInvolvedServers))

	def UpdatePlayerDoughs(self, uid, doughs, cb=None):
		"""
		更新玩家货币
		"""
		if not doughs or not isinstance(doughs, dict):
			logout.warning('invalid arg doughs: {}'.format(doughs))
			return
		sql = 'INSERT INTO {} (uid, dough_id, balance) VALUES (%s, %s, %s) ON DUPLICATE KEY UPDATE balance = VALUES(balance)'.format(tradeConst.TableTradeDough)
		mysqlPool.AsyncExecutemanyWithOrderKey(
			'UPDATE_PLAYER_%s_DOUGHS' % uid, sql, [(uid, doughId, str(balance)) for doughId, balance in doughs.iteritems()], cb or (lambda rtn: self.OnUpdatePlayerDoughs(rtn)))

	def OnUpdatePlayerDoughs(self, rtn):
		if not rtn:
			# 严重问题
			logout.error('UpdatePlayerDoughs failed')

	def UpdateDeals(self, deals, cb=None):
		"""
		更新玩家购买记录
		"""
		if not deals or not isinstance(deals, list):
			logout.warning('invalid arg deals: {}'.format(deals))
			return
		sql = 'INSERT INTO {} (uid, grocery_id, good_id, bought) VALUES (%s, %s, %s, %s) ON DUPLICATE KEY UPDATE bought = VALUES(bought)'.format(tradeConst.TableTradeGrocery)
		mysqlPool.AsyncExecutemanyWithOrderKey(
			'TRADE_UPDATE_DEALS', sql, deals, cb or (lambda rtn: self.OnUpdateDeals(rtn)))

	def OnUpdateDeals(self, rtn):
		if not rtn:
			# 严重问题
			logout.error('UpdateDeals failed')

	def PreDisplayGrocery(self, uid, groceryId, serverId, callbackId):
		if uid not in self.mTradeData[tradeConst.CfgKeyDoughs]:
			sql = 'SELECT dough_id, balance FROM {} WHERE uid=%s'.format(tradeConst.TableTradeDough)
			mysqlPool.AsyncQueryWithOrderKey(
				'DISPLAY_PLAYER_{}_GROCERY_{}'.format(uid, groceryId), sql, (uid,),
				lambda resultSet: self.OnQueryPlayerDoughs(resultSet, uid))
		sql = 'SELECT good_id, bought FROM {} WHERE uid=%s AND grocery_id=%s'.format(tradeConst.TableTradeGrocery)
		mysqlPool.AsyncQueryWithOrderKey(
			'DISPLAY_PLAYER_{}_GROCERY_{}'.format(uid, groceryId), sql, (uid, groceryId),
			lambda resultSet: self.DisplayGrocery(resultSet, uid, groceryId, serverId, callbackId))

	def DisplayGrocery(self, resultSet, uid, groceryId, serverId, callbackId):
		respData = {
			'code': tradeConst.RespCodeSuccess,
			'message': '请求成功',
		}
		data = self.OnDisplayGrocery(resultSet, uid, groceryId)
		if data is None:
			respData['code'] = tradeConst.RespCodeDBError
			respData['message'] = '数据库操作失败'
		else:
			respData['entity'] = {
				'grocery': data[0],
				'bought': data[-1],
				'doughs': {doughId: self.mTradeData[tradeConst.CfgKeyDoughs].get(uid, {}).get(doughId) for doughId in data[0]['grocery_doughs']},
				'icons': {doughId: self.mSystem.GetTradeCfg()[0].get(doughId, {}).get('dough_icon') for doughId in data[0]['grocery_doughs']}
			}
		self.mSystem.ResponseToServer(serverId, callbackId, respData)

	def OnDisplayGrocery(self, resultSet, uid, groceryId):
		if resultSet is None:
			logout.error('DisplayGrocery failed')
			return
		grocery = self.mSystem.GetTradeCfg()[-1][groceryId]
		if self.mGroceryResetFlag in self.mTradeData[tradeConst.CfgKeyGroceries].get(uid, {}).get(groceryId, {}):
			self.mTradeData[tradeConst.CfgKeyGroceries].setdefault(uid, {})[groceryId] = {}
		elif resultSet:
			goods = {good['good_id'] for good in grocery['grocery_goods']}
			for row in resultSet:
				goodId = row[0]
				if goodId in goods and goodId not in self.mTradeData[tradeConst.CfgKeyGroceries].setdefault(uid, {}).setdefault(groceryId, {}):
					# 当前配置有效且内存没有才更新
					self.mTradeData[tradeConst.CfgKeyGroceries][uid][groceryId][goodId] = row[-1]
		return grocery, self.mTradeData[tradeConst.CfgKeyGroceries].setdefault(uid, {}).setdefault(groceryId, {})

	def CheckUpdateDeals(self):
		if self.mGroceryRecentCustomers:
			deals = []
			customers = list(self.mGroceryRecentCustomers)
			for uid in customers:
				self.mGroceryRecentCustomers.discard(uid)
				data = self.mTradeData[tradeConst.CfgKeyGroceries].get(uid, {})
				for groceryId in data.keys():
					bought = data.get(groceryId, {}).copy()
					if self.mGroceryResetFlag in bought:
						self.mTradeData[tradeConst.CfgKeyGroceries].setdefault(uid, {})[groceryId] = {}
						continue
					for k, v in bought.iteritems():
						deals.append((uid, groceryId, k, v))
			if deals:
				self.UpdateDeals(deals)

	# def CheckRefreshGroceries(self, now=None, date=None):
	def CheckRefreshGroceries(self):
		if self.mTradeData[tradeConst.CfgKeyRefreshGroceries]:
			# if now is None:
			# 	now = calendar.datetime.datetime.now()
			# if date is None:
			# 	date = time.strftime('%Y-%m-%d')
			now = calendar.datetime.datetime.now()
			date = time.strftime('%Y-%m-%d')
			args = []
			for groceryId in self.mTradeData[tradeConst.CfgKeyRefreshGroceries].keys():
				if self.mTradeData[tradeConst.CfgKeyRefreshGroceries][groceryId] == date:
					grocery = self.mSystem.GetTradeCfg()[-1][groceryId]
					policy = grocery['grocery_update_policy']
					s = time.mktime(time.strptime(date, '%Y-%m-%d'))
					if policy == REFRESH_MODE_DAY:
						if now.hour >= int(grocery['grocery_update_time']):
							args.append((groceryId, date))
							self.mTradeData[tradeConst.CfgKeyRefreshGroceries][groceryId] = time.strftime('%Y-%m-%d', time.localtime(s + 86400))
					elif policy == REFRESH_MODE_WEEK:
						w, h = map(lambda x: int(x), grocery['grocery_update_time'].split('-'))
						if now.hour >= h:
							args.append((groceryId, date))
							self.mTradeData[tradeConst.CfgKeyRefreshGroceries][groceryId] = time.strftime('%Y-%m-%d', time.localtime(s + 86400 * 7))
					elif policy == REFRESH_MODE_MONTH:
						m, h = map(lambda x: int(x), grocery['grocery_update_time'].split('-'))
						if now.hour >= h:
							args.append((groceryId, date))
							follow = now.month > 11 and [now.year + 1, 1] or [now.year, now.month + 1]
							follow.append(min(m, calendar.monthrange(*follow)[-1]))
							follow = time.strptime('{}-{}-{}'.format(*follow), '%Y-%m-%d')
							self.mTradeData[tradeConst.CfgKeyRefreshGroceries][groceryId] = time.strftime('%Y-%m-%d', follow)
				else:
					# 理论上不会出现因过点导致判断不到的情况
					# TODO: 只能往后不能往前
					pass
			if args:
				self.RefreshGroceries(tuple(t[0] for t in args))
				sql = 'INSERT INTO {} (grocery_id, last_reset_date) VALUES (%s, %s) ON DUPLICATE KEY UPDATE last_reset_date = VALUES(last_reset_date)'.format(tradeConst.TableTradeGroceryRefresh)
				mysqlPool.AsyncExecutemanyWithOrderKey(
					'TRADE_REFRESH_GROCERIES', sql, args, lambda rtn: self.OnRefreshGroceries(rtn))
		elif self.mAvailable:
			logout.error('已加载过数据库数据但依旧没有数据')  # TODO
		else:
			sql = 'SELECT grocery_id, last_reset_date FROM {}'.format(tradeConst.TableTradeGroceryRefresh)
			mysqlPool.AsyncQueryWithOrderKey('CHECK_REFRESH_GROCERIES', sql, (), self.OnCheckRefreshGroceries)
		# if self.mRefreshGroceriesTimer:
		# 	timermanager.timerManager.delTimer(self.mRefreshGroceriesTimer)
		# 	self.mRefreshGroceriesTimer = None
		self.mRefreshGroceriesTimer = timermanager.timerManager.addTimer((60 - calendar.datetime.datetime.now().minute) * 60, self.CheckRefreshGroceries)

	def OnCheckRefreshGroceries(self, resultSet):
		if resultSet is None:
			logout.error('CheckRefreshGroceries failed')
			return
		groceries = self.mSystem.GetTradeCfg()[-1]
		raw = {}
		now = calendar.datetime.datetime.now()
		date = time.strftime('%Y-%m-%d')
		for row in resultSet:
			groceryId = row[0]
			if groceryId in groceries:
				# 可能需要刷新
				follow = time.strptime(row[-1], '%Y-%m-%d')
				grocery = groceries[groceryId]
				policy = grocery['grocery_update_policy']
				stamp = time.mktime(follow)
				if policy == REFRESH_MODE_DAY:
					follow = time.localtime(stamp + 86400)
				elif policy == REFRESH_MODE_WEEK:
					w = int(grocery['grocery_update_time'].split('-')[0])
					follow = time.localtime(stamp + 86400 * ((w - (follow.tm_wday + 1) % 7) if w > (follow.tm_wday + 1) % 7 else (7 + w - (follow.tm_wday + 1) % 7)))
				elif policy == REFRESH_MODE_MONTH:
					m = int(grocery['grocery_update_time'].split('-')[0])
					year, month = follow.tm_year, follow.tm_mon
					if follow.tm_mday < min(m, calendar.monthrange(year, month)[-1]):
						year, month = month < 2 and (year - 1, 12) or (year, month - 1)
					follow = month > 11 and [year + 1, 1] or [year, month + 1]
					follow.append(min(m, calendar.monthrange(*follow)[-1]))
					follow = time.strptime('{}-{}-{}'.format(*follow), '%Y-%m-%d')
				elif policy == 0:
					continue
				else:
					logout.error('商店类型 {} 刷新策略配置有误'.format(groceryId))  # TODO
					continue
				raw[groceryId] = follow
		args = []
		for groceryId, grocery in groceries.iteritems():
			if not raw.get(groceryId) or time.strptime(date, '%Y-%m-%d') > raw[groceryId] or date == time.strftime('%Y-%m-%d', raw[groceryId]):
				# 现在日期大于等于更新日期
				same = groceryId in raw and date == time.strftime('%Y-%m-%d', raw[groceryId])
				s = time.mktime(time.strptime(date, '%Y-%m-%d'))
				policy = grocery['grocery_update_policy']
				if policy == REFRESH_MODE_DAY:
					if now.hour >= int(grocery['grocery_update_time']):
						# 今天都过点了
						raw[groceryId] = time.strftime('%Y-%m-%d', time.localtime(s + 86400))
						args.append((groceryId, date))
					else:
						raw[groceryId] = date
						if not same:
							pseudo = time.strftime('%Y-%m-%d', time.localtime(s - 86400))
							args.append((groceryId, pseudo))
				elif policy == REFRESH_MODE_WEEK:
					w, h = map(lambda x: int(x), grocery['grocery_update_time'].split('-'))
					follow = raw.get(groceryId)
					if w == now.isoweekday() % 7:
						# 今天要刷
						if now.hour >= h:
							# 今天都过点了
							raw[groceryId] = time.strftime('%Y-%m-%d', time.localtime(s + 86400 * 7))
							args.append((groceryId, date))
						else:
							if follow:
								raw[groceryId] = date
								if not same:
									pseudo = time.strftime('%Y-%m-%d', time.localtime(s - 86400))
									args.append((groceryId, pseudo))
							else:
								# 直接刷
								raw[groceryId] = time.strftime('%Y-%m-%d', time.localtime(s + 86400 * 7))
								args.append((groceryId, date))
					else:
						# 说明不可能是同一天
						# if not follow:
						# 	pass
						# else:
						# 	pseudo = date
						# 	raw[groceryId] = time.strftime('%Y-%m-%d', time.localtime(s + 86400 * (w - now.isoweekday() % 7 if w > now.isoweekday() % 7 else 7 + w - now.isoweekday() % 7)))
						# 	# args.append((groceryId, time.strftime('%Y-%m-%d', time.localtime(s - 86400 * (7 - w + now.isoweekday() % 7 if w > now.isoweekday() % 7 else now.isoweekday() % 7 - w)))))
						# 	args.append((groceryId, pseudo))
						pseudo = date
						raw[groceryId] = time.strftime('%Y-%m-%d', time.localtime(s + 86400 * ((w - now.isoweekday() % 7) if w > now.isoweekday() % 7 else (7 + w - now.isoweekday() % 7))))
						args.append((groceryId, pseudo))
				elif policy == REFRESH_MODE_MONTH:
					m, h = map(lambda x: int(x), grocery['grocery_update_time'].split('-'))
					follow = raw.get(groceryId)
					if now.day == min(m, calendar.monthrange(now.year, now.month)[-1]):
						# 今天要刷
						if now.hour >= h:
							# 今天都过点了
							follow = now.month > 11 and [now.year + 1, 1] or [now.year, now.month + 1]
							follow.append(min(m, calendar.monthrange(*follow)[-1]))
							follow = time.strptime('{}-{}-{}'.format(*follow), '%Y-%m-%d')
							raw[groceryId] = time.strftime('%Y-%m-%d', follow)
							args.append((groceryId, date))
						else:
							if follow:
								raw[groceryId] = date
								if not same:
									pseudo = time.strftime('%Y-%m-%d', time.localtime(s - 86400))
									args.append((groceryId, pseudo))
							else:
								# 直接刷
								follow = now.month > 11 and [now.year + 1, 1] or [now.year, now.month + 1]
								follow.append(min(m, calendar.monthrange(*follow)[-1]))
								follow = time.strptime('{}-{}-{}'.format(*follow), '%Y-%m-%d')
								raw[groceryId] = time.strftime('%Y-%m-%d', follow)
								args.append((groceryId, date))
					else:
						# 说明不可能是同一天
						# if not follow:
						# 	pass
						# else:
						# 	pseudo = date
						# 	if now.day < min(m, calendar.monthrange(now.year, now.month)[-1]):
						# 		follow = [now.year, now.month]
						# 	else:
						# 		follow = now.month > 11 and [now.year + 1, 1] or [now.year, now.month + 1]
						# 	follow.append(min(m, calendar.monthrange(*follow)[-1]))
						# 	follow = time.strptime('{}-{}-{}'.format(*follow), '%Y-%m-%d')
						# 	raw[groceryId] = time.strftime('%Y-%m-%d', follow)
						# 	args.append((groceryId, pseudo))
						pseudo = date
						if now.day < min(m, calendar.monthrange(now.year, now.month)[-1]):
							# 这个月还有这一天
							follow = [now.year, now.month]
						else:
							follow = now.month > 11 and [now.year + 1, 1] or [now.year, now.month + 1]
						follow.append(min(m, calendar.monthrange(*follow)[-1]))
						follow = time.strptime('{}-{}-{}'.format(*follow), '%Y-%m-%d')
						raw[groceryId] = time.strftime('%Y-%m-%d', follow)
						args.append((groceryId, pseudo))
				elif policy == 0:
					continue
				else:
					logout.error('商店类型 {} 刷新策略配置有误'.format(groceryId))  # TODO
					continue
			else:
				raw[groceryId] = time.strftime('%Y-%m-%d', raw[groceryId])
		if args:
			self.RefreshGroceries(tuple(t[0] for t in args))
			sql = 'INSERT INTO {} (grocery_id, last_reset_date) VALUES (%s, %s) ON DUPLICATE KEY UPDATE last_reset_date = VALUES(last_reset_date)'.format(tradeConst.TableTradeGroceryRefresh)
			mysqlPool.AsyncExecutemanyWithOrderKey(
				'TRADE_REFRESH_GROCERIES', sql, args, lambda rtn: self.OnRefreshGroceries(rtn))
		self.mTradeData[tradeConst.CfgKeyRefreshGroceries] = raw
		self.mAvailable = True

	def RefreshGroceries(self, groceries):
		"""
		刷新商店限购
		"""
		if not groceries or not (isinstance(groceries, list) or isinstance(groceries, tuple)):
			logout.warning('invalid arg groceries: {}'.format(groceries))
			return
		sql = 'DELETE FROM {} WHERE grocery_id=%s'.format(tradeConst.TableTradeGrocery)
		for i in xrange(1, len(groceries)):
			sql += ' OR grocery_id=%s'
		print 'RefreshGroceries', sql, groceries
		mysqlPool.AsyncExecuteWithOrderKey(
			'TRADE_REFRESH_GROCERIES', sql, tuple(groceries), lambda rtn: self.OnRefreshGroceries(rtn))
		for uid in self.mTradeData[tradeConst.CfgKeyGroceries].keys():
			for groceryId in groceries:
				self.mTradeData[tradeConst.CfgKeyGroceries].get(uid, {}).setdefault(groceryId, {})[self.mGroceryResetFlag] = True

	def OnRefreshGroceries(self, rtn):
		if not rtn:
			logout.error('RefreshGroceries failed')

	def OnDisplayStallReq(self, serverId, callbackId, data):
		uid = data.get('uid')
		owner = data.get('owner')
		name = data.get('name', '神秘人')
		if owner in self.mSaleData[tradeConst.CfgKeySales] and time.time() >= self.mSaleData[tradeConst.CfgKeySales][owner]['deadline']:
			self.mSaleData[tradeConst.CfgKeySales].pop(owner, -1)
		if not (owner in self.mSaleData[tradeConst.CfgKeySales] or uid == owner):
			self.mSystem.ResponseToServer(serverId, callbackId, {
				'code': tradeConst.RespCodeInvalidUser,
				'message': '该摊位尚未开张',
				'entity': {
					'uid': uid,
				}
			})
			return
		self.mSaleData[tradeConst.CfgKeyDealers].setdefault(uid, {}).clear()
		self.mSaleData[tradeConst.CfgKeyDealers][uid].update({'uid': uid, 'name': name, 'serverId': serverId})
		mysqlPool.AsyncExecuteFunctionWithOrderKey(
			self.Find,
			'PLAYER_%s_S' % uid,
			lambda rows: self.mSystem.ResponseToServer(serverId, callbackId, {
				'code': tradeConst.RespCodeSuccess,
				'message': '',
				'entity': {
					'time': int(time.time()),
					'uid': uid,
					'owner': owner,
					'stall': self.mSaleData[tradeConst.CfgKeySales].get(owner, 0),
					'rules': self.mSystem.GetSaleRules() or 0,
					'merchs': (lambda rows: [{
						'_id': row[0],
						'currency': self.mSystem.GetTradeCfg()[0].get(row[1], {}).get('dough_icon'),
						'unit': row[2], 'qty': row[3], 'init': row[-2],
						'stuff': row[-1]
					} for row in rows])(rows)
				}
			}),
			'SELECT _id, currency, unit, qty, init, stuff FROM {} WHERE uid=%s'.format(tradeConst.TableTradeSaleMerch),
			(owner,)
		)

	def OnPlayerOpenStallReq(self, serverId, callbackId, data):
		uid = data.get('uid')
		duration = data.get('duration')
		label = data.get('label')
		if not (uid and isinstance(label, str) and isinstance(duration, int) and 1 <= duration <= self.mSystem.GetSaleCfg()['sale_time_limit']):
			self.mSystem.ResponseToServer(serverId, callbackId, {
				'code': tradeConst.RespCodeInvalidParameter,
				'message': ''
			})
			return
		now = time.time()
		if uid not in self.mTradeData[tradeConst.CfgKeyDoughs]:
			self.mSystem.ResponseToServer(serverId, callbackId, {
				'code': tradeConst.RespCodeInvalidUser,
				'message': '用户不存在或不在线'
			})
			return
		if uid in self.mSaleData[tradeConst.CfgKeySales]:
			self.mSystem.ResponseToServer(serverId, callbackId, {
				'code': tradeConst.RespCodeInvalidUser,
				'message': '您已在摆摊'
			})
			return
		if not commonNetgameApi.CheckNameValid(label):
			logout.info('OnPlayerOpenStallReq invalid label: {}'.format(label))
			self.mSystem.ResponseToServer(serverId, callbackId, {
				'code': tradeConst.RespCodeInvalidParameter,
				'message': '存在敏感词'
			})
			return
		fee = self.mSystem.GetSaleCfg()['hourly_fee'] * duration
		if fee > self.mTradeData[tradeConst.CfgKeyDoughs][uid].get(self.mSystem.GetSaleCfg()['fee_dough'], 0):
			self.mSystem.ResponseToServer(serverId, callbackId, {
				'code': tradeConst.RespCodeInvalidUser,
				'message': '摆摊所需费用不足'
			})
			return
		if fee > 0:
			doughId = self.mSystem.GetSaleCfg()['fee_dough']
			self.mTradeData[tradeConst.CfgKeyDoughs][uid][doughId] -= fee
			self.UpdatePlayerDoughs(uid, {doughId: self.mTradeData[tradeConst.CfgKeyDoughs][uid][doughId]})
		inc = 3600 * duration
		self.mDeadlines.setdefault(self.mSecondHand + inc, []).append(uid)
		deadline = int(now + inc)
		self.mSaleData[tradeConst.CfgKeySales][uid] = {
			'duration': duration,
			'deadline': deadline,
			'ver': 0,
			'label': label,
			'deals': []
		}
		self.mSystem.ResponseToServer(serverId, callbackId, {
			'code': tradeConst.RespCodeSuccess,
			'message': '',
			'entity': {
				'uid': uid,
				'duration': duration,
				'deadline': deadline,
				'label': label,
				'time': int(time.time()),
			}
		})

	def OnPlayerCloseStallReq(self, serverId, callbackId, data):
		uid = data.get('uid')
		if not uid:
			self.mSystem.ResponseToServer(serverId, callbackId, {
				'code': tradeConst.RespCodeInvalidParameter,
				'message': ''
			})
			return
		if uid not in self.mTradeData[tradeConst.CfgKeyDoughs]:
			self.mSystem.ResponseToServer(serverId, callbackId, {
				'code': tradeConst.RespCodeInvalidUser,
				'message': '用户不存在或不在线'
			})
			return
		if uid not in self.mSaleData[tradeConst.CfgKeySales]:
			self.mSystem.ResponseToServer(serverId, callbackId, {
				'code': tradeConst.RespCodeInvalidUser,
				'message': '您未在摆摊'
			})
			return
		self.mSaleData[tradeConst.CfgKeySales].pop(uid, -1)
		self.mSystem.ResponseToServer(serverId, callbackId, {
			'code': tradeConst.RespCodeSuccess,
			'message': ''
		})
		for serverId in self.mTradeInvolvedServers.copy():
			self.mSystem.NotifyToServerNode(serverId, tradeConst.PlayerCloseStallEvent, {'outcasts': [uid]})

	def Find(self, conn, operation, parameters):
		try:
			c = conn.cursor()
			c.execute(operation, parameters)
			return c.fetchall()
		except Exception as e:
			conn.rollback()
			logout.error('Exception in Find e: {} operation: {} parameters: {}'.format(e, operation, parameters))
			return False

	def ManipulateOneMerch(self, conn, operation, parameters):
		try:
			c = conn.cursor()
			c.execute(operation, parameters)
			rowcount = c.rowcount
			conn.commit()
		except Exception as e:
			conn.rollback()
			logout.error('Exception in ManipulateOneMerch e: {} operation: {} parameters: {}'.format(e, operation, parameters))
			return False
		return rowcount

	def InsertOneMerch(self, conn, uid, currency, qty, unit, stuff):
		try:
			c = conn.cursor()
			c.execute('SELECT COUNT(1) FROM {} WHERE uid=%s'.format(tradeConst.TableTradeSaleMerch), (uid,))
			if c.fetchone()[0] >= self.mSystem.GetSaleCfg()['merch_count_limit']:
				return {
					'code': tradeConst.RespCodeInvalidUser,
					'message': '上架商品数量达到上限'
				}
			sql = 'INSERT INTO {} (uid, currency, unit, qty, init, stuff) VALUES (%s, %s, %s, %s, %s, %s)'.format(tradeConst.TableTradeSaleMerch)
			c.execute(sql, (uid, currency, unit, qty, qty, stuff))
			_id = conn.insert_id()
			conn.commit()
		except Exception as e:
			conn.rollback()
			logout.error('Exception in InsertOneMerch e: {}'.format(e))
			return {
				'code': tradeConst.RespCodeDBError,
				'message': '数据库操作失败'
			}
		return {
			'code': tradeConst.RespCodeSuccess,
			'message': '',
			'entity': {
				'_id': _id,
				'currency': self.mSystem.GetTradeCfg()[0].get(currency, {}).get('dough_icon'),
				'unit': unit,
				'init': qty,
				'uid': uid,
				'stuff': stuff,
				'qty': qty
			}
		}

	def FindOneMerchAndUpdate(self, serverId, callbackId, _id, uid, qty, step=0, **kwargs):
		if not step:
			merch = kwargs['rows'][0]
			if merch[1] not in self.mSaleData[tradeConst.CfgKeySales]:
				self.mSystem.ResponseToServer(serverId, callbackId, {
					'code': tradeConst.RespCodeInvalidUser,
					'message': '摊位已关闭',
					'entity': {
						'uid': uid,
					}
				})
				return
			if qty > merch[4]:
				self.mSystem.ResponseToServer(serverId, callbackId, {
					'code': tradeConst.RespCodeInvalidUser,
					'message': '商品库存不足',
					'entity': {
						'uid': uid,
						'_id': merch[0],
						'qty': merch[4],
						'msg': '商品库存不足',
					}
				})
				return
			if merch[3]:
				subtotal = merch[3] * qty
				if self.mTradeData[tradeConst.CfgKeyDoughs].get(uid, {}).get(merch[2], 0) < subtotal:
					self.mSystem.ResponseToServer(serverId, callbackId, {
						'code': tradeConst.RespCodeInvalidUser,
						'message': '余额不足',
					})
					return
				doughs = self.mSystem.GetTradeCfg()[0]
				doughId = merch[2]
				if subtotal > 0:
					self.mTradeData[tradeConst.CfgKeyDoughs][uid][doughId] -= subtotal
					self.UpdatePlayerDoughs(uid, {doughId: self.mTradeData[tradeConst.CfgKeyDoughs][uid][doughId]})
				elif self.mTradeData[tradeConst.CfgKeyDoughs][uid][doughId] < doughs[doughId]['dough_limit']:
					if self.mTradeData[tradeConst.CfgKeyDoughs][uid][doughId] > doughs[doughId]['dough_limit'] + subtotal:
						self.mTradeData[tradeConst.CfgKeyDoughs][uid][doughId] = doughs[doughId]['dough_limit']
					else:
						self.mTradeData[tradeConst.CfgKeyDoughs][uid][doughId] -= subtotal
					self.UpdatePlayerDoughs(uid, {doughId: self.mTradeData[tradeConst.CfgKeyDoughs][uid][doughId]})
			mysqlPool.AsyncExecuteFunctionWithOrderKey(
				self.ManipulateOneMerch,
				'PLAYER_%s_U' % uid,
				lambda rowcount: self.FindOneMerchAndUpdate(serverId, callbackId, merch[0], uid, qty, 1, merch=merch, rowcount=rowcount),
				'UPDATE {} t SET t.qty = t.qty - %s WHERE t._id=%s AND t.available=1 AND t.qty >= %s'.format(tradeConst.TableTradeSaleMerch),
				(qty, _id, qty)
			)
		elif step == 1:
			merch = kwargs['merch']
			subtotal = merch[3] * qty
			if kwargs['rowcount']:
				self.mSystem.ResponseToServer(serverId, callbackId, {
					'code': tradeConst.RespCodeSuccess,
					'message': '',
					'entity': {
						'uid': uid,
						'_id': _id,
						'qty': qty,
						'owner': merch[1],
						'currency': merch[2],
						'unit': merch[3],
						'subtotal': subtotal,
						'stuff': merch[-2]
					}
				})
				return
			if subtotal:
				doughs = self.mSystem.GetTradeCfg()[0]
				doughId = merch[2]
				if subtotal < 0:
					self.mTradeData[tradeConst.CfgKeyDoughs][uid][doughId] += subtotal
					self.UpdatePlayerDoughs(uid, {doughId: self.mTradeData[tradeConst.CfgKeyDoughs][uid][doughId]})
				elif self.mTradeData[tradeConst.CfgKeyDoughs][uid][doughId] < doughs[doughId]['dough_limit']:
					if self.mTradeData[tradeConst.CfgKeyDoughs][uid][doughId] > doughs[doughId]['dough_limit'] - subtotal:
						self.mTradeData[tradeConst.CfgKeyDoughs][uid][doughId] = doughs[doughId]['dough_limit']
					else:
						self.mTradeData[tradeConst.CfgKeyDoughs][uid][doughId] += subtotal
					self.UpdatePlayerDoughs(uid, {doughId: self.mTradeData[tradeConst.CfgKeyDoughs][uid][doughId]})
			mysqlPool.AsyncExecuteFunctionWithOrderKey(
				self.Find,
				'PLAYER_%s_S' % uid,
				lambda rows: self.mSystem.ResponseToServer(serverId, callbackId, {
					'code': tradeConst.RespCodeInvalidUser,
					'message': '商品库存不足',
					'entity': {
						'uid': uid,
						'_id': _id,
						'qty': rows[0][0],
						'msg': '商品库存不足',
					}
				}) if rows else self.mSystem.ResponseToServer(serverId, callbackId, {
					'code': tradeConst.RespCodeInvalidParameter,
					'message': '摊主修改了商品信息，请重新打开摊位'
				}),
				'SELECT qty FROM {} WHERE _id=%s AND available=1'.format(tradeConst.TableTradeSaleMerch),
				(_id,)
			)

	def OnTradeSaleRollbackReq(self, serverId, callbackId, data):
		uid = data.get('uid')
		currency = data.get('currency')
		subtotal = data.get('subtotal')
		if uid not in self.mTradeData[tradeConst.CfgKeyDoughs]:
			self.mSystem.ResponseToServer(serverId, callbackId, {
				'code': tradeConst.RespCodeInvalidUser,
				'message': '用户不存在或不在线'
			})
			return
		if subtotal:
			doughs = self.mSystem.GetTradeCfg()[0]
			doughId = currency
			if subtotal < 0:
				self.mTradeData[tradeConst.CfgKeyDoughs][uid][doughId] += subtotal
				self.UpdatePlayerDoughs(uid, {doughId: self.mTradeData[tradeConst.CfgKeyDoughs][uid][doughId]})
			elif self.mTradeData[tradeConst.CfgKeyDoughs][uid][doughId] < doughs[doughId]['dough_limit']:
				if self.mTradeData[tradeConst.CfgKeyDoughs][uid][doughId] > doughs[doughId]['dough_limit'] - subtotal:
					self.mTradeData[tradeConst.CfgKeyDoughs][uid][doughId] = doughs[doughId]['dough_limit']
				else:
					self.mTradeData[tradeConst.CfgKeyDoughs][uid][doughId] += subtotal
				self.UpdatePlayerDoughs(uid, {doughId: self.mTradeData[tradeConst.CfgKeyDoughs][uid][doughId]})
		self.mSystem.ResponseToServer(serverId, callbackId, {
			'code': tradeConst.RespCodeSuccess,
			'message': ''
		})

	def OnMerchOnSaleReq(self, serverId, callbackId, data):
		uid = data.get('uid')
		currency = data.get('currency')
		qty = data.get('qty')
		unit = data.get('unit')
		stuff = data.get('stuff')
		if uid not in self.mSaleData[tradeConst.CfgKeySales]:
			self.mSystem.ResponseToServer(serverId, callbackId, {
				'code': tradeConst.RespCodeInvalidUser,
				'message': '您未在摆摊'
			})
			return
		if not (currency in self.mSystem.GetSaleCfg()['sale_doughs'] and 0 <= unit <= self.mSystem.GetSaleCfg()['unit_price_limit'] and 0 <= qty <= 64):
			self.mSystem.ResponseToServer(serverId, callbackId, {
				'code': tradeConst.RespCodeInvalidParameter,
				'message': ''
			})
			return
		mysqlPool.AsyncExecuteFunctionWithOrderKey(
			self.InsertOneMerch,
			'PLAYER_%s_I' % uid,
			lambda data: logout.error('unlikely Exception in InsertOneMerch') if data is None else self.mSystem.ResponseToServer(serverId, callbackId, data),
			uid, currency, qty, unit, str(stuff)
		)

	def OnStallSaleUpdateReq(self, serverId, callbackId, data):
		uid = data['uid']
		_id = data['_id']
		owner = data['owner']
		currency = data['currency']
		unit = data['unit']
		qty = data['qty']
		subtotal = data['subtotal']
		stuff = data['stuff']
		if owner not in self.mTradeData[tradeConst.CfgKeyDoughs]:
			self.mSystem.ResponseToServer(serverId, callbackId, {
				'code': tradeConst.RespCodeInvalidUser,
				'message': '用户不存在或不在线'
			})
			return
		if subtotal:
			doughs = self.mSystem.GetTradeCfg()[0]
			doughId = currency
			if subtotal < 0:
				self.mTradeData[tradeConst.CfgKeyDoughs][owner][doughId] += subtotal
				self.UpdatePlayerDoughs(owner, {doughId: self.mTradeData[tradeConst.CfgKeyDoughs][owner][doughId]})
			elif self.mTradeData[tradeConst.CfgKeyDoughs][owner][doughId] < doughs[doughId]['dough_limit']:
				if self.mTradeData[tradeConst.CfgKeyDoughs][owner][doughId] > doughs[doughId]['dough_limit'] - subtotal:
					self.mTradeData[tradeConst.CfgKeyDoughs][owner][doughId] = doughs[doughId]['dough_limit']
				else:
					self.mTradeData[tradeConst.CfgKeyDoughs][owner][doughId] += subtotal
				self.UpdatePlayerDoughs(owner, {doughId: self.mTradeData[tradeConst.CfgKeyDoughs][owner][doughId]})
		if owner in self.mSaleData[tradeConst.CfgKeySales]:
			deal = (time.strftime('%Y-%m-%d %H:%M:%S'), stuff, self.mSaleData[tradeConst.CfgKeyDealers].get(uid, {}).get('name', '神秘人'), self.mSystem.GetTradeCfg()[0].get(currency, {}).get('dough_icon'), _id, unit, qty, subtotal)
			self.mSaleData[tradeConst.CfgKeySales][owner]['deals'].append(deal)
			# if len(self.mSaleData[tradeConst.CfgKeySales][owner]['deals']) > xxxxx:
			# 	del self.mSaleData[tradeConst.CfgKeySales][owner]['deals'][0]
			if owner in self.mSaleData[tradeConst.CfgKeyDealers]:
				self.mSystem.NotifyToServerNode(self.mSaleData[tradeConst.CfgKeyDealers][owner]['serverId'], tradeConst.StallSaleUpdateEvent, {'uid': owner, 'deal': deal})
		self.mSystem.ResponseToServer(serverId, callbackId, {
			'code': tradeConst.RespCodeSuccess,
			'message': ''
		})

	def OnPlayerSpotMerchReq(self, serverId, callbackId, data):
		uid = data.get('uid')
		_id = data.get('_id')
		qty = data.get('qty')
		if qty <= 0:
			logout.error('OnPlayerSpotMerchReq uid: {} _id: {} qty: {}'.format(uid, _id, qty))
			self.mSystem.ResponseToServer(serverId, callbackId, {
				'code': tradeConst.RespCodeInvalidParameter,
				'message': ''
			})
			return
		if uid not in self.mTradeData[tradeConst.CfgKeyDoughs]:
			self.mSystem.ResponseToServer(serverId, callbackId, {
				'code': tradeConst.RespCodeInvalidUser,
				'message': '用户不存在或不在线'
			})
			return
		mysqlPool.AsyncExecuteFunctionWithOrderKey(
			self.Find,
			'PLAYER_%s_S' % uid,
			lambda rows: self.FindOneMerchAndUpdate(serverId, callbackId, _id, uid, qty, rows=rows) if rows else self.mSystem.ResponseToServer(serverId, callbackId, {
				'code': tradeConst.RespCodeInvalidParameter,
				'message': '摊主修改了商品信息，请重新打开摊位'
			}),
			'SELECT * FROM {} WHERE _id=%s AND available=1'.format(tradeConst.TableTradeSaleMerch),
			(_id,)
		)

	def OnCountStallsReq(self, serverId, callbackId, data):
		self.mSystem.ResponseToServer(serverId, callbackId, {
			'code': tradeConst.RespCodeSuccess,
			'message': '请求成功',
			'entity': {
				'stalls': self.mSaleData[tradeConst.CfgKeySales]
			}
		})

	def OnBatchCheckReq(self, serverId, callbackId, data):
		results = {}
		for uid in data.get('samples', []):
			results[uid] = self.mSaleData[tradeConst.CfgKeySales][uid]['label'] if uid in self.mSaleData[tradeConst.CfgKeySales] else -1
		self.mSystem.ResponseToServer(serverId, callbackId, results)
