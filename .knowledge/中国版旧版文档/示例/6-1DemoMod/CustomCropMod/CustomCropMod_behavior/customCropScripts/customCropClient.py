# -*- coding: utf-8 -*-
#

import mod.client.extraClientApi as clientApi 


class CustomCropClient(clientApi.GetClientSystemCls()):
	def __init__(self, namespace, name):
		super(CustomCropClient, self).__init__(namespace, name)

