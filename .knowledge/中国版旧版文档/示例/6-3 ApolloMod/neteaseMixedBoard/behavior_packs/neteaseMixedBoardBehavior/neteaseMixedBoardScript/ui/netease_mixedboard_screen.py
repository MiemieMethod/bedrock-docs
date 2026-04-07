# -*- coding: utf-8 -*-
import client.extraClientApi as clientApi
from mod_log import logger

ScreenNode = clientApi.GetScreenNodeCls()

class MixedBoardScreen(ScreenNode):
	"""
	MixedBoard
	"""

	def __init__(self, namespace, name, param):
		ScreenNode.__init__(self, namespace, name, param)
		logger.info('==== %s ====' % 'init MixedBoardScreen')

		self.m_mixed_panel_path = '/pnl_mixedboard_window'
		self.m_board_id = ''


	# Create函数是继承自ScreenNode，会在UI创建完成后被调用
	def Create(self):
		logger.info('==== %s ====' % 'MixedBoardScreen Create')

		# 主面板
		self.m_mixedboard_panel = self.GetBaseUIControl(self.m_mixed_panel_path)

		
		self.m_close_btn = self.m_mixedboard_panel.GetChildByPath('/img_mixboard_bg/btn_close').asButton()
		self.m_title = self.m_mixedboard_panel.GetChildByPath('/img_mixboard_bg/lb_top_title').asLabel()
		self.m_scroll_view = self.m_mixedboard_panel.GetChildByPath('/img_mixboard_bg/scroll_view').asScrollView()
		self.m_scroll_path = self.m_scroll_view.GetScrollViewContentPath()
		self.m_scroll_content = self.GetBaseUIControl(self.m_scroll_path)
		
		self.m_close_btn.AddTouchEventParams({"isSwallow": True})
		self.m_close_btn.SetButtonTouchUpCallback(self.onClosePanel)

		scroll_text_path = '{}/scroll_text_content'.format(self.m_scroll_path)
		self.m_scroll_text = self.GetBaseUIControl(scroll_text_path).asLabel()
		self.m_scroll_text_pos = self.m_scroll_text.GetPosition()

		self.m_button_list = []
		button0_path = '{}/btn_bottom_0'.format(self.m_scroll_path)
		button0 = self.GetBaseUIControl(button0_path).asButton()
		self.m_scorll_view_size = self.m_scroll_view.GetSize()
		self.m_button_size = button0.GetSize()
		self.m_button_pos = button0.GetPosition()
		self.m_button_list.append(button0_path)

		self.m_custom_callback = None

		self.SetScreenVisible(False)
		self.SetIsHud(1)

	def onClosePanel(self, args=None):
		self.SetScreenVisible(False)
		self.SetIsHud(1)

	def Open(self, args):
		logger.info('netease mixedboard screen open args: %s', args)

		self.SetScreenVisible(True)
		self.SetIsHud(0)

		self.m_title.SetText(args['title'] if 'title' in args else '')
		self.m_scroll_text.SetText(args['text'] if 'text' in args else '', True)

		scroll_text_size = self.m_scroll_text.GetSize()
		button_offset = (self.m_scroll_text_pos[0], self.m_scroll_text_pos[1] + scroll_text_size[1] + 5)

		# 最多显示16个按钮
		button_demand = min(16, len(args['button_list'])) if 'button_list' in args else 0
		if button_demand > 0:
			cur= len(self.m_button_list)
			if button_demand > cur:
				for i in xrange(cur,button_demand):
					button_name = 'btn_bottom_{}'.format(i)
					self.Clone(self.m_button_list[0], self.m_scroll_path, button_name)
					button_path = '{}/{}'.format(self.m_scroll_path, button_name)
					self.m_button_list.append(button_path)
		
		for i, button_path in enumerate(self.m_button_list):
			button = self.GetBaseUIControl(button_path).asButton()
			if i < button_demand:
				button.GetChildByPath("/label").asLabel().SetText(args['button_list'][i].get('label', ''))
				self.SetUiItem(button_path+'/item_renderer',args['button_list'][i].get('icon', ''), 0)
				button.SetPosition((button_offset[0], button_offset[1] + (self.m_button_size[1]+5)*i))

				button.AddTouchEventParams({"isSwallow": True})
				button.SetButtonTouchUpCallback(self.ButtonCallBackWrap)

			button.SetVisible(i < button_demand)

		self.m_scroll_content.SetSize((self.m_scorll_view_size[0],button_offset[1] + (self.m_button_size[1]+5)*button_demand))

		
		self.m_board_id = args.get('board_id', '')
	
	def Close(self, board_id):
		# board_id为空则默认关闭
		if (not board_id) or (board_id == self.m_board_id):
			self.onClosePanel()

	def SetButtonCallback(self, callback):
		self.m_custom_callback = callback

	def ButtonCallBackWrap(self, args):
		if self.m_custom_callback:
			button_id = int(args["ButtonPath"].split("/")[-1].split("_")[-1])
			self.m_custom_callback(self.m_board_id, button_id)

	
