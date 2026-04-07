# -*- coding: utf-8 -*-
# 一些配置相关
# 一些属性相关的函数
# 例如格式化属性文本显示等


#---------------------------------------------------------------------------------------
# 整个Mod的一些绑定配置
ModVersion = "1.0.3"
ModNameSpace = "neteaseBattle"
ClientSystemName = "neteaseBattleBeh"
ClientSystemClsPath = "neteaseBattleScript.battleClientSystem.BattleClientSystem"
ServerSystemName = "neteaseBattleDev"
ServerSystemClsPath = "neteaseBattleScript.battleServerSystem.BattleServerSystem"

GemInlayModNameSpace = "neteaseGemInlay"
GemInlayClientSystemName = "neteaseGemInlayBeh"
GemInlayServerSystemName = "neteaseGemInlayDev"
#---------------------------------------------------------------------------------------
HpKey = ""					# 生命上限属性字符串ID
DestroyWhenHp0 = True		# 生命为零时是否杀死实体
KeepHpFull = True			# 是否维持玩家原生血量为满
CanUseShowInfo = True		# 是否支持使用【@op showinfo】指令输出范围5以内的实体属性
HelmetItems = []			# 可以装备在头部的装备列表
ClothesItems = []			# 可以装备在胸部的装备列表
TrousersItems = []			# 可以装备在下裤的装备列表
ShoesItems = []				# 可以装备在脚部的装备列表
OffhandItems = []			# 可以装备在副手的装备列表
NecklaceItems = []			# 项链装备位可装备物品列表
EarringsItems = []			# 耳环装备位可装备物品列表
BeltItems = []				# 腰带装备位可装备物品列表
RingItems = []				# 耳环装备位可装备物品列表
#
ExtraAttrs = []				# 属性类型列表配置
ExtraAttrNames = {}			# 属性类型名的字典
EntityAttrs = {}			# 实体的初始属性
EquipAttrs = {}				# 装备提供的属性配置
#
IsPeaceMode = False			# 是否是和平模式（lobby等环境，可以替换装备但是无法造成伤害）
PlayerStatusChangeWithLevel	= True	# 玩家属性是否与等级相关
ShowStatusBtnOnDesk = True 	# 是否在主界面显示打开属性的按钮



ConfigurableDefineDict = {
	"hp_key": "HpKey",
	"destroy_when_hp0": "DestroyWhenHp0",
	"keep_hp_full": "KeepHpFull",
	"canuse_showinfo": "CanUseShowInfo",
	"helmet_items": "HelmetItems",
	"clothes_items": "ClothesItems",
	"trousers_items": "TrousersItems",
	"shoes_items": "ShoesItems",
	"offhand_items": "OffhandItems",
	"necklace_items": "NecklaceItems",
	"earrings_items": "EarringsItems",
	"belt_items": "BeltItems",
	"ring_items": "RingItems",
	"player_status_change_with_level": "PlayerStatusChangeWithLevel",
	"show_status_btn_on_desk": "ShowStatusBtnOnDesk",
}
ConfigurablePostToClient = ["HpKey", "DestroyWhenHp0", "KeepHpFull",
	"ExtraAttrs", "ExtraAttrNames", "IsPeaceMode", "PlayerStatusChangeWithLevel", "ShowStatusBtnOnDesk"]

MobAttrBaseMap = {}
EquipAttrBaseMap = {}
def GetMobAttrBase(name):
	global MobAttrBaseMap
	if MobAttrBaseMap.has_key(name):
		return MobAttrBaseMap[name]
	attrBase = {}
	for attrName, attrValue in EntityAttrs["default"].iteritems():
		attrBase[attrName] = attrValue
	if EntityAttrs.has_key(name):
		for attrName, attrValue in EntityAttrs[name].iteritems():
			attrBase[attrName] = attrValue
	MobAttrBaseMap[name] = attrBase
	return attrBase

PlayerAttrBaseWithLevelMap = {}
def SetPlayerAttrBase(level, extraAttrs):
	global PlayerAttrBaseWithLevelMap
	attrBase = {}
	for attrName, attrValue in EntityAttrs["default"].iteritems():
		attrBase[attrName] = attrValue	
	for attrName, attrValue in extraAttrs.iteritems():
		attrBase[attrName] = attrValue
	PlayerAttrBaseWithLevelMap[level] = attrBase
	return True

