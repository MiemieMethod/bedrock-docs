# -*- coding: utf-8 -*-

import neteaseDailyScript.dailyConst as dailyConst
import client.extraClientApi as clientApi

ClientSystem = clientApi.GetClientSystemCls()


class DailyClientSystem(ClientSystem):
	"""
	该mod的客户端类
	与服务端类通信
	显示每日登录奖励的状态
	"""

	def __init__(self, namespace, systemName):
		ClientSystem.__init__(self, namespace, systemName)
		self.mPlayerId = clientApi.GetLocalPlayerId()
		self.mDailyUINode = None

		self.ListenForEvent(clientApi.GetEngineNamespace(), clientApi.GetEngineSystemName(), dailyConst.UiInitFinishedEvent, self, self.OnUiInitFinished)
		self.ListenForEvent(dailyConst.ModName, dailyConst.ServerSystemName, dailyConst.DisplayDailyRewardEvent, self, self.OnDisplayDailyReward)  # 服务端调用接口打开每日登录奖励界面
		self.ListenForEvent(dailyConst.ModName, dailyConst.ServerSystemName, dailyConst.PlayerRecvEvent, self, self.OnPlayerRecv)  # 玩家正常领取奖励后更新每日登录奖励界面

	def Destroy(self):
		self.mDailyUINode = None
		self.UnListenForEvent(clientApi.GetEngineNamespace(), clientApi.GetEngineSystemName(), dailyConst.UiInitFinishedEvent, self, self.OnUiInitFinished)
		self.UnListenForEvent(dailyConst.ModName, dailyConst.ServerSystemName, dailyConst.DisplayDailyRewardEvent, self, self.OnDisplayDailyReward)
		self.UnListenForEvent(dailyConst.ModName, dailyConst.ServerSystemName, dailyConst.PlayerRecvEvent, self, self.OnPlayerRecv)

	def OnUiInitFinished(self, *args):
		# 注册UI 详细解释参照《UI API》
		clientApi.RegisterUI(dailyConst.ModName, dailyConst.dailyUIName, dailyConst.dailyUIClsPath, dailyConst.dailyUIScreenDef)
		# 创建UI 详细解释参照《UI API》
		clientApi.CreateUI(dailyConst.ModName, dailyConst.dailyUIName, {"isHud": 1})
		self.mDailyUINode = clientApi.GetUI(dailyConst.ModName, dailyConst.dailyUIName)
		if self.mDailyUINode:
			self.mDailyUINode.InitScreen()
		else:
			print '==== %s ====' % 'create UI: %s failed' % dailyConst.dailyUIScreenDef

	def OnDisplayDailyReward(self, data):
		print 'OnDisplayDailyReward', data
		if self.mDailyUINode:
			self.mDailyUINode.open(data)

	def OnPlayerRecv(self, data):
		print 'OnPlayerRecv', data
		if self.mDailyUINode:
			self.mDailyUINode.refresh(data)
