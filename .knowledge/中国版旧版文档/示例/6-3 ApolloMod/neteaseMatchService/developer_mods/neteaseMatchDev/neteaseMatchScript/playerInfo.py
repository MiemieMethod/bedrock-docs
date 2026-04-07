# -*- coding: utf-8 -*-
import time
gUIUniqueId = 0
def genUniqueId():
	global gUIUniqueId
	ret = gUIUniqueId
	gUIUniqueId += 1
	return ret

class MemberPlayerInfo(object):
	def __init__(self, uid, nickname, matchVal = 1):
		self.mUID = uid
		self.mNickname = nickname
		self.mMatchVal = matchVal

class MatchPlayerInfo(object):
	'''
	匹配玩家信息
	'''
	def __init__(self, uid, nickname, isTeam, chooseGroup, matchVal = 1, members = []):
		self.mUID = uid
		self.mNickname = nickname
		self.mMatchValue = matchVal
		self.mStartMatchTime = int(time.time())
		self.mRealStartTime = self.mStartMatchTime
		if uid in members:
			members.remove(uid)
		self.mGroupMembers = members
		self.mFristMatch = True
		self.mBTeam = isTeam
		self.mChooseGroupId = chooseGroup

	def GetUIDs(self):
		uids = [self.mUID]
		for m in self.mGroupMembers:
			uids.append(m.mUID)
		return uids

	def GetNickname(self, uid):
		if uid == self.mUID:
			return self.mNickname
		for info in self.mGroupMembers:
			if info.mUID == uid:
				return info.mNickname
		return ''

	def AgainMatch(self):
		'''
		超时后继续报名
		'''
		self.mFristMatch = False
		self.mStartMatchTime = int(time.time())

	def GetPlayerNum(self):
		return 1 + len(self.mGroupMembers)

	def GetTotalMatchVal(self):
		total = self.mMatchValue
		for m in self.mGroupMembers:
			total += m.mMatchVal
		return total

	def IsTimeout(self, firstTimeout, againTimeout):
		cur = int(time.time())
		if self.mFristMatch:
			return cur > self.mStartMatchTime + firstTimeout
		else:
			return cur > self.mStartMatchTime + againTimeout

class TeamPlayerInfo(MatchPlayerInfo):
	'''
	队伍中某个玩家匹配信息
	'''
	def __init__(self, uid, matchInfo):
		MatchPlayerInfo.__init__(self, uid, "", matchInfo.mBTeam, matchInfo.mChooseGroupId)
		self.mTeamMatchInfo = matchInfo
		for member in matchInfo.mGroupMembers:
			if member.mUID == uid:
				self.mNickname = member.mNickname
				self.mMatchValue = member.mMatchVal

class GroupInfo(object):
	'''
	一个阵营信息
	'''
	def __init__(self, id, num):
		self.mGroupId = id
		self.mTotalNum = num
		self.mCurNum = 0
		self.mWaitingPlayerList = []
		self.mTotalMatchVal = 0

	def IsFull(self):
		return self.mCurNum == self.mTotalNum

	def GetAverageVal(self):
		if 0 == self.mCurNum:
			return 0
		return self.mTotalMatchVal * 1.0 / self.mCurNum

	def GetRemainNum(self):
		return self.mTotalNum - self.mCurNum

	def AddPlayer(self, matchInfo):
		if matchInfo.mChooseGroupId >= 0 and matchInfo.mChooseGroupId != self.mGroupId:
			return False
		num = matchInfo.GetPlayerNum()
		if self.mCurNum + num <= self.mTotalNum:
			self.mWaitingPlayerList.append(matchInfo)
			self.mCurNum += num
			self.mTotalMatchVal += matchInfo.GetTotalMatchVal()
			return True
		return False

	def removePlayer(self, matchInfo):
		self.mCurNum -= matchInfo.GetPlayerNum()
		self.mWaitingPlayerList.remove(matchInfo)
		self.mTotalMatchVal -= matchInfo.GetTotalMatchVal()

	def PopAllSinglePlayer(self):
		'''
		注意：若选定了阵营，则不要pop出来
		'''
		singlePlayers = []
		for i, matchInfo in enumerate(self.mWaitingPlayerList):
			if matchInfo.mChooseGroupId < 0 and 1 == matchInfo.GetPlayerNum():
				singlePlayers.append(matchInfo)
		for p in singlePlayers:
			self.removePlayer(p)
		return singlePlayers

	def GetUIDs(self):
		uids = []
		for p in self.mWaitingPlayerList:
			uids.extend(p.GetUIDs())
		return uids

