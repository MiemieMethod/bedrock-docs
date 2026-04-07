# -*- coding: utf-8 -*-

#---------------------------------------------------------------------------------------
# 整个Mod的一些绑定配置
ModVersion = "1.0.10"
ModNameSpace = "neteaseAnnounce"
ClientSystemName = "neteaseAnnounceBeh"
ClientSystemClsPath = "neteaseAnnounceScript.announceClientSystem.AnnounceClientSystem"
ServerSystemName = "neteaseAnnounceDev"
ServerSystemClsPath = "neteaseAnnounceScript.announceServerSystem.AnnounceServerSystem"
ServiceSystemName = "neteaseAnnounceService"
ServiceSystemClsPath = "neteaseAnnounceScript.announceServiceSystem.AnnounceServiceSystem"
MasterSystemName = "neteaseAnnounceMaster"
MasterSystemClsPath = "neteaseAnnounceScript.announceMasterSystem.AnnounceMasterSystem"

YunModNameSpace = "neteaseCloud"
YunServerSystemName = "neteaseCloudDev"
YunClientSystemName = "neteaseCloudBeh"
#---------------------------------------------------------------------------------------
SecondPerDay = 3600 * 24		# 一天的秒数
LoginPopExpire = SecondPerDay * 30	# 登录弹窗默认的有效时长
FloatWinExpire = 60	# 浮窗公告默认的有效时长
FloatWinExpireFactor = 5	# 浮窗公告默认的有效时长倍数
MailExpire = SecondPerDay *  30	# 邮件的默认有效期
MailItemLimit = 10	# 一封邮件最多带多少物品
MailExpireMax = 1575534898	# 2019年12月的时间戳，有效期大于此时间戳，认为是绝对时间，而不是从邮件创建开始的相对时间
GroupMailExpire = SecondPerDay * 30	# 全局邮件的默认有效期
MailQueryOnce = 20	# 邮件一次最多取多少条
MailReadOnceLimit = 30	# 每次最多同时设置多少条邮件已读
MailBonusOnceLimit = 10	# 每次最多同时领取多少条邮件的附件
MailBonusLockTime = 30	# 领取邮件附件锁的时长
MailDelOnceLimit = 100	# 每次最多同时删除多少条邮件（玩家主动）
MailDelExpireOnceLimit = 1000	# 每次最多同时删除多少条邮件（定时删除过期邮件）
MailDelExpireInterval = 60		# 每间隔多少时间，尝试删除一次过期邮件
LoginPopupTitleLimit = 10	# 登录弹窗标题长度限制
LoginPopupContentLimit = 1000	# 登录弹窗正文长度限制
FloatWinContentLimit = 20	#  浮窗公告正文长度限制
MailTitleLimit = 10		# 邮件标题长度限制
MailContentLimit = 400	# 邮件正文长度限制
MailShowButtonOnDesk = 1 # 是否在主界面显示邮件入口按钮
MailItemListLengthLimit = 980	# 邮件附件长度限制（与数据库建表语句有关）
MailOpenGetItemWithoutYun = False	# 是否可在未使用云端玩家信息的服务器中领取附件的配置，如果配置为否，那么未使用云端背包的服务器，领取按钮隐藏
ShowPopOncePerLogin = True 		# 一次登录只出现一次弹窗


ConfigurableDefineList = ["LoginPopExpire", "FloatWinExpire", "FloatWinExpireFactor",
						  "MailExpire", "GroupMailExpire", "MailDelExpireOnceLimit",
						  "MailDelExpireInterval", "LoginPopupTitleLimit", "LoginPopupContentLimit",
						  "FloatWinContentLimit", "MailTitleLimit", "MailContentLimit",
						  "MailShowButtonOnDesk", "MailOpenGetItemWithoutYun", "ShowPopOncePerLogin"
						  ]
