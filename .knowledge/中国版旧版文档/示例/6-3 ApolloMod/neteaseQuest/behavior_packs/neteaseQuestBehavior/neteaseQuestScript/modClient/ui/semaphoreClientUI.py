# -*- coding: utf-8 -*-

from .. import logger
# 从客户端API中拿到我们需要的ViewBinder / ViewRequest / ScreenNode
import client.extraClientApi as clientApi

ScreenNode = clientApi.GetScreenNodeCls()


class SemaphoreScreen(ScreenNode):
	def __init__(self, namespace, name, param):
		ScreenNode.__init__(self, namespace, name, param)
		logger.info('==== %s ====' % 'init SemaphoreScreen')

		# 'textures/ui/netease_quest/{}'

		self.m_semaphore_panel = '/semaphore_panel'
		self.m_semaphore_icon = '/semaphore_panel/icon'

		self.m_icon = None

	# Create函数是继承自ScreenNode，会在UI创建完成后被调用
	def Create(self):
		pass

	# 继承自ScreenNode的方法，会被引擎自动调用，1秒钟30帧
	def Update(self):
		pass

	def get_icon(self):
		return self.m_icon

	def set_icon(self, phrase):
		self.m_icon = phrase
		self.SetSprite(self.m_semaphore_icon, 'textures/ui/netease_quest/{}'.format(phrase))

	def show(self):
		self.SetVisible(self.m_semaphore_icon, True)

	def hide(self):
		self.SetVisible(self.m_semaphore_icon, False)
