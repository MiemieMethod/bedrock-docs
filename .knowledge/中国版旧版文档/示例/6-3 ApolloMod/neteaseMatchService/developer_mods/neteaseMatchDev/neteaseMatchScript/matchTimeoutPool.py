# -*- coding: utf-8 -*-
import neteaseMatchScript.playerInfo as playerInfo
import neteaseMatchScript.serviceConsts as serviceConsts
import neteaseMatchScript.apiUtil as apiUtil
import logout

class MatchTimeoutPool(object):
	'''
	管理匹配超时的玩家
	'''
	def __init__(self, activityData, tipsCb):
		self.mActivityData = activityData
		self.mUID2True = {}
		self.mTimeoutPlayers = []
		self.mTipsCB = tipsCb

	def Update(self):
		'''
		超时ui 10s后超时，超时后告知玩家显示错误提示
		'''
		if not self.mTimeoutPlayers:
			return
		timeoutPlayer = self.mTimeoutPlayers[0]
		if timeoutPlayer.IsTimeout():
			self.mTimeoutPlayers.remove(timeoutPlayer)
			self._delToUID2TRUE(timeoutPlayer.mMatchPlayerInfo)
			uiInfo = {
				'code' : serviceConsts.MatchCodeAutoCancelMatch,
				'message' : serviceConsts.Code2Message[serviceConsts.MatchCodeAutoCancelMatch],
				'display_time' : 3,
				'activity_id' : self.mActivityData['id']
			}
			self.mTipsCB(timeoutPlayer.mMatchPlayerInfo, uiInfo)

	def CancelMatch(self, uid):
		matchInfo = self.PopByUID(uid)
		if matchInfo:
			code = serviceConsts.MatchCodeCanceBySelf
			uiInfo = {
				'code': code,
				'message': serviceConsts.Code2Message[code],
				'activity_id': self.mActivityData['id'],
				'display_time' : 3,
			}
			self.mTipsCB(matchInfo, uiInfo)

	def NotifyToShowUI(self, uid):
		'''
		通知显示超时ui
		'''
		for timeoutPlayer in self.mTimeoutPlayers:
			matchInfo = timeoutPlayer.mMatchPlayerInfo
			if uid == matchInfo.mUID:
				code = serviceConsts.MatchCodeTimeoutCanRetry
				timeoutInfo = {
					'code': code,
					'message': serviceConsts.Code2Message[code],
					'activity_id': self.mActivityData['id'],
					'start_time': timeoutPlayer.mStartTime,
				}
				apiUtil.NotyfToServerByUID(matchInfo.mUID, serviceConsts.MatchResultServiceEvent, timeoutInfo)

	def AddTimeoutPlayer(self, matchInfo):
		'''
		添加一个匹配超时的玩家
		'''
		logout.warning('match timeout.uid:', matchInfo.mUID)
		if matchInfo.mBTeam:
			uiInfo = {
				'code' : serviceConsts.MatchCodeTimeoutNoRetry,
				'message' : serviceConsts.Code2Message[serviceConsts.MatchCodeTimeoutNoRetry],
				'display_time' : 3,
				'activity_id' : self.mActivityData['id']
			}
			uids = matchInfo.GetUIDs()
			for uid in uids:
				teamPlayer = playerInfo.TeamPlayerInfo(uid, matchInfo)
				self.mTipsCB(teamPlayer, uiInfo)
			return
		timeoutPlayer = playerInfo.MatchTimeoutPlayerInfo(matchInfo)
		self.mTimeoutPlayers.append(timeoutPlayer)
		timeoutInfo = {
			'code': serviceConsts.MatchCodeTimeoutCanRetry,
			'message': serviceConsts.Code2Message[serviceConsts.MatchCodeTimeoutCanRetry],
			'activity_id' : self.mActivityData['id'],
			'start_time' : timeoutPlayer.mStartTime,
		}
		apiUtil.NotyfToServerByUID(matchInfo.mUID, serviceConsts.MatchResultServiceEvent, timeoutInfo)
		self._addToUID2TRUE(matchInfo)

	def GetPlayerApplyTime(self, uid):
		if not self.IsInTimeout(uid):
			return -1
		matchInfo = self.getTimeoutPlayerInfo(uid)
		if matchInfo:
			return matchInfo.mRealStartTime
		return -1

	def getTimeoutPlayerInfo(self, uid):
		for timeoutPlayer in self.mTimeoutPlayers:
			matchInfo = timeoutPlayer.mMatchPlayerInfo
			matchUIDs = matchInfo.GetUIDs()
			if uid in matchUIDs:
				return matchInfo
		return None

	def PopByUID(self, uid):
		for timeoutPlayer in self.mTimeoutPlayers:
			matchInfo = timeoutPlayer.mMatchPlayerInfo
			if matchInfo.mUID == uid:
				self.mTimeoutPlayers.remove(timeoutPlayer)
				self._delToUID2TRUE(matchInfo)
				return matchInfo
		return None

	def IsInTimeout(self, uid):
		return self.mUID2True.get(uid, False)

	def _addToUID2TRUE(self, matchInfo):
		uid = matchInfo.mUID
		self.mUID2True[uid] = True
		uids = matchInfo.GetUIDs()
		for one in uids:
			self.mUID2True[one] = True

	def _delToUID2TRUE(self, matchInfo):
		uid = matchInfo.mUID
		uids = matchInfo.GetUIDs()
		uids.append(uid)
		for one in uids:
			if one in self.mUID2True:
				del self.mUID2True[one]
