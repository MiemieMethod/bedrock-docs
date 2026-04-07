from common.mod import Mod
import client.extraClientApi as clientApi

@Mod.Binding(name = "neteaseNpcBehavior", version = "1.0.4")
class NpcClientMod(object):
	def __init__(self):
		pass

	@Mod.InitClient()
	def InitClient(self):
		print '===========================init_NpcClientMod!==============================='
		self.mClient = clientApi.RegisterSystem("neteaseNpc", "npcClient", "neteaseNpcScript.neteaseNpcSystem.NpcClientSystem")
		
	@Mod.DestroyClient()
	def DestroyClient(self):
		pass
