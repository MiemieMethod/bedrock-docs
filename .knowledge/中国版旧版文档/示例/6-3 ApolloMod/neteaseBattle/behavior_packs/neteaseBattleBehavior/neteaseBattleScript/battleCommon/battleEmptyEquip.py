# -*- coding:utf-8 -*-

from neteaseBattleScript.battleCommon.battleConsts import GameObjType
from neteaseBattleScript.battleCommon.battleEquip import BattleEquip
from neteaseBattleScript.battleCommon.battleGameObj import GameObj
import neteaseBattleScript.battleCommon.battleConsts as battleConsts
import neteaseBattleScript.battleCommon.apiUtil as apiUtil

class BattleEmptyEquip(BattleEquip):
	"""
	空的装备类
	用于保持逻辑的一致性
	有的装备或者物品是战斗插件不关心的
	创建一个没有记录信息的空类
	用于正常管理和判断
	"""

	def __init__(self, guid, objType=GameObjType.Equip):
		super(BattleEmptyEquip, self).__init__(guid, objType)

	def OnCreate(self, name, auxValue):
		super(BattleEmptyEquip, self).OnCreate(name, auxValue)
		self.SetEntityName(battleConsts.GetEquipDefinedName(name))
		self.mAttrBase = {}

	def GetAttribute(self, attrName):
		return 0
