from common.mod import Mod
import mod.client.extraClientApi as clientApi
from awesomeScripts.modCommon import modConfig

@Mod.Binding(name = modConfig.LobbyClientModName, version = "0.1")
class LobbyMod(object):
	def __init__(self):
		pass

	@Mod.InitClient()
	def initClient(self):
		#加载mod入口
		print '===========================init_LobbyMod!==============================='
		self.client = clientApi.RegisterSystem(modConfig.Minecraft,modConfig.LobbyClientSystemName,modConfig.LobbyClientSystemClsPath)
		
	@Mod.DestroyClient()
	def destroyClient(self):
		#退出游戏时注销mod
		pass
