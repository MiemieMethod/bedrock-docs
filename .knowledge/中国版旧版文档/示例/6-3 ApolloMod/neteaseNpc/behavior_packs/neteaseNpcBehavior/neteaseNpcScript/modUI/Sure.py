# -*- coding: utf-8 -*-

# 从客户端API中拿到我们需要的ViewBinder / ViewRequest / ScreenNode
import client.extraClientApi as clientApi
ViewBinder = clientApi.GetViewBinderCls()
ViewRequest = clientApi.GetViewViewRequestCls()
ScreenNode = clientApi.GetScreenNodeCls()
import neteaseNpcScript.clientUtils.apiUtil as apiUtil

def strCamp(str, maxLength):
   if len(str) <= maxLength:
        return str
   else:
        return str[0:maxLength]

# 所有的UI类需要继承自引擎的ScreenNode类
class SureScreen(ScreenNode):
    def __init__(self, namespace, name, param):
        ScreenNode.__init__(self, namespace, name, param)
        # 当前客户端的玩家Id
        #self.mPlayerId = clientApi.GetLocalPlayerId()
        self.mSurePanel = "/Sure"
        self.mSureButton = self.mSurePanel + "/mask_bg/npc_keepon_btn"
        self.mCanelButton = self.mSurePanel + "/mask_bg/npc_canel_btn"
        self.mTipText = self.mSurePanel + "/mask_bg/npc_main"
        self.mNpcName = self.mSurePanel + "/mask_bg/npc_name"
        self.mAimServer = ""

    # Create函数是继承自ScreenNode，会在UI创建完成后被调用
    def Create(self):
        print "===== SureScreen Create ====="
        self.SetVisible(self.mSurePanel, False)
        self.AddTouchEventHandler(self.mSureButton, self.OnSureButtonClick)
        self.AddTouchEventHandler(self.mCanelButton, self.OnCanelButtonClick)

        # 界面的一些初始化操作
    def Init(self):
        apiUtil.GetClientModSystem().ListenForEvent("neteaseNpc", "npcServer", "CheckSureFromServerEvent", self, self.SureEnterGame)
        apiUtil.GetClientModSystem().ListenForEvent("neteaseNpc", "npcServer", "PlayerDieFromServerEvent", self, self.TurnOff)

    def Destory(self):
        apiUtil.GetClientModSystem().UnListenForEvent("neteaseNpc", "npcServer", "CheckSureFromServerEvent", self, self.SureEnterGame)
        apiUtil.GetClientModSystem().UnListenForEvent("neteaseNpc", "npcServer", "PlayerDieFromServerEvent", self, self.TurnOff)

    def SureEnterGame(self, args):
        '''
        显示对话框
        '''
        playerId = clientApi.GetLocalPlayerId()
        if not playerId or playerId != args.get('playerId'):
           return
        clientApi.SetInputMode(1)
        clientApi.HideSlotBarGui(True)
        self.SetVisible(self.mSurePanel, True)
        self.mAimServer = args.get("aimServer", "")
        self.SetText(self.mTipText, args["talkContent"])
        self.SetText(self.mNpcName, args["npcName"])
        
    def TurnOff(self,args):
        '''
        关闭对话框
        '''
        playerId = clientApi.GetLocalPlayerId()
        if not playerId or playerId != args.get('playerId'):
            return
        self.mAimServer = ""
        clientApi.SetInputMode(0)
        clientApi.HideSlotBarGui(False)
        self.SetVisible(self.mSurePanel, False)

    def OnSureButtonClick(self, args):
        '''
        确定按钮
        '''
        touchEvent = args["TouchEvent"]
        touch_event_enum = clientApi.GetMinecraftEnum().TouchEvent
        if touchEvent == touch_event_enum.TouchUp:
            args["playerId"] = clientApi.GetLocalPlayerId()
            args['aimServer'] = self.mAimServer
            apiUtil.GetClientModSystem().NotifyToServer("ClickSureFromClientEvent", args)
            clientApi.SetInputMode(0)
            clientApi.HideSlotBarGui(False)
            self.SetVisible(self.mSurePanel, False)

    def OnCanelButtonClick(self, args):
        '''
        取消按钮
        '''
        touchEvent = args["TouchEvent"]
        touch_event_enum = clientApi.GetMinecraftEnum().TouchEvent
        if touchEvent == touch_event_enum.TouchUp:
            clientApi.SetInputMode(0)
            clientApi.HideSlotBarGui(False)
            self.SetVisible(self.mSurePanel, False)
	
    # 继承自ScreenNode的方法，会被引擎自动调用，1秒钟30帧
    def Update(self):
        """
        node tick function
        """
        pass
    


