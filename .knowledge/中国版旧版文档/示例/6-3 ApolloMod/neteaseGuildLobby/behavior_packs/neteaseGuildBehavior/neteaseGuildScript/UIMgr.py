# -*- coding: utf-8 -*-
import client.extraClientApi as clientApi
import logout
import guildConsts as guildConsts
from guildConsts import UIDef

class UIMgr(object):
	"""
	UI界面管理器
	"""
	def __init__(self):
		super(UIMgr, self).__init__()
		self.uis = {}
		self.present_uis = {}
		
	def InitAllUI(self, *args, **kwargs):
		self.Clear()
		self.InitUI(UIDef.UI_APPLY)
		self.InitUI(UIDef.UI_CREATEGUILD)
		self.InitUI(UIDef.UI_JOIN)
		self.InitUI(UIDef.UI_MYGUILD)
		self.InitUI(UIDef.UI_QUIT)
		self.InitUI(UIDef.UI_GUILDBTN)
		self.AfterInit()
	
	def AfterInit(self):
		pass
		# guildConsts.GetClientModSystem().GetGuildMgrGac().SetMyGuildUI()
		# guildConsts.GetClientModSystem().GetGuildMgrGac().SetCoinLabel()
	
	def CreateUI(self, ui_data, input_mode=0):
		print "CreateUI", ui_data
		ui_key = ui_data['ui_key']
		clientApi.RegisterUI(guildConsts.ModNameSpace, ui_key, ui_data["ui_cls_path"], ui_data["ui_def"])
		if ui_key == UIDef.UI_CREATEGUILD:
			ui = clientApi.CreateUI(guildConsts.ModNameSpace, ui_key, {"isHud": 0})
		else:
			ui = clientApi.CreateUI(guildConsts.ModNameSpace, ui_key, {"isHud": 1})
		if not ui:
			logout.error('==== %s ====' % '"create UI failed": %s' % ui_data['ui_def'])
			return
		self.uis[ui_key] = ui
		return ui

	def InitUI(self, ui_data, input_mode=0):
		print "InitUI", ui_data
		ui_key = ui_data['ui_key']
		if not self.present_uis.get(ui_key):
			ui = self.GetUI(ui_data) or self.CreateUI(ui_data, input_mode)
			ui.InitScreen()
			self.present_uis[ui_key] = True
			
	def GetUI(self, ui_data):
		ui_key = ui_data['ui_key']
		ui = self.uis.get(ui_key)
		if ui:
			return ui
		return clientApi.GetUI(guildConsts.ModNameSpace, ui_key)

	def RmUI(self, ui_key):
		ui = clientApi.GetUI(guildConsts.ModNameSpace, ui_key)
		if ui:
			if ui_key in self.uis:
				del self.uis[ui_key]
			ui.SetRemove()
			return True
		return False
	
	def Clear(self):
		self.uis.clear()
		self.present_uis.clear()
		
	def UnShowAllUI(self):
		for ui_key, ui in self.uis.items():
			if ui_key not in(UIDef.UI_QUIT.get('ui_key'), UIDef.UI_GUILDBTN.get('ui_key')):
				ui.ShowPanel(False)
			