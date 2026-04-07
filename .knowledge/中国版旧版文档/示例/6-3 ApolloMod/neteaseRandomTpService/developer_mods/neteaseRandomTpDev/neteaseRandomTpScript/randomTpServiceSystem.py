# -*- coding: utf-8 -*-

import time
import server.extraServiceApi as serviceApi
ServiceSystem = serviceApi.GetServiceSystemCls()

import neteaseRandomTpScript.randomTpConst as randomTpConst
import apolloCommon.commonNetgameApi as commonNetgameApi

class RandomTpServiceSystem(ServiceSystem):
	"""
	"""
	def __init__(self, namespace, systemName):
		ServiceSystem.__init__(self, namespace, systemName)

		# 记录玩家冷却完毕时间
		self.userCDRecord = {}

		# 定时清理无用记录
		self.cleanerTimer = commonNetgameApi.AddRepeatedTimer(300.0, self.CleanRecordMap)

		# 注册监听
		self.RegisterRpcMethod(randomTpConst.ModName, randomTpConst.ServerEvent.CheckTpCD, self.OnCheckTpCD)
		self.RegisterRpcMethod(randomTpConst.ModName, randomTpConst.ServerEvent.StartTp, self.OnStartTp)
		self.RegisterRpcMethod(randomTpConst.ModName, randomTpConst.ServerEvent.TpInterrupt, self.OnTpInterrupt)

	def Destroy(self):
		pass

	# 扫描玩家冷却时间记录表，清理无用记录
	def CleanRecordMap(self):
		now = time.time()
		for uid in list(self.userCDRecord.keys()):
			if now - self.userCDRecord[uid] > 60.0:
				# 如果距离玩家冷却完毕时间已经过去1分钟以上，就不用留这个记录了
				self.userCDRecord.pop(uid)

	# 检查CD
	def OnCheckTpCD(self, serverId, callbackId, args):
		uid = args['uid']
		cdLeftTime = 0.0
		now = time.time()
		if uid in self.userCDRecord and self.userCDRecord[uid] > now:
			# 处于CD中，无法传送
			cdLeftTime = self.userCDRecord[uid] - now
		args['cdLeftTime'] = cdLeftTime
		self.ResponseToServer(serverId, callbackId, args)

	# 开始传送
	def OnStartTp(self, serverId, callbackId, args):
		uid = args['uid']
		args['cdLeftTime'] = 0.0
		now = time.time()
		if uid in self.userCDRecord and self.userCDRecord[uid] > now:
			# 处于CD中，无法传送
			args['cdLeftTime'] = self.userCDRecord[uid] - now
			self.ResponseToServer(serverId, callbackId, args)
			return
		# 开始传送，具体传送交由原服自己处理
		self.userCDRecord[uid] = now + args['coolingTime']
		self.ResponseToServer(serverId, callbackId, args)

	# 打断传送
	def OnTpInterrupt(self, serverId, callbackId, args):
		if args['isCoolingAfterInterrupt']:
			now = time.time()
			uid = args['uid']
			self.userCDRecord[uid] = now + args['coolingTime']
