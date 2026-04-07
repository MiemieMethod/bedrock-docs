# -*- coding: utf-8 -*-
import client.extraClientApi as extraClientApi
ClientSystem = extraClientApi.GetClientSystemCls()
import neteaseAnnounceScript.announceConsts as announceConsts
from neteaseAnnounceScript.announceConsts import ModNameSpace, ServerSystemName
from neteaseAnnounceScript.announceConsts import ClientSpecEvent, ServerSpecEvent, FloatingWindowEvent, LoginPopupEvent
import neteaseAnnounceScript.mgr.uiMgr as uiMgr
from neteaseAnnounceScript.ui.uiDef import UIDef
import neteaseAnnounceScript.mgr.mailMgr as mailMgr
import neteaseAnnounceScript.apiUtil as apiUtil

class AnnounceClientSystem(ClientSystem):
	def __init__(self, namespace, systemName):
		ClientSystem.__init__(self,namespace,systemName)
		self.mUIMgr = uiMgr.UIMgr()
		self.mMailMgr = mailMgr.MailMgr()
		# 引擎事件
		self.ListenForEvent(extraClientApi.GetEngineNamespace(), extraClientApi.GetEngineSystemName(),
							"OnScriptTickClient", self, self.OnScriptUpdate)
		self.ListenForEvent(extraClientApi.GetEngineNamespace(), extraClientApi.GetEngineSystemName(),
							"UiInitFinished", self, self.OnUiInitFinished)
		# server事件
		self.ListenForEvent(ModNameSpace, ServerSystemName, ServerSpecEvent.SyncConfig,
							self, self.OnSyncConfig)
		self.ListenForEvent(ModNameSpace, ServerSystemName, LoginPopupEvent.SyncData,
							self, self.OnLoginPopupSync)
		self.ListenForEvent(ModNameSpace, ServerSystemName, FloatingWindowEvent.SyncData,
							self, self.OnFloatWinSync)

	def Destroy(self):
		if self.mMailMgr:
			self.mMailMgr.Destroy()
		if self.mUIMgr:
			self.mUIMgr.Destroy()
		# 引擎事件
		self.UnListenForEvent(extraClientApi.GetEngineNamespace(), extraClientApi.GetEngineSystemName(),
							"OnScriptTickClient", self, self.OnScriptUpdate)
		self.UnListenForEvent(extraClientApi.GetEngineNamespace(), extraClientApi.GetEngineSystemName(),
							"UiInitFinished", self, self.OnUiInitFinished)
		# server事件
		self.UnListenForEvent(ModNameSpace, ServerSystemName, ServerSpecEvent.SyncConfig,
							self, self.OnSyncConfig)
		self.UnListenForEvent(ModNameSpace, ServerSystemName, LoginPopupEvent.SyncData,
							  self, self.OnLoginPopupSync)
		self.UnListenForEvent(ModNameSpace, ServerSystemName, FloatingWindowEvent.SyncData,
							  self, self.OnFloatWinSync)
		# service事件
		ClientSystem.Destroy(self)
	# ----------------------------------------------------------------------------------------
	# 对外提供的接口
	def OpenMainUI(self):
		ui = self.mUIMgr.GetUI(UIDef.UIMail)
		if ui:
			ui.Show()

	# 注册玩家收到邮件的回调函数
	def RegisterMailArriveCallback(self, cbFunc):
		if self.mMailMgr:
			return self.mMailMgr.RegisterMailArriveCallback(cbFunc)
		return None
	
	def UnRegisterMailArriveCallback(self, index):
		if self.mMailMgr:
			return self.mMailMgr.UnRegisterMailArriveCallback(index)
		return False
	# ------------------------------------------------------------------------------------------
	def OnScriptUpdate(self):
		pass

	def OnUiInitFinished(self, data):
		print "OnUiInitFinished"
		self.mMailMgr.Init()
		self.mUIMgr.Init()
		self.NotifyToServer(ClientSpecEvent.Enter, {"playerId":extraClientApi.GetLocalPlayerId()})

	def OnSyncConfig(self, data):
		print "OnSyncConfig version=%s" % data["version"]
		for keyname, value in data["configDict"].iteritems():
			setattr(announceConsts, keyname, value)
		# 目前客户端的唯一配置，就是主界面是否显示邮件界面入口按钮
		apiUtil.GetMailButtonUI().ReInit()

		# def callbackFunc1():
		#	print "has new mail arrive register OnSyncConfig 111"
		# index = self.RegisterMailArriveCallback(callbackFunc1)
		# print "RegisterMailArriveCallback index={}".format(index)

		# def callbackFunc2():
		#	print "has new mail arrive register OnSyncConfig 222"
		# index = self.RegisterMailArriveCallback(callbackFunc2)
		# print "RegisterMailArriveCallback index={}".format(index)
		# suc = self.UnRegisterMailArriveCallback(index)
		# print "UnRegisterMailArriveCallback suc={}".format(suc)

	def OnLoginPopupSync(self, data):
		apiUtil.GetLoginPopUI().Show(data)

	def OnFloatWinSync(self, data):
		apiUtil.GetFloatWinUI().Show(data)
	# ----------------------------------------------------------------------------------------
	def GetUiMgr(self):
		return self.mUIMgr

	def GetMailMgr(self):
		return self.mMailMgr
	# ----------------------------------------------------------------------------------------
	def ShowMailMain(self):
		ui = self.mUIMgr.GetUI(UIDef.UIMail)
		if ui:
			ui.Show()
