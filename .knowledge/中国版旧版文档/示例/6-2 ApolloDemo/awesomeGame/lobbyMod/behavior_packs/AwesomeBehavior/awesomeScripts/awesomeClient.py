# -*- coding: utf-8 -*-
#
import mod.client.extraClientApi as clientApi
ClientSystem = clientApi.GetClientSystemCls()
import modCommon.playerData as playerData
from mod_log import logger
from awesomeScripts.modCommon import modConfig

class AwesomeClient(ClientSystem):
	def __init__(self,namespace,systemName):
		logger.info('AwesomeClient %s, %s' % (namespace,systemName))
		ClientSystem.__init__(self,namespace,systemName)
		self.mSureUINode = None
		# 注册事件
		# 监听服务端自定义事件，用于初始化玩家数据
		self.ListenForEvent(modConfig.Minecraft, modConfig.LobbyServerSystemName, modConfig.LoginResponseEvent, self, self.OnLoginResponse)
		#监听引擎事件，UI初始化框架完成,此时可以创建UI
		self.ListenForEvent(clientApi.GetEngineNamespace(), clientApi.GetEngineSystemName(),modConfig.UiInitFinished, self, self.OnUIInitFinished)
		#玩家自身的信息
		self.mMyPlayerData = None
	
	def OnUIInitFinished(self, args):
		'''
		请求登录到服务端，获取玩家数据
		'''
		logger.info("OnUIInitFinished : %s", args)
		playerId = clientApi.GetLocalPlayerId()
		loginData = {}
		loginData['id'] = playerId
		self.NotifyToServer(modConfig.LoginRequestEvent, loginData)

	def OnLoginResponse(self, args):
		'''
		初始化玩家数据，然后开始客户端逻辑
		'''
		logger.info("OnLoginResponse : %s", args)
		playerInfo = args
		self.mMyPlayerData = playerData.PlayerData()
		self.mMyPlayerData.initPlayer(playerInfo['player_id'], playerInfo)
		self.InitUi()

	def InitUi(self):
		#开发者在这里初始化ui，开始客户端操作。
		# 注册UI 详细解释参照:《UI API》
		clientApi.RegisterUI(modConfig.Minecraft, modConfig.SureUIName, modConfig.SureUIPyClsPath,
		                     modConfig.SureUIScreenDef)
		# 创建UI 详细解释参照《UI API》
		clientApi.CreateUI(modConfig.Minecraft, modConfig.SureUIName, {"isHud": 1})
		self.mSureUINode = clientApi.GetUI(modConfig.Minecraft, modConfig.SureUIName)
		if self.mSureUINode:
			self.mSureUINode.Init()
			print 'create ui success'
		else:
			logger.error("create ui %s failed!")
	
	def Destroy(self):
		'''
		卸下 mod时会执行Destroy 函数。用于清理现场。
		'''
		# 注销事件
		self.UnListenForEvent(modConfig.Minecraft, modConfig.LobbyServerSystemName, modConfig.SyncUserDataEvent, self, self.OnLoginResponse)
		self.UnListenForEvent(clientApi.GetEngineNamespace(), clientApi.GetEngineSystemName(), modConfig.UiInitFinished,self, self.OnUIInitFinished)
		self.mMyPlayerData = None