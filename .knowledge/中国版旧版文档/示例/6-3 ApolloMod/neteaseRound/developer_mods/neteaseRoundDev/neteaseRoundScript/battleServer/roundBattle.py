# -*- coding: utf-8 -*-

import random
import time
import weakref

import server.extraServerApi as serverApi
from mod_log import engine_logger as logger

import neteaseRoundScript.roundConst as roundConst
import neteaseRoundScript.battleServer.monster.roundMonster as roundMonster


# 创建一场新的战斗
# 暂时所有类型的战斗共享一个类
def CreateBattle(battleStyle, uniqueId, system):
	if battleStyle == roundConst.BattleStyle.PVP:
		return RoundBattle(uniqueId, battleStyle, system)
	elif battleStyle == roundConst.BattleStyle.PVE:
		return RoundBattle(uniqueId, battleStyle, system)
	else:
		raise "CreateBattle fail by wrong battleStyle [{}]".format(battleStyle)
# --------------------------------------------------------------------------------------------------------------------------------------
class RoundBattle(object):
	def __init__(self, uniqueId, battleStyle, system):
		super(RoundBattle, self).__init__()
		self.mId = uniqueId
		self.mBattleStyle = battleStyle
		self.mSystem = system
		self.mControlSideA = None 
		self.mControlSideB = None 
		self.mMaxUsedId = 0
		self.mMobDict = {}
		self.mMobPos2Id = {}
		# 当前第几回合
		self.mRoundNum = 0
		# 当前回合的行动顺序
		self.mMobOrders = []
		# 当前回合，轮到第几个角色行动
		self.mActionIndex = None 
		#
		self.mRoundState = roundConst.BattleState.BattleInit
		self.mRoundStateTick = 0
		comp = serverApi.GetEngineCompFactory().CreateGame(serverApi.GetLevelId())
		self.mRoundTimer = comp.AddRepeatedTimer(1.0, self.Tick)
		#
		self.mClientAckNeedNum = 0
		self.mBattleStartAckRecv = set()
		self.mActionSkillAckRecv = set()
		self.mBattleFinAckRecv = set()
		self.mAlreadyLeavePlayers = set()
		self.mBattleResult = None
	
	def PackSyncData(self):
		eventData = {
			"mControlSideA": self.mControlSideA,
			"mControlSideB": self.mControlSideB,
			"mId": self.mId,
			"mBattleStyle": self.mBattleStyle,
			"mMobDict": {},
			"mRoundState": self.mRoundState,
			"mRoundNum": self.mRoundNum,
		}
		for id, mob in self.mMobDict.iteritems():
			eventData["mMobDict"][id] = mob.PackSyncData()
		return eventData

	def Destroy(self):
		if self.mRoundTimer:
			comp = serverApi.GetEngineCompFactory().CreateGame(serverApi.GetLevelId())
			comp.CancelTimer(self.mRoundTimer)
			self.mRoundTimer = None
		for mob in self.mMobDict.itervalues():
			mob.Destroy()
		self.mMobDict.clear()
		self.mMobPos2Id.clear()

	def GetNewId(self):
		self.mMaxUsedId += 1
		return self.mMaxUsedId	
	# ----------------------------------------------------------------------------------------------------------------------------------
	def InitSideA(self, control, mob1, mob2, mob3, mob4, mob5):
		self.mControlSideA = control
		side = roundConst.BattleSide.SideA
		# 初始化战斗角色1
		uniqueId = self.GetNewId()
		pos = roundConst.BattlePos.StandPos1
		if mob1:
			mob = roundMonster.CreateMonsterByIdentifier(uniqueId, control, side, pos, mob1)
			mob.InitFromBattle(self.mSystem, self)
			self.mMobDict[uniqueId] = mob
			self.mMobPos2Id[(side, pos)] = uniqueId
		# 初始化战斗角色2
		uniqueId = self.GetNewId()
		pos = roundConst.BattlePos.StandPos2
		if mob2:
			mob = roundMonster.CreateMonsterByIdentifier(uniqueId, control, side, pos, mob2)
			mob.InitFromBattle(self.mSystem, self)
			self.mMobDict[uniqueId] = mob
			self.mMobPos2Id[(side, pos)] = uniqueId
		# 初始化战斗角色3
		uniqueId = self.GetNewId()
		pos = roundConst.BattlePos.StandPos3
		if mob3:
			mob = roundMonster.CreateMonsterByIdentifier(uniqueId, control, side, pos, mob3)
			mob.InitFromBattle(self.mSystem, self)
			self.mMobDict[uniqueId] = mob
			self.mMobPos2Id[(side, pos)] = uniqueId
		# 初始化战斗角色4
		uniqueId = self.GetNewId()
		pos = roundConst.BattlePos.StandPos4
		if mob4:
			mob = roundMonster.CreateMonsterByIdentifier(uniqueId, control, side, pos, mob4)
			mob.InitFromBattle(self.mSystem, self)
			self.mMobDict[uniqueId] = mob
			self.mMobPos2Id[(side, pos)] = uniqueId
		# 初始化战斗角色5
		uniqueId = self.GetNewId()
		pos = roundConst.BattlePos.StandPos5
		if mob5:
			mob = roundMonster.CreateMonsterByIdentifier(uniqueId, control, side, pos, mob5)
			mob.InitFromBattle(self.mSystem, self)
			self.mMobDict[uniqueId] = mob
			self.mMobPos2Id[(side, pos)] = uniqueId

	def InitSideB(self, control, mob1, mob2, mob3, mob4, mob5):
		self.mControlSideB = control
		side = roundConst.BattleSide.SideB
		# 初始化战斗角色1
		uniqueId = self.GetNewId()
		pos = roundConst.BattlePos.StandPos1
		if mob1:
			mob = roundMonster.CreateMonsterByIdentifier(uniqueId, control, side, pos, mob1)
			mob.InitFromBattle(self.mSystem, self)
			self.mMobDict[uniqueId] = mob
			self.mMobPos2Id[(side, pos)] = uniqueId
		# 初始化战斗角色2
		uniqueId = self.GetNewId()
		pos = roundConst.BattlePos.StandPos2
		if mob2:
			mob = roundMonster.CreateMonsterByIdentifier(uniqueId, control, side, pos, mob2)
			mob.InitFromBattle(self.mSystem, self)
			self.mMobDict[uniqueId] = mob
			self.mMobPos2Id[(side, pos)] = uniqueId
		# 初始化战斗角色3
		uniqueId = self.GetNewId()
		pos = roundConst.BattlePos.StandPos3
		if mob3:
			mob = roundMonster.CreateMonsterByIdentifier(uniqueId, control, side, pos, mob3)
			mob.InitFromBattle(self.mSystem, self)
			self.mMobDict[uniqueId] = mob
			self.mMobPos2Id[(side, pos)] = uniqueId
		# 初始化战斗角色4
		uniqueId = self.GetNewId()
		pos = roundConst.BattlePos.StandPos4
		if mob4:
			mob = roundMonster.CreateMonsterByIdentifier(uniqueId, control, side, pos, mob4)
			mob.InitFromBattle(self.mSystem, self)
			self.mMobDict[uniqueId] = mob
			self.mMobPos2Id[(side, pos)] = uniqueId
		# 初始化战斗角色5
		uniqueId = self.GetNewId()
		pos = roundConst.BattlePos.StandPos5
		if mob5:
			mob = roundMonster.CreateMonsterByIdentifier(uniqueId, control, side, pos, mob5)
			mob.InitFromBattle(self.mSystem, self)
			self.mMobDict[uniqueId] = mob
			self.mMobPos2Id[(side, pos)] = uniqueId
	# -------------------------------------------------------------------------------------------------------------------------------------------
	def Tick(self):
		self.mRoundStateTick += 1
		# 战斗准备阶段，
		# 等待所有client回应初始化战场完成后结束进入下个阶段
		# 如果超时了，那么本场战斗以平局结算
		if self.mRoundState == roundConst.BattleState.BattleStartWaitClientAck:
			if len(self.mBattleStartAckRecv) >= self.mClientAckNeedNum:
				self.OnBattleStartEnd()
			elif self.mRoundStateTick >= roundConst.BattleStartWaitTick:
				self.OnBattleFinishBegin(roundConst.BattleResult.Draw)
		# 回合开始阶段，等待一小段时间后自动进入角色行动阶段
		elif self.mRoundState == roundConst.BattleState.BattleRoundStart:
			if self.mRoundStateTick >= roundConst.BattleRoundStartWaitTick:
				self.OnActionStartBegin(0)
		# 玩家选择角色行动阶段
		# 超过最大等待时间，自动进入角色使用技能阶段
		# 玩家已经选择了技能，自动进入角色使用技能阶段
		# 角色是AI控制的，执行AI逻辑选择行动技能
		elif self.mRoundState == roundConst.BattleState.BattleActionSelect:
			if self.mRoundStateTick >= roundConst.BattleActionSelectServerTick:
				self.OnActionPlayBegin()
			else:
				mob = self.GetActionMob()
				if not mob:
					self.OnActionPlayEnd()
				if mob.mHasSelectNextSkill:
					self.OnActionPlayBegin()
				else:
					if mob.mControl == roundConst.BattleControlAI:
						mob.AIDoBattleActionSelect()
		# 角色播放技能动画阶段
		# 等待每个client的动画播放结束回应
		# 或者超过最大限制时间
		# 自动进入技能实际生效阶段
		elif self.mRoundState == roundConst.BattleState.BattleActionPlay:
			if self.mRoundStateTick >= roundConst.BattleActionPlayWaitTick:
				self.OnActionPlayEnd()
			elif len(self.mActionSkillAckRecv) >= self.mClientAckNeedNum:
				self.OnActionPlayEnd()
		# 角色技能实际生效阶段
		# 等待一小段时间后进入行动结束阶段
		elif self.mRoundState == roundConst.BattleState.BattleActionPlayEnd:
			if self.mRoundStateTick >= roundConst.BattleActionPlayEndWaitTick:
				self.OnActionFinish()
		# 角色行动完毕阶段（使用技能结束）
		# 等待一小段时间
		# 最后一个角色行动完毕，进入回合结束状态
		# 否则下一个角色开始行动
		elif self.mRoundState == roundConst.BattleState.BattleActionFin:
			if self.mRoundStateTick >= roundConst.BattleActionFinWaitTick:
				actionIndex = self.mActionIndex + 1
				if actionIndex >= len(self.mMobOrders):
					self.OnBattleRoundFinish()
				else:
					self.OnActionStartBegin(actionIndex)
		# 回合结束状态
		# 等待一小段时间，进入下一个回合
		elif self.mRoundState == roundConst.BattleState.BattleRoundFinish:
			if self.mRoundStateTick >= roundConst.BattleRoundFinishWaitTick:
				self.OnRoundStartBegin(self.mRoundNum+1)
		# 准备战斗结算状态
		# 由于战斗结算可能由任意事件触发，为了防止逻辑中断引起的各种问题，延时1秒钟才开始结算
		elif self.mRoundState == roundConst.BattleState.BattleFinishWaitServerAck:
			if self.mRoundStateTick >= 1:
				self.OnBattleFinishWaitAck()
		# 战斗结算状态
		# 等待所有client都回应结算完成
		# 一场战斗正式结束
		elif self.mRoundState == roundConst.BattleState.BattleFinishWaitClientAck:
			if len(self.mBattleFinAckRecv) >= self.mClientAckNeedNum:
				self.OnBattleFinishEnd()
			# elif self.mRoundStateTick >= roundConst.BattleFinishWaitTick:
			#	self.OnBattleFinishEnd()
	# -------------------------------------------------------------------------------------------------------------------------------------------
	# client声明战场初始化完成
	def OnBattleStartAck(self, playerId, data):
		self.mBattleStartAckRecv.add(playerId)

	def OnActionSkillSelect(self, playerId, data):
		mob = self.GetActionMob()
		if mob.mControl != playerId:
			return False, "选择使用技能失败，当前可行动角色不属于玩家控制"
		if not mob.mNextSkillIndex is None:
			return False, "选择使用技能失败，当前可行动角色已经决定了使用的技能了"
		suc, reason = mob.CheckSelectSkill(data["skillIndex"], data["skillTargets"])
		if not suc:
			return False, reason
		mob.SaveSelectSkill(data["skillIndex"], data["skillTargets"])
		return True, data

	def OnActionSkillAck(self, playerId, data):
		self.mActionSkillAckRecv.add(playerId)

	def OnBattleFinishAck(self, playerId, data):
		self.mBattleFinAckRecv.add(playerId)
	
	# 玩家离线
	# 任何状态下，都等价于client主动回应结算完成
	# 假如战斗已经进入结算状态，那么自动根据回应情况切换状态
	# 假如战斗尚未结算，那么触发结算逻辑
	def OnPlayerLeave(self, playerId):
		self.mBattleFinAckRecv.add(playerId)
		self.mAlreadyLeavePlayers.add(playerId)
		if self.mRoundState >= roundConst.BattleState.BattleFinishWaitClientAck:
			return
		if playerId == self.mControlSideA:
			self.OnBattleFinishBegin(roundConst.BattleResult.SideBWin)
		elif playerId == self.mControlSideB:
			self.OnBattleFinishBegin(roundConst.BattleResult.SideAWin)

	# 每当有角色死亡时，判定双方残留角色数量
	# 假如双方角色都死亡了，那么就进入平局结算
	# 否则还有残留未死亡角色的一方获得胜利
	def OnMobDie(self, uniqueId):
		AliveA, AliveB = 0, 0
		for mob in self.mMobDict.itervalues():
			if mob.IsDie():
				continue
			if mob.mSide == roundConst.BattleSide.SideA:
				AliveA += 1
			elif mob.mSide == roundConst.BattleSide.SideB:
				AliveB += 1
		if AliveA == 0:
			if AliveB == 0:
				self.OnBattleFinishBegin(roundConst.BattleResult.Draw)
			else:
				self.OnBattleFinishBegin(roundConst.BattleResult.SideBWin)
		elif AliveB == 0:
			self.OnBattleFinishBegin(roundConst.BattleResult.SideAWin)
	# -------------------------------------------------------------------------------------------------------------------------------------------
	def OnBattleStartBegin(self):
		self.ChangeRoundState(roundConst.BattleState.BattleStartWaitClientAck)
		self.mClientAckNeedNum = 0
		if self.mControlSideA != roundConst.BattleControlAI:
			self.mClientAckNeedNum += 1
		if self.mControlSideB != roundConst.BattleControlAI:
			self.mClientAckNeedNum += 1
		eventData = self.PackSyncData()
		self.SendToAll(roundConst.BattleServerEvent.BattleStart, eventData)
	
	def OnBattleStartEnd(self):
		round = self.mRoundNum + 1
		self.OnRoundStartBegin(round)
	
	def OnRoundStartBegin(self, round):
		suc = self.ChangeRoundState(roundConst.BattleState.BattleRoundStart)
		if not suc:
			return
		self.mRoundNum = round
		self.mMobOrders = self.GetMobOrderBySpeed()
		self.mActionIndex = 0
		eventData = {
			"mRoundState": self.mRoundState,
			"mRoundNum": self.mRoundNum,
			"mMobOrders": self.mMobOrders,
			"mActionIndex": self.mActionIndex,
		}
		self.SendToAll(roundConst.BattleServerEvent.RoundStart, eventData) 
		for mob in self.mMobDict.itervalues():
			mob.OnRoundStartBegin()
		# 暂时来说，每回合开始中间没有参杂其他逻辑
		for mob in self.mMobDict.itervalues():
			mob.OnRoundStartEnd()
		
	def OnActionStartBegin(self, actionIndex):
		suc = self.ChangeRoundState(roundConst.BattleState.BattleActionSelect)
		if not suc:
			return
		self.mActionIndex = actionIndex
		mob = self.GetActionMob()
		# 死去的怪物也会进入循环
		if mob.IsDie():
			self.OnActionStartBegin(actionIndex+1)
			return
		mob.OnActionStartBegin()
		eventData = {
			"mRoundState": self.mRoundState,
			"mRoundNum": self.mRoundNum,
			"mActionIndex": self.mActionIndex,
			"BattleActionSelectClientTick": roundConst.BattleActionSelectClientTick,
		}
		self.SendToAll(roundConst.BattleServerEvent.ActionStart, eventData)
		# 中毒后可能会死
		if mob.IsDie():
			self.OnActionFinish()
			return
		mob.OnActionStartEnd()
		# 晕眩的怪物，直接进入行动结束
		if mob.IsForbidAction():
			self.OnActionFinish()
	
	def OnActionPlayBegin(self):
		suc = self.ChangeRoundState(roundConst.BattleState.BattleActionPlay)
		if not suc:
			return
		mob = self.GetActionMob()
		eventData = mob.OnActionPlayBegin()
		self.mActionSkillAckRecv = set()
		self.SendToAll(roundConst.BattleServerEvent.SkillPlayStart, eventData)
	
	def OnActionPlayEnd(self):
		suc = self.ChangeRoundState(roundConst.BattleState.BattleActionPlayEnd)
		if not suc:
			return
		mob = self.GetActionMob()
		mob.OnActionPlayEnd()
		# 重新计算下个回合的顺序
		mobOrders = self.GetMobOrderBySpeed()
		eventData = {
			"mobOrders": mobOrders,
		}
		self.SendToAll(roundConst.BattleServerEvent.UpdateNextOrder, eventData)
			
	def OnActionFinish(self):
		suc = self.ChangeRoundState(roundConst.BattleState.BattleActionFin)
		if not suc:
			return
		mob = self.GetActionMob()
		mob.OnActionFinish()
		eventData = {
			"mRoundState": self.mRoundState,
			"mRoundNum": self.mRoundNum,
			"mActionIndex": self.mActionIndex,
		}
		self.SendToAll(roundConst.BattleServerEvent.ActionFinish, eventData)

	def OnBattleRoundFinish(self):
		suc = self.ChangeRoundState(roundConst.BattleState.BattleRoundFinish)
		if not suc:
			return
		eventData = {
			"mRoundState": self.mRoundState,
		}
		self.SendToAll(roundConst.BattleServerEvent.RoundFinish, eventData)
		for mobId in self.mMobOrders:
			mob = self.mMobDict.get(mobId, None)
			if not mob:
				continue
			mob.OnBattleRoundFinish()

	def OnBattleFinishBegin(self, battleResult):
		suc = self.ChangeRoundState(roundConst.BattleState.BattleFinishWaitServerAck)
		if not suc:
			return
		self.mBattleResult = battleResult
		
	def OnBattleFinishWaitAck(self):
		suc = self.ChangeRoundState(roundConst.BattleState.BattleFinishWaitClientAck)
		if not suc:
			return
		if self.mControlSideA != roundConst.BattleControlAI and self.mControlSideA not in self.mAlreadyLeavePlayers:
			itemList = []
			num = random.randint(1, 5)
			for i in xrange(num):
				item = {
					"itemName": "minecraft:apple",
					"auxValue": 0,
					"count": random.randint(1, 10),
				}
				itemList.append(item)
				eventData = {
					"battleId": self.mId,
					"mRoundState": self.mRoundState,
					"battleResult": self.mBattleResult,
					"itemList": itemList
				}
				self.mSystem.NotifyToClient(self.mControlSideA, roundConst.BattleServerEvent.BattleFinish, eventData)
				# todo:放进背包
		if self.mControlSideB != roundConst.BattleControlAI and self.mControlSideB not in self.mAlreadyLeavePlayers:
			itemList = []
			num = random.randint(1, 5)
			for i in xrange(num):
				item = {
					"itemName": "minecraft:apple",
					"auxValue": 0,
					"count": random.randint(1, 10),
				}
				itemList.append(item)
				eventData = {
					"battleId": self.mId,
					"mRoundState": self.mRoundState,
					"battleResult": self.mBattleResult,
					"itemList": itemList
				}
				self.mSystem.NotifyToClient(self.mControlSideB, roundConst.BattleServerEvent.BattleFinish, eventData)
				# todo:放进背包
	
	def OnBattleFinishEnd(self):
		self.mSystem.DeclareBattleEnd(self.mId)
	# -------------------------------------------------------------------------------------------------------------------------------------------
	def SendToAll(self, eventName, eventData):
		eventData["battleId"] = self.mId
		if self.mControlSideA != roundConst.BattleControlAI and self.mControlSideA not in self.mAlreadyLeavePlayers:
			self.mSystem.NotifyToClient(self.mControlSideA, eventName, eventData)
		if self.mControlSideB != roundConst.BattleControlAI and self.mControlSideB not in self.mAlreadyLeavePlayers:
			self.mSystem.NotifyToClient(self.mControlSideB, eventName, eventData)
	# -------------------------------------------------------------------------------------------------------------------------------------------
	def CmpMobSpeed(self, mobA, mobB):
		return cmp(mobB.speed, mobA.speed)
	
	# 战斗状态，一旦切换到【BattleFinishWaitServerAck】状态
	# 就不会再切换回战斗中的状态了
	def ChangeRoundState(self, state):
		if state <= roundConst.BattleState.BattleFinishWaitServerAck and self.mRoundState >= roundConst.BattleState.BattleFinishWaitServerAck:
			return False
		self.mRoundState = state
		self.mRoundStateTick = 0
		return True
	
	def GetActionMob(self):
		if self.mActionIndex >= len(self.mMobOrders):
			return None
		mobId = self.mMobOrders[self.mActionIndex]
		return self.mMobDict.get(mobId, None)
	
	def GetMobById(self, mobId):
		return self.mMobDict.get(mobId, None)

	def GetTargetAble(self, side):
		friendList = []
		enemyList = []
		for mob in self.mMobDict.itervalues():
			if mob.IsDie():
				continue
			if mob.mSide == side:
				friendList.append(mob)
			else:
				enemyList.append(mob)
		return friendList, enemyList
	
	def GetMobOrderBySpeed(self):
		propMobs = self.mMobDict.values()
		propMobs.sort(self.CmpMobSpeed)
		mobOrders = []
		for mob in propMobs:
			mobOrders.append(mob.mId)
		return mobOrders
	# -------------------------------------------------------------------------------------------------------------------------------------------
