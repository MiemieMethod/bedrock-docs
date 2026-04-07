# -*- coding:utf-8 -*-

from neteaseBattleScript.battleCommon.battleConsts import GameObjType
from neteaseBattleScript.battleCommon.battleGameObj import GameObj
import neteaseBattleScript.battleCommon.battleConsts as battleConsts
import client.extraClientApi as clientApi
import json


def post_json_loads(p_object):
	# python2的json读取默认转换成utf8的方法
	if isinstance(p_object, dict):
		return {post_json_loads(key): post_json_loads(value) for key, value in p_object.iteritems()}
	elif isinstance(p_object, list):
		return [post_json_loads(item) for item in p_object]
	elif isinstance(p_object, unicode):
		return p_object.encode('utf-8')
	else:
		return p_object

# 再定一个方法代替json.loads
json_loads = lambda s, encoding=None, cls=None, object_hook=None, parse_float=None, parse_int=None, parse_constant=None, object_pairs_hook=None, **kwargs: post_json_loads(json.loads(s, encoding, cls, object_hook, parse_float, parse_int, parse_constant, object_pairs_hook, **kwargs))

class BattleEquip(GameObj):
	"""
	gameobjmgr可管理的游戏对象
	装备实体类
	对应了装备物品
	存放从引擎通过GetPlayerItem获取的信息
	"""
	def __init__(self, guid, objType=GameObjType.Equip):
		super(BattleEquip, self).__init__(guid, objType)

	def OnCreate(self, name, auxValue):
		super(BattleEquip, self).OnCreate(name, auxValue)
		self.SetEntityName(battleConsts.GetEquipDefinedName(name))
		# 客户端的attrBase直接从服务端传输过来
		# self.mAttrBase = battleConsts.GetEquipAttrBase(self.mFullName)

	def GetAttribute(self, attrName):
		base = super(BattleEquip, self).GetAttribute(attrName)
		try:
			data = json_loads(self.GetItemDict()['extraId'].strip() or '{}')
			for k in data:
				if k.startswith('calculator:'):
					calculator = clientApi.GetSystem(k[len('calculator:'):], "calc")
					if calculator:
						base += calculator.calc(*data[k]).get(attrName, 0)
		except:
			import traceback
			traceback.print_exc()
		return base

	def GetItemDict(self):
		itemDict = {
			"itemName": self.mMcName,
			"auxValue": self.mAuxValue,
			"count": 1,
			"enchantData": self.mExtraDataDict.get("enchantData", []),
			"customTips": self.mExtraDataDict.get("customTips", ""),
			"extraId": self.mExtraDataDict.get("extraId", ""),
		}
		if self.mExtraDataDict.has_key("durability"):
			itemDict["durability"] = self.mExtraDataDict["durability"]
		if 'userData' in self.mExtraDataDict:
			itemDict["userData"] = self.mExtraDataDict["userData"]
		return itemDict
