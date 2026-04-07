# -*- coding: utf-8 -*-

from common.mod import Mod
import feedbackConsts as feedbackConsts


@Mod.Binding(name=feedbackConsts.ModNameSpace, version=feedbackConsts.ModVersion)
class neteaseFeedbackClient(object):
	def __init__(self):
		pass
	
	@Mod.InitClient()
	def initClient(self):
		print '===========================neteaseFeedback initClient==============================='
		import client.extraClientApi as clientApi
		self.mClentSystem = clientApi.RegisterSystem(feedbackConsts.ModNameSpace, feedbackConsts.ClientSystemName, feedbackConsts.ClientSystemClsPath)
	
	@Mod.DestroyClient()
	def destroyClient(self):
		print '===========================neteaseFeedback destroyClient==============================='