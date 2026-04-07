# -*- coding: utf-8 -*-

from CustomFurnaceScripts.modCommon import modConfig
from mod_log import logger  # 用来打印规范的log
import mod.client.extraClientApi as clientApi


class UIMgr(object):
    def __init__(self):
        super(UIMgr, self).__init__()
        self.mUIDict = {}
        self.mPresentUIDict = {}

    def initAllUI(self, *args, **kwargs):
        self.clear()
        for _, uiData in modConfig.UI_DEFS.items():
            self.initUI(uiData)

    def createUINode(self, uiData):
        uiName = uiData['uiName']
        clientApi.RegisterUI(modConfig.ModName, uiName, uiData["uiClassPath"], uiData["uiScreenDef"])
        uiNode = clientApi.CreateUI(modConfig.ModName, uiName, {"isHud": 1})
        if not uiNode:
            logger.error('==== %s ====' % '"create UI failed": %s' % uiData['uiScreenDef'])
            return
        self.mUIDict[uiName] = uiNode
        return uiNode

    def initUI(self, uiData):
        uiName = uiData['uiName']
        if not self.mPresentUIDict.get(uiName):
            uiNode = self.getUINode(uiData) or self.createUINode(uiData)
            uiNode.InitScreen()
            self.mPresentUIDict[uiName] = True

    def getUINode(self, uiData):
        uiName = uiData['uiName']
        uiNode = self.mUIDict.get(uiName)
        if uiNode:
            return uiNode
        return clientApi.GetUI(modConfig.ModName, uiName)

    def removeUINode(self, uiName):
        uiNode = clientApi.GetUI(modConfig.ModName, uiName)
        if uiNode:
            if uiName in self.mUIDict:
                del self.mUIDict[uiName]
            uiNode.SetRemove()
            return True
        return False

    def clear(self):
        self.mUIDict.clear()
        self.mPresentUIDict.clear()
