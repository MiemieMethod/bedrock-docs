# -*- coding: utf-8 -*-
import client.extraClientApi as extraClientApi
ClientSystem = extraClientApi.GetClientSystemCls()
import neteaseResidenceScript.residenceGacMgr as residenceGacMgr
import neteaseResidenceScript.residenceConsts as residenceConsts
import neteaseResidenceScript.playerGac as playerGac
import neteaseResidenceScript.util as util
import neteaseResidenceScript.effect.effectFunc as effectFunc
import neteaseResidenceScript.ui.uiMgr as uiMgr
import neteaseResidenceScript.ui.uiDef as uiDef

class ResidenceClientSys(ClientSystem):
	"""
	该mod的客户端类
	"""
	def __init__(self, namespace, systemName):
		ClientSystem.__init__(self, namespace, systemName)
		self.DefineEvent(residenceConsts.LoginRequestEvent)
		util.SetResidenceSystem(self)  # 添加该类的引用
		self.ListenForEvent(extraClientApi.GetEngineNamespace(), extraClientApi.GetEngineSystemName(),
							'UiInitFinished', self, self.OnUiInitFinished)
		self.ListenForEvent(residenceConsts.ModNameSpace, residenceConsts.ServerSystemName,
							residenceConsts.LoginResponseEvent, self, self.OnLoginResponse)
		self.ListenForEvent(residenceConsts.ModNameSpace, residenceConsts.ServerSystemName,
		                    "ShowUIFromClient", self, self.OnShowUIFromClient)
		self.mResidenceMgr = residenceGacMgr.ResidenceGacMgr(self)
		playerId = extraClientApi.GetLocalPlayerId()
		self.mPlayerGac = playerGac.PlayerGac(playerId)  # 玩家实体封装类
		self.mUIMgr = uiMgr.UIMgr()  # UI封装类
		
	def SetShowResPreEffect(self, args):
		'''
		设置是否显示领地的预览光圈
		'''
		showResPreEffect = args.get("showResPreEffect", True)
		ui = self.mUIMgr.GetUI(uiDef.UIDef.UIResidenceMy)
		ui.SHOW_RES_PRE_EFFECT = showResPreEffect
		
	def SetShowResEffect(self, args):
		'''
		设置是否显示领地的光圈
		'''
		showResEffect = args.get("showResEffect", True)
		self.mResidenceMgr.set_show_res_effect(showResEffect)
		
	def OnShowUIFromClient(self, args):
		"""
		响应服务端的事件，显示指定的UI界面
		"""
		print "OnShowUIFromClient", args
		ui = self.mUIMgr.GetUI(args["UI"])
		if ui:
			ui.Show()
		#self.SetShowResEffect({"showResEffect": args.get("bool", True)})
		
			
	def OpenResidenceUI(self):
		"""
		打开领地界面，默认显示【申请权限】分页
		"""
		ui = self.mUIMgr.GetUI(uiDef.UIDef.UIResidenceApply)
		if ui:
			ui.Show()
	
	def OnApplyBtn(self, args):
		"""
		切换领地界面到【申请权限】分页
		"""
		touchEvent = args["TouchEvent"]
		touch_event_enum = extraClientApi.GetMinecraftEnum().TouchEvent
		if touchEvent == touch_event_enum.TouchUp:
			for keys in uiDef.UIData.keys():
				if keys != uiDef.UIDef.UIResidenceApply:
					ui = self.mUIMgr.GetUI(keys)
					ui.ClosePanel()
			ui = self.mUIMgr.GetUI(uiDef.UIDef.UIResidenceApply)
			if ui:
				ui.Show()
	
	def OnTransferBtn(self, args):
		"""
		切换领地界面到【领地传送】分页
		"""
		touchEvent = args["TouchEvent"]
		touch_event_enum = extraClientApi.GetMinecraftEnum().TouchEvent
		if touchEvent == touch_event_enum.TouchUp:
			for keys in uiDef.UIData.keys():
				if keys != uiDef.UIDef.UIResidenceTransfer:
					ui = self.mUIMgr.GetUI(keys)
					ui.ClosePanel()
			ui = self.mUIMgr.GetUI(uiDef.UIDef.UIResidenceTransfer)
			if ui:
				ui.Show()
	
	def OnGiveBtn(self, args):
		"""
		切换领地界面到【权限赋予】分页
		"""
		touchEvent = args["TouchEvent"]
		touch_event_enum = extraClientApi.GetMinecraftEnum().TouchEvent
		if touchEvent == touch_event_enum.TouchUp:
			for keys in uiDef.UIData.keys():
				if keys != uiDef.UIDef.UIResidenceGive:
					ui = self.mUIMgr.GetUI(keys)
					ui.ClosePanel()
			ui = self.mUIMgr.GetUI(uiDef.UIDef.UIResidenceGive)
			if ui:
				ui.Show()
	
	def OnManageBtn(self, args):
		"""
		切换领地界面到【地皮管理】分页
		"""
		touchEvent = args["TouchEvent"]
		touch_event_enum = extraClientApi.GetMinecraftEnum().TouchEvent
		if touchEvent == touch_event_enum.TouchUp:
			for keys in uiDef.UIData.keys():
				if keys != uiDef.UIDef.UIResidenceManage:
					ui = self.mUIMgr.GetUI(keys)
					ui.ClosePanel()
			ui = self.mUIMgr.GetUI(uiDef.UIDef.UIResidenceManage)
			if ui:
				ui.Show()
	
	def OnMyBtn(self, args):
		"""
		切换领地界面到【我的领地】分页
		"""
		touchEvent = args["TouchEvent"]
		touch_event_enum = extraClientApi.GetMinecraftEnum().TouchEvent
		if touchEvent == touch_event_enum.TouchUp:
			for keys in uiDef.UIData.keys():
				if keys != uiDef.UIDef.UIResidenceMy:
					ui = self.mUIMgr.GetUI(keys)
					ui.ClosePanel()
			ui = self.mUIMgr.GetUI(uiDef.UIDef.UIResidenceMy)
			if ui:
				ui.Show()
		
	
	def GetResidenceMgr(self):
		return self.mResidenceMgr

	def GetPlayerGac(self):
		return self.mPlayerGac

	def OnUiInitFinished(self, data):
		"""
		UI初始化完成，通知服务端
		"""
		print 'OnUiInitFinished', data
		self.mUIMgr.Init(self)  # 创建UI
		requestData = {}
		requestData['playerId'] = extraClientApi.GetLocalPlayerId()
		self.NotifyToServer(residenceConsts.LoginRequestEvent, requestData)  # 登录请求
		#effectFunc.DrawResidenceBox((1395.5, 68, 35.5), (1375.5, 78, 65.5))
		
		

	def OnLoginResponse(self, data):
		"""
		登陆请求返回
		"""
		#print 'OnResponseServerResidence', data
		self.mPlayerGac.SetUid(data['uid'])
		self.mPlayerGac.SetDimensionId(data['dimensionId'])
		util.CacheModConf(data["modConf"])
		
		listenBlocks = util.GetModConfByField('cannot_interact_block_list')
		for block in listenBlocks:
			comp = self.CreateComponent(extraClientApi.GetLevelId(), "Minecraft", "blockUseEventWhiteList")
			comp.AddBlockItemListenForUseEvent(block)

	def Update(self):
		self.mPlayerGac.Update()

	def Destroy(self):
		util.Destroy()
		self.UnListenForEvent(extraClientApi.GetEngineNamespace(), extraClientApi.GetEngineSystemName(),
							'UiInitFinished', self, self.OnUiInitFinished)
		self.UnListenForEvent(residenceConsts.ModNameSpace, residenceConsts.ServerSystemName,
							residenceConsts.LoginResponseEvent, self, self.OnLoginResponse)
