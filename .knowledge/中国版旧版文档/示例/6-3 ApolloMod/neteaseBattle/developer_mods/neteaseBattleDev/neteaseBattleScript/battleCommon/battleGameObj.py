# -*- coding:utf-8 -*-

from neteaseBattleScript.battleCommon.battleConsts import GameObjType
import neteaseBattleScript.battleCommon.battleConsts as battleConsts

class GameObj(object):
	"""
	通用标记类
	"""
	def __init__(self, guid, objType=GameObjType.Base):
		self.mAttrBase = {}
		self.mId = guid
		self.mGameObjType = objType
		self.mNeedTick = False
		self.mEntityName = ""
		self.mMcName = ""
		self.mAuxValue = 0
		self.mFullName = None
		self.mExtraDataDict = {}
		self.mInterestPlayers = set()
		if self.mId is None:
			raise ValueError('guid can not be None')
		if self.mGameObjType is None:
			raise ValueError('objType can not be None')

	def __str__(self):
		if self.mGameObjType == GameObjType.Player:
			return "TypePlayer %s" % self.mId
		elif self.mGameObjType == GameObjType.Mob:
			return "TypeMob %s" % self.mId
		elif self.mGameObjType == GameObjType.Bullet:
			return "TypeBullet %s" % self.mId
		else:
			return "TypeOther %s" % self.mId

	__repr__ = __str__

	def Tick(self):
		pass

	def OnCreate(self, name, auxValue):
		self.mMcName = name
		self.mAuxValue = auxValue
		self.mFullName = battleConsts.GetEquipFullName(name, auxValue)

	def SaveExtraData(self, dataDict):
		self.mExtraDataDict = dataDict

	def GetExtraData(self):
		return self.mExtraDataDict

	def GetId(self):
		return self.mId

	def GetGameObjType(self):
		return self.mGameObjType

	def GetInterested(self):
		return self.mInterestPlayers

	def AddInterest(self, playerId):
		self.mInterestPlayers.add(playerId)

	def DiscardInterest(self, playerId):
		self.mInterestPlayers.discard(playerId)

	def HasHp(self):
		return False

	def SetDie(self):
		raise NotImplementedError

	def SetKnockBack(self, xd=0.1, zd=0.1, power=0.5, height=0.3, heightCap=1.0):
		raise NotImplementedError

	def SetEntityName(self, entityName):
		self.mEntityName = entityName

	def GetAttrBase(self):
		return self.mAttrBase

	def GetAttribute(self, attrName):
		return self.mAttrBase[attrName]

	def __setattr__(self, key, value):
		if battleConsts.ExtraAttrNames.has_key(key):
			raise "setattr [%s] for [%s] fail, cannot changed attr" % (key, self.mMcName)
		super(GameObj, self).__setattr__(key, value)

	def __getattr__(self, key):
		if battleConsts.ExtraAttrNames.has_key(key):
			return self.GetAttribute(key)
		return getattr(self, key)

	def Destroy(self):
		pass

	def PackForSync(self):
		return {
			"mId": self.mId,
			"mGameObjType": self.mGameObjType,
			"mMcName": self.mMcName,
			"mAuxValue": self.mAuxValue,
			"mExtraDataDict": self.mExtraDataDict,
			"mAttrBase": self.mAttrBase,
		}

	def UnPackFromSync(self, data):
		self.mId = data["mId"]
		self.mGameObjType = data["mGameObjType"]
		self.mAttrBase = data["mAttrBase"]
		self.OnCreate(data["mMcName"], data["mAuxValue"])
		self.SaveExtraData(data["mExtraDataDict"])

	def PackForUpdate(self):
		return self.mId, {}

	def UnPackFromUpdate(self, data):
		pass