PlayerAttrBaseWithLevelCallback = None
def GetPlayerAttrBase(level):
	if not PlayerStatusChangeWithLevel:
		return GetMobAttrBase("player")
	global PlayerAttrBaseWithLevelMap, PlayerAttrBaseWithLevelCallback
	if PlayerAttrBaseWithLevelMap.has_key(level):
		return PlayerAttrBaseWithLevelMap[level]
	if not callable(PlayerAttrBaseWithLevelCallback):
		return GetMobAttrBase("player")
	try:
		extraAttrs = PlayerAttrBaseWithLevelCallback(level)
	except:
		import traceback
		traceback.print_stack()
		extraAttrs = {}
	attrBase = {}
	for attrName, attrValue in EntityAttrs["default"].iteritems():
		attrBase[attrName] = attrValue	
	for attrName, attrValue in extraAttrs.iteritems():
		attrBase[attrName] = attrValue
	PlayerAttrBaseWithLevelMap[level] = attrBase
	return attrBase

def GetEquipAttrBase(name):
	global EquipAttrBaseMap
	if EquipAttrBaseMap.has_key(name):
		return EquipAttrBaseMap[name]
	attrBase = {}
	for attrName, attrValue in EquipAttrs["default"].iteritems():
		attrBase[attrName] = attrValue
	if EquipAttrs.has_key(name):
		for attrName, attrValue in EquipAttrs[name].iteritems():
			attrBase[attrName] = attrValue
	EquipAttrBaseMap[name] = attrBase
	return attrBase

def GetEquipDefinedName(name, auxValue=0):
	fullName = "%s:%s" % (name, auxValue)
	if EquipAttrs.has_key(fullName):
		chName = EquipAttrs[fullName].get("name", None)
	elif EquipAttrs.has_key(name):
		chName = EquipAttrs[name].get("name", None)
	else:
		chName = None
	if not chName is None:
		return chName
	import client.extraClientApi as clientApi
	comp = clientApi.CreateComponent("", "Minecraft", "item")
	itemBaseInfo = comp.GetItemBasicInfo(name, auxValue)
	if itemBaseInfo:
		return itemBaseInfo["itemName"]
	return "未命名装备"

def IsEquip(name, auxValue=0):
	fullName = "%s:%s" % (name, auxValue)
	if EquipAttrs.has_key(fullName) or EquipAttrs.has_key(name):
		return True
	else:
		return False

def GetEquipFullName(name, auxValue):
	fullName = "%s:%s" % (name, auxValue)
	if EquipAttrs.has_key(fullName):
		return fullName
	elif EquipAttrs.has_key(name):
		return name
	return None

def FormatCustomTips(equipName, auxValue):
	fullName = GetEquipFullName(equipName, auxValue)
	attrBase = GetEquipAttrBase(fullName)
	propAttrs = []
	for attrConfig in ExtraAttrs:
		attrName = attrConfig["key"]
		ret = FormatSingleAttr(attrName, attrBase.get(attrName, 0))
		if ret is None:
			continue
		name, value = ret
		line = "%s %s " % (value, name)
		if attrName == HpKey:
			propAttrs.insert(0, line)
		else:
			propAttrs.append(line)
	chName = GetEquipDefinedName(equipName, auxValue)
	propAttrs.insert(0, " ")
	propAttrs.insert(0, chName)
	return "\n".join(propAttrs)

def GetEquipCustomAttr(itemName, auxValue):
	fullName = GetEquipFullName(itemName, auxValue)
	attrBase = GetEquipAttrBase(fullName)
	result = {}
	for attrConfig in ExtraAttrs:
		attrName = attrConfig["key"]
		attrValue = attrBase.get(attrName, 0)
		result[attrName] = attrValue
	return result
#---------------------------------------------------------------------------------------
# 客户端专属事件
class ClientSpecEvent(object):
	RpcEvent = "C2SRpcCall"

class CInterEvent(object):
	UIInitFinish = 1
	UIClosePopup = 2
	UIDeskOpen = 10
	UIDeskClose = 11
	UIDeskHealth = 12
	UIStatusOpen = 13
	UIStatusDraw = 14
	UIEnemyDraw = 15
	UIFlyAnimate = 16
	UIDeskReinit = 17

