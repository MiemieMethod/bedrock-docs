# -*- coding:utf-8 -*-

from neteaseBattleScript.battleCommon.battleConsts import GameObjType
from neteaseBattleScript.battleCommon.battleEquip import BattleEquip
from neteaseBattleScript.battleCommon.battleGameObj import GameObj
import neteaseBattleScript.battleCommon.battleConsts as battleConsts
import neteaseBattleScript.battleCommon.apiUtil as apiUtil

class BattleEmptyEquip(BattleEquip):
	def __init__(self, guid, objType=GameObjType.Equip):
		super(BattleEmptyEquip, self).__init__(guid, objType)

	def OnCreate(self, name, auxValue):
		super(BattleEmptyEquip, self).OnCreate(name, auxValue)
		self.SetEntityName(battleConsts.GetEquipDefinedName(name))
		self.mAttrBase = {}

	def GetAttribute(self, attrName):
		return 0
