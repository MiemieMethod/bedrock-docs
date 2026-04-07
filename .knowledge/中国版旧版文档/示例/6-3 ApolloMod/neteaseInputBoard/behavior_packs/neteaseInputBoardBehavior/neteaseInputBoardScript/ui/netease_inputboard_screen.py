# -*- coding: utf-8 -*-
import client.extraClientApi as clientApi
from mod_log import logger

ScreenNode = clientApi.GetScreenNodeCls()

class InputBoardScreen(ScreenNode):
	"""
	InputBoard
	"""

	def __init__(self, namespace, name, param):
		ScreenNode.__init__(self, namespace, name, param)
		logger.info('==== %s ====' % 'init InputBoardScreen')

		self.m_input_panel_path = '/pnl_inputboard'
		self.m_custom_callback = None
		self.m_button_list = []
		self.m_board_id = ''

	# Create函数是继承自ScreenNode，会在UI创建完成后被调用
	def Create(self):
		logger.info('==== %s ====' % 'InputBoardScreen Create')

		# 主面板
		self.m_inputboard_panel = self.GetBaseUIControl(self.m_input_panel_path)

		self.m_close_btn = self.m_inputboard_panel.GetChildByPath('/img_bg/btn_close').asButton()
		self.m_title = self.m_inputboard_panel.GetChildByPath('/img_bg/lb_top_title').asLabel()
		self.m_text = self.m_inputboard_panel.GetChildByPath('/img_bg/lb_middle_content').asLabel()
		self.m_input_box = self.m_inputboard_panel.GetChildByPath('/img_bg/text_edit_input').asTextEditBox()
		self.m_button_0 = self.m_inputboard_panel.GetChildByPath('/img_bg/pnl_bottom/btn_bottom_0').asButton()
		self.m_button_1 = self.m_inputboard_panel.GetChildByPath('/img_bg/pnl_bottom/btn_bottom_1').asButton()

		self.m_close_btn.AddTouchEventParams({"isSwallow": True})
		self.m_close_btn.SetButtonTouchUpCallback(self.onClosePanel)

		
		self.m_button_0.AddTouchEventParams({"isSwallow": True})
		self.m_button_0.SetButtonTouchUpCallback(self.ButtonCallBackWrap)

		self.m_button_1.AddTouchEventParams({"isSwallow": True})
		self.m_button_1.SetButtonTouchUpCallback(self.ButtonCallBackWrap)

		self.m_button_list = [self.m_button_0,self.m_button_1]

		self.SetScreenVisible(False)
		self.SetIsHud(1)

	def onClosePanel(self, args=None):
		self.SetScreenVisible(False)
		self.SetIsHud(1)

	def Open(self, args):
		logger.info('netease inputboard screen open args: %s', args)
		self.m_title.SetText(args['title'] if 'title' in args else '')
		self.m_text.SetText(args['text'] if 'text' in args else '')
		self.m_input_box.SetEditText(args['input_text'] if 'input_text' in args else '')

		button_list = args['button_list'] if 'button_list' in args else []

		for i,button_args in enumerate(button_list):
			if i > len(self.m_button_list):
				break
			self.m_button_list[i].GetChildByPath('/label').asLabel().SetText(button_args['label'] if 'label' in button_args else '')


		self.SetScreenVisible(True)
		self.SetIsHud(0)

		self.m_board_id = args.get('board_id', '')

	
	def Close(self, board_id):
		# board_id为空则默认关闭
		if (not board_id) or (board_id == self.m_board_id):
			self.onClosePanel()

	def SetInputText(self, board_id, text):
		if ((not board_id) or (board_id == self.m_board_id)) and (text != None):
			self.m_input_box.SetEditText(text)

	def SetButtonCallback(self, callback):
		self.m_custom_callback = callback

	def ButtonCallBackWrap(self, args):
		if self.m_custom_callback:
			button_id = int(args["ButtonPath"].split("/")[-1].split("_")[-1])
			self.m_custom_callback(self.m_board_id, button_id, {'input_text': self.m_input_box.GetEditText()})

	
