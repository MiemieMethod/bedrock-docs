# -*- coding: utf-8 -*-
#
import client.extraClientApi as clientApi
ClientSystem = clientApi.GetClientSystemCls()

class NpcClientSystem(ClientSystem):
	def __init__(self,namespace,systemName):
		print 'NpcClient', namespace,systemName
		ClientSystem.__init__(self,namespace,systemName)
		self.ListenForEvent(clientApi.GetEngineNamespace(), clientApi.GetEngineSystemName(), "UiInitFinished",
		                    self, self.InitUi)
		
	def InitUi(self,args):
		#开发者在这里初始化ui，开始客户端操作。
		# 注册UI 详细解释参照:《UI API》
		clientApi.RegisterUI("Minecraft", "npcSure", "neteaseNpcScript.modUI.Sure.SureScreen","npcSure.main")
		# 创建UI 详细解释参照《UI API》
		clientApi.CreateUI("Minecraft", "npcSure", {"isHud": 1})
		self.mSureUINode = clientApi.GetUI("Minecraft", "npcSure")
		if self.mSureUINode:
			self.mSureUINode.Init()
			print 'create ui success'
		else:
			print "create ui failed!"
	
	def Destroy(self):
		'''
		卸下 mod时会执行Destroy 函数。用于清理现场。
		'''
		# 注销事件
		self.UnListenForEvent(clientApi.GetEngineNamespace(), clientApi.GetEngineSystemName(), "UiInitFinished",
		                    self, self.InitUi)