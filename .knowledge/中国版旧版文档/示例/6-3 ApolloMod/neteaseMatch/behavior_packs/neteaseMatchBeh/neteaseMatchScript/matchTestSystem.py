# -*- coding: utf-8 -*-
'''
测试demo，服主可以参考本示例使用报名匹配插件
功能：
	1、进入界面显示报名界面
	2、使用自定义报名逻辑，使用分段匹配
'''
import client.extraClientApi as extraClientApi
ClientSystem = extraClientApi.GetClientSystemCls()
import client.extraClientApi as clientApi

class NeteaseMatchTest(ClientSystem):
	def __init__(self, namespace, systemName):
		ClientSystem.__init__(self, namespace, systemName)
		self.mMatchSystem = clientApi.GetSystem("neteaseMatch", "neteaseMatchClient")
		self.mMatchSystem.ShieldDefaultApplyMethod(3) #活动3 需要使用自定义的报名逻辑
		self.ListenForEvent('neteaseMatch', 'neteaseMatchClient', 'ApplyToMatchLocalEvent',
		                self, self.OnApplyToMatch)#由于使用分段匹配，所以必须要监听这个事件
		self.ListenForEvent('neteaseMatch', 'neteaseMatchClient', 'ApplyToMatchResultEvent',
		                self, self.OnApplyToMatchResult)#监听报名结果事件
		self.ListenForEvent('neteaseMatch', 'neteaseMatchClient', 'MatchResultEvent',
		                self, self.OnMatchResult)#监听匹配结果事件
		comp = clientApi.GetEngineCompFactory().CreatePlayer(clientApi.GetLocalPlayerId())
		self.mLocalUID = int(comp.getUid())
		self.mPlayerLevel = 9 #玩家等级是9，按照玩家等级匹配
		self.mOpenMatchCnt = 0

	def Update(self):
		self.mOpenMatchCnt += 1
		if 300 == self.mOpenMatchCnt:
			self.mMatchSystem.OpenMatchUI(3) #打开报名界面
		# if 700 == self.mOpenMatchCnt:
		# 	self.mMatchSystem.ApplyToMatchActivity(3, 7, 9)
		# 	self.mMatchSystem.ApplyToMatchActivity(3, 8, 9)
		# if 300 == self.mOpenMatchCnt:
		# 	self.mMatchSystem.OpenMatchUI(1)  # 打开活动3的报名界面
		# if self.mOpenMatchCnt > 200 and self.mOpenMatchCnt % 100 == 0:
		# 	self.mMatchSystem.ApplyToMatchActivity(1, self.mLocalUID, self.mPlayerLevel)
		# if 300 == self.mOpenMatchCnt:
		# 	self.mMatchSystem.OpenMatchUI(3)  # 打开活动3的报名界面
		# if 600 == self.mOpenMatchCnt:
		# 	self.mMatchSystem.OpenMatchUI(3)  # 打开活动3的报名界面

	def OnApplyToMatch(self, args):
		'''
		申请报名，使用分段报名，单人报名。分段值为玩家等级，会匹配到第一个分段的玩家，匹配到玩家等级范围为[0, 10]
		'''
		print 'OnApplyToMatch', args
		self.mMatchSystem.ApplyToMatchActivity(args['activity_id'], self.mLocalUID, self.mPlayerLevel, False)

	def OnApplyToMatchResult(self, args):
		'''
		打印报名的结果
		'''
		print 'Test OnApplyToMatchResult', args

	def OnMatchResult(self, args):
		'''
		打印匹配结果
		'''
		print 'Test OnMatchResult', args

	def Destroy(self):
		self.mMatchSystem = None
		ClientSystem.Destroy(self)

