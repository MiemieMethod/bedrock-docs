# -*- coding: utf-8 -*-

import neteasePeaceScript.peaceConst as peaceConst
import client.extraClientApi as clientApi

ClientSystem = clientApi.GetClientSystemCls()


class PeaceClientSystem(ClientSystem):
	"""
	该mod的客户端类
	根据服务端推送下来的数据显示PVP界面
	"""

	def __init__(self, namespace, systemName):
		ClientSystem.__init__(self, namespace, systemName)
		self.mPeaceUINode = None

		self.ListenForEvent(clientApi.GetEngineNamespace(), clientApi.GetEngineSystemName(), peaceConst.UiInitFinishedEvent, self, self.OnUiInitFinished)
		self.ListenForEvent(peaceConst.ModName, peaceConst.ServerSystemName, 'DisplayPeaceBoardEvent', self, self.OnDisplayPeaceBoard)

	def Destroy(self):
		self.mPeaceUINode = None
		self.UnListenForEvent(clientApi.GetEngineNamespace(), clientApi.GetEngineSystemName(), peaceConst.UiInitFinishedEvent, self, self.OnUiInitFinished)
		self.UnListenForEvent(peaceConst.ModName, peaceConst.ServerSystemName, 'DisplayPeaceBoardEvent', self, self.OnDisplayPeaceBoard)

	def OnDisplayPeaceBoard(self, data):
		"""
		服务端通知打开PVP界面
		"""

		print 'OnDisplayPeaceBoard', data
		if self.mPeaceUINode:
			self.mPeaceUINode.open(data)

	def OnUiInitFinished(self, *args):
		# 注册UI 详细解释参照《UI API》
		clientApi.RegisterUI(peaceConst.ModName, peaceConst.peaceUIName, peaceConst.peaceUIClsPath, peaceConst.peaceUIScreenDef)
		# 创建UI 详细解释参照《UI API》
		clientApi.CreateUI(peaceConst.ModName, peaceConst.peaceUIName, {"isHud": 1})
		self.mPeaceUINode = clientApi.GetUI(peaceConst.ModName, peaceConst.peaceUIName)
		if self.mPeaceUINode:
			self.mPeaceUINode.InitScreen()
			self.NotifyToServer(  # 客户端玩家进入游戏，查询是否应生效死亡掉落保护
				'DropProtectEvent',
				{'playerId': clientApi.GetLocalPlayerId()}
			)
		else:
			print '==== %s ====' % 'create UI: %s failed' % peaceConst.peaceUIScreenDef
