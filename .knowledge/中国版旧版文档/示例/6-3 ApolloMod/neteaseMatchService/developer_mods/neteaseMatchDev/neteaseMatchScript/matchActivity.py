# -*- coding: utf-8 -*-
import neteaseMatchScript.matchPool as matchPool
import neteaseMatchScript.segmentMatchPool as segmentMatchPool
import neteaseMatchScript.matchTimeoutPool as matchTimeoutPool
import neteaseMatchScript.matchOKPool as matchOKPool
import neteaseMatchScript.matchTipsPool as matchTipsPool
import neteaseMatchScript.serviceConsts as serviceConsts
import logout

class MatchActivity(object):
	'''
	处理一个活动相关逻辑
	'''
	def __init__(self, data):
		self.mActivityData = data
		self.mMatchTipsPool = matchTipsPool.MatchTipsPool()
		tipsCb = self.mMatchTipsPool.AddMatchErr
		self.mMatchTimeoutPool = matchTimeoutPool.MatchTimeoutPool(data, tipsCb)
		self.mMatchOKPool = matchOKPool.MatchOKPool(data)
		matchOKCb = self.mMatchOKPool.AddRoom
		timeoutCB = self.mMatchTimeoutPool.AddTimeoutPlayer
		data = self.mActivityData
		if self.mActivityData['is_match_by_segment']:
			self.mMatchPool = segmentMatchPool.SegmentMatchPool(self.mActivityData, timeoutCB, matchOKCb, tipsCb)
		else:
			firstTimeout = data.get('first_match_timeout', 10)
			againTimeout = data.get('again_match_timeout', 10)
			bSameGroup = data.get('is_team_same_group', False)
			self.mMatchPool = matchPool.MatchPool(data, firstTimeout, againTimeout, data['group_player_num'],
						bSameGroup, data['is_match_by_segment'], timeoutCB, matchOKCb, tipsCb)

	def IsInMatching(self, uid):
		'''
		是否匹配中
		'''
		if self.mMatchPool.IsInMatching(uid):
			return True
		return self.mMatchTimeoutPool.IsInTimeout(uid)

	def GetAppliedUIDs(self):
		return self.mMatchPool.GetAppliedUIDs()

	def GetPlayerApplyTime(self, uid):
		apply = self.mMatchPool.GetPlayerApplyTime(uid)
		if apply > 0:
			return apply
		return self.mMatchTimeoutPool.GetPlayerApplyTime(uid)

	def ReMatch(self, uid):
		'''
		重新匹配
		'''
		logout.error('ReMatch begin.uid:', uid)
		if self.mMatchPool.IsInMatching(uid):
			logout.warning('ReMatch success.player is in pool.uid:%s' % uid)
			return serviceConsts.CodeSuccess
		matchInfo = self.mMatchTimeoutPool.PopByUID(uid)
		if matchInfo is None:
			logout.error('ReMatch fail.player not in timeout pool.uid:', uid)
			return serviceConsts.ReMatchCodeNotInPool
		self.mMatchPool.AddOldPlayer(matchInfo)
		return serviceConsts.CodeSuccess

	def CancelMatching(self, uid):
		self.mMatchPool.CancelMatching(uid)
		self.mMatchTimeoutPool.CancelMatch(uid)

	def PlayerLogout(self, uid):
		self.mMatchTimeoutPool.CancelMatch(uid)
		self.mMatchPool.PlayerLogout(uid)
		self.mMatchTipsPool.PlayerLogout(uid)
		self.mMatchOKPool.PlayerLogout(uid)

	def NotifyShowWaitUIByUid(self, uid):
		self.mMatchTimeoutPool.NotifyToShowUI(uid)
		self.mMatchPool.NotifyShowWaitUIByUid(uid)
		self.mMatchTipsPool.NotifyToShowTips(uid)
		self.mMatchOKPool.ComfirmToUser(uid)

	def AddNewPlayer(self, matchInfo):
		self.mMatchPool.AddNewPlayer(matchInfo)

	def RemoveTips(self, tipsId):
		self.mMatchTipsPool.RemoveById(tipsId)

	def ConfirmMatchOK(self, id, uid):
		self.mMatchOKPool.ConfirmOk(id, uid)

	def Update(self):
		self.mMatchPool.Update()
		self.mMatchOKPool.Update()
		self.mMatchTipsPool.Update()
		self.mMatchTimeoutPool.Update()