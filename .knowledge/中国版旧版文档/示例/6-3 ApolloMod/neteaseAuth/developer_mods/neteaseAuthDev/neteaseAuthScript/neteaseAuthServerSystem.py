# -*- coding: utf-8 -*-

import server.extraServerApi as serverApi  # MODSDK提供的服务端库模块

ServerSystem = serverApi.GetServerSystemCls()  # MODSDK提供的服务端基类
import logout  # 用于统一输出日志的模块
import netgame.apolloCommon.commonNetgameApi as commonNetgameApi  # Apollo提供的网络游戏api模块
from authManager import AuthManager  # 权限管理封装类
from mysqlOperation import MysqlOperation  # 数据库操作封装类
import authConsts as authConsts  # 一些常量配置
from coroutineMgrGas import CoroutineMgr  # 生成器管理器
import apolloCommon.redisPool as redisPool  # Apollo提供的redis操作模块

class ServerOpType(object):
	DEOP = 2  # 删除玩家管理员身份
	OP = 1  # 添加玩家管理员身份

class AuthServerSystem(ServerSystem):
	"""
	权限管理服务端类
	控制了引擎的聊天事件
	通过AuthManager管理玩家的权限
	实现各式权限控制操作
	例如
	欢迎文本
	聊天语句格式
	"""
	def __init__(self, namespace, systemName):
		ServerSystem.__init__(self, namespace, systemName)
		
		self.mAuthManager = AuthManager()  # 初始化权限管理封装类，一些本插件的逻辑都封装在里面
		self.mysqlMgr = MysqlOperation()  # 初始化数据库操作封装类，将代码抽离出来
		self.mCoroutineMgr = CoroutineMgr()  # 初始化生成器管理器，用于执行和管理延迟函数
		self.ListenForEvent(serverApi.GetEngineNamespace(), serverApi.GetEngineSystemName(), "ServerChatEvent",
		                    self, self.OnServerChat)  # 监听引擎的聊天事件
		self.ListenForEvent(serverApi.GetEngineNamespace(), serverApi.GetEngineSystemName(), "AddServerPlayerEvent",
	                        self,self.OnAddServerPlayer)  # 监听引擎的服务端玩家进入本服事件
		self.ListenForEvent(serverApi.GetEngineNamespace(), serverApi.GetEngineSystemName(), "DelServerPlayerEvent",
		                    self, self.OnDelServerPlayer)  # 监听引擎的服务端玩家离开本服事件
		self.ListenForEvent(authConsts.ModNameSpace, authConsts.MasterSystemName, 'OpPlayerFromMasterEvent', self,
							self.OnOpPlayerFromMasterEvent)  # 监听该Mod的master的事件
		self.ListenForEvent(serverApi.GetEngineNamespace(), serverApi.GetEngineSystemName(),
		                    "PlayerJoinMessageEvent",self, self.OnPlayerJoinMessage)  # 监听引擎“发送XXX玩家加入游戏”文本（游戏左上侧的黑底黄字的玩家进入游戏的提示）事件
		self.ListenForEvent(authConsts.ModNameSpace, authConsts.MasterSystemName, "ChangeGroupEvent",
		                    self, self.OnChangeGroup)  # 监听该Mod的master的事件
		# 玩家登录事件
		self.ListenForEvent(authConsts.ModNameSpace, authConsts.ClientSystemName, 'playerLoginEvent', self, self.OnPlayerLoginEvent)  # 监听该Mod的客户端发送上来的玩家已经在客户端处加载好
		self.Init()
		
	def OnOpPlayerFromMasterEvent(self, args):
		"""
		master推消息下来
		通知玩家的op权限被修改了
		:param args: master推送下来的数据结构，是个字典，对应了master发消息处的入参，包含玩家的uid和op权限类型
		"""
		neteaseId = args.get("neteaseId")  # 玩家的uid
		opType = args.get("opType")  # op权限枚举，对应上面两种中的一种，删除或者添加
		import lobbyGame.netgameApi as lobbyGameApi
		playerId = lobbyGameApi.GetPlayerIdByUid(neteaseId)
		comp = serverApi.CreateComponent(serverApi.GetLevelId(), "Minecraft", "command")
		if opType == ServerOpType.OP:
			comp.SetCommand("op @s", playerId)
		elif opType == ServerOpType.DEOP:
			comp.SetCommand("deop @s", playerId)

	def GetOpPlayerKey(self, uid):
		"""
		根据uid返回redis中存储的key
		:param uid: 玩家的uid
		:return: 返回格式化后的redis中的key
		"""
		return "user:op:%d" % uid
	
	def getOpPlayerCb(self, playerId, opType):
		"""
		在redis中查询玩家op权限的回调函数
		:param playerId: 玩家的playerId
		:param opType: 查询返回的op权限类型
		"""
		comp = serverApi.CreateComponent(serverApi.GetLevelId(), "Minecraft", "command")
		if opType:
			# 查询有结果，正常返回
			logout.info("getOpPlayerCb uid:%s,opType:%s", playerId, opType, type(opType), int(opType) == ServerOpType.OP)
			if int(opType) == ServerOpType.OP:
				logout.info("getOpPlayerCb1")
				comp.SetCommand("op @s", playerId)  # 有op权限
			elif int(opType) == ServerOpType.DEOP:
				logout.info("getOpPlayerCb2")
				comp = self.CreateComponent(playerId, "Minecraft", "player")
				operation = comp.GetPlayerOperation()
				if operation == 2:
					comp.SetCommand("deop @s", playerId)  # 没有op权限
				comp.SetCommand("deop @s", playerId)  # 没有op权限
		else:
			comp = self.CreateComponent(playerId, "Minecraft", "player")
			operation = comp.GetPlayerOperation()
			if operation == 2:
				comp.SetCommand("deop @s", playerId)
	
	def Update(self):
		self.mCoroutineMgr.Tick()  # 根据引擎的tick来驱动生成器管理器，达到触发延迟函数的目的，若有使用官方Mod的这个代码注意不要忘记在这加上这个调用
	
	def Init(self):
		# 该服务端mod的一些初始化时的逻辑
		modConfig = commonNetgameApi.GetModJsonConfig('neteaseAuthScript')  # 获取mod.json中的配置
		self.mAuthManager.SetParam(modConfig)  # 根据配置初始化权限管理封装类的一些参数
		self.mysqlMgr.InitMysqlDb()  # 初始化MySQL连接池
		redisPool.InitDB(30)  # 初始化redis连接池
		
	def OnChangeGroup(self, args):
		"""
		master通知权限组转变
		:param args: master推送下来的数据结构，是个字典，对应了master发消息处的入参，包含玩家的uid和authGroup权限组
		"""
		self.mAuthManager.ChangeUid2Group(args)  # 交给封装类处理逻辑
	
	def OnPlayerJoinMessage(self, args):
		"""
		引擎通知要发送“玩家xxx加入游戏”前
		"""
		self.mAuthManager.LoginAuthOperation(args)  # 交给封装类处理逻辑
	
	def OnServerChat(self, args):
		'''
		聊天
		'''
		# 聊天权限
		self.mAuthManager.ChatAuthOperation(args)
	
	def OnAddServerPlayer(self, args):
		'''
		登陆
		理论上这个方法先于OnPlayerLoginEvent执行
		'''
		#登陆载入个人的权限
		self.mAuthManager.LoadAuth(args)
		logout.verbose("OnAddServerPlayer", args)
		
	def OnPlayerLoginEvent(self, args):
		import lobbyGame.netgameApi as lobbyGameApi
		playerId = args.get("playerId")
		neteaseId = lobbyGameApi.GetPlayerUid(playerId)
		
		op_key = self.GetOpPlayerKey(neteaseId)
		redisPool.AsyncFuncWithKey(lambda conn, k: conn.get(k), op_key,
									  lambda opType: self.getOpPlayerCb(playerId, opType), op_key)  # 在redis中查该玩家的op权限
		
	def OnDelServerPlayer(self,args):
		'''
		玩家离开，删除权限
		'''
		self.mAuthManager.RemoveAuth(args['id'])
	
	def Destroy(self):
		self.UnListenForEvent(serverApi.GetEngineNamespace(), serverApi.GetEngineSystemName(), "ServerChatEvent",
		                      self, self.OnServerChat)
		self.UnListenForEvent(serverApi.GetEngineNamespace(), serverApi.GetEngineSystemName(), "AddServerPlayerEvent",
		                    self, self.OnAddServerPlayer)
		self.UnListenForEvent(serverApi.GetEngineNamespace(), serverApi.GetEngineSystemName(), "DelServerPlayerEvent",
		                    self, self.OnDelServerPlayer)
		self.UnListenForEvent(serverApi.GetEngineNamespace(), serverApi.GetEngineSystemName(),
		                    "PlayerJoinMessageEvent", self, self.OnPlayerJoinMessage)
		self.UnListenForEvent(authConsts.ModNameSpace, authConsts.MasterSystemName, "ChangeGroupEvent",
		                    self, self.OnChangeGroup)
		self.mysqlMgr.Destroy()