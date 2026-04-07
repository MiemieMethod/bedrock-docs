# -*- coding:utf-8 -*-

import server.extraServerApi as extraServerApi
from neteaseBattleScript.battleCommon.battleConsts import GameObjType
from neteaseBattleScript.battleCommon.battleGameObj import GameObj
import neteaseBattleScript.battleCommon.battleConsts as battleConsts
import neteaseBattleScript.battleCommon.apiUtil as apiUtil

class BattleMob(GameObj):
	"""
	怪物实体
	"""
	def __init__(self, guid, objType=GameObjType.Mob):
		super(BattleMob, self).__init__(guid, objType)
		self.mAttrDirty = False
		self.mIsDie = False

	def OnCreate(self, name, auxValue):
		super(BattleMob, self).OnCreate(name, auxValue)
		# 客户端的attrBase直接从服务端传输过来
		# self.mAttrBase = battleConsts.GetMobAttrBase(name)
		self.mAttrDirty = True
		self.RebuildAttribute()
		self.propRecentHp = self.propMaxHp

	def RebuildAttribute(self):
		pass

	def HasHp(self):
		return True

	def SetRespawn(self):
		self.mIsDie = False
		self.RebuildAttribute()
		self.propRecentHp = self.propMaxHp

	def SetDie(self):
		self.mIsDie = True
		comp = apiUtil.GetServerSystem().CreateComponent(self.mId, "Minecraft", "attr")
		comp.SetAttrValue(extraServerApi.GetMinecraftEnum().AttrType.HEALTH, 0)  # 设置引擎血量为0，实体则死亡

	def SetKnockBack(self, xd=0.1, zd=0.1, power=0.5, height=0.3, heightCap=1.0):
		comp = apiUtil.GetServerSystem().CreateComponent(self.mId, "Minecraft", "action")
		comp.SetMobKnockback(xd, zd, power, height, heightCap)

	@property
	def propMaxHp(self):
		if self.mAttrDirty:
			self.RebuildAttribute()
		return int(self.GetAttribute(battleConsts.HpKey))

	@property
	def propRecentHp(self):
		if self.mAttrDirty:
			self.RebuildAttribute()
		if self.mHiddenRecentHp > self.propMaxHp:
			self.mHiddenRecentHp = self.propMaxHp
		return self.mHiddenRecentHp

	@propRecentHp.setter
	def propRecentHp(self, value):
		if self.mAttrDirty:
			self.RebuildAttribute()
		self.mHiddenRecentHp = value
		if self.mHiddenRecentHp > self.propMaxHp:
			self.mHiddenRecentHp = self.propMaxHp

	def PackForSync(self):
		base = super(BattleMob, self).PackForSync()
		base["mHiddenRecentHp"] = self.mHiddenRecentHp
		return base

	def UnPackFromSync(self, data):
		super(BattleMob, self).UnPackFromSync(data)
		self.mHiddenRecentHp = data["mHiddenRecentHp"]

	def PackForUpdate(self):
		return self.mId, {"mHiddenRecentHp":self.mHiddenRecentHp}

	def UnPackFromUpdate(self, data):
		super(BattleMob, self).UnPackFromUpdate(data)
		self.mHiddenRecentHp = data["mHiddenRecentHp"]

	def FormatStatus(self, trans=True, zero=None):
		propAttrs = []
		HpName = ""
		for attrConfig in battleConsts.ExtraAttrs:
			attrName = attrConfig["key"]
			attrValue = self.GetAttribute(attrName)
			ret = battleConsts.FormatSingleAttr(attrName, attrValue, "", trans, zero)
			if ret is None:
				continue
			name, value = ret
			if attrName == battleConsts.HpKey:
				HpName = name
			else:
				propAttrs.append((name, value))
		propAttrs.insert(0, ("当前%s" % HpName, "%s"%self.propRecentHp))
		propAttrs.insert(0, ("最大%s" % HpName, "%s"%self.propMaxHp))
		return propAttrs

	def FormatStatusWithIcon(self, trans=True, zero=None):
		propAttrs = []
		HpName = ""
		HpIcon = ""
		for attrConfig in battleConsts.ExtraAttrs:
			attrName = attrConfig["key"]
			attrIcon = attrConfig["icon"]
			attrValue = self.GetAttribute(attrName)
			ret = battleConsts.FormatSingleAttr(attrName, attrValue, "", trans, zero)
			if ret is None:
				continue
			name, value = ret
			if attrName == battleConsts.HpKey:
				HpName = name
				HpIcon = attrIcon
			else:
				propAttrs.append((name, value, attrIcon))
		propAttrs.insert(0, ("当前%s" % HpName, "%s"%self.propRecentHp, HpIcon))
		propAttrs.insert(0, ("最大%s" % HpName, "%s"%self.propMaxHp, HpIcon))
		return propAttrs





