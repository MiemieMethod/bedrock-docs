# -*- coding: utf-8 -*-
import neteaseResidenceScript.util as util
import  neteaseResidenceScript.residenceConsts as residenceConsts

class ResidenceBaseMgr(object):
	"""
	领地逻辑管理基类
	与服务端保持结构一致
	不过大多数方法在客户端并未使用
	"""
	def __init__(self, system):
		import weakref
		self.mSystem = weakref.proxy(system)
		self.mResidenceGridMap = {}
		self.mResidenceNames = {}
		self.mResidenceChildren = {}
		self.mResidenceMap = {}  # residence id => residence info
	# -----------------------------------------------------------------------------------------------
	def OutputResidenceGridData(self):
		for gridPos, idList in self.mResidenceGridMap.iteritems():
			print "gridPos=%s idList=%s" % (str(gridPos), str(idList))
		for resInfo in self.mResidenceMap.itervalues():
			gridList = residenceConsts.FindChunkByArea(resInfo["dimension"], resInfo["minPos"], resInfo["maxPos"])
			print "resId=%s success gridList=%s" % (resInfo["id"], str(gridList))

	def CheckUniqueResidenceName(self, name):
		"""
		检查领地是否重名
		"""
		if self.mResidenceNames.has_key(name):
			return False
		return True

	def CheckSubResidenceArea(self, parentResInfo, minPos, maxPos, ignoreResId = None):
		"""
		检查某块区域（基于AABB）是否可以创建新的子领地
		"""
		# 子领地范围小于等于父领地
		if not util.IsSubArea(parentResInfo["minPos"], parentResInfo["maxPos"], minPos, maxPos):
			reason = 'CheckSubResidenceArea failed!Is not sub area with parent, parentResidenceID=%s' % parentResInfo["id"]
			return False, reason
		# 同级子领地不能重叠
		resIdList = self.mResidenceChildren.get(parentResInfo["id"], None)
		if resIdList:
			for resId in resIdList:
				if ignoreResId != None and resId == ignoreResId:
					continue
				resInfo = self.mResidenceMap.get(resId, None)
				if not resInfo:
					continue
				if util.AabbIntersects(resInfo['maxPos'], resInfo['minPos'], maxPos, minPos):
					reason = 'CheckSubResidenceArea failed!Intersects with other, ResidenceID=%s' % resId
					return False, reason
		return True, ""
	
	def CheckChangeResidence(self, resId, minPos, maxPos):
		"""
		检查某块区域（基于AABB）是否可以创建新的子领地
		"""
		# 同级子领地不能重叠
		resIdList = self.mResidenceChildren.get(resId, None)
		if resIdList:
			for resId in resIdList:
				resInfo = self.mResidenceMap.get(resId, None)
				if not resInfo:
					continue
				if util.IsOutArea(resInfo['maxPos'], resInfo['minPos'], maxPos, minPos):
					reason = 'CheckSubResidenceArea failed!Intersects with other, ResidenceID=%s' % resId
					return False, reason
		return True, ""
	
	def ServerCheckSubResidenceArea(self, parentResInfo, minPos, maxPos, ignoreResId = None):
		"""
		检查某块区域（基于AABB）是否可以创建新的子领地（server端）
		"""
		# 子领地范围小于等于父领地
		if not util.IsSubArea(parentResInfo["minPos"], parentResInfo["maxPos"], minPos, maxPos):
			reason = 'CheckSubResidenceArea failed!Is not sub area with parent, parentResidenceID=%s' % parentResInfo["id"]
			return False, reason, "当前选中的子领地区域超过了父领地范围，圈地失败"
		# 同级子领地不能重叠
		resIdList = self.mResidenceChildren.get(parentResInfo["id"], None)
		if resIdList:
			for resId in resIdList:
				resInfo = self.mResidenceMap.get(resId, None)
				if ignoreResId != None and resId == ignoreResId:
					continue
				if not resInfo:
					continue
				if util.AabbIntersects(resInfo['maxPos'], resInfo['minPos'], maxPos, minPos):
					reason = 'CheckSubResidenceArea failed!Intersects with other, ResidenceID=%s' % resId
					return False, reason, "当前选中的子领地区域与其他同层级领地有交叉，圈地失败"
		return True, "", ""

	def GetTopLevelResidenceId(self, parentResInfo):
		"""
		返回指定领地的顶层父领地的ID
		"""
		topLevelResId = parentResInfo["id"]
		while True:
			if parentResInfo is None or parentResInfo["resLevel"] == 0:
				break
			topLevelResId = parentResInfo["parentResId"]
			parentResInfo = self.mResidenceMap.get(topLevelResId, None)
		return topLevelResId

	def GetTopLevelResidenceIdFromId(self, resId):
		"""
		返回指定领地的顶层父领地的ID
		"""
		parentResInfo = self.mResidenceMap.get(resId, None)
		if not parentResInfo:
			return resId
		return self.GetTopLevelResidenceId(parentResInfo)

	def GetSubResidenceNumber(self, resId):
		"""
		返回指定ID的领地的子领地数量（包括子领地的子领地）
		"""
		resIdList = self.mResidenceChildren.get(resId, [])
		num = len(resIdList)
		for subResId in resIdList:
			num += self.GetSubResidenceNumber(subResId)
		return num

	def AddResidenceNameAndChild(self, resId, parentResId, name):
		"""
		新增领地，更新领地名的字典与领地对应子领地ID集合的字典，这些数据在内存中维护是为了便于查询定位
		"""
		self.mResidenceNames[name] = resId
		if parentResId <= 0:
			return
		if not self.mResidenceChildren.has_key(parentResId):
			self.mResidenceChildren[parentResId] = set()
		self.mResidenceChildren[parentResId].add(resId)

	def DelResidenceNameAndChild(self, resId, parentResId, name):
		"""
		删除领地，更新领地名的字典与领地对应子领地ID集合的字典，这些数据在内存中维护是为了便于查询定位
		"""
		if self.mResidenceNames.has_key(name):
			del self.mResidenceNames[name]
		if parentResId <= 0:
			return
		if not self.mResidenceChildren.has_key(parentResId):
			return
		self.mResidenceChildren[parentResId].discard(resId)

	def GetDirtyResidenceInfoList(self, dim, minPos, maxPos, syncedResVersion):
		"""
		返回需要同步的领地信息
		"""
		checkedResIds = []
		needSyncList = []
		gridList = residenceConsts.FindChunkByArea(dim, minPos, maxPos)
		for gridPos in gridList:
			propResIds = self.mResidenceGridMap.get(gridPos, None)
			if not propResIds:
				continue
			for resId in propResIds:
				if resId in checkedResIds:
					continue
				checkedResIds.append(resId)
				resInfo = self.mResidenceMap.get(resId, None)
				if not resInfo:
					continue
				syncVersion = syncedResVersion.get(resId, 0)
				if resInfo["version"] > syncVersion:
					needSyncList.append(resInfo)
		return needSyncList

	def CheckTopLevelResidenceArea(self, dim, minPos, maxPos, ignoreResId = None):
		"""
		检查指定区域是否可以创建顶层领地
		"""
		gridList = residenceConsts.FindChunkByArea(dim, minPos, maxPos)
		checkedResIds = []
		if ignoreResId is not None:
			checkedResIds.append(ignoreResId)
		for gridPos in gridList:
			propResIds = self.mResidenceGridMap.get(gridPos, None)
			if not propResIds:
				continue
			for resId in propResIds:
				if resId in checkedResIds:
					continue
				checkedResIds.append(resId)
				resInfo = self.mResidenceMap.get(resId, None)
				if not resInfo:
					continue
				if resInfo["resLevel"] != 0:
					continue
				if util.AabbIntersects(resInfo['maxPos'], resInfo['minPos'], maxPos, minPos):
					reason = 'CheckTopLevelResidenceArea failed! other ResidenceID=%s' % resId
					return False, reason
		return True, ""

	def AddResidenceToGrid(self, resId, dim, minPos, maxPos):
		"""
		新增领地，更新领地区块分割AOI
		"""
		gridList = residenceConsts.FindChunkByArea(dim, minPos, maxPos)
		for gridPos in gridList:
			if not self.mResidenceGridMap.has_key(gridPos):
				self.mResidenceGridMap[gridPos] = set()
			self.mResidenceGridMap[gridPos].add(resId)
			
	def ChangeResidenceToGrid(self, resId, dim, minPos, maxPos, oldMinPos, oldMaxPos):
		"""
		领地区域范围变化，更新领地区块分割AOI
		"""
		gridList = residenceConsts.FindChunkByArea(dim, oldMinPos, oldMaxPos)
		for gridPos in gridList:
			if not self.mResidenceGridMap.has_key(gridPos):
				self.mResidenceGridMap[gridPos] = set()
			self.mResidenceGridMap[gridPos].discard(resId)
		gridList = residenceConsts.FindChunkByArea(dim, minPos, maxPos)
		for gridPos in gridList:
			if not self.mResidenceGridMap.has_key(gridPos):
				self.mResidenceGridMap[gridPos] = set()
			self.mResidenceGridMap[gridPos].add(resId)

	def DelResidenceToGrid(self, resId, dim, minPos, maxPos):
		"""
		删除领地，更新领地区块分割AOI
		"""
		gridList = residenceConsts.FindChunkByArea(dim, minPos, maxPos)
		for gridPos in gridList:
			if not self.mResidenceGridMap.has_key(gridPos):
				continue
			self.mResidenceGridMap[gridPos].discard(resId)

	def FindResidenceByPos(self, dim, pos):
		"""
		返回指定维度坐标所属的领地信息列表，按照领地层级排序，顶层领地在最后
		"""
		propResIds = set()
		if isinstance(pos[0], int) and isinstance(pos[1], int) and isinstance(pos[2], int):
			gridPos = residenceConsts.FindChunkByPos(dim, pos)
			for resId in self.mResidenceGridMap.get(gridPos, []):
				propResIds.add(resId)
		else:
			x, y, z = int(pos[0]), int(pos[1]), int(pos[2])
			for i in (0, 1):
				for j in (0, 1):
					gridPos = residenceConsts.FindChunkByPos(dim, (x+i, y, z+j))
					for resId in self.mResidenceGridMap.get(gridPos, []):
						propResIds.add(resId)
		if not propResIds:
			return []
		result = []
		for resId in propResIds:
			resInfo = self.mResidenceMap.get(resId, None)
			if not resInfo:
				continue
			if util.IsInArea(pos, resInfo['minPos'], resInfo['maxPos']):
				result.append(resInfo)
		result.sort(self.CmpResLv)
		return result

	def CmpResLv(self, a, b):
		return cmp(b["resLevel"], a["resLevel"])

	def IsInResidence(self, pos, residenceId):
		"""
		返回指定坐标是否在指定领地中
		"""
		resInfo = self.mResidenceMap.get(residenceId, None)
		if resInfo is None:
			print 'IsInResidence warning! no such residence.id:%s', residenceId
			return False
		return util.IsInArea(pos, resInfo['minPos'], resInfo['maxPos'])

	def FindResidenceById(self, resId):
		"""
		返回指定ID领地的信息
		"""
		return self.mResidenceMap.get(resId, None)
	# ------------------------------------------------------------------------------------------------
	def GetAllAuthorityByResidence(self, resId):
		"""
		返回指定ID领地的权限配置
		"""
		resInfo = self.mResidenceMap.get(resId, None)
		if not resInfo:
			return None
		return resInfo["authority"]

	def GetAllAuthorityByUid(self, uid, resId):
		"""
		返回指定uid的玩家在指定ID领地的特殊权限配置
		"""
		player = util.GetResidenceSystem().GetPlayerMgr().GetPlayerByUid(uid)
		if not player:
			return None
		return player.GetAllAuthority(resId)

	def GetAllAuthorityByEntityId(self, playerId, resId):
		"""
		返回指定entityId的玩家在指定ID领地的特殊权限配置
		"""
		player = util.GetResidenceSystem().GetPlayerMgr().GetPlayerById(playerId)
		if not player:
			return None
		return player.GetAllAuthority(resId)
	# -------------------------------------------------------------------------------------------
	def FindAuthority(self, aukey, dim, pos, playerId=None):
		"""
		返回指定entityId的玩家在指定维度坐标的指定权限的值（按照优先级）
		"""
		usePlayer = residenceConsts.AuthorityForPlayer.get(aukey, False)
		if usePlayer:
			player = util.GetResidenceSystem().GetPlayerMgr().GetPlayerById(playerId)
			if player:
				return self.FindAuthorityByPlayer(aukey, dim, pos, player)
			else:
				return self.FindAuthorityByPos(aukey, dim, pos)
		else:
			return self.FindAuthorityByPos(aukey, dim, pos)

	def FindAuthorityByPos(self, aukey, dim, pos):
		"""
		返回指定维度坐标的指定权限的值（按照优先级）
		"""
		# 定位坐标所在的领地
		resInfoList = self.FindResidenceByPos(dim, pos)
		# 不属于任何领地，返回mod.json的默认值
		if not resInfoList:
			return -1, util.GetModConfByField(aukey)
		# 从最小的子领地开始
		recentResId = None
		for resInfo in resInfoList:
			recentResId = resInfo["id"]
			ret = resInfo["authority"].get(aukey, None)
			if not ret is None:
				return recentResId, ret
		# 最终保底还是返回mod.json的默认值
		return recentResId, util.GetModConfByField(aukey)

	def FindAuthorityByPlayer(self, aukey, dim, pos, player):
		"""
		返回指定玩家在指定维度坐标的指定权限的值（按照优先级）
		"""
		# 定位坐标所在的领地
		resInfoList = self.FindResidenceByPos(dim, pos)
		# 不属于任何领地，返回mod.json的默认值
		if not resInfoList:
			return -1, util.GetModConfByField(aukey)
		# 从最小的子领地开始
		recentResId = None
		for resInfo in resInfoList:
			recentResId = resInfo["id"]
			# 如果玩家独立配置了领地权限
			# 那么玩家自身的权限配置拥有最高的优先级
			ret = player.FindPlayerAuthority(aukey, recentResId)
			if not ret is None:
				return recentResId, ret
			# 否则查看子领地权限
			ret = resInfo["authority"].get(aukey, None)
			if not ret is None:
				return recentResId, ret
		# 最终保底还是返回mod.json的默认值
		return recentResId, util.GetModConfByField(aukey)
	# -----------------------------------------------------------------------------------------------
	def AddOneResidence(self, resInfo):
		"""
		新增一个领地，更新各种内存缓存
		"""
		_id = resInfo['id']
		self.mResidenceMap[_id] = resInfo
		self.AddResidenceToGrid(_id, resInfo["dimension"], resInfo["minPos"], resInfo["maxPos"])
		self.AddResidenceNameAndChild(_id, resInfo["parentResId"], resInfo["name"])
		
	def ChangeOneResidence(self, resInfo, oldMinPos, oldMaxPos):
		"""
		修改一个领地的占据区域，更新各种内存缓存
		"""
		_id = resInfo['id']
		self.mResidenceMap[_id] = resInfo
		self.ChangeResidenceToGrid(_id, resInfo["dimension"], resInfo["minPos"], resInfo["maxPos"], oldMinPos, oldMaxPos)
		self.AddResidenceNameAndChild(_id, resInfo["parentResId"], resInfo["name"])
		
	def DelResidenceByResidenceId(self, resId):
		"""
		删除一个领地，更新各种内存缓存
		"""
		resInfo = self.mResidenceMap.get(resId, None)
		if not resInfo:
			return None
		del self.mResidenceMap[resId]
		self.DelResidenceToGrid(resId, resInfo["dimension"], resInfo["minPos"], resInfo["maxPos"])
		self.DelResidenceNameAndChild(resId, resInfo["parentResId"], resInfo["name"])
		return resInfo

	def FindAllSubResidenceList(self, resId, result):
		"""
		返回一个领地的全部子领地，结果存储到参数result中
		"""
		resIdList = self.mResidenceChildren.get(resId, [])
		for subResId in resIdList:
			result.add(subResId)
			self.FindAllSubResidenceList(subResId, result)
