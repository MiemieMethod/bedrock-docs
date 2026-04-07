# -*- coding:utf-8 -*-

from neteaseBattleScript.battleCommon.battleConsts import GameObjType
from neteaseBattleScript.battleCommon.battleGameObj import GameObj
import neteaseBattleScript.battleCommon.battleConsts as battleConsts

class BattleBullet(GameObj):
	"""
	gameobjmgr可管理的游戏对象
	对应了引擎的弹射物对象
	id即为引擎弹射物的id
	"""

	def __init__(self, guid, objType=GameObjType.Bullet):
		super(BattleBullet, self).__init__(guid, objType)

	# 飞射物设计上直接继承发射者的属性（防御类属性事实上无效）
	# 重新赋值是为了防止命中时，发射者已经被删除了
	def OnCreateByInherit(self, parent):
		self.mAttrBase = {}
		for attrName in battleConsts.ExtraAttrNames.iterkeys():
			self.mAttrBase[attrName] = parent.GetAttribute(attrName)

	def PackForSync(self):
		# 类似序列化
		base = super(BattleBullet, self).PackForSync()
		base["mAttrBase"] = self.mAttrBase
		return base

	def UnPackFromSync(self, data):
		# 类似反序列化
		suc = super(BattleBullet, self).UnPackFromSync(data)
		self.mAttrBase = data["mAttrBase"]
