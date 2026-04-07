# -*- coding: utf-8 -*-
import lobbyGame.netgameApi as netgameApi
import authConsts as authConsts
import logout

class AuthManager(object):
	ADMIN_GROUP = 3
	OP_COMMAND_LIST = [authConsts.BAN_COMMAND, authConsts.UNBAN_COMMAND,
	                  authConsts.SILENT_COMMAND, authConsts.UNSILENT_COMMAND]

	def __init__(self):
		super(AuthManager, self).__init__()
		self.mGroupNames = {} #分组名字列表 {"0":"normal","1":"vip","2":"op"}
		self.mGroupAuth = {} #分组的权限
		self.mUid2Group = {} #玩家分组，服务器启动的时候load一下{uid:group}
		
	def SetParam(self, modConfig):
		self.mGroupNames = modConfig.get("group", {})
		self.mGroupAuth = modConfig.get("groupAuth", {})
		
	def SetUid2Group(self):
		'''
		设置配置信息
		'''
		def setUid2GroupCb(sqlResult):
			for resultOne in sqlResult:
				self.mUid2Group[resultOne[0]] = resultOne[1]
		authConsts.GetServerModSystem().mysqlMgr.QueryAllPlayerGroup(lambda sqlResult:setUid2GroupCb(sqlResult))
	
	def ChangeUid2Group(self, args):
		'''
		改变玩家分组
		'''
		uid = args.get("uid", -1)
		authGroup = args.get("authGroup", 0)
		self.mUid2Group[uid] = authGroup

	def _GenOPArgs(self, inputArgs):
		try:
			op = inputArgs[1]
			opArgs = {'op' : op}
			if authConsts.BAN_COMMAND == op:
				if len(inputArgs) < 3:
					return None
				opArgs['nickname'] = inputArgs[2]
				opArgs['banTime'] = int(inputArgs[3]) if len(inputArgs) >= 4 else -1
				opArgs['reason'] = inputArgs[4] if len(inputArgs) >= 5 else '被超级管理员封禁'
			elif authConsts.UNBAN_COMMAND == op:
				if len(inputArgs) < 3:
					return None
				opArgs['nickname'] = inputArgs[2]
			elif authConsts.SILENT_COMMAND == op:
				if len(inputArgs) < 3:
					return None
				opArgs['nickname'] = inputArgs[2]
				opArgs['banTime'] = int(inputArgs[3]) if len(inputArgs) >= 4 else -1
				opArgs['reason'] = inputArgs[4] if len(inputArgs) >= 5 else '被超级管理员禁言'
			elif authConsts.UNSILENT_COMMAND == op:
				if len(inputArgs) < 3:
					return None
				opArgs['nickname'] = inputArgs[2]
			return opArgs
		except:
			return None
	
	def ChatAuthOperation(self, args):
		'''
		聊天权限
		'''
		playerId = args["playerId"]
		uid = netgameApi.GetPlayerUid(playerId)
		# admin 账号，允许执行指令
		if self.IsAdmin(uid):
			message = args["message"].strip()
			messageArgs = [one.strip() for one in message.split()]
			if len(messageArgs) >= 2 and "op" == messageArgs[0] and messageArgs[1] in self.OP_COMMAND_LIST:
				logout.info("exec op command.uid:%s.command:%s" % (uid, message))
				opArgs = self._GenOPArgs(messageArgs)
				if opArgs is None :
					logout.error("op command err.op format error.command:%s" % message)
					args["message"] = 'op指令格式不正确'
				else:
					opArgs['requestUID'] = uid
					authConsts.GetServerModSystem().NotifyToMaster("OpCommandEvent", opArgs)
					args["message"] = '执行指令:%s' % args["message"]
				args["bChatById"] = True
				args["toPlayerIds"] = [playerId]
				args["cancel"] = False
				print 'yfgtesttest', args, uid
				return
		if args.get('cancel', False):
			return
		if self.mUid2Group.has_key(uid):
			group = self.mUid2Group[uid]
		else:
			group = 0
			newAuthData = {"uid":uid,
			               "group":0 #默认是0，normal
			               }
			authConsts.GetServerModSystem().mysqlMgr.InsertPlayerGroup(uid, newAuthData)  # 默认分组加到数据库
			self.mUid2Group[uid] = group
		groupName = self.mGroupNames.get(str(group), "")
		if groupName == "":
			return
		chatAuthDict = self.mGroupAuth[groupName].get("chat", None)
		if chatAuthDict == None:
			return
		userName = args["username"]
		message = args["message"]
		args["username"] = ""  # 修改原版消息，去掉原版玩家名字
		args["message"] = ""
		if chatAuthDict.has_key("chatPrefix"):
			args["message"] = args["message"] + chatAuthDict["chatPrefix"].encode("utf-8") + "§r"  # 添加名字前缀
		args["message"] = args["message"] + "<"
		args["message"] = args["message"] + userName  # 给玩家名字拼个'<>'
		args["message"] = args["message"] + ">"
		if chatAuthDict.has_key("chatSuffix"):
			args["message"] = args["message"] + chatAuthDict["chatSuffix"].encode("utf-8") + "§r"  # 添加名字后缀
		args["message"] = args["message"] + " : " + message
		
	def NotifyMsg(self, playerId, message, delayTime = 0):
		"""
		延迟弹出欢迎语句
		"""
		yield -30 * delayTime
		comp = authConsts.GetServerModSystem().CreateComponent(playerId, "Minecraft", "game")
		comp.SetNotifyMsg(message)
	
	def LoadAuth(self,args):
		'''
		载入单人权限
		'''
		def getPlayerGroupCb(uid, result, useMysql):
			if len(result) <= 0:
				#如果没搜到，则给默认值
				authGroup = 0
				newAuthData = {"uid":uid,
				               "authGroup":0 #默认是0，normal
				               }
				authConsts.GetServerModSystem().mysqlMgr.InsertPlayerGroup(uid, newAuthData)
			else:
				authGroup = result[0][0]
			if useMysql:
				self.mUid2Group[uid] = authGroup
		playerId = args["id"]
		uid = netgameApi.GetPlayerUid(playerId)
		#玩家登陆的时候重新载入一下对应玩家的权限信息
		authConsts.GetServerModSystem().mysqlMgr.QueryPlayerGroup(uid, lambda sqlResult: getPlayerGroupCb(uid, sqlResult, True))  # 查数据库

	def RemoveAuth(self, playerId):
		'''
		删除权限
		'''
		uid = netgameApi.GetPlayerUid(playerId)
		if self.mUid2Group.has_key(uid):
			self.mUid2Group.pop(uid)

	def IsAdmin(self, uid):
		if uid not in self.mUid2Group:
			return False
		group = self.mUid2Group[uid]
		return group == self.ADMIN_GROUP
		
	def LoginAuthOperation(self,args):
		'''
		登陆欢迎语
		'''
		def getPlayerGroupCb(args,uid,userName,result,useMysql):
			if len(result) <= 0:
				#如果没搜到，则给默认值
				authGroup = 0
				newAuthData = {"uid":uid,
				               "authGroup":0 #默认是0，normal
				               }
				authConsts.GetServerModSystem().mysqlMgr.InsertPlayerGroup(uid,newAuthData)
			else:
				authGroup = result[0][0]
			if useMysql:
				self.mUid2Group[uid] = authGroup
			groupName = self.mGroupNames.get(str(authGroup), "")
			if groupName == "":
				return
			loginAuthDict = self.mGroupAuth[groupName].get("login", None)
			if loginAuthDict == None:
				return
			welcomeMessage = loginAuthDict.get("welcomeMessage", "").encode("utf-8")
			welMesDelayTime = loginAuthDict.get("welMesDelayTime", 0)
			if welcomeMessage != "":
				# 至此表示所有验证通过可以播放欢迎消息
				welcomeMessage = welcomeMessage.replace("%s", userName)
				authConsts.GetServerModSystem().mCoroutineMgr.StartCoroutine(self.NotifyMsg(playerId, welcomeMessage, welMesDelayTime))
		#取消聊天事件
		args["cancel"] = True
		playerId = args["id"]
		userName = netgameApi.GetPlayerNickname(playerId)
		uid = netgameApi.GetPlayerUid(playerId)
		if self.mUid2Group.has_key(uid):
			#内存有，直接读取
			group = self.mUid2Group[uid]
			getPlayerGroupCb(args, uid,userName,((group,),),False)  # 把参数拼出来直接调用后续逻辑
		else:
			#内存没有，从数据库里读
			authConsts.GetServerModSystem().mysqlMgr.QueryPlayerGroup(uid, lambda sqlResult: getPlayerGroupCb(args, uid, userName, sqlResult, True))