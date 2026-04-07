# -*- coding: utf-8 -*-
import neteaseMatchScript.playerInfo as playerInfo
import logout
import neteaseMatchScript.apiUtil as apiUtil
import neteaseMatchScript.serviceConsts as serviceConsts

class MatchTipsPool(object):
	'''
	管理匹配提示信息。注意：切服和切维度不会丢失错误提示
	'''
	def __init__(self):
		self.mPlayerTipsList = []

	def AddMatchErr(self, matchInfo, errInfo):
		'''
		添加匹配错误提示
		'''
		tips = playerInfo.PlayerUITips(matchInfo, errInfo)
		self.mPlayerTipsList.append(tips)
		apiUtil.NotyfToServerByUID(matchInfo.mUID, serviceConsts.MatchResultServiceEvent, tips.mTipsInfo)

	def Update(self):
		'''
		错误提示超时则删除掉提示
		'''
		if not self.mPlayerTipsList:
			return
		tips = self.mPlayerTipsList[0]
		if tips.IsTimeout():
			matchInfo = tips.matchPlayerInfo
			logout.info("tips not send to player.uid:%s.tips info:" % matchInfo.mUID, tips.mTipsInfo)

	def GetTipsByUID(self, uid):
		userTips = [tips for tips in self.mPlayerTipsList if tips.mMatchPlayerInfo.mUID == uid]
		return userTips

	def RemoveById(self, tipsId):
		for tips in self.mPlayerTipsList:
			if tips.mId == tipsId:
				self.mPlayerTipsList.remove(tips)
				break

	def PlayerLogout(self, uid):
		cnt = 0
		for idx, tips in enumerate(self.mPlayerTipsList):
			if tips.mMatchPlayerInfo.mUID == uid:
				cnt += 1
				self.mPlayerTipsList[idx] = None
		for i in xrange(cnt):
			self.mPlayerTipsList.remove(None)

	def NotifyToShowTips(self, uid):
		'''
		通知玩家显示错误提示
		'''
		for tips in self.mPlayerTipsList:
			if tips.mMatchPlayerInfo.mUID == uid:
				apiUtil.NotyfToServerByUID(uid, serviceConsts.MatchResultServiceEvent, tips.mTipsInfo)



