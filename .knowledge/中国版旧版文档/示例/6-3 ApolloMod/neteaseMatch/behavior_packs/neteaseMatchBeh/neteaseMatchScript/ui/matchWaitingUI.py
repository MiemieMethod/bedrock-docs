# -*- coding: utf-8 -*-

import client.extraClientApi as clientApi
ViewBinder = clientApi.GetViewBinderCls()
ViewRequest = clientApi.GetViewViewRequestCls()
ScreenNode = clientApi.GetScreenNodeCls()
import neteaseMatchScript.apiUtil as apiUtil
import neteaseMatchScript.clientConsts as clientConsts
import time

class MatchWaitingUI(ScreenNode):
	def __init__(self, namespace, name, param):
		ScreenNode.__init__(self, namespace, name, param)
		#ui相关常量
		self.mActivityBase = '/main_activity/image_base'
		self.mTipsPath = '/main_waiting/img_cancel_tips'
		self.mWaitBase = '/main_waiting/img_waiting%s'
		self.mWait0Base = self.mWaitBase % 0
		self.mWaitTextFormat = '%s    已报名:%d/%d    已等待%s'
		self.mTimeoutBase = '/main_waiting/img_tips'
		#游戏相关变量
		self.mTipsUIQueue = [] #提示ui列表，一段时间自动消失
		self.mActivityOrTimeoutUIList = [] #活动或超时ui列表
		self.mId2WaitingMatch = {} #activityId-->等待报名信息
		self.mWaitingUIIdToActivityId = [] #等待报名ui id到报名活动的映射，数组索引表示ui id, 表示第几个等待匹配界面
		self.mWaitCancelUIToActId = {} #取消报名ui路径到活动映射
		self.mTickCount = 0
		self.mTimer = None

	# Create函数是继承自ScreenNode，会在UI创建完成后被调用
	def Create(self):
		self.AddTouchEventHandler(self.mWait0Base + '/btn_cancel_waiting', self.OnCancelMatch)
		self.AddTouchEventHandler(self.mTimeoutBase + '/btn_continue', self.OnContinueWait)
		self.AddTouchEventHandler(self.mTimeoutBase + '/btn_cancel_match', self.OnCancelWait)
		self.AddTouchEventHandler(self.mTimeoutBase + '/btn_close', self.OnCancelWait)
		self.AddTouchEventHandler(self.mActivityBase + '/btn_match', self.OnMatch)
		self.AddTouchEventHandler(self.mActivityBase + '/btn_close_activity', self.OnCloseApplyMatch)

	def Clear(self):
		if self.mTimer:
			comp = clientApi.GetEngineCompFactory().CreateGame(clientApi.GetLevelId())
			comp.CancelTimer(self.mTimer)
		self.ClearUI()
		self.mTimer = None
		self.mTipsUIQueue = []
		self.mActivityOrTimeoutUIList = []
		self.mId2WaitingMatch = {}
		self.mWaitingUIIdToActivityId = []
		self.mWaitCancelUIToActId = {}
		self.mTickCount = 0

	def ClearUI(self):
		self.SetVisible(self.mTimeoutBase, False)
		self.SetVisible(self.mActivityBase, False)
		self.CloseTips()
		while self.mWaitCancelUIToActId:
			uiPath = iter(self.mWaitCancelUIToActId).next() #取出第一个元素
			self.DelWaitingMatchUI(uiPath)
		self.SetVisible(self.mWait0Base, False)

	def Destroy(self):
		self.Clear()

	def ShowNextActivityOrTimeoutUI(self):
		self.mActivityOrTimeoutUIList.pop()
		self.ShowActivityOrTimeoutUI()

	def ShowActivityOrTimeoutUI(self):
		'''
		显示活动ui或超时ui
		'''
		if not self.mActivityOrTimeoutUIList:
			self.SetVisible(self.mTimeoutBase, False)
			self.SetVisible(self.mActivityBase, False)
			return
		uiInfo = self.mActivityOrTimeoutUIList[-1]
		if 'activity' == uiInfo['ui_type']:
			self._doShowActivity(uiInfo)
		else:
			self._doShowTimeoutUI(uiInfo)

	def _doShowTimeoutUI(self, timeoutInfo):
		'''
		显示超时ui
		'''
		self.SetVisible(self.mTimeoutBase, True)
		self.SetVisible(self.mActivityBase, False)
		curTime = int(time.time())
		remainSeconds = timeoutInfo['start_time'] + 10 - curTime
		#倒计时完毕了，直接关闭ui界面
		if remainSeconds < 0:
			self.ShowNextActivityOrTimeoutUI()
			return
		tipsPath = '%s/%s' % (self.mTimeoutBase, 'lb_tips')
		self.SetText(tipsPath, timeoutInfo['name'])
		contentPath = '%s/%s' % (self.mTimeoutBase, 'lb_tipscontent')
		self.SetText(contentPath, '匹配时间过长，是否继续等待')
		cancelText = '取消报名(%ds)'
		cancelPath = '%s/%s/button_label' % (self.mTimeoutBase, 'btn_cancel_match')
		self.SetText(cancelPath, cancelText % remainSeconds)

	def _doShowActivity(self, uiInfo):
		'''
		显示活动ui
		'''
		print '_doShowActivity', uiInfo
		self.SetVisible(self.mTimeoutBase, False)
		self.SetVisible(self.mActivityBase, True)
		namePath = '%s/lb_name' % self.mActivityBase
		self.SetText(namePath, uiInfo['name'])
		scrollBase = '%s/scroll_activity_detail' % self.mActivityBase
		scrollMouse = scrollBase + '/scroll_mouse/scroll_view/stack_panel/background_and_viewport/scrolling_view_port/scrolling_content/pnl_activity/lb_activity'
		size = self.GetSize(scrollMouse)
		if size:
			self.SetText(scrollMouse, uiInfo['detail'])
			self.SetSize(scrollBase + '/scroll_mouse/scroll_view/stack_panel/background_and_viewport/scrolling_view_port/scrolling_content',
			    (size[0], size[1]*1.1))
		else:
			scrollTouch = scrollBase + '/scroll_touch/scroll_view/panel/background_and_viewport/scrolling_view_port/scrolling_content/pnl_activity/lb_activity'
			size = self.GetSize(scrollTouch)
			self.SetText(scrollTouch, uiInfo['detail'])
			self.SetSize(
				scrollBase + '/scroll_touch/scroll_view/panel/background_and_viewport/scrolling_view_port/scrolling_content',
				(size[0], size[1]*1.1))

	def UpdateTimeoutUI(self):
		'''
		更新超时ui
		'''
		if not self.mActivityOrTimeoutUIList:
			return
		uiInfo = self.mActivityOrTimeoutUIList[-1]
		uiType = uiInfo.get('ui_type', '')
		if 'timeout' == uiType:
			self._doShowTimeoutUI(uiInfo)

	def ShowTips(self):
		'''
		显示提示信息
		'''
		if not self.mTipsUIQueue or self.mTimer:
			return
		tipsInfo = self.mTipsUIQueue[0]
		print 'ShowTips', tipsInfo
		self.mTipsUIQueue.remove(tipsInfo)
		msg = tipsInfo['message']
		showTime = tipsInfo.get('display_time', 3)
		self.SetVisible(self.mTipsPath, True)
		self.SetText(self.mTipsPath + '/lb_cancel_tips', msg)
		comp = clientApi.GetEngineCompFactory().CreateGame(clientApi.GetLevelId())
		self.mTimer = comp.AddTimer(showTime, self.CloseTips)

	def CloseTips(self):
		self.mTimer = None
		self.SetVisible(self.mTipsPath, False)
		self.ShowTips()

	# 继承自ScreenNode的方法，会被引擎自动调用，1秒钟30帧
	def Update(self):
		self.mTickCount += 1
		if 0 == self.mTickCount % 6 and self.mWaitingUIIdToActivityId:
			self.ShowWaitingList()
		if 0 == self.mTickCount % 6:
			self.UpdateTimeoutUI()

	def ShowWaitingList(self):
		'''
		显示所有的等待匹配ui
		'''
		for uiId, actId in enumerate(self.mWaitingUIIdToActivityId):
			self._showWaitingUI(uiId, actId)

	def _showWaitingUI(self, uiId, actId):
		waitActivityInfo = self.mId2WaitingMatch[actId]
		basePath = self.mWaitBase % uiId
		labelWaitingPath = '%s/lb_waiting' % basePath
		startTime = waitActivityInfo['start_time']
		waitText = self.mWaitTextFormat % (waitActivityInfo['name'], waitActivityInfo['cur_num'],
		    waitActivityInfo['total_num'], self._timestampToWaitTimeStr(startTime))
		self.SetText(labelWaitingPath, waitText)

	def _timestampToWaitTimeStr(self, start):
		cur = int(time.time())
		wait = cur - start + 57600
		local = time.localtime(wait)
		return time.strftime("%H:%M:%S", local)

	def UpdateWaitingMatchUI(self, actId, curNum):
		'''
		更新等待匹配ui信息
		'''
		waitInfo = self.mId2WaitingMatch.get(actId, None)
		if not waitInfo:
			print 'UpdateWaitingMatchUI err!activity is not applied!args:', actId, curNum
			return
		waitInfo['cur_num'] = curNum
		self.ShowWaitingList()

	def AddTimeoutUI(self, timeoutInfo):
		'''
		新增一个超时ui，需要排队显示ui
		'''
		print 'AddTimeoutUI', timeoutInfo
		timeoutInfo['ui_type'] = 'timeout'
		actId = timeoutInfo['activity_id']
		self.DelWaitingMatchUIByActId(actId)
		for info in self.mActivityOrTimeoutUIList:
			if 'timeout' == info['ui_type'] and actId == info['activity_id']:
				return
		self.mActivityOrTimeoutUIList.append(timeoutInfo)
		self._doShowTimeoutUI(timeoutInfo)

	def AddActivityUI(self, uiInfo):
		'''
		新增一个活动ui，需要排队显示ui
		'''
		uiInfo['ui_type'] = 'activity'
		actId = uiInfo['activity_id']
		for info in self.mActivityOrTimeoutUIList:
			if 'activity' == info['ui_type'] and actId == info['activity_id']:
				self.mActivityOrTimeoutUIList.remove(info)
				break
		self.mActivityOrTimeoutUIList.append(uiInfo)
		self._doShowActivity(uiInfo)

	def AddTips(self, uiInfo):
		'''
		现在一个提示信息，需要排队显示提示
		'''
		print 'AddTips', uiInfo
		self.mTipsUIQueue.append(uiInfo)
		self.ShowTips()

	def AddWaitingMatchUI(self, waitInfo):
		'''
		新增一个等待匹配ui
		'''
		print 'AddWaitingMatchUI', waitInfo
		actId = waitInfo['activity_id']
		self.mId2WaitingMatch[actId] = waitInfo
		uiId = len(self.mWaitingUIIdToActivityId)
		self.mWaitingUIIdToActivityId.append(actId)
		basePath = self.mWaitBase % uiId
		btnCancelPath = '%s/btn_cancel_waiting' % basePath
		self.mWaitCancelUIToActId[btnCancelPath] = actId
		if uiId > 0:
			newName = 'img_waiting%d' % uiId
			self.Clone(self.mWait0Base, '/main_waiting', newName)
			wait0Pos = self.GetPosition(self.mWait0Base)
			wait0Size = self.GetSize(self.mWait0Base)
			fullname = '/main_waiting/%s' % newName
			height = wait0Pos[1] + uiId * (wait0Size[1] + 2)
			self.SetPosition(fullname, (wait0Pos[0], height))
		else:
			self.SetVisible(self.mWait0Base, True)
		self.ShowWaitingList()

	def DelTimeoutUIByActId(self, actId):
		'''
		删除超时ui
		'''
		print 'DelTimeoutUIByActId', actId
		for one in self.mActivityOrTimeoutUIList:
			if 'activity' == one['ui_type'] and one['activity_id'] == actId:
				self.mActivityOrTimeoutUIList.remove(one)
				break
		self.ShowActivityOrTimeoutUI()

	def DelWaitingMatchUIByActId(self, actId):
		'''
		删除等待匹配ui
		'''
		print 'DelWaitingMatchUIByActId', actId
		findPath = None
		for k, v in self.mWaitCancelUIToActId.iteritems():
			if v == actId:
				findPath = k
		if findPath:
			self.DelWaitingMatchUI(findPath)

	def DelWaitingMatchUI(self, cancelUIPath):
		'''
		删除等待匹配ui
		'''
		print 'DelWaitingMatchUI', cancelUIPath
		actId = self.mWaitCancelUIToActId.get(cancelUIPath, None)
		if actId is None:
			print 'DelWaitingMatchUI err.no activity', cancelUIPath, self.mWaitCancelUIToActId
			return
		if actId in self.mId2WaitingMatch:
			del self.mId2WaitingMatch[actId]
		findUiId = -1
		for uiId, checkActId in enumerate(self.mWaitingUIIdToActivityId):
			if checkActId == actId:
				findUiId = uiId
				self.mWaitingUIIdToActivityId.remove(checkActId)
				break
		if findUiId < 0:
			print 'DelWaitingMatchUI err.not found activity', cancelUIPath, self.mWaitCancelUIToActId
			return
		self.mWaitCancelUIToActId = {}
		for uiId, oneActId in enumerate(self.mWaitingUIIdToActivityId):
			basePath = self.mWaitBase % uiId
			btnCancelPath = '%s/btn_cancel_waiting' % basePath
			self.mWaitCancelUIToActId[btnCancelPath] = oneActId
		lastUiId = len(self.mWaitingUIIdToActivityId)
		if 0 == lastUiId:
			self.SetVisible(self.mWait0Base, False)
		else:
			uiPath = self.mWaitBase % lastUiId
			self.RemoveComponent(uiPath, '/main_waiting')
		self.ShowWaitingList()

	@apiUtil.touch_filter("up")
	def OnCancelWait(self, args):
		'''
		取消报名，不继续等待了
		'''
		print 'OnCancelWait', args
		uiInfo = self.mActivityOrTimeoutUIList[-1]
		if 'timeout' != uiInfo['ui_type']:
			print 'is not timeout ui.not send cancel request!'
			return
		activityId = uiInfo['activity_id']
		eventData = {
			'activity_id' : activityId,
		}
		apiUtil.DoNotifyToServer(clientConsts.RequestCancelMatchClientEvent, eventData)
		self.ShowNextActivityOrTimeoutUI()

	@apiUtil.touch_filter("up")
	def OnContinueWait(self, args):
		'''
		继续等待匹配
		'''
		print 'OnContinueWait', args
		uiInfo = self.mActivityOrTimeoutUIList[-1]
		if 'timeout' != uiInfo['ui_type']:
			print 'not timeout ui.not send continue request!'
			return
		activityId = uiInfo['activity_id']
		eventData = {
			'activity_id' : activityId
		}
		print 'OnMatch', eventData
		apiUtil.GetMatchClientSystem().BroadcastEvent(clientConsts.RetryApplyToMatchLocalEvent, eventData)
		self.ShowNextActivityOrTimeoutUI()

	@apiUtil.touch_filter("up")
	def OnCancelMatch(self, args):
		'''
		取消报名
		'''
		print 'OnCancelMatch', args
		buttonPath = args['ButtonPath']
		activityId = self.mWaitCancelUIToActId[buttonPath]
		eventData = {
			'activity_id' : activityId,
		}
		self.DelWaitingMatchUI(buttonPath)
		apiUtil.DoNotifyToServer(clientConsts.RequestCancelMatchClientEvent, eventData)

	@apiUtil.touch_filter("up")
	def OnCloseApplyMatch(self, args):
		'''
		关闭报名界面
		'''
		print 'OnCloseApplyMatch', args
		if not self.mActivityOrTimeoutUIList:
			print 'OnCloseApplyMatch err.no activity ui'
			return
		uiInfo = self.mActivityOrTimeoutUIList[-1]
		if 'activity' != uiInfo['ui_type']:
			print 'OnCloseApplyMatch err.not activity ui.cur ui info:', uiInfo
			return
		self.ShowNextActivityOrTimeoutUI()

	@apiUtil.touch_filter("up")
	def OnMatch(self, args):
		'''
		申请报名
		'''
		print 'OnMatch', args
		if not self.mActivityOrTimeoutUIList:
			print 'UI is closed.not send match request!'
			return
		uiInfo = self.mActivityOrTimeoutUIList[-1]
		if 'activity' != uiInfo['ui_type']:
			print 'currenct ui is not match ui.not send match request!'
			return
		print 'OnMatch.ui info:', uiInfo
		activityId = uiInfo['activity_id']
		eventData = {
			'activity_id' : activityId
		}
		print 'OnMatch', eventData
		if apiUtil.IsShieldApplyMatch(activityId):
			apiUtil.GetMatchClientSystem().BroadcastEvent(clientConsts.ApplyToMatchLocalEvent, eventData)
		else:
			apiUtil.GetMatchClientSystem().BroadcastEvent(clientConsts.DefaultApplyToMatchEvent, eventData)
		self.ShowNextActivityOrTimeoutUI()
