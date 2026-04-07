# -*- coding: utf-8 -*-
#
import time
import weakref
import json
#
import apolloCommon.commonNetgameApi as commonNetgameApi
import logout
import apolloCommon.mysqlPool as mysqlPool
import apolloCommon.redisPool as redisPool
import neteaseAnnounceScript.announceConsts as announceConsts
import neteaseAnnounceScript.timermanager as timermanager
from neteaseAnnounceScript.announceConsts import LoginPopupEvent, FloatingWindowEvent, MailEvent
import neteaseAnnounceScript.apiUtil as apiUtil
#---------------------------------------------------------------------------------
class AnnounceMgr(object):
	def __init__(self, system, moduleName):
		super(AnnounceMgr, self).__init__()
		self.mSystem = weakref.proxy(system)
		self.mModuleName = moduleName
		# 登录弹窗
		self.mLoginPopupList = []
		self.mLoginPopupVersion = None
		self.QueryLoginPopup()
		self.mSystem.RegisterRpcMethod(moduleName, LoginPopupEvent.New, self.OnLoginPopupNew)
		self.mSystem.RegisterRpcMethod(moduleName, LoginPopupEvent.Del, self.OnLoginPopupDel)
		self.mSystem.RegisterRpcMethod(moduleName, LoginPopupEvent.View, self.OnLoginPopupView)
		self.mSystem.RegisterRpcMethod(moduleName, LoginPopupEvent.Clean, self.OnLoginPopupClean)
		self.mSystem.RegisterRpcMethod(moduleName, LoginPopupEvent.AskNew, self.OnLoginPopupAskNew)
		# 浮窗公告
		self.mFloatingWindowList = []
		self.mFloatingWindowVersion = None
		self.QueryFloatingWindow()
		self.mSystem.RegisterRpcMethod(moduleName, FloatingWindowEvent.New, self.OnFloatWinNew)
		self.mSystem.RegisterRpcMethod(moduleName, FloatingWindowEvent.Del, self.OnFloatWinDel)
		self.mSystem.RegisterRpcMethod(moduleName, FloatingWindowEvent.View, self.OnFloatWinView)
		self.mSystem.RegisterRpcMethod(moduleName, FloatingWindowEvent.Clean, self.OnFloatWinClean)
		self.mSystem.RegisterRpcMethod(moduleName, FloatingWindowEvent.AskNew, self.OnFloatWinAskNew)
		# 全局邮件
		self.mGroupMailList = []
		self.mGroupMailsVersion = None
		self.QueryGroupMails()
		self.mMailBonusLock = {}
		self.mSystem.RegisterRpcMethod(moduleName, MailEvent.SendToSingle, self.OnMailSendToSingle)
		self.mSystem.RegisterRpcMethod(moduleName, MailEvent.SendToMany, self.OnMailSendToMany)
		self.mSystem.RegisterRpcMethod(moduleName, MailEvent.SendToGroup, self.OnMailSendToGroup)
		self.mSystem.RegisterRpcMethod(moduleName, MailEvent.RegUser, self.OnMailRegUser)
		self.mSystem.RegisterRpcMethod(moduleName, MailEvent.GetMailList, self.OnMailGetList)
		self.mSystem.RegisterRpcMethod(moduleName, MailEvent.SetRead, self.OnMailSetRead)
		self.mSystem.RegisterRpcMethod(moduleName, MailEvent.GetBonus, self.OnMailGetBonus)
		self.mSystem.RegisterRpcMethod(moduleName, MailEvent.ReleaseLock, self.OnMailReleaseLock)
		self.mSystem.RegisterRpcMethod(moduleName, MailEvent.DelFixMail, self.OnMailDelFix)
		self.mSystem.RegisterRpcMethod(moduleName, MailEvent.CleanMail, self.OnMailCleanNouse)
		self.mSystem.RegisterRpcMethod(moduleName, MailEvent.CheckHasUnread, self.OnCheckHasUnread)
		self.mDelExpireTimer = timermanager.timerManager.addRepeatTimer(announceConsts.MailDelExpireInterval, self.DoMailDelExpire)
		logout.info("CREATE_MANAGER_SUCCESS moduleName=%s" % moduleName)

	def Destroy(self):
		if self.mDelExpireTimer:
			timermanager.timerManager.delTimer(self.mDelExpireTimer)
			self.mDelExpireTimer = None
		self.mSystem = None
	# -------------------------------------------------------------------------------------
	# 拉取尚未过期的登录弹窗记录，并缓存到内存
	def QueryLoginPopup(self):
		now = int(time.time())
		sql = "SELECT _id, title, content, pic, priority, beginTime, endTime FROM %s " % announceConsts.TableLoginPopup
		sql += "WHERE endTime > %s"
		params = (now,)
		callback = lambda records: self.QueryLoginPopupCallback(records)
		mysqlPool.AsyncQueryWithOrderKey("initQuery", sql, params, callback)

	def QueryLoginPopupCallback(self, records):
		if records is None:
			logout.error("QueryLoginPopup on init fail by database")
			return
		if records:
			for one in records:
				one = apiUtil.UnicodeConvert(one)
				data = {
					"_id": one[0],
					"title": one[1],
					"content": one[2],
					"pic": one[3],
					"priority": one[4],
					"beginTime": one[5],
					"endTime": one[6],
				}
				self.mLoginPopupList.append(data)
		self.mLoginPopupList.sort(apiUtil.SortById)
		self.mLoginPopupVersion = int(time.time())
		for _dict in self.mLoginPopupList:
			print "_id=%s title=%s" % (_dict["_id"], _dict["title"])

	# 拉取尚未过期的浮窗公告记录，并缓存到内存
	def QueryFloatingWindow(self):
		now = int(time.time())
		sql = "SELECT _id, content, displayTime, lobbyShow, gameShow, beginTime, endTime FROM %s " % announceConsts.TableFloatingWindow
		sql += "WHERE endTime > %s"
		params = (now,)
		callback = lambda records: self.QueryFloatingWindowCallback(records)
		mysqlPool.AsyncQueryWithOrderKey("initQuery", sql, params, callback)

	def QueryFloatingWindowCallback(self, records):
		if records is None:
			logout.error("QueryFloatingWindow on init fail by database")
			return
		if records:
			for one in records:
				one = apiUtil.UnicodeConvert(one)
				data = {
					"_id": one[0],
					"content": one[1],
					"displayTime": one[2],
					"lobbyShow": one[3],
					"gameShow": one[4],
					"beginTime": one[5],
					"endTime": one[6],
				}
				self.mFloatingWindowList.append(data)
		self.mFloatingWindowList.sort(apiUtil.SortById)
		self.mFloatingWindowVersion = int(time.time())
		for _dict in self.mFloatingWindowList:
			print "_id=%s content=%s" % (_dict["_id"], _dict["content"][:10])

	# 拉取尚未过期的群发邮件记录，并缓存到内存
	def QueryGroupMails(self):
		now = int(time.time())
		sql = "SELECT _id, effectTime, title, content, itemList, cTime, expire, srcName FROM %s " % announceConsts.TableGroupMail
		sql += "WHERE expire > %s"
		params = (now,)
		callback = lambda records: self.QueryGroupMailsCallback(records)
		mysqlPool.AsyncQueryWithOrderKey("initQuery", sql, params, callback)

	def QueryGroupMailsCallback(self, records):
		if records is None:
			logout.error("QueryGroupMails on init fail by database")
			return
		if records:
			for one in records:
				one = apiUtil.UnicodeConvert(one)
				data = {
					"_id": one[0],
					"effectTime": one[1],
					"title": one[2],
					"content": one[3],
					"itemList": apiUtil.UnicodeConvert(json.loads(one[4])),
					"cTime": one[5],
					"expire": one[6],
					"srcName": one[7],
				}
				self.mGroupMailList.append(data)
		self.mGroupMailList.sort(apiUtil.SortByIdReverse)
		self.mGroupMailsVersion = int(time.time())
		for _dict in self.mGroupMailList:
			print "_id=%s title=%s items=%s" % (_dict["_id"], _dict["title"], _dict["itemList"])

	# ------------------------------------------------------------------------------------
	# 通用请求返回
	def ResponseSingle(self, serverId, callbackId, code, entity=None):
		if serverId is None:
			return
		eventData = {
			"code": code,
			"message": announceConsts.ErrorText.get(code, "未知错误"),
			"entity": entity,
		}
		self.mSystem.ResponseToServer(serverId, callbackId, eventData)

	def ResponseMany(self, serverId, callbackId, code, entityList=[]):
		eventData = {
			"code": code,
			"message": announceConsts.ErrorText.get(code, "未知错误"),
			"entities": entityList,
		}
		self.mSystem.ResponseToServer(serverId, callbackId, eventData)
	# -------------------------------------------------------------------------------------
	# 登录弹窗相关请求
	# 遍历内存缓存中的登录弹窗记录，删除已经过期的记录
	def InspectLoginPopupCache(self):
		now = int(time.time())
		delCount = 0
		for idx, data in enumerate(self.mLoginPopupList):
			if data["endTime"] <= now:
				self.mLoginPopupList[idx] = None
				delCount += 1
		for i in xrange(delCount):
			self.mLoginPopupList.remove(None)
		if delCount > 0:
			self.mLoginPopupVersion = now
			self.DeleteExpiredLoginPopup(now)

	# 删除数据库里过期的登录弹窗记录
	def DeleteExpiredLoginPopup(self, now):
		sql = "DELETE FROM %s " % announceConsts.TableLoginPopup
		sql += "WHERE endTime <= %s"
		params = (now,)
		callback = lambda suc: self.DeleteExpiredLoginPopupCallback(suc)
		mysqlPool.AsyncExecuteWithOrderKey("login", sql, params, callback)

	def DeleteExpiredLoginPopupCallback(self, suc):
		if not suc:
			logout.error("DeleteExpiredLoginPopup fail by database error")

	# 向所有服务器进程广播登录弹窗记录列表
	def BroadcastLoginPopupData(self):
		from service.serviceConf import serverListMap
		event = LoginPopupEvent.SyncData
		eventData = {
			"version": self.mLoginPopupVersion,
			"dataList": self.mLoginPopupList,
		}
		for serverId, conf in serverListMap.iteritems():
			svrType = conf.get("type", "empty")
			if svrType == "proxy":
				continue
			self.mSystem.NotifyToServerNode(serverId, event, eventData)

	# 新建登录弹窗，步骤：
	# 1、检查传入参数，组织信息
	# 2、把新记录插入数据库，从数据库回调中获取新记录的唯一ID
	# 3、返回请求方，新建登录弹窗成功
	# 4、更新本地内存缓存中的登录弹窗记录列表
	# 5、向所有在线的服务器进程广播登录弹窗记录变化的事件
	def OnLoginPopupNew(self, serverId, callbackId, args):
		title = args.get("title", None)
		content = args.get("content", None)
		if not title or not content:
			self.ResponseSingle(serverId, callbackId, announceConsts.CodeLoginEmptyParam)
			return
		if apiUtil.CheckInputOverLimit(title, announceConsts.LoginPopupTitleLimit) or apiUtil.CheckInputOverLimit(content, announceConsts.LoginPopupContentLimit):
			self.ResponseSingle(serverId, callbackId, announceConsts.CodeLoginTextOverLimit)
			return
		pic = args.get("pic", "")
		now = int(time.time())
		priority = args.get("priority", 1)
		beginTime = apiUtil.MakeTime(args, "beginTime", now)
		endTime = apiUtil.MakeTime(args, "endTime", beginTime + announceConsts.LoginPopExpire)
		if beginTime >= endTime:
			self.ResponseSingle(serverId, callbackId, announceConsts.CodeLoginWrongParam)
			return
		data = {
			"title": title,
			"content": content,
			"pic": pic,
			"priority": priority,
			"beginTime": beginTime,
			"beginTimeStr": time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(beginTime)),
			"endTime": endTime,
			"endTimeStr": time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(endTime)),
		}
		sql = "INSERT INTO %s (title, content, pic, priority, beginTime, endTime) " % announceConsts.TableLoginPopup
		sql += "VALUES (%s, %s, %s, %s, %s, %s)"
		params = (title, content, pic, priority, beginTime, endTime)
		callback = lambda newId: self.InsertLoginPopupCallback(newId, serverId, callbackId, data)
		mysqlPool.AsyncInsertOneWithOrderKey("login", sql, params, callback)

	def InsertLoginPopupCallback(self, newId, serverId, callbackId, data):
		if not newId:
			logout.error("InsertLoginPopupFail detail=%s" % str(data))
			self.ResponseSingle(serverId, callbackId, announceConsts.CodeLoginDatabaseFail)
			return
		data["_id"] = newId
		self.ResponseSingle(serverId, callbackId, announceConsts.CodeSuc, data)
		# 更新本地缓存
		self.mLoginPopupList.append(data)
		self.mLoginPopupVersion = int(time.time())
		# 通知全部的server，登录弹窗更新了
		self.BroadcastLoginPopupData()

	# 删除登录弹窗，步骤：
	# 1、检查传入参数，组织信息
	# 2、从数据库中删除指定Id的记录
	# 3、从本地内存缓存中删除指定Id的记录
	# 4、返回给请求方请求的结果
	def OnLoginPopupDel(self, serverId, callbackId, args):
		_id = args.get("_id", None)
		if not _id:
			self.ResponseSingle(serverId, callbackId, announceConsts.CodeLoginDelEmptyParam)
			return
		sql = "DELETE FROM %s " % announceConsts.TableLoginPopup
		sql += "WHERE _id=%s"
		params = (_id,)
		callback = lambda suc: self.DeleteLoginPopupCallback(suc, serverId, callbackId, _id)
		mysqlPool.AsyncExecuteWithOrderKey("login", sql, params, callback)

	def DeleteLoginPopupCallback(self, suc, serverId, callbackId, _id):
		logout.info("DeleteLoginPopup _id=%s ret=%s" % (_id, str(suc)))
		# 更新本地缓存
		find = None
		for idx, data in enumerate(self.mLoginPopupList):
			if data["_id"] == _id:
				find = data
				self.mLoginPopupList[idx] = None
				break
		# 通知全部的server，登录弹窗更新了
		# 没找到就不需要同步了
		if find:
			self.mLoginPopupList.remove(None)
			self.mLoginPopupVersion = int(time.time())
			self.BroadcastLoginPopupData()
			self.ResponseSingle(serverId, callbackId, announceConsts.CodeSuc, find)
		else:
			self.ResponseSingle(serverId, callbackId, announceConsts.CodeLoginDelEmptyRecord)

	def ResponseLoginPopupList(self, serverId, callbackId):
		entity = {
			"version": self.mLoginPopupVersion,
			"dataList": self.mLoginPopupList,
		}
		self.ResponseSingle(serverId, callbackId, announceConsts.CodeSuc, entity)

	# 获取当前尚未过期的登录弹窗记录列表
	def OnLoginPopupView(self, serverId, callbackId, args):
		# 内存缓存中清理一下已经过期的弹窗
		self.InspectLoginPopupCache()
		self.ResponseLoginPopupList(serverId, callbackId)

	# 清空全部登录弹窗列表
	def OnLoginPopupClean(self, serverId, callbackId, args):
		sql = "DELETE FROM %s" % announceConsts.TableLoginPopup
		params = ()
		callback = lambda suc: self.CleanLoginPopupCallback(suc, serverId, callbackId)
		mysqlPool.AsyncExecuteWithOrderKey("login", sql, params, callback)

	def CleanLoginPopupCallback(self, suc, serverId, callbackId):
		if not suc:
			logout.error("CleanLoginPopup fail ret=%s" % str(suc))
			self.ResponseSingle(serverId, callbackId, announceConsts.CodeLoginCleanDabaseFail)
			return
		logout.info("CleanLoginPopup success")
		self.InspectLoginPopupCache()
		self.ResponseLoginPopupList(serverId, callbackId)
		# 通知全部的server，登录弹窗更新了
		# 前提是当前确实有生效的登录弹窗
		if self.mLoginPopupList:
			self.mLoginPopupList = []
			self.mLoginPopupVersion = int(time.time())
			self.BroadcastLoginPopupData()

	# lobby/game进程定时发送的请求
	# 比较版本后，只给版本较旧的返回最新版本的登录弹窗信息
	# 主要是为了处理网络断开，进程dump等意外导致的信息同步丢失问题
	def OnLoginPopupAskNew(self, serverId, callbackId, args):
		if self.mLoginPopupVersion is None:
			self.ResponseSingle(serverId, callbackId, announceConsts.CodeLoginAskNewNotInited)
			return
		version = args.get("version", 0)
		if self.mLoginPopupVersion <= version:
			self.ResponseSingle(serverId, callbackId, announceConsts.CodeLoginAskNewSame)
			return
		self.ResponseLoginPopupList(serverId, callbackId)
	# --------------------------------------------------------------------------------------
	# 浮窗公告
	# 遍历内存缓存中的浮窗公告记录，删除已经过期的记录
	def InspectFloatingWindowCache(self):
		now = int(time.time())
		delCount = 0
		for idx, data in enumerate(self.mFloatingWindowList):
			if data["endTime"] <= now:
				self.mFloatingWindowList[idx] = None
				delCount += 1
		for i in xrange(delCount):
			self.mFloatingWindowList.remove(None)
		if delCount > 0:
			self.mFloatingWindowVersion = now
			self.DeleteExpiredFloatingWindow(now)

	# 从数据库中删除过期的浮窗公告记录
	def DeleteExpiredFloatingWindow(self, now):
		sql = "DELETE FROM %s " % announceConsts.TableFloatingWindow
		sql += "WHERE endTime <= %s"
		params = (now,)
		callback = lambda suc: self.DeleteExpiredFloatingWindowCallback(suc)
		mysqlPool.AsyncExecuteWithOrderKey("floating", sql, params, callback)

	def DeleteExpiredFloatingWindowCallback(self, suc):
		if not suc:
			logout.error("DeleteExpiredFloatingWindow fail by database error")

	# 向服务器广播当前的浮窗公告记录列表
	def BroadcastFloatingWindowData(self, toLobby=True, toGame=True):
		from service.serviceConf import serverListMap
		event = FloatingWindowEvent.SyncData
		eventData = {
			"version": self.mFloatingWindowVersion,
			"dataList": self.mFloatingWindowList,
		}
		for serverId, conf in serverListMap.iteritems():
			svrType = conf.get("type", "empty")
			if toLobby and svrType == "lobby":
				self.mSystem.NotifyToServerNode(serverId, event, eventData)
			elif toGame and svrType not in ("lobby", "proxy"):
				self.mSystem.NotifyToServerNode(serverId, event, eventData)

	# 新建浮窗公告，步骤：
	# 1、检查传入参数，组织信息
	# 2、把新记录插入数据库，从数据库回调中获取新记录的唯一ID
	# 3、返回请求方，新建登录弹窗成功
	# 4、更新本地内存缓存中的登录弹窗记录列表
	# 5、向所有在线的服务器进程广播浮窗公告列表变化的事件
	def OnFloatWinNew(self, serverId, callbackId, args):
		content = args.get("content", None)
		displayTime = args.get("displayTime", None)
		if not content or not displayTime:
			self.ResponseSingle(serverId, callbackId, announceConsts.CodeFloatingEmptyParam)
			return
		if type(displayTime) != int or displayTime <= 0:
			self.ResponseSingle(serverId, callbackId, announceConsts.CodeFloatingDisplayWrong)
			return
		if apiUtil.CheckInputOverLimit(content, announceConsts.FloatWinContentLimit):
			self.ResponseSingle(serverId, callbackId, announceConsts.CodeFloatingTextOverLimit)
			return
		lobbyShow = args.get("lobbyShow", None)
		if lobbyShow:
			lobbyShow = 1
		else:
			lobbyShow = 0
		gameShow = args.get("gameShow", None)
		if gameShow:
			gameShow = 1
		else:
			gameShow = 0
		if (not lobbyShow) and (not gameShow):
			self.ResponseSingle(serverId, callbackId, announceConsts.CodeFloatingEmptyDisplay)
			return
		now = int(time.time())
		beginTime = apiUtil.MakeTime(args, "beginTime", now)
		if displayTime >= announceConsts.FloatWinExpire:
			expire = displayTime * announceConsts.FloatWinExpireFactor
		else:
			expire = announceConsts.FloatWinExpire
		endTime = apiUtil.MakeTime(args, "endTime", beginTime+expire)
		if beginTime >= endTime:
			self.ResponseSingle(serverId, callbackId, announceConsts.CodeFloatingWrongParam)
			return
		data = {
			"content": content,
			"displayTime": displayTime,
			"lobbyShow": lobbyShow,
			"gameShow": gameShow,
			"beginTime": beginTime,
			"beginTimeStr": time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(beginTime)),
			"endTime": endTime,
			"endTimeStr": time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(endTime)),
		}
		sql = "INSERT INTO %s (content, displayTime, lobbyShow, gameShow, beginTime, endTime) " % announceConsts.TableFloatingWindow
		sql += "VALUES (%s, %s, %s, %s, %s, %s)"
		params = (content, displayTime, lobbyShow, gameShow, beginTime, endTime)
		callback = lambda newId: self.InsertFloatingWindowCallback(newId, serverId, callbackId, data)
		mysqlPool.AsyncInsertOneWithOrderKey("floating", sql, params, callback)

	def InsertFloatingWindowCallback(self, newId, serverId, callbackId, data):
		if not newId:
			logout.error("InsertFloatingWindowFail detail=%s" % str(data))
			return
		data["_id"] = newId
		self.ResponseSingle(serverId, callbackId, announceConsts.CodeSuc, data)
		# 更新本地缓存
		self.mFloatingWindowList.append(data)
		self.mFloatingWindowVersion = int(time.time())
		# 通知全部的server，登录弹窗更新了
		# 新增的情况，只有需要弹出的对应类型服务器，才需要被同步
		self.BroadcastFloatingWindowData(data["lobbyShow"], data["gameShow"])

	# 删除指定Id的公告
	def OnFloatWinDel(self, serverId, callbackId, args):
		_id = args.get("_id", None)
		if not _id:
			self.ResponseSingle(serverId, callbackId, announceConsts.CodeFloatingDelEmptyParam)
			return
		sql = "DELETE FROM %s " % announceConsts.TableFloatingWindow
		sql += "WHERE _id=%s"
		params = (_id,)
		callback = lambda suc: self.DeleteFloatWinCallback(suc, serverId, callbackId, _id)
		mysqlPool.AsyncExecuteWithOrderKey("floating", sql, params, callback)

	def DeleteFloatWinCallback(self, suc, serverId, callbackId, _id):
		logout.info("DeleteFloatWin _id=%s ret=%s" % (_id, str(suc)))
		# 更新本地缓存
		find = None
		for idx, data in enumerate(self.mFloatingWindowList):
			if data["_id"] == _id:
				find = data
				self.mFloatingWindowList[idx] = None
				break
		# 通知全部的server，浮窗公告更新了
		# 没找到就不需要同步了
		if find:
			self.mFloatingWindowList.remove(None)
			self.mFloatingWindowVersion = int(time.time())
			self.BroadcastFloatingWindowData(find["lobbyShow"], find["gameShow"])
			self.ResponseSingle(serverId, callbackId, announceConsts.CodeSuc, find)
		else:
			self.ResponseSingle(serverId, callbackId, announceConsts.CodeFloatingDelEmptyRecord)

	# 返回当前的浮窗公告的列表
	def ResponseFloatingWindowList(self, serverId, callbackId):
		entity = {
			"version": self.mFloatingWindowVersion,
			"dataList": self.mFloatingWindowList,
		}
		self.ResponseSingle(serverId, callbackId, announceConsts.CodeSuc, entity)

	# 返回当前尚未过期的浮窗公告的列表
	def OnFloatWinView(self, serverId, callbackId, args):
		self.InspectFloatingWindowCache()
		self.ResponseFloatingWindowList(serverId, callbackId)

	# 删除所有的浮窗公告， 步骤
	# 1、从数据库删除所有浮窗公告记录
	# 2、从内存缓存中删除全部的浮窗公告记录
	# 3、通知全部的lobby/game进程，删除浮窗公告记录
	def OnFloatWinClean(self, serverId, callbackId, args):
		sql = "DELETE FROM %s" % announceConsts.TableFloatingWindow
		params = ()
		callback = lambda suc: self.CleanFloatingWindowCallback(suc, serverId, callbackId)
		mysqlPool.AsyncExecuteWithOrderKey("floating", sql, params, callback)

	def CleanFloatingWindowCallback(self, suc, serverId, callbackId):
		if not suc:
			logout.error("CleanFloatingWindow fail ret=%s" % str(suc))
			self.ResponseSingle(serverId, callbackId, announceConsts.CodeFloatingCleanDabaseFail)
			return
		logout.info("CleanFloatingWindow success")
		self.InspectFloatingWindowCache()
		self.ResponseFloatingWindowList(serverId, callbackId)
		# 通知全部的server，浮窗公告更新了
		# 前提是当前确实有生效的登录弹窗
		if self.mFloatingWindowList:
			self.mFloatingWindowList = []
			self.mFloatingWindowVersion = int(time.time())
			self.BroadcastFloatingWindowData(True, True)

	# lobby/game进程定时发送的请求
	# 比较版本后，只给版本较旧的返回最新版本的公告信息
	# 主要是为了处理网络断开，进程dump等意外导致的信息同步丢失问题
	def OnFloatWinAskNew(self, serverId, callbackId, args):
		if self.mFloatingWindowVersion is None:
			self.ResponseSingle(serverId, callbackId, announceConsts.CodeFloatingAskNewNotInited)
			return
		version = args.get("version", 0)
		if self.mFloatingWindowVersion <= version:
			self.ResponseSingle(serverId, callbackId, announceConsts.CodeFloatingAskNewSame)
			return
		self.ResponseFloatingWindowList(serverId, callbackId)

	# -------------------------------------------------------------------------------------
	# 向指定uid单发一封邮件
	def OnMailSendToSingle(self, serverId, callbackId, args):
		uid = args.get("uid", None)
		if (not uid) or (type(uid) != int):
			self.ResponseSingle(serverId, callbackId, announceConsts.CodeMailNewEmptyParam)
			return
		self.DoMailSendToUser([uid, ], serverId, callbackId, args)

	# 向一组uid，各自单发一封邮件
	def OnMailSendToMany(self, serverId, callbackId, args):
		uidList = args.get("touids", None)
		if (not uidList) or (type(uidList) not in (list, tuple)):
			self.ResponseSingle(serverId, callbackId, announceConsts.CodeMailNewEmptyParam)
			return
		self.DoMailSendToUser(uidList, serverId, callbackId, args)
	
	def OutDoMailSendToUser(self, uidList, args):
		title = args.get("title", None)
		content = args.get("content", None)
		print "DoMailSendToUser", args
		if (not title) or (not content):
			return False
		if apiUtil.CheckInputOverLimit(title, announceConsts.MailTitleLimit) or apiUtil.CheckInputOverLimit(content, announceConsts.MailContentLimit):
			return False
		itemList = args.get("itemList", [])
		code, itemList = announceConsts.CheckMailItem(itemList)
		if code != announceConsts.CodeSuc:
			return False
		itemListStr = json.dumps(itemList)
		if len(itemListStr) >= announceConsts.MailItemListLengthLimit:
			return False
		now = int(time.time())
		cTime = now
		expire = apiUtil.MakeTime(args, "expire", now + announceConsts.MailExpire)
		if expire < announceConsts.MailExpireMax:
			expire = now + expire
		srcName = args.get("srcName", "")
		hasRead = 0
		if itemList:
			getBonus = 0
		else:
			getBonus = 1
		sql = "INSERT INTO %s (uid, title, content, itemList, cTime, expire, srcName, hasRead, getBonus) " % announceConsts.TableUserMail
		sql += "VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s)"
		mailContent = {
			"uidList": uidList,
			"title": title,
			"content": content,
			"itemList": itemList,
			"cTime": time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(cTime)),
			"expire": time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(expire)),
			"srcName": srcName,
			"hasRead": hasRead,
			"getBonus": getBonus,
		}
		if len(uidList) == 1:
			params = (uidList[0], title, content, itemListStr, cTime, expire, srcName, hasRead, getBonus)
			callback = lambda newId: self.InsertSingleMailCallback(newId, uidList[0], None, None, mailContent)
			mysqlPool.AsyncInsertOneWithOrderKey("mail%s" % uidList[0], sql, params, callback)
		else:
			paramsList = []
			for uid in uidList:
				paramsList.append((uid, title, content, itemListStr, cTime, expire, srcName, hasRead, getBonus))
			callback = lambda num: self.InsertManyMailCallback(num, uidList, None, None, mailContent)
			mysqlPool.AsyncExecutemanyWithOrderKey("mail", sql, paramsList, callback)
		return True

	# 单发邮件，步骤
	# 1、检查参数正确性和完整性
	# 2、根据目标uid列表的长度，选定insertOne还是insertMany，租住sql语句与参数
	# 3、sql执行完毕后，返回结果给请求方
	# 4、插入邮件成功，推送【有新邮件】事件给对应uid的用户客户端
	def DoMailSendToUser(self, uidList, serverId, callbackId, args):
		title = args.get("title", None)
		content = args.get("content", None)
		if (not title) or (not content):
			self.ResponseSingle(serverId, callbackId, announceConsts.CodeMailNewEmptyParam)
			return
		if apiUtil.CheckInputOverLimit(title, announceConsts.MailTitleLimit) or apiUtil.CheckInputOverLimit(content, announceConsts.MailContentLimit):
			self.ResponseSingle(serverId, callbackId, announceConsts.CodeMailNewTextOverLimit)
			return
		itemList = args.get("itemList", [])
		code, itemList = announceConsts.CheckMailItem(itemList)
		if code != announceConsts.CodeSuc:
			self.ResponseSingle(serverId, callbackId, code)
			return
		itemListStr = json.dumps(itemList)
		if len(itemListStr) >= announceConsts.MailItemListLengthLimit:
			self.ResponseSingle(serverId, callbackId, announceConsts.CodeMailAddItemListLengthLimit)
			return
		now = int(time.time())
		cTime = now
		expire = apiUtil.MakeTime(args, "expire", now+announceConsts.MailExpire)
		if expire < announceConsts.MailExpireMax:
			expire = now + expire
		srcName = args.get("srcName", "")
		hasRead = 0
		if itemList:
			getBonus = 0
		else:
			getBonus = 1
		sql = "INSERT INTO %s (uid, title, content, itemList, cTime, expire, srcName, hasRead, getBonus) " % announceConsts.TableUserMail
		sql += "VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s)"
		mailContent = {
			"uidList": uidList,
			"title": title,
			"content": content,
			"itemList": itemList,
			"cTime": time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(cTime)),
			"expire": time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(expire)),
			"srcName": srcName,
			"hasRead": hasRead,
			"getBonus": getBonus,
		}
		if len(uidList) == 1:
			params = (uidList[0], title, content, itemListStr, cTime, expire, srcName, hasRead, getBonus)
			callback = lambda newId:self.InsertSingleMailCallback(newId, uidList[0], serverId, callbackId, mailContent)
			mysqlPool.AsyncInsertOneWithOrderKey("mail%s"%uidList[0], sql, params, callback)
		else:
			paramsList = []
			for uid in uidList:
				paramsList.append((uid, title, content, itemListStr, cTime, expire, srcName, hasRead, getBonus))
			callback = lambda num:self.InsertManyMailCallback(num, uidList, serverId, callbackId, mailContent)
			mysqlPool.AsyncExecutemanyWithOrderKey("mail", sql, paramsList, callback)

	def InsertSingleMailCallback(self, newId, uid, serverId, callbackId, mailContent):
		if not newId:
			logout.error("InsertSingleMail fail data=%s"%str(mailContent))
			self.ResponseSingle(serverId, callbackId, announceConsts.CodeMailNewDatabaseFail)
			return
		mailContent["_id"] = newId
		self.ResponseSingle(serverId, callbackId, announceConsts.CodeSuc, mailContent)
		# 推送目标玩家，有新邮件了
		self.DoPushToUserClient(uid, MailEvent.NewMailArrive, {"group":False,})

	def InsertManyMailCallback(self, num, uidList, serverId, callbackId, mailContent):
		if not num:
			logout.error("InsertManyMail fail data=%s"%str(mailContent))
			self.ResponseSingle(serverId, callbackId, announceConsts.CodeMailNewDatabaseFail)
			return
		mailContent["number"] = num
		self.ResponseSingle(serverId, callbackId, announceConsts.CodeSuc, mailContent)
		# 推送目标玩家，有新邮件了
		for uid in uidList:
			self.DoPushToUserClient(uid, MailEvent.NewMailArrive, {"group":False,})

	def OutSendMailToGroup(self, title, content, itemList, effectTime, expire, srcName):
		if (not title) or (not content):
			return False
		code, itemList = announceConsts.CheckMailItem(itemList)
		if code != announceConsts.CodeSuc:
			return False
		itemListStr = json.dumps(itemList)
		if len(itemListStr) >= announceConsts.MailItemListLengthLimit:
			return False
		now = int(time.time())
		if effectTime is None:
			effectTime = now
		cTime = now
		if expire is None:
			expire = now + announceConsts.MailExpire
		if expire < announceConsts.MailExpireMax:
			expire = now + expire
		sql = "INSERT INTO %s (effectTime, title, content, itemList, cTime, expire, srcName) " % announceConsts.TableGroupMail
		sql += "VALUES (%s, %s, %s, %s, %s, %s, %s)"
		params = (effectTime, title, content, itemListStr, cTime, expire, srcName)
		data = {
			"effectTime": effectTime,
			"title": title,
			"content": content,
			"itemList": itemList,
			"cTime": cTime,
			"expire": expire,
			"srcName": srcName,
		}
		callback = lambda newId:self.OutInsertGroupMailCallback(newId, data)
		mysqlPool.AsyncInsertOneWithOrderKey("mailGroup", sql, params, callback)
	
	def OutInsertGroupMailCallback(self, newId, data):
		if not newId:
			logout.error("OutInsertGroupMailCallback fail data=%s"%str(data))
			return
		data["_id"] = newId
		# 更新内存缓存
		self.mGroupMailList.insert(0, data)
		self.mGroupMailsVersion = int(time.time())
		print "update group mail cache"
		for _dict in self.mGroupMailList:
			print "_id=%s title=%s items=%s" % (_dict["_id"], _dict["title"], _dict["itemList"])
		# 广播邮件更新了
		event = MailEvent.NewMailArrive
		eventData = {
			"group": True,
			"version": self.mGroupMailsVersion,
		}
		self.mSystem.RemoteBroadcastToClient(event, eventData)

	# 向全体用户群发邮件，步骤
	# 1、检查参数正确性和完整性
	# 2、组织sql语句与参数，执行insertOne
	# 3、sql请求成功后，返回结果给请求方
	# 4、更新本地内存缓存中的群邮件数据
	# 5、向当前全部的在线客户端广播【有新邮件】事件
	def OnMailSendToGroup(self, serverId, callbackId, args):
		title = args.get("title", None)
		content = args.get("content", None)
		if (not title) or (not content):
			self.ResponseSingle(serverId, callbackId, announceConsts.CodeMailGroupEmptyParam)
			return
		itemList = args.get("itemList", [])
		code, itemList = announceConsts.CheckMailItem(itemList)
		if code != announceConsts.CodeSuc:
			self.ResponseSingle(serverId, callbackId, code)
			return
		itemListStr = json.dumps(itemList)
		if len(itemListStr) >= announceConsts.MailItemListLengthLimit:
			self.ResponseSingle(serverId, callbackId, announceConsts.CodeMailAddItemListLengthLimit)
			return
		now = int(time.time())
		cTime = now
		effectTime = apiUtil.MakeTime(args, "effectTime", now)
		expire = apiUtil.MakeTime(args, "expire", now + announceConsts.MailExpire)
		if expire < announceConsts.MailExpireMax:
			expire = now + expire
		srcName = args.get("srcName", "")
		sql = "INSERT INTO %s (effectTime, title, content, itemList, cTime, expire, srcName) " % announceConsts.TableGroupMail
		sql += "VALUES (%s, %s, %s, %s, %s, %s, %s)"
		params = (effectTime, title, content, itemListStr, cTime, expire, srcName)
		data = {
			"effectTime": effectTime,
			"title": title,
			"content": content,
			"itemList": itemList,
			"cTime": cTime,
			"expire": expire,
			"srcName": srcName,
		}
		callback = lambda newId:self.InsertGroupMailCallback(newId, serverId, callbackId, data)
		mysqlPool.AsyncInsertOneWithOrderKey("mailGroup", sql, params, callback)

	def InsertGroupMailCallback(self, newId, serverId, callbackId, data):
		if not newId:
			logout.error("InsertGroupMail fail data=%s"%str(data))
			self.ResponseSingle(serverId, callbackId, announceConsts.CodeMailGroupDatabaseFail)
			return
		data["_id"] = newId
		mailContent = {
			"_id": newId,
			"effectTime": time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(data["effectTime"])),
			"title": data["title"],
			"content": data["content"],
			"itemList": data["itemList"],
			"cTime": time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(data["cTime"])),
			"expire": time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(data["expire"])),
			"srcName": data["srcName"],
		}
		self.ResponseSingle(serverId, callbackId, announceConsts.CodeSuc, mailContent)
		# 更新内存缓存
		self.mGroupMailList.insert(0, data)
		self.mGroupMailsVersion = int(time.time())
		print "update group mail cache"
		for _dict in self.mGroupMailList:
			print "_id=%s title=%s items=%s" % (_dict["_id"], _dict["title"], _dict["itemList"])
		# 广播邮件更新了
		event = MailEvent.NewMailArrive
		eventData = {
			"group": True,
			"version": self.mGroupMailsVersion,
		}
		self.mSystem.RemoteBroadcastToClient(event, eventData)

	# 注册新邮件用户，每次客户端登录都会调用
	def OnMailRegUser(self, serverId, callbackId, args):
		uid = args.get("uid", None)
		if not uid:
			self.ResponseSingle(serverId, callbackId, announceConsts.CodeMailRegEmptyParam)
			return
		sql = "SELECT lastGroupSync, version, cTime FROM %s " % announceConsts.TableMailUserProp
		sql += "WHERE uid=%s"
		params = (uid, )
		callback = lambda records:self.QueryPropByRegUserCallback(records, serverId, callbackId, uid)
		mysqlPool.AsyncQueryWithOrderKey("mail%s"%uid, sql, params, callback)

	def QueryPropByRegUserCallback(self, records, serverId, callbackId, uid):
		if records is None:
			logout.error("QueryPropByRegUser database fail uid=%s"%uid)
			self.ResponseSingle(serverId, callbackId, announceConsts.CodeMailRegDatabaseFail)
			return
		if records:
			data = {
				"uid": uid,
				"lastGroupSync": records[0][0],
				"version": records[0][1],
				"cTime": time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(records[0][2])),
			}
			self.ResponseSingle(serverId, callbackId, announceConsts.CodeSuc, data)
			return
		now = int(time.time())
		sql = "INSERT INTO %s (uid, lastGroupSync, version, cTime) " % announceConsts.TableMailUserProp
		sql += "VALUES (%s, %s, %s, %s)"
		params = (uid, 0, 1, now)
		data = {
			"uid": uid,
			"lastGroupSync": 0,
			"version": 1,
			"cTime": time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(now)),
		}
		callback = lambda suc:self.InsertMailUserPropCallback(suc, serverId, callbackId, data)
		mysqlPool.AsyncExecuteWithOrderKey("mail%s"%uid, sql, params, callback)

	def InsertMailUserPropCallback(self, suc, serverId, callbackId, data):
		if not suc:
			logout.error("InsertMailUserProp database fail data=%s"%str(data))
			self.ResponseSingle(serverId, callbackId, announceConsts.CodeMailRegDatabaseFail)
			return
		self.ResponseSingle(serverId, callbackId, announceConsts.CodeSuc, data)
	
	def OnCheckHasUnread(self, serverId, callbackId, args):
		uid = args.get("uid", None)
		# 第一步，query prop
		sql = "SELECT lastGroupSync, version, cTime FROM %s " % announceConsts.TableMailUserProp
		sql += "WHERE uid=%s"
		params = (uid,)
		callback = lambda records: self.QueryUnreadPropCallback(records, serverId, callbackId, uid)
		mysqlPool.AsyncQueryWithOrderKey("mail%s" % uid, sql, params, callback)
	
	def QueryUnreadPropCallback(self, records, serverId, callbackId, uid):
		if not records:
			eventData = {
				"suc": False,
				"hasUnread": None,
			}
			self.mSystem.ResponseToServer(serverId, callbackId, eventData)
			return
		lastGroupSync, version, cTime = records[0][0], records[0][1], records[0][2]
		now = int(time.time())
		newGroupSync = lastGroupSync
		paramsList = []
		for idx, mailContent in enumerate(self.mGroupMailList):
			# 已经过期了
			if mailContent["expire"] <= now:
				continue
			# 设置的起始时间之后建立的新号
			if mailContent["effectTime"] < cTime:
				continue
			# 已经完成转化的群邮件
			# 群邮件是严格按照id从大到小排序的，遇到第一封转化完毕的邮件，就说明之后的邮件都已经转化完毕了
			if mailContent["_id"] <= lastGroupSync:
				break
			newGroupSync = max(newGroupSync, mailContent["_id"])
			if mailContent["itemList"]:
				getBonus = 0
			else:
				getBonus = 1
			params = (uid, mailContent["title"], mailContent["content"], json.dumps(mailContent["itemList"]),
					  mailContent["cTime"], mailContent["expire"], mailContent["srcName"],
					  0, getBonus)
			paramsList.append(params)
		# 转化群邮件为个人邮件
		if paramsList:
			# 先升级同步版本
			sql = "UPDATE %s " % announceConsts.TableMailUserProp
			sql += "SET lastGroupSync=%s WHERE uid=%s AND lastGroupSync=%s"
			params = (newGroupSync, uid, lastGroupSync)
			callback = lambda suc:self.DoUnreadTransGroupToUser(suc, serverId, callbackId, uid, paramsList)
			mysqlPool.AsyncExecuteWithOrderKey("mail%s"%uid, sql, params, callback)
		# 假如没有群邮件需要转化，那么直接拉取邮件总数
		else:
			self.DoQueryUserUnreadMailCount(serverId, callbackId, uid)
	
	def DoUnreadTransGroupToUser(self, suc, serverId, callbackId, uid, paramsList):
		if not suc:
			eventData = {
				"suc": False,
				"hasUnread": None,
			}
			self.mSystem.ResponseToServer(serverId, callbackId, eventData)
			return
		sql = "INSERT INTO %s (uid, title, content, itemList, cTime, expire, srcName, hasRead, getBonus) " % announceConsts.TableUserMail
		sql += "VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s)"
		callback = lambda num:self.UnreadTransGroupToUserCallback(num, serverId, callbackId, uid, paramsList)
		mysqlPool.AsyncExecutemanyWithOrderKey("mail%s"%uid, sql, paramsList, callback)

	def UnreadTransGroupToUserCallback(self, num, serverId, callbackId, uid, paramsList):
		if not num:
			for params in paramsList:
				logout.error("TransGroupToUser fail params=%s" % str(params))
			eventData = {
				"suc": False,
				"hasUnread": None,
			}
			self.mSystem.ResponseToServer(serverId, callbackId, eventData)
			return
		eventData = {
			"suc": True,
			"hasUnread": True,
		}
		self.mSystem.ResponseToServer(serverId, callbackId, eventData)
	
	def DoQueryUserUnreadMailCount(self, serverId, callbackId, uid):
		sql = "SELECT COUNT(*) FROM %s " % announceConsts.TableUserMail
		sql += "WHERE uid=%s AND hasRead=0 AND expire>%s"
		params = (uid, int(time.time()))
		callback = lambda records:self.QueryUserUnreadMailCountCallback(records, serverId, callbackId, uid)
		mysqlPool.AsyncQueryWithOrderKey("mail%s"%uid, sql, params, callback)
	
	def QueryUserUnreadMailCountCallback(self, records, serverId, callbackId, uid):
		if records is None:
			eventData = {
				"suc": False,
				"hasUnread": None,
			}
			self.mSystem.ResponseToServer(serverId, callbackId, eventData)
			return
		number = records[0][0]
		if number > 0:
			hasUnread = True
		else:
			hasUnread = False
		eventData = {
			"suc": True,
			"hasUnread": hasUnread,
		}
		self.mSystem.ResponseToServer(serverId, callbackId, eventData)

	# 拉取邮件列表，分两种情况使用不同的步骤。
	# 情况1，从头开始拉邮件列表（mailId=0），步骤
	# 1、查询用户基本信息，获取用户首次登录时间，与群邮件的同步进度
	# 2、根据用户的首次登录时间与群邮件的同步进度，以及内存缓存中的群邮件信息，组织需要转化为个人邮件的群邮件
	# 3、把转化后的个人邮件，插入数据库中。
	# 4、查询当前用户尚未过期的个人邮件数量
	# 5、从_id最大的开始，拉取指定数量的个人邮件
	# 6、返回结果给请求方
	# 情况2，从指定_id的邮件开始，拉取接下来的N封邮件，步骤
	# 1、从_id小于请求中指定_id的邮件开始，按照_id从大到小拉取指定数量的邮件
	# 2、返回结果给请求方
	def OnMailGetList(self, serverId, callbackId, args):
		uid = args.get("uid", None)
		mailId = args.get("mailId", None)
		if uid is None or mailId is None:
			self.ResponseSingle(serverId, callbackId, announceConsts.CodeMailListEmptyParam)
			return
		# 从最新的邮件开始拉，需要考虑插入群邮件
		if mailId <= 0:
			self.DoQueryMailFromTop(serverId, callbackId, uid)
		else:
			self.DoQueryMailById(serverId, callbackId, uid, mailId)

	def DoQueryMailFromTop(self, serverId, callbackId, uid):
		# 第一步，query prop
		sql = "SELECT lastGroupSync, version, cTime FROM %s " % announceConsts.TableMailUserProp
		sql += "WHERE uid=%s"
		params = (uid,)
		callback = lambda records: self.QueryPropCallback(records, serverId, callbackId, uid)
		mysqlPool.AsyncQueryWithOrderKey("mail%s" % uid, sql, params, callback)

	def QueryPropCallback(self, records, serverId, callbackId, uid):
		if not records:
			logout.error("QueryProp when get maillist database fail uid=%s"%uid)
			self.ResponseSingle(serverId, callbackId, announceConsts.CodeMailListQueryUserDbFail)
			return
		lastGroupSync, version, cTime = records[0][0], records[0][1], records[0][2]
		now = int(time.time())
		newGroupSync = lastGroupSync
		paramsList = []
		for idx, mailContent in enumerate(self.mGroupMailList):
			# 已经过期了
			if mailContent["expire"] <= now:
				continue
			# 设置的起始时间之后建立的新号
			if mailContent["effectTime"] < cTime:
				continue
			# 已经完成转化的群邮件
			# 群邮件是严格按照id从大到小排序的，遇到第一封转化完毕的邮件，就说明之后的邮件都已经转化完毕了
			if mailContent["_id"] <= lastGroupSync:
				break
			newGroupSync = max(newGroupSync, mailContent["_id"])
			if mailContent["itemList"]:
				getBonus = 0
			else:
				getBonus = 1
			params = (uid, mailContent["title"], mailContent["content"], json.dumps(mailContent["itemList"]),
					  mailContent["cTime"], mailContent["expire"], mailContent["srcName"],
					  0, getBonus)
			paramsList.append(params)
		# 转化群邮件为个人邮件
		if paramsList:
			# 先升级同步版本
			sql = "UPDATE %s " % announceConsts.TableMailUserProp
			sql += "SET lastGroupSync=%s WHERE uid=%s AND lastGroupSync=%s"
			params = (newGroupSync, uid, lastGroupSync)
			callback = lambda suc:self.DoTransGroupToUser(suc, serverId, callbackId, uid, paramsList)
			mysqlPool.AsyncExecuteWithOrderKey("mail%s"%uid, sql, params, callback)
		# 假如没有群邮件需要转化，那么直接拉取邮件总数
		else:
			self.DoQueryUserMailCount(serverId, callbackId, uid)

	def DoTransGroupToUser(self, suc, serverId, callbackId, uid, paramsList):
		if not suc:
			logout.error("UpdateLastGroupSync fail for uid=%s"%uid)
			self.ResponseSingle(serverId, callbackId, announceConsts.CodeMailListUpdateSyncFail)
			return
		sql = "INSERT INTO %s (uid, title, content, itemList, cTime, expire, srcName, hasRead, getBonus) " % announceConsts.TableUserMail
		sql += "VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s)"
		callback = lambda num:self.TransGroupToUserCallback(num, serverId, callbackId, uid, paramsList)
		mysqlPool.AsyncExecutemanyWithOrderKey("mail%s"%uid, sql, paramsList, callback)

	def TransGroupToUserCallback(self, num, serverId, callbackId, uid, paramsList):
		if not num:
			for params in paramsList:
				logout.error("TransGroupToUser fail params=%s" % str(params))
			self.ResponseSingle(serverId, callbackId, announceConsts.CodeMailListSyncGroup)
			return
		# 拉取邮件总数
		self.DoQueryUserMailCount(serverId, callbackId, uid)

	def DoQueryUserMailCount(self, serverId, callbackId, uid):
		sql = "SELECT COUNT(*) FROM %s " % announceConsts.TableUserMail
		sql += "WHERE uid=%s AND expire>%s"
		params = (uid, int(time.time()))
		callback = lambda records:self.QueryUserMailCountCallback(records, serverId, callbackId, uid)
		mysqlPool.AsyncQueryWithOrderKey("mail%s"%uid, sql, params, callback)

	def QueryUserMailCountCallback(self, records, serverId, callbackId, uid):
		if records is None:
			logout.error("QueryUserMailCount fail uid=%s"%uid)
			self.ResponseSingle(serverId, callbackId, announceConsts.CodeMailListQueryCount)
			return
		number = records[0][0]
		if number <= 0:
			data = {
				"uid": uid,
				"number": 0,
				"mails": [],
			}
			self.ResponseSingle(serverId, callbackId, announceConsts.CodeSuc, data)
			return
		sql = "SELECT _id, title, content, itemList, cTime, expire, srcName, hasRead, getBonus FROM %s " % announceConsts.TableUserMail
		sql += "WHERE uid=%s AND expire>%s ORDER BY _id DESC LIMIT %s"
		params = (uid, int(time.time()), announceConsts.MailQueryOnce)
		callback = lambda records:self.QueryMailListCallback(records, serverId, callbackId, uid, number)
		mysqlPool.AsyncQueryWithOrderKey("mail%s"%uid, sql, params, callback)

	def DoQueryMailById(self, serverId, callbackId, uid, mailId):
		sql = "SELECT _id, title, content, itemList, cTime, expire, srcName, hasRead, getBonus FROM %s " % announceConsts.TableUserMail
		sql += "WHERE uid=%s AND expire>%s AND _id<%s ORDER BY _id DESC LIMIT %s"
		params = (uid, int(time.time()), mailId, announceConsts.MailQueryOnce)
		callback = lambda records: self.QueryMailListCallback(records, serverId, callbackId, uid, None)
		mysqlPool.AsyncQueryWithOrderKey("mail%s" % uid, sql, params, callback)

	def QueryMailListCallback(self, records, serverId, callbackId, uid, number):
		if records is None:
			logout.error("QueryMailList fail uid=%s"%uid)
			self.ResponseSingle(serverId, callbackId, announceConsts.CodeMailListQueryDetail)
			return
		data = {
			"uid": uid,
			"number": number,
			"mails": []
		}
		for single in records:
			_dict = {
				"_id": single[0],
				"title": single[1],
				"content": single[2],
				"itemList": json.loads(single[3]),
				"cTime": single[4],
				"expire": single[5],
				"srcName": single[6],
				"hasRead": single[7],
				"getBonus": single[8],
			}
			data["mails"].append(_dict)
		self.ResponseSingle(serverId, callbackId, announceConsts.CodeSuc, data)

	# 设置邮件为已读
	def OnMailSetRead(self, serverId, callbackId, args):
		uid = args.get("uid", None)
		mailIds = args.get("mailIds", None)
		if not mailIds or not uid:
			self.ResponseSingle(serverId, callbackId, announceConsts.CodeMailReadEmptyParam)
			return
		if type(mailIds) not in (list, tuple):
			mailIds = [mailIds, ]
		if len(mailIds) > announceConsts.MailReadOnceLimit:
			self.ResponseSingle(serverId, callbackId, announceConsts.CodeMailReadOverLimit)
			return
		formation, params = announceConsts.FormatMailIds(uid, mailIds)
		sql = "UPDATE %s SET hasRead=1 " % announceConsts.TableUserMail
		sql += "WHERE uid=%s "
		sql += "AND _id IN (%s)" % formation
		callback = lambda suc:self.MailSetReadCallback(suc, serverId, callbackId, uid, mailIds)
		mysqlPool.AsyncExecuteWithOrderKey("mail%s"%uid, sql, params, callback)

	def MailSetReadCallback(self, suc, serverId, callbackId, uid, mailIds):
		if not suc:
			logout.error("MailSetRead database fail uid=%s mailIds=%s"%(uid, str(mailIds)))
			self.ResponseSingle(serverId, callbackId, announceConsts.CodeMailReadDatabaseFail)
			return
		data = {
			"uid": uid,
			"mailIds": mailIds,
		}
		self.ResponseSingle(serverId, callbackId, announceConsts.CodeSuc, data)

	# 获取邮件锁（内存锁），为了防止并发领取附件物品
	def GetMailBonusLock(self, uid):
		now = int(time.time())
		lockTime = self.mMailBonusLock.get(uid, 0)
		if now - lockTime < announceConsts.MailBonusLockTime:
			return False
		self.mMailBonusLock[uid] = now
		return True

	# 释放邮件锁
	def ReleaseMailBonusLock(self, uid):
		if self.mMailBonusLock.has_key(uid):
			del self.mMailBonusLock[uid]

	# 领取邮件附件物品，步骤
	# 1、获取邮件锁
	# 2、查询指定的邮件，获取附件物品信息
	# 3、过滤查询结果，检查物品是否存在以及附件是否已经领取过了
	# 4、修改数据库记录，标识对应邮件附件领取状态为已经领取过了
	# 5、返回请求方可以成功领取附件物品的邮件id和对应的物品信息
	# 6、释放邮件锁
	def OnMailGetBonus(self, serverId, callbackId, args):
		uid = args.get("uid", None)
		mailIds = args.get("mailIds", None)
		if not mailIds or not uid:
			self.ResponseSingle(serverId, callbackId, announceConsts.CodeMailBonusEmptyParam)
			return
		if type(mailIds) not in (list, tuple):
			mailIds = [mailIds, ]
		if len(mailIds) > announceConsts.MailBonusOnceLimit:
			self.ResponseSingle(serverId, callbackId, announceConsts.CodeMailBonusOverLimit)
			return
		# 为了防止并发逻辑冲突，加个内存锁
		if not self.GetMailBonusLock(uid):
			self.ResponseSingle(serverId, callbackId, announceConsts.CodeMailBonusTooFast)
			return
		formation, params = announceConsts.FormatMailIds(uid, mailIds)
		sql = "SELECT _id, itemList, getBonus FROM %s " % announceConsts.TableUserMail
		sql += "WHERE uid=%s "
		sql += "AND _id IN (%s)" % formation
		callback = lambda records:self.QueryMailItemListCallback(records, serverId, callbackId, uid, mailIds)
		mysqlPool.AsyncQueryWithOrderKey("mail%s"%uid, sql, params, callback)

	def QueryMailItemListCallback(self, records, serverId, callbackId, uid, mailIds):
		if records is None:
			logout.error("QueryMailItemList database fail uid=%s mailIds=%s"%(uid, str(mailIds)))
			self.ReleaseMailBonusLock(uid)
			self.ResponseSingle(serverId, callbackId, announceConsts.CodeMailBonusQueryDatabaseFail)
			return
		if not records:
			self.ReleaseMailBonusLock(uid)
			self.ResponseSingle(serverId, callbackId, announceConsts.CodeMailBonusFindFail)
			return
		realMailIds = []
		realItemDatas = []
		for one in records:
			_id = one[0]
			itemList = json.loads(one[1])
			getBonus = one[2]
			if (not itemList) or getBonus:
				continue
			realMailIds.append(_id)
			realItemDatas.append(itemList)
		if not realMailIds:
			self.ReleaseMailBonusLock(uid)
			self.ResponseSingle(serverId, callbackId, announceConsts.CodeMailBonusAlreadyGet)
			return
		formation, params = announceConsts.FormatMailIds(uid, realMailIds)
		sql = "UPDATE %s SET getBonus=1 " % announceConsts.TableUserMail
		sql += "WHERE uid=%s AND getBonus=0 "
		sql += "AND _id IN (%s)" % formation
		callback = lambda suc:self.UpdateMailGetBonusCallback(suc, serverId, callbackId, uid, realMailIds, realItemDatas)
		mysqlPool.AsyncExecuteWithOrderKey("mail%s"%uid, sql, params, callback)
		logout.info("UpdateMailGetBonus start uid=%s mailIds=%s data=%s"%(uid, realMailIds, realItemDatas))

	def UpdateMailGetBonusCallback(self, suc, serverId, callbackId, uid, realMailIds, realItemDatas):
		if not suc:
			logout.error("UpdateMailGetBonus fail uid=%s mailIds=%s data=%s"%(uid, realMailIds, realItemDatas))
			self.ReleaseMailBonusLock(uid)
			self.ResponseSingle(serverId, callbackId, announceConsts.CodeMailBonusUpdateDatabaseFail)
			return
		for idx, mailId in enumerate(realMailIds):
			logout.info("UpdateMailGetBonus success uid=%s mailId=%s, itemList=%s" % (uid, mailId, realItemDatas[idx]))
		data = {
			"uid": uid,
			"mailIds": realMailIds,
			"items": realItemDatas,
		}
		self.ReleaseMailBonusLock(uid)
		self.ResponseSingle(serverId, callbackId, announceConsts.CodeSuc, data)

	# 为了防止邮件锁被锁死，增加了强制解锁的逻辑
	# 支持Master指令执行
	def OnMailReleaseLock(self, serverId, callbackId, args):
		uid = args.get("uid", None)
		if not uid:
			self.ResponseSingle(serverId, callbackId, announceConsts.CodeMailReleaseLockEmptyParam)
			return
		lockTime = self.mMailBonusLock.get(uid, None)
		self.ReleaseMailBonusLock(uid)
		self.ResponseSingle(serverId, callbackId, announceConsts.CodeSuc, {"lockTime":lockTime, "uid":uid})

	# 删除指定邮件
	def OnMailDelFix(self, serverId, callbackId, args):
		uid = args.get("uid", None)
		mailIds = args.get("mailIds", None)
		if not mailIds or not uid:
			self.ResponseSingle(serverId, callbackId, announceConsts.CodeMailDelEmptyParam)
			return
		if type(mailIds) not in (list, tuple):
			mailIds = [mailIds, ]
		if len(mailIds) > announceConsts.MailDelOnceLimit:
			self.ResponseSingle(serverId, callbackId, announceConsts.CodeMailDelOverLimit)
			return
		formation, params = announceConsts.FormatMailIds(uid, mailIds)
		sql = "DELETE FROM %s " % announceConsts.TableUserMail
		sql += "WHERE uid=%s "
		sql += "AND _id IN (%s)" % formation
		callback = lambda suc:self.DeleteFixMailCallback(suc, serverId, callbackId, uid, mailIds)
		mysqlPool.AsyncExecuteWithOrderKey("mail%s"%uid, sql, params, callback)

	def DeleteFixMailCallback(self, suc, serverId, callbackId, uid, mailIds):
		if not suc:
			logout.error("DeleteFixMail fail uid=%s mailIds=%s"%(uid, mailIds))
			self.ResponseSingle(serverId, callbackId, announceConsts.CodeMailDelDatabaseFail)
			return
		self.ResponseSingle(serverId, callbackId, announceConsts.CodeSuc, {"uid":uid, "mailIds":mailIds})

	# 清理无效的邮件
	# 无效邮件是指已读且已经领取附件物品完毕（或没有附件物品）
	def OnMailCleanNouse(self, serverId, callbackId, args):
		uid = args.get("uid", None)
		if not uid:
			self.ResponseSingle(serverId, callbackId, announceConsts.CodeMailCleanEmptyParam)
			return
		sql = "DELETE FROM %s " % announceConsts.TableUserMail
		sql += "WHERE uid=%s AND getBonus=1 AND hasRead=1"
		params = (uid, )
		callback = lambda suc:self.CleanNouseMailCallback(suc, serverId, callbackId, uid)
		mysqlPool.AsyncExecuteWithOrderKey("mail%s"%uid, sql, params, callback)

	def CleanNouseMailCallback(self, suc, serverId, callbackId, uid):
		if not suc:
			logout.error("CleanNouseMail fail uid=%s"%uid)
			self.ResponseSingle(serverId, callbackId, announceConsts.CodeMailCleanDatabaseFail)
			return
		self.ResponseSingle(serverId, callbackId, announceConsts.CodeSuc, {"uid":uid,})

	# 清理过期邮件，定时执行
	def DoMailDelExpire(self):
		now = int(time.time())
		print "DoMailDelExpire", time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(now))
		sql = "DELETE FROM %s " % announceConsts.TableUserMail
		sql += "WHERE expire<%s LIMIT %s"
		params = (now, announceConsts.MailDelExpireOnceLimit)
		callback = lambda suc:self.DeleteExpireMailCallback(suc)
		mysqlPool.AsyncExecuteWithOrderKey("mail", sql, params, callback)

	def DeleteExpireMailCallback(self, suc):
		if not suc:
			logout.error("DeleteExpireMail database fail")
			return
		logout.info("DeleteExpireMail success")
	# -------------------------------------------------------------------------------------------
	# 推送到客户端，步骤
	# 1、从redis中获取客户端所在的proxyId
	# 2、通知proxy将指定消息转发给对应的客户端
	def DoPushToUserClient(self, uid, event, eventData):
		callback = lambda record:self.QueryClientProxyCallback(record, uid, event, eventData)
		keyPlayer = commonNetgameApi.GetOnlineKey(uid)
		redisPool.AsyncHgetall(keyPlayer, callback)

	def QueryClientProxyCallback(self, record, uid, event, eventData):
		if not record:  # 不在线
			return
		serverId = int(record.get('serverid', '0'))
		proxyId = int(record.get('proxyid', '0'))
		if (not serverId) or (not proxyId):  # 不在线
			return
		self.mSystem.RemoteNotifyToClient(uid, proxyId, event, eventData)






