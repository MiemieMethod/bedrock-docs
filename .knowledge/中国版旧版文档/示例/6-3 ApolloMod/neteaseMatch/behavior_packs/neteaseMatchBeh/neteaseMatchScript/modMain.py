# -*- coding: utf-8 -*-

from common.mod import Mod
import client.extraClientApi as clientApi
import neteaseMatchScript.clientConsts as clientConsts

@Mod.Binding(name = clientConsts.ModName, version = clientConsts.ModVersion)
class MatchClientMod(object):
	@Mod.InitClient()
	def NeteaseMatchModClientInit(self):
		print '===========================NeteaseMatchMod initClient==============================='
		clientApi.RegisterSystem(clientConsts.ModName, clientConsts.ClientSystemName, clientConsts.ClientSystemClsPath)
		#测试示例，测试时取消屏蔽下面语句
		# clientApi.RegisterSystem(clientConsts.ModName, 'neteaseMatchTestClient', 'neteaseMatchScript.matchTestSystem.NeteaseMatchTest')

	@Mod.DestroyClient()
	def NeteaseMatchModClientDestroy(self):
		print '===========================NeteaseMatchMod destroyClient==============================='

