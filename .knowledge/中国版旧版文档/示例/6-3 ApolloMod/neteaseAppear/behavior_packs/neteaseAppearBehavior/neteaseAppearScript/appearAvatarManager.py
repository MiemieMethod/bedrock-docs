# -*- coding: utf-8 -*-

# -*- coding: utf-8 -*-
#
import weakref
import random
import time
import client.extraClientApi as clientApi
from mod_log import engine_logger as logger

from neteaseAppearScript.appearConst import ModName, ServerSystemName, ClientEvent, ServerEvent
import neteaseAppearScript.appearConst as appearConst

UseJudgeAppearType = None
JudgePos = None 
JudgeRot = None
#-----------------------------------------------------------------------------------------------------
class AppearAvatarManager(object):
	def __init__(self, system):
		self.mSystem = weakref.proxy(system)
		self.mTickTimer = None
		self.mDirtyPlayerSet = set()
		self.mExistPlayerList = []

		self.mSystem.ListenForEvent(clientApi.GetEngineNamespace(), clientApi.GetEngineSystemName(), 
			"AddPlayerAOIClientEvent", self, self.OnAddPlayer)
		self.mSystem.ListenForEvent(clientApi.GetEngineNamespace(), clientApi.GetEngineSystemName(), 
			"RemovePlayerAOIClientEvent", self, self.OnDelPlayer)
		self.mSystem.ListenForEvent(ModName, ServerSystemName, ServerEvent.PlayerDie, self, self.OnPlayerDie)
		self.mSystem.ListenForEvent(ModName, ServerSystemName, ServerEvent.JudgePosAndRot, self, self.OnJudgePosAndRot)
		self.mSystem.ListenForEvent(clientApi.GetEngineNamespace(), clientApi.GetEngineSystemName(), 
			"AttackAnimBeginClientEvent", self, self.OnAttackAnimBegin)
		self.mSystem.ListenForEvent(clientApi.GetEngineNamespace(), clientApi.GetEngineSystemName(), 
			"AttackAnimEndClientEvent", self, self.OnAttackAnimEnd)
		self.mSystem.ListenForEvent(clientApi.GetEngineNamespace(), clientApi.GetEngineSystemName(), 
			"WalkAnimBeginClientEvent", self, self.OnWalkAnimBegin)
		self.mSystem.ListenForEvent(clientApi.GetEngineNamespace(), clientApi.GetEngineSystemName(), 
			"WalkAnimEndClientEvent", self, self.OnWalkAnimEnd)
		
	def Destroy(self):
		if self.mTickTimer:
			comp = clientApi.CreateComponent(clientApi.GetLevelId(), "Minecraft", "game")
			comp.CancelTimer(self.mTickTimer)
			self.mTickTimer = None
		#
		self.mSystem.UnListenForEvent(clientApi.GetEngineNamespace(), clientApi.GetEngineSystemName(), 
			"AddPlayerAOIClientEvent", self, self.OnAddPlayer)
		self.mSystem.UnListenForEvent(clientApi.GetEngineNamespace(), clientApi.GetEngineSystemName(), 
			"RemovePlayerAOIClientEvent", self, self.OnDelPlayer)
		self.mSystem.UnListenForEvent(ModName, ServerSystemName, ServerEvent.PlayerDie, self, self.OnPlayerDie)
		self.mSystem.UnListenForEvent(ModName, ServerSystemName, ServerEvent.JudgePosAndRot, self, self.OnJudgePosAndRot)
		self.mSystem.UnListenForEvent(clientApi.GetEngineNamespace(), clientApi.GetEngineSystemName(), 
			"AttackAnimBeginClientEvent", self, self.OnAttackAnimBegin)
		self.mSystem.UnListenForEvent(clientApi.GetEngineNamespace(), clientApi.GetEngineSystemName(), 
			"AttackAnimEndClientEvent", self, self.OnAttackAnimEnd)
		self.mSystem.UnListenForEvent(clientApi.GetEngineNamespace(), clientApi.GetEngineSystemName(), 
			"WalkAnimBeginClientEvent", self, self.OnWalkAnimBegin)
		self.mSystem.UnListenForEvent(clientApi.GetEngineNamespace(), clientApi.GetEngineSystemName(), 
			"WalkAnimEndClientEvent", self, self.OnWalkAnimEnd)
		self.mSystem = None
	
	def OnServerReady(self):
		comp = clientApi.CreateComponent(clientApi.GetLevelId(), "Minecraft", "game")
		self.mTickTimer = comp.AddRepeatedTimer(0.1, self.Tick)
	
	def OnPlayerDirty(self, playerId):
		self.mDirtyPlayerSet.add(playerId)
	#------------------------------------------------------------------------------------------------
	def Tick(self):
		if not self.mDirtyPlayerSet:
			return
		for playerId in self.mExistPlayerList:
			if playerId not in self.mDirtyPlayerSet:
				continue
			isDone = self.DoCheckAppear(playerId)
			if isDone:
				self.mDirtyPlayerSet.discard(playerId)

	def DoCheckAppear(self, playerId):
		player = self.mSystem.GetPlayerByEntityId(playerId)
		if not player:
			return True
		# 首先看人物模型
		changed, active, use = player.CheckDirtyAppear(appearConst.AppearType.Body)
		if changed:
			self.DoChangeModel(player, use)
			# 人物模型一旦替换，那么剩下的外观改变操作需要延时执行
			return False
		# 接着看坐骑
		changed, active, use = player.CheckDirtyAppear(appearConst.AppearType.Mount)
		if changed:
			self.DoChangeMount(player, use)
			# 坐骑模型一旦替换，那么剩下的外观改变操作需要延时执行
			return False
		# 其他外观效果，目前只有翅膀和脚底光环
		for appearType in appearConst.AllAppearTypes:
			if appearType in (appearConst.AppearType.Body, appearConst.AppearType.Mount):
				continue
			changed, active, use = player.CheckDirtyAppear(appearType)
			if changed:
				suc = self.DoChangeOtherAppear(player, appearType, use)
				if not suc:
					return False
		return True
	#------------------------------------------------------------------------------------------------
	def OnAddPlayer(self, args):
		playerId = args['playerId']
		if playerId in self.mExistPlayerList:
			return
		self.mExistPlayerList.append(playerId)
		self.DeleteAllAppear(playerId)
	
	def OnDelPlayer(self, args):
		playerId = args['playerId']
		if playerId not in self.mExistPlayerList:
			return
		self.mExistPlayerList.remove(playerId)
		self.DeleteAllAppear(playerId)
	
	def OnPlayerDie(self, args):
		playerId = args['playerId']
		if playerId not in self.mExistPlayerList:
			return
		self.DeleteOtherAppear(playerId, [appearConst.AppearType.Wing, appearConst.AppearType.Aura])
	
	def OnJudgePosAndRot(self, args):
		appearType, style, x, y, z = args["appearType"], args["style"], float(args["x"]), float(args["y"]), float(args["z"])
		global UseJudgeAppearType, JudgePos, JudgeRot
		UseJudgeAppearType = appearType
		if style == "pos":
			JudgePos = (x, y, z)
		elif style == "rot":
			JudgeRot = (x, y, z)
		self.DeleteOtherAppear(self.mSystem.mPlayerId, [UseJudgeAppearType,])
		self.OnPlayerDirty(self.mSystem.mPlayerId)
	#------------------------------------------------------------------------------------------------
	def OnAttackAnimBegin(self, args):
		entityId = args["id"]
		player, isMount = self.mSystem.GetModelEntity(entityId)
		if player is None:
			return
		aniName = player.GetAnimateName(isMount, "attack")
		comp = clientApi.GetEngineCompFactory().CreateModel(entityId)
		comp.PlayAnim(aniName, True)
	
	def OnAttackAnimEnd(self, args):
		entityId = args["id"]
		player, isMount = self.mSystem.GetModelEntity(entityId)
		if player is None:
			return
		aniName = player.GetAnimateName(isMount, "idle")
		comp = clientApi.GetEngineCompFactory().CreateModel(entityId)
		comp.PlayAnim(aniName, True)
	
	def OnWalkAnimBegin(self, args):
		entityId = args["id"]
		player, isMount = self.mSystem.GetModelEntity(entityId)
		if player is None:
			return
		aniName = player.GetAnimateName(isMount, "walk")
		comp = clientApi.GetEngineCompFactory().CreateModel(entityId)
		comp.PlayAnim(aniName, True)
	
	def OnWalkAnimEnd(self, args):
		entityId = args["id"]
		player, isMount = self.mSystem.GetModelEntity(entityId)
		if player is None:
			return
		aniName = player.GetAnimateName(isMount, "idle")
		comp = clientApi.GetEngineCompFactory().CreateModel(entityId)
		comp.PlayAnim(aniName, True)
	#------------------------------------------------------------------------------------------------
	def DoChangeModel(self, player, use):
		modelComp = clientApi.CreateComponent(player.mPlayerId, "Minecraft", "model")
		if not use:
			suc = modelComp.ResetModel()
			if not suc:
				logger.error("DoChangeModel for {} ResetModel failed".format(player.mPlayerId))
			player.CacheActiveBody(use, None)
		else:
			appearConfig = appearConst.PropAppears[use]
			# 人物模型替换仅仅支持模型一种类型
			modelName = appearConfig["src"][1]
			modelConfig = appearConst.PropModels[modelName]
			suc = modelComp.SetModel(modelConfig["modelName"])
			if not suc:
				logger.error("DoChangeModel for {} SetModel {} failed".format(player.mPlayerId, modelName))
			player.CacheActiveBody(use, modelConfig)
		# 替换模型，清理一下翅膀和光环挂接特效
		self.DeleteOtherAppear(player.mPlayerId, [appearConst.AppearType.Wing, appearConst.AppearType.Aura])
		return True
	
	def DoChangeMount(self, player, use):
		# 如果是取消坐骑，那么由服务端处理，客户端仅清理缓存
		if not use:
			player.CacheActiveMount(use, None)
			return True
		# 如果坐骑还没有刷新出来，那么需要等待一下
		if not player.mMountId:
			return False
		modelComp = clientApi.CreateComponent(player.mMountId, "Minecraft", "model")
		appearConfig = appearConst.PropAppears[use]
		# 模型替换仅仅支持模型一种类型
		modelName = appearConfig["src"][1]
		modelConfig = appearConst.PropModels[modelName]
		modelId = modelComp.SetModel(modelConfig["modelName"])
		if modelId == -1:
			suc = False
			logger.error("DoChangeMount for {} SetModel {} failed".format(player.mPlayerId, modelConfig["modelName"]))
		else:
			suc = True
		print "DoChangeMount for {} SetModel {} suc={}".format(player.mPlayerId, modelConfig["modelName"], suc)
		player.CacheActiveMount(use, modelConfig)
		# 替换坐骑，清理一下光环特效
		self.DeleteOtherAppear(player.mPlayerId, [appearConst.AppearType.Aura,])
		return True
	
	def DoChangeOtherAppear(self, player, appearType, use):
		# 先清理一下原有的特效
		effectIds = player.GetAppearInstance(appearType)
		for idData in effectIds:
			self.DestroyAppearInstance(idData)
		player.CleanActiveAppear(appearType)
		if not use:
			return
		player.CacheActiveAppear(appearType, use)
		appearConfig = appearConst.PropAppears[use]
		length = len(appearConfig["src"]) // 2
		for i in xrange(length):
			srcType, srcName = appearConfig["src"][i*2], appearConfig["src"][i*2+1]
			if srcType == "model":
				srcConfig = appearConst.PropModels[srcName]
				idData = self.DoAddModelEffect(player, srcConfig)
			elif srcType == "effect":
				srcConfig = appearConst.PropEffects[srcName]
				if srcConfig["type"] == "sfx":
					idData = self.DoAddSfxEffect(player, srcConfig)
				else:
					idData = self.DoAddParticleEffect(player, srcConfig)
			else:
				logger.error("DoChangeOtherAppear config not exist type={} name={}".format(srcType, srcName))
				continue
			if idData:
				player.CacheAppearInstance(appearType, idData)
			else:
				logger.error("DoChangeOtherAppear create failed type={} name={}".format(srcType, srcName))
	#------------------------------------------------------------------------------------------------
	def DeleteOtherAppear(self, playerId, appearTypeList):
		player = self.mSystem.GetPlayerByEntityId(playerId)
		if not player:
			return
		for appearType in appearTypeList:
			effectIds = player.GetAppearInstance(appearType)
			for idData in effectIds:
				self.DestroyAppearInstance(idData)
			player.CleanActiveAppear(appearType)

	def DeleteAllAppear(self, playerId):
		player = self.mSystem.GetPlayerByEntityId(playerId)
		if not player:
			return
		for appearType in appearConst.AllAppearTypes:
			# 坐骑和本体模型，会自动删除，只要更新脚本中的信息就可以了
			if appearType in (appearConst.AppearType.Body, appearConst.AppearType.Mount):
				player.CleanActiveAppear(appearType)
			else:	# 其他效果，要主动删除
				effectIds = player.GetAppearInstance(appearType)
				for idData in effectIds:
					self.DestroyAppearInstance(idData)
				player.CleanActiveAppear(appearType)
	
	def DestroyAppearInstance(self, idData):
		style = idData[0]
		if style == "model":
			effectId, modelId = idData[1], idData[2]
			otherModelComp = clientApi.GetEngineCompFactory().CreateModel(modelId)
			otherModelComp.UnBindModelToModel(effectId)
		else:
			effectId = idData[1]
			self.mSystem.DestroyEntity(effectId)
	
	def DoAddModelEffect(self, player, srcConfig):
		modelName, bindBone, aniName, pos, rot = srcConfig["modelName"], srcConfig["bindBone"], srcConfig["aniName"], tuple(srcConfig["pos"]), tuple(srcConfig["rot"])
		#effectId = self.mSystem.CreateEngineEffect(path, player.mPlayerId, aniName)

		if UseJudgeAppearType:
			if JudgePos:
				pos = JudgePos
			if JudgeRot:
				rot = JudgeRot
		
		modelComp = clientApi.GetEngineCompFactory().CreateModel(player.mPlayerId)
		modelId = modelComp.GetModelId()
		otherModelComp = clientApi.GetEngineCompFactory().CreateModel(modelId)
		effectId = otherModelComp.BindModelToModel(bindBone, modelName, pos, rot)
		#print "DoAddModelEffect effectId={}".format(effectId)
		if not effectId:
			return None
		otherModelComp.ModelPlayAni(effectId, aniName, True)

		return "model", effectId, modelId

	def DoAddSfxEffect(self, player, srcConfig):
		path, bindBone, pos, rot = srcConfig["path"], srcConfig["bindBone"], tuple(srcConfig["pos"]), tuple(srcConfig["rot"])
		if player.mMountId:
			pos, rot = tuple(srcConfig.get("pos4mount", pos)), tuple(srcConfig.get("rot4mount", pos))
		
		if UseJudgeAppearType:
			if JudgePos:
				pos = JudgePos
			if JudgeRot:
				rot = JudgeRot

		effectId = self.mSystem.CreateEngineSfxFromEditor(path)
		#print "DoAddSfxEffect effectId={}".format(effectId)
		if not effectId:
			return None
		modelComp = clientApi.GetEngineCompFactory().CreateModel(player.mPlayerId)
		modelId = modelComp.GetModelId()

		bindComp = clientApi.GetEngineCompFactory().CreateFrameAniSkeletonBind(effectId)
		bindComp.Bind(modelId, bindBone, pos, rot)
		controlComp = clientApi.CreateComponent(effectId, "Minecraft", "frameAniControl")
		controlComp.Play()

		return "sfx", effectId

	def DoAddParticleEffect(self, player, srcConfig):
		path, bindBone, pos, rot = srcConfig["path"], srcConfig["bindBone"], tuple(srcConfig["pos"]), tuple(srcConfig["rot"])
		if player.mMountId:
			pos, rot = tuple(srcConfig.get("pos4mount", pos)), tuple(srcConfig.get("rot4mount", pos))

		if UseJudgeAppearType:
			if JudgePos:
				pos = JudgePos
			if JudgeRot:
				rot = JudgeRot

		effectId = self.mSystem.CreateEngineParticle(path, (0,0,0))
		#print "DoAddParticleEffect effectId={}".format(effectId)
		if not effectId:
			return None
		modelComp = clientApi.GetEngineCompFactory().CreateModel(player.mPlayerId)
		modelId = modelComp.GetModelId()

		bindComp = clientApi.GetEngineCompFactory().CreateParticleSkeletonBind(effectId)
		bindComp.Bind(modelId, bindBone, pos, rot)
		controlComp = clientApi.CreateComponent(effectId, "Minecraft", "particleControl")
		controlComp.Play()
		
		return "particle", effectId
	#------------------------------------------------------------------------------------------------