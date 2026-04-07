# -*- coding: utf-8 -*-

from common.mod import Mod
import feedbackConsts as feedbackConsts


@Mod.Binding(name=feedbackConsts.ModNameSpace, version=feedbackConsts.ModVersion)
class neteaseFeedbackServer(object):
	def __init__(self):
		pass
	
	@Mod.InitServer()
	def initServer(self):
		print '===========================neteaseFeedback initServer==============================='
		import server.extraServerApi as serverApi
		self.mServerSystem = serverApi.RegisterSystem(feedbackConsts.ModNameSpace, feedbackConsts.ServerSystemName, feedbackConsts.ServerSystemClsPath)
	
	@Mod.DestroyServer()
	def destroyServer(self):
		print '===========================neteaseFeedback destroyServer==============================='