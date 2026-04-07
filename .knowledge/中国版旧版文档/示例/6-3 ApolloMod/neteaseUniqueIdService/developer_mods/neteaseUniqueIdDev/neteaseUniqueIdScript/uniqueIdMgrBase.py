# -*- coding: utf-8 -*-
#
import weakref
import logout
import neteaseUniqueIdScript.uniqueIdConsts as uniqueIdConsts
from neteaseUniqueIdScript.uniqueIdConsts import UniqueIdEvent
#---------------------------------------------------------------------------------
# 唯一ID模块具体逻辑实现的基类
# 注册事件，返回结果等过程都在基类中实现
# 保留部分需要数据库行为支持的函数，在具体的子类中实现
class CUniqueIdMgr(object):
	def __init__(self, system, modulName):
		super(CUniqueIdMgr, self).__init__()
		self.mSystem = weakref.proxy(system)
		self.mModuleName = modulName
		# 注册【neteaseUniqueId】事件的响应函数
		# 所有lobby/game发送的【neteaseUniqueId】事件都由此函数处理
		self.mSystem.RegisterRpcMethod(modulName, UniqueIdEvent.AskNew, self.OnUniqueidAskNew)
		# service启动时需要从数据库读取历史数据，没有读取成功前，是否无法提供服务的
		self.mModuleReady = False
		# 内存中的缓存数据
		self.mUniqueIdMap = {}
		# 正在等待数据库调用返回，尚未返回结果的请求
		self.mQueryingRequests = {}
		
	def Destroy(self):
		self.mSystem = None
	#-----------------------------------------------------------------------------------------------
	# 需要重载实现的函数
	# 插入一条新的keyword记录
	# 当一个keyword第一次申请唯一ID时，会触发数据库insert新记录
	def InsertKeyword(self, keyword, requireNum):
		pass

	# 更新数据库中，指定keyword的，当前已经用到的最大唯一ID的值
	def RequireMoreKeyword(self, keyword, cacheData, requireNum):
		pass
	#-----------------------------------------------------------------------------------------------
	# 数据库请求完毕后，需要调用这个函数更新内存中的记录数据
	def UpdateMemoryCache(self, keyword, plusSize, dbMaxId, useMaxId=None):
		# plusSize代表一次数据库请求申请多少个唯一ID
		# dbMaxId代表数据库中最大唯一ID
		# useMaxId代表当前已经发放出去的最大唯一ID
		if self.mUniqueIdMap.has_key(keyword):
			self.mUniqueIdMap[keyword]['plusSize'] = plusSize
			self.mUniqueIdMap[keyword]['dbMaxId'] = dbMaxId
			if not useMaxId is None:
				self.mUniqueIdMap[keyword]['useMaxId'] = useMaxId
		else:
			self.mUniqueIdMap[keyword] = {
				"keyword": keyword,
				"plusSize": plusSize,
				"dbMaxId": dbMaxId,
			}
			if useMaxId is None:
				self.mUniqueIdMap[keyword]['useMaxId'] = dbMaxId
			else:
				self.mUniqueIdMap[keyword]['useMaxId'] = useMaxId
	
	# 申请唯一ID失败，只返回一个代表reason的message
	def MakeFailResponse(self, serverId, callbackId, code):
		eventData = {
			"code": code,
			"message": uniqueIdConsts.ErrorText.get(code, "未知错误"),
		}
		self.mSystem.ResponseToServer(serverId, callbackId, eventData)
		logout.info("[UniqueIdServiceSystem] response fail code=%s"%code)

	# 申请唯一ID成功，返回
	# startId 可用的唯一ID的第一个（包括start_id）
	# endId 可用的唯一ID的最后一个（包括end_id）
	def MakeSuccessResponse(self, serverId, callbackId, keyword, requireNum, startId, endId):
		eventData = {
			"code": uniqueIdConsts.CodeSuc,
			"message": uniqueIdConsts.ErrorText[uniqueIdConsts.CodeSuc],
			"keyword": keyword,
			"requireNum": requireNum,
			"startId": startId,
			"endId": endId,
		}
		self.mSystem.ResponseToServer(serverId, callbackId, eventData)
		logout.info("[UniqueIdServiceSystem] response suc keyword=%s requireNum=%s startId=%s endId=%s"%(keyword,requireNum,startId,endId))
	#-----------------------------------------------------------------------------------------------
	# 申请唯一ID的请求事件处理函数
	# serverId：发送请求的lobby/game的进程ID
	# callbackId：发送的请求的唯一index，用去区分多个不同的申请请求
	# args['keyword']：申请唯一ID的关键字，用于类型区分
	# args['requireNum']：申请唯一ID的个数，建议使用时一次申请多个，而不是用一个申请一个，避免请求过于频繁
	def OnUniqueidAskNew(self, serverId, callbackId, args):
		logout.verbose("[UniqueIdServiceSystem] OnRequireUniqueid args=%s"%str(args))
		# 初始化是否完成的检查
		if not self.mModuleReady:
			self.MakeFailResponse(serverId, callbackId, uniqueIdConsts.CodeAskNewNotReady)
			return
		# 请求的参数是否正确的检查
		keyword = args.get("keyword", None)
		requireNum = args.get("requireNum", None)
		if not keyword:
			self.MakeFailResponse(serverId, callbackId, uniqueIdConsts.CodeAskNewEmptyKeyWord)
			return
		if not requireNum:
			self.MakeFailResponse(serverId, callbackId, uniqueIdConsts.CodeAskNewEmptyNum)
			return
		try:
			requireNum = int(requireNum)
		except:
			self.MakeFailResponse(serverId, callbackId, uniqueIdConsts.CodeAskNewWrongNum)
			return
		if requireNum <= 0:
			self.MakeFailResponse(serverId, callbackId, uniqueIdConsts.CodeAskNewWrongNum)
			return
		# 已经有排队任务了
		# 任务直接放到排队任务的最后
		# 等待数据库操作返回之后再处理
		if self.mQueryingRequests.has_key(keyword):
			self.mQueryingRequests[keyword].append((serverId, callbackId, requireNum))
			return
		data = self.mUniqueIdMap.get(keyword, None)
		# 某个keyword首次申请uniqueId
		# 创建一个新的排队任务队列
		# 触发数据库插入操作
		if data is None:
			self.mQueryingRequests[keyword] = []
			self.mQueryingRequests[keyword].append((serverId, callbackId, requireNum))
			# print "empty keyword need insert"
			self.InsertKeyword(keyword, requireNum)
			return
		# 剩余可用的id小于require，那么还是要query
		if (data["dbMaxId"] - data["useMaxId"]) < requireNum:
			self.mQueryingRequests[keyword] = []
			self.mQueryingRequests[keyword].append((serverId, callbackId, requireNum))
			# print "not enough keyword need more"
			self.RequireMoreKeyword(keyword, data, requireNum)
			return
		# 剩余可用的id够用，直接返回了
		startId = data["useMaxId"] + 1
		data["useMaxId"] = data["useMaxId"] + requireNum
		self.MakeSuccessResponse(serverId, callbackId, keyword, requireNum, startId, data["useMaxId"])
	
	# 数据库请求失败
	# 遍历请求列表，全部返回失败
	def OnMakeUniqueIdFailed(self, keyword, code):
		requestList = self.mQueryingRequests.get(keyword, None)
		if requestList is None:
			return
		del self.mQueryingRequests[keyword]
		for cachedData in requestList:
			serverId, callbackId, requireNum = cachedData
			self.MakeFailResponse(serverId, callbackId, code)
	
	# 数据库请求成功
	# 按照请求的先后顺序，返回可用的唯一ID
	# 假如从数据库成功申请的唯一ID依旧不够满足全部的请求
	# 那么再次触发从数据库申请唯一ID的函数
	def OnMakeUniqueIdSuccess(self, keyword):
		# 假如已经没有待处理的请求了，直接return
		requestList = self.mQueryingRequests.get(keyword, None)
		if requestList is None:
			return
		# 获取keyword对应的内存cache
		# 数据库请求返回时第一时间更新内存
		data = self.mUniqueIdMap[keyword]
		# 按照请求的先后顺序一一处理
		# 直到请求列表被清空
		while requestList:
			# 当前成功申请的唯一ID不够满足请求总数，则退出循环
			serverId, callbackId, requireNum = requestList[0]
			if (data['dbMaxId'] - data['useMaxId']) < requireNum:
				break
			# 满足请求总数，则成功返回
			start_id = data['useMaxId'] + 1
			data['useMaxId'] = data['useMaxId'] + requireNum
			self.MakeSuccessResponse(serverId, callbackId, keyword, requireNum, start_id, data['useMaxId'])
			# 请求被成功处理后，从请求列表中清除
			requestList.pop(0)
		# 如果请求尚未处理完，那么需要再次向数据库申请
		if requestList:
			serverId, callbackId, requireNum = requestList[0]
			# print "not enough keyword by update once"
			self.RequireMoreKeyword(keyword, data, requireNum)
		# 如果请求处理完了，删除请求列表
		else:
			del self.mQueryingRequests[keyword]


		



