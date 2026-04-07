# -*- coding: utf-8 -*-
#

import mod.client.extraClientApi as clientApi 


class CustomBlocksClient(clientApi.GetClientSystemCls()):
	def __init__(self, namespace, name):
		super(CustomBlocksClient, self).__init__(namespace, name)

