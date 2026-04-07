# -*- coding: utf-8 -*-

import client.extraClientApi as clientApi
import neteaseInputBoardScript.inputBoardConst as inputBoardConst
import neteaseInputBoardScript.ui.uiMgr as uiMgr
from neteaseInputBoardScript.ui.uiDef import UIDef
from mod_log import logger

ClientSystem = clientApi.GetClientSystemCls()


class InputBoardClientSystem(ClientSystem):
	"""
	该mod的客户端类
	根据服务端推送下来的数据显示输入界面
	"""

	def __init__(self, namespace, systemName):
		ClientSystem.__init__(self, namespace, systemName)
		self.mPlayerId = clientApi.GetLocalPlayerId()
		self.mUIMgr = uiMgr.UIMgr()
		
		self.ListenForEvent(clientApi.GetEngineNamespace(), clientApi.GetEngineSystemName(), inputBoardConst.UiInitFinishedEvent, self, self.OnUiInitFinished)
		self.ListenForEvent(inputBoardConst.ModName, inputBoardConst.ServerSystemName, inputBoardConst.OpenInputBoardEvent, self, self.OnOpenInputBoard)
		self.ListenForEvent(inputBoardConst.ModName, inputBoardConst.ServerSystemName, inputBoardConst.CloseInputBoardEvent, self, self.OnCloseInputBoard)
		self.ListenForEvent(inputBoardConst.ModName, inputBoardConst.ServerSystemName, inputBoardConst.SetInputTextEvent, self, self.OnSetInputTextEvent)

	def Destroy(self):
		self.UnListenForEvent(clientApi.GetEngineNamespace(), clientApi.GetEngineSystemName(), inputBoardConst.UiInitFinishedEvent, self, self.OnUiInitFinished)
		if self.mUIMgr:
			self.mUIMgr.Destroy()
	
	# UI加载完成
	def OnUiInitFinished(self, args):
		self.mUIMgr.Init(self)
		self.mUIMgr.GetUI(UIDef.InputBoardScreen).SetButtonCallback(self.ButtonCallback)

	# 打开输入界面
	def OnOpenInputBoard(self, args):
		logger.info("-------------- OnOpenInputBoard --------------")
		self.mUIMgr.GetUI(UIDef.InputBoardScreen).Open(args)
		
	# 关闭输入界面
	def OnCloseInputBoard(self, args):
		logger.info("-------------- OnCloseInputBoard -------------- %s", args)
		self.mUIMgr.GetUI(UIDef.InputBoardScreen).Close(args.get('board_id'))

	def OnSetInputTextEvent(self, args):
		logger.info("-------------- OnSetInputTextEvent -------------- %s", args)
		self.mUIMgr.GetUI(UIDef.InputBoardScreen).SetInputText(args.get('board_id'), args.get('text'))

	# 按钮回调
	def ButtonCallback(self, board_id, button_id, args):
		logger.info('Button callback board_id:%s button_id:%s', board_id, button_id)
		self.NotifyToServer(inputBoardConst.ButtonCallbackEvent, {'playerId': self.mPlayerId, 'board_id': board_id, 'button_id': button_id, 'callback_args': args})

