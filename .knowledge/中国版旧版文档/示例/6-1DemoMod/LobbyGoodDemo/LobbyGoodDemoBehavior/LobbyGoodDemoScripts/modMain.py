from mod.common.mod import Mod
import mod.client.extraClientApi as clientApi
import mod.server.extraServerApi as serverApi

@Mod.Binding(name = "LobbyGoodDemo", version = "0.1")
class LobbyGoodDemoMain(object):
	def __init__(self):
		pass

	@Mod.InitServer()
	def init_server(self):
		serverApi.RegisterSystem("LobbyGoodDemo", "LobbyGoodDemoServer", "LobbyGoodDemoScripts.modSystem.LobbyGoodDemoSysServer.LobbyGoodDemoServer")

	@Mod.DestroyServer()
	def destroy_server(self):
		pass


	@Mod.InitClient()
	def init_client(self):
		clientApi.RegisterSystem("LobbyGoodDemo", "LobbyGoodDemoClient", "LobbyGoodDemoScripts.modSystem.LobbyGoodDemoSysClient.LobbyGoodDemoClient")

	@Mod.DestroyClient()
	def destroy_client(self):
		pass
