# -*- coding: utf-8 -*-
import neteaseResidenceScript.util as util
import neteaseResidenceScript.residenceConsts as residenceConsts
import client.extraClientApi as clientApi


class PlayerCreateState(object):
	COMMON = 0  # 常规状态
	CREATINGPARENT = 1  # 创建父领地中状态
	CREATINGSUB = 2  # 创建子领地中状态


class PlayerGac(object):
	"""
	客户端玩家实体封装类
	"""

	def __init__(self, playerId):
		self.mFrame = 0  # 帧计数
		self.mLastSyncFrame = 0  # 上次同步帧计数
		util.ListenServerEvent(residenceConsts.SyncPersonalDataEvent, self, self.OnSyncPersonalData)
		util.ListenEngineEvent('DimensionChangeClientEvent', self, self.OnDimensionChange)
		util.ListenEngineEvent('ClientBlockUseEvent', self, self.OnClientBlockUse)
		util.ListenEngineEvent('ClientItemUseOnEvent', self, self.OnClientItemUseOnEvent)
		# util.ListenEngineEvent('ClientItemUseOnEvent', self, self.OnClientItemUseOn)
		self.mDimensionId = residenceConsts.DimensionIdOverWorld  # 当前所在维度id，默认主世界
		self.mPlayerId = playerId
		self.mUid = None
		# 服务端同步下来的领地信息
		self.mResData = {}  # 领地
		self.mAuthorityData = {}  # 权限
		
		self.mCreatInfo = {}
		self.mCreatInfo["createState"] = PlayerCreateState.COMMON
		self.mCreatInfo["firstPos"] = None
		self.mCreatInfo["parentId"] = 0
		
		self.mClientUseDelay = {}  # entityId:
		
	def LeaveResidence(self, resId):
		if self.mResData.has_key(resId):
			self.mResData.pop(resId)
	
	def IsResidenceOwner(self, topLevelResId):
		return self.mResData.has_key(topLevelResId)

	def FindPlayerAuthority(self, aukey, resId):
		authorityData = self.mAuthorityData.get(resId, None)
		if authorityData is None:
			return None 
		return authorityData.get(aukey, None)
	
	def CheckCanOnUse(self):
		import time
		now = int(time.time())
		lastTime = self.mClientUseDelay.get(self.mPlayerId, 0)
		if now - lastTime <= 1:
			return False
		self.mClientUseDelay[self.mPlayerId] = now
		return True
	
	def OnClientItemUseOnEvent(self, args):
		"""
		使用配置的特定道具，视为开始创建领地（打桩2次）
		"""
		#print "OnClientItemUseOnEvent", args
		blockX = args.get("x")
		blockY = args.get("y")
		blockZ = args.get("z")
		blockPos = (blockX, blockY, blockZ)
		entityId = args.get("entityId")
		residence_baton = util.GetModConfByField("residence_baton")
		lv0_residence_num_limit = util.GetModConfByField("lv0_residence_num_limit")
		sub_num_limit = util.GetModConfByField("sub_num_limit")
		sub_lv_limit = util.GetModConfByField("sub_lv_limit")
		comp = clientApi.CreateComponent(entityId, "Minecraft", "item")
		GetCarriedItem = comp.GetCarriedItem()
		# print "OnClientItemUseOnEvent offhandData", GetCarriedItem
		if GetCarriedItem["itemName"] != residence_baton:
			return
		if self.CheckCanOnUse() == False:
			return
		if self.mCreatInfo["createState"] == PlayerCreateState.COMMON:
			# 常规状态，则是第一个点
			resResult = util.GetResidenceGacMgr().FindResidenceByPos(self.mDimensionId, blockPos)
			if len(resResult) <= 0:  # 不在任何领地内
				if len(self.mResData) < lv0_residence_num_limit:  # 数量没到上限
					self.mCreatInfo["createState"] = PlayerCreateState.CREATINGPARENT
					self.mCreatInfo["firstPos"] = blockPos
					# TODO 提示选择第二个点
					self.ShowTips(self.mPlayerId, "选择的 %s 不在任何领地内，准备创建新领地，该点将 作为领地的第一个对角点，请选择第二个对角点" % str(blockPos))
				else:
					# TODO 提示创建失败，数量到达上限
					self.ShowTips(self.mPlayerId, "选择的 %s 不在任何领地内，但由于领地数量已达上限，无法创建新领地" % str(blockPos))
					self.mCreatInfo["createState"] = PlayerCreateState.COMMON
			else:
				parentRes = resResult[0]
				if parentRes["parentResId"] == 0 and parentRes["id"] not in self.mResData.keys():
					# TODO 提示创建失败，在别人的领地内
					self.ShowTips(self.mPlayerId, "选择的 %s 在其他人的领地内，无法进行任何圈地操作。" % str(blockPos))
					self.mCreatInfo["createState"] = PlayerCreateState.COMMON
				else:  # 在自己的领地
					if (len(resResult) - 1) >= sub_num_limit:
						# TODO 提示创建失败，子领地数量达到上限
						self.ShowTips(self.mPlayerId, "选择的 %s 不在任何领地内，但由于领地数量已达上限，无法创建新领地" % str(blockPos))
						self.mCreatInfo["createState"] = PlayerCreateState.COMMON
					elif parentRes["resLevel"] >= sub_lv_limit:
						# TODO 提示创建失败，子领地层级达到上限
						self.ShowTips(self.mPlayerId, "选择的 %s 在自己的领地内，但该领地的子领地层级已达上限，无法创建子领地" % str(blockPos))
						self.mCreatInfo["createState"] = PlayerCreateState.COMMON
					else:
						self.ShowTips(self.mPlayerId, "选择的 %s 在自己的领地内，准备创建子领地，该点将 作为子领地的第一个对角点，请选择第二个对角点" % str(blockPos))
						self.mCreatInfo["createState"] = PlayerCreateState.CREATINGSUB
						self.mCreatInfo["firstPos"] = blockPos
						self.mCreatInfo["parentId"] = parentRes["id"]
		
		elif self.mCreatInfo["createState"] == PlayerCreateState.CREATINGPARENT:
			# 创建状态，则选择第二个点
			firstPos = self.mCreatInfo["firstPos"]
			secondPos = blockPos
			minPos = (min(firstPos[0], secondPos[0]), min(firstPos[1], secondPos[1]), min(firstPos[2], secondPos[2]))
			maxPos = (max(firstPos[0], secondPos[0]), max(firstPos[1], secondPos[1]), max(firstPos[2], secondPos[2]))
			util.GetClientModSystem().NotifyToServer("CreateParentResidenceFromClient",
			                                         {"minPos": minPos, "maxPos": maxPos,
			                                          "dimension": self.mDimensionId, "playerId": self.mPlayerId,
			                                          "name": str(minPos) + str(maxPos)})
			self.mCreatInfo["createState"] = PlayerCreateState.COMMON
			self.mCreatInfo["firstPos"] = None
			self.mCreatInfo["parentId"] = 0
		else:
			firstPos = self.mCreatInfo["firstPos"]
			secondPos = blockPos
			minPos = (min(firstPos[0], secondPos[0]), min(firstPos[1], secondPos[1]), min(firstPos[2], secondPos[2]))
			maxPos = (max(firstPos[0], secondPos[0]), max(firstPos[1], secondPos[1]), max(firstPos[2], secondPos[2]))
			util.GetClientModSystem().NotifyToServer("CreateSubResidenceFromClient",
			                                         {"minPos": minPos, "maxPos": maxPos,
			                                          "dimension": self.mDimensionId, "playerId": self.mPlayerId,
			                                          "name": str(minPos) + str(maxPos),
			                                          "parentId": self.mCreatInfo["parentId"]})
			self.mCreatInfo["createState"] = PlayerCreateState.COMMON
			self.mCreatInfo["firstPos"] = None
			self.mCreatInfo["parentId"] = 0
	
	def ShowTips(self, entityId, tips):
		"""
		发送提示文本统一入口
		"""
		util.GetClientModSystem().NotifyToServer("ShowCreateTipsFromClient", {"entityId": entityId, "tips": tips})
	
	def OnDimensionChange(self, data):
		"""
		响应事件维护当前玩家所在的维度
		"""
		self.mDimensionId = data["toDimensionId"]
	
	def SetUid(self, uid):
		self.mUid = uid
	
	def SetDimensionId(self, dimensionId):
		self.mDimensionId = dimensionId
	
	def OnSyncPersonalData(self, data):
		"""
		领地数据同步
		"""
		# print 'OnSyncPersonalData', data["resDataList"], data["authorityDataList"]
		for resData in data["resDataList"]:
			resId = resData["resId"]
			self.mResData[resId] = resData
		for authorityData in data["authorityDataList"]:
			resId = authorityData["resId"]
			self.mAuthorityData[resId] = authorityData
		for resId in data["delResidenceList"]:
			if self.mResData.has_key(resId):
				del self.mResData[resId]
		for resId in data["delAuthorityList"]:
			if self.mAuthorityData.has_key(resId):
				del self.mAuthorityData[resId]
	
	def OnClientBlockUse(self, data):
		'''
		处理【不可交互的方块】逻辑，需要客户端服务端两边同时限制
		'''
		print "OnClientBlockUse", data
		playerId = data["playerId"]
		# 不是自己使用就不管了
		if self.mPlayerId != playerId:
			return
		dim = self.mDimensionId
		blockPos = (data['x'], data['y'], data['z'])
		beLimit, notInteractItems = util.GetResidenceGacMgr().GetLimitAndAuthorityByResidence(self, dim, blockPos,
		                                                                                      "cannot_interact_block_list")
		resInfoList = util.GetResidenceGacMgr().FindResidenceByPos(dim, blockPos)
		print "useDoorAuth1", resInfoList
		if not resInfoList:  # 非领地玩家行为不受限
			return
		topLevelResId = resInfoList[-1]["id"]
		playerUid = self.mUid
		#print "useDoorAuth", util.GetResidenceGacMgr().mResAuthority.get(topLevelResId, {}).get(playerUid, {}).get("authority", {})
		if util.GetResidenceGacMgr().mResAuthority.get(topLevelResId, {}).get(playerUid, {}).get("authority", {}).get("UseDoor", False) == True:
			data["cancel"] = False
			return
		# 不受限的玩家
		if beLimit == False:
			return
		# 强制受限的玩家
		if beLimit == True:
			data["cancel"] = True
			return
		# 需要看具体权限的外部玩家
		blockItem = '%s:%s' % (data['blockName'], data['aux'])
		blockItemAll = '%s:%s' % (data['blockName'], "*")
		# print "notInteractItems", notInteractItems
		if blockItem in notInteractItems or blockItemAll in notInteractItems:
			data["cancel"] = True
	
	def OnClientItemUseOn(self, data):
		"""
		处理【限制放置方块】逻辑，需要客户端服务端两边同时限制
		"""
		entityId = data["entityId"]
		# 不是自己使用就不管了
		if self.mPlayerId != entityId:
			return
		dim = self.mDimensionId
		placePos = (data['x'], data['y'], data['z'])
		beLimit, limitItems = util.GetResidenceGacMgr().GetLimitAndAuthorityByResidence(self, dim, placePos,
		                                                                                "place_on_block_items_limit")
		# 不受限的玩家
		if beLimit == False:
			return
		# 强制受限的玩家
		if beLimit == True:
			data["ret"] = True
			return
		# 需要看具体权限的外部玩家
		useItem = '%s:%s' % (data['itemName'], data['auxValue'])
		if useItem not in limitItems:
			data["ret"] = True
	
	def Update(self):
		pass
