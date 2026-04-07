# -*- coding: utf-8 -*-

import time
import weakref

import client.extraClientApi as clientApi
from mod_log import engine_logger as logger
import neteaseRoundScript.roundConst as roundConst
import neteaseRoundScript.battleClient.roundViewConst as roundViewConst
# --------------------------------------------------------------------------------------------------------------------------------------
def CreateAction(actionName, actionData):
	if actionData["type"] == "move":
		return RoundActionMove(actionName, actionData)
	elif actionData["type"] == "playAni":
		return RoundActionPlayAni(actionName, actionData)
	elif actionData["type"] == "applySkillResult":
		return RoundActionApplySkillResult(actionName, actionData)
	elif actionData["type"] == "createModel":
		return RoundActionCreateModel(actionName, actionData)
	elif actionData["type"] == "destroyModel":
		return RoundActionDestroyModel(actionName, actionData)
	elif actionData["type"] == "playBindEffect":
		return RoundActionPlayBindEffect(actionName, actionData)
	elif actionData["type"] == "createBindEffect":
		return RoundActionCreateBindEffect(actionName, actionData)
	elif actionData["type"] == "destroyBindEffect":
		return RoundActionDestroyBindEffect(actionName, actionData) 
	else:
		logger.error("CreateAction failed action {} is not defined".format(actionName))
		return None
# --------------------------------------------------------------------------------------------------------------------------------------
class RoundActionBase(object):
	def __init__(self, name, config):
		super(RoundActionBase, self).__init__()
		self.mUniqueName = name
		self.mConfig = config
	
	def GetName(self):
		return self.mUniqueName

	def InitFromPerform(self, performInst):
		self.mStartTimestamp = time.time()

	def AchieveCondition(self, performInst):
		for oneCond in self.mConfig["condition"]:
			if oneCond["type"] == "finAction":
				if not performInst.IsActionFinish(oneCond["param"]):
					return False
			else:	# 未定义的条件类型
				return False
		return True
	
	def DoUpdate(self):
		now = time.time()
		if now - self.mStartTimestamp >= self.mConfig["costTime"]:
			return True
		return False
	
	def DoFinish(self, performInst):
		pass
# --------------------------------------------------------------------------------------------------------------------------------------
class RoundActionMove(RoundActionBase):
	def __init__(self, name, config):
		super(RoundActionMove, self).__init__(name, config)
	
	def InitFromPerform(self, performInst):
		super(RoundActionMove, self).InitFromPerform(performInst)
		spData = performInst.GetActionActor(self.mConfig["actor"])
		if not spData:
			logger.error("RoundActionMove cannot find actor {}".format(self.mConfig["actor"]))
			return
		if spData["type"] != "model":
			logger.error("RoundActionMove not support type {}".format(spData["type"]))
			return
		startPos = performInst.GetActionPos(self.mConfig["startPos"], spData)
		endPos = performInst.GetActionPos(self.mConfig["endPos"], spData)
		performInst.mScene.mWorldComp.ModelSetPos(spData["id"], startPos)
		performInst.mScene.mWorldComp.ModelMoveTo(spData["id"], endPos, self.mConfig["costTime"])	
# --------------------------------------------------------------------------------------------------------------------------------------
class RoundActionPlayAni(RoundActionBase):
	def __init__(self, name, config):
		super(RoundActionPlayAni, self).__init__(name, config)
	
	def InitFromPerform(self, performInst):
		super(RoundActionPlayAni, self).InitFromPerform(performInst)
		spData = performInst.GetActionActor(self.mConfig["actor"])
		if not spData:
			logger.error("RoundActionPlayAni cannot find actor {}".format(self.mConfig["actor"]))
			return
		if spData["type"] != "model":
			logger.error("RoundActionPlayAni not support type {}".format(spData["type"]))
			return
		aniName = roundViewConst.GetModelAnimate(spData["modelName"], self.mConfig["animate"])
		performInst.mScene.mWorldComp.ModelPlayAnimation(spData["id"], aniName, loop=False)
	
	def DoFinish(self, performInst):
		spData = performInst.GetActionActor(self.mConfig["actor"])
		if not spData:
			return
		if spData["type"] != "model":
			return
		aniName = roundViewConst.GetModelAnimate(spData["modelName"], "stand")
		performInst.mScene.mWorldComp.ModelPlayAnimation(spData["id"], aniName, loop=True)
# --------------------------------------------------------------------------------------------------------------------------------------
class RoundActionApplySkillResult(RoundActionBase):
	def __init__(self, name, config):
		super(RoundActionApplySkillResult, self).__init__(name, config)
	
	def InitFromPerform(self, performInst):
		super(RoundActionApplySkillResult, self).InitFromPerform(performInst)
		index = self.mConfig.get("index", None)
		if index is None:
			allResult = performInst.GetSkillResultAll()
			for result in allResult:
				self.ApplyOnceResult(performInst, result)
		else:
			result = performInst.GetSkillResult(index)
			self.ApplyOnceResult(performInst, result)

	def ApplyOnceResult(self, performInst, result):
		for one in result:
			resultType = one["resultType"]
			if resultType == roundConst.SkillResultType.Damage:
				performInst.mBattle.FormatDamageResult(one)
			elif resultType == roundConst.SkillResultType.Heal:
				performInst.mBattle.FormatHealResult(one)
			elif resultType == roundConst.SkillResultType.Effect:
				performInst.mBattle.FormatEffectResult(one)
