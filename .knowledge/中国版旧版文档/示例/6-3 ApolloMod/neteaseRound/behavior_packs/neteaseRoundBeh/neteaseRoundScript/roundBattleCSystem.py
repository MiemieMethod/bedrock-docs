# -*- coding: utf-8 -*-

import client.extraClientApi as clientApi
ClientSystem = clientApi.GetClientSystemCls()
from mod_log import engine_logger as logger

from neteaseRoundScript.roundConst import ModName, ServerBattleSystemName, BattleServerEvent, BattleClientEvent
import neteaseRoundScript.roundConst as roundConst
import neteaseRoundScript.battleClient.roundBattle as roundBattle
import neteaseRoundScript.battleClient.roundScene as roundScene
import neteaseRoundScript.ui.uiMgr as uiMgr
from neteaseRoundScript.ui.uiDef import UIDef

class RoundBattleClientSystem(ClientSystem):
	def __init__(self, namespace, systemName):
		ClientSystem.__init__(self, namespace, systemName)
		self.mPlayerId = clientApi.GetLocalPlayerId()
		self.mUid = None
		#
		self.mUIMgr = uiMgr.UIMgr()
		self.mScene = roundScene.RoundScene()
		self.mActiveBattle = None
		#
		self.ListenForEvent(clientApi.GetEngineNamespace(), clientApi.GetEngineSystemName(), "UiInitFinished", self, self.OnUiInitFinished)
		self.ListenForEvent(clientApi.GetEngineNamespace(), clientApi.GetEngineSystemName(), "PlayMusicClientEvent", self, self.OnPlayMusic)
		self.ListenForEvent(clientApi.GetEngineNamespace(), clientApi.GetEngineSystemName(), "PlaySoundClientEvent", self, self.OnPlaySound)
		self.ListenForEvent(ModName, ServerBattleSystemName, BattleServerEvent.BattleStart, self, self.OnBattleStart)
		self.ListenForEvent(ModName, ServerBattleSystemName, BattleServerEvent.RoundStart, self, self.OnRoundStart)
		self.ListenForEvent(ModName, ServerBattleSystemName, BattleServerEvent.ActionStart, self, self.OnActionStart)
		self.ListenForEvent(ModName, ServerBattleSystemName, BattleServerEvent.SkillSelectResponse, self, self.OnSkillSelectResponse)
		self.ListenForEvent(ModName, ServerBattleSystemName, BattleServerEvent.SkillPlayStart, self, self.OnSkillPlayStart)
		self.ListenForEvent(ModName, ServerBattleSystemName, BattleServerEvent.ActionFinish, self, self.OnActionFinish)
		self.ListenForEvent(ModName, ServerBattleSystemName, BattleServerEvent.RoundFinish, self, self.OnRoundFinish)
		self.ListenForEvent(ModName, ServerBattleSystemName, BattleServerEvent.BattleFinish, self, self.OnBattleFinish)
		self.ListenForEvent(ModName, ServerBattleSystemName, BattleServerEvent.MonsterAddEffect, self, self.OnMonsterAddEffect)
		self.ListenForEvent(ModName, ServerBattleSystemName, BattleServerEvent.MonsterDiscardEffect, self, self.OnMonsterDiscardEffect)
		self.ListenForEvent(ModName, ServerBattleSystemName, BattleServerEvent.MonsterUpdate, self, self.OnMonsterUpdate)
		self.ListenForEvent(ModName, ServerBattleSystemName, BattleServerEvent.EffectUpdate, self, self.OnEffectUpdate)
		self.ListenForEvent(ModName, ServerBattleSystemName, BattleServerEvent.EffectAction, self, self.OnEffectAction)
		self.ListenForEvent(ModName, ServerBattleSystemName, BattleServerEvent.EnergyRestore, self, self.OnEnergyRestore)
		self.ListenForEvent(ModName, ServerBattleSystemName, BattleServerEvent.UpdateNextOrder, self, self.OnUpdateNextOrder)

	def Destroy(self):
		self.mScene.Destroy()
		self.UnListenForEvent(clientApi.GetEngineNamespace(), clientApi.GetEngineSystemName(), "UiInitFinished", self, self.OnUiInitFinished)
		self.UnListenForEvent(clientApi.GetEngineNamespace(), clientApi.GetEngineSystemName(), "PlayMusicClientEvent", self, self.OnPlayMusic)
		self.UnListenForEvent(clientApi.GetEngineNamespace(), clientApi.GetEngineSystemName(), "PlaySoundClientEvent", self, self.OnPlaySound)
		self.UnListenForEvent(ModName, ServerBattleSystemName, BattleServerEvent.BattleStart, self, self.OnBattleStart)
		self.UnListenForEvent(ModName, ServerBattleSystemName, BattleServerEvent.RoundStart, self, self.OnRoundStart)
		self.UnListenForEvent(ModName, ServerBattleSystemName, BattleServerEvent.ActionStart, self, self.OnActionStart)
		self.UnListenForEvent(ModName, ServerBattleSystemName, BattleServerEvent.SkillSelectResponse, self, self.OnSkillSelectResponse)
		self.UnListenForEvent(ModName, ServerBattleSystemName, BattleServerEvent.SkillPlayStart, self, self.OnSkillPlayStart)
		self.UnListenForEvent(ModName, ServerBattleSystemName, BattleServerEvent.ActionFinish, self, self.OnActionFinish)
		self.UnListenForEvent(ModName, ServerBattleSystemName, BattleServerEvent.RoundFinish, self, self.OnRoundFinish)
		self.UnListenForEvent(ModName, ServerBattleSystemName, BattleServerEvent.BattleFinish, self, self.OnBattleFinish)
		self.UnListenForEvent(ModName, ServerBattleSystemName, BattleServerEvent.MonsterAddEffect, self, self.OnMonsterAddEffect)
		self.UnListenForEvent(ModName, ServerBattleSystemName, BattleServerEvent.MonsterDiscardEffect, self, self.OnMonsterDiscardEffect)
		self.UnListenForEvent(ModName, ServerBattleSystemName, BattleServerEvent.MonsterUpdate, self, self.OnMonsterUpdate)
		self.UnListenForEvent(ModName, ServerBattleSystemName, BattleServerEvent.EffectUpdate, self, self.OnEffectUpdate)
		self.UnListenForEvent(ModName, ServerBattleSystemName, BattleServerEvent.EffectAction, self, self.OnEffectAction)
		self.UnListenForEvent(ModName, ServerBattleSystemName, BattleServerEvent.EnergyRestore, self, self.OnEnergyRestore)
		self.UnListenForEvent(ModName, ServerBattleSystemName, BattleServerEvent.UpdateNextOrder, self, self.OnUpdateNextOrder)
		
	def OnUiInitFinished(self, args):
		print "OnUiInitFinished", args
		self.mUIMgr.Init(self)
		self.mScene.Init(self)
	
	# 战斗中不播放普通音乐
	def OnPlayMusic(self, args):
		if self.mActiveBattle:
			args["cancel"] = True

	# 战斗中不播放普通音效
	def OnPlaySound(self, args):
		if self.mActiveBattle:
			args["cancel"] = True

	def GetUiMgr(self):
		return self.mUIMgr
	
	def ShowDefaultControl(self, isShow):
		if isShow:
			clientApi.HideHudGUI(False)
		else:
			clientApi.HideHudGUI(True)
	# ------------------------------------------------------------------------------------------------------------------------------------------
	def GetBattleScene(self):
		return self.mScene
	
	def OnBattleStart(self, data):
		if self.mActiveBattle:
			logger.error("OnBattleStart but battle is already exist")
			self.mActiveBattle.Destroy()
			self.mActiveBattle = None
		self.mActiveBattle = roundBattle.CreateBattle(data["mBattleStyle"])
		self.mActiveBattle.UnPackSyncData(data)
		self.mActiveBattle.InitScene(self)
		# 停止渲染普通场景，开始渲染战斗场景
		ui = self.mUIMgr.GetUI(UIDef.UIBattleControl)
		self.mScene.RegisterBattleUI(ui)
		ui.RegisterBattleScene(self.mScene)
		self.mScene.CreateBattle(self.mActiveBattle)
		# 停止显示原生UI
		self.ShowDefaultControl(False)
		# 显示战斗界面
		ui = self.mUIMgr.GetUI(UIDef.UIBattleStart)
		ui.Show()

	def OnBattleStartSuccess(self):
		self.mActiveBattle.DeclareInitSceneComplete()
		ui = self.mUIMgr.GetUI(UIDef.UIBattleControl)
		ui.Show(self.mActiveBattle)

	def OnBattleClientFinish(self):
		# 停止渲染战斗场景，开始渲染普通场景
		self.mScene.DestroyBattle()
		# 显示原生UI
		self.ShowDefaultControl(True)
		self.mActiveBattle.Destroy()
		self.mActiveBattle = None
		self.NotifyToServer(roundConst.BattleClientEvent.BattleFinishAck, {"playerId":clientApi.GetLocalPlayerId()})
	
	def OnRoundStart(self, data):
		if not self.mActiveBattle:
			logger.error("recv OnRoundStart. but activeBattle not exist")
			return
		if self.mActiveBattle.mId != data["battleId"]:
			logger.error("recv OnRoundStart. but battleId {} is not fit {}".format(data["battleId"], self.mActiveBattle.mId))
			return
		self.mActiveBattle.OnRoundStart(data)

	def OnActionStart(self, data):
		if not self.mActiveBattle:
			logger.error("recv OnActionStart. but activeBattle not exist")
			return
		if self.mActiveBattle.mId != data["battleId"]:
			logger.error("recv OnActionStart. but battleId {} is not fit {}".format(data["battleId"], self.mActiveBattle.mId))
			return
		self.mActiveBattle.OnActionStart(data)

	def OnSkillSelectResponse(self, data):
		if not self.mActiveBattle:
			logger.error("recv OnSkillSelectResponse. but activeBattle not exist")
			return
		if self.mActiveBattle.mId != data["battleId"]:
			logger.error("recv OnSkillSelectResponse. but battleId {} is not fit {}".format(data["battleId"], self.mActiveBattle.mId))
			return
		self.mActiveBattle.OnSkillSelectResponse(data)

	def OnSkillPlayStart(self, data):
		if not self.mActiveBattle:
			logger.error("recv OnSkillPlayStart. but activeBattle not exist")
			return
		if self.mActiveBattle.mId != data["battleId"]:
			logger.error("recv OnSkillPlayStart. but battleId {} is not fit {}".format(data["battleId"], self.mActiveBattle.mId))
			return
		self.mActiveBattle.OnSkillPlayStart(data)

	def OnActionFinish(self, data):
		if not self.mActiveBattle:
			logger.error("recv OnActionFinish. but activeBattle not exist")
			return
		if self.mActiveBattle.mId != data["battleId"]:
			logger.error("recv OnActionFinish. but battleId {} is not fit {}".format(data["battleId"], self.mActiveBattle.mId))
			return
		self.mActiveBattle.OnActionFinish(data)

	def OnRoundFinish(self, data):
		if not self.mActiveBattle:
			logger.error("recv OnRoundFinish. but activeBattle not exist")
			return
		if self.mActiveBattle.mId != data["battleId"]:
			logger.error("recv OnRoundFinish. but battleId {} is not fit {}".format(data["battleId"], self.mActiveBattle.mId))
			return
		self.mActiveBattle.OnRoundFinish(data)

	def OnBattleFinish(self, data):
		if not self.mActiveBattle:
			logger.error("recv OnBattleFinish. but activeBattle not exist")
			return
		if self.mActiveBattle.mId != data["battleId"]:
			logger.error("recv OnBattleFinish. but battleId {} is not fit {}".format(data["battleId"], self.mActiveBattle.mId))
			return
		self.mActiveBattle.OnBattleFinish(data)

	def DoShowBattleResult(self, data):
		# 隐藏战斗界面
		ui = self.mUIMgr.GetUI(UIDef.UIBattleControl)
		ui.Close()
		itemList = data["itemList"]
		if data["battleResult"] == roundConst.BattleResult.Draw:
			ui = self.mUIMgr.GetUI(UIDef.UIBattleWin)
		elif data["battleResult"] == roundConst.BattleResult.SideAWin:
			if self.mActiveBattle.mMySide == roundConst.BattleSide.SideA:
				ui = self.mUIMgr.GetUI(UIDef.UIBattleWin)
			else:
				ui = self.mUIMgr.GetUI(UIDef.UIBattleLose)
		elif data["battleResult"] == roundConst.BattleResult.SideBWin:
			if self.mActiveBattle.mMySide == roundConst.BattleSide.SideA:
				ui = self.mUIMgr.GetUI(UIDef.UIBattleLose)
			else:
				ui = self.mUIMgr.GetUI(UIDef.UIBattleWin)
		else:
			return
		ui.Show(itemList)

	def OnMonsterAddEffect(self, data):
		if not self.mActiveBattle:
			logger.error("recv OnMonsterAddEffect. but activeBattle not exist")
			return
		if self.mActiveBattle.mId != data["battleId"]:
			logger.error("recv OnMonsterAddEffect. but battleId {} is not fit {}".format(data["battleId"], self.mActiveBattle.mId))
			return
		self.mActiveBattle.OnMonsterAddEffect(data)

	def OnMonsterDiscardEffect(self, data):
		if not self.mActiveBattle:
			logger.error("recv OnMonsterDiscardEffect. but activeBattle not exist")
			return
		if self.mActiveBattle.mId != data["battleId"]:
			logger.error("recv OnMonsterDiscardEffect. but battleId {} is not fit {}".format(data["battleId"], self.mActiveBattle.mId))
			return
		self.mActiveBattle.OnMonsterDiscardEffect(data)

	def OnMonsterUpdate(self, data):
		if not self.mActiveBattle:
			logger.error("recv OnMonsterUpdate. but activeBattle not exist")
			return
		if self.mActiveBattle.mId != data["battleId"]:
			logger.error("recv OnMonsterUpdate. but battleId {} is not fit {}".format(data["battleId"], self.mActiveBattle.mId))
			return
		self.mActiveBattle.OnMonsterUpdate(data)

	def OnEffectUpdate(self, data):
		if not self.mActiveBattle:
			logger.error("recv OnEffectUpdate. but activeBattle not exist")
			return
		if self.mActiveBattle.mId != data["battleId"]:
			logger.error("recv OnEffectUpdate. but battleId {} is not fit {}".format(data["battleId"], self.mActiveBattle.mId))
			return
		self.mActiveBattle.OnEffectUpdate(data)

	def OnEffectAction(self, data):
		if not self.mActiveBattle:
			logger.error("recv OnEffectAction. but activeBattle not exist")
			return
		if self.mActiveBattle.mId != data["battleId"]:
			logger.error("recv OnEffectAction. but battleId {} is not fit {}".format(data["battleId"], self.mActiveBattle.mId))
			return
		self.mActiveBattle.OnEffectAction(data)

	def OnEnergyRestore(self, data):
		if not self.mActiveBattle:
			logger.error("recv OnEnergyRestore. but activeBattle not exist")
			return
		if self.mActiveBattle.mId != data["battleId"]:
			logger.error("recv OnEnergyRestore. but battleId {} is not fit {}".format(data["battleId"], self.mActiveBattle.mId))
			return
		self.mActiveBattle.OnEnergyRestore(data)
	
	def OnUpdateNextOrder(self, data):
		if not self.mActiveBattle:
			logger.error("recv OnUpdateNextOrder. but activeBattle not exist")
			return
		if self.mActiveBattle.mId != data["battleId"]:
			logger.error("recv OnUpdateNextOrder. but battleId {} is not fit {}".format(data["battleId"], self.mActiveBattle.mId))
			return
		self.mActiveBattle.OnUpdateNextOrder(data)


