# -*- coding: utf-8 -*-
import neteaseMatchScript.playerInfo as playerInfo
import neteaseMatchScript.baseMatchPool as baseMatchPool
import neteaseMatchScript.apiUtil as apiUtil
import neteaseMatchScript.serviceConsts as serviceConsts
import logout
class MatchPool(baseMatchPool.BaseMatchPool):
	'''
	匹配池
	'''
	def __init__(self, activityData, firstTimeout, againTimeout, groupNumList, sameGroup, matchBySegment,
	             timeoutCb, matchOKCb, tipsCb):
		self.mFirstTimeout = firstTimeout #首次超时时间
		self.mAgainTimeout = againTimeout #再次匹配超时时间
		self.mWaitingPlayers = [] #排队玩家列表
		self.mRoomTotalNum = 0 #一个房间需要的总人数
		self.mCurWaitingNum = 0 #正在排队人数
		self.mGroupNumList = groupNumList #每个阵营需要人数
		self.mUID2True = {} #记录队列中存在玩家
		self.mTimeoutCb = timeoutCb #超时回调函数
		self.mMatchOkCb = matchOKCb #匹配成功回调函数
		self.mBSameGroup = sameGroup #组队报名，队伍是否要求一个阵营
		self.mBMatchBySegment = matchBySegment #是否分段匹配
		self.mActivityData = activityData
		self.mTipsCb = tipsCb
		for num in groupNumList:
			self.mRoomTotalNum += num
		self.mGetMatchingNumFunc = self.GetMatchingNum
		self.mGetWaitingUIDsFunc = self.GetWaitingUIDs

	def SetGetMatchingNumFunc(self, func):
		'''
		设置获取匹配队列长度function
		'''
		self.mGetMatchingNumFunc = func

	def SetGetWaitingUIDsFunc(self, func):
		self.mGetWaitingUIDsFunc = func

	def GetAppliedUIDs(self):
		return self.mUID2True.keys()

	def PlayerLogout(self, uid):
		self.CancelMatching(uid)

	def GetPlayerApplyTime(self, uid):
		if not self.IsInMatching(uid):
			return -1
		matchInfo = self.getMatchInfo(uid)
		if matchInfo:
			return matchInfo.mRealStartTime
		return -1

	def getMatchInfo(self, uid):
		for matchInfo in self.mWaitingPlayers:
			matchUIDs = matchInfo.GetUIDs()
			if uid in matchUIDs:
				return matchInfo
		return None

	def CancelMatching(self, uid):
		for matchInfo in self.mWaitingPlayers:
			matchUIDs = matchInfo.GetUIDs()
			if uid in matchUIDs:
				if matchInfo.mBTeam:
					code = serviceConsts.MatchCodeCancelMatch
					message = serviceConsts.Code2Message[code] % matchInfo.GetNickname(uid)
				else:
					code = serviceConsts.MatchCodeCanceBySelf
					message = serviceConsts.Code2Message[code]
				uiInfo = {
					'code': code,
					'message': message,
					'display_time': 3,
					'activity_id': self.mActivityData['id']
				}
				for one in matchUIDs:
					teamPlayer = playerInfo.TeamPlayerInfo(one, matchInfo)
					self.mTipsCb(teamPlayer, uiInfo)
				self.removeByPlayer(matchInfo)
				return

	def IsInMatching(self, uid):
		return self.mUID2True.get(uid, False)

	def AddNewPlayer(self, matchInfo):
		'''
		队列中新增一个玩家
		'''
		self.mWaitingPlayers.append(matchInfo)
		self.mCurWaitingNum += matchInfo.GetPlayerNum()
		self._addToUID2TRUE(matchInfo)
		self.notifyShowWaitUI(matchInfo)

	def GetMatchingNum(self):
		return len(self.mUID2True)

	def GetWaitingUIDs(self):
		return self.mUID2True.keys()

	def NotifyShowWaitUIByUid(self, uid):
		'''
		告知玩家显示等待匹配ui
		'''
		for matchInfo in self.mWaitingPlayers:
			if uid in matchInfo.GetUIDs():
				eventData = {
					'activity_id': self.mActivityData['id'],
					'start_time': matchInfo.mRealStartTime,
					'name': self.mActivityData['name'],
					'cur_num': self.mGetMatchingNumFunc(),
					'total_num': self.mRoomTotalNum
				}
				apiUtil.NotyfToServerByUID(uid, serviceConsts.ShowWaitUIServiceEvent, eventData)
				return

	def notifyShowWaitUI(self, matchInfo):
		eventData = {
			'activity_id' :self.mActivityData['id'],
			'start_time': matchInfo.mRealStartTime,
			'name' : self.mActivityData['name'],
			'cur_num' : self.mGetMatchingNumFunc(),
			'total_num' : self.mRoomTotalNum
		}
		apiUtil.BroadcastToServer(matchInfo.GetUIDs(), serviceConsts.ShowWaitUIServiceEvent, eventData)

	def notifyMatchNumChange(self):
		'''
		通知匹配人数发生变化
		'''
		eventData = {
			'activity_id': self.mActivityData['id'],
			'cur_num': self.mGetMatchingNumFunc(),
		}
		waitingUIDs = self.mGetWaitingUIDsFunc()
		apiUtil.BroadcastToServer(waitingUIDs, serviceConsts.WaitNumChangedServiceEvent, eventData)

	def _addToUID2TRUE(self, matchInfo):
		uid = matchInfo.mUID
		self.mUID2True[uid] = True
		uids = matchInfo.GetUIDs()
		for one in uids:
			self.mUID2True[one] = True
		self.notifyMatchNumChange()

	def _delToUID2TRUE(self, matchInfo, bNotifyChange = True):
		uid = matchInfo.mUID
		uids = matchInfo.GetUIDs()
		uids.append(uid)
		for one in uids:
			if one in self.mUID2True:
				del self.mUID2True[one]
		if bNotifyChange:
			self.notifyMatchNumChange()

	def AddOldPlayer(self, matchInfo):
		'''
		添加一个player，按照开始匹配时间放到队列中
		'''
		matchInfo.AgainMatch()
		if not self.mWaitingPlayers:
			self.mWaitingPlayers.append(matchInfo)
		else:
			for i, info in enumerate(self.mWaitingPlayers):
				if matchInfo.mRealStartTime < info.mRealStartTime:
					self.mWaitingPlayers.insert(i, matchInfo)
					break
		self.mCurWaitingNum += matchInfo.GetPlayerNum()
		self._addToUID2TRUE(matchInfo)
		self.notifyShowWaitUI(matchInfo)

	def removeByPlayer(self, matchInfo):
		if matchInfo in self.mWaitingPlayers:
			self.mCurWaitingNum -= matchInfo.GetPlayerNum()
			self.mWaitingPlayers.remove(matchInfo)
			self._delToUID2TRUE(matchInfo, False)
		self.notifyMatchNumChange()

	def GetPlayerByUID(self, uid):
		for p in self.mWaitingPlayers:
			if p.mUID == uid:
				return p
		return None

	def removeByRoom(self, roomInfo):
		uids = roomInfo.GetUIDs()
		for uid in uids:
			player = self.GetPlayerByUID(uid)
			self.removeByPlayer(player)

	def Update(self):
		'''
		处理匹配逻辑
		'''
		if not self.mWaitingPlayers:
			return
		retry = 20
		for i in xrange(retry):
			if not self._doMatch():
				break

	def _doMatch(self):
		'''
		执行匹配逻辑。true还可以在队列中再次匹配，否则队列不满足匹配条件了
		'''
		roomInfo = playerInfo.RoomInfo(self.mGroupNumList, self.mBSameGroup, self.mBMatchBySegment)
		for i, matchInfo in enumerate(self.mWaitingPlayers):
			if matchInfo.IsTimeout(self.mFirstTimeout, self.mAgainTimeout):
				self.removeByPlayer(matchInfo)
				self.mTimeoutCb(matchInfo)
				return True
			if self.mCurWaitingNum < self.mRoomTotalNum:
				return False
			if roomInfo.AddPlayer(matchInfo) and roomInfo.IsFull():
				roomInfo.AverageGroup()
				self.removeByRoom(roomInfo)
				self.mMatchOkCb(roomInfo)
				return True
		return False


