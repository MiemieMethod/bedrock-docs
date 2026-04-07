# -*- coding: utf-8 -*-

from neteaseBattleScript.battleCommon.battleGameObjMgr import GameObjMgr
from neteaseBattleScript.battleCommon.battleConsts import CInterEvent
import neteaseBattleScript.battleCommon.battleConsts as battleConsts
import neteaseBattleScript.battleCommon.apiUtil as apiUtil
from neteaseBattleScript.battleCommon.battleConsts import GameObjType
import neteaseBattleScript.battleCommon.battleMob as battleMob
import neteaseBattleScript.battleCommon.battlePlayer as battlePlayer
import neteaseBattleScript.battleCommon.battleBullet as battleBullet
import neteaseBattleScript.battleCommon.battleEquip as battleEquip

class GameObjMgrClient(GameObjMgr):
	"""
	客户端游戏对象管理类
	管理游戏实体生命周期
	"""
	def __init__(self):
		super(GameObjMgrClient, self).__init__()
		self.mHasSendEnter = False
		self.mNeedAddObjs = set()
		self.mNeedDiscardObjs = set()
		self.mInterestObjs = set()

	def Init(self):
		apiUtil.GetClientSystem().RegisterClientEvent("ActorAcquiredItemClientEvent", self, self.OnPlayerGetItem)  # 监听引擎事件
		apiUtil.GetClientSystem().RegisterClientEvent("AddEntityEvent", self, self.OnAddEntity)  # 监听引擎事件
		apiUtil.GetClientSystem().RegisterClientEvent("AddPlayerEvent", self, self.OnAddPlayer)  # 监听引擎事件
		apiUtil.GetClientSystem().RegisterInterEvent(CInterEvent.UIInitFinish, self.OnUIInitFinish)  # 监听引擎事件

	def Destroy(self):
		apiUtil.GetClientSystem().UnRegisterClientEvent("ActorAcquiredItemClientEvent", self, self.OnPlayerGetItem)
		apiUtil.GetClientSystem().UnRegisterClientEvent("AddEntityEvent", self, self.OnAddEntity)
		apiUtil.GetClientSystem().UnRegisterClientEvent("AddPlayerEvent", self, self.OnAddPlayer)
		apiUtil.GetClientSystem().UnRegisterInterEvent(CInterEvent.UIInitFinish, self.OnUIInitFinish)
		super(GameObjMgrClient, self).DelAllObj()  # 清除所有实体的引用

	def Tick(self, frame):
		if not self.mHasSendEnter:  # UI初始化好了才等于玩家视觉上进入游戏，这时候再开始tick逻辑
			return
		if frame % 5 == 0:
			self.DoCheckDisappear()
		if self.mNeedAddObjs or self.mNeedDiscardObjs:
			playerId = apiUtil.GetClientSystem().GetLocalPlayer()
			apiUtil.GetClientSystem().GetRpcUtil().ServerRpc().DeclearInterest(playerId, list(self.mNeedAddObjs), list(self.mNeedDiscardObjs))  # 客户端感兴趣的实体才让服务端同步下来，不关心的都删除掉
			self.mNeedAddObjs = set()
			self.mNeedDiscardObjs = set()
	#---------------------------------------------------------------------------------------
	def CreateGameObj(self, guid, objType):
		if objType == GameObjType.Mob:
			return battleMob.BattleMob(guid, objType)
		elif objType == GameObjType.Player:
			return battlePlayer.BattlePlayer(guid, objType)
		elif objType == GameObjType.Bullet:
			return battleBullet.BattleBullet(guid, objType)
		elif objType == GameObjType.Equip:
			return battleEquip.BattleEquip(guid, objType)
		else:
			print "CreateGameObj fail objType=%s guid=%s" % (objType, guid)
			return None

	def DoCheckDisappear(self):
		"""
		某些实体离开玩家太远了就会取不到pos
		这样也没必要管理了因为太远本身也看不见
		于是清除一些过远的实体
		即可减少一些tick的负荷
		"""
		for entityId in self.mInterestObjs:
			comp = apiUtil.GetClientSystem().CreateComponent(entityId, "Minecraft", "pos")
			if not comp:
				self.mNeedDiscardObjs.add(entityId)
				continue
			entityPos = comp.GetPos()
			if not entityPos:
				self.mNeedDiscardObjs.add(entityId)
		for entityId in self.mNeedDiscardObjs:
			self.mInterestObjs.discard(entityId)
	# ---------------------------------------------------------------------------------------
	def OnUIInitFinish(self, data):
		print "OnUIInitFinish", data
		self.mHasSendEnter = True  # 可以开始tick了

	def OnPlayerGetItem(self, data):
		print "OnPlayerGetItem", data
		actor = data["actor"]
		apiUtil.GetClientSystem().GetRpcUtil().ServerRpc().NotifyPlayerGetItem(apiUtil.GetClientSystem().GetLocalPlayer(), actor)  # 捡到道具了，通知服务端刷新背包

	def OnAddEntity(self, data):
		# 客户端有实体加入
		entityId = data["id"]
		self.mNeedAddObjs.add(entityId)  # 需要新建
		self.mInterestObjs.add(entityId)  # 需要保持检查是否离开过远

	def OnAddPlayer(self, data):
		# 同上
		playerId = data["id"]
		self.mNeedAddObjs.add(playerId)
		self.mInterestObjs.add(playerId)

	def OnSyncGameObj(self, data):
		"""
		服务端通过这里告知客户端已经创建了一个实体
		将实体的id和数据同步下来让客户端初始化
		"""
		entity = self.CreateGameObj(data["mId"], data["mGameObjType"])
		if not entity:
			print "ERROR OnSyncGameObj empty entity", data
			return
		entity.UnPackFromSync(data)  # 同步数据
		oldEntity = self.GetObject(data["mId"])
		if oldEntity:
			self.UpdateObject(entity)
			#print "OnSyncGameObj UpdateOld %s" % entity
		else:
			self.AddObject(entity)
			#print "OnSyncGameObj Add %s" % entity

	def OnUpdateGameObj(self, guid, data):
		"""
		实体数据同步
		"""
		entity = self.GetObject(guid)
		if not entity:
			print "ERROR OnUpdateGameObj empty entity", guid, data
			return
		entity.UnPackFromUpdate(data)  # 同步数据
		print "OnUpdateGameObj %s" % entity
		if entity.GetGameObjType() & GameObjType.Mob == GameObjType.Mob:
			print "maxHp=%s recentHp=%s" % (entity.propMaxHp, entity.propRecentHp)


