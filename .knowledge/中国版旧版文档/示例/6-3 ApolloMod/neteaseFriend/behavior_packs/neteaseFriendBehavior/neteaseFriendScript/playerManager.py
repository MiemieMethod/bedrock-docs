# -*- coding:utf-8 -*-
import friendConsts as friendConsts
import logout
import neteaseFriendScript.friendCommon.friendData as friendData
import neteaseFriendScript.friendCommon.playerData as playerData
import neteaseFriendScript.friendCommon.chatRecordData as chatRecordData
import client.extraClientApi as clientApi
import time


class PlayerManager(object):
	def __init__(self, system):
		import weakref
		self.system = weakref.proxy(system)
		
		#self.mPlayerData = playerData.PlayerData()
		
		self.mPlayerMap = {}
		self.mPlayerQueryTime = {}
		
		self.system.ListenForEvent(friendConsts.ModNameSpace, friendConsts.ServerSystemName, 'UpdatePlayerDataFromServer', self, self.OnUpdatePlayerData)
		
	def getPlayerData(self, uid):
		query_time = self.mPlayerQueryTime.get(uid, None)
		now = int(time.time())
		if query_time and (now - query_time < 600):
			return self.mPlayerMap.get(uid)
		data = self.system.CreateEventData()
		data["id"] = clientApi.GetLocalPlayerId()
		data["uid"] = uid
		
		self.system.NotifyToServer("QueryPlayerDataFromClient", data)
		#先返回一个旧的
		return self.mPlayerMap.get(uid)
	
	def OnUpdatePlayerData(self, args):
		if args is None:
			return
		uid = args.get("uid")
		nickname = args.get("nickname")
		head_image = args.get("head_image")
		temp_playerdata = playerData.PlayerData()
		temp_playerdata.SetPlayerData(uid, nickname, head_image)
		self.mPlayerMap[uid] = temp_playerdata
		self.mPlayerQueryTime[uid] = time.time()
		
		self.system.BroadcastEvent('LocalUpdatePlayerData', {"uid":uid})
		