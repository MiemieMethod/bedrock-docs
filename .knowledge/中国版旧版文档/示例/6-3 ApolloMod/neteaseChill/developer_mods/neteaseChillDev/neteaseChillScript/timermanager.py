# -*- coding: utf-8 -*-

"""
系统的定时器功能
addTimer是一次性的Timer
addRepeatTimer是重复的Timer
"""

# import time
import service.asyncore_with_timer as asyncore_with_timer

UniqueTimerId = 0


def getTimerId():
	global UniqueTimerId
	timerId = UniqueTimerId
	UniqueTimerId = UniqueTimerId + 1
	return timerId


class TimerManager(object):
	def __init__(self):
		self.timers = {}

	def addTimer(self, delay, func, *args, **kwargs):
		"""
		- (float) delay: the number of seconds to wait. The timer granularity
			depends on the timeout value of asyncore_with_timer.loop
		- (obj) func: the callable object to call later
		- args: the arguments to call it with
		- kwargs: the keyword arguments to call it with; a special
			'_errback' parameter can be passed: it is a callable
			called in case target function raises an exception.
		- return a timer object can reset or cancel
		"""
		timerId = getTimerId()
		self.timers[timerId] = asyncore_with_timer.CallLater(delay, func, *args, **kwargs)
		return timerId

	def addRepeatTimer(self, delay, func, *args, **kwargs):
		"""
		- (float) delay: call it every 'delay' seconds
		- (obj) func: the callable object to call later
		- args: the arguments to call it with
		- kwargs: the keyword arguments to call it with; a special
			'_errback' parameter can be passed: it is a callable
			called in case target function raises an exception.
		- return a timer object can reset or cancel
		"""
		timerId = getTimerId()
		self.timers[timerId] = asyncore_with_timer.CallEvery(delay, func, *args, **kwargs)
		return timerId

	def delTimer(self, timerId):
		timer = self.timers.pop(timerId, None)
		if timer:
			timer.cancel()

	def tick(self):
		for timerId in self.timers:
			timer = self.timers[timerId]
			if timer.expired:
				timer.cancel()
				self.delTimer(timerId)
		asyncore_with_timer.scheduler()

	def finish(self):
		asyncore_with_timer.close_all()
		self.delTimer = None


timerManager = TimerManager()
