from common.mod import Mod
import client.extraClientApi as clientApi

import guildConsts as guildConsts

@Mod.Binding(name=guildConsts.ModNameSpace, version=guildConsts.ModVersion)
class GuildGameClientMod(object):
	def __init__(self):
		pass
	
	@Mod.InitClient()
	def InitClient(self):
		print '===========================init_GuildGameClientMod!==============================='
		self.mClient = clientApi.RegisterSystem(guildConsts.ModNameSpace, guildConsts.GameClientSystemName, guildConsts.GameClientSystemClsPath)
	
	@Mod.DestroyClient()
	def DestroyClient(self):
		pass