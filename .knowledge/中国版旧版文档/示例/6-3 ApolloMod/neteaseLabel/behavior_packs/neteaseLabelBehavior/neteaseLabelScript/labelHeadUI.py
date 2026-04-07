# -*- coding: utf-8 -*-

# 从客户端API中拿到我们需要的ViewBinder / ViewRequest / ScreenNode
import client.extraClientApi as clientApi

ScreenNode = clientApi.GetScreenNodeCls()


class LabelHeadScreen(ScreenNode):
	def __init__(self, namespace, name, param):
		ScreenNode.__init__(self, namespace, name, param)
		print '==== %s ====' % 'init LabelHeadScreen'

		self.mLabelPic = '/label_head_panel/text/pic'
		self.mLabelText = '/label_head_panel/text'

		self.mLabel = None

	def GetLabel(self):
		return self.mLabel

	def SetLabel(self, label):
		self.mLabel = label
		if label['part'] == 2 and label['res']:
			self.SetSprite(self.mLabelPic, label['res'])
			self.SetVisible(self.mLabelPic, True)
			self.SetText(self.mLabelText, '')
		else:
			self.SetVisible(self.mLabelPic, False)
			self.SetText(self.mLabelText, label['text'])

	def Show(self):
		self.SetVisible("", True)

	def Hide(self):
		self.SetVisible("", False)
