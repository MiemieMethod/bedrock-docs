# -*- coding: utf-8 -*-
#

import mod.client.extraClientApi as clientApi 


class MicroBlocksClient(clientApi.GetClientSystemCls()):
	def __init__(self, namespace, name):
		super(MicroBlocksClient, self).__init__(namespace, name)

