# -*- coding: utf-8 -*-

import neteaseChillScript.chillConst as chillConst
import client.extraClientApi as clientApi

ClientSystem = clientApi.GetClientSystemCls()


class ChillClientSystem(ClientSystem):
	"""
	该mod的客户端类
	主要负责显示活动奖励界面及根据服务端推送下来的领取状态改变领取状态的显示
	"""
	def __init__(self, namespace, systemName):
		ClientSystem.__init__(self, namespace, systemName)
		self.mPlayerId = clientApi.GetLocalPlayerId()
		self.mChillUINode = None

		self.ListenForEvent(clientApi.GetEngineNamespace(), clientApi.GetEngineSystemName(), chillConst.UiInitFinishedEvent, self, self.OnUiInitFinished)
		self.ListenForEvent(chillConst.ModName, chillConst.ServerSystemName, chillConst.DisplayChillRewardEvent, self, self.OnDisplayChillReward)
		self.ListenForEvent(chillConst.ModName, chillConst.ServerSystemName, chillConst.PlayerRecvChillRewardEvent, self, self.OnPlayerChill)
		self.ListenForEvent(chillConst.ModName, chillConst.ServerSystemName, chillConst.PlayerAchvChillRewardEvent, self, self.OnPlayerChill)

	def Destroy(self):
		self.mChillUINode = None
		self.UnListenForEvent(clientApi.GetEngineNamespace(), clientApi.GetEngineSystemName(), chillConst.UiInitFinishedEvent, self, self.OnUiInitFinished)
		self.UnListenForEvent(chillConst.ModName, chillConst.ServerSystemName, chillConst.DisplayChillRewardEvent, self, self.OnDisplayChillReward)
		self.UnListenForEvent(chillConst.ModName, chillConst.ServerSystemName, chillConst.PlayerRecvChillRewardEvent, self, self.OnPlayerChill)
		self.UnListenForEvent(chillConst.ModName, chillConst.ServerSystemName, chillConst.PlayerAchvChillRewardEvent, self, self.OnPlayerChill)

	def OnUiInitFinished(self, *args):
		# 注册UI 详细解释参照《UI API》
		clientApi.RegisterUI(chillConst.ModName, chillConst.chillUIName, chillConst.chillUIClsPath, chillConst.chillUIScreenDef)
		# 创建UI 详细解释参照《UI API》
		clientApi.CreateUI(chillConst.ModName, chillConst.chillUIName, {"isHud": 1})
		self.mChillUINode = clientApi.GetUI(chillConst.ModName, chillConst.chillUIName)
		if self.mChillUINode:
			self.mChillUINode.InitScreen()
		else:
			print '==== %s ====' % 'create UI: %s failed' % chillConst.chillUIScreenDef

	def OnDisplayChillReward(self, data):
		"""
		处理server驱动的【显示活动奖励界面】的事件
		"""
		print 'OnDisplayChillReward', data
		if self.mChillUINode:
			self.mChillUINode.open(data)

	def OnPlayerChill(self, data):
		"""
		处理来自server的奖励领取状态刷新的事件
		"""
		print 'OnPlayerChill', data
		if self.mChillUINode:
			self.mChillUINode.refresh(data)