# 服务器专属事件
class ServerSpecEvent(object):
	RpcEvent = "S2CRpcCall"

class SInterEvent(object):
	ClientEnter = 1
	ClientGetItem = 2
	ClientDeclearInterest = 3
	ChangeExtraEquip = 4
	ClientEquipAction = 5
	ExchangeBagItem = 6
#---------------------------------------------------------------------------------------
# 游戏脚本中的对象
class GameObjType(object):
	Base = 0
	Mask = 0xFF
	Mob = 0x0100
	Bullet = 0x0200
	Equip = 0x0400
	Player = 1 | Mob
	EmptyEquip = 1 | Equip

# 装备部位
class GameEquipPart(object):
	Helmet = 0
	Clothes = 1
	Trousers = 2
	Shoes = 3
	MainHand = 4
	OffHand = 5
	Earrings = 6
	Necklace = 7
	Belt = 8
	Ring = 9

EquipSetArmor = (GameEquipPart.Helmet, GameEquipPart.Clothes, GameEquipPart.Trousers, GameEquipPart.Shoes)
EquipSetExtra = (GameEquipPart.Necklace, GameEquipPart.Earrings, GameEquipPart.Belt, GameEquipPart.Ring)
EquipPartToItemMap = {
GameEquipPart.Helmet: "HelmetItems",
GameEquipPart.Clothes: "ClothesItems",
GameEquipPart.Trousers: "TrousersItems",
GameEquipPart.Shoes: "ShoesItems",
GameEquipPart.OffHand: "OffhandItems",
GameEquipPart.Necklace: "NecklaceItems",
GameEquipPart.Earrings: "EarringsItems",
GameEquipPart.Belt: "BeltItems",
GameEquipPart.Ring: "RingItems",
}

def IsEquipByPart(itemName, auxValue, part):
	name = GetEquipFullName(itemName, auxValue)
	if not name:
		return False
	if part == GameEquipPart.Helmet:
		return name in HelmetItems
	elif part == GameEquipPart.Clothes:
		return name in ClothesItems
	elif part == GameEquipPart.Trousers:
		return name in TrousersItems
	elif part == GameEquipPart.Shoes:
		return name in ShoesItems
	elif part == GameEquipPart.OffHand:
		return name in OffhandItems
	elif part == GameEquipPart.Necklace:
		return name in NecklaceItems
	elif part == GameEquipPart.Earrings:
		return name in EarringsItems
	elif part == GameEquipPart.Belt:
		return name in BeltItems
	elif part == GameEquipPart.Ring:
		return name in RingItems
	else:
		return False
#---------------------------------------------------------------------------------------
def FormatSingleAttr(attrName, attrValue, plus="+", trans=True, zero=None):
	global ExtraAttrNames
	findConfig = ExtraAttrNames.get(attrName, None)
	if not findConfig:
		return None
	name = "%s" % findConfig["name"]
	if findConfig["style"] == "int":
		if attrValue == 0:
			if zero is None:
				return None
		if attrValue > 0:
			value = "%s%d" % (plus, attrValue)
		else:
			value = "%d" % attrValue
	elif findConfig["style"] == "float":
		if abs(attrValue) <= 0.00001:
			if zero is None:
				return None
			attrValue = 0.0
		if findConfig["view"] == "百分数":
			attrValue = attrValue*100
			attrValue = round(attrValue, findConfig["view_acc"])
			if attrValue > 0:
				if trans:
					value = "%s%s%%%%" % (plus, attrValue)
				else:
					value = "%s%s%%" % (plus, attrValue)
			else:
				if trans:
					value = "%s%%%%" % attrValue
				else:
					value = "%s%%" % attrValue
		elif findConfig["view"] == "小数":
			attrValue = round(attrValue, findConfig["view_acc"])
			if attrValue > 0:
				value = "%s%s" % (plus, attrValue)
			else:
				value = "%s" % attrValue
		else:
			return None
	else:
		return None
	return (name, value)
#---------------------------------------------------------------------------------------
# 错误码
ErrorText = {}
CodeSuc = 0
ErrorText[CodeSuc] = "请求成功"

def ReloadErrorText():
	global ErrorText
