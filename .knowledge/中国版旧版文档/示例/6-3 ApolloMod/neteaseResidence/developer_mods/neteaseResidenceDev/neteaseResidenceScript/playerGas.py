# -*- coding: utf-8 -*-
import time
import json
import apolloCommon.commonNetgameApi as commonNetgameApi
import neteaseResidenceScript.util as util
import neteaseResidenceScript.residenceConsts as residenceConsts

class PlayerGas(object):
	"""
	服务端单个玩家封装类
	"""
	def __init__(self, playerId, uid):
		self.mServerType = commonNetgameApi.GetServerType()
		self.mPlayerId = playerId
		self.mUid = uid
		self.mLastSafePos = None
		self.mCanUseSafePosList = []
		self.mResLock = False
		self.mResDataQueryed = False
		self.mClientKnock = False
		self.mFinishedQuery = set()
		self.mResData = {}
		self.mAuthorityData = {}
		#
		self.mDirtyPersonalSet = set()
		self.mSyncedResVersion = {}
		self.mLastHintTime = {}

	# 被领地插件限制的行为提示文字显示冷却时间
	def CheckCanHint(self, aukey):
		now = int(time.time())
		lastTime = self.mLastHintTime.get(aukey, 0)
		if now - lastTime <= 2:
			return False
		self.mLastHintTime[aukey] = now
		return True

	def RegisterResDirty(self, resId):
		self.mDirtyPersonalSet.add(resId)

	# 同步权限信息变化给客户端
	def SyncPersonalDataToClient(self):
		if not self.mClientKnock:
			return
		if not self.mResDataQueryed:
			return
		if not self.mDirtyPersonalSet:
			return
		resDataList = []
		authorityDataList = []
		delResidenceList = []
		delAuthorityList = []
		for resId in self.mDirtyPersonalSet:
			resData = self.mResData.get((self.mServerType, resId), None)
			if resData:
				resDataList.append(resData)
			else:
				delResidenceList.append(resId)
			authorityData = self.mAuthorityData.get(resId, None)
			if authorityData:
				authorityDataList.append(authorityData)
			else:
				delAuthorityList.append(resId)
		util.GetResidenceSystem().SyncPersonalData(self, resDataList, authorityDataList, delResidenceList, delAuthorityList)
		self.mDirtyPersonalSet = set()

	# 尝试获取操作并发锁
	def GetResidenceActionLock(self):
		if not self.mResDataQueryed:
			return False
		if self.mResLock:
			return False
		self.mResLock = True
		return True

	# 释放操作并发锁
	def ReleaseResidenceActionLock(self):
		if not self.mResDataQueryed:
			return False
		if not self.mResLock:
			return False
		self.mResLock = False
		return True

	# 缓存拥有的领地信息
	def CacheResData(self, records):
		self.mResData = {}
		for record in records:
			record = util.UnicodeConvert(record)
			resId, name, serverType, resLevel = record
			data = {
				"serverType": serverType,
				"resId": resId,
				"name": name,
				"resLevel": resLevel,
			}
			self.mResData[(serverType, resId)] = data
			self.mDirtyPersonalSet.add(resId)
		self.mFinishedQuery.add("res")
		if len(self.mFinishedQuery) >= 2:
			self.mResDataQueryed = True

	# 缓存作为外部玩家的领地权限信息
	def CacheAuthorityData(self, records):
		for record in records:
			record = util.UnicodeConvert(record)
			uniqueId, resId, authority = record
			if authority:
				authority = json.loads(authority)
			else:
				authority = {}
			data = {
				"uniqueId": uniqueId,
				"resId": resId,
				"authority": authority,
			}
			self.mAuthorityData[resId] = data
			self.mDirtyPersonalSet.add(resId)
		self.mFinishedQuery.add("authority")
		if len(self.mFinishedQuery) >= 2:
			self.mResDataQueryed = True

	# 领地删除，清理内存中的相关缓存信息
	def CleanOwnerAndAuthorityByDeleteResidence(self, resIdList):
		for resId in resIdList:
			self.RegisterResDirty(resId)
			key = (self.mServerType, resId)
			if self.mResData.has_key(key):
				del self.mResData[key]
			if self.mAuthorityData.has_key(resId):
				del self.mAuthorityData[resId]

	# 成为某个领地所有者
	def JoinResidence(self, resInfo):
		data = {
			"serverType": self.mServerType,
			"resId": resInfo["id"],
			"name": resInfo["name"],
			"resLevel": resInfo["resLevel"],
		}
		self.mResData[(self.mServerType, resInfo["id"])] = data
		self.RegisterResDirty(resInfo["id"])

	# 失去某个领地的所有权
	def LeaveResidence(self, resInfo):
		key = (self.mServerType, resInfo["id"])
		if not self.mResData.has_key(key):
			return
		del self.mResData[key]
		self.RegisterResDirty(resInfo["id"])

	# 判断是否是某个领地的所有者
	def IsResidenceOwner(self, resId):
		if not self.mResDataQueryed:
			return False
		topLevelResId = util.GetResidenceGasMgr().GetTopLevelResidenceIdFromId(resId)
		return self.mResData.has_key((self.mServerType, topLevelResId))

	# 获取基于指定领地的全部权限字典
	def GetAllAuthority(self, resId):
		data = self.mAuthorityData.get(resId, None)
		if not data:
			return None
		return data["authority"]

	# 修改基于指定领地的权限缓存
	def ApplyAuthorityByResId(self, resId, authority):
		data = self.mAuthorityData.get(resId, None)
		if data:
			data["authority"] = authority
		else:
			self.mAuthorityData[resId] = {
				"uniqueId": None,
				"resId": resId,
				"authority": authority,
			}
		self.RegisterResDirty(resId)

	# 删除基于指定领地的权限	
	def DeleteAuthorityByResId(self, resId):
		data = self.mAuthorityData.get(resId, None)
		if data:
			self.mAuthorityData.pop(resId)
			self.RegisterResDirty(resId)
		
	# 获取基于指定领地的指定权限的具体的值
	def FindPlayerAuthority(self, aukey, resId):
		data = self.mAuthorityData.get(resId, None)
		#print "FindPlayerAuthority",data
		if not data:
			return None
		return data["authority"].get(aukey, None)

	# 获取玩家拥有领地的数量
	def GetTopLevelResNumber(self):
		if not self.mResDataQueryed:
			return -1
		num = 0
		for _, data in self.mResData.iteritems():
			if data["resLevel"] == 0:
				num += 1
		return num
	# -------------------------------------------------------------------------------------------
	# 假如玩家正在骑乘坐骑，那么从坐骑中下来
	def CheckAndStopRading(self):
		comp = util.GetResidenceSystem().CreateComponent(self.mPlayerId, "Minecraft", "ride")
		if not comp:
			return
		if comp.IsEntityRiding():
			comp.StopEntityRiding()
			util.GetPlayerMgr().DoShowHintToPlayer(self.mPlayerId, "can_ride")

	# 缓存最近的合法移动地点
	def CacheLastSafePos(self, dim, pos):
		x, y, z = int(pos[0]), int(pos[1])+1, int(pos[2])
		if not self.mLastSafePos or (self.mLastSafePos[0] != x or self.mLastSafePos[1] != y or self.mLastSafePos[2] != z):
			self.mLastSafePos = (dim, x, y, z)
			self.mCanUseSafePosList.insert(0,  (dim, x, y, z))
			if len(self.mCanUseSafePosList) > 50:
				self.mCanUseSafePosList = self.mCanUseSafePosList[:20]
	
	# 获取当前生效的指定权限具体的值（根据具体地点）
	def GetAuthorityWithPlayer(self, aukey, resInfoList):
		for resInfo in resInfoList:
			# 如果玩家独立配置了领地权限
			# 那么玩家自身的权限配置拥有最高的优先级
			ret = self.FindPlayerAuthority(aukey, resInfo["id"])
			#print "GetAuthorityWithPlayer1", ret
			if ret is not None:
				return ret
			# 否则查看子领地权限
			ret = resInfo["authority"].get(aukey, None)
			#print "GetAuthorityWithPlayer2", ret
			if ret is not None:
				return ret
		# 最终保底还是返回mod.json的默认值
		return util.GetModConfByField(aukey)

	# 获取玩家最近移动轨迹记录中，可以合法停留的位置坐标（玩家进入到拒绝外部玩家进入的领地范围内，会被强制传送）
	def FindUsableSafePos(self, dimension):
		print "FindUsableSafePos", self.mCanUseSafePosList
		for dimPos in self.mCanUseSafePosList:
			dim, x, y, z = dimPos
			if dimension != dim:
				continue
			resInfoList = util.GetResidenceSystem().FindResidenceByPos(dim, (x,y,z))
			if not resInfoList:
				print "FindUsableSafePos1"
				return x, y, z
			topLevelResId = resInfoList[-1]["id"]
			if self.IsResidenceOwner(topLevelResId):
				print "FindUsableSafePos2"
				return x, y, z
			# print "FindUsableSafePos", topLevelResId, self.mUid, util.GetResidenceGasMgr().mResAuthority.get(topLevelResId, {}).get(self.mUid, {}).get("authority", {})
			# if util.GetResidenceGasMgr().mResAuthority.get(topLevelResId, {}).get(self.mUid, {}).get("authority", {}).get("Enter", True) == False:
			# 	return None
			canOtherPlayerEnter = self.GetAuthorityWithPlayer("can_other_player_enter", resInfoList)
			
			if canOtherPlayerEnter:
				return x, y, z
		return None

	# 获取当前处于那个领地内
	def CalResidenceIdOfCurPos(self):
		playerPos = util.GetPlayerPos(self.mPlayerId)
		return util.GetResidenceGasMgr().CalResidenceIdByPos(playerPos)

	# 把玩家传送到最近移动轨迹记录中，最近的允许合法停留的位置
	def SyncPlayerToSafePos(self, dim):
		# 如果找不到可以放置的点，就不重新设置了
		safePos = self.FindUsableSafePos(dim)
		if safePos is None:
			print "SyncPlayerToSafePos cannot find safe pos"
			return
		rideComp = util.GetResidenceSystem().CreateComponent(self.mPlayerId, "Minecraft", "ride")
		if rideComp:
			riderId = rideComp.GetEntityRider()
			if riderId != -1:
				rideComp.StopEntityRiding()
				def work():
					riderPosComp = util.GetResidenceSystem().CreateComponent(riderId, "Minecraft", "pos")
					riderPosComp.SetPos(safePos)
				util.GetResidenceSystem().RegisterLaterWork(work)
		posComp = util.GetResidenceSystem().CreateComponent(self.mPlayerId, "Minecraft", "pos")
		posComp.SetPos(safePos)
		util.GetPlayerMgr().DoShowHintToPlayer(self.mPlayerId, "can_other_player_enter")

	# 玩家的逻辑帧，每秒执行一次
	def CheckMove(self):
		self.SyncPersonalDataToClient()
		if self.mPlayerId == residenceConsts.SERVER_PLAYER_PLAYERID:
			return
		dim = util.GetEntityDimensionId(self.mPlayerId)
		pos = util.GetPlayerPos(self.mPlayerId)
		if not pos:
			return
		self.SyncResidenceDataToClient(dim, pos)
		self.RefreshResidence(dim, pos)

	# 同步领地信息给客户端
	def SyncResidenceDataToClient(self, dim, pos):
		viewRange = util.GetModConfByField("residence_view_range")
		minPos = (int(pos[0] - viewRange), int(pos[1]), int(pos[2] - viewRange))
		maxPos = (int(pos[0] + viewRange), int(pos[1]), int(pos[2] + viewRange))
		needSyncList = util.GetResidenceGasMgr().GetDirtyResidenceInfoList(dim, minPos, maxPos, self.mSyncedResVersion)
		if not needSyncList:
			return
		for resInfo in needSyncList:
			self.mSyncedResVersion[resInfo["id"]] = resInfo["version"]
		util.GetResidenceSystem().SyncResidenceData(self, needSyncList)

	# 检查玩家的位置是否合法（是否侵入了不允许进入的领地）
	def RefreshResidence(self, dim=None, pos=None):
		if dim is None:
			dim = util.GetEntityDimensionId(self.mPlayerId)
		if pos is None:
			pos = util.GetPlayerPos(self.mPlayerId)
		if not pos:
			return
		resInfoList = util.GetResidenceGasMgr().FindResidenceByPos(dim, pos)
		# 非领地位置，自由行动
		if not resInfoList:
			self.CacheLastSafePos(dim, pos)
			return
		topLevelResId = resInfoList[-1]["id"]
		if self.IsResidenceOwner(topLevelResId):  # 玩家是领地所有者，行为不受限
			return
		#print "enterAuth", util.GetResidenceGasMgr().mResAuthority.get(topLevelResId, {}).get(self.mUid, {}).get("authority", {}).get("Enter", False)
		if util.GetResidenceGasMgr().mResAuthority.get(topLevelResId, {}).get(self.mUid, {}).get("authority", {}).get("Enter", False) == True:
			return
		#print "enterAuth1", self.GetAuthorityWithPlayer("can_other_player_enter", resInfoList)
		canOtherPlayerEnter = self.GetAuthorityWithPlayer("can_other_player_enter", resInfoList)
		if canOtherPlayerEnter:
			self.CacheLastSafePos(dim, pos)
		else:  # 强制移动出领地
			self.SyncPlayerToSafePos(dim)
		# 检查坐骑
		canRide = self.GetAuthorityWithPlayer("can_ride", resInfoList)
		if not canRide:
			self.CheckAndStopRading()