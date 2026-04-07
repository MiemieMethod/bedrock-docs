from common.mod import Mod
import client.extraClientApi as clientApi
import chestConsts as chestConsts

@Mod.Binding(name = chestConsts.ModNameSpace, version = chestConsts.ModVersion)
class ChestClientMod(object):
	def __init__(self):
		pass

	@Mod.InitClient()
	def InitClient(self):
		print '===========================init_ChestClientMod!==============================='
		self.mClient = clientApi.RegisterSystem(chestConsts.ModNameSpace, chestConsts.ClientSystemName, chestConsts.ClientSystemClsPath)
		
	@Mod.DestroyClient()
	def DestroyClient(self):
		pass
