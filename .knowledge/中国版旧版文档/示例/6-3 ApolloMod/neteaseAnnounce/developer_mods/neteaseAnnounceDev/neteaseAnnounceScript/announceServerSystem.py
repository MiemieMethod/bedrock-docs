# -*- coding: utf-8 -*-
import time
import server.extraServerApi as extraServerApi
ServerSystem = extraServerApi.GetServerSystemCls()
import lobbyGame.netgameApi as netgameApi
import apolloCommon.commonNetgameApi as commonNetgameApi
import logout
import neteaseAnnounceScript.announceConsts as announceConsts
from neteaseAnnounceScript.announceConsts import ModNameSpace, ServiceSystemName, ClientSystemName
from neteaseAnnounceScript.announceConsts import ClientSpecEvent, ServerSpecEvent, MailEvent, FloatingWindowEvent, LoginPopupEvent
import neteaseAnnounceScript.timermanager as timermanager


class AnnounceServerSystem(ServerSystem):
	def __init__(self, namespace, systemName):
		ServerSystem.__init__(self, namespace, systemName)
		self.mPlayerLoginByTransferDict = {}
		self.ListenForEvent(extraServerApi.GetEngineNamespace(), extraServerApi.GetEngineSystemName(), "AddServerPlayerEvent",
							self, self.OnAddServerPlayer)
		self.ListenForEvent(ModNameSpace, ClientSystemName, ClientSpecEvent.Enter,
							self, self.OnClientEnter)
		# 登录弹窗
		self.ListenForEvent(ModNameSpace, ServiceSystemName, LoginPopupEvent.SyncData,
							self, self.OnLoginPopupSyncData)
		self.mLoginPopupList = []
		self.mLoginPopupVersion = 0
		# 启动时向Service询问最新版本，频率较高
		self.mAskSyncTimer = timermanager.timerManager.addRepeatTimer(5, self.OnAskSync)
		# 每隔5分钟问一次最新版本
		# 主要是为了防止链路中断，service重启等特殊情况导致的直接同步失败
		self.mNormalAskSyncTimer = timermanager.timerManager.addRepeatTimer(300, self.OnNormalAskSync)
		# 浮窗公告
		self.mFloatingWindowList = []
		self.mFloatingWindowVersion = 0
		self.mFloatingWindowBroadcasted = []
		self.ListenForEvent(ModNameSpace, ServiceSystemName, FloatingWindowEvent.SyncData,
							self, self.OnFloatingWindowSyncData)
		self.mCheckFloatTimer = timermanager.timerManager.addRepeatTimer(1, self.OnCheckFloat)
		# 邮件
		self.ListenForEvent(ModNameSpace, ClientSystemName, MailEvent.GetMailList,
							self, self.OnMailGetList)
		self.ListenForEvent(ModNameSpace, ClientSystemName, MailEvent.SetRead,
							self, self.OnMailSetRead)
		self.ListenForEvent(ModNameSpace, ClientSystemName, MailEvent.GetBonus,
							self, self.OnMailGetBonus)
		self.ListenForEvent(ModNameSpace, ClientSystemName, MailEvent.DelFixMail,
							self, self.OnMailDelFix)

	def Destroy(self):
		if self.mAskSyncTimer:
			timermanager.timerManager.delTimer(self.mAskSyncTimer)
			self.mAskSyncTimer = None
		if self.mNormalAskSyncTimer:
			timermanager.timerManager.delTimer(self.mNormalAskSyncTimer)
			self.mNormalAskSyncTimer = None
		if self.mCheckFloatTimer:
			timermanager.timerManager.delTimer(self.mCheckFloatTimer)
			self.mCheckFloatTimer = None
		self.UnListenForEvent(extraServerApi.GetEngineNamespace(), extraServerApi.GetEngineSystemName(),
							"AddServerPlayerEvent", self, self.OnAddServerPlayer)
		self.UnListenForEvent(ModNameSpace, ClientSystemName, ClientSpecEvent.Enter,
							self, self.OnClientEnter)
		# 登录弹窗
		self.UnListenForEvent(ModNameSpace, ServiceSystemName, LoginPopupEvent.SyncData,
							self, self.OnLoginPopupSyncData)
		# 浮窗公告
		self.UnListenForEvent(ModNameSpace, ServiceSystemName, FloatingWindowEvent.SyncData,
							self, self.OnFloatingWindowSyncData)
		# 邮件
		self.UnListenForEvent(ModNameSpace, ClientSystemName, MailEvent.GetMailList,
							self, self.OnMailGetList)
		self.UnListenForEvent(ModNameSpace, ClientSystemName, MailEvent.SetRead,
							self, self.OnMailSetRead)
		self.UnListenForEvent(ModNameSpace, ClientSystemName, MailEvent.GetBonus,
							self, self.OnMailGetBonus)
		self.UnListenForEvent(ModNameSpace, ClientSystemName, MailEvent.DelFixMail,
							self, self.OnMailDelFix)
		ServerSystem.Destroy(self)

	def Update(self):
		timermanager.timerManager.tick()
	# ------------------------------------------------------------------------------------------
	# 某UID玩家是否有未读邮件
	def CheckHasUnreadMail(self, uid, cbFunc):
		eventData = {
			"uid": uid,
		}
		def OnCheckUnreadCallback(suc, args):
			if not suc:
				cbFunc(False, None)
				return
			suc, hasUnread = args["suc"], args["hasUnread"]
			cbFunc(suc, hasUnread)
		self.RequestToService(ModNameSpace, MailEvent.CheckHasUnread, eventData, OnCheckUnreadCallback)

	# 单发邮件封装，简易版，无回调函数
	def SendMailToUser(self, touids, title, content, itemList=[], expire=None, srcName=""):
		eventData = {
			"touids": touids,
			"title": title,
			"content": content,
			"itemList": itemList,
			"expire": expire,
			"srcName": srcName,
		}
		self.RequestToService(ModNameSpace, MailEvent.SendToMany, eventData)

	# 群发邮件封装，简易版，无回调函数，发送给所有当前已经成功登录过游戏的玩家
	def SendMailToGroup(self, title, content, effectTime, itemList=[], expire=None, srcName=""):
		eventData = {
			"title": title,
			"content": content,
			"effectTime": effectTime,
			"itemList": itemList,
			"expire": expire,
			"srcName": srcName,
		}
		self.RequestToService(ModNameSpace, MailEvent.SendToGroup, eventData)

	# 在客户端画面中心显示提示文字
	def SendCentreNotice(self, playerId, message):
		comp = extraServerApi.CreateComponent(playerId, 'Minecraft', 'command')
		return comp.SetCommand("title @s title %s" % message)
	# ------------------------------------------------------------------------------------------
	# 给客户端发送配置的变化
	def SendToClientSyncConfig(self, playerId):
		eventData = {
			"version": announceConsts.ModVersion,
			"configDict": {},
		}
		for keyname in announceConsts.ConfigurablePostToClient:
			value = getattr(announceConsts, keyname)
			eventData["configDict"][keyname] = value
		self.NotifyToClient(playerId, ServerSpecEvent.SyncConfig, eventData)

	def OnAddServerPlayer(self, args):
		#print "OnAddServerPlayer", args
		isTransfer = args.get("isTransfer", False)
		self.mPlayerLoginByTransferDict[args["id"]] = isTransfer

	# 客户端UI初始化完成后发送的事件响应函数
	# 1、通知客户端可配置属性的变化
	# 2、去Service注册邮件新用户（因为不知道是否是首次登录，注册用户支持重复调用）
	# 3、遍历本地缓存，获取需要显示的登录弹窗列表，发送给客户端
	# 4、遍历本地缓存，获取需要显示的浮窗公告列表，发送给客户端
	def OnClientEnter(self, args):
		playerId = args.get("playerId", "-1")
		uid = netgameApi.GetPlayerUid(playerId)
		# 通知client配置属性的变化
		self.SendToClientSyncConfig(playerId)
		# 注册邮件用户
		callback = lambda suc,args: self.RegMailUserCallback(suc, args, playerId, uid)
		eventData = {
			"uid": uid,
		}
		self.RequestToService(ModNameSpace, MailEvent.RegUser, eventData, callback)
		# 显示登录弹窗
		isTransfer = self.mPlayerLoginByTransferDict.get(playerId, False)
		#print "OnClientEnter isTransfer=", isTransfer
		if not isTransfer:
			self.SendToClientLoginPop(playerId)
		# 显示浮窗公告
		self.SendToClientFloatingWindow(playerId)

	# 注册用户成功后向Service请求邮件列表
	def RegMailUserCallback(self, suc, args, playerId, uid):
		if not suc:
			return
		if args["code"] != announceConsts.CodeSuc:
			return
		# 注册成功，立刻拉邮件一次
		callback = lambda suc,args: self.GetMailListCallback(suc, args, playerId)
		eventData = {
			"uid": uid,
			"mailId": 0,
		}
		self.RequestToService(ModNameSpace, MailEvent.GetMailList, eventData, callback)

	# 客户端发来请求，再次获取邮件列表
	# 拉取邮件是分步骤进行的
	# 1、服务器主动向Service请求邮件列表
	# 2、Service返回当前邮件总数和前N封邮件全文（当前N=20）
	# 3、服务器转手把这些信息发送给客户端
	# 4、客户端收到后，判断是否还有邮件没拉完，假如邮件没有拉取完毕，
	# 		则客户端再次发送拉取邮件列表的事件，此时带上上次拉取到的邮件中
	#		唯一Id最小的邮件的Id
	# 5、服务器转手将此请求发送给Service
	# 6、Service根据请求中的Id，拉取接下来的N封邮件全文返回
	# 循环3、4、5、6直到所有邮件都拉取完毕
	def OnMailGetList(self, args):
		playerId = args.get("playerId", "-1")
		uid = netgameApi.GetPlayerUid(playerId)
		if not uid:
			return
		args["uid"] = uid
		callback = lambda suc, args: self.GetMailListCallback(suc, args, playerId)
		self.RequestToService(ModNameSpace, MailEvent.GetMailList, args, callback)

	def GetMailListCallback(self, suc, args, playerId):
		if not suc:
			return
		self.NotifyToClient(playerId, MailEvent.GetMailList, args)

	# 设置邮件已读，触发条件是客户端点开对应邮件的全文
	def OnMailSetRead(self, args):
		playerId = args.get("playerId", "-1")
		uid = netgameApi.GetPlayerUid(playerId)
		if not uid:
			return
		args["uid"] = uid
		callback = lambda suc, args: self.SetReadCallback(suc, args, playerId)
		self.RequestToService(ModNameSpace, MailEvent.SetRead, args, callback)

	def SetReadCallback(self, suc, args, playerId):
		if not suc:
			return
		self.NotifyToClient(playerId, MailEvent.SetRead, args)

	# 是否允许领取附件
	def HasYun(self):
		system = extraServerApi.GetSystem(announceConsts.YunModNameSpace, announceConsts.YunServerSystemName)
		if system:
			return True
		else:
			return False

	def ForbidGetBonus(self):
		if announceConsts.MailOpenGetItemWithoutYun:
			return False
		if self.HasYun():
			return False
		return True

	# 领取邮件附件中的物品到背包
	# 先检查一下背包中是否有足够的空间
	def OnMailGetBonus(self, args):
		playerId = args.get("playerId", "-1")
		uid = netgameApi.GetPlayerUid(playerId)
		if not uid:
			return
		if self.ForbidGetBonus():
			return
		args["uid"] = uid
		itemNum = len(args.get("itemList", []))
		if itemNum > self.GetEmptySlotNumber(playerId):
			self.SendCentreNotice(playerId, announceConsts.ErrorText[announceConsts.CodeMailBonusBagFull])
			return
		callback = lambda suc, args: self.GetBonusCallback(suc, args, playerId)
		self.RequestToService(ModNameSpace, MailEvent.GetBonus, args, callback)

	# Service返回领取附件物品成功，把物品放进背包
	def GetBonusCallback(self, suc, args, playerId):
		if not suc:
			return
		if args["code"] == announceConsts.CodeSuc:
			for idx, mailId in enumerate(args["entity"]["mailIds"]):
				itemList = args["entity"]["items"][idx]
				self.DoRecvMailItems(playerId, mailId, itemList)
		self.NotifyToClient(playerId, MailEvent.GetBonus, args)

	# 把物品放进背包
	def DoRecvMailItems(self, playerId, mailId, itemList):
		logout.info("DoRecvMailItems start playerId=%s mailId=%s itemList=%s" % (playerId, mailId, itemList))
		comp = extraServerApi.CreateComponent(playerId, 'Minecraft', 'item')
		if not comp:
			logout.warning("DoRecvMailItems fail by player leave playerId=%s"%playerId)
			return
		for idx, singleItem in enumerate(itemList):
			if type(singleItem) == str:
				code, item = announceConsts.CheckSingleMailItemFromString(singleItem)
			elif type(singleItem) == dict:
				code, item = announceConsts.CheckSingleMailItemFromDict(singleItem)
			else:
				logout.error("DoRecvMailItems with wrong format playerId=%s mailId=%s singleItem=%s" % (playerId, mailId, singleItem))
				continue
			if code != announceConsts.CodeSuc:
				logout.error("DoRecvMailItems with wrong format playerId=%s mailId=%s singleItem=%s" % (playerId, mailId, singleItem))
				continue
			enchantData = []
			tmpData = item.get("enchantData", [])
			if tmpData and type(tmpData) == list:
				for info in tmpData:
					if type(info) == list:
						enchantData.append(tuple(info))
			itemDict = {
				'itemName': item["itemName"],
				'count': item["count"],
				'enchantData': enchantData,
				'auxValue': item["auxValue"],
				'customTips': item.get("customTips", ""),
				'extraId': item.get("extraId", ""),
			}
			slot = self.GetEmptySlot(playerId)
			if slot is None:
				logout.error("bag full playerId=%s mailId=%s idx=%s singleItem=%s" % (playerId, mailId, idx, singleItem))
				continue
			comp.SpawnItemToPlayerInv(itemDict, playerId, slot)
			durability = item.get("durability", None)
			if not durability is None:
				comp.SetInvItemDurability(slot, durability)
			logout.info("trans mail to bag success playerId=%s mailId=%s idx=%s singleItem=%s" % (playerId, mailId, idx, singleItem))

	# 获取背包中的剩余空格
	def GetEmptySlotNumber(self, playerId):
		comp = self.CreateComponent(playerId, 'Minecraft', 'item')
		number = 0
		for slot in xrange(36):
			item = comp.GetPlayerItem(extraServerApi.GetMinecraftEnum().ItemPosType.INVENTORY, slot)
			if not item:
				number += 1
		return number

	# 获取一个空闲的背包位置
	def GetEmptySlot(self, playerId):
		comp = self.CreateComponent(playerId, 'Minecraft', 'item')
		for slot in xrange(36):
			item = comp.GetPlayerItem(extraServerApi.GetMinecraftEnum().ItemPosType.INVENTORY, slot)
			if not item:
				return slot
		return None

	# 删除指定的邮件
	def OnMailDelFix(self, args):
		playerId = args.get("playerId", "-1")
		uid = netgameApi.GetPlayerUid(playerId)
		if not uid:
			return
		args["uid"] = uid
		callback = lambda suc, args: self.DelFixMailCallback(suc, args, playerId)
		self.RequestToService(ModNameSpace, MailEvent.DelFixMail, args, callback)

	def DelFixMailCallback(self, suc, args, playerId):
		if not suc:
			return
		self.NotifyToClient(playerId, MailEvent.DelFixMail, args)
	# ---------------------------------------------------------------------------------------
	# 启动服务器后，要向Service快速轮询，以获取当前的登录弹窗和浮窗公告
	def OnAskSync(self):
		needStop = True
		if self.mLoginPopupVersion <= 0:
			needStop = False
			eventData = {"version":self.mLoginPopupVersion,}
			self.RequestToService(ModNameSpace, LoginPopupEvent.AskNew, eventData, self.LoginPopupAskNewCallback)
		if self.mFloatingWindowVersion <= 0:
			needStop = False
			eventData = {"version":self.mFloatingWindowVersion,}
			self.RequestToService(ModNameSpace, FloatingWindowEvent.AskNew, eventData, self.FloatingWindowAskNewCallback)
		# print "OnAskSync", needStop
		# 首次同步完成之后，快速轮询关闭
		if needStop:
			timermanager.timerManager.delTimer(self.mAskSyncTimer)

	# 拿到一个版本的弹窗和公告内容后，就只需要每5分钟重新获取就行了
	# 因为有变动Service会主动通知组网成功服务器信息变化了，
	# 5分钟的重新拉取是为了防止断网等意外情况下也能同步回来
	def OnNormalAskSync(self):
		# print "OnNormalAskSync"
		eventData = {"version": self.mLoginPopupVersion, }
		self.RequestToService(ModNameSpace, LoginPopupEvent.AskNew, eventData, self.LoginPopupAskNewCallback)
		eventData = {"version": self.mFloatingWindowVersion, }
		self.RequestToService(ModNameSpace, FloatingWindowEvent.AskNew, eventData, self.FloatingWindowAskNewCallback)
	# ---------------------------------------------------------------------------------------
	# 登录弹窗
	def LoginPopupAskNewCallback(self, suc, args):
		if not suc:
			return
		if args["code"] != announceConsts.CodeSuc:
			return
		self.mLoginPopupVersion = args["entity"]["version"]
		self.mLoginPopupList = args["entity"]["dataList"]
		# print "LoginPopupAskNewCallback", self.mLoginPopupVersion

	def OnLoginPopupSyncData(self, data):
		self.mLoginPopupVersion = data["version"]
		self.mLoginPopupList = data["dataList"]
		# print "OnLoginPopupSyncData", self.mLoginPopupVersion

	def SendToClientLoginPop(self, playerId):
		now = int(time.time())
		delCount = 0
		eventData = {
			"version": self.mLoginPopupVersion,
			"dataList": [],
		}
		for idx, record in enumerate(self.mLoginPopupList):
			if record["endTime"] <= now:
				self.mLoginPopupList[idx] = None
				delCount += 1
				continue
			if record["beginTime"] > now:
				continue
			eventData["dataList"].append(record)
		if eventData["dataList"]:
			self.NotifyToClient(playerId, LoginPopupEvent.SyncData, eventData)
		for i in xrange(delCount):
			self.mLoginPopupList.remove(None)
	# ---------------------------------------------------------------------------------------
	# 浮窗公告
	# 当前每秒都会检查是不是有浮窗公告到了触发时间点了，到了就直接告诉客户端显示公告
	def OnCheckFloat(self):
		now = int(time.time())
		delCount = 0
		eventData = {
			"version": self.mFloatingWindowVersion,
			"dataList": [],
		}
		for idx, record in enumerate(self.mFloatingWindowList):
			if record["endTime"] <= now:
				self.mFloatingWindowList[idx] = None
				delCount += 1
				continue
			if record["beginTime"] > now:
				continue
			if record["_id"] in self.mFloatingWindowBroadcasted:
				continue
			eventData["dataList"].append(record)
			self.mFloatingWindowBroadcasted.append(record["_id"])
		if eventData["dataList"]:
			self.BroadcastToAllClient(FloatingWindowEvent.SyncData, eventData)
		for i in xrange(delCount):
			self.mFloatingWindowList.remove(None)

	def FloatingWindowAskNewCallback(self, suc, args):
		if not suc:
			return
		if args["code"] != announceConsts.CodeSuc:
			return
		self.mFloatingWindowVersion = args["entity"]["version"]
		self.mFloatingWindowList = []
		for record in args["entity"]["dataList"]:
			if commonNetgameApi.GetServerType() == "lobby":
				if record["lobbyShow"]:
					self.mFloatingWindowList.append(record)
			else:
				if record["gameShow"]:
					self.mFloatingWindowList.append(record)
		#print "FloatingWindowAskNewCallback", self.mFloatingWindowVersion
		#for record in self.mFloatingWindowList:
		#	print record

	def OnFloatingWindowSyncData(self, data):
		self.mFloatingWindowVersion = data["version"]
		self.mFloatingWindowList = []
		for record in data["dataList"]:
			if commonNetgameApi.GetServerType() == "lobby":
				if record["lobbyShow"]:
					self.mFloatingWindowList.append(record)
			else:
				if record["gameShow"]:
					self.mFloatingWindowList.append(record)
		#print "OnFloatingWindowSyncData", self.mFloatingWindowVersion
		#for record in self.mFloatingWindowList:
		#	print record

	def SendToClientFloatingWindow(self, playerId):
		now = int(time.time())
		eventData = {
			"version": self.mFloatingWindowVersion,
			"dataList": [],
		}
		for idx, record in enumerate(self.mFloatingWindowList):
			if record["endTime"] <= now:
				continue
			if record["beginTime"] > now:
				continue
			eventData["dataList"].append(record)
		if eventData["dataList"]:
			self.NotifyToClient(playerId, FloatingWindowEvent.SyncData, eventData)
