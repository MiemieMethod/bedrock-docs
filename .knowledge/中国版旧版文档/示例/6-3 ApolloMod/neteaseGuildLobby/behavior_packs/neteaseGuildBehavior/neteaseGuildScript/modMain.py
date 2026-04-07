from common.mod import Mod
import client.extraClientApi as clientApi

import guildConsts as guildConsts

@Mod.Binding(name=guildConsts.ModNameSpace, version=guildConsts.ModVersion)
class GuildClientMod(object):
	def __init__(self):
		pass
	
	@Mod.InitClient()
	def InitClient(self):
		print '===========================init_GuildClientMod!==============================='
		self.mClient = clientApi.RegisterSystem(guildConsts.ModNameSpace, guildConsts.ClientSystemName, guildConsts.ClientSystemClsPath)
	
	@Mod.DestroyClient()
	def DestroyClient(self):
		pass