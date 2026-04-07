# -*- coding: utf-8 -*-
#
import client.extraClientApi as clientApi
ClientSystem = clientApi.GetClientSystemCls()
import chestConsts
from chestConsts import UIDef, NotifyDef
from UIMgr import UIMgr

class ChestClientSystem(ClientSystem):
	def __init__(self, namespace, systemName):
		ClientSystem.__init__(self, namespace, systemName)
		print "ChestClientSystem init =======", namespace, systemName
		self.mPlayerId = clientApi.GetLocalPlayerId()  # 获取客户端本地玩家的playerId
		self.mUIMgr = UIMgr()
		#self.ListenForEvent(clientApi.GetEngineNamespace(), clientApi.GetEngineSystemName(), "ClientChestOpenEvent", self, self.OnClientChestOpenEvent)
		self.ListenForEvent(clientApi.GetEngineNamespace(), clientApi.GetEngineSystemName(),
		                    chestConsts.UiInitFinishedEvent, self, self.OnUiInitFinished)
		self.ListenForEvent(chestConsts.ModNameSpace, chestConsts.ServerSystemName, chestConsts.ShowApplicationTipsFromServerEvent,
		                    self, self.OnShowApplicationTipsFromServerEvent)
		self.ListenForEvent(chestConsts.ModNameSpace, chestConsts.ServerSystemName, chestConsts.ShowTipsFromServerEvent,
		                    self, self.OnShowTipsFromServerEvent)
		# self.ListenForEvent(chestConsts.ModNameSpace, chestConsts.ServerSystemName, chestConsts.ShowChestManageFromServerEvent,
		#                     self, self.OnShowChestManageFromServerEvent)
		
	def OnUiInitFinished(self, args):
		print "OnUiInitFinished", args
		self.mUIMgr.InitAllUI()
		
	# def OnShowChestManageFromServerEvent(self, args):
	# 	print "OnShowChestManageFromServerEvent", args
	
	def OnShowTipsFromServerEvent(self, args):
		print "OnShowTipsFromServerEvent", args
		def ClickCancelCB():
			print "ClickCancelCB"
			pass
		def ClickSureCB():
			print "ClickSureCB"
			pass
		UITips = self.GetUIMgr().GetUI(UIDef.UI_TIPS)
		print "UITips1", UITips
		CopyTips = NotifyDef.TIPS.copy()
		CopyTips["confirm"] = "确定"
		print "UITips2", UITips
		if UITips:
			UITips.SetNotifyPanel(CopyTips, ClickSureCB, ClickCancelCB, args.get("message"))
	
	def OnShowApplicationTipsFromServerEvent(self, args):
		print "OnShowApplicationTipsFromServerEvent", args
		owner = args.get("owner")
		cid = args.get("cid")
		pos = args.get("pos")
		blockText = args.get("blockText", "容器")
		message = "当前【%s】拥有者：【%s】" \
		          " 你没有使用该【%s】的权限，是否向【%s】申请使用权限？" % (blockText, owner, blockText, owner)
		def ClickCancelCB():
			print "ClickCancelCB"
			pass
		def ClickSureCB():
			print "ClickSureCB"
			data = {
				"cid" : cid,
				"pos" : pos,
				"playerId": self.mPlayerId
			}
			self.NotifyToServer(chestConsts.ApplicateFromClientEvent, data)
		UITips = self.GetUIMgr().GetUI(UIDef.UI_TIPS)
		print "UITips", UITips
		if UITips:
			UITips.SetNotifyPanel(NotifyDef.TIPS, ClickSureCB, ClickCancelCB, message)
		
	def GetUIMgr(self):
		return self.mUIMgr
	
	def Destroy(self):
		'''
		卸下 mod时会执行Destroy 函数。用于清理现场。
		'''
		pass