# -*- coding: utf-8 -*-
import client.extraClientApi as extraClientApi
ClientSystem = extraClientApi.GetClientSystemCls()

class AuthClientSystem(ClientSystem):
	"""
	该mod的客户端
	仅通知一下该mod的服务端玩家已进入游戏
	"""
	def __init__(self, namespace, systemName):
		ClientSystem.__init__(self, namespace, systemName)
		self.ListenForEvent(extraClientApi.GetEngineNamespace(), extraClientApi.GetEngineSystemName(),
							'OnLocalPlayerStopLoading', self, self.OnLocalPlayerStopLoading)  # 监听引擎提供的"OnLocalPlayerStopLoading"事件，表示客户端初始基本完毕，客户端玩家已进入游戏
		
	def OnLocalPlayerStopLoading(self, args):
		self.NotifyToServer("playerLoginEvent", args)  # 向该Mod的服务端发送一条消息，表示客户端玩家已经初始化完毕，服务端有什么要在玩家进入后做的逻辑可以开始进行了