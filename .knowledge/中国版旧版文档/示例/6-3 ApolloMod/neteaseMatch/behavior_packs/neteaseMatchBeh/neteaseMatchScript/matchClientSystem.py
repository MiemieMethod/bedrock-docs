# -*- coding: utf-8 -*-
import client.extraClientApi as extraClientApi
ClientSystem = extraClientApi.GetClientSystemCls()
import client.extraClientApi as clientApi
import neteaseMatchScript.clientConsts as clientConsts
import neteaseMatchScript.apiUtil as apiUtil

class MatchClientSystem(ClientSystem):
	def __init__(self, namespace, systemName):
		ClientSystem.__init__(self, namespace, systemName)
		self.ListenEvents()
		self.mModJsonData = {} #mod.json中活动部分配置信息
		self.mShiledApplyActivity = {}#记录屏蔽活动默认申请开关
		self.mMatchWaitingUINode = None#报名匹配ui
		comp = clientApi.GetEngineCompFactory().CreatePlayer(clientApi.GetLocalPlayerId())
		self.mLocalUID = 0
		apiUtil.Init(self)

	def Destroy(self):
		ClientSystem.Destroy(self)
		apiUtil.Destroy()

	def ListenEvents(self):
		self.ListenForEvent(clientApi.GetEngineNamespace(), clientApi.GetEngineSystemName(),
							"OnLocalPlayerStopLoading", self, self.OnLocalPlayerStopLoading)
		self.ListenForEvent(clientApi.GetEngineNamespace(), clientApi.GetEngineSystemName(),
							"UiInitFinished", self, self.OnUiInitFinished)
		self.ListenForEvent(clientConsts.ModName, clientConsts.ClientSystemName, clientConsts.DefaultApplyToMatchEvent,
		                    self, self.OnDefaultApplyToMatch)
		self.ListenForEvent(clientConsts.ModName, clientConsts.ClientSystemName, clientConsts.RetryApplyToMatchLocalEvent,
		                    self, self.OnRetryApplyToMatch)
		self.ListenForEvent(clientConsts.ModName, clientConsts.ServerSystemName,
							clientConsts.ResponseModJsonDataEvent, self, self.OnResponseModJsonData)
		self.ListenForEvent(clientConsts.ModName, clientConsts.ServerSystemName,
							clientConsts.ShowWaitUIServerEvent, self, self.OnShowWaitUI)
		self.ListenForEvent(clientConsts.ModName, clientConsts.ServerSystemName,
							clientConsts.WaitNumChangedServerEvent, self, self.OnWaitNumChanged)
		self.ListenForEvent(clientConsts.ModName, clientConsts.ServerSystemName,
							clientConsts.MatchResultServerEvent, self, self.OnMatchResult)
		self.ListenForEvent(clientConsts.ModName, clientConsts.ServerSystemName,
							clientConsts.ClearMatchUIServerEvent, self, self.OnClearMatchUI)
		self.ListenForEvent(clientConsts.ModName, clientConsts.ServerSystemName,
		                    clientConsts.ApplyErrServerEvent, self, self.OnApplyErr)

	def OnClearMatchUI(self, args):
		'''
		清除匹配的ui。玩家死亡后会退出匹配逻辑，此时需要清除匹配相关ui
		'''
		print 'OnClearMatchUI', args
		self.mMatchWaitingUINode.Clear()

	def OnMatchResult(self, args):
		'''
		处理匹配结果
		'''
		print 'OnMatchResult', args
		code = args['code']
		activityId = args['activity_id']
		activityData = self.mModJsonData[activityId]
		uiId = args.get('ui_id', -1)
		if uiId >= 0:
			uiType = 'match_ok' if clientConsts.CodeSuccess == code else 'tips'
			eventData = {'activity_id' : activityId, 'type' : uiType, 'uid' : self.mLocalUID, 'ui_id' : uiId}
			apiUtil.DoNotifyToServer(clientConsts.ConfirmOKClientEvent, eventData)
		if clientConsts.MatchCodeTimeoutCanRetry == code:
			timeoutInfo = {
				'activity_id' : activityId,
				'start_time' : args['start_time'],
				'name' : activityData['name']

			}
			self.mMatchWaitingUINode.AddTimeoutUI(timeoutInfo)
		elif clientConsts.MatchCodeTimeoutNoRetry == code:
			self.mMatchWaitingUINode.DelWaitingMatchUIByActId(activityId)
			tipsInfo = {
				'message' : args['message'],
				'display_time' : args.get('display_time', 3),
				'ui_id' : args['ui_id'],
				'activity_id' : args['activity_id']
			}
			self.mMatchWaitingUINode.AddTips(tipsInfo)
		elif clientConsts.MatchCodeAutoCancelMatch == code:
			self.mMatchWaitingUINode.DelTimeoutUIByActId(activityId)
			tipsInfo = {
				'message' : args['message'],
				'display_time' : args.get('display_time', 3),
				'ui_id' : args['ui_id'],
				'activity_id' : args['activity_id']
			}
			self.mMatchWaitingUINode.AddTips(tipsInfo)
		elif clientConsts.MatchCodeCancelMatch == code:
			activityId = args['activity_id']
			self.mMatchWaitingUINode.DelWaitingMatchUIByActId(activityId)
			tipsInfo = {
				'message' : args['message'],
				'display_time' : args.get('display_time', 3),
				'ui_id' : args['ui_id'],
				'activity_id' : args['activity_id']
			}
			self.mMatchWaitingUINode.AddTips(tipsInfo)
		elif clientConsts.CodeSuccess == code:
			self.mMatchWaitingUINode.DelWaitingMatchUIByActId(activityId)
			tipsInfo = {
				'message' : '报名成功',
				'display_time' : args.get('display_time', 3),
				'ui_id' : -1,
				'activity_id' : args['activity_id']
			}
			self.mMatchWaitingUINode.AddTips(tipsInfo)
		else:
			tipsInfo = {
				'message' : args['message'],
				'display_time' : args.get('display_time', 3),
				'ui_id' : args['ui_id'],
				'activity_id' : args['activity_id']
			}
			self.mMatchWaitingUINode.AddTips(tipsInfo)
		eventData = {
			'activity_id': activityId,
			'code' : args['code'],
			'group_uids' : args.get('group_uids', [])
		}
		self.BroadcastEvent(clientConsts.MatchResultEvent, eventData)

	def OnWaitNumChanged(self, args):
		'''
		匹配界面报名人数发生变化
		'''
		self.mMatchWaitingUINode.UpdateWaitingMatchUI(args['activity_id'], args['cur_num'])

	def OnShowWaitUI(self, args):
		'''
		显示等待界面
		'''
		uiInfo = {
			'activity_id' : args['activity_id'],
			'start_time': args['start_time'],
			'name': args['name'],
			'cur_num': args.get('cur_num', 1),
			'total_num' : args['total_num'],
		}
		self.mMatchWaitingUINode.AddWaitingMatchUI(uiInfo)

	def OnApplyErr(self, args):
		'''
		申请结果处理
		'''
		print 'OnApplyErr', args
		if clientConsts.CodeSuccess != args['code']:
			uiInfo = {
				'message' : args['message'],
				'display_time': args.get('display_time', 3),
				'ui_id' : args.get('ui_id', -1)
			}
			self.mMatchWaitingUINode.AddTips(uiInfo)

		eventData = {
			'activity_id' : args['activity_id'],
			'code':args['code']
		}
		self.BroadcastEvent(clientConsts.ApplyToMatchResultEvent, eventData)

	def OnLocalPlayerStopLoading(self, args):
		'''
		请求获取mod.json信息
		'''
		eventData = {'id' : clientApi.GetLocalPlayerId()}
		self.NotifyToServer(clientConsts.GetModJsonDataEvent, eventData)

	def OnResponseModJsonData(self, args):
		'''
		获取mod.json信息
		'''
		self.mModJsonData = args['data']
		self.mLocalUID = args['uid']
		apiUtil.InitLocalUser(self.mLocalUID)

	def OnUiInitFinished(self, args):
		print "On UiInitFinished"
		clientApi.RegisterUI(clientConsts.ModName, "matchWaitingUI",
							 "neteaseMatchScript.ui.matchWaitingUI.MatchWaitingUI",
							 "matchWaitingUI.main")
		self.mMatchWaitingUINode = clientApi.CreateUI(clientConsts.ModName, "matchWaitingUI", {"isHud": 1})
		self.mMatchWaitingUINode.ClearUI()
		self.NotifyToServer(clientConsts.GetLoginUIClientEvent, {'id' : clientApi.GetLocalPlayerId()})

	def OpenMatchUI(self, activityId):
		'''
		打开报名界面。
		activityId:活动id，对应mod.json中activity_list中活动唯一id配置
		return:None
		'''
		activityData = self.mModJsonData.get(activityId, None)
		print 'OpenMatchUI', activityData, self.mModJsonData
		if not activityData:
			print 'OpenMatchUI fail!activity not exist.activity id:%d' % activityId
			return
		uiInfo = {
			'activity_id' : activityId,
			'ui_type' : 'activity',
			'name' : activityData['name'],
			'detail' : activityData['detail'],
		}
		self.mMatchWaitingUINode.AddActivityUI(uiInfo)

	def ShieldDefaultApplyMethod(self, activityId):
		'''
		屏蔽默认的报名逻辑，单人匹配逻辑不会生效。开发者要求监听ApplyToMatchLocalEvent事件实现报名匹配逻辑
		activityId:活动id，屏蔽该活动的默认报名逻辑
		return:None
		'''
		print 'ShieldDefaultApplyMethod', activityId
		self.mShiledApplyActivity[activityId] = True

	def OnRetryApplyToMatch(self, args):
		'''
		超时后，重新报名匹配
		'''
		print 'OnRetryApplyToMatch', args
		activityId = args['activity_id']
		self.ReApplyToMatchActivity(activityId)

	def IsShieldApplyMatch(self, activityId):
		return activityId in self.mShiledApplyActivity

	def OnDefaultApplyToMatch(self, args):
		'''
		申请匹配
		'''
		print 'OnDefaultApplyToMatch', args
		activityId = args['activity_id']
		if self.IsShieldApplyMatch(activityId):
			return
		if activityId not in self.mModJsonData:
			print 'OnDefaultApplyToMatch fail.no activity.id:', activityId
			return
		self.ApplyToMatchActivity(activityId, self.mLocalUID, 1)

	def ReApplyToMatchActivity(self, activityId):
		'''
		继续申请匹配，要求玩家之前有发送过匹配超时
		'''
		self.ApplyToMatchActivity(activityId, self.mLocalUID, -1, False, [], -1, True)

	def ApplyToMatchActivity(self, activityId, uid, matchValue, isTeam = False, memberInfo = [], groupId = -1, bRetryMatch = False):
		'''
		申请加入某个活动
		memberInfo 包含所有成员信息，包括队长自己
		'''
		print 'ApplyToMatchActivity', activityId, uid, matchValue, isTeam, memberInfo, groupId, bRetryMatch
		eventData = {
			'player_id': clientApi.GetLocalPlayerId(),
			'match_value' : matchValue,
			'activity_id' : activityId,
			'uid' : uid,
			'is_team':isTeam,
			'member' : memberInfo,
			'group_id' : groupId,
			'is_retry_match' : bRetryMatch
		}
		self.NotifyToServer(clientConsts.ApplyToMatchClientEvent, eventData)