ConfigurablePostToClient = ["MailShowButtonOnDesk", "MailOpenGetItemWithoutYun"]
#---------------------------------------------------------------------------------------
# 数据库表名
# 登录弹窗，每条弹出一条记录
TableLoginPopup = "neteaseLoginPopup"
# 浮窗公告，每条记录一条公告
TableFloatingWindow = "neteaseFloatingWindow"
# 玩家个人信息，每个玩家一条记录
TableMailUserProp = "neteaseMailUserProp"
# 玩家邮件，每封邮件一条记录
TableUserMail = "neteaseUserMail"
# 群发邮件，每封邮件一条记录
TableGroupMail = "neteaseGroupMail"
#---------------------------------------------------------------------------------------
# 客户端专属事件
class ClientSpecEvent(object):
	Enter = "ClientEnter"

# game/lobby服务器专属事件
class ServerSpecEvent(object):
	SyncConfig = "ServerSyncConfig"

# 登录弹窗请求
class LoginPopupRequest(object):
	New = "/login-pop-new"
	Del = "/login-pop-del"
	View = "/login-pop-list"
	Clean = "/login-pop-clean"
	AskNew = "/login-pop-ask"

class LoginPopupEvent(object):
	New = "LoginPopupNew"	# 新建
	Del	= "LoginPopupDel"	# 删除
	View = "LoginPopupView"	# 查询当前尚未过期的
	Clean = "LoginPopupClean"	# 清理
	AskNew = "LoginPopupAskNew"	# Server向Service请求最新版本的弹窗配置
	SyncData = "LoginPopupSync"	# Service向Server广播最新版本的弹窗配置
	Appear = "LoginPopupAppear"	# Server告知Client当前版本的弹窗配置
#---------------------------------------------------------------------------------------
# 浮窗公告请求
class FloatingWindowRequest(object):
	New = "/float-win-new"
	Del = "/float-win-del"
	View = "/float-win-list"
	Clean = "/float-win-clean"
	AskNew = "/float-win-ask"

class FloatingWindowEvent(object):
	New = "FloatingWindowNew"	# 新建
	Del = "FloatingWindowDel"	# 删除
	View = "FloatingWindowView"	# 查询当前尚未过期的
	Clean = "FloatingWindowClean"	# 清理
	AskNew = "FloatingWindowAskNew"	# Server向Service请求最新版本的公告配置
	SyncData = "FloatingWindowSync"	# Service向Server广播最新版本的公告配置
	Appear = "FloatingWindowAppear"	# Server告知Client显示指定浮窗公告
#---------------------------------------------------------------------------------------
# 邮件请求
class MailRequest(object):
	RegUser = "/mail-reg-user"
	SendToSingle = "/mail-send-single"
	SendToMany = "/mail-send-many"
	SendToGroup = "/mail-send-to-group"
	GetMailList = "/mail-get-list"
	DelFixMail = "/mail-del-fix"
	CleanMail = "/mail-clean"
	SetRead = "/mail-set-read"
	GetBonus = "/mail-get-bonus"
	ReleaseLock = "/mail-release-lock"

class MailEvent(object):
	RegUser = "MailRegUser"
	SendToSingle = "MailSendToSingle"
	SendToMany = "MailSendToMany"
	SendToGroup = "MailSendToGroup"
	GetMailList = "MailGetList"
	DelFixMail = "MailDelFix"
	CleanMail = "MailCleanNouse"
	SetRead = "MailSetRead"
	GetBonus = "MailGetBonus"
	NewMailArrive = "MailArraiveNew"
	ReleaseLock = "MailReleaseLock"
	CheckHasUnread = "CheckHasUnread"

def CheckMailItem(itemList):
	if type(itemList) not in (list, tuple):
		return CodeMailNewItemWrong, None
	if len(itemList) > MailItemLimit:
		return CodeMailNewItemTooLong, None
	result = []
	for singleItem in itemList:
		if type(singleItem) == str:
			code, item = CheckSingleMailItemFromString(singleItem)
		elif type(singleItem) == dict:
			code, item = CheckSingleMailItemFromDict(singleItem)
		else:
			return CodeMailNewItemWrong, None
		if code == CodeSuc:
			result.append(item)
		else:
			return code, None
	return CodeSuc, result

