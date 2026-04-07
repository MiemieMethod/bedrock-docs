# -*- coding: utf-8 -*-
import server.extraServerApi as serverApi
ServerSystem = serverApi.GetServerSystemCls()
import neteaseMatchScript.serverConsts as serverConsts
import apolloCommon.commonNetgameApi as commonNetgameApi
import lobbyGame.netgameApi as lobbyGameApi

class MatchServerSystem(ServerSystem):
	def __init__(self, namespace, systemName):
		ServerSystem.__init__(self, namespace, systemName)
		self.ListenEvents()
		self.mActivityMap = {} #activity id---> activity data
		self.mUID2Id = {} #player uid --> player id
		self.Init()

	def Init(self):
		self.mModJsonData = commonNetgameApi.GetModJsonConfig('neteaseMatchScript')
		for activity in self.mModJsonData['activity_list']:
			self.mActivityMap[activity['id']] = activity

	def ListenEvents(self):
		self.ListenForEvent(serverConsts.ModName, serverConsts.ClientSystemName,
							serverConsts.GetModJsonDataEvent, self, self.OnGetModJsonData)
		self.ListenForEvent(serverConsts.ModName, serverConsts.ClientSystemName,
							serverConsts.RequestCancelMatchClientEvent, self, self.OnRequestCancelMatch)
		self.ListenForEvent(serverConsts.ModName, serverConsts.ClientSystemName,
							serverConsts.GetLoginUIClientEvent, self, self.OnGetLoginUI)
		self.ListenForEvent(serverConsts.ModName, serverConsts.ClientSystemName,
							serverConsts.ApplyToMatchClientEvent, self, self.OnApplyToMatch)
		self.ListenForEvent(serverConsts.ModName, serverConsts.ServiceSystemName,
							serverConsts.ApplyErrServiceEvent, self, self.OnApplyErrServer)
		self.ListenForEvent(serverConsts.ModName, serverConsts.ServiceSystemName,
							serverConsts.ShowWaitUIServiceEvent, self, self.ONShowWaitUIServer)
		self.ListenForEvent(serverConsts.ModName, serverConsts.ServiceSystemName,
							serverConsts.WaitNumChangedServiceEvent, self, self.OnWaitNumChanged)
		self.ListenForEvent(serverConsts.ModName, serverConsts.ServiceSystemName,
							serverConsts.MatchResultServiceEvent, self, self.OnMatchResult)
		self.ListenForEvent(serverConsts.ModName, serverConsts.ClientSystemName,
							serverConsts.ConfirmOKClientEvent, self, self.OnConfirmUIOK)

		self.ListenForEvent(serverApi.GetEngineNamespace(), serverApi.GetEngineSystemName(), "DelServerPlayerEvent",
		                    self, self.OnDelServerPlayer)
		self.ListenForEvent(serverApi.GetEngineNamespace(), serverApi.GetEngineSystemName(), "PlayerDieEvent",
		                    self, self.OnPlayerDieEvent)
	# 	self.ListenForEvent(serverApi.GetEngineNamespace(), serverApi.GetEngineSystemName(), "ServerChatEvent",
	# 	                    self, self.OnTest) #for test
	# def OnTest(self, args):
	# 	if '1' == args['message']:
	# 		testUID = None
	# 		for x in self.mUID2Id.iterkeys():
	# 			testUID = x
	# 			break
	# 		testId = self.mUID2Id[testUID]
	# 		comp = serverApi.GetEngineCompFactory().CreateDimension(serverApi.GetLevelId())
	# 		comp.CreateDimension(3)
	# 		comp = serverApi.GetEngineCompFactory().ChangePlayerDimension(testId)
	# 		comp.ChangePlayerDimension(3, (0,4,0))
	# 	elif '2' == args['message']:
	# 		testUID = None
	# 		for x in self.mUID2Id.iterkeys():
	# 			testUID = x
	# 			break
	# 		testId = self.mUID2Id[testUID]
	# 		lobbyGameApi.TransferToOtherServer(testId, 'lobby', '')
	# 	elif '3' == args['message']:
	# 		self.RequestToService(serverConsts.ModName, 'service_test', args)
	# 	elif '4' == args['message']:
	# 		self.OnPlayerDieEvent({'id' : args['playerId']})

	def OnRequestCancelMatch(self, args):
		self.RequestToService(serverConsts.ModName, serverConsts.RequestCancelMatchServiceEvent, args)

	def OnGetLoginUI(self, args):
		playerId = args['id']
		uid = lobbyGameApi.GetPlayerUid(playerId)
		args['uid'] = int(uid)
		self.RequestToService(serverConsts.ModName, serverConsts.GetLoginUIServiceEvent, args)

	def OnDelServerPlayer(self, args):
		uid = args['uid']
		if uid in self.mUID2Id:
			del self.mUID2Id[uid]
		self.RequestToService(serverConsts.ModName, serverConsts.PlayerQuitServerEvent, args)

	def OnPlayerDieEvent(self, args):
		id = args['id']
		args['uid'] = lobbyGameApi.GetPlayerUid(id)
		self.RequestToService(serverConsts.ModName, serverConsts.MatchPlayerDieEvent, args,
		            lambda suc, tmp:self._RequestPlayerDieToServiceResponse(args, suc))

	def _RequestPlayerDieToServiceResponse(self, args, suc):
		self.NotifyToClient(args['id'], serverConsts.ClearMatchUIServerEvent, args)

	def OnGetModJsonData(self, args):
		'''
		将mod.json中相关内容告知客户端
		'''
		activityDataMap = {}
		playerId = args['id']
		for activity in self.mModJsonData['activity_list']:
			data = {}
			id = activity['id']
			data['id'] =id
			data['name'] = activity['name']
			data['apply_mode'] = activity['apply_mode']
			data['is_match_by_segment'] = activity['is_match_by_segment']
			data['detail'] = activity['detail']
			activityDataMap[id] = data
		resData = {'data' : activityDataMap}
		uid =lobbyGameApi.GetPlayerUid(playerId)
		self.mUID2Id[uid] = playerId
		resData['uid'] = int(uid)
		self.NotifyToClient(playerId, serverConsts.ResponseModJsonDataEvent, resData)
		args['uid'] = int(uid)
		self.RequestToService(serverConsts.ModName, serverConsts.PlayerEnterServerEvent, args)

	def OnConfirmUIOK(self, args):
		self.RequestToService(serverConsts.ModName, serverConsts.ConfirmOKServiceEvent, args)

	def OnMatchResult(self, args):
		uid = args['uid']
		if uid in self.mUID2Id:
			self.NotifyToClient(self.mUID2Id[uid], serverConsts.MatchResultServerEvent, args)

	def OnWaitNumChanged(self, args):
		uid = args['uid']
		if uid in self.mUID2Id:
			self.NotifyToClient(self.mUID2Id[uid], serverConsts.WaitNumChangedServerEvent, args)

	def ONShowWaitUIServer(self, args):
		uid = args['uid']
		if uid in self.mUID2Id:
			self.NotifyToClient(self.mUID2Id[uid], serverConsts.ShowWaitUIServerEvent, args)

	def OnApplyErrServer(self, args):
		if 'player_id' in args:
			self.NotifyToClient(args['player_id'], serverConsts.ApplyErrServerEvent, args)
		else:
			uid = args['uid']
			if uid in self.mUID2Id:
				self.NotifyToClient(self.mUID2Id[uid], serverConsts.ApplyErrServerEvent, args)

	def OnApplyToMatch(self, args):
		'''
		申请匹配
		'''
		activityId = args['activity_id']
		playerId = args['player_id']
		# 活动不存在
		activityData = self.mActivityMap.get(activityId, None)
		if not activityData:
			self._notifyToShowTips(playerId, activityId, serverConsts.ApplyCodeActivityNotExist)
			return
		bRetry = args.get('is_retry_match', False)
		if bRetry:
			self.RequestToService(serverConsts.ModName, serverConsts.ApplyToMatchServiceEvent, args)
			return
		memberInfo = args['member']
		#member 去重处理
		removeCnt = 0
		uid = args['uid']
		for idx, info in enumerate(memberInfo):
			if info['uid'] == uid:
				memberInfo[idx] = None
				removeCnt += 1
		for i in xrange(removeCnt):
			memberInfo.remove(None)
		args['member'] = memberInfo
		# 是否满足申请条件
		singleApplyMode = 1
		isRequestTeam = args['is_team']
		if singleApplyMode == activityData['apply_mode'] and isRequestTeam:
			self._notifyToShowTips(playerId, activityId, serverConsts.ApplyCodeApplyModeErr,
			        activityData['not_match_mode_error_message'])
			return
		teamApplyMod = 2
		if teamApplyMod == activityData['apply_mode'] and not isRequestTeam:
			self._notifyToShowTips(playerId, activityId, serverConsts.ApplyCodeApplyModeErr,
			        activityData['not_match_mode_error_message'])
			return
		# 检查是否满足分段条件
		nickname = lobbyGameApi.GetPlayerNickname(playerId)
		if activityData['is_match_by_segment']:
			segmentId, code, errMessage = self._getTeamSegment(activityData, args['match_value'], nickname, memberInfo)
			if segmentId < 0:
				self._notifyToShowTips(playerId, activityId, code, errMessage)
				return
			args['segment_id'] = segmentId
		# 检查是否满足阵营条件
		groupId = args['group_id']
		totalPlayer = len(memberInfo) + 1
		if groupId > 0:
			if groupId >= len(activityData['group_player_num']):
				self._notifyToShowTips(playerId, activityId, serverConsts.ApplyCodeGroupIdNotExist)
				return
			groupNum = activityData['group_player_num'][groupId]
			if totalPlayer > groupNum:
				self._notifyToShowTips(playerId, activityId, serverConsts.ApplyCodeTeamToManyPeopleToGroup)
				return
		else:
			if totalPlayer > sum(activityData['group_player_num']):
				self._notifyToShowTips(playerId, activityId, serverConsts.ApplyCodeTeamToManyPeopleToGroup)
				return
		playerInfo = {
			'uid': uid,
			'nickname': nickname,
			'match_value' : args['match_value']
		}
		args['player_info'] = playerInfo
		args['server_id'] = lobbyGameApi.GetServerId()
		self.RequestToService(serverConsts.ModName, serverConsts.ApplyToMatchServiceEvent, args)

	def _getTeamSegment(self, activityData, playerVal, nickname, memberInfo):
		notMatchErr = serverConsts.Code2Message[serverConsts.ApplyCodeNotMatchFregment]
		findSegment = None
		for segment in activityData['match_segment']:
			if playerVal >= segment['min'] and playerVal <= segment['max']:
				findSegment = segment
				break
		if not findSegment:
			return (-1, serverConsts.ApplyCodeNotMatchFregment, notMatchErr % nickname)
		for one in memberInfo:
			matchVal = one['match_value']
			if matchVal < findSegment['min'] or matchVal > findSegment['max']:
				return (-1, serverConsts.ApplyCodeNotMatchFregment, notMatchErr % one['nickname'])
		return (findSegment['id'], serverConsts.CodeSuccess, '')


	def _notifyToShowTips(self, id, activityId, code, message = '', displayTime = 3):
		if not message:
			message = serverConsts.Code2Message[code]
		resData = {
			'code' : code,
			'message': message,
			'display_time': displayTime,
			'ui_id': -1,  # -1表示不需要告知服务端ui已经显示了
			'activity_id' : activityId,
		}
		self.NotifyToClient(id, serverConsts.ApplyErrServerEvent, resData)



