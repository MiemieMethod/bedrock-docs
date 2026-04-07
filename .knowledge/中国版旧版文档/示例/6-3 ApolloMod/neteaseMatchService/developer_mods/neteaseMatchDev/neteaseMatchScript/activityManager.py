# -*- coding: utf-8 -*-
import neteaseMatchScript.matchActivity as matchActivity
import apolloCommon.commonNetgameApi as commonNetgameApi
import neteaseMatchScript.serviceConsts as serviceConsts
import neteaseMatchScript.playerInfo as playerInfo
import logout
class ActivityManager(object):
	'''
	处理活动相关逻辑
	'''
	def __init__(self, system):
		import weakref
		self.mModJsonData = commonNetgameApi.GetModJsonConfig('neteaseMatchScript')
		self.mId2MatchActivity = {}
		for data in self.mModJsonData['activity_list']:
			activity = matchActivity.MatchActivity(data)
			self.mId2MatchActivity[data['id']] = activity
		self.mSystem = weakref.proxy(system)
		self.RegisterMethods()

	def RegisterMethods(self):
		self.mSystem.RegisterRpcMethod(serviceConsts.ModName, serviceConsts.MatchPlayerLogoutEvent,
				self.OnMatchPlayerLogout)
		self.mSystem.RegisterRpcMethod(serviceConsts.ModName, serviceConsts.MatchPlayerDieEvent,
				self.OnMatchPlayerDie)
		self.mSystem.RegisterRpcMethod(serviceConsts.ModName, serviceConsts.ApplyToMatchServiceEvent,
		        self.OnApplyToMatch)
		self.mSystem.RegisterRpcMethod(serviceConsts.ModName, serviceConsts.ConfirmOKServiceEvent,
		        self.OnConfirmUIOK)
		self.mSystem.RegisterRpcMethod(serviceConsts.ModName, serviceConsts.GetLoginUIServiceEvent,
		        self.OnGetLoginUI)
		self.mSystem.RegisterRpcMethod(serviceConsts.ModName, serviceConsts.RequestCancelMatchServiceEvent,
		        self.OnRequestCancelMatch)

	def GetPlayerApplyTime(self, uid, activityId):
		'''
		获取某个玩家参加某个活动的报名时间
		'''
		activity = self.mId2MatchActivity.get(activityId, None)
		if not activity:
			logout.warning('GetPlayerApplyTime err.activity not exist!args:', activityId, uid)
			return -1
		return activity.GetPlayerApplyTime(uid)

	def OnRequestCancelMatch(self, serverId, callbackId, args):
		'''
		取消匹配
		'''
		print 'OnRequestCancelMatch', args
		actId = args['activity_id']
		uid = args['uid']
		activity = self.mId2MatchActivity.get(actId, None)
		if not activity:
			logout.warning('OnRequestCancelMatch err.activity not exist!args:', args)
			return
		activity.CancelMatching(uid)

	def OnGetLoginUI(self, serverId, callbackId, args):
		'''
		登陆后，获取需要显示的匹配ui界面
		'''
		uid = int(args['uid'])
		for activity in self.mId2MatchActivity.itervalues():
			activity.NotifyShowWaitUIByUid(uid)

	def OnConfirmUIOK(self, serverId, callbackId, args):
		'''
		确认提示ui或匹配成功
		'''
		uiId = args['ui_id']
		activityId = args['activity_id']
		activity = self.mId2MatchActivity.get(activityId, None)
		if not activity:
			logout.warning('OnConfirmUIOK err.activity not exist!args:', args)
			return
		if 'tips' == args['type']:
			activity.RemoveTips(uiId)
		elif 'match_ok' == args['type']:
			activity.ConfirmMatchOK(uiId, args['uid'])

	def GetApppliedActivityList(self, uid):
		'''
		获取玩家报名活动列表
		'''
		lst = []
		for activityId, activity in self.mId2MatchActivity.iteritems():
			if activity.IsInMatching(uid):
				lst.append(activityId)
		return lst

	def GetAppliedUIDs(self, activityId):
		'''
		获取匹配队列
		'''
		activity = self.mId2MatchActivity.get(activityId, None)
		if not activity:
			logout.warning('GetAppliedUIDs err.activity not exist!apply args:', activityId)
			return []
		return activity.GetAppliedUIDs()

	def OnApplyToMatch(self, serverId, callbackId, args):
		'''
		报名参加活动
		'''
		print 'OnApplyToMatch', args
		activityId = args['activity_id']
		uid = args['uid']
		activity = self.mId2MatchActivity.get(activityId, None)
		if not activity:
			logout.error('OnApplyToMatch err.activity not exist!apply args:', args)
			return
		if args['is_retry_match']:
			code = activity.ReMatch(uid)
			eventData = {
				'code': code,
				'message': serviceConsts.Code2Message[code],
				'ui_id': -1,
				'activity_id': activityId,
				'player_id': args['player_id'],
				'id': args,
				'uid' : uid
			}
			print 'Rematch result.apply uid:%s.result code:%s' % (uid, code)
			self.mSystem.NotifyToServerNode(serverId, serviceConsts.ApplyErrServiceEvent, eventData)
			return
		playerArgs = args['player_info']
		memberInfo = []
		applyUIDs = [uid]
		for oneArgs in args['member']:
			oneMember = playerInfo.MemberPlayerInfo(oneArgs['uid'], oneArgs['nickname'], oneArgs['match_value'])
			memberInfo.append(oneMember)
			applyUIDs.append(oneArgs['uid'])
		matchInfo = playerInfo.MatchPlayerInfo(uid, playerArgs['nickname'], args['is_team'],
		        args['group_id'], args['match_value'], memberInfo)
		#是否匹配中
		for one in applyUIDs:
			if activity.IsInMatching(one):
				if matchInfo.mBTeam:
					code = serviceConsts.ApplyCodeTeamPlayerInMatching
					message = serviceConsts.Code2Message[code] % matchInfo.GetNickname(one)
				else:
					code = serviceConsts.ApplyCodeInMatching
					message = serviceConsts.Code2Message[code]
				eventData = {
					'message' : message,
					'code' : code,
					'display_time' : 3,
					'ui_id' : -1,
					'activity_id' : activityId,
					'player_id' : args['player_id'],
					'uid' : uid
				}
				logout.warning('OnApplyToMatch err.match err!player in match:%s.apply args:' % one, args)
				self.mSystem.NotifyToServerNode(serverId, serviceConsts.ApplyErrServiceEvent, eventData)
				return
		activity.AddNewPlayer(matchInfo)
		eventData = {
			'code': serviceConsts.CodeSuccess,
			'ui_id': -1,
			'activity_id': activityId,
			'player_id': args['player_id'],
			'uid': uid
		}
		self.mSystem.NotifyToServerNode(args['server_id'], serviceConsts.ApplyErrServiceEvent, eventData)

	def OnMatchPlayerDie(self, serverId, callbackId, args):
		'''
		玩家登出游戏处理
		'''
		uid = args['uid']
		for activity in self.mId2MatchActivity.itervalues():
			activity.CancelMatching(uid)
		self.mSystem.ResponseToServer(serverId, callbackId, {})

	def OnMatchPlayerLogout(self, serverId, callbackId, args):
		'''
		玩家登出游戏处理
		'''
		uid = args['uid']
		for activity in self.mId2MatchActivity.itervalues():
			activity.PlayerLogout(uid)

	def Update(self):
		for activity in self.mId2MatchActivity.itervalues():
			activity.Update()

	def Destroy(self):
		self.mSystem = None