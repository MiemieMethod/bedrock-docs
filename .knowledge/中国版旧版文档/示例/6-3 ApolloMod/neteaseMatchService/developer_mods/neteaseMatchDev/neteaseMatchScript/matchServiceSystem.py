# -*- coding: utf-8 -*-
import server.extraServiceApi as serviceApi
ServiceSystem = serviceApi.GetServiceSystemCls()
import neteaseMatchScript.activityManager as activityManager
import neteaseMatchScript.apiUtil as apiUtil
import neteaseMatchScript.serviceConsts as serviceConsts

class MatchServiceSystem(ServiceSystem):
	def __init__(self, namespace, systemName):
		ServiceSystem.__init__(self,namespace,systemName)
		self.mPlayer2ServerId = {}#记录玩家所在服务器
		self.mActivityManager = activityManager.ActivityManager(self)
		apiUtil.SetSystem(self)
		self.RegisterMethods()

	def RegisterMethods(self):
		self.RegisterRpcMethod(serviceConsts.ModName, serviceConsts.PlayerEnterServerEvent,
				self.OnPlayerEnter)
		self.RegisterRpcMethod(serviceConsts.ModName, serviceConsts.PlayerQuitServerEvent,
				self.OnPlayerQuit)
	# 	self.RegisterRpcMethod(serviceConsts.ModName, 'service_test',
	# 			self.OnTest)#for yfgtest
	#
	# def OnTest(self, serverId, callbackId, args):#yfgtest
	# 	for uid in self.mPlayer2ServerId.iterkeys():
	# 		print 'GetPlayerApplyTime', self.GetPlayerApplyTime(uid, 3)
	# 		print 'GetApppliedActivityList', self.GetApppliedActivityList(uid)
	# 		print 'GetApppliedActivityList', self.GetAppliedUIDs(3)

	def OnPlayerEnter(self, serverId, callbackId, args):
		uid = args['uid']
		self.mPlayer2ServerId[uid] = serverId

	def OnPlayerQuit(self, serverId, callbackId, args):
		uid = args['uid']
		if uid in self.mPlayer2ServerId:
			del self.mPlayer2ServerId[uid]

	def GetPlayerServerId(self, uid):
		return self.mPlayer2ServerId.get(uid, None)

	def Update(self):
		self.mActivityManager.Update()

	def Destroy(self):
		apiUtil.Destroy()
		self.mActivityManager.Destroy()
		self.mActivityManager = None

	def GetPlayerApplyTime(self, uid, activityId):
		'''
		获得某玩家的报名某活动的开始报名时间。-1表示没有报名活动
		'''
		return self.mActivityManager.GetPlayerApplyTime(uid, activityId)

	def GetAppliedUIDs(self, activityId):
		'''
		获得某活动的报名队列
		'''
		return self.mActivityManager.GetAppliedUIDs(activityId)

	def GetApppliedActivityList(self, uid):
		'''
		获得某玩家报名的活动
		'''
		return self.mActivityManager.GetApppliedActivityList(uid)