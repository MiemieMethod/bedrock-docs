# -*- coding: utf-8 -*-

import time
import weakref

import client.extraClientApi as clientApi
from mod_log import engine_logger as logger
import neteaseRoundScript.roundConst as roundConst
import neteaseRoundScript.battleClient.roundViewConst as roundViewConst

# --------------------------------------------------------------------------------------------------------------------------------------
class RoundScene(object):
	def __init__(self):
		super(RoundScene, self).__init__()
		self.mSystem = None
		self.mSceneInited = False
	
	def Init(self, system):
		self.mSystem = weakref.proxy(system)
		self.mSystem.ListenForEvent(clientApi.GetEngineNamespace(), clientApi.GetEngineSystemName(), 
			"GetEntityByCoordEvent", self, self.OnClickScreen)
		self.mSceneModels = []
		self.mUIInstance = {}
		self.mWorldComp = clientApi.GetEngineCompFactory().CreateVirtualWorld(clientApi.GetLevelId())
		self.mTextBoardComp = clientApi.GetEngineCompFactory().CreateTextBoard(clientApi.GetLevelId())
		# 参战角色
		self.mMobIdToData = {}
		self.mModelIdToMob = {}
		self.mMaxUsedSpId = 0
		self.mExistSpData = {}
		# 当前活跃角色特效
		self.mActiveMobId = None
		self.mActiveMobEffects = []
		# 浮空文字
		self.mFlyingTimer = None
		self.mFlyingTextBoard = {}
		self.mWaitingFlyingTextBoard = {}
		# 技能选择对象
		self.mWaitingSelectMobs = set()
	
	def Destroy(self):
		self.mSystem.UnListenForEvent(clientApi.GetEngineNamespace(), clientApi.GetEngineSystemName(), 
			"GetEntityByCoordEvent", self, self.OnClickScreen)
		if not self.mSceneInited:
			return
		self.DestroyBattle()
		for modelId in self.mSceneModels:
			self.mWorldComp.ModelRemove(modelId)
		self.mSceneModels = []
		for ui in self.mUIInstance.itervalues():
			ui.SetRemove()
		self.mUIInstance.clear()
		self.mWorldComp.VirtualWorldDestroy()
		self.mSceneInited = False
	
	def RegisterBattleUI(self, ui):
		self.mUIObj = weakref.proxy(ui)

	def CreateBattle(self, battle):
		self.mBattleObj = weakref.proxy(battle)
		if self.mSceneInited:
			self.mWorldComp.VirtualWorldToggleVisibility(True)
		else:
			self.mWorldComp.VirtualWorldCreate()
			# self.mWorldComp.VirtualWorldSetCollidersVisible(True)
			# 战场摄像头
			self.mWorldComp.CameraSetPos((0, 15, 5))
			self.mWorldComp.CameraLookAt((0, 0, -13), (0, 1, 0))
			# 战场场景
			modelId = self.mWorldComp.ModelCreateObject("netease_round_shilaimu", "")
			self.mWorldComp.ModelSetPos(modelId, (0, -2, -22))
			self.mWorldComp.ModelSetRot(modelId, (0, 180, 0))
			self.mWorldComp.ModelSetScale(modelId, (80.0, 2.0, 60.0))
			self.mSceneModels.append(modelId)
			self.mSceneInited = True
			# 用来暂时绑血条的模型
			self.mFakeModelId = self.mWorldComp.ModelCreateObject("v_unvisible_bind", "idle")
			print "mFakeModelId", self.mFakeModelId
			self.mWorldComp.ModelSetPos(self.mFakeModelId, (0, 0, 0))
			self.mSceneModels.append(self.mFakeModelId)
			# 注册血条
			self.mUIKey = "headBloodUI"
			clientApi.RegisterUI(roundConst.ModName, self.mUIKey, "neteaseRoundScript.ui.netease_round_headUI.HeadScreen", "netease_round_headUI.main")
		# 浮空文字
		comp = clientApi.GetEngineCompFactory().CreateGame(clientApi.GetLevelId())
		self.mFlyingTimer = comp.AddRepeatedTimer(0.05, self.OnFlyingUpdate)
		# 参战角色
		for monster in self.mBattleObj.mMobDict.itervalues():
			self.CreateBattleMonster(monster)

	def DestroyBattle(self):
		if not self.mSceneInited:
			return
		if self.mFlyingTimer:
			comp = clientApi.GetEngineCompFactory().CreateGame(clientApi.GetLevelId())
			comp.CancelTimer(self.mFlyingTimer)
			self.mFlyingTimer = None
		for data in self.mFlyingTextBoard.itervalues():
			# self.mTextBoardComp.SetBoardPos(data["boardId"], (0, 10.0, 100.0))
			self.mTextBoardComp.RemoveTextBoard(data["boardId"])
		self.mFlyingTextBoard.clear()
		self.mWaitingFlyingTextBoard.clear()
		# 参战角色
		self.ClearActiveMonsterEffect()
		if self.mBattleObj:
			for monster in self.mBattleObj.mMobDict.itervalues():
				self.DestroyBattleMonster(monster)
		self.mMobIdToData.clear()
		self.mModelIdToMob.clear()
		for uniqueId in self.mExistSpData.keys():
			self.DestroyEffectById(uniqueId)
		self.mExistSpData.clear()
		self.mBattleObj = None
		self.mWaitingSelectMobs = set()
		self.mWorldComp.VirtualWorldToggleVisibility(False)
	# -------------------------------------------------------------------------------------------------------------------------------------------
	def GetStandPos(self, side, posIndex):
		if side == self.mBattleObj.mMySide:
			return roundViewConst.LeftSideToPos.get(posIndex, None)
		else:
			return roundViewConst.RightSideToPos.get(posIndex, None)
	
	def GetStandRotate(self, side):
		if side == self.mBattleObj.mMySide:
			return roundViewConst.LeftDegreeAngle, roundViewConst.RotAxis
		else:
			return roundViewConst.RightDegreeAngle, roundViewConst.RotAxis
	
	def GetHeadUIOffset(self, side, posIndex):
		if side == self.mBattleObj.mMySide:
			return roundViewConst.LeftSideToHeadUI.get(posIndex, None)
		else:
			return roundViewConst.RightSideToHeadUI.get(posIndex, None)
	
	def GetModelByMonster(self, monster):
		data = self.mMobIdToData.get(monster.mId, None)
		if not data:
			return None
		return data["modelId"]
	# -------------------------------------------------------------------------------------------------------------------------------------------
	# 血条
	def GetHeadUI(self, side, posIndex):
		if side == self.mBattleObj.mMySide:
			uiKey = "left_{}".format(posIndex)
		else:
			uiKey = "right_{}".format(posIndex)
		ui = self.mUIInstance.get(uiKey, None)
		if ui:
			return ui
		params = {
			"bindEntityId": clientApi.GetLocalPlayerId(),
			"bindOffset": (0, 2, 0),
			"autoScale": 1
		}
		ui = clientApi.CreateUI(roundConst.ModName, self.mUIKey, params)
		if not ui:
			logger.error("CreateUI fail uiKey={}".format(uiKey))
			return None
		ui.InitScreen()
		ui.ChangeNicknameShow(self.mUIObj.mIsShowNickname)
		self.mUIInstance[uiKey] = ui
		return ui
	
	def UpdateNicknameShow(self):
		for ui in self.mUIInstance.itervalues():
			ui.ChangeNicknameShow(self.mUIObj.mIsShowNickname)
	# -------------------------------------------------------------------------------------------------------------------------------------------
	# 浮空文字
	def OnFlyingUpdate(self):
		if not self.mFlyingTextBoard and not self.mWaitingFlyingTextBoard:
			return
		now = int(time.time())
		needRemove = []
		for uniqueId, data in self.mFlyingTextBoard.iteritems():
			if now >= data["endTp"]:
				needRemove.append(data)
				continue
			pos = (data["pos"][0]+data["dpos"][0], data["pos"][1]+data["dpos"][1], data["pos"][2]+data["dpos"][2])
			data["pos"] = pos
			self.mTextBoardComp.SetBoardPos(data["boardId"], pos)
		for data in needRemove:
			del self.mFlyingTextBoard[data["uniqueId"]]
			self.mTextBoardComp.RemoveTextBoard(data["boardId"])
		needAppend = []
		for uniqueId, data in self.mWaitingFlyingTextBoard.iteritems():
			if now >= data["startTp"]:
				continue
			needAppend.append(data)
		for data in needAppend:
			del self.mWaitingFlyingTextBoard[data["uniqueId"]]
			apply(self.CreateFlyingTextBorad, data["createArgs"])

	def CreateFlyingDamage(self, monster, isCrit, damage):
		text = "-%d" % damage
		basePos = self.GetStandPos(monster.mSide, monster.mPos)
		offset = self.GetHeadUIOffset(monster.mSide, monster.mPos)
		pos = (basePos[0]+offset[0], basePos[1]+offset[1], basePos[2]+offset[2])
		dpos = (3.0/20, 3.0/20, -3.0/20)
		if isCrit:
			scale = (6.0, 6.0)
			color = (1, 1, 0, 0.8)
		else:
			scale = (4.0, 4.0)
			color = (1, 0, 0, 0.8)
		self.CreateFlyingTextBorad(text, color, scale, pos, dpos, 1.5)

	def CreateFlyingHeal(self, monster, isCrit, heal):
		text = "+%d" % heal
		basePos = self.GetStandPos(monster.mSide, monster.mPos)
		offset = self.GetHeadUIOffset(monster.mSide, monster.mPos)
		pos = (basePos[0]+offset[0], basePos[1]+offset[1], basePos[2]+offset[2])
		dpos = (0, 3.0/20, -3.0/20)
		if isCrit:
			scale = (6.0, 6.0)
			color = (0, 1, 0, 0.8)
		else:
			scale = (4.0, 4.0)
			color = (0, 1, 0, 0.8)
		self.CreateFlyingTextBorad(text, color, scale, pos, dpos, 1.5)
	
	def CreateFlyingEffect(self, monster, color, text):
		basePos = self.GetStandPos(monster.mSide, monster.mPos)
		offset = self.GetHeadUIOffset(monster.mSide, monster.mPos)
		pos = (basePos[0]+offset[0], basePos[1]+offset[1], basePos[2]+offset[2])
		dpos = (0, 2.0/20, 0)
		scale = (4.0, 4.0)
		existTp = 1.5
		uniqueId = self.GetUniqueId()
		data = {
			"uniqueId": uniqueId,
			"startTp": time.time() + 0.8,
			"createArgs": (text, color, scale, pos, dpos, existTp),
		}
		self.mWaitingFlyingTextBoard[uniqueId] = data

	def CreateFlyingTextBorad(self, text, color, scale, pos, dpos, existTp):
		textBoardId = self.mTextBoardComp.CreateTextBoardInWorld(text, color, (1, 1, 1, 0.1), True)
		self.mWorldComp.MoveToVirtualWorld(clientApi.GetMinecraftEnum().VirtualWorldObjectType.Textboard, textBoardId)
		self.mTextBoardComp.SetBoardPos(textBoardId, pos)
		self.mTextBoardComp.SetBoardScale(textBoardId, scale)
		uniqueId = self.GetUniqueId()
		data = {
			"uniqueId": uniqueId,
			"boardId": textBoardId,
			"pos": pos,
			"dpos": dpos,
			"endTp": time.time() + existTp,
		}
		self.mFlyingTextBoard[uniqueId] = data
	# -------------------------------------------------------------------------------------------------------------------------------------------
	def CreateBattleMonster(self, monster):
		pos = self.GetStandPos(monster.mSide, monster.mPos)
		if not pos:
			logger.error("cannot find stand pos for side {} and pos {}".format(monster.mSide, monster.mPos))
			return
		modelName = monster.mConfig.get("modelName", None)
		if not modelName:
			logger.error("cannot find modelName config for {}".format(monster.mIdentifier))
			return
		aniStand = roundViewConst.GetModelAnimate(modelName, "stand")
		modelId = self.mWorldComp.ModelCreateObject(modelName, aniStand)
		if not modelId:
			logger.error("ModelCreateObject fail for {} with animate {}".format(modelName, aniStand))
			return
		self.mWorldComp.ModelSetPos(modelId, pos)
		degreeAngle, axis = self.GetStandRotate(monster.mSide)
		self.mWorldComp.ModelRotate(modelId, degreeAngle, axis)
		self.mWorldComp.ModelSetBoxCollider(modelId, (1.0, 2.0, 1.0), (0.0, 0.0, 0.0))
		# 血条
		ui = self.GetHeadUI(monster.mSide, monster.mPos)
		if not ui:
			return
		# print "GetHeadUI ui={} modelId={}".format(ui, modelId)
		offset = self.GetHeadUIOffset(monster.mSide, monster.mPos)
		ui.BindVirtualWorldModel(modelId, offset)
		if monster.mSide == self.mBattleObj.mMySide:
			ui.InitOnGameStart(monster.GetNickName(), True)
		else:
			ui.InitOnGameStart(monster.GetNickName(), False)
		ui.UpdateByMonster(monster)
		monster.LinkUIInstance(ui)
		# 技能目标光环
		waitingSignList = []
		spData = self.CreateEffectForBind("netease_round_guanghuan", modelId)
		waitingSignList.append(spData)
		spData = self.CreateEffectForBind("netease_round_guanghuan_lizi", modelId)
		waitingSignList.append(spData)
		#
		self.mMobIdToData[monster.mId] = {
			"modelId": modelId,
			"waitingSignList": waitingSignList,
			"modelName": modelName,
			"ui": ui,
		}
		self.mModelIdToMob[modelId] = monster.mId
		self.HideWaitingSelectSign(monster.mId)
	
	def DestroyBattleMonster(self, monster):
		data = self.mMobIdToData.get(monster.mId, None)
		if not data:
			return
		del self.mMobIdToData[monster.mId]
		# 技能目标光环
		for spData in data["waitingSignList"]:
			self.DestroyEffectByData(spData)
		# 血条
		data["ui"].BindVirtualWorldModel(self.mFakeModelId, (0, 0, 0))
		# 模型
		self.mWorldComp.ModelRemove(data["modelId"])
	
	def PlayMonsterDie(self, monster):
		data = self.mMobIdToData.get(monster.mId, None)
		if not data:
			return
		modelId = data["modelId"]
		aniName = roundViewConst.GetModelAnimate(data["modelName"], "die")
		self.mWorldComp.ModelPlayAnimation(modelId, aniName, loop=False)
	# -------------------------------------------------------------------------------------------------------------------------------------------
	def ChangeActiveMonster(self, monster):
		if monster and self.mActiveMobId == monster.mId:
			return 
		self.ClearActiveMonsterEffect()
		if not monster:
			return
		self.mActiveMobId = monster.mId
		modelId = self.GetModelByMonster(monster)
		spData = self.CreateEffectForBind("netease_round_guanghuan_big", modelId)
		self.mActiveMobEffects.append(spData)
		spData = self.CreateEffectForBind("netease_round_guanghuan_lizi_big", modelId)
		self.mActiveMobEffects.append(spData)
	
	def ClearActiveMonsterEffect(self):
		if not self.mActiveMobEffects:
			return
		for spData in self.mActiveMobEffects:
			self.DestroyEffectByData(spData)
		self.mActiveMobEffects = []
		self.mActiveMobId = None
	# -------------------------------------------------------------------------------------------------------------------------------------------
	# 技能选择释放对象
	def ShowWaitingSelectSign(self, mobId):
		data = self.mMobIdToData.get(mobId, None)
		if not data:
			return
		for spData in data["waitingSignList"]:
			self.ChangeEffectShowByData(spData, True)

	def HideWaitingSelectSign(self, mobId):
		data = self.mMobIdToData.get(mobId, None)
		if not data:
			return
		for spData in data["waitingSignList"]:
			self.ChangeEffectShowByData(spData, False)

	def EnterSkillSelect(self, mobIds):
		self.LeaveSkillSelect()
		for mobId in mobIds:
			self.ShowWaitingSelectSign(mobId)
			self.mWaitingSelectMobs.add(mobId)

	def LeaveSkillSelect(self):
		if not self.mWaitingSelectMobs:
			return
		for mobId in self.mWaitingSelectMobs:
			self.HideWaitingSelectSign(mobId)
		self.mWaitingSelectMobs = set()

	def OnClickScreen(self, args):
		# print "OnClickScreen", args
		if not self.mWaitingSelectMobs:
			return
		modelId = self.mWorldComp.CameraGetClickModel()
		if modelId < 0:
			return
		mobId = self.mModelIdToMob.get(modelId, None)
		if mobId is None:
			return
		if mobId not in self.mWaitingSelectMobs:
			return
		self.mUIObj.TrySkillTarget(mobId)
	# -------------------------------------------------------------------------------------------------------------------------------------------
	# 特效
	def GetUniqueId(self):
		self.mMaxUsedSpId += 1
		return self.mMaxUsedSpId

	def CreateEffectForBind(self, name, modelId):
		config = roundViewConst.EffectConfig.get(name, None)
		if not config:
			logger.error("CreateEffectForBind fail. {} config not exist".format(name))
			return None
		style = config.get("style", "empty")
		if style == "sfx":
			entityId = self.mSystem.CreateEngineSfxFromEditor(config["path"])
			if config.has_key("scale"):
				transComp = clientApi.GetEngineCompFactory().CreateFrameAniTrans(entityId)
				transComp.SetScale(config["scale"])
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
			entityId = self.mWorldComp.ModelCreateObject(config["model"], config["animate"])
			ObjectType = clientApi.GetMinecraftEnum().VirtualWorldObjectType.Model
		else:
			logger.error("CreateEffectForBind fail. {} style {} not support".format(name, style))
			return None
		suc = self.mWorldComp.BindModel(ObjectType, entityId, modelId, config["pos"], config["rot"], config["bone"])
		if not suc:
			logger.error("CreateEffectForBind fail. BindModel fail")
			if style == "model":
				self.mWorldComp.ModelRemove(entityId)
			else:
				self.mSystem.DestroyEntity(entityId)
			return None
		uniqueId = self.GetUniqueId()
		spData = {
			"uniqueId": uniqueId,
			"style": style,
			"entityId": entityId,
		}
		self.mExistSpData[uniqueId] = spData
		return spData
	
	def CreateEffectForFree(self, name):
		pass

	def DestroyEffectById(self, uniqueId):
		spData = self.mExistSpData.get(uniqueId, None)
		if not spData:
			return False
		del self.mExistSpData[uniqueId]
		if spData["style"] == "model":
			self.mWorldComp.ModelRemove(spData["entityId"])
		else:
			self.mSystem.DestroyEntity(spData["entityId"])
		return True
	
	def DestroyEffectByData(self, spData):
		if spData["style"] == "model":
			self.mWorldComp.ModelRemove(spData["entityId"])
		else:
			self.mSystem.DestroyEntity(spData["entityId"])
		if spData["uniqueId"] in self.mExistSpData:
			del self.mExistSpData[spData["uniqueId"]]
		return True
	
	def ChangeEffectShowById(self, uniqueId, isShow):
		spData = self.mExistSpData.get(uniqueId, None)
		if not spData:
			return False
		return self.ChangeEffectShowByData(spData, isShow)
	
	def ChangeEffectShowByData(self, spData, isShow):
		if spData["style"] == "sfx":
			controlComp = clientApi.GetEngineCompFactory().CreateFrameAniControl(spData["entityId"])
			if isShow:
				controlComp.Play()
			else:
				controlComp.Stop()
		elif spData["style"] == "particle":
			controlComp = clientApi.GetEngineCompFactory().CreateParticleControl(spData["entityId"])
			if isShow:
				controlComp.Play()
			else:
				controlComp.Stop()
		else:
			return False
		return True
	# -------------------------------------------------------------------------------------------------------------------------------------------


		

		