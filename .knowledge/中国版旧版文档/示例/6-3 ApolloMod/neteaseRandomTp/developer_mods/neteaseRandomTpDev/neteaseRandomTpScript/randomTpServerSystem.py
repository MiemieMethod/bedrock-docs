# -*- coding: utf-8 -*-

import time
import random
import math
import json
import server.extraServerApi as serverApi
ServerSystem = serverApi.GetServerSystemCls()
import lobbyGame.netgameApi as lobbyGameApi
import apolloCommon.commonNetgameApi as commonNetgameApi
import lobbyGame.netgameApi as lobbyGameApi
from mod_log import engine_logger as logger


from neteaseRandomTpScript.randomTpConst import ModName, ClientSystemName, ClientEvent, ServerEvent
import neteaseRandomTpScript.randomTpConst as randomTpConst


def CleanDict(_dict, exKey):
	if exKey in _dict:
		del _dict[exKey]
	for v in _dict.values():
		if type(v) == dict:
			CleanDict(v, exKey)

class RandomTpServerSystem(ServerSystem):
	"""
	"""
	def __init__(self, namespace, systemName):
		ServerSystem.__init__(self, namespace, systemName)
		# 初始化默认参数值
		self.coolingTime = randomTpConst.DefaultParams.CoolingTime
		self.readingTime = randomTpConst.DefaultParams.ReadingTime
		self.interruptType = randomTpConst.DefaultParams.InterruptType
		self.isCoolingAfterInterrupt = randomTpConst.DefaultParams.IsCoolingAfterInterrupt
		self.randomRange = randomTpConst.DefaultParams.RandomRange
		self.blockBlackList = randomTpConst.DefaultParams.BlockBlackList
		self.tpBlackList = randomTpConst.DefaultParams.TpBlackList
		self.safePosRange = randomTpConst.DefaultParams.SafePosRange

		self.playerId2ReadingTimeRecord = {} # 记录玩家读秒记录，{playerId: {"data": tpRequestData, "timer": timer}}
		self.chunkToLoadRecordList = {} # 记录要常加载的区块，{areaName: {"playerId": str, "dimensionId": int, "targetPos": (x, y, z), "data": tpRequestData, "chunkList": [(x, y, z),]}}

		# 加载配置信息
		self.ReloadConfig()

		# 注册事件
		self.ListenForEvent(serverApi.GetEngineNamespace(), serverApi.GetEngineSystemName(), "PlayerHurtEvent", self, self.OnPlayerHurt)
		self.ListenForEvent(serverApi.GetEngineNamespace(), serverApi.GetEngineSystemName(), "AddServerPlayerEvent", self, self.OnAddServerPlayer)

	def Destroy(self):
		# 注销事件
		self.UnListenForEvent(serverApi.GetEngineNamespace(), serverApi.GetEngineSystemName(), "PlayerHurtEvent", self, self.OnPlayerHurt)
		self.UnListenForEvent(serverApi.GetEngineNamespace(), serverApi.GetEngineSystemName(), "AddServerPlayerEvent", self, self.OnAddServerPlayer)

	def Update(self):
		# 每帧用来检测玩家移动打断
		for playerId, timeRecord in self.playerId2ReadingTimeRecord.items():
			if timeRecord['data']['interruptType'] == randomTpConst.InterruptType.Moving or timeRecord['data']['interruptType'] == randomTpConst.InterruptType.MovingOrHurting:
				currentPos = timeRecord['data']['currentPos']
				comp = serverApi.GetEngineCompFactory().CreatePos(playerId)
				pos = comp.GetPos()
				delta = 0.1
				if abs(pos[0]-currentPos[0]) > delta or abs(pos[1]-currentPos[1]) > delta or abs(pos[2]-currentPos[2]) > delta:
					# 用delta值的方式避免float计算问题
					self.PlayerInterrupt(playerId, randomTpConst.InterruptType.Moving)

		# 每帧判断是否有加载中的区块，检测是否加载完成
		delayDeleteArea = [] # 延迟删除区块
		comp = serverApi.GetEngineCompFactory().CreateChunkSource(serverApi.GetLevelId())
		for areaName in list(self.chunkToLoadRecordList.keys()):
			isAllLoaded = True
			loadRecord = self.chunkToLoadRecordList[areaName]
			chunkList = loadRecord['chunkList']
			for pos in chunkList:
				# 检查这些区块是否已加载
				if not comp.CheckChunkState(loadRecord['dimensionId'], pos):
					isAllLoaded = False
					break
			if isAllLoaded:
				delayDeleteArea.append(areaName)
				self.chunkToLoadRecordList.pop(areaName)
				self.FinalDoTp(loadRecord['playerId'], loadRecord['dimensionId'], loadRecord['targetPos'], loadRecord['data'])
		for areaName in delayDeleteArea:
			if not comp.DeleteArea(areaName):
				# 删除常加载区域失败
				logger.error("==== neteaseRandomTp Update: delete area({}) failed".format(areaName))

	def ReloadConfig(self):
		# 读取 mod.json 配置文件
		cfg = commonNetgameApi.GetModJsonConfig("neteaseRandomTpScript")
		if not cfg:
			logger.error("==== neteaseRandomTp ReloadConfig: read config failed")
			return False

		randomTpConst.ConfigParams.update(cfg["configParams"])
		CleanDict(randomTpConst.ConfigParams, "_comment")
		if "blockBlackList" in cfg["configParams"]:
			self.blockBlackList = cfg["configParams"]["blockBlackList"]
		if "tpBlackList" in cfg["configParams"]:
			self.tpBlackList = cfg["configParams"]["tpBlackList"]
		logger.info("==== neteaseRandomTp ReloadConfig: finished, new config: {}".format(randomTpConst.ConfigParams))

	# 玩家加入游戏时触发
	def OnAddServerPlayer(self, args):
		if args['isTransfer']:
			transferParam = json.loads(args['transferParam'])
			if type(transferParam) == dict and 'tpType' in transferParam:
				# 随机传送过来的
				if transferParam['tpType'] == randomTpConst.TpType.TpTypeCrossServer:
					# 同跨纬度传送处理
					self.DoTpCrossDimension(args["id"], transferParam)

	# 玩家受伤害时触发
	def OnPlayerHurt(self, args):
		playerId = args["id"]
		if playerId in self.playerId2ReadingTimeRecord:
			interruptType = self.playerId2ReadingTimeRecord[playerId]['data']['interruptType']
			if interruptType == randomTpConst.InterruptType.Hurting or interruptType == randomTpConst.InterruptType.MovingOrHurting:
				# 造成打断
				self.PlayerInterrupt(playerId, randomTpConst.InterruptType.Hurting)

	# 玩家读秒被打断
	def PlayerInterrupt(self, playerId, interruptType):
		timeRecord = self.playerId2ReadingTimeRecord[playerId]
		commonNetgameApi.CancelTimer(timeRecord['timer'])
		self.playerId2ReadingTimeRecord.pop(playerId)
		# 读秒被打断
		uid = lobbyGameApi.GetPlayerUid(playerId)
		eventData = {"uid": uid, "interruptType": interruptType}
		self.BroadcastEvent(randomTpConst.OutputEvent.ReadingInterrupted, eventData)
		self.NotifyClientMessage(playerId, randomTpConst.MsgTpInterrupt)
		self.NotifyToClient(playerId, randomTpConst.ClientEvent.ReadingInterrupted, {})
		self.RequestToService(ModName, randomTpConst.ServerEvent.TpInterrupt, timeRecord['data'])

	# 导出API：本维度传送
	def TpInDimension(self, playerId, targetPos=None, randomRange=None, coolingTime=None, readingTime=None, interruptType=None, isCoolingAfterInterrupt=None):
		self.DoTpReadingRequest(playerId, randomTpConst.TpType.TpTypeInDimension, targetPos, [], randomRange, coolingTime, readingTime, interruptType, isCoolingAfterInterrupt)
	
	# 导出API：跨维度传送
	def TpCrossDimension(self, playerId, targetPos, tpParams=[], randomRange=None, coolingTime=None, readingTime=None, interruptType=None, isCoolingAfterInterrupt=None):
		self.DoTpReadingRequest(playerId, randomTpConst.TpType.TpTypeCrossDimension, targetPos, tpParams, randomRange, coolingTime, readingTime, interruptType, isCoolingAfterInterrupt)

	# 导出API：跨服传送
	def TpCrossServer(self, playerId, targetPos, tpParams={}, randomRange=None, coolingTime=None, readingTime=None, interruptType=None, isCoolingAfterInterrupt=None):
		self.DoTpReadingRequest(playerId, randomTpConst.TpType.TpTypeCrossServer, targetPos, tpParams, randomRange, coolingTime, readingTime, interruptType, isCoolingAfterInterrupt)

	# 通知客户端提示
	def NotifyClientMessage(self, playerId, message):
		alertSystem = serverApi.GetSystem("neteaseAlert", "neteaseAlertDev")
		if alertSystem:
			alertSystem.Alert(playerId, message, 2, 0.5, 0.8)
		else:
			comp = self.CreateComponent(playerId, "Minecraft", "command")
			comp.SetCommand('tellraw @s {"rawtext": [{"text": "%s"}]}' % ('§e' + message), playerId)

	# 统一处理参数，检查CD
	def DoTpReadingRequest(self, playerId, tpType, targetPos, tpParams, randomRange=None, coolingTime=None, readingTime=None, interruptType=None, isCoolingAfterInterrupt=None):
		"""
		tpType: 传送类型
		tpParams: 传送参数
		"""
		# 导出服务端事件：玩家开始发起传送请求时广播
		uid = lobbyGameApi.GetPlayerUid(playerId)
		eventData = {"uid": uid, "cancel": False}
		self.BroadcastEvent(randomTpConst.OutputEvent.TpStarted, eventData)
		if eventData['cancel']:
			# 如果广播后cancel被设置为True，则取消发起传送
			return

		# 先检查传送黑名单，确定当前维度是否允许传送
		serverType = commonNetgameApi.GetServerType()
		if serverType in self.tpBlackList:
			if len(self.tpBlackList[serverType]) == 0:
				# 表示全都禁止
				self.NotifyClientMessage(playerId, randomTpConst.MsgTpForbiden)
				return
			comp = serverApi.GetEngineCompFactory().CreateDimension(playerId)
			dimensionId = int(comp.GetEntityDimensionId())
			if dimensionId in self.tpBlackList[serverType]:
				# 该维度被禁止
				self.NotifyClientMessage(playerId, randomTpConst.MsgTpForbiden)
				return

		# 初始化部分未传入的参数
		if targetPos is None:
			if tpType == randomTpConst.TpType.TpTypeCrossDimension or tpType == randomTpConst.TpType.TpTypeCrossServer:
				# 不允许目标点为空
				self.NotifyClientMessage(playerId, randomTpConst.MsgTpTargetPosEmpty)
				return
			comp = serverApi.GetEngineCompFactory().CreatePos(playerId)
			targetPos = comp.GetPos()
		# 强转成整型，只能传送到整数点
		targetPos = (int(targetPos[0]), int(targetPos[1]), int(targetPos[2]))
		if tpType == randomTpConst.TpType.TpTypeCrossServer:
			# 跨服传送如果没有设置正确参数的话，默认为本服本维度
			if type(tpParams) != dict or len(tpParams) == 0:
				tpParams = {}
				tpParams[serverType] = []
		if tpType not in randomTpConst.ConfigParams:
			# 如果配置文件中没有配这类，用默认的
			if coolingTime is None:
				coolingTime = self.coolingTime
			if readingTime is None:
				readingTime = self.readingTime
			if interruptType is None:
				interruptType = self.interruptType
			if isCoolingAfterInterrupt is None:
				isCoolingAfterInterrupt = self.isCoolingAfterInterrupt
			if randomRange is None:
				randomRange = self.randomRange
		else:
			# 否则，用配置文件中的
			if coolingTime is None:
				coolingTime = randomTpConst.ConfigParams[tpType]["coolingTime"]
			if readingTime is None:
				readingTime = randomTpConst.ConfigParams[tpType]["readingTime"]
			if interruptType is None:
				interruptType = randomTpConst.ConfigParams[tpType]["interruptType"]
			if isCoolingAfterInterrupt is None:
				isCoolingAfterInterrupt = randomTpConst.ConfigParams[tpType]["isCoolingAfterInterrupt"]
			if randomRange is None:
				randomRange = randomTpConst.ConfigParams[tpType]["randomRange"]
		# 检查CD
		requestData = {
			'uid': uid,
			'playerId': playerId,
			'targetPos': targetPos,
			'coolingTime': coolingTime,
			'readingTime': readingTime,
			'interruptType': interruptType,
			'isCoolingAfterInterrupt': isCoolingAfterInterrupt,
			'randomRange': randomRange,
			'tpType': tpType,
			'tpParams': tpParams,
		}
		self.RequestToService(ModName, randomTpConst.ServerEvent.CheckTpCD, requestData, self.OnCheckTpCDCallback)

	# 检查CD的回调
	def OnCheckTpCDCallback(self, suc, args):
		if not suc:
			logger.error("==== neteaseRandomTp OnCheckTpCDCallback: timeout")
			return
		playerId = args['playerId']
		if args['cdLeftTime'] > 0:
			# CD中，还不能传送
			cdLeftTime = int(math.ceil(args['cdLeftTime']))
			self.NotifyClientMessage(playerId, randomTpConst.MsgInCD % cdLeftTime)
			return

		# 记录玩家当前位置
		comp = serverApi.GetEngineCompFactory().CreatePos(playerId)
		args['currentPos'] = comp.GetPos()
		comp = serverApi.GetEngineCompFactory().CreateDimension(playerId)
		args['currentDimensionId'] = int(comp.GetEntityDimensionId())
		args['currentServerType'] = commonNetgameApi.GetServerType()

		# 判断读秒
		readingTime = args['readingTime']
		if readingTime > 0:
			# 开始读秒
			# 通知客户端读秒事件
			eventData = {'readingTime': readingTime}
			self.NotifyToClient(playerId, randomTpConst.ClientEvent.ReadingStarted, eventData)
			if playerId in self.playerId2ReadingTimeRecord:
				# 之前已经有定时器了，把之前的顶掉
				commonNetgameApi.CancelTimer(self.playerId2ReadingTimeRecord[playerId]['timer'])
				self.playerId2ReadingTimeRecord.pop(playerId)
			# 计算首次延时时间，确保后面的取整
			deltaTime = readingTime - math.floor(readingTime)
			if deltaTime > 0:
				# 先停小数位的时间再提示，本次不提示
				args['readingTime'] += 1.0 - deltaTime
				timer = commonNetgameApi.AddTimer(deltaTime, self.TimerTick, playerId)
			else:
				# 否则提示当前剩余的整数秒数
				self.NotifyClientMessage(playerId, randomTpConst.MsgReadingTime % readingTime)
				timer = commonNetgameApi.AddTimer(1.0, self.TimerTick, playerId)
			self.playerId2ReadingTimeRecord[playerId] = {'data': args, 'timer': timer}
			return

		# 不需要读秒的直接开始申请传送
		self.RequestToService(ModName, randomTpConst.ServerEvent.StartTp, args, self.OnStartTpCallback)

	# 处理读秒
	def TimerTick(self, playerId):
		timeRecord = self.playerId2ReadingTimeRecord[playerId]
		data = timeRecord['data']
		readingTime = data['readingTime'] - 1
		if readingTime == 0:
			# 读秒结束，开始传送
			self.playerId2ReadingTimeRecord.pop(playerId)
			# 读秒完成时
			eventData = {"uid": data['uid'], "cancel": False}
			self.BroadcastEvent(randomTpConst.OutputEvent.ReadingFinished, eventData)
			if eventData['cancel']:
				# 如果广播后被设置为True，则取消传送
				return
			self.RequestToService(ModName, randomTpConst.ServerEvent.StartTp, data, self.OnStartTpCallback)
			return
		# 继续读秒
		self.playerId2ReadingTimeRecord[playerId]['data']['readingTime'] = readingTime
		self.NotifyClientMessage(playerId, randomTpConst.MsgReadingTime % readingTime)
		timer = commonNetgameApi.AddTimer(1.0, self.TimerTick, playerId)
		self.playerId2ReadingTimeRecord[playerId]['timer'] = timer

	# 开始传送的回调
	def OnStartTpCallback(self, suc, args):
		if not suc:
			logger.error("==== neteaseRandomTp OnStartTpCallback: timeout")
			return
		playerId = args['playerId']
		if args['cdLeftTime'] > 0:
			# CD中，还不能传送
			cdLeftTime = int(math.ceil(args['cdLeftTime']))
			self.NotifyClientMessage(playerId, randomTpConst.MsgInCD % cdLeftTime)
			return

		# 开始处理传送
		tpType = args['tpType']
		if tpType == randomTpConst.TpType.TpTypeInDimension:
			# 维度内传送
			self.DoTpInDimension(playerId, args)
		elif tpType == randomTpConst.TpType.TpTypeCrossDimension:
			# 跨纬度传送
			self.DoTpCrossDimension(playerId, args)
		elif tpType == randomTpConst.TpType.TpTypeCrossServer:
			# 跨服传送
			self.DoTpCrossServer(playerId, args)

	# 给定目标维度和目标点，在附近寻找安全位置
	def SearchSafePos(self, dimensionId, targetPos):
		# 搜索方式是从中心点逐步向外一圈圈扩张搜索
		targetX = int(targetPos[0])
		targetY = int(targetPos[1])
		targetZ = int(targetPos[2])
		minY = max(targetY - self.safePosRange, 0)
		maxY = targetY + self.safePosRange
		for delta in xrange(self.safePosRange):
			x = targetX - delta
			for z in xrange(targetZ-delta, targetZ+delta+1):
				y = self.GetSafeHeightAtXZ(dimensionId, x, z, minY, maxY)
				if y != None and self.IsPosSafe(dimensionId, x, y-1, z):
					return (x, y, z)
			x = targetX + delta
			for z in xrange(targetZ-delta, targetZ+delta+1):
				y = self.GetSafeHeightAtXZ(dimensionId, x, z, minY, maxY)
				if y != None and self.IsPosSafe(dimensionId, x, y-1, z):
					return (x, y, z)
			z = targetZ - delta
			for x in xrange(targetX-delta+1, targetX+delta):
				y = self.GetSafeHeightAtXZ(dimensionId, x, z, minY, maxY)
				if y != None and self.IsPosSafe(dimensionId, x, y-1, z):
					return (x, y, z)
			z = targetZ + delta
			for x in xrange(targetX-delta+1, targetX+delta):
				y = self.GetSafeHeightAtXZ(dimensionId, x, z, minY, maxY)
				if y != None and self.IsPosSafe(dimensionId, x, y-1, z):
					return (x, y, z)
		# 都没有找到
		return None

	# 在给定XZ坐标上搜索安全的Y
	def GetSafeHeightAtXZ(self, dimensionId, targetX, targetZ, minY, maxY):
		# 首先找最高非空气方块
		comp = serverApi.GetEngineCompFactory().CreateBlockInfo(serverApi.GetLevelId())
		height = comp.GetTopBlockHeight((targetX, targetZ), dimensionId)
		height += 1 # +1 的原因是人要站在这个方块上
		# 判断这个位置是否超过范围
		if height > maxY: 
			# 超过上限，则在范围内从下往上找最低空气方块
			for y in xrange(minY, maxY+1):
				blockDict = comp.GetBlockNew((targetX, y, targetZ), dimensionId)
				if blockDict['name'] == 'minecraft:air':
					if y == minY:
						# 找到的最低空气方块恰好是最底下那格，还需要检查这个方块下面一格是否是非空气方块
						blockDict = comp.GetBlockNew((targetX, y-1, targetZ), dimensionId)
						if blockDict['name'] != 'minecraft:air':
							return y
					else:
						return y
			# 都没有找到，则放弃
			return None
		elif height < minY:
			# 最高的也不在范围内，那么这个XZ上肯定找不到了
			return None
		else:
			# 在范围内，则直接返回这个点
			return height

	# 判断某格是否为安全方块
	def IsPosSafe(self, dimensionId, targetX, targetY, targetZ):
		comp = serverApi.GetEngineCompFactory().CreateBlockInfo(serverApi.GetLevelId())
		blockDict = comp.GetBlockNew((targetX, targetY, targetZ), dimensionId)
		if blockDict["name"] in self.blockBlackList:
			return False
		elif blockDict["name"]+":"+str(blockDict["aux"]) in self.blockBlackList:
			return False
		return True

	# 维度内传送
	def DoTpInDimension(self, playerId, data):
		# 等价于跨纬度传送，只是tpParams为[]，默认为本维度传送
		self.DoTpCrossDimension(playerId, data)

	# 跨纬度传送
	def DoTpCrossDimension(self, playerId, data):
		targetPos = data['targetPos']
		randomRange = data['randomRange']
		tpParams = data['tpParams']

		# 如果是跨服传送过来的，需要调整一下参数格式，取出对应游戏类型的配置
		if data['tpType'] == randomTpConst.TpType.TpTypeCrossServer:
			serverType = commonNetgameApi.GetServerType()
			tpParams = tpParams[serverType]
		# 随机维度id
		if len(tpParams) == 0:
			# 默认选中当前维度
			comp = serverApi.GetEngineCompFactory().CreateDimension(playerId)
			dimensionId = int(comp.GetEntityDimensionId())
		else:
			dimensionId = int(tpParams[random.randint(0, len(tpParams)-1)])

		# 计算随机落点
		randX = targetPos[0] + random.randint(min(randomRange[0], randomRange[2]), max(randomRange[0], randomRange[2]))
		randZ = targetPos[2] + random.randint(min(randomRange[1], randomRange[3]), max(randomRange[1], randomRange[3]))

		# 加载目标区块
		self.LoadTargetArea(playerId, dimensionId, (randX, targetPos[1], randZ), data)

	# 跨服传送
	def DoTpCrossServer(self, playerId, data):
		# 随机游戏类型
		randomServerType = random.choice(data['tpParams'].keys())
		# 切服过去，后续的随机维度和坐标由目标服务器处理
		lobbyGameApi.TransferToOtherServer(playerId, randomServerType, json.dumps(data))

	# 加载目标区块
	def LoadTargetArea(self, playerId, dimensionId, targetPos, data):
		# 向外扩展1确保后面搜索的时候边界也被加载
		minX = targetPos[0] - self.safePosRange - 1
		maxX = targetPos[0] + self.safePosRange + 1
		minZ = targetPos[2] - self.safePosRange - 1
		maxZ = targetPos[2] + self.safePosRange + 1
		# 确定目标范围所涉及的区块列表
		chunkToLoadList = []
		chunkMinX = (minX / 16) * 16
		chunkMinZ = (minZ / 16) * 16
		isUnload = False
		comp = serverApi.GetEngineCompFactory().CreateChunkSource(serverApi.GetLevelId())
		for x in xrange(chunkMinX, maxX+1, 16): # +1 是为了确保上限点在xrange范围内
			for z in xrange(chunkMinZ, maxZ+1, 16):
				# 检查这些区块是否已加载
				chunkToLoadList.append((x, targetPos[1], z))
				if not comp.CheckChunkState(dimensionId, (x, targetPos[1], z)):
					isUnload = True
		if isUnload:
			# 存在未加载的区块，则统一都设置常加载，异步后续处理
			areaName = "toload_"+playerId
			allAreaKeys = comp.GetAllAreaKeys()
			if areaName in allAreaKeys:
				# 之前已存在加载中的区块列表，把之前的清掉
				logger.error("==== neteaseRandomTp LoadTargetArea: area({}) exist, clear first".format(areaName))
				comp.DeleteArea(areaName)
				if areaName in self.chunkToLoadRecordList:
					self.chunkToLoadRecordList.pop(areaName)
			if comp.SetAddArea(areaName, dimensionId, (minX-80, targetPos[1], minZ-80), (maxX+80, targetPos[1], maxZ+80)):
				logger.info("==== neteaseRandomTp LoadTargetArea: SetAddArea success, area({}), min={}, max={}".format(areaName, (minX-80, targetPos[1], minZ-80), (maxX+80, targetPos[1], maxZ+80)))
				self.chunkToLoadRecordList[areaName] = {'playerId': playerId, 'dimensionId': dimensionId, 'targetPos': targetPos, 'data': data, 'chunkList': chunkToLoadList}
				return
			else:
				# 加载区块失败，直接传送过去，不搜索了
				logger.error("==== neteaseRandomTp LoadTargetArea: SetAddArea failed. tp directly")
				self.DoTp(playerId, dimensionId, targetPos, data)
				return
		# 区块都已加载，则直接跳转
		self.FinalDoTp(playerId, dimensionId, targetPos, data)

	# 最终传送过去
	def FinalDoTp(self, playerId, dimensionId, targetPos, data):
		# 寻找安全位置降落
		finalPos = self.SearchSafePos(dimensionId, targetPos)
		if not finalPos:
			# 找不到则直接传送到中心点
			finalPos = targetPos
		# 传送维度
		self.DoTp(playerId, dimensionId, finalPos, data)

	# 传送到某个点
	def DoTp(self, playerId, dimensionId, targetPos, data):
		# 执行传送
		comp = serverApi.GetEngineCompFactory().CreateDimension(playerId)
		comp.ChangePlayerDimension(dimensionId, targetPos)
		if data['tpType'] == randomTpConst.TpType.TpTypeInDimension:
			self.NotifyClientMessage(playerId, randomTpConst.MsgInDimensionTpFinished % (targetPos[0], targetPos[1], targetPos[2]))
		elif data['tpType'] == randomTpConst.TpType.TpTypeCrossDimension:
			self.NotifyClientMessage(playerId, randomTpConst.MsgCrossDimensionTpFinished % (dimensionId, targetPos[0], targetPos[1], targetPos[2]))
		elif data['tpType'] == randomTpConst.TpType.TpTypeCrossServer:
			serverType = commonNetgameApi.GetServerType().encode('utf-8')
			self.NotifyClientMessage(playerId, randomTpConst.MsgCrossServerTpFinished % (serverType, dimensionId, targetPos[0], targetPos[1], targetPos[2]))
		logger.info("final dim({}), pos({})".format(dimensionId, targetPos))
		# 传送完成时
		originPos = (int(data['currentPos'][0]), int(data['currentPos'][1]), int(data['currentPos'][2]))
		eventData = {"uid": data['uid'], "originServerType": data['currentServerType'], "originDimensionId": data['currentDimensionId'], "originPos": originPos}
		self.BroadcastEvent(randomTpConst.OutputEvent.TpFinished, eventData)
		self.NotifyToClient(playerId, randomTpConst.ClientEvent.TpFinished, eventData)
