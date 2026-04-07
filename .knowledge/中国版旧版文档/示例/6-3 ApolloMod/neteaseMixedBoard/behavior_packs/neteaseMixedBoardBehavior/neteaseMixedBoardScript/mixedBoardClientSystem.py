# -*- coding: utf-8 -*-

import client.extraClientApi as clientApi
import neteaseMixedBoardScript.mixedBoardConst as mixedBoardConst
import neteaseMixedBoardScript.ui.uiMgr as uiMgr
from neteaseMixedBoardScript.ui.uiDef import UIDef
from mod_log import logger

ClientSystem = clientApi.GetClientSystemCls()


class MixedBoardClientSystem(ClientSystem):
	"""
	该mod的客户端类
	根据服务端推送下来的数据显示综合界面
	"""

	def __init__(self, namespace, systemName):
		ClientSystem.__init__(self, namespace, systemName)
		self.mPlayerId = clientApi.GetLocalPlayerId()
		self.mUIMgr = uiMgr.UIMgr()
		
		self.ListenForEvent(clientApi.GetEngineNamespace(), clientApi.GetEngineSystemName(), mixedBoardConst.UiInitFinishedEvent, self, self.OnUiInitFinished)
		self.ListenForEvent(mixedBoardConst.ModName, mixedBoardConst.ServerSystemName, mixedBoardConst.OpenMixedBoardEvent, self, self.OnOpenMixedBoard)
		self.ListenForEvent(mixedBoardConst.ModName, mixedBoardConst.ServerSystemName, mixedBoardConst.CloseMixedBoardEvent, self, self.OnCloseMixedBoard)

	def Destroy(self):
		self.UnListenForEvent(clientApi.GetEngineNamespace(), clientApi.GetEngineSystemName(), mixedBoardConst.UiInitFinishedEvent, self, self.OnUiInitFinished)
		if self.mUIMgr:
			self.mUIMgr.Destroy()
	
	# UI加载完成
	def OnUiInitFinished(self, args):
		self.mUIMgr.Init(self)
		self.mUIMgr.GetUI(UIDef.MixedBoardScreen).SetButtonCallback(self.ButtonCallback)

	# 打开综合界面
	def OnOpenMixedBoard(self, args):
		logger.info("-------------- OnOpenMixedBoard --------------")
		self.mUIMgr.GetUI(UIDef.MixedBoardScreen).Open(args)
		
	# 关闭综合界面
	def OnCloseMixedBoard(self, args):
		logger.info("-------------- OnCloseMixedBoard -------------- %s", args)
		self.mUIMgr.GetUI(UIDef.MixedBoardScreen).Close(args.get('board_id'))

	# 按钮回调
	def ButtonCallback(self, board_id, button_id):
		logger.info('Button callback board_id:%s button_id:%s', board_id, button_id)
		self.NotifyToServer(mixedBoardConst.ButtonCallbackEvent, {'playerId': self.mPlayerId, 'board_id': board_id, 'button_id': button_id, 'callback_args': {}})