def CheckSingleMailItemFromString(itemStr):
	data = itemStr.split(":")
	if len(data) != 4:
		return CodeMailNewItemWrong, None
	try:
		auxValue = int(data[2])
		count = int(data[3])
	except:
		return CodeMailNewItemWrong, None
	if (auxValue < 0) or (count<= 0):
		return CodeMailNewItemWrong, None
	item = {
		"itemName": "%s:%s" % (data[0], data[1]),
		"auxValue": auxValue,
		"count": count,
	}
	return CodeSuc, item

def CheckSingleMailItemFromDict(itemDict):
	itemName = itemDict.get("itemName", None)
	auxValue = itemDict.get("auxValue", None)
	count = itemDict.get("count", None)
	enchantData = itemDict.get("enchantData", None)
	customTips = itemDict.get("customTips", None)
	extraId = itemDict.get("extraId", None)
	durability = itemDict.get("durability", None)
	if (itemName is None) or (auxValue is None) or (count is None):
		return CodeMailNewItemWrong, None
	if type(auxValue) != int or auxValue < 0:
		return CodeMailNewItemWrong, None
	if type(count) != int or count <= 0:
		return CodeMailNewItemWrong, None
	item = {
		"itemName": itemName,
		"auxValue": auxValue,
		"count": count,
	}
	if not enchantData is None:
		if type(enchantData) != list:
			return CodeMailNewItemWrong, None
		item["enchantData"] = enchantData
	if not customTips is None:
		if type(customTips) != str:
			return CodeMailNewItemWrong, None
		item["customTips"] = customTips
	if not extraId is None:
		if type(extraId) != str:
			return CodeMailNewItemWrong, None
		item["extraId"] = extraId
	if not durability is None:
		if type(durability) != int or durability <= 0:
			return CodeMailNewItemWrong, None
		item["durability"] = durability
	return CodeSuc, item

def FormatMailIds(uid, mailIds):
	formation = ["%s", ] * len(mailIds)
	formation = ", ".join(formation)
	params = [uid, ]
	params.extend(mailIds)
	params = tuple(params)
	return formation, params
