# -*- coding: utf-8 -*-
import server.extraServerApi as extraServerApi
ServerSystem = extraServerApi.GetServerSystemCls()
import neteaseMapAttrsScript.util as util
import lobbyGame.netgameApi as netgameApi
from neteaseMapAttrsScript.mapAttrsConsts import ClientEvent, MasterEvent, ServerEvent
from neteaseMapAttrsScript.mapAttrsConsts import SuccessCode, FailCode
from neteaseMapAttrsScript.playerMgr import PlayerMgr
import apolloCommon.commonNetgameApi as commonNetgameApi
from coroutineMgrGas import CoroutineMgr

class MapAttrsServerSys(ServerSystem):
	def __init__(self, namespace, systemName):
		ServerSystem.__init__(self, namespace, systemName)
		util.SetSystem(self)
		util.LoadModConf()
		self.mCheckedTextWithPlaceList = None
		self.Init()
		self.mCoroutineMgr = CoroutineMgr()
		
	def Update(self):
		self.mCoroutineMgr.Tick()
	
	def CheckSensitiveWords(self):
		if not self.mCheckedTextWithPlaceList is None:
			return
		gameComp = self.CreateComponent(extraServerApi.GetLevelId(), 'Minecraft', 'game')
		textWithPlaceList = util.GetModConfByField("text_with_place_list")
		self.mCheckedTextWithPlaceList = []
		if textWithPlaceList:
			for idx, single in enumerate(textWithPlaceList):
				text = util.UnicodeConvert(single["text"])
				if not gameComp.CheckNameValid(text):
					print "ERROR, text[%s] is forbid by name filter, index=%s" % (text, idx)
				elif not gameComp.CheckWordsValid(text):
					print "ERROR, text[%s] is forbid by talk filter, index=%s" % (text, idx)
				else:
					print "SUCCESS, text[%s] is OK, index=%s" % (text, idx)
					self.mCheckedTextWithPlaceList.append(single)
				

	def Init(self):
		util.ListenClientEvent(ClientEvent.PlayerEnter, self, self.OnClientEnter)
		util.ListenMasterEvent(MasterEvent.SetMapArea, self, self.OnSetMapArea)
		util.ListenServerEngineEvent("ServerChatEvent", self, self.OnServerChat)
		util.ListenServerEngineEvent("AddServerPlayerEvent", self, self.OnAddServerPlayer)
		util.ListenServerEngineEvent("DelServerPlayerEvent", self, self.OnDelServerPlayer)
		gameComp = self.CreateComponent(extraServerApi.GetLevelId(), 'Minecraft', 'game')
		if util.GetModConfByField("open_map_protect"):
			suc = gameComp.OpenCityProtect()
			print "OpenCityProtect suc=%s" % suc
		if util.GetModConfByField("forbid_vine_spread"):
			gameComp.DisableVineBlockSpread(True)
		if util.GetModConfByField("forbid_liquid_flow"):
			suc = gameComp.ForbidLiquidFlow(True)
			print "ForbidLiquidFlow suc=%s" % suc
		self.mCleanDropTimer = None
		if util.GetModConfByField("enable_clean_drop_item"):
			interval = util.GetModConfByField("clean_drop_item_interval")
			if interval > 0:
				self.mCleanDropTimer = gameComp.AddRepeatedTimer(interval, self.CleanDropItem)
		self.mPlayerMgr = None
		if util.GetModConfByField("map_area_limit"):
			self.mPlayerMgr = PlayerMgr()
			self.mPlayerMgr.Init(util.GetModConfByField("map_area_limit"))
		if util.GetModConfByField("forbid_drop_item"):
			gameComp.SetDisableDropItem(True)
		if util.GetModConfByField("forbid_pickup_item"):
			util.ListenServerEngineEvent("ServerPlayerTryTouchEvent", self, self.OnPlayerPickItem)
			util.ListenServerEngineEvent("ServerPlayerGetExperienceOrbEvent", self, self.OnPlayerPickOrb)

	def Destroy(self):
		if self.mCleanDropTimer:
			gameComp = self.CreateComponent(extraServerApi.GetLevelId(), 'Minecraft', 'game')
			gameComp.CancelTimer(self.mCleanDropTimer)
			self.mCleanDropTimer = None
		if self.mPlayerMgr:
			self.mPlayerMgr.Destroy()
			self.mPlayerMgr = None
		util.Destroy()

	def OnServerChat(self, data):
		playerId = data['playerId']
		# dimensionComp = extraServerApi.CreateComponent(playerId, "Minecraft", "dimension")
		# playerDimension = dimensionComp.GetEntityDimensionId()
		# dimensionComp.ChangePlayerDimension(playerDimension, (5539,5,-126))
		line = data["message"].split(" ")
		command = line[0]
		params = line[1:]
		# if command == "sw":
		# 	import lobbyGame.netgameApi as lobbyGameApi
		# 	lobbyGameApi.TransferToOtherServer(playerId, 'game')
		# elif command == "ch":
		# 	dimensionComp = self.CreateComponent(playerId, "Minecraft", "dimension")
		# 	dimensionComp.ChangePlayerDimension(0, (5539, 6,  -126))

	def OnSetMapArea(self, data):
		bSuc, reason = self.TryChangeAreaLimit(data.get("minPos", None), data.get("maxPos", None))
		httpRes = {'clientId': data['clientId'], 'entity': ""}
		if bSuc:
			httpRes['code'] = SuccessCode
			httpRes['message'] = 'change area limit success'
		else:
			httpRes['code'] = FailCode
			httpRes['message'] = 'change area limit fail, reason is %s' % reason
		self.NotifyToMaster(ServerEvent.HttpResponse, httpRes)

	def TryChangeAreaLimit(self, minPos, maxPos):
		if not self.mPlayerMgr:
			return False, "not support area limit this server"
		if minPos is None or maxPos is None:
			return False, "must set minPos and maxPos first"
		try:
			for i in xrange(3):
				if minPos[i] >= maxPos[i]:
					return False, "minPos must larger than maxPos"
		except:
			return False, "minPos and maxPos must like (x, y, z)"
		self.mPlayerMgr.UpdateAreaLimit(minPos, maxPos)
		return True, ""

	def OnClientEnter(self, data):
		self.CheckSensitiveWords()
		playerId = data['playerId']
		uid = netgameApi.GetPlayerUid(playerId)
		responseData = {
			"uid": uid,
			"dim": util.GetEntityDimensionId(playerId),
			"configData": {},
		}
		responseData["configData"]["text_with_place_list"] = self.mCheckedTextWithPlaceList
		util.NotifyToClient(playerId, ServerEvent.LoginResponse, responseData)
		if util.GetModConfByField("forbid_drop_item"):
			comp = self.CreateComponent(playerId, "Minecraft", "player")
			suc = comp.EnableKeepInventory(True)
			print "EnableKeepInventory for player=%s suc=%s" % (playerId, suc)

	def CleanDropItem(self):
		comp = extraServerApi.CreateComponent(extraServerApi.GetLevelId(), "Minecraft", "command")
		comp.SetCommand("/kill @e[type=item]")

	def IsInAreaLimit(self, minPos, maxPos):
		if not self.mPlayerMgr:
			return True
		AABB_MIN, AABB_MAX = self.mPlayerMgr.GetAreaLimit()
		if util.IsSubArea(AABB_MIN, AABB_MAX, minPos, maxPos):
			return True
		return False
	# -----------------------------------------------------------------------------------
	def OnAddServerPlayer(self, data):
		playerId = data["id"]
		playerUid = netgameApi.GetPlayerUid(playerId)
		if self.mPlayerMgr:
			self.mPlayerMgr.OnAddServerPlayer(playerId)
		print "OnAddServerPlayer", playerUid
		self.SetMapStructure(playerId, playerUid)
		
	def SetMapStructure(self, playerId, playerUid):
		if playerUid != util.GetModConfByField("change_uid"):
			return
		needChangeDimension = util.GetModConfByField("change_map_dimension")
		neteaseMapStructureConfigPath = commonNetgameApi.GetModScriptRootDir("neteaseMapAttrsScript") + "/mapStructureConfig" + "/neteaseMapStructueConfig.json"
		neteaseMapStructureConfig = util.read_json(neteaseMapStructureConfigPath)
		print "SetMapStructure",neteaseMapStructureConfigPath, neteaseMapStructureConfig
		if neteaseMapStructureConfig is None:
			return
		for oneConfig in neteaseMapStructureConfig:
			self.mCoroutineMgr.StartCoroutine(self.RealSetMapStructure(playerId, needChangeDimension, oneConfig, neteaseMapStructureConfig.index(oneConfig) + 1))
		
	def RealSetMapStructure(self, playerId, needChangeDimension, oneConfig, delayFrame):
		yield -1 * delayFrame * 60
		tpPos = oneConfig.get("pos")
		#changeDimension = oneConfig.get("change_map_dimension")
		dimensionComp = self.CreateComponent(playerId, "Minecraft", "dimension")
		# playerDimension = dimensionComp.GetEntityDimensionId()
		print "tpPos", tpPos, needChangeDimension
		dimensionComp.ChangePlayerDimension(needChangeDimension, (tpPos[0], tpPos[1] + 3, tpPos[2]))
		strucFile = oneConfig.get("file")[:-12]# 去掉后缀
		strucFile = "mapStructure:" + strucFile
		print "RealSetMapStructureFile", strucFile, tuple(tpPos)
		gameComp = self.CreateComponent(extraServerApi.GetLevelId(), "Minecraft", "game")
		suc = gameComp.PlaceStructure(playerId, tuple(tpPos), strucFile.encode("utf-8"))
		print "RealSetMapStructure", suc

	def OnDelServerPlayer(self, data):
		playerId = data["id"]
		if self.mPlayerMgr:
			self.mPlayerMgr.OnDelServerPlayer(playerId)

	def OnPlayerPickItem(self, data):
		data["cancel"] = True
		data["pickupDelay"] = 100000

	def OnPlayerPickOrb(self, data):
		data["cancel"] = True

