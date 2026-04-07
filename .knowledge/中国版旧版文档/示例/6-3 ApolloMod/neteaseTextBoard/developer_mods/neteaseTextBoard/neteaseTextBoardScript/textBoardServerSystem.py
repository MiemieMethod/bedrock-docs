# -*- coding: utf-8 -*-

import server.extraServerApi as serverApi
import neteaseTextBoardScript.textBoardConst as textBoardConst
from mod_log import logger

ServerSystem = serverApi.GetServerSystemCls()

class TextBoardServerSystem(ServerSystem):
	"""
	该mod的服务端类
	设置客户端通用显示界面
	"""

	def __init__(self, namespace, systemName):
		ServerSystem.__init__(self, namespace, systemName)
		
		self.ListenForEvent(textBoardConst.ModName, textBoardConst.ClientSystemName, textBoardConst.SendTextContentEvent, self, self.OnSendTextContentEvent)

		self.mPlayerContent = {}

	# 客户端同步内容更新，更新服务端缓存
	def OnSendTextContentEvent(self, args):
		logger.info("OnSendTextContentEvent %s", args)
		playerId = args["playerId"]
		self.mPlayerContent[playerId] = args["content"]

	# 打开通用显示界面
	def OpenTextBoard(self, playerId):
		self.NotifyToClient(playerId, textBoardConst.OpenTextBoardEvent, {})
	
	# 关闭通用显示界面
	def CloseTextBoard(self, playerId):
		self.NotifyToClient(playerId, textBoardConst.CloseTextBoardEvent, {})

	# 清空显示内容
	def ClearTextBoard(self, playerId):
		self.NotifyToClient(playerId, textBoardConst.SetTextContentEvent, {"content": ""})
	
	# 设置显示内容
	def SetTextBoard(self, playerId, content):
		self.NotifyToClient(playerId, textBoardConst.SetTextContentEvent, {"content": content})

	# 获取显示内容
	def GetTextBoard(self, playerId):
		return self.mPlayerContent[playerId] if playerId in self.mPlayerContent else None