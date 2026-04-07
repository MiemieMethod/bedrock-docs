# -*- coding: utf-8 -*-
import server.extraServerApi as extraServerApi
import neteaseMapAttrsScript.util as util
from neteaseMapAttrsScript.mapAttrsConsts import DimensionIdOverWorld

AABB_MIN = None
AABB_MAX = None

def UpdateAreaLimit(map_area_limit):
	global AABB_MIN, AABB_MAX
	AABB_MIN, AABB_MAX = map_area_limit[0], map_area_limit[1]

def GetAreaLimit():
	global AABB_MIN, AABB_MAX
	return AABB_MIN, AABB_MAX

def GetLimitAreaCenter():
	global AABB_MIN, AABB_MAX
	return ((AABB_MIN[0]+AABB_MAX[0])/2 , (AABB_MIN[1]+AABB_MAX[1])/2, (AABB_MIN[2]+AABB_MAX[2])/2)

class SinglePlayer(object):
	def __init__(self, playerId):
		super(SinglePlayer, self).__init__()
		self.mPlayerId = playerId
		self.mLastSafePos = None
		self.mCanUseSafePosList = []

	def CacheLastSafePos(self, x, y, z):
		if self.mLastSafePos and self.mLastSafePos[0] == x and self.mLastSafePos[1] == y and self.mLastSafePos[2] == z:
			return
		pos = (x, y, z)
		self.mLastSafePos = pos
		self.mCanUseSafePosList.insert(0, pos)
		if len(self.mCanUseSafePosList) > 30:
			self.mCanUseSafePosList = self.mCanUseSafePosList[:15]

	def FindUsableSafePos(self):
		for pos in self.mCanUseSafePosList:
			if util.IsInArea(pos, AABB_MIN, AABB_MAX):
				return pos
		return GetLimitAreaCenter()

	def SyncToSafePos(self):
		#print "SyncToSafePos", self.mPlayerId
		# 如果找不到可以放置的点，就不重新设置了
		safePos = self.FindUsableSafePos()
		if safePos is None:
			#print "Sync [%s] ToSafePos cannot find safe pos" % self.mPlayerId
			return
		rideComp = extraServerApi.CreateComponent(self.mPlayerId, "Minecraft", "ride")
		if rideComp:
			riderId = rideComp.GetEntityRider()
			if riderId != -1:
				rideComp.StopEntityRiding()
				riderPosComp = extraServerApi.CreateComponent(riderId, "Minecraft", "pos")
				riderPosComp.SetPos(safePos)
		posComp = extraServerApi.CreateComponent(self.mPlayerId, "Minecraft", "pos")
		posComp.SetPos(safePos)

class PlayerMgr(object):
	def __init__(self):
		super(PlayerMgr, self).__init__()
		self.mPlayerMap = {}
		self.mCheckTimer = None

	def Init(self, map_area_limit):
		gameComp = extraServerApi.CreateComponent(extraServerApi.GetLevelId(), 'Minecraft', 'game')
		self.mCheckTimer = gameComp.AddRepeatedTimer(1.0, self.CheckSafePos)
		UpdateAreaLimit(map_area_limit)

	def UpdateAreaLimit(self, minPos, maxPos):
		UpdateAreaLimit((minPos, maxPos))
	
	def GetAreaLimit(self):
		return GetAreaLimit()

	def Destroy(self):
		if self.mCheckTimer:
			gameComp = extraServerApi.CreateComponent(extraServerApi.GetLevelId(), 'Minecraft', 'game')
			gameComp.CancelTimer(self.mCheckTimer)
			self.mCheckTimer = None

	def OnAddServerPlayer(self, playerId):
		self.mPlayerMap[playerId] = SinglePlayer(playerId)

	def OnDelServerPlayer(self, playerId):
		if self.mPlayerMap.has_key(playerId):
			del self.mPlayerMap[playerId]

	def CheckSafePos(self):
		for playerId, obj in self.mPlayerMap.iteritems():
			dim = util.GetEntityDimensionId(playerId)
			if dim != DimensionIdOverWorld:
				continue
			pos = util.GetEntityPos(playerId)
			if not pos:
				continue
			x, y, z = int(pos[0]), int(pos[1]) + 1, int(pos[2])
			if util.IsInArea((x, y, z), AABB_MIN, AABB_MAX):
				obj.CacheLastSafePos(x, y, z)
			else:
				obj.SyncToSafePos()