# --------------------------------------------------------------------------------------------------------------------------------------
class RoundActionCreateModel(RoundActionBase):
	def __init__(self, name, config):
		super(RoundActionCreateModel, self).__init__(name, config)
	
	def InitFromPerform(self, performInst):
		super(RoundActionCreateModel, self).InitFromPerform(performInst)
		modelName = self.mConfig["modelName"]
		aniName = roundViewConst.GetModelAnimate(modelName, self.mConfig["animate"])
		modelId = performInst.mScene.mWorldComp.ModelCreateObject(modelName, aniName)
		if modelId < 0:
			logger.error("ModelCreateObject failed. modelName={} aniName={}".format(modelName, aniName))
			return
		logger.error("ModelCreateObject . modelName={} aniName={}".format(modelName, aniName))
		performInst.mScene.mWorldComp.ModelSetScale(modelId, tuple(self.mConfig["scale"]))
		spData = {
			"type":"model", 
			"id":modelId, 
			"modelName":modelName
		}
		pos = performInst.GetActionPos(self.mConfig["pos"], spData)
		performInst.mScene.mWorldComp.ModelSetPos(modelId, pos)
		performInst.CacheOtherInstance(self.mConfig["saveName"], spData)
# --------------------------------------------------------------------------------------------------------------------------------------
class RoundActionDestroyModel(RoundActionBase):
	def __init__(self, name, config):
		super(RoundActionDestroyModel, self).__init__(name, config)
	
	def InitFromPerform(self, performInst):
		super(RoundActionDestroyModel, self).InitFromPerform(performInst)
		spData = performInst.GetActionActor(self.mConfig["actor"])
		if not spData:
			logger.error("RoundActionDestroyModel cannot find actor {}".format(self.mConfig["actor"]))
			return
		if spData["type"] != "model":
			logger.error("RoundActionDestroyModel not support type {}".format(spData["type"]))
			return
		performInst.mScene.mWorldComp.ModelRemove(spData["id"])
		performInst.ReleaseOtherInstance(self.mConfig["actor"])
# --------------------------------------------------------------------------------------------------------------------------------------
class RoundActionPlayBindEffect(RoundActionBase):
	def __init__(self, name, config):
		super(RoundActionPlayBindEffect, self).__init__(name, config)
		self.mCachedInstanceKey = []
	
	def InitFromPerform(self, performInst):
		super(RoundActionPlayBindEffect, self).InitFromPerform(performInst)
		spDataList = performInst.GetBindTarget(self.mConfig["bind"])
		if not spDataList:
			logger.error("RoundActionPlayBindEffect find bind target {} empty".format(self.mConfig["bind"]))
			return
		for spData in spDataList:
			if spData["type"] != "model":
				logger.error("RoundActionPlayBindEffect not support type {}".format(spData["type"]))
				return
		self.mCachedInstanceKey = []
		effectList = self.mConfig.get("effectList", [])
		for bindTargetData in spDataList:
			for singleConf in effectList:
				data = performInst.ApplyBindEffect(singleConf, bindTargetData)
				if data is None:
					continue
				uniqueId = performInst.GetUniqueId()
				instKey = "bindEffect%d" % uniqueId
				performInst.CacheOtherInstance(instKey, data)
				self.mCachedInstanceKey.append(instKey)
	
	def DoFinish(self, performInst):
		for instKey	in self.mCachedInstanceKey:
			performInst.DestroyOtherInstance(instKey)
		self.mCachedInstanceKey = []
		super(RoundActionPlayBindEffect, self).DoFinish(performInst)
# --------------------------------------------------------------------------------------------------------------------------------------
class RoundActionCreateBindEffect(RoundActionBase):
	def __init__(self, name, config):
		super(RoundActionCreateBindEffect, self).__init__(name, config)
	
	def InitFromPerform(self, performInst):
		super(RoundActionCreateBindEffect, self).InitFromPerform(performInst)
		spDataList = performInst.GetBindTarget(self.mConfig["bind"])
		if not spDataList:
			logger.error("RoundActionCreateBindEffect find bind target {} empty".format(self.mConfig["bind"]))
			return
		for spData in spDataList:
			if spData["type"] != "model":
				logger.error("RoundActionCreateBindEffect not support type {}".format(spData["type"]))
				return
		tempInstanceList = []
		effectList = self.mConfig.get("effectList", [])
		for bindTargetData in spDataList:
			for singleConf in effectList:
				data = performInst.ApplyBindEffect(singleConf, bindTargetData)
				if data is None:
					continue
				tempInstanceList.append(data)
		spData = {
			"type": "effectList",
			"instanceList": tempInstanceList,
		}
		performInst.CacheOtherInstance(self.mConfig["saveName"], spData)
# --------------------------------------------------------------------------------------------------------------------------------------
class RoundActionDestroyBindEffect(RoundActionBase):
	def __init__(self, name, config):
		super(RoundActionDestroyBindEffect, self).__init__(name, config)
	
	def InitFromPerform(self, performInst):
		super(RoundActionDestroyBindEffect, self).InitFromPerform(performInst)
		spData = performInst.GetActionActor(self.mConfig["actor"])
		if not spData:
			logger.error("RoundActionDestroyBindEffect cannot find actor {}".format(self.mConfig["actor"]))
			return
		performInst.DestroyOtherInstance(self.mConfig["actor"])
# --------------------------------------------------------------------------------------------------------------------------------------


		

		