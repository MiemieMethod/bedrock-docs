# -*- coding: utf-8 -*-
#

import mod.client.extraClientApi as clientApi
from customEffectScripts.modCommon import modConfig
from customEffectScripts import logger


class CustomEffectClientSystem(clientApi.GetClientSystemCls()):
    def __init__(self, namespace, name):
        super(CustomEffectClientSystem, self).__init__(namespace, name)
