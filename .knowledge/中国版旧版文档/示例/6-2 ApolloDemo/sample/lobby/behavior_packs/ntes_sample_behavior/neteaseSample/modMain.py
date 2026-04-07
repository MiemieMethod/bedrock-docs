from common.mod import Mod
import server.extraServerApi as serverApi
import client.extraClientApi as clientApi

@Mod.Binding(name = "neteaseSample", version = "0.5")
class LobbyMod(object):
	def __init__(self):
		pass
		
	@Mod.InitServer()
	def initServer(self):
		print '===========================init_sample_mod!==============================='
		
	@Mod.DestroyServer()
	def destroyServer(self):
		print 'destroy_server==============='
		
	@Mod.InitClient()
	def initClient(self):
		print '===========================init_sample_mod!==============================='
		self.client = clientApi.RegisterSystem("Minecraft","SampleClient","neteaseSample.modSystem.sampleClient.SampleClient")
		
	@Mod.DestroyClient()
	def destroyClient(self):
		pass
