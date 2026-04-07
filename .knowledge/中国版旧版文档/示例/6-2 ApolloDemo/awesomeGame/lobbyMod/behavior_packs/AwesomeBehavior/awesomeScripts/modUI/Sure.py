# -*- coding: utf-8 -*-

# 从客户端API中拿到我们需要的ViewBinder / ViewRequest / ScreenNode
import mod.client.extraClientApi as clientApi
ViewBinder = clientApi.GetViewBinderCls()
ViewRequest = clientApi.GetViewViewRequestCls()
ScreenNode = clientApi.GetScreenNodeCls()
from mod_log import logger
from awesomeScripts.modCommon import modConfig
from awesomeScripts.modCommon.modConfig import TipType
import awesomeScripts.clientUtils.apiUtil as apiUtil

# 所有的UI类需要继承自引擎的ScreenNode类
class SureScreen(ScreenNode):
    def __init__(self, namespace, name, param):
        ScreenNode.__init__(self, namespace, name, param)
        # 当前客户端的玩家Id
        #self.mPlayerId = clientApi.GetLocalPlayerId()
        self.mSurePanel = "/SurePanel"
        self.mSureButton = self.mSurePanel + "/content_panel/confirm_button"
        self.mCanelButton = self.mSurePanel + "/content_panel/cancel_button"
        self.mTipText = self.mSurePanel + "/content_panel/message_label"
        self.aimGame = ""

    # Create函数是继承自ScreenNode，会在UI创建完成后被调用
    def Create(self):
        logger.info("===== SureScreen Create =====")
        # 隐藏
        self.SetVisible(self.mSurePanel, False)
        self.AddTouchEventHandler(self.mSureButton, self.OnSureButtonClick)
        self.AddTouchEventHandler(self.mCanelButton, self.OnCanelButtonClick)

    # 界面的一些初始化操作
    def Init(self):
        apiUtil.GetClientModSystem().ListenForEvent(modConfig.Minecraft, modConfig.LobbyServerSystemName, modConfig.SureEnterGameEvent, self, self.SureEnterGame)
        apiUtil.GetClientModSystem().ListenForEvent(modConfig.Minecraft, modConfig.LobbyServerSystemName, modConfig.SureMatchGameEvent, self, self.SureMatchGame)
	    
    def Destory(self):
        apiUtil.GetClientModSystem().UnListenForEvent(modConfig.Minecraft, modConfig.LobbyServerSystemName,modConfig.SureEnterGameEvent, self, self.SureEnterGame)
        apiUtil.GetClientModSystem().UnListenForEvent(modConfig.Minecraft, modConfig.LobbyServerSystemName,modConfig.SureMatchGameEvent, self, self.SureMatchGame)
	    
	    
    def SureEnterGame(self,args):
        player_id = clientApi.GetLocalPlayerId()
        if not player_id or player_id != args.get('player_id'):
           return
        apiUtil.GetClientModSystem().ListenForEvent(modConfig.Minecraft, modConfig.LobbyServerSystemName,modConfig.MatchResultTip, self, self.showResult)
        clientApi.SetInputMode(1)
        self.SetVisible(self.mSurePanel, True)
        self.SetTouchEnable(self.mSureButton, True)
        if args['game'] == 'gameA':
            self.aimGame = args["game"]
            self.SetText(self.mTipText,"确定前往玩法A吗？（当前玩法在线人数"+str(args["playernum"])+"人）\n"
             "玩法A介绍：\n"
             "玩法A中装载了官方示例awesomeMod：玩家模型替换为骨骼模型，主界面添加了射击等操作按钮，模拟了简单的射击体验。")
        elif args['game'] == 'gameB':
            self.aimGame = args["game"]
            self.SetText(self.mTipText, "确定前往玩法B吗？（当前玩法在线人数" + str(args["playernum"]) + "人）\n"
            "玩法B介绍：\n"
            "玩法B中，当在聊天栏中发送消息“钻石剑”后，会向背包添加1把钻石剑。添加钻石剑的次数会记录在数据库中。")
            
    def SureMatchGame(self,args):
        player_id = clientApi.GetLocalPlayerId()
        if not player_id or player_id != args.get('player_id'):
            return
        apiUtil.GetClientModSystem().ListenForEvent(modConfig.Minecraft, modConfig.LobbyServerSystemName,
	                                                modConfig.MatchResultTip, self, self.showResult)
        clientApi.SetInputMode(1)
        self.SetVisible(self.mSurePanel, True)
        self.SetTouchEnable(self.mSureButton, True)
        if args['game'] == 'gameC':
            self.aimGame = args["game"]
            self.SetText(self.mTipText, "确定匹配玩法C吗？（当前匹配人数" + str(args["playernum"]) + "人）当等级>=1级的玩家人数达到2人以上时，一起传至C"
             "（匹配的玩家中，等级1级或以上的玩家人数达到2人或以上时，会一起传往玩法C中）")

    # 继承自ScreenNode的方法，会被引擎自动调用，1秒钟30帧
    def Update(self):
        """
        node tick function
        """
        pass
    
    def showResult(self,args):
       if args["tipType"] == TipType.levelNotEnough:
           self.SetText(self.mTipText, "你的等级不够.......")
           self.SetTouchEnable(self.mSureButton, False)
       elif args["tipType"] == TipType.matching:
           self.SetText(self.mTipText,"匹配中.......")
           self.SetTouchEnable(self.mSureButton,False)
       elif args["tipType"] == TipType.toTransfer:
           self.SetText(self.mTipText, "匹配成功，即将传至C")
           self.SetTouchEnable(self.mSureButton, False)


    def OnSureButtonClick(self, args):
        touchEvent = args["TouchEvent"]
        touch_event_enum = clientApi.GetMinecraftEnum().TouchEvent
        if touchEvent == touch_event_enum.TouchUp:
            args["playerId"] = clientApi.GetLocalPlayerId()
            args['game'] = self.aimGame
            apiUtil.GetClientModSystem().NotifyToServer(modConfig.OnSureGameEvent, args)
            if self.aimGame != 'gameC':
                clientApi.SetInputMode(0)
                self.SetVisible(self.mSurePanel, False)
            #self.SetVisible(self.mFpsSurePanel, False)


    def OnCanelButtonClick(self, args):
        touchEvent = args["TouchEvent"]
        touch_event_enum = clientApi.GetMinecraftEnum().TouchEvent
        if touchEvent == touch_event_enum.TouchUp:
           clientApi.SetInputMode(0)
           self.SetVisible(self.mSurePanel, False)
           apiUtil.GetClientModSystem().UnListenForEvent(modConfig.Minecraft, modConfig.LobbyServerSystemName,
                                                       modConfig.MatchResultTip, self, self.showResult)
           if self.aimGame == 'gameC':
               args["playerId"] = clientApi.GetLocalPlayerId()
               args['game'] = self.aimGame
               apiUtil.GetClientModSystem().NotifyToServer(modConfig.OnCancelGameEvent, args)

