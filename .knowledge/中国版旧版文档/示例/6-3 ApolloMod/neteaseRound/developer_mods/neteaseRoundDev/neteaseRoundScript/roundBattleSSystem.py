# -*- coding: utf-8 -*-

import random

import server.extraServerApi as serverApi
ServerSystem = serverApi.GetServerSystemCls()
import lobbyGame.netgameApi as lobbyGameApi
import apolloCommon.commonNetgameApi as commonNetgameApi
from mod_log import engine_logger as logger

from neteaseRoundScript.roundConst import ModName, ClientBattleSystemName, BattleClientEvent, BattleServerEvent
import neteaseRoundScript.roundConst as roundConst
import neteaseRoundScript.battleServer.roundBattle as roundBattle

class RoundBattleServerSystem(ServerSystem):
	def __init__(self, namespace, systemName):
		ServerSystem.__init__(self, namespace, systemName)
		self.mMaxBattleId = 0
		self.mBattleMap = {}
		self.mPlayer2Battle = {}

		self.ListenForEvent(ModName, ClientBattleSystemName, BattleClientEvent.BattleStartAck, self, self.OnBattleStartAck)
		self.ListenForEvent(ModName, ClientBattleSystemName, BattleClientEvent.ActionSkillSelect, self, self.OnActionSkillSelect)
		self.ListenForEvent(ModName, ClientBattleSystemName, BattleClientEvent.ActionSkillAck, self, self.OnActionSkillAck)
		self.ListenForEvent(ModName, ClientBattleSystemName, BattleClientEvent.BattleFinishAck, self, self.OnBattleFinishAck)

	def Destroy(self):
		self.UnListenForEvent(ModName, ClientBattleSystemName, BattleClientEvent.BattleStartAck, self, self.OnBattleStartAck)
		self.UnListenForEvent(ModName, ClientBattleSystemName, BattleClientEvent.ActionSkillSelect, self, self.OnActionSkillSelect)
		self.UnListenForEvent(ModName, ClientBattleSystemName, BattleClientEvent.ActionSkillAck, self, self.OnActionSkillAck)
		self.UnListenForEvent(ModName, ClientBattleSystemName, BattleClientEvent.BattleFinishAck, self, self.OnBattleFinishAck)

	def GetNewId(self):
		self.mMaxBattleId += 1
		return self.mMaxBattleId
	# ---------------------------------------------------------------------------------------------------------------------------------------------
	def GetBattleMobs(self, entityId):
		base = ["neteaseRound:yohko", "neteaseRound:yohko", "neteaseRound:yohko", "neteaseRound:yuki", "neteaseRound:yuki", "neteaseRound:yuki"]
		random.shuffle(base)
		return base[:5]
	
	def GetBattleByPlayerId(self, playerId):
		uniqueId = self.mPlayer2Battle.get(playerId, None)
		if uniqueId is None:
			return None 
		return self.mBattleMap.get(uniqueId, None)
	
	def GetBattle(self, uniqueId):
		return self.mBattleMap.get(uniqueId, None)
	# ---------------------------------------------------------------------------------------------------------------------------------------------
	def CreatePVPBattle(self, srcPlayer, tarPlayer):
		uniqueId = self.GetNewId()
		battle = roundBattle.CreateBattle(roundConst.BattleStyle.PVP, uniqueId, self)
		self.mBattleMap[uniqueId] = battle
		#
		mobs = srcPlayer.GetBattleMobs()
		battle.InitSideA(srcPlayer.mPlayerId, mobs[0], mobs[1], mobs[2], mobs[3], mobs[4])
		self.mPlayer2Battle[srcPlayer.mPlayerId] = uniqueId
		mobs = tarPlayer.GetBattleMobs()
		battle.InitSideB(tarPlayer.mPlayerId, mobs[0], mobs[1], mobs[2], mobs[3], mobs[4])
		self.mPlayer2Battle[tarPlayer.mPlayerId] = uniqueId
		#
		battle.OnBattleStartBegin()
		print "CreatePVPBattle uniqueI={}".format(uniqueId)

	def CreatePVEBattle(self, srcPlayer, entityId):
		print "CreatePVEBattle", srcPlayer, entityId
		uniqueId = self.GetNewId()
		battle = roundBattle.CreateBattle(roundConst.BattleStyle.PVE, uniqueId, self)
		self.mBattleMap[uniqueId] = battle
		#
		mobs = srcPlayer.GetBattleMobs()
		battle.InitSideA(srcPlayer.mPlayerId, mobs[0], mobs[1], mobs[2], mobs[3], mobs[4])
		self.mPlayer2Battle[srcPlayer.mPlayerId] = uniqueId
		mobs = self.GetBattleMobs(entityId)
		battle.InitSideB(roundConst.BattleControlAI, mobs[0], mobs[1], mobs[2], mobs[3], mobs[4])
		#
		battle.OnBattleStartBegin()
		print "CreatePVEBattle uniqueI={}".format(uniqueId)
	
	def DeclareBattleEnd(self, uniqueId):
		print "DeclareBattleEnd uniqueId={} start".format(uniqueId)
		battle = self.mBattleMap.get(uniqueId, None)
		if not battle:
			return
		battle.Destroy()
		del self.mBattleMap[uniqueId]
		if battle.mControlSideA in self.mPlayer2Battle:
			del self.mPlayer2Battle[battle.mControlSideA]
		if battle.mControlSideB in self.mPlayer2Battle:
			del self.mPlayer2Battle[battle.mControlSideB]
		print "DeclareBattleEnd uniqueId={} finish".format(uniqueId)
	# ---------------------------------------------------------------------------------------------------------------------------------------------
	def OnBattleStartAck(self, data):
		battle = self.GetBattleByPlayerId(data["playerId"])
		if not battle:
			return
		battle.OnBattleStartAck(data["playerId"], data)
	
	def OnActionSkillSelect(self, data):
		battle = self.GetBattleByPlayerId(data["playerId"])
		if not battle:
			return
		suc, reasonOrDetail = battle.OnActionSkillSelect(data["playerId"], data)
		if suc:
			eventData = {"suc": True, "message":""}
			eventData.update(reasonOrDetail)
			battle.SendToAll(BattleServerEvent.SkillSelectResponse, eventData)
		else:
			eventData = {"suc": False, "message":reasonOrDetail, "battleId":battle.mId}
			self.NotifyToClient(data["playerId"], BattleServerEvent.SkillSelectResponse, eventData)

	def OnActionSkillAck(self, data):
		battle = self.GetBattleByPlayerId(data["playerId"])
		if not battle:
			return
		battle.OnActionSkillAck(data["playerId"], data)

	def OnBattleFinishAck(self, data):
		battle = self.GetBattleByPlayerId(data["playerId"])
		if not battle:
			return
		battle.OnBattleFinishAck(data["playerId"], data)
	
	def OnPlayerLeave(self, playerId):
		battle = self.GetBattleByPlayerId(playerId)
		if not battle:
			return
		battle.OnPlayerLeave(playerId)
	# ---------------------------------------------------------------------------------------------------------------------------------------------
	# ---------------------------------------------------------------------------------------------------------------------------------------------
	

	
		
		




