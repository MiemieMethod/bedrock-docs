# -*- coding: utf-8 -*-

import server.extraServerApi as serverApi
import apolloCommon.commonNetgameApi as commonNetgameApi
import neteaseMixedBoardScript.mixedBoardConst as mixedBoardConst
import time
from mod_log import logger

ServerSystem = serverApi.GetServerSystemCls()



class MixedBoardServerSystem(ServerSystem):
	"""
	该mod的服务端类
	设置客户端综合界面
	"""

	def __init__(self, namespace, systemName):
		ServerSystem.__init__(self, namespace, systemName)

		if not self.InitMixedBoardCfg():
			return

		# 保存按钮回调
		self.m_button_callback = {}

		# uuid 相关
		self.m_uuid_timestamp = 0
		self.m_uuid_num = 0

		self.ListenForEvent(serverApi.GetEngineNamespace(), serverApi.GetEngineSystemName(), mixedBoardConst.DelServerPlayerEvent, self, self.OnDelServerPlayerEvent)
		self.ListenForEvent(mixedBoardConst.ModName, mixedBoardConst.ClientSystemName, mixedBoardConst.ButtonCallbackEvent, self, self.OnButtonCallbackEvent)


	def Destroy(self):
		self.UnListenForEvent(serverApi.GetEngineNamespace(), serverApi.GetEngineSystemName(), mixedBoardConst.DelServerPlayerEvent, self, self.OnDelServerPlayerEvent)

	def InitMixedBoardCfg(self):
		cfg = commonNetgameApi.GetModJsonConfig("neteaseMixedBoardScript")
		if not cfg:
			logger.error("nothing in InitMixedBoardCfg")
			return False
		
		self.m_content_example = cfg['content_example']
		return True

	def OnDelServerPlayerEvent(self, args):
		logger.info("OnDelServerPlayerEvent args: %s", args)
		playerId = args['id']
		if playerId in self.m_button_callback:
			del self.m_button_callback[playerId]
			logger.info("OnDelServerPlayerEvent delete player button callback playerId:%s", playerId)

	def OnButtonCallbackEvent(self, args):
		logger.info("OnButtonCallbackEvent args: %s", args)
		playerId = args.get("playerId")
		board_id = args.get("board_id")
		button_id = args.get("button_id")
		callback_args = args.get("callback_args")

		callback_cache = self.m_button_callback.get(playerId, [])
		for cache in callback_cache:
			if board_id != cache['board_id'] or button_id > len(cache['callback_list']) or cache['callback_list'] == None:
				break
			
			callback = cache['callback_list'][button_id]
			callback(playerId, callback_args)

	# 打开综合界面
	def OpenMixedBoard(self, playerId, args):
		board_id = self.GetUUID()
		args['board_id'] = board_id
		button_list = args.get("button_list", [])
		callback_list = []
		for i, button_args in enumerate(button_list):
			if 'callback' in button_args:
				callback_list.append(button_args['callback'])
				del button_args['callback']
		if callback_list:
			# 每个玩家缓存两个面板的 回调列表
			callback_cache = self.m_button_callback.get(playerId, [])
			self.m_button_callback[playerId] = [{'board_id': board_id, 'callback_list': callback_list}]
			if callback_cache:
				self.m_button_callback[playerId].append(callback_cache[0])
		
		self.NotifyToClient(playerId, mixedBoardConst.OpenMixedBoardEvent, args)
		return board_id
	
	# 关闭综合界面
	def CloseMixedBoard(self, playerId, board_id=None):
		self.NotifyToClient(playerId, mixedBoardConst.CloseMixedBoardEvent, {'board_id': board_id})

	def ButtonCallbackExample(self, playerId, args):
		logger.info("ButtonCallbackExample playerId:%s args: %s", playerId, args)

	def ButtonCallbackClose(self, playerId, args):
		self.CloseMixedBoard(playerId)

	def GetUUID(self):
		now = int(time.time())
		if now != self.m_uuid_timestamp:
			self.m_uuid_timestamp = now
			self.m_uuid_num = 0
		else:
			self.m_uuid_num += 1
		return '{}-{}'.format(self.m_uuid_timestamp, self.m_uuid_num)