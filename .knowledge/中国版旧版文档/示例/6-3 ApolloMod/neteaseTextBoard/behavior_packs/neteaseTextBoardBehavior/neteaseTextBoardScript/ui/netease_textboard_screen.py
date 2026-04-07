# -*- coding: utf-8 -*-
import client.extraClientApi as clientApi

ScreenNode = clientApi.GetScreenNodeCls()

class TextBoardScreen(ScreenNode):
	"""
	TextBoard
	"""

	def __init__(self, namespace, name, param):
		ScreenNode.__init__(self, namespace, name, param)
		print '==== %s ====' % 'init TextBoardScreen'

		self.m_text_panel_path = '/pnl_textInterface'

	# Create函数是继承自ScreenNode，会在UI创建完成后被调用
	def Create(self):
		print '==== %s ====' % 'TextBoardScreen Create'

		# 主面板
		self.m_textboard_panel = self.GetBaseUIControl(self.m_text_panel_path)

		# 文本信息
		self.m_text_content  = self.m_textboard_panel.GetChildByPath("/img_text_bg/lb_text_content").asLabel()
		
		self.SetScreenVisible(False)
		
	def SetContent(self, content):
		self.m_text_content.SetText(content)
	
	def GetContent(self):
		return self.m_text_content.GetText()

	def Open(self):
		self.SetScreenVisible(True)
	
	def Close(self):
		self.SetScreenVisible(False)
	
