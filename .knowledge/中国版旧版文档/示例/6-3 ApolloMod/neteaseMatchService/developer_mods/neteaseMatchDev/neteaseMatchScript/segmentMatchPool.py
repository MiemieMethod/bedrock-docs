# -*- coding: utf-8 -*-
import neteaseMatchScript.matchPool as matchPool
import neteaseMatchScript.baseMatchPool as baseMatchPool
import logout
import neteaseMatchScript.serviceConsts as serviceConsts
import neteaseMatchScript.apiUtil as apiUtil
class SegmentMatchPool(baseMatchPool.BaseMatchPool):
	'''
	分段匹配池，每个分段对应一个匹配池，匹配逻辑委托匹配池处理
	'''
	def __init__(self, activityData, timeoutCb, matchOKCb, tipsCb):
		self.mSegId2MatchPool = {}
		for data in activityData['match_segment']:
			pool = matchPool.MatchPool(activityData, data['first_match_timeout'], data['again_match_timeout'],
					activityData['group_player_num'], activityData['is_team_same_group'],
					True, timeoutCb, matchOKCb, tipsCb)
			pool.SetGetMatchingNumFunc(self.GetMatchingNum)
			pool.SetGetWaitingUIDsFunc(self.GetWaitingUIDs)
			self.mSegId2MatchPool[data['id']] = pool
		self.mTipsCb = tipsCb
		self.mActivityData = activityData

	def GetPlayerApplyTime(self, uid):
		for pool in self.mSegId2MatchPool.itervalues():
			apply = pool.GetPlayerApplyTime(uid)
			if apply > 0:
				return apply
		return -1

	def GetAppliedUIDs(self):
		uids = []
		for pool in self.mSegId2MatchPool.itervalues():
			lst = pool.GetAppliedUIDs()
			uids.extend(lst)
		return uids

	def PlayerLogout(self, uid):
		self.CancelMatching(uid)

	def CancelMatching(self, uid):
		for pool in self.mSegId2MatchPool.itervalues():
			pool.CancelMatching(uid)

	def GetMatchingNum(self):
		curNum = 0
		for pool in self.mSegId2MatchPool.itervalues():
			curNum += pool.GetMatchingNum()
		return curNum

	def GetWaitingUIDs(self):
		uids = []
		for pool in self.mSegId2MatchPool.itervalues():
			lst = pool.GetWaitingUIDs()
			uids.extend(lst)
		return uids

	def NotifyShowWaitUIByUid(self, uid):
		for pool in self.mSegId2MatchPool.itervalues():
			pool.NotifyShowWaitUIByUid(uid)

	def IsInMatching(self, uid):
		for pool in self.mSegId2MatchPool.itervalues():
			if pool.IsInMatching(uid):
				return True
		return False

	def AddNewPlayer(self, matchInfo):
		segmentId, err = self._findSementId(matchInfo)
		if segmentId < 0:
			logout.error('AddNewPlayer.not match segment.match uid:', matchInfo.mUID)
			eventData = {
				'message': err,
				'code': serviceConsts.ApplyCodeNotMatchFregment,
				'display_time': 3,
				'ui_id': -1,
				'activity_id': self.mActivityData['id'],
				'uid': matchInfo.mUID
			}
			apiUtil.NotyfToServerByUID(matchInfo.mUID, serviceConsts.ApplyErrServiceEvent, eventData)
			return
		pool = self.mSegId2MatchPool[segmentId]
		pool.AddNewPlayer(matchInfo)

	def AddOldPlayer(self, matchInfo):
		matchInfo.AgainMatch()
		segmentId, err = self._findSementId(matchInfo)
		if segmentId < 0:
			logout.error('AddOldPlayer.not match segment.match uid:', matchInfo.mUID)
			eventData = {
				'message': err,
				'code': serviceConsts.ApplyCodeNotMatchFregment,
				'display_time': 3,
				'ui_id': -1,
				'activity_id': self.mActivityData['id'],
				'uid': matchInfo.mUID
			}
			apiUtil.NotyfToServerByUID(matchInfo.mUID, serviceConsts.ApplyErrServiceEvent, eventData)
			return
		pool = self.mSegId2MatchPool[segmentId]
		pool.AddOldPlayer(matchInfo)

	def _findSementId(self, matchInfo):
		'''
		return (segmentId, err)找到所属的分段，segmentId:-1表示不满足分段
		'''
		matchId = -1
		segmentDataList = self.mActivityData['match_segment']
		val = matchInfo.mMatchValue
		segmentData = None
		for data in segmentDataList:
			if val >= data['min'] and val <= data['max']:
				matchId = data['id']
				segmentData = data
				break
		if matchId < 0:
			return (matchId, serviceConsts.Code2Message[serviceConsts.ApplyCodeNotMatchFregment] % matchInfo.mNickname)
		#检查队员是否也满足条件
		for member in matchInfo.mGroupMembers:
			val = member.mMatchVal
			if val < segmentData['min'] or val > segmentData['max']:
				return (-1, serviceConsts.Code2Message[serviceConsts.ApplyCodeNotMatchFregment] % member.mNickname)
		return matchId, ''

	def Update(self):
		for pool in self.mSegId2MatchPool.itervalues():
			pool.Update()