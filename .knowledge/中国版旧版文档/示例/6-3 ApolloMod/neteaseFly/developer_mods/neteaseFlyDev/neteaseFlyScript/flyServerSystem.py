# -*- coding: utf-8 -*-
import time

import apolloCommon.commonNetgameApi as commonNetgameApi
import apolloCommon.mysqlPool as mysqlPool
import lobbyGame.netgameApi as netgameApi
import logout
import neteaseFlyScript.flyServerConsts as flyConsts
import server.extraServerApi as serverApi
from neteaseFlyScript.mgr.flyStateMachine import FlyStateMachine, NodeId, EventType

ServerSystem = serverApi.GetServerSystemCls()


class FlyServerSystem(ServerSystem):
	def __init__(self, namespace, systemName):
		ServerSystem.__init__(self, namespace, systemName)
		if not self.InitMysqlPool():
			return
		self.mPlayerData = {}
		self.mPlayerList = {} # { playerId : playerUid}
		self.mFlyAreaList = {} # { areaName: (dimension, minX, minY, minZ, maxX, maxY, maxZ)}
		self.Init()
		self.ListenEvents()

	def Init(self):
		modConfig = commonNetgameApi.GetModJsonConfig('neteaseFlyScript')
		self.mFlyInterval = modConfig.get("FLY_INTERVAL", 0) * 30
		self.mFlyCost = modConfig.get("FLY_COST", 0)
		self.mHugerLimit = modConfig.get("HUNGER_LIMIT", 0)
		self.mHugerStopFly = modConfig.get("HUNGER_STOP_FLY", 0)
		self.mIsBlackListMode = modConfig.get("IS_BLACK_LIST_MODE", True)
		self.InitAOIList(modConfig.get("AOI_LIST", []))

	def InitAOIList(self, AOIList):
		if isinstance(AOIList, list) and len(AOIList) > 0:
			index = 0
			for area in AOIList:
				dimension = area[0]
				aabb = tuple(area[1:])
				comp = self.CreateComponent("", "Minecraft", "dimension")
				areaName = "area_{}".format(index)
				comp.CreateDimension(dimension)
				if comp.RegisterEntityAOIEvent(dimension, areaName, aabb, None):
					self.mFlyAreaList[areaName] = (dimension,) + aabb
					index += 1
				else:
					logout.error("RegisterEntityAOIEvent Failed! dimension is ", dimension)

	def Destroy(self):
		self.UnListenEvents()
		mysqlPool.Finish()

	def ListenEvents(self):
		self.ListenForEvent(flyConsts.ModNameSpace, flyConsts.ClientSystemName, flyConsts.ClientEnterEvent,
							self, self.OnClientEnter)
		self.ListenForEvent(flyConsts.ModNameSpace, flyConsts.ClientSystemName, flyConsts.ChangeFlyStateEvent,
							self, self.OnFlyStateChange)
		self.ListenForEvent(serverApi.GetEngineNamespace(), serverApi.GetEngineSystemName(), "OnEntityAreaEvent",
							self, self.OnEntityAreaEvent)
		self.ListenForEvent(serverApi.GetEngineNamespace(), serverApi.GetEngineSystemName(), "DelServerPlayerEvent",
							self, self.OnClientLeave)

	def UnListenEvents(self):
		self.UnListenForEvent(flyConsts.ModNameSpace, flyConsts.ClientSystemName, flyConsts.ClientEnterEvent,
							self, self.OnClientEnter)
		self.UnListenForEvent(flyConsts.ModNameSpace, flyConsts.ClientSystemName, flyConsts.ChangeFlyStateEvent,
							self, self.OnFlyStateChange)
		self.UnListenForEvent(serverApi.GetEngineNamespace(), serverApi.GetEngineSystemName(), "OnEntityAreaEvent",
							self, self.OnEntityAreaEvent)
		self.UnListenForEvent(serverApi.GetEngineNamespace(), serverApi.GetEngineSystemName(), "DelServerPlayerEvent",
							self, self.OnClientLeave)

	# ------------------------------------------------------------------------------------------
	def OnClientEnter(self, args):
		playerId = args.get("playerId", "-1")
		if playerId == -1:
			logout.warning("Clien Enter Warning [-1]")
			return
		comp = serverApi.CreateComponent(playerId, "Minecraft", "dimension")
		dimension = comp.GetPlayerDimensionId()
		comp = serverApi.CreateComponent(playerId, "Minecraft", "pos")
		pos = comp.GetPos()
		playerUid = netgameApi.GetPlayerUid(playerId)
		if playerUid in self.mPlayerData:
			# 玩家已存在，因为切换维度触发该事件
			playerData = self.mPlayerData[playerUid]
			flyEnable = playerData["flyEnabled"]
			flyState = playerData["flyState"]
			if self.CheckIsInArea(dimension, pos):
				logout.info("OnClientEnter player not in areas")
				# 黑名单模式下若玩家在该范围内禁止飞行
				flyEnable = not self.mIsBlackListMode
			else:
				flyEnable = self.mIsBlackListMode
			isFly = flyState == 1 and flyEnable
			data = {
				"flyState": isFly,
				"flyEnable": flyEnable
			}
			if isFly != flyState:
				playerData["flyStateMachine"].ChangeState(NodeId.Fly, EventType.APICall, playerUid)
			self.NotifyToClient(playerId, flyConsts.SyncConfigEvent, data)
		else:
			# 玩家不存在，请求数据库读取数据
			self.mPlayerList[playerId] = playerUid
			logout.info("player [{0}] enter game.".format(playerUid))
			sql = "SELECT flyState, flyCnt FROM {} ".format(flyConsts.TableUserFlyPluginInfo)
			sql += "WHERE uid = %s"
			params = (playerUid, )
			callback = lambda records:self.QueryPlayerInfoCallBack(records, playerUid, dimension, pos)
			mysqlPool.AsyncQueryWithOrderKey('playerLogin', sql, params, callback)

	def OnClientLeave(self, args):
		# 客户端离开该服务器（退出或者切服）时把对应的飞行状态机删除
		logout.info("OnClientLeave ", str(args))
		playerUid = args.get("uid", -1)
		playerId = args.get("id")
		if playerUid == -1:
			logout.warning("Clien leave Warning [-1]")
			return
		if playerId in self.mPlayerList:
			del self.mPlayerList[playerId]
		if playerUid in self.mPlayerData:
			state = self.mPlayerData[playerUid]["flyState"]
			flyCnt = self.mPlayerData[playerUid]["flyCnt"]
			sql = "INSERT INTO {} (uid, flyState, flyCnt)".format(flyConsts.TableUserFlyPluginInfo)
			sql += "VALUES (%s, %s, %s) ON DUPLICATE KEY UPDATE flyState=%s, flyCnt=%s"
			params = (playerUid, state, flyCnt, state, flyCnt)
			mysqlPool.AsyncExecuteWithOrderKey('playerLogout', sql, params, None)
			del self.mPlayerData[playerUid]

	def OnFlyStateChange(self, args):
		# 客户端点击开启/关闭按钮时、控制服收到http请求开关飞行时会通知服务端进行处理
		playerUid = args.get("uid", None)
		playerId = args.get("playerId", "-1")
		if playerUid is None:
			if playerId == "-1":
				return
			playerUid = self.mPlayerList.get(playerId)
		logout.info("OnFlyStateChange playerUid is", playerUid)
		state = args.get("state", False)
		if playerUid in self.mPlayerData:
			if state:
				playerData = self.mPlayerData[playerUid]
				playerData["flyStateMachine"].ReceiveEvent(playerData["flyEnabled"], EventType.OpenFly, playerUid)
			else:
				playerData = self.mPlayerData[playerUid]
				playerData["flyStateMachine"].ReceiveEvent(playerData["flyEnabled"], EventType.CloseFly, playerUid)
		else:
			logout.error("player[{}] not in server dict".format(playerUid))

	def OnEntityAreaEvent(self, args):
		# 进入黑/白名单区域时调用
		logout.info("OnEntityAreaEvent", args)
		import json
		dictArgs = json.loads(args)
		enteredEntities = dictArgs.get("enteredEntities", [])
		leftEntities = dictArgs.get("leftEntities", [])
		# 分别遍历进入/离开该区域的实体，如果有玩家，根据当前黑/白名单模式给飞行状态机发送对事件
		for entityId in enteredEntities:
			playerUid = playerUid = self.mPlayerList.get(entityId)
			logout.info("OnEntityAreaEvent", playerUid, str(self.mPlayerData))
			if playerUid not in self.mPlayerData:
				continue
			logout.info("Player[{}] enter area".format(playerUid))
			if self.mIsBlackListMode:
				playerData = self.mPlayerData[playerUid]
				playerData["flyEnabled"] = False
				playerData["flyStateMachine"].ReceiveEvent(playerData["flyEnabled"], EventType.FlyEnabledChange, playerUid)
			else:
				playerData = self.mPlayerData[playerUid]
				playerData["flyEnabled"] = True
			self.SetFlyEnable(entityId, not self.mIsBlackListMode)
		for entityId in leftEntities:
			playerUid = playerUid = self.mPlayerList.get(entityId)
			if playerUid not in self.mPlayerData:
				continue
			logout.info("Player[{}] leave area".format(playerUid))
			if not self.mIsBlackListMode:
				playerData = self.mPlayerData[playerUid]
				playerData["flyEnabled"] = False
				playerData["flyStateMachine"].ReceiveEvent(playerData["flyEnabled"], EventType.FlyEnabledChange, playerUid)
			else:
				playerData = self.mPlayerData[playerUid]
				playerData["flyEnabled"] = True
			self.SetFlyEnable(entityId, self.mIsBlackListMode)

	def Update(self):
		# tick玩家信息计算饥饿值消耗,如果self.mFlyInterval或self.mFlyCost为0不走后续逻辑
		if self.mFlyInterval == 0 or self.mFlyCost == 0:
			return
		for playerUid, playerData in self.mPlayerData.items():
			hunger = playerData.get("hunger", -1)
			flyState = playerData.get("flyState", False)
			if flyState and hunger != -1:
				# 飞行状态下tick飞行时间消耗饥饿值
				playerData["flyCnt"] += 1
				if playerData["flyCnt"] >= self.mFlyInterval:
					playerData["flyCnt"] = 0
					playerId = netgameApi.GetPlayerIdByUid(playerUid)
					playerComp = self.CreateComponent(playerId, "Minecraft", "player")
					hunger = playerComp.GetPlayerHunger()
					hunger -= self.mFlyCost
					if hunger <= 0:
						hunger = 0
					playerComp.SetPlayerHunger(hunger)
				# 如果饥饿值不满足条件发送对应事件给状态机
				if self.mHugerStopFly > 0 and hunger < self.mHugerStopFly or hunger == 0:
					playerData["flyStateMachine"].ReceiveEvent(playerData["flyEnabled"], EventType.Hungry, playerUid)

	# ------------------------------------------------------------------------------------------
	def QueryPlayerInfoCallBack(self, records, uid, dimension, pos):
		logout.info("QueryPlayerInfoCallBack: ", dimension, pos)
		if records is None or len(records) < 1:
			flyState = False
			flyCnt = 0
		else:
			flyState = records[0][0]
			flyCnt = records[0][1]
		flyStateMachine = FlyStateMachine()
		self.RegisterFlyStateMachine(flyStateMachine)
		flyEnable = True
		if self.CheckIsInArea(dimension, pos):
			logout.info("OnClientEnter player not in areas")
			# 黑名单模式下若玩家在该范围内禁止飞行
			flyEnable = not self.mIsBlackListMode
		else:
			flyEnable = self.mIsBlackListMode
		isFly = flyState == 1 and flyEnable
		playerData = {
			"flyCnt": flyCnt,
			"flyState": isFly,
			"flyEnabled": flyEnable,
			"flyStateMachine": flyStateMachine,
			"dimension": dimension
		}
		self.mPlayerData[uid] = playerData
		data = {
			"flyState": isFly,
			"flyEnable": flyEnable
		}
		playerId = netgameApi.GetPlayerIdByUid(uid)
		if isFly:
			playerData["flyStateMachine"].ChangeState(NodeId.Fly, EventType.APICall, uid)
		self.NotifyToClient(playerId, flyConsts.SyncConfigEvent, data)

	def CheckIsInArea(self, dimension, pos):
		for area in self.mFlyAreaList.values():
			if area[0] != dimension:
				continue
			if area[1] <= pos[0] <= area[4] and area[2] <= pos[1] <= area[5] and area[3] <= pos[2] <= area[6]:
				return True
		return False

	# ------------------------------------------------------------------------------------------
	def HandleDefault(self, eventType, playerUid):
		# 进入默认状态时调用
		playerId = netgameApi.GetPlayerIdByUid(playerUid)
		logout.info("HandleDefault playerId [{0}], playerUid [{1}]".format(playerId, playerUid))
		self.SetFlyState(playerId, False)
		self.mPlayerData[playerUid]["flyState"] = False
		if eventType == EventType.FlyEnabledChange:
			self.NotifyClientShowTips(playerId, "你无法在飞行区以外飞行！")
		elif eventType == EventType.CloseFly:
			self.NotifyClientShowTips(playerId, "已关闭飞行")
		elif eventType == EventType.Hungry:
			self.NotifyClientShowTips(playerId, "饥饿值较低，已关闭飞行！")
		elif eventType == EventType.APICall:
			self.NotifyClientShowTips(playerId, "已通过API关闭飞行！")

	def HandleFly(self, eventType, playerUid):
		# 进入飞行状态时调用
		playerId = netgameApi.GetPlayerIdByUid(playerUid)
		self.SetFlyState(playerId, True)
		self.mPlayerData[playerUid]["flyState"] = True
		playerComp = self.CreateComponent(playerId, "Minecraft", "player")
		hunger = playerComp.GetPlayerHunger()
		self.mPlayerData[playerUid]["hunger"] = hunger
		self.NotifyClientShowTips(playerId, "已开启飞行")

	def CanFly(self, enableFly, eventType, playerUid):
		# 如果禁飞或者非开启飞行事件直接返回false
		playerId = netgameApi.GetPlayerIdByUid(playerUid)
		if not enableFly or eventType not in [EventType.OpenFly, EventType.APICall]:
			if not enableFly:
				self.NotifyClientShowTips(playerId, "你无法在飞行区以外飞行！")
			return False
		playerComp = self.CreateComponent(playerId, "Minecraft", "player")
		hunger = playerComp.GetPlayerHunger()
		logout.info("player can fly, hunger: ", hunger)
		if self.mHugerLimit > 0 and hunger < self.mHugerLimit:
			self.NotifyClientShowTips(playerId, "饥饿值不低于{}点时才可以开启飞行".format(self.mHugerLimit))
			return False
		return True

	def CanStopFly(self, enableFly, eventType, playerUid):
		# 如果接受到的事件是关闭飞行、进入黑名单或饥饿直接返回True停止飞行
		if eventType in [EventType.CloseFly, EventType.FlyEnabledChange, EventType.Hungry]:
			return True
		return False

	def RegisterFlyStateMachine(self, flyStateMachine):
		# 注册状态机相关转换事件及回调
		# 注册状态节点
		flyStateMachine.AddNode(NodeId.Default, self.HandleDefault, None, True)
		flyStateMachine.AddNode(NodeId.Fly, self.HandleFly)
		# 注册状态转移事件
		flyStateMachine.AddEdge(NodeId.Default, NodeId.Fly, self.CanFly)
		flyStateMachine.AddEdge(NodeId.Fly, NodeId.Default, self.CanStopFly)

	# ------------------------------------------------------------------------------------------
	# 用于通知客户端做相应修改
	def SetFlyState(self, playerId, state):
		"""设置玩家飞行状态，主要用于控制客户端开启飞行按钮的状态改变"""
		args = { "state": state }
		comp = self.CreateComponent(playerId, "Minecraft", "fly")
		if comp.ChangePlayerFlyState(state):
			args["success"] = True
			self.NotifyToClient(playerId, flyConsts.ChangeFlyStateEvent, args)

	def NotifyClientShowTips(self, playerId, msg):
		"""通知客户端显示对应的tips"""
		args = { "tips": msg }
		self.NotifyToClient(playerId, flyConsts.ShowTipsEvent, args)

	def SetFlyEnable(self, playerId, enable):
		"""设置玩家是否处于禁飞区域，主要用于控制客户端开启飞行按钮的状态改变"""
		args = { "flyEnable": enable }
		self.NotifyToClient(playerId, flyConsts.ChangeFlyPermissionEvent, args)

	# ------------------------------------------------------------------------------------------
	# API
	def OpenFly(self, playerUid):
		"""
		开启飞行
		params: playerUid int 玩家uid
		"""
		if playerUid in self.mPlayerData:
			playerData = self.mPlayerData[playerUid]
			playerData["flyStateMachine"].ReceiveEvent(playerData["flyEnabled"], EventType.APICall, playerUid)
		else:
			logout.error("There is no player [{}]".format(playerUid))

	def CloseFly(self, playerUid):
		"""
		关闭飞行
		params: playerUid int 玩家uid
		"""
		if playerUid in self.mPlayerData:
			playerData = self.mPlayerData[playerUid]
			playerData["flyStateMachine"].ChangeState(NodeId.Default, EventType.APICall, playerUid)
		else:
			logout.error("There is no player [{}]".format(playerUid))

	def GetFlyState(self, playerUid):
		"""
		获取玩家飞行状态，如果玩家不存在返回None
		params: playerUid int 玩家uid
		"""
		if playerUid in self.mPlayerData:
			playerData = self.mPlayerData[playerUid]
			return playerData["flyState"]
		return None

	def GetCostAndInterval(self):
		"""
		获取飞行时间间隔与饥饿值的消耗
		return (cost, interval) 每interval秒消耗cost饥饿度
		"""
		return (self.mFlyCost, self.mFlyInterval / 30.0)

	def SetCostAndInterval(self, cost, interval):
		"""
		设置飞行时间间隔与饥饿值的消耗
		params: cost int,每interval秒消耗cost饥饿度
		params: interval int,每interval秒消耗cost饥饿度
		"""
		self.mFlyCost = cost
		self.mFlyInterval = interval * 30

	def GetHungerRequest(self):
		"""
		获取饥饿度要求
		return: (hungerLimit, hungerStopFly) 参考对应设置注释
		"""
		return (self.mHugerLimit, self.mHugerStopFly)

	def SetHungerRequest(self, hungerLimit, hungerStopFly):
		"""
		设置开启、关闭飞行的饥饿度要求
		params: hungerLimit int 开启飞行的最低饥饿度要求，低于该值无法开启飞行
		params: hungerStopFly int 关闭飞行的饥饿度阈值，飞行状态下低于该值会自动关闭飞行
		"""
		self.mHugerLimit = hungerLimit
		self.mHugerStopFly = hungerStopFly

	def GetFlyAreaList(self):
		"""
		获取飞行区域黑/白名单
		return: dict { areaName: (dimension, minX, minY, minZ, maxX, maxY, maxZ)}
		"""
		return self.mFlyAreaList

	def ClearFlyAreaList(self):
		"""清空飞行区域黑/白名单"""
		for name, area in self.mFlyAreaList.items():
			comp = self.CreateComponent("", "Minecraft", "dimension")
			if not comp.UnRegisterEntityAOIEvent(area[0], name):
				logout.error("UnRegisterEntityAOIEvent [{}] failed".format(name))
		for playerUid, playerData in self.mPlayerData.items():
			# 根据当前黑/白名单模式给玩家发送离开区域的事件
			if self.mIsBlackListMode and not playerData["flyEnabled"]:
				# 黑名单模式下在区域里面的玩家清空黑名单列表后允许飞行
				playerData["flyEnabled"] = True
			if not self.mIsBlackListMode and playerData["flyEnabled"]:
				# 白名单模式下在区域里面的玩家清空白名单列表后禁止飞行
				playerData["flyEnabled"] = False
				playerData["flyStateMachine"].ReceiveEvent(playerData["flyEnabled"], EventType.FlyEnabledChange, playerUid)
			self.SetFlyEnable(netgameApi.GetPlayerIdByUid(playerUid), self.mIsBlackListMode)

	def GetBlackListMode(self):
		"""
		获取黑/白名单模式
		return: bool 返回True则是黑名单模式，飞行区域为禁飞区域。反之则是白名单模式，飞行区域为允许飞行区域。
		"""
		return self.mIsBlackListMode

	def SetBlackListMode(self, isBlackListMode):
		"""
		设置黑/白名单模式
		params: bool True则是黑名单模式，飞行区域为禁飞区域。反之则是白名单模式，飞行区域为允许飞行区域。
		"""
		self.mIsBlackListMode = isBlackListMode
		# 切换模式后所有玩家状态改变
		for playerUid, playerData in self.mPlayerData.items():
			playerData["flyEnabled"] = not playerData["flyEnabled"]
			playerData["flyStateMachine"].ReceiveEvent(playerData["flyEnabled"], EventType.FlyEnabledChange, playerUid)
			self.SetFlyEnable(netgameApi.GetPlayerIdByUid(playerUid), self.mIsBlackListMode)

	#------------------------------------------------------------------------------------------------
	# 初始化mysql连接池
	def InitMysqlPool(self):
		# 尝试初始化mysql连接池，失败则打印ERROR日志并返回False
		try:
			mysqlPool.InitDB(20)
		except:
			logout.error("start_fly_server fail when init mysql")
			return False
		return True