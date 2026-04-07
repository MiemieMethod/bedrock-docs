# -*- coding:utf-8 -*-

from neteaseBattleScript.battleCommon.battleConsts import GameObjType, GameEquipPart
from neteaseBattleScript.battleCommon.battleMob import BattleMob
from neteaseBattleScript.battleCommon.battleEquip import BattleEquip
import neteaseBattleScript.battleCommon.apiUtil as apiUtil
import neteaseBattleScript.battleCommon.battleConsts as battleConsts
import client.extraClientApi as clientApi

class BattlePlayer(BattleMob):
	"""
	玩家实体
	"""
	def __init__(self, guid, objType=GameObjType.Player):
		super(BattlePlayer, self).__init__(guid, objType)
		self.mIsNewBee = False
		self.mAttrFinal = {}
		self.mEquipDict = {  # 装备字典，即戴在玩家身上的装备
			GameEquipPart.Helmet: None,
			GameEquipPart.Clothes: None,
			GameEquipPart.Trousers: None,
			GameEquipPart.Shoes: None,
			GameEquipPart.MainHand: None,
			GameEquipPart.OffHand: None,
			GameEquipPart.Necklace: None,
			GameEquipPart.Earrings: None,
			GameEquipPart.Belt: None,
			GameEquipPart.Ring: None,
		}
		self.mLevel = 0
		self.mBagsInfo = {}  # 服务端同步下来的背包信息

	# player的auxValue永远为零，正好用来代替等级
	def OnCreate(self, name, auxValue):
		self.mMcName = name
		self.mAuxValue = 0
		self.mLevel = auxValue
		self.mFullName = battleConsts.GetEquipFullName(name, 0)
		# 客户端的attrBase直接来自服务端
		# self.mAttrBase = battleConsts.GetPlayerAttrBase(self.mLevel)
		self.mAttrDirty = True
		self.RebuildAttribute()
		self.propRecentHp = self.propMaxHp
		# print "player OnCreate maxHp=%s Hp=%s" % (self.propMaxHp, self.propRecentHp)

	def RebuildAttribute(self):
		# 属性计算
		self.mAttrFinal = {}
		equipList = []
		for part, equip in self.mEquipDict.iteritems():
			if equip:
				equipList.append(equip)
		for attrName, attrValue in self.mAttrBase.iteritems():
			self.mAttrFinal[attrName] = attrValue
			for equip in equipList:
				self.mAttrFinal[attrName] += getattr(equip, attrName)
		self.mAttrDirty = False
		# print "player RebuildAttribute"
		# print "propMaxHp =", self.propMaxHp
		# for attrName, attrValue in self.mAttrFinal.iteritems():
		# 	print "attr[%s] value=%s" % (attrName, attrValue)

	# 玩家无法被击退
	def SetKnockBack(self, xd=0.1, zd=0.1, power=0.5, height=0.3, heightCap=1.0):
		pass

	# 玩家的属性要算上装备的
	def GetAttribute(self, attrName):
		if self.mAttrDirty:
			self.RebuildAttribute()
		_system = clientApi.GetSystem("neteaseLabel", "neteaseLabelBeh")
		if _system:
			attrInfo = _system.GetAttrInfoByPlayerId(self.GetId())
		else:
			attrInfo = {}
		return self.mAttrFinal[attrName] + attrInfo.get(attrName, 0)

	def ChangeEquip(self, part, equip):
		if equip:
			self.mEquipDict[part] = equip
		else:
			self.mEquipDict[part] = None
		self.mAttrDirty = True
		self.RebuildAttribute()

	def GetEquipByPart(self, part):
		return self.mEquipDict.get(part, None)

	def PackForSync(self):
		base = super(BattlePlayer, self).PackForSync()
		base["mLevel"] = self.mLevel
		base["mAttrFinal"] = self.mAttrFinal
		base["mEquipDict"] = {}
		for part, equip in self.mEquipDict.iteritems():
			if equip:
				base["mEquipDict"][part] = equip.PackForSync()
			else:
				base["mEquipDict"][part] = None
		return base

	def UnPackFromSync(self, data):
		super(BattlePlayer, self).UnPackFromSync(data)
		self.mLevel = data["mLevel"]
		print "UnPackFromSync mLevel={}, mAttrBase={}".format(self.mLevel, self.mAttrBase)
		self.mAttrFinal = data["mAttrFinal"]
		self.mEquipDict = {}
		for part, subData in data["mEquipDict"].iteritems():
			if subData is None:
				self.mEquipDict[part] = None
			else:
				equip = BattleEquip(1)
				equip.UnPackFromSync(subData)
				self.mEquipDict[part] = equip

	def PackForUpdate(self):
		guid, base = super(BattlePlayer, self).PackForUpdate()
		# player的attrBase会随着等级变化
		base["mLevel"] = self.mLevel
		base["mAttrBase"] = self.mAttrBase
		base["mAttrFinal"] = self.mAttrFinal
		base["mEquipDict"] = {}
		for part, equip in self.mEquipDict.iteritems():
			if equip:
				base["mEquipDict"][part] = equip.PackForSync()
			else:
				base["mEquipDict"][part] = None
		return guid, base

	def UnPackFromUpdate(self, data):
		super(BattlePlayer, self).UnPackFromUpdate(data)
		# player的attrBase会随着等级变化
		self.mLevel = data["mLevel"]
		self.mAttrBase = data["mAttrBase"]
		print "UnPackFromUpdate mLevel={} mAttrBase={}".format(self.mLevel, self.mAttrBase)
		self.mAttrFinal = data["mAttrFinal"]
		self.mEquipDict = {}
		for part, subData in data["mEquipDict"].iteritems():
			if subData is None:
				self.mEquipDict[part] = None
			else:
				equip = BattleEquip("empty")
				equip.UnPackFromSync(subData)
				self.mEquipDict[part] = equip

	def UpdateBagsInfo(self, baginfo):
		self.mBagsInfo = baginfo

	def GetBagsInfo(self):
		return self.mBagsInfo

