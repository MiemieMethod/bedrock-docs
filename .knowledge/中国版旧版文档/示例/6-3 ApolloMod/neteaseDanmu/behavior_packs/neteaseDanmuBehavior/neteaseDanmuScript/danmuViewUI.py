# -*- coding: utf-8 -*-

import client.extraClientApi as clientApi

ScreenNode = clientApi.GetScreenNodeCls()


class Wrapper:
	"""
	通道封装类
	"""

	def __init__(self, p, o, m):
		self.p = p  # 控件路径
		self.o = o  # 序号
		self.m = m  # 类型[从右至左|中部]
		self.done = True  # 完成状态
		self.msg = None  # 消息封装类，详见MyMsg

	def prepare(self, node):
		node.SetVisible(self.p, True)
		self.msg.prepare(node, self)  # 播放前的准备

	def tick(self, node):
		if self.msg:
			return self.msg.tick(node, self)
		node.SetVisible(self.p, False)
		self.done = True


class DanmuScreen(ScreenNode):
	"""
	弹幕界面
	"""

	def __init__(self, namespace, name, param):
		ScreenNode.__init__(self, namespace, name, param)
		print '==== %s ====' % 'init DanmuScreen'

		self.ms = {i: {  # 分为空闲和工作中两种状态，初始均为空闲，开始运作时会从空闲的通道中弹出一个至工作中列表
			'available': [Wrapper('/scope_panel/top_middle{}'.format(i), i, 'm')],
			'busy': []
		} for i in xrange(20)}  # 20条中部弹幕通道
		self.rs = {i: {  # 同上
			'available': [Wrapper('/scope_panel/top_right{}'.format(i * 10 + j), i, 'r') for j in xrange(10)],  # 每行10条
			'busy': []
		} for i in xrange(20)}  # 200条从右至左弹幕通道
		self.flow = []
		self.protocol = None
		self.producer = None  # 数据在客户端类中

	# Create函数是继承自ScreenNode，会在UI创建完成后被调用
	def Create(self):
		print '==== %s ====' % 'DanmuScreen Create'

		self.width = self.GetSize('/scope_panel')[0]  # 屏幕总宽度，一条弹幕需位移这个量加上自身文本框的长度才能算播放完毕
		self.pm = {i: self.GetPosition(self.rs[i]['available'][0].p) for i in xrange(20)}  # 从右至左通道的初始位置

	def InitScreen(self):
		print '==== %s ====' % 'DanmuScreen Init'

		if self.producer is None:
			self.producer = clientApi.GetSystem('neteaseDanmu', 'neteaseDanmuBeh')

	# 继承自ScreenNode的方法，会被引擎自动调用，1秒钟30帧
	def Update(self, closure={'count': 0}):  # 闭包记录一个tick次数
		for i in xrange(len(self.flow) - 1, -1, -1):  # 这是一个技巧，涉及到删除链表操作，从链表长度倒着数就可以不会影响到后续的序号正常取出元素
			w = self.flow[i]  # 工作中的一条通道
			w.tick(self)  # 该通道自运作，详见Wrapper类
			if w.done:
				# 该条弹幕已播放完毕
				c = w.m == 'm' and self.ms or self.rs  # 找到是哪种位置类型
				c[w.o]['busy'].remove(w)  # 找到是0-19哪个序号的通道，从工作中列表移出
				c[w.o]['available'].append(w)  # 找到是0-19哪个序号的通道，加入空闲列表
				del self.flow[i]  # 从运作中列表剔除

		if self.producer:
			if self.protocol != self.producer.Partition and 0 < self.producer.Partition < 5:
				# 可用范围改变了
				self.protocol = self.producer.Partition
				for i in xrange(5 * self.protocol, 20):
					for c in (self.rs, self.ms):
						for work in c[i]['busy']:
							work.msg = None  # 下轮update就会直接判定为播放完毕并关闭显示

			if self.protocol is None:
				# 并未有弹幕的情况
				return

			closure['count'] += 1
			if closure['count'] % 16:
				closure['count'] = 0
				msg = self.producer.produce()  # 取出一条弹幕消息
				if msg:
					# 取到了
					c = msg.mode == 'm' and self.ms or self.rs
					k = max(xrange(5 * self.protocol), key=lambda k: len(c[k]['available']))  # 空闲通道持有数最多的组弹出一个通道
					a = len(c[k]['available'])
					if a:
						w = c[k]['available'].pop(0)
						w.done = False
						w.msg = msg
						w.prepare(self)
						c[k]['busy'].append(w)
						self.flow.append(w)
					else:
						# a为0
						self.producer.shift(msg)  # 均无空闲，先把消息放回去

	def appear(self):
		self.SetVisible('/scope_panel', True)

	def disable(self):
		self.SetVisible('/scope_panel', False)
