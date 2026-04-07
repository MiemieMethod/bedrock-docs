# -*- coding: utf-8 -*-

import client.extraClientApi as clientApi
import neteaseTextBoardScript.textBoardConst as textBoardConst
import neteaseTextBoardScript.ui.uiMgr as uiMgr
from neteaseTextBoardScript.ui.uiDef import UIDef
from mod_log import logger

ClientSystem = clientApi.GetClientSystemCls()


class TextBoardClientSystem(ClientSystem):
	"""
	该mod的客户端类
	根据服务端推送下来的数据显示通用显示界面
	"""

	def __init__(self, namespace, systemName):
		ClientSystem.__init__(self, namespace, systemName)
		self.mUIMgr = uiMgr.UIMgr()
		
		self.ListenForEvent(clientApi.GetEngineNamespace(), clientApi.GetEngineSystemName(), textBoardConst.UiInitFinishedEvent, self, self.OnUiInitFinished)
		self.ListenForEvent(textBoardConst.ModName, textBoardConst.ServerSystemName, textBoardConst.OpenTextBoardEvent, self, self.OnOpenTextBoard)
		self.ListenForEvent(textBoardConst.ModName, textBoardConst.ServerSystemName, textBoardConst.CloseTextBoardEvent, self, self.OnCloseTextBoard)
		self.ListenForEvent(textBoardConst.ModName, textBoardConst.ServerSystemName, textBoardConst.SetTextContentEvent, self, self.OnSetTextContent)
		self.ListenForEvent(textBoardConst.ModName, textBoardConst.ServerSystemName, textBoardConst.GetTextContentEvent, self, self.OnGetTextContent)

	def Destroy(self):
		self.UnListenForEvent(clientApi.GetEngineNamespace(), clientApi.GetEngineSystemName(), textBoardConst.UiInitFinishedEvent, self, self.OnUiInitFinished)
		if self.mUIMgr:
			self.mUIMgr.Destroy()
	
	# UI加载完成
	def OnUiInitFinished(self, args):
		self.mUIMgr.Init(self)
		self.NotifyToServer(textBoardConst.SendTextContentEvent, {"playerId": clientApi.GetLocalPlayerId(), "content": self.mUIMgr.GetUI(UIDef.TextBoardScreen).GetContent()})

	# 打开通用显示界面
	def OnOpenTextBoard(self, args):
		logger.info("OnOpenTextBoard")
		self.mUIMgr.GetUI(UIDef.TextBoardScreen).Open()
		
	# 关闭通用显示界面
	def OnCloseTextBoard(self, args):
		logger.info("OnCloseTextBoard")
		self.mUIMgr.GetUI(UIDef.TextBoardScreen).Close()

	
	# 设置通用显示界面内容
	def OnSetTextContent(self, args):
		content = args["content"]
		logger.info("OnSetTextContent: %s", content)
		self.mUIMgr.GetUI(UIDef.TextBoardScreen).SetContent(content)
		self.NotifyToServer(textBoardConst.SendTextContentEvent, {"playerId": clientApi.GetLocalPlayerId(), "content": content})
		

	# 获取通用显示界面内容
	def OnGetTextContent(self, args):
		logger.info("OnGetTextContent")
		self.NotifyToServer(textBoardConst.SendTextContentEvent, {"playerId": clientApi.GetLocalPlayerId(), "content": self.mUIMgr.GetUI(UIDef.TextBoardScreen).GetContent()})