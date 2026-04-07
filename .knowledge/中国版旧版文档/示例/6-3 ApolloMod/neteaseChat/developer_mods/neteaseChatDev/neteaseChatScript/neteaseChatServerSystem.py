# -*- coding:utf-8 -*-
import server.extraServerApi as serverApi
ServerSystem = serverApi.GetServerSystemCls()
import neteaseChatScript.chatManager as chatManager
import apolloCommon.mysqlPool as mysqlPool
import logout
import lobbyGame.netgameApi as netgameApi
import netgame.apolloCommon.commonNetgameApi as commonNetgameApi
import chatConsts
import re, time
import lobbyGame.netgameApi as lobbyGameApi

class ChatServerSystem(ServerSystem):
	def __init__(self, namespace, systemName):
		ServerSystem.__init__(self, namespace, systemName)
		logout.info(namespace, systemName, "====init====")
		lobbyGameApi.SetLevelGameType(1)
		self.mChatManagers = {}
		#self.mChatManager = chatManager.ChatManager(self)
		self.Init()
		self.InitMysqlDb()
		self.ListenForEvent(serverApi.GetEngineNamespace(), serverApi.GetEngineSystemName(), 'ServerChatEvent', self, self.OnServerChatEvent)
		self.ListenForEvent(chatConsts.ModNameSpace, chatConsts.ClientSystemName, 'ClientUiInitFinished', self, self.OnClientUiInitFinished)
		self.ListenForEvent(chatConsts.ModNameSpace, chatConsts.ServiceSystemName, 'newChatFromServiceEvent', self, self.OnNewChatFromServiceEvent)
		self.ListenForEvent(chatConsts.ModNameSpace, chatConsts.ClientSystemName, 'PlayerChatFromClientEvent', self, self.OnPlayerChatFromClientEvent)
		self.ListenForEvent(chatConsts.ModNameSpace, chatConsts.ClientSystemName, 'JoinTeamFromClientEvent', self, self.OnJoinTeamFromClientEvent)
		self.ListenForEvent(chatConsts.ModNameSpace, chatConsts.ClientSystemName, 'TempChatFromClientEvent', self, self.OnTempChatFromClient)
		self.ListenForEvent(chatConsts.ModNameSpace, chatConsts.ClientSystemName, 'AddBlackFromClientEvent', self, self.OnAddBlackFromClientEvent)
		self.ListenForEvent(chatConsts.ModNameSpace, chatConsts.ClientSystemName, 'AddFriendFromClientEvent', self, self.OnAddFriendFromClientEvent)

	def Init(self):
		self.modConfig = commonNetgameApi.GetModJsonConfig('neteaseChatScript')
		self.mServerid = netgameApi.GetServerId()
		self.mChatManagers[self.mServerid] = chatManager.ChatManager(self, self.mServerid)
		self.mChatManagers[chatConsts.ALL_SERVER_CHANNEL] = chatManager.ChatManager(self, chatConsts.ALL_SERVER_CHANNEL)
		self.mChatIntervalCD = {
			self.mServerid: self.modConfig['localeCD'],
			chatConsts.ALL_SERVER_CHANNEL: self.modConfig['worldCD']
		}
		self.mChatCD = {
			self.mServerid: {},
			chatConsts.ALL_SERVER_CHANNEL: {}
		}

	def OnServerChatEvent(self, args):
		playerId = args.get("playerId")
		if args["message"] == "1":
			self.NotifyToClient(playerId, "OpenChatList", {})
		
	def OnClientUiInitFinished(self, args):
		playerId = args.get("entityId")
		playerUid = netgameApi.GetPlayerUid(playerId)
		nickName = lobbyGameApi.GetPlayerNickname(playerId)
		self.NotifyToClient(playerId, "ModConfigResponseFromServerEvent", self.modConfig)
		self.NotifyToClient(playerId, "TellYourPlayerUidAndSidEvent", {"playerId":playerId, "playerUid":playerUid, "nickName":nickName, "serverid":self.mServerid, 'exBtnList': self.modConfig.get('exBtnList')})
		# for key, chatManager in self.mChatManagers.iteritems():
		# 	chatManager.QueryScreenUid(playerId, playerUid)
			
	def OnPlayerChatFromClientEvent(self, args):
		chatChannel = args.get("chatChannel")
		message = args.get("message")
		if not (message and isinstance(message, str)):
			return
		gcomp = serverApi.CreateComponent(serverApi.GetLevelId(), "Minecraft", "game")
		if not gcomp.CheckWordsValid(message):
			print '屏蔽字'
			alertSystem = serverApi.GetSystem("neteaseAlert", "neteaseAlertDev")
			if alertSystem:
				alertSystem.Alert(args['playerId'], '§c内容包含屏蔽字。', 2, 0.5, 0.5)
			return
		playerId = args.get("playerId")
		playerUid = lobbyGameApi.GetPlayerUid(playerId)

		if chatChannel not in self.mChatCD:
			return
		now = time.time()
		if now - self.mChatCD[chatChannel].get(playerUid, 0.0) < self.mChatIntervalCD[chatChannel]:
			alertSystem = serverApi.GetSystem("neteaseAlert", "neteaseAlertDev")
			if alertSystem:
				alertSystem.Alert(args['playerId'], '§e发言过快，请稍事休息。', 2, 0.5, 0.5)
			return
		self.mChatCD[chatChannel][playerUid] = now

		nickname = lobbyGameApi.GetPlayerNickname(playerId)
		#获取等级
		levelComp = serverApi.CreateComponent(playerId, "Minecraft", "lv")
		playerLevel = levelComp.GetPlayerLevel()
		print "OnPlayerChatFromClientEvent", args
		res = re.search(chatConsts.BAG_ITEM_REGREX, message.rstrip())
		if res is not None:
			chatType = chatConsts.ChatType.Item
			slotPos = int(res.groups()[0])
			if slotPos not in xrange(36):
				alertSystem = serverApi.GetSystem("neteaseAlert", "neteaseAlertDev")
				if alertSystem:
					alertSystem.Alert(args['playerId'], '§c不存在的背包格子。', 2, 0.5, 0.5)
				return
			itemComp = serverApi.CreateComponent(playerId, 'Minecraft', 'item')
			itemDict = itemComp.GetPlayerItem(serverApi.GetMinecraftEnum().ItemPosType.INVENTORY, slotPos, True)
			print "OnPlayerChatFromClientEvent", slotPos, itemDict
			if itemDict is None:
				alertSystem = serverApi.GetSystem("neteaseAlert", "neteaseAlertDev")
				if alertSystem:
					alertSystem.Alert(args['playerId'], '§c所选槽位没有物品，无法发送超链接。', 2, 0.5, 0.5)
				return
			chatDict = {"chatChannel":chatChannel, "playerUid":playerUid,"nickName":nickname,"playerLevel":playerLevel,"chatType":chatType,"infoDict":itemDict,"mes":message}
			self.RequestToService(chatConsts.ModNameSpace, "ChatFromServerEvent", chatDict)
		elif re.match(chatConsts.TEAM_REGREX, message) is not None:
			print "OnPlayerChatFromClientEvent", chatConsts.TEAM_REGREX
			chatType = chatConsts.ChatType.Team
			chatDict = {"chatChannel": chatChannel, "playerUid": playerUid, "nickName": nickname,
			            "playerLevel": playerLevel, "chatType": chatType, "infoDict": {}, "mes": message}
			self.RequestToService(chatConsts.ModNameSpace, "ChatFromServerEvent", chatDict)
			# def CheckPlayerSquadCb(success, data):
			# 	if not success or data["code"] != 1 or not data['entity'].get('squad'):
			# 		#TODO 查找队伍失败
			# 		return
			# 	else:
			# 		self.RequestToService(chatConsts.ModNameSpace, "ChatFromServerEvent", chatDict)
			# chatConsts.CheckPlayerSquad(playerUid, CheckPlayerSquadCb)
		else:
			print "OnPlayerChatFromClientEvent Common"
			chatType = chatConsts.ChatType.Common
			chatDict = {"chatChannel": chatChannel, "playerUid": playerUid, "nickName": nickname,
			            "playerLevel": playerLevel, "chatType": chatType, "mes":message}
			self.RequestToService(chatConsts.ModNameSpace, "ChatFromServerEvent", chatDict)
			
	def OutPlayerChat(self, args):
		chatType = args.get("chatType", chatConsts.ChatType.Common)
		chatChannel = args.get("chatChannel", chatConsts.ALL_SERVER_CHANNEL)
		playerUid = args.get("playerUid", 0)
		nickname = args.get("nickName", "")
		playerLevel = args.get("playerLevel", 0)
		message = args.get("message", "")
		infoDict = args.get("infoDict", {})
		chatDict = {"chatChannel": chatChannel, "playerUid": playerUid, "nickName": nickname,
		            "playerLevel": playerLevel, "chatType": chatType, "infoDict": infoDict, "mes": message}
		self.RequestToService(chatConsts.ModNameSpace, "ChatFromServerEvent", chatDict)

	def OnTempChatFromClient(self, data):
		friendUid = data['friendUid']
		uid = lobbyGameApi.GetPlayerUid(data['entityId'])
		if uid:
			import server.extraServerApi as serverApi
			fri = serverApi.GetSystem("neteaseFriend", "neteaseFriendDev")
			if fri:
				fri.CreateTempChat({
					"selfUid": uid,
					"friendUid": friendUid
				})
				
	def OnAddFriendFromClientEvent(self, data):
		friendUid = data['friendUid']
		uid = lobbyGameApi.GetPlayerUid(data['entityId'])
		if uid:
			import server.extraServerApi as serverApi
			fri = serverApi.GetSystem("neteaseFriend", "neteaseFriendDev")
			if fri:
				fri.ServerAddFriend(data)
				
	def OnAddBlackFromClientEvent(self, data):
		friendUid = data['friendUid']
		uid = lobbyGameApi.GetPlayerUid(data['entityId'])
		if uid:
			import server.extraServerApi as serverApi
			fri = serverApi.GetSystem("neteaseFriend", "neteaseFriendDev")
			if fri:
				fri.ServerAddBlack(data)

	def OnJoinTeamFromClientEvent(self, args):
		teamLeaderUid = args["teamLeaderUid"]
		joinTeamPlayerId = args["joinTeamPlayerId"]
		print "OnJoinTeamFromClientEvent", args
		joinTeamPlayerUid = lobbyGameApi.GetPlayerUid(joinTeamPlayerId)
		def CheckPlayerSquadCb(success, data):
			if not success:
				print('请求超时')
				print('返回数据为 data: {}'.format(data))
			else:
				if data['code'] == 1:
					print('请求成功')
					squad = data['entity'].get('squad')
					if not squad:
						# print('uid为{}的玩家暂未组队'.format(data['entity']['uid']))

						alertSystem = serverApi.GetSystem("neteaseAlert", "neteaseAlertDev")
						if alertSystem:
							alertSystem.Alert(joinTeamPlayerId, '§e队伍不存在。', 2, 0.5, 0.5)
					else:
						# print('队伍数字编号 order: {}'.format(squad['order']))
						# print('队长uid chief: {}'.format(squad['chief']))
						# print('队伍招募信息 label: {}'.format(squad.get('label')))
						# print('队伍成员信息 members: {}'.format(squad['members']))

						alertSystem = serverApi.GetSystem("neteaseAlert", "neteaseAlertDev")
						if 'recruiting' not in data['entity']:
							if alertSystem:
								alertSystem.Alert(joinTeamPlayerId, '§e当前队伍未在招募队员。', 2, 0.5, 0.5)
						else:
							if alertSystem:
								alertSystem.Alert(joinTeamPlayerId, '§a已发送申请。', 2, 0.5, 0.5)
							chatConsts.OnSquadRecruitmentApply({'playerId':joinTeamPlayerId, 'order': squad['order']})
				else:
					print('请求失败')
					print('失败信息为 message: {}'.format(data['message']))

		chatConsts.CheckPlayerSquad(teamLeaderUid, CheckPlayerSquadCb)
	
		
	def OnNewChatFromServiceEvent(self, chatDict):
		print "OnNewChatFromServiceEvent", chatDict
		chatChannel = chatDict["chatChannel"]
		if self.mChatManagers.has_key(chatChannel):
			self.mChatManagers[chatChannel].InsertChatMes(chatDict)
			
	def InitMysqlDb(self):
		# 创建Mysql线程池，这里封装了Mysql的连接建立，多线程执行的功能
		try:
			mysqlPool.InitDB(20)
		except:
			logout.error("start_Friend fail when init mysql")
			return False
		return True
		
		



		
		
	