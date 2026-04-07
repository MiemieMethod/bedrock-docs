# -*- coding: utf-8 -*-
import server.extraServerApi as extraServerApi
ServerSystem = extraServerApi.GetServerSystemCls()
import lobbyGame.netgameApi as netgameApi
import apolloCommon.commonNetgameApi as commonNetgameApi
import logout
import neteaseCloudScript.playerMgr as playerMgr  # 玩家封装模块，里面有一些玩家相关的逻辑
import neteaseCloudScript.itemSyncAction as itemSyncAction  # 玩家物品相关操作封装模块
import apolloCommon.mysqlPool as mysqlPool
import neteaseCloudScript.cloudConsts as cloudConsts
import neteaseCloudScript.engineApi as engineApi
import lobbyGame.netgameApi as lobbyGameApi
from neteaseCloudScript.cloudConsts import ProcessType

class CloudServerSystem(ServerSystem):
	"""
	该mod的服务端
	根据不同类型的配置策略同步玩家数据
	存储玩家数据至数据库
	"""

	def __init__(self, namespace, systemName):
		ServerSystem.__init__(self, namespace, systemName)
		print 'init CloudServerSystem', namespace, systemName
		playerMgr.Init(self)  # 添加该服务端mod对象的引用
		engineApi.SetServerSystem(self)  # 添加该服务端mod对象的引用
		self.ListenForEvent(extraServerApi.GetEngineNamespace(), extraServerApi.GetEngineSystemName(),
							"AddServerPlayerEvent", self, self.OnAddServerPlayer)
		self.ListenForEvent(extraServerApi.GetEngineNamespace(), extraServerApi.GetEngineSystemName(),
							"EntityRemoveEvent", self, self.OnEntityRemove)
		self.ListenForEvent(cloudConsts.ModNameSpace, cloudConsts.MasterSystemName,
							cloudConsts.SetUserInventoryEvent, self, self.OnSetUserInventory)
		self.ListenForEvent(cloudConsts.ModNameSpace, cloudConsts.ClientSystemName,
							cloudConsts.LoginCloudServerEvent, self, self.OnLoginCloudServer)
		self.Init()

	def Init(self):
		modJson = commonNetgameApi.GetModJsonConfig("neteaseCloudScript")
		serverType = commonNetgameApi.GetServerType()
		self.mServerConf = modJson['servers_conf'].get(serverType, None)
		self.mApplyTag = self.mServerConf.get('apply_tag', "")
		mysqlPool.InitDB(30)
		if self.mServerConf is None:
			# 本服没有任何配置
			self.mCloudAction = None
		else:
			self.mCloudAction = itemSyncAction.CreateSyncAction(self.mServerConf)

	def OnLoginCloudServer(self, data):
		# 客户端登入，要求同步数据
		playerId = data['playerId']
		uid = lobbyGameApi.GetPlayerUid(playerId)
		if self.mCloudAction:
			self.mCloudAction.Login(uid)

	def OnSetUserInventory(self, data):
		import copy
		uid = data['uid']
		playerId = lobbyGameApi.GetPlayerIdByUid(uid)
		if not playerId:
			data['user_exit'] = False
			self.NotifyToMaster(cloudConsts.SetUserInventoryResultEvent, data)
			return
		if self.mApplyTag != data.get("apply_tag", ""):
			return
		data['user_exit'] = True
		inventory = copy.deepcopy(data['inventory'])
		itemsDict = {
			data['slot'] : inventory
		}
		if self.mServerConf and self.mServerConf.get('process_type', 0) == ProcessType.CLOUD_ACTION:
			suc = engineApi.SpawnItemsToPlayerInv(itemsDict, playerId, uid)
		else:
			data['user_exit'] = False
			self.NotifyToMaster(cloudConsts.SetUserInventoryResultEvent, data)
			return
		data['suc'] = suc
		self.NotifyToMaster(cloudConsts.SetUserInventoryResultEvent, data)

	def OnAddServerPlayer(self, data):
		# 玩家登入，记录一下玩家的id
		playerId = data['id']
		playerMgr.instanceMgr.Login(playerId, data['uid'])

	def OnDelServerPlayer(self, data):
		# 玩家登出
		uid = data['uid']
		playerId = data['id']
		playerMgr.instanceMgr.Logout(playerId, uid)

	def OnEntityRemove(self, data):
		# 实体清除的时候触发
		# 理论上玩家实体是不会清除的
		# 除了玩家登出的时候
		# 所以可以将下面的逻辑写到上面玩家登出
		# 但若有后续扩展需求可在这个事件处理一些其他实体的保存逻辑
		entityId = data['id']
		uid = playerMgr.instanceMgr.GetPlayerUid(entityId)
		if uid is None:
			return
		if self.mCloudAction:
			self.mCloudAction.Logout(uid)

	def Destroy(self):
		if self.mCloudAction:
			self.mCloudAction.Destroy()
		self.mCloudAction = None
		playerMgr.instanceMgr.Destroy()
		self.UnListenForEvent(extraServerApi.GetEngineNamespace(), extraServerApi.GetEngineSystemName(),
							"AddServerPlayerEvent", self, self.OnAddServerPlayer)
		self.UnListenForEvent(extraServerApi.GetEngineNamespace(), extraServerApi.GetEngineSystemName(),
							"DelServerPlayerEvent", self, self.OnDelServerPlayer)
		self.UnListenForEvent(cloudConsts.ModNameSpace, cloudConsts.MasterSystemName,
							cloudConsts.SetUserInventoryEvent, self, self.OnSetUserInventory)
		self.UnListenForEvent(extraServerApi.GetEngineNamespace(), extraServerApi.GetEngineSystemName(),
							"EntityRemoveEvent", self, self.OnEntityRemove)
		self.UnListenForEvent(cloudConsts.ModNameSpace, cloudConsts.ClientSystemName,
							cloudConsts.LoginCloudServerEvent, self, self.OnLoginCloudServer)
