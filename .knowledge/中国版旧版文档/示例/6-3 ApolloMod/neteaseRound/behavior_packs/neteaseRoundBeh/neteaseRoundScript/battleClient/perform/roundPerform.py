# -*- coding: utf-8 -*-

import time
import weakref

import client.extraClientApi as clientApi
from mod_log import engine_logger as logger
import neteaseRoundScript.roundConst as roundConst
import neteaseRoundScript.battleClient.roundViewConst as roundViewConst
import neteaseRoundScript.battleClient.perform.roundPerformAction as roundPerformAction
# --------------------------------------------------------------------------------------------------------------------------------------
def CreatePerform(identifier):
	return RoundPerformBase(identifier)
# --------------------------------------------------------------------------------------------------------------------------------------
class RoundPerformBase(object):
	def __init__(self, identifier):
		super(RoundPerformBase, self).__init__()
		self.mId = None 
		self.mIdentifier = identifier
		self.mConfig = roundConst.ConfigPerformMap.get(identifier, None)
		if not self.mConfig:
			logger.error("cannot find perform config for {}".format(identifier))
			return
		self.mBattle = None
		self.mSystem = None
		self.mScene = None
		self.mTimer = None
	
	def Destroy(self):
		self.mBattle = None
		self.mSystem = None
		self.mScene = None
		self.mActor = None
		self.mTargetList = []
		self.mResultList = []
		for instKey in self.mOtherInstance.keys():
			self.DestroyOtherInstance(instKey)
		self.mOtherInstance.clear()
		if self.mTimer:
			comp = clientApi.GetEngineCompFactory().CreateGame(clientApi.GetLevelId())
			comp.CancelTimer(self.mTimer)
			self.mTimer = None
	
	def DeclearFinish(self):
		self.mBattle.OnPerformFinish(self.mId)
	
	def InitSkillPlay(self, uniqueId, battle, actor, params):
		self.mId = uniqueId
		self.mBattle = battle
		self.mSystem = battle.mSystem
		self.mScene = battle.mSystem.GetBattleScene()
		self.mActor = actor
		#
		self.mTargetList = []
		for mobId in params["targetIdList"]:
			mob = battle.GetMobById(mobId)
			if mob:
				self.mTargetList.append(mob)
		self.mResultList = params["result"]
		self.mOtherInstance = {}
		self.mWaitingApplyActions = {}
		for actionName, actionData in self.mConfig["actionData"].iteritems():
			self.mWaitingApplyActions[actionName] = roundPerformAction.CreateAction(actionName, actionData)
		self.mActions = {}
		self.mFinActions = set()
		comp = clientApi.GetEngineCompFactory().CreateGame(clientApi.GetLevelId())
		self.mTimer = comp.AddRepeatedTimer(0.1, self.UpdatePerform)
	
	def UpdatePerform(self):
		finActions = []
		for actionName, action in self.mActions.iteritems():
			isFin = action.DoUpdate()
			if isFin:
				action.DoFinish(self)
				finActions.append(actionName)
		for actionName in finActions:
			del self.mActions[actionName]
			self.mFinActions.add(actionName)
		#
		readyActions = []
		for actionName, action in self.mWaitingApplyActions.iteritems():
			if not action.AchieveCondition(self):
				continue
			readyActions.append(actionName)
			action.InitFromPerform(self)
			self.mActions[actionName] = action
		for actionName in readyActions:
			del self.mWaitingApplyActions[actionName]
		#
		if not self.mActions and not self.mWaitingApplyActions:
			self.DeclearFinish()
	# -------------------------------------------------------------------------------------------------------------------------------------------
	def IsActionFinish(self, actionName):
		return actionName in self.mFinActions
	
	def GetActionActor(self, name):
		if name == "actor":
			modelId = self.mScene.GetModelByMonster(self.mActor)
			modelName = self.mActor.mConfig.get("modelName", None)
			return {"type":"model", "id":modelId, "modelName":modelName}
		else:
			return self.mOtherInstance.get(name, None)
	
	def GetBindTarget(self, name):
		if name == "actor":
			modelId = self.mScene.GetModelByMonster(self.mActor)
			modelName = self.mActor.mConfig.get("modelName", None)
			spData = {"type":"model", "id":modelId, "modelName":modelName}
			return [spData,]
		elif name == "target":
			anchor = self.mTargetList[0]
			modelId = self.mScene.GetModelByMonster(anchor)
			modelName = anchor.mConfig.get("modelName", None)
			spData = {"type":"model", "id":modelId, "modelName":modelName}
			return [spData,]
		elif name == "allTarget":
			ret = []
			for anchor in self.mTargetList:
				modelId = self.mScene.GetModelByMonster(anchor)
				modelName = anchor.mConfig.get("modelName", None)
				spData = {"type":"model", "id":modelId, "modelName":modelName}
				ret.append(spData)
			return ret
		else:
			spData = self.mOtherInstance.get(name, None)
			if spData:
				return [spData,]
			else:
				return []
	
	def GetSpEffectPos(self, spData):
		if spData["type"] == "model":
			return self.mScene.mWorldComp.ModelGetPos(spData["id"])
		else:
			return spData.get("savePos", None)
	
	def GetActionPos(self, config, spData):
		style, basePos, offset = config
		if basePos == "standNow":
			pos = self.GetSpEffectPos(spData)
			anchor = self.mActor 
		elif basePos == "standTarget":
			anchor = self.mTargetList[0]
			pos = self.mScene.GetStandPos(anchor.mSide, anchor.mPos)
		elif basePos == "standActor":
			anchor = self.mActor 
			pos = self.mScene.GetStandPos(anchor.mSide, anchor.mPos)
		else:
			logger.error("cannot find action_pos for basePos {}".format(basePos))
			return None
		if style == "fixPoint":
			return (pos[0] + offset[0], pos[1] + offset[1], pos[2] + offset[2])
		elif style == "mirrorPoint":
			if anchor.mSide == self.mBattle.mMySide:
				return (pos[0] + offset[0], pos[1] + offset[1], pos[2] + offset[2])
			else:
				return (pos[0] - offset[0], pos[1] + offset[1], pos[2] - offset[2])
		else:
			logger.error("cannot find action_pos for style {}".format(style))
			return None
	
	def GetSkillResultAll(self):
		return self.mResultList

	def GetSkillResult(self, index):
		if index >= len(self.mResultList):
			return []
		return self.mResultList[index]

	def GetUniqueId(self):
		return self.mBattle.GetUniqueId()
	# -------------------------------------------------------------------------------------------------------------------------------------------
	def ApplyBindEffect(self, config, targetData):
		style = config.get("style", "empty")
		if style == "sfx":
			entityId = self.mSystem.CreateEngineSfxFromEditor(config["path"])
			controlComp = clientApi.GetEngineCompFactory().CreateFrameAniControl(entityId)
			controlComp.SetLoop(True)
			controlComp.Play()
			ObjectType = clientApi.GetMinecraftEnum().VirtualWorldObjectType.Sfx
		elif style == "particle":
			entityId = self.mSystem.CreateEngineParticle(config["path"], (0, 0, 0))
			controlComp = clientApi.GetEngineCompFactory().CreateParticleControl(entityId)
			controlComp.Play()
			ObjectType = clientApi.GetMinecraftEnum().VirtualWorldObjectType.Particle
		elif style == "model":
			entityId = self.mScene.mWorldComp.ModelCreateObject(config["model"], config["animate"])
			ObjectType = clientApi.GetMinecraftEnum().VirtualWorldObjectType.Model
		else:
			logger.error("ApplyBindEffect fail. {} not support".format(str(config)))
			return None
		modelId = targetData["id"]
		suc = self.mScene.mWorldComp.BindModel(ObjectType, entityId, modelId, tuple(config["pos"]), tuple(config["rot"]), config["bone"])
		if not suc:
			logger.error("ApplyBindEffect fail. BindModel fail")
			if style == "model":
				self.mScene.mWorldComp.ModelRemove(entityId)
			else:
				self.mSystem.DestroyEntity(entityId)
			return None
		spData = {
			"type": style,
			"id": entityId,
			"modelName": config.get("model", ""),
		}
		return spData
	
	# 缓存临时生成的模型、特效信息
	def CacheOtherInstance(self, instKey, spData):
		if instKey in self.mOtherInstance:
			return False 
		self.mOtherInstance[instKey] = spData
		return True

	# 释放临时生成的模型、特效信息
	def ReleaseOtherInstance(self, instKey):
		spData = self.mOtherInstance.get(instKey, None)
		if not spData:
			return
		del self.mOtherInstance[instKey]
	
	# 释放临时生成的模型、特效信息并且销毁对应的对象
	def DestroyOtherInstance(self, instKey):
		spData = self.mOtherInstance.get(instKey, None)
		if not spData:
			return
		del self.mOtherInstance[instKey]
		if spData["type"] == "model":
			self.mScene.mWorldComp.ModelRemove(spData["id"])
		elif spData["type"] == "sfx":
			self.mSystem.DestroyEntity(spData["id"])
		elif spData["type"] == "particle":
			self.mSystem.DestroyEntity(spData["id"])
		elif spData["type"] == "effectList":
			for one in spData["instanceList"]:
				if one["type"] == "model":
					self.mScene.mWorldComp.ModelRemove(one["id"])
				else:
					self.mSystem.DestroyEntity(one["id"])
	# -------------------------------------------------------------------------------------------------------------------------------------------


		

		