#---------------------------------------------------------------------------------------
# 错误码
ErrorText = {}
CodeSuc = 1
ErrorText[CodeSuc] = "请求成功"
# 登录弹窗
CodeLoginEmptyParam = 10
ErrorText[CodeLoginEmptyParam] = "新建登录弹窗失败，参数title和content不能为空"
CodeLoginTextOverLimit = 11
ErrorText[CodeLoginTextOverLimit] = "新建登录弹窗失败，title限制%s字、content限制%s字"%(LoginPopupTitleLimit, LoginPopupContentLimit)
CodeLoginWrongParam = 12
ErrorText[CodeLoginWrongParam] = "新建登录弹窗失败，开始时间不能晚于结束时间"
CodeLoginDatabaseFail = 13
ErrorText[CodeLoginDatabaseFail] = "新建登录弹窗失败，数据库插入记录失败"
CodeLoginServiceTimeout = 14
ErrorText[CodeLoginServiceTimeout] = "新建登录弹窗失败，请求响应超时"
CodeLoginViewTimeout = 15
ErrorText[CodeLoginViewTimeout] = "查询登录弹窗失败，请求响应超时"
CodeLoginDelEmptyParam = 16
ErrorText[CodeLoginDelEmptyParam] = "删除登录弹窗失败，参数_id不能为空"
CodeLoginDelEmptyRecord = 17
ErrorText[CodeLoginDelEmptyRecord] = "删除登录弹窗失败，对应_id的弹窗不存在或已经过期"
CodeLoginDelTimeout = 18
ErrorText[CodeLoginDelTimeout] = "删除登录弹窗失败，请求响应超时"
CodeLoginCleanDabaseFail = 19
ErrorText[CodeLoginDelTimeout] = "清空登录弹窗失败，清理数据库记录失败"
CodeLoginCleanTimeout = 20
ErrorText[CodeLoginCleanTimeout] = "清空登录弹窗失败，请求响应超时"
CodeLoginAskNewSame = 21
ErrorText[CodeLoginAskNewSame] = "获取当前登录弹窗列表无效，已经是最新版本了"
CodeLoginAskNewNotInited = 22
ErrorText[CodeLoginAskNewNotInited] = "获取当前登录弹窗列表失败，服务尚未初始化完成"
CodeLoginAskNewTimeout = 23
ErrorText[CodeLoginAskNewTimeout] = "获取当前登录弹窗列表失败，请求响应超时"
# 浮窗公告
CodeFloatingEmptyParam = 101
ErrorText[CodeFloatingEmptyParam] = "新建弹出公告失败，参数content和displayTime不能为空"
CodeFloatingDisplayWrong = 102
ErrorText[CodeFloatingDisplayWrong] = "新建弹出公告失败，参数displayTime只能是正整数"
CodeFloatingTextOverLimit = 103
ErrorText[CodeFloatingTextOverLimit] = "新建弹出公告失败，content限制%s字"%FloatWinContentLimit
CodeFloatingEmptyDisplay = 104
ErrorText[CodeFloatingEmptyDisplay] = "新建弹出公告失败，至少要在lobby或game中选一显示"
CodeFloatingWrongParam = 105
ErrorText[CodeFloatingWrongParam] = "新建弹出公告失败，开始时间不能晚于结束时间"
CodeFloatingDatabaseFail = 106
ErrorText[CodeFloatingDatabaseFail] = "新建弹出公告失败，数据库插入记录失败"
CodeFloatingServiceTimeout = 107
ErrorText[CodeFloatingServiceTimeout] = "新建弹出公告失败，请求响应超时"
CodeFloatingViewTimeout = 108
ErrorText[CodeFloatingViewTimeout] = "查询弹出公告失败，请求响应超时"
CodeFloatingDelEmptyParam = 109
ErrorText[CodeFloatingDelEmptyParam] = "删除弹出公告失败，参数_id不能为空"
CodeFloatingDelEmptyRecord = 110
ErrorText[CodeFloatingDelEmptyRecord] = "删除弹出公告失败，对应_id的弹窗不存在或已经过期"
CodeFloatingDelTimeout = 111
ErrorText[CodeFloatingDelTimeout] = "删除弹出公告失败，请求响应超时"
CodeFloatingCleanDabaseFail = 112
ErrorText[CodeFloatingCleanDabaseFail] = "清空弹出公告失败，清理数据库记录失败"
CodeFloatingCleanTimeout = 113
ErrorText[CodeFloatingCleanTimeout] = "清空弹出公告失败，请求响应超时"
CodeFloatingAskNewSame = 114
ErrorText[CodeFloatingAskNewSame] = "获取当前弹出公告列表无效，已经是最新版本了"
CodeFloatingAskNewNotInited = 115
ErrorText[CodeFloatingAskNewNotInited] = "获取当前弹出公告列表失败，服务尚未初始化完成"
CodeFloatingAskNewTimeout = 116
ErrorText[CodeFloatingAskNewTimeout] = "获取当前弹出公告列表失败，请求响应超时"
# 邮件
CodeMailNewItemTooLong = 201
ErrorText[CodeMailNewItemTooLong] = "发送邮件失败，一封邮件最多发送%d种物品"%MailItemLimit
CodeMailNewItemWrong = 202
ErrorText[CodeMailNewItemWrong] = "发送邮件失败，附件物品格式错误"
CodeMailNewEmptyParam = 203
ErrorText[CodeMailNewEmptyParam] = "发送邮件失败，标题、内容与目标玩家uid不能为空"
CodeMailNewTextOverLimit = 204
ErrorText[CodeMailNewTextOverLimit] = "发送邮件失败，标题限制%s字、正文限制%s字"%(MailTitleLimit, MailContentLimit)
CodeMailNewDatabaseFail = 205
ErrorText[CodeMailNewDatabaseFail] = "发送邮件失败，数据库插入数据失败"
CodeMailNewTimeout = 206
ErrorText[CodeMailNewTimeout] = "发送邮件失败，请求响应超时"
CodeMailGroupEmptyParam = 207
ErrorText[CodeMailGroupEmptyParam] = "发送群邮件失败，标题、内容不能为空"
CodeMailGroupTextOverLimit = 208
ErrorText[CodeMailGroupTextOverLimit] = "发送群邮件失败，标题限制%s字、正文限制%s字"%(MailTitleLimit, MailContentLimit)
CodeMailGroupTimeout = 209
ErrorText[CodeMailGroupTimeout] = "发送群邮件失败，请求响应超时"
CodeMailGroupDatabaseFail = 210
ErrorText[CodeMailGroupDatabaseFail] = "发送群邮件失败，数据库插入数据失败"
CodeMailRegEmptyParam = 211
ErrorText[CodeMailRegEmptyParam] = "用户注册失败，需要提供玩家uid"
CodeMailRegTimeout = 212
ErrorText[CodeMailRegTimeout] = "用户注册失败，请求响应超时"
CodeMailRegDatabaseFail = 213
ErrorText[CodeMailRegDatabaseFail] = "用户注册失败，数据库插入数据失败"
CodeMailListQueryUserDbFail = 214
ErrorText[CodeMailListQueryUserDbFail] = "获取邮件列表失败，获取用户注册信息失败"
CodeMailListUpdateSyncFail = 215
ErrorText[CodeMailListUpdateSyncFail] = "获取邮件列表失败，同步群邮件转化信息失败"
CodeMailListSyncGroup = 216
ErrorText[CodeMailListSyncGroup] = "获取邮件列表失败，转化群邮件为个人邮件失败"
CodeMailListQueryCount = 217
ErrorText[CodeMailListQueryCount] = "获取邮件列表失败，无法取得邮件数量"
CodeMailListQueryDetail = 218
ErrorText[CodeMailListQueryDetail] = "获取邮件列表失败，从数据库拉取邮件详情失败"
CodeMailListTimeout = 219
ErrorText[CodeMailListTimeout] = "获取邮件列表失败，请求响应超时"
CodeMailListEmptyParam = 220
ErrorText[CodeMailListEmptyParam] = "获取邮件列表失败，参数uid和mailId不能为空"
CodeMailReadEmptyParam = 221
ErrorText[CodeMailReadEmptyParam] = "设置邮件已读失败，参数uid和mailIds不能为空"
CodeMailReadTimeout = 222
ErrorText[CodeMailReadTimeout] = "设置邮件已读失败，请求响应超时"
CodeMailReadDatabaseFail = 223
ErrorText[CodeMailReadDatabaseFail] = "设置邮件已读失败，修改数据库记录失败"
CodeMailReadOverLimit = 224
ErrorText[CodeMailReadOverLimit] = "设置邮件已读失败，单次修改的记录不能超过%d条"%MailReadOnceLimit
CodeMailBonusTimeout = 225
ErrorText[CodeMailBonusTimeout] = "领取邮件附件失败，请求响应超时"
CodeMailBonusEmptyParam = 226
ErrorText[CodeMailBonusEmptyParam] = "领取邮件附件失败，参数uid和mailIds不能为空"
CodeMailBonusOverLimit = 227
ErrorText[CodeMailBonusOverLimit] = "领取邮件附件失败，单次领取的邮件不能超过%d条"%MailBonusOnceLimit
CodeMailBonusQueryDatabaseFail = 228
ErrorText[CodeMailBonusQueryDatabaseFail] = "领取邮件附件失败，从数据库拉取目标邮件失败"
CodeMailBonusFindFail = 229
ErrorText[CodeMailBonusFindFail] = "领取邮件附件失败，目标邮件不存在或已经过期"
CodeMailBonusAlreadyGet = 230
ErrorText[CodeMailBonusAlreadyGet] = "领取邮件附件失败，目标邮件的物品已经领取过了"
CodeMailBonusTooFast = 231
ErrorText[CodeMailBonusTooFast] = "领取邮件附件失败，上次领取附件尚未完成，请勿连续操作"
CodeMailBonusUpdateDatabaseFail = 232
ErrorText[CodeMailBonusUpdateDatabaseFail] = "领取邮件附件失败，更新数据库状态失败"
CodeMailBonusBagFull = 233
ErrorText[CodeMailBonusBagFull] = "领取邮件附件失败，背包空位不足"
CodeMailReleaseLockTimeout = 234
ErrorText[CodeMailReleaseLockTimeout] = "释放领取附件锁失败，请求响应超时"
CodeMailReleaseLockEmptyParam = 235
ErrorText[CodeMailReleaseLockEmptyParam] = "释放领取附件锁失败，参数uid不能为空"
CodeMailDelTimeout = 236
ErrorText[CodeMailDelTimeout] = "删除指定邮件失败，请求响应超时"
CodeMailDelEmptyParam = 237
ErrorText[CodeMailDelEmptyParam] = "删除指定邮件失败，参数uid和mailIds不能为空"
CodeMailDelOverLimit = 238
ErrorText[CodeMailDelOverLimit] = "删除指定邮件失败，单次删除的邮件不能超过%d条"%MailDelOnceLimit
CodeMailDelDatabaseFail = 239
ErrorText[CodeMailDelDatabaseFail] = "删除指定邮件失败，删除数据库记录失败"
CodeMailCleanTimeout = 240
ErrorText[CodeMailCleanTimeout] = "删除无用邮件失败，请求响应超时"
CodeMailCleanEmptyParam = 241
ErrorText[CodeMailCleanEmptyParam] = "删除无用邮件失败，参数uid不能为空"
CodeMailCleanDatabaseFail = 242
ErrorText[CodeMailCleanDatabaseFail] = "删除无用邮件失败，删除数据库记录失败"
CodeMailAddItemListLengthLimit = 243
ErrorText[CodeMailAddItemListLengthLimit] = "发送邮件失败，附件数据太大了，请分多封邮件发送"

