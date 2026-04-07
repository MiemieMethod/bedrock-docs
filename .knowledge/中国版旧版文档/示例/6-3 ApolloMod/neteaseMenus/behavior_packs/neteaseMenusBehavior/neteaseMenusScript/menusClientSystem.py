# -*- coding: utf-8 -*-

import neteaseMenusScript.menusConst as menusConst
import client.extraClientApi as clientApi

ClientSystem = clientApi.GetClientSystemCls()


class MenusClientSystem(ClientSystem):
	"""
	该mod的客户端
	UI初始化完毕以后发请求至服务端获取主菜单配置
	"""

	def __init__(self, namespace, systemName):
		ClientSystem.__init__(self, namespace, systemName)
		self.mMenus = None
		self.mMenusUINode = None

		self.ListenForEvent(clientApi.GetEngineNamespace(), clientApi.GetEngineSystemName(), menusConst.UiInitFinishedEvent, self, self.OnUiInitFinished)
		self.ListenForEvent(menusConst.ModName, menusConst.ServerSystemName, menusConst.DisplayMenusEvent, self, self.OnDisplayMenus)

	def Destroy(self):
		self.mMenusUINode = None
		self.mMenus = None
		self.UnListenForEvent(clientApi.GetEngineNamespace(), clientApi.GetEngineSystemName(), menusConst.UiInitFinishedEvent, self, self.OnUiInitFinished)
		self.UnListenForEvent(menusConst.ModName, menusConst.ServerSystemName, menusConst.DisplayMenusEvent, self, self.OnDisplayMenus)

	def GetMenus(self):
		return self.mMenus

	def OnUiInitFinished(self, *args):
		# 后面要看下UI的创建是否需要在这个时候，而不是在收到服务器下发的展示的时候创建
		clientApi.RegisterUI(menusConst.ModName, menusConst.menusUIName, menusConst.menusUIClsPath, menusConst.menusUIScreenDef)
		clientApi.CreateUI(menusConst.ModName, menusConst.menusUIName, {"isHud": 1})

		self.mMenusUINode = clientApi.GetUI(menusConst.ModName, menusConst.menusUIName)
		if self.mMenusUINode:
			print '==== OnUiInitFinished create UI: %s success' % menusConst.menusUIScreenDef
			self.mMenusUINode.SetMenuCallback(self.OnMenuCallback)
			playerId = clientApi.GetLocalPlayerId()
			self.NotifyToServer(menusConst.DisplayMenusEvent, {"id": playerId})
		else:
			print '==== OnUiInitFinished create UI: %s failed' % menusConst.menusUIScreenDef

	def OnMenuCallback(self, index):
		print 'OnMenuCallback index: ', index
		# 通过被点击的菜单索引编号，确定对应数据是哪个
		data = self.mMenus['menusConfig'][index]
		playerId = clientApi.GetLocalPlayerId()
		eventData = {'playerId': playerId, 'order': index}
		self.BroadcastEvent(menusConst.OutputEvent.MenusNavigateEvent, eventData)

	def OnDisplayMenus(self, data):
		if not (data and self.mMenusUINode):
			logger.error('menusClientSystem OnDisplayMenus: empty uinode or data')
			return
		self.mMenus = data
		self.mMenusUINode.Refresh(data)

	def UpdateMenus(self, data):
		"""
		设置主菜单按钮状态
		详见readme
		"""
		if not (self.mMenus and self.mMenusUINode):
			logger.error('menusClientSystem UpdateMenus: empty uinode or mMenus')
			return False
		c = len(self.mMenus['menusConfig'])
		for index, enabled in data.iteritems():
			if index >= 0 and index < c:
				if enabled:
					self.mMenus['menusConfig'][index]['enabled'] = True
				else:
					self.mMenus['menusConfig'][index]['enabled'] = False
		return self.mMenusUINode.Refresh(self.mMenus)
