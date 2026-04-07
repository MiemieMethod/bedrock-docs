# -*- coding: utf-8 -*-
import client.extraClientApi as clientApi
ViewBinder = clientApi.GetViewBinderCls()
ViewRequest = clientApi.GetViewViewRequestCls()
ScreenNode = clientApi.GetScreenNodeCls()
import guildConsts as guildConsts

class CreateGuildScreen(ScreenNode):
	"""
	创建公会界面
	"""
	def __init__(self, namespace, name, param):
		ScreenNode.__init__(self, namespace, name, param)
		print "===%s===" % "init CreateGuildScreen"
		
		self.mCreateGuildPanel = "/CreateGuildPanel"
		self.mCreatePartyImg = self.mCreateGuildPanel + "/createparty_img"
		#关闭按钮
		self.mCloseBtn = self.mCreatePartyImg + "/close_btn"
		self.mCoinImg = self.mCreatePartyImg + "/coin_img"
		#砖石数量
		self.mCoinLabel = self.mCoinImg + "/coin_lbl"
		#创建按钮
		self.mCreateBtn = self.mCreatePartyImg + "/create_btn"
		self.mGuildNameTitleLabel = self.mCreatePartyImg + "/partyname_title_lbl"
		self.mGuildNameBtn = self.mGuildNameTitleLabel + "/partyname_import"
		#公会名字
		self.mGuildNameText = self.mGuildNameBtn + "/partyname_lbl"
		
		self.mGuildName = ""
		self.holder = str("请输入公会名字")
		
		
	# def OnShowUI(self, args):
	# 	if args["UIDef"] == guildConsts.UIDef.UI_CREATEGUILD:
	# 		self.ShowPanel(True)
	
	def Create(self):
		#self.ShowPanel(False)
		self.SetVisible(self.mCreateGuildPanel, False)
		self.AddTouchEventHandler(self.mCreateBtn, self.CreateGuild)
		self.AddTouchEventHandler(self.mCloseBtn, self.ClosePanel)
		
	def ClosePanel(self, args):
		touchEvent = args["TouchEvent"]
		touch_event_enum = clientApi.GetMinecraftEnum().TouchEvent
		if touchEvent == touch_event_enum.TouchUp:
			self.ShowPanel(False)
	
	def SetCoinLabel(self, coinNum):
		self.SetText(self.mCoinLabel, str(coinNum))
	
	def SetCoinColor(self ,enoughDia):
		greenColor = (0, 1, 0, 0.8)
		redColor = (1, 0, 0, 0.8)
		self.SetTextColor(self.mCoinLabel, greenColor if enoughDia == True else redColor)
	
	@ViewBinder.binding(ViewBinder.BF_EditChanged | ViewBinder.BF_EditFinished)
	def TextBox(self, args):
		#print "TextBox", args['Text']
		self.mGuildName = args['Text']
		self.SetInputEnable(True)
		if args['Finish'] and args['Mode'] == 'Finished':
			self.SetInputEnable(False)
		return ViewRequest.Refresh
	
	@ViewBinder.binding(ViewBinder.BF_InteractButtonClick)
	def ClearButtonClick(self, args):
		self.mGuildName = ""
		return ViewRequest.Refresh

	@ViewBinder.binding(ViewBinder.BF_BindString)
	def ReturnTextString(self):
		return self.mGuildName

	@ViewBinder.binding(ViewBinder.BF_BindString)
	def ReturnHolderContent(self):
		return self.holder
		
	def CreateGuild(self, args):
		print "CreateGuild", args
		touchEvent = args["TouchEvent"]
		touch_event_enum = clientApi.GetMinecraftEnum().TouchEvent
		if touchEvent == touch_event_enum.TouchUp:
			data = {'playerId': clientApi.GetLocalPlayerId(), "guildName": self.mGuildName}
			guildConsts.GetClientModSystem().NotifyToServer(guildConsts.CreateGuildFromClientEvent, data)
			self.ShowPanel(False)
		
	
	def InitScreen(self):
		# guildConsts.GetClientModSystem().ListenForEvent(guildConsts.ModNameSpace, guildConsts.ClientSystemName,
		#                                                 guildConsts.ShowUIFromClientEvent, self, self.OnShowUI)
		#clientApi.SetInputMode(0)
		self.SetInputEnable(False)
	
	def ShowPanel(self, isShow):
		# if isShow:
		# 	clientApi.SetInputMode(1)
		# else:
		# 	clientApi.SetInputMode(0)
		self.SetVisible(self.mCreateGuildPanel, isShow)
		if isShow:
			data = {'playerId': clientApi.GetLocalPlayerId()}
			guildConsts.GetClientModSystem().NotifyToServer(guildConsts.ShowCreateGuildUIFromClientEvent, data)