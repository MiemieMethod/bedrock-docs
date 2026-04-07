# -*- coding: utf-8 -*-

class BaseMatchPool(object):
	'''
	玩家匹配基类
	'''
	def IsInMatching(self, uid):
		return False

	def Update(self):
		pass

	def AddNewPlayer(self, matchInfo):
		pass

	def GetMatchingNum(self):
		return 0

	def NotifyShowWaitUIByUid(self, uid):
		pass

	def PlayerLogout(self, uid):
		pass

	def CancelMatching(self, uid):
		pass

	def GetPlayerApplyTime(self, uid):
		return -1

	def GetAppliedUIDs(self):
		return []