# -*- coding: utf-8 -*-
import time

# 这个类的作用是延迟执行给定的函数
# 使用参考每个具体使用的地方，yield 正数为时间，负数为帧数
class CoroutineMgr(object):
	def __init__(self):
		self.coroutines = {}
		self.globalEnd = []
		self.addCoroutines = {}

	def DelayNoParamFunc(self, frame, function):
		def DelayFunc():
			yield -frame
			function()

		self.StartCoroutine(DelayFunc())

	def DelayExecFunc(self, func, delay, *args, **kwargs):
		def DelayFunc():
			yield delay
			func(*args, **kwargs)

		self.StartCoroutine(DelayFunc())

	def StartCoroutine(self, iterFunc):
		self.addCoroutines[iterFunc] = 0
		return iterFunc

	def StopCoroutine(self, iterFunc):
		self.globalEnd.append(iterFunc)

	def Tick(self):
		if self.addCoroutines:
			for c,v in self.addCoroutines.iteritems():
				self.coroutines[c] = v
		self.addCoroutines = {}
		if self.globalEnd:
			for c in self.globalEnd:
				if self.coroutines.get(c):
					del self.coroutines[c]
			self.globalEnd = []
		endList = []
		for c, v in self.coroutines.iteritems():
			try:
				if v < 0:
					v += 1
					self.coroutines[c] = v
				if v == 0 or (time.time() >= v > 0):
					newv = c.next()
					if newv > 0:
						newv = newv + time.time()
					self.coroutines[c] = newv
			except StopIteration:
				endList.append(c)
		for c in endList:
			del self.coroutines[c]

	def Destroy(self):
		self.coroutines = {}
		self.globalEnd = []
		self.addCoroutines = {}