# -*- coding:utf-8 -*-

class EventManger(object):
	"""
	用于mod游戏逻辑的事件系统，用于解决“不知道在哪里加代码逻辑”的问题，类似modSDK提供的事件功能，只是这个不限于系统之间的通知
	"""
	def __init__(self):
		super(EventManger, self).__init__()
		self.mEventDict = {}  # {eventId : func}

	def RegisterEvent(self, eventId, func):
		"""
		监听事件，传入函数实例
		"""
		if eventId not in self.mEventDict:
			self.mEventDict[eventId] = set()
		self.mEventDict[eventId].add(func)

	def NotifyEvent(self, eventId, eventArgs=None):
		"""
		触发事件，执行之前Register传进来的函数，调用时注意规范好eventArgs
		"""
		if not eventId in self.mEventDict:
			return
		for func in list(self.mEventDict[eventId]):
			func(eventArgs)
			#try:
			#	func(eventArgs)
			#except Exception, e:
			#	print "NotifyEvent {} {} error : {}".format(eventId, func.__name__, e)
			#	import traceback
			#	traceback.print_stack()

	def UnRegisterEvent(self, eventId, func):
		"""
		反监听事件，与Register一致
		:return:
		"""
		if eventId in self.mEventDict:
			self.mEventDict[eventId].discard(func)

	def Destroy(self):
		for eventId, funcSet in self.mEventDict.iteritems():
			self.mEventDict[eventId] = None
		self.mEventDict = {}
