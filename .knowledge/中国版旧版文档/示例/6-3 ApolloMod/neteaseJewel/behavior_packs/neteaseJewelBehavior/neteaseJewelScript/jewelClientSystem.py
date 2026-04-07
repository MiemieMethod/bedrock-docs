# -*- coding: utf-8 -*-

import neteaseJewelScript.jewelConst as jewelConst
import client.extraClientApi as clientApi

ClientSystem = clientApi.GetClientSystemCls()


class JewelClientSystem(ClientSystem):
	def __init__(self, namespace, systemName):
		ClientSystem.__init__(self, namespace, systemName)
		self.mPlayerId = clientApi.GetLocalPlayerId()
		self.mJewelUINode = None
		self.mOpenedUI = set()
		self.mArms = None 
		self.mGems = None 

		self.ListenForEvent(clientApi.GetEngineNamespace(), clientApi.GetEngineSystemName(), jewelConst.UiInitFinishedEvent, self, self.OnUiInitFinished)
		self.ListenForEvent(clientApi.GetEngineNamespace(), clientApi.GetEngineSystemName(), jewelConst.OnLocalPlayerStopLoading, self, self.OnLocalPlayerStopLoading)
		self.ListenForEvent(jewelConst.ModName, jewelConst.ServerSystemName, jewelConst.DisplayJewelBoardEvent, self, self.OnDisplayJewelBoard)
		self.ListenForEvent(jewelConst.ModName, jewelConst.ServerSystemName, jewelConst.SyncJewelConfigEvent, self, self.OnSyncJewelConfig)

		self.ListenForEvent(jewelConst.ModName, 'bag', 'SyncPlayerInventoryEvent', self, self.OnSyncPlayerInventory)

	def Destroy(self):
		self.mJewelUINode = None
		self.UnListenForEvent(clientApi.GetEngineNamespace(), clientApi.GetEngineSystemName(), jewelConst.UiInitFinishedEvent, self, self.OnUiInitFinished)
		self.UnListenForEvent(clientApi.GetEngineNamespace(), clientApi.GetEngineSystemName(), jewelConst.OnLocalPlayerStopLoading, self, self.OnLocalPlayerStopLoading)
		self.UnListenForEvent(jewelConst.ModName, jewelConst.ServerSystemName, jewelConst.DisplayJewelBoardEvent, self, self.OnDisplayJewelBoard)
		self.UnListenForEvent(jewelConst.ModName, jewelConst.ServerSystemName, jewelConst.SyncJewelConfigEvent, self, self.OnSyncJewelConfig)

		self.UnListenForEvent(jewelConst.ModName, 'bag', 'SyncPlayerInventoryEvent', self, self.OnSyncPlayerInventory)

	def OnUiInitFinished(self, *args):
		"""
		client原生界面初始化完成，在这个回调后可以初始化自定义的界面
		"""
		# 注册UI 详细解释参照《UI API》
		clientApi.RegisterUI(jewelConst.ModName, jewelConst.jewelUIName, jewelConst.jewelUIClsPath, jewelConst.jewelUIScreenDef)
		# 创建UI 详细解释参照《UI API》
		clientApi.CreateUI(jewelConst.ModName, jewelConst.jewelUIName, {"isHud": 1})
		self.mJewelUINode = clientApi.GetUI(jewelConst.ModName, jewelConst.jewelUIName)
		if self.mJewelUINode:
			# 设置UI显示层次为【一级弹出界面】
			self.mJewelUINode.SetLayer("", clientApi.GetMinecraftEnum().UiBaseLayer.PopUpLv1)
			self.mJewelUINode.InitScreen()
			self.mJewelUINode.InitSystem(self)
		else:
			print '==== %s ====' % 'create UI: %s failed' % jewelConst.jewelUIScreenDef

	def RegisterUIOpen(self, uiKey):
		"""
		任意弹出界面显示时调用此函数，调整原生界面的显示和响应状态
		"""
		self.mOpenedUI.add(uiKey)
		clientApi.SetResponse(False)
		clientApi.SetInputMode(1)
		clientApi.HideSlotBarGui(True)

	def RegisterUIClose(self, uiKey):
		"""
		任意弹出界面隐藏时调用此函数，当没有任何弹出界面显示时，调整原生界面的显示和响应状态
		"""
		self.mOpenedUI.discard(uiKey)
		if not self.mOpenedUI:
			clientApi.SetResponse(True)
			clientApi.SetInputMode(0)
			clientApi.HideSlotBarGui(False)

	def OnLocalPlayerStopLoading(self, args):
		"""
		此事件标识client初始化完成
		"""
		self.NotifyToServer(jewelConst.PlayerEnterEvent, {"playerId":clientApi.GetLocalPlayerId(),})

	def OnDisplayJewelBoard(self, data):
		"""
		server发送的显示/刷新宝石镶嵌界面的事件，事件信息中包含了背包信息、装备/宝石的镶嵌配置、宝石镶嵌台中装备的信息
		同时，每当任意宝石镶嵌相关的操作执行成功后，也通过此事件刷新新的背包和镶嵌中装备的信息
		"""
		# print 'OnDisplayJewel', data
		if self.mJewelUINode:
			self.mJewelUINode.Show(data)

	def OnSyncPlayerInventory(self, data):
		"""
		server发送的同步背包中物品的事件，当外部事件导致背包变化，最终在镶嵌操作时验证失败后触发。
		"""
		# print 'OnSyncPlayerInventory', data
		if self.mJewelUINode:
			self.mJewelUINode.Refresh(data)

	def OnSyncJewelConfig(self, data):
		"""
		server向client同步宝石类物品的配置信息（哪些物品输出可镶嵌宝石）
		"""
		print 'OnSyncJewelConfig', data
		self.mArms = data.get("mArms", {})
		self.mGems = data.get("mGems", {})

	def IsAvailableJewel(self, identifier, auxValue=0):
		"""
		判定某个物品是否属于可镶嵌宝石
		"""
		name = "{}:{}".format(identifier, auxValue)
		if name in self.mGems:
			return True
		if identifier in self.mGems:
			return True
		return False

	def GetAvailableSlot(self, identifier, auxValue=0):
		"""
		获取物品的可镶嵌孔的数量（非可镶嵌物品也是返回0）
		"""
		name = "{}:{}".format(identifier, auxValue)
		if name in self.mArms:
			return self.mArms[name]
		if identifier in self.mArms:
			return self.mArms[identifier]
		return 0

		