def ReloadErrorText():
	global ErrorText
	ErrorText[CodeLoginTextOverLimit] = "新建登录弹窗失败，title限制%s字、content限制%s字" % (LoginPopupTitleLimit, LoginPopupContentLimit)
	ErrorText[CodeFloatingTextOverLimit] = "新建弹出公告失败，content限制%s字" % FloatWinContentLimit
	ErrorText[CodeMailNewItemTooLong] = "发送邮件失败，一封邮件最多发送%d种物品" % MailItemLimit
	ErrorText[CodeMailNewTextOverLimit] = "发送邮件失败，标题限制%s字、正文限制%s字" % (MailTitleLimit, MailContentLimit)
	ErrorText[CodeMailGroupTextOverLimit] = "发送群邮件失败，标题限制%s字、正文限制%s字" % (MailTitleLimit, MailContentLimit)
	ErrorText[CodeMailReadOverLimit] = "设置邮件已读失败，单次修改的记录不能超过%d条" % MailReadOnceLimit
	ErrorText[CodeMailBonusOverLimit] = "领取邮件附件失败，单次领取的邮件不能超过%d条" % MailBonusOnceLimit
	ErrorText[CodeMailDelOverLimit] = "删除指定邮件失败，单次删除的邮件不能超过%d条" % MailDelOnceLimit