class RoomConfirmInfo(object):
	'''
	匹配确认信息
	'''
	TIMEOUT_SECONDS = 10
	def __init__(self, room):
		self.mRoomInfo = room
		self.mNeedConfrimUIDs = room.GetUIDs()
		self.mLogoutUIDs = []
		self.mStartTime = int(time.time())
		self.mId = genUniqueId()

	def Logout(self, uid):
		self.Check(uid)
		if uid not in self.mLogoutUIDs:
			self.mLogoutUIDs.append(uid)

	def IsChecked(self):
		return not self.mNeedConfrimUIDs

	def IsNeedCheck(self, uid):
		return uid in self.mNeedConfrimUIDs

	def Check(self, uid):
		if uid in self.mNeedConfrimUIDs:
			self.mNeedConfrimUIDs.remove(uid)

	def IsTimeout(self):
		cur = int(time.time())
		return cur > self.mStartTime + RoomConfirmInfo.TIMEOUT_SECONDS

class RoomInfo(object):
	'''
	匹配结果信息
	'''
	def __init__(self, groupNumList, sameGroup, matchBySegment):
		self.mSameGroup = sameGroup
		self.mMatchBySegment = matchBySegment
		self.mWaitingSinglePlayers = []
		self.mGroupList = []
		self.mTotalNum = 0
		self.mCurNum = 0
		for idx, num in enumerate(groupNumList):
			group = GroupInfo(idx, num)
			self.mTotalNum += num
			self.mGroupList.append(group)

	def GetGroupUIDs(self):
		uids = []
		for g in self.mGroupList:
			uids.append(g.GetUIDs())
		return uids

	def IsFull(self):
		return self.mTotalNum == self.mCurNum

	def GetUIDs(self):
		uids = []
		for g in self.mGroupList:
			uids.extend(g.GetUIDs())
		return uids

	def AddPlayer(self, matchInfo):
		'''
		return：True表示需要继续添加玩家，False表示房间已满，匹配成功了
		'''
		if self.mSameGroup:
			return self._addTeamToSameGroup(matchInfo)
		return self._addTeamToGroup(matchInfo)

	def _addTeamToSameGroup(self, matchInfo):
		'''
		组队的队伍分配到同一个阵营
		匹配算法：使用最简单算法，依次向每个阵营塞人，直到塞满为止
		'''
		for group in self.mGroupList:
			if group.AddPlayer(matchInfo):
				self.mCurNum += matchInfo.GetPlayerNum()
				return True
		return False

	def _addTeamToGroup(self, matchInfo):
		'''
		组队的队伍可以分配到不同阵营
		匹配算法：使用最简单算法，依次向每个阵营塞，直到塞满为止
		'''
		num = matchInfo.GetPlayerNum()
		if self.mCurNum + num <= self.mTotalNum:
			if matchInfo.mChooseGroupId >= 0:
				group = self.mGroupList[matchInfo.mChooseGroupId]
				if group.AddPlayer(matchInfo):
					self.mCurNum += num
					return True
			else:
				self._addToSinglePlayer(matchInfo)
				self.mCurNum += num
				return True
		return False

	def _addToSinglePlayer(self, matchInfo):
		teamPlayer = TeamPlayerInfo(matchInfo.mUID, matchInfo)
		self.mWaitingSinglePlayers.append(teamPlayer)
		for player in matchInfo.mGroupMembers:
			uid = player.mUID
			teamPlayer = TeamPlayerInfo(uid, matchInfo)
			self.mWaitingSinglePlayers.append(teamPlayer)

	def AverageGroup(self):
		if not self.mMatchBySegment:
			self._fillGroup()
		else:
			self._averageGroupVal()

	def _averageGroupVal(self):
		'''
		让每个阵营匹配值接近
		算法：1：先从mWaitingSinglePlayers中取出匹配中值，塞入阵营中，让阵营剩余人数一样
			2：从mWaitingSinglePlayers取出最大匹配值，塞入匹配值最小的阵营
		'''
		for group in self.mGroupList:
			singleList = group.PopAllSinglePlayer()
			self.mWaitingSinglePlayers.extend(singleList)
		def cmpPlayer(x, y):
			return x.mMatchValue - y.mMatchValue
		self.mWaitingSinglePlayers = sorted(self.mWaitingSinglePlayers, cmp = cmpPlayer)
		self._doGroupRemainNumToSame()
		self._doAverageGroup()

	def _fillGroup(self):
		'''
		把每个阵营填充满
		'''
		for group in self.mGroupList:
			while not group.IsFull() and self.mWaitingSinglePlayers:
				matchInfo = self.mWaitingSinglePlayers.pop()
				group.AddPlayer(matchInfo)

	def _doGroupRemainNumToSame(self):
		idx = self._getMaxRemainGroupIdx()
		while idx != -1:
			num = len(self.mWaitingSinglePlayers)
			middle = num / 2
			player = self.mWaitingSinglePlayers[middle]
			group = self.mGroupList[idx]
			group.AddPlayer(player)
			self.mWaitingSinglePlayers.remove(player)
			idx = self._getMaxRemainGroupIdx()

	def _getMaxRemainGroupIdx(self):
		lst = self._getGroupRemainNum()
		idx = 0
		maxV = lst[0]
		bSame = True
		for i in xrange(1, len(lst)):
			if lst[i] != maxV:
				bSame = False
			if lst[i] > maxV:
				idx = i
		if bSame:
			return -1
		return idx

	def _getGroupRemainNum(self):
		num = []
		for group in self.mGroupList:
			num.append(group.GetRemainNum())
		return num

	def _doAverageGroup(self):
		while self.mWaitingSinglePlayers:
			groupAveVal = []
			for idx, group in enumerate(self.mGroupList):
				groupAveVal.append((idx, group.GetAverageVal()))
			def cmpVal(ele):
				return ele[1]
			groupAveVal.sort(key = cmpVal)
			playerIdx = 0
			for idx, v in groupAveVal:
				self.mGroupList[idx].AddPlayer(self.mWaitingSinglePlayers[playerIdx])
				playerIdx += 1
			self.mWaitingSinglePlayers = self.mWaitingSinglePlayers[playerIdx:]

class MatchTimeoutPlayerInfo(object):
	'''
	超时玩家信息
	'''
	TIMEOUT_SECONDS = 10
	def __init__(self, matchPlayerInfo):
		self.mMatchPlayerInfo = matchPlayerInfo
		self.mStartTime = int(time.time())

	def IsTimeout(self):
		cur = int(time.time())
		return cur > self.mStartTime + MatchTimeoutPlayerInfo.TIMEOUT_SECONDS

class PlayerUITips(object):
	'''
	玩家ui提示信息。
	'''
	TIMEOUT_SECONDS = 86400
	def __init__(self, matchPlayerInfo, tips):
		self.mMatchPlayerInfo = matchPlayerInfo
		self.mId = genUniqueId()
		tips['ui_id'] = self.mId
		self.mTipsInfo = tips
		self.mStartTime = int(time.time())

	def IsTimeout(self):
		cur = int(time.time())
		return cur > self.mStartTime + PlayerUITips.TIMEOUT_SECONDS