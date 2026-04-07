# -*- coding: utf-8 -*-
import client.extraClientApi as clientApi
import logout
import chestConsts as chestConsts
from chestConsts import UIDef


class UIMgr(object):
	def __init__(self):
		super(UIMgr, self).__init__()
		self.uis = {}
		self.present_uis = {}
	
	def InitAllUI(self, *args, **kwargs):
		self.Clear()
		self.InitUI(UIDef.UI_TIPS)
		self.InitUI(UIDef.UI_MANAGE)
		self.AfterInit()
	
	def AfterInit(self):
		pass
	
	def CreateUI(self, ui_data, input_mode=0):
		print "CreateUI===========", ui_data
		ui_key = ui_data['ui_key']
		clientApi.RegisterUI(chestConsts.ModNameSpace, ui_key, ui_data["ui_cls_path"], ui_data["ui_def"])
		print "ui_key : %s == ui_cls_path : %s == ui_def : %s", ui_data['ui_key'], ui_data["ui_cls_path"], ui_data["ui_def"]
		ui = clientApi.CreateUI(chestConsts.ModNameSpace, ui_key, {"isHud": 1})
		print "CreateUI2==========="
		if not ui:
			print '==== %s ====' % '"create UI failed": %s' % ui_data['ui_def']
			logout.error('==== %s ====' % '"create UI failed": %s' % ui_data['ui_def'])
			return
		self.uis[ui_key] = ui
		print "End CreateUI===========", ui_data
		return ui
	
	def InitUI(self, ui_data, input_mode=0):
		print "InitUI============", ui_data
		ui_key = ui_data['ui_key']
		if not self.present_uis.get(ui_key):
			ui = self.GetUI(ui_data) or self.CreateUI(ui_data, input_mode)
			print "before InitScreen===========", ui
			ui.InitScreen()
			self.present_uis[ui_key] = True
	
	def GetUI(self, ui_data):
		ui_key = ui_data['ui_key']
		ui = self.uis.get(ui_key)
		if ui:
			return ui
		return clientApi.GetUI(chestConsts.ModNameSpace, ui_key)
	
	def RmUI(self, ui_key):
		ui = clientApi.GetUI(chestConsts.ModNameSpace, ui_key)
		if ui:
			if ui_key in self.uis:
				del self.uis[ui_key]
			ui.SetRemove()
			return True
		return False
	
	def Clear(self):
		self.uis.clear()
		self.present_uis.clear()
	
