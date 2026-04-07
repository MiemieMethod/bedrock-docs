# -*- coding: utf-8 -*-

import logout
from common.mod import Mod
from neteaseBattleScript.battleCommon.battleConsts import ModVersion, ModNameSpace, ServerSystemName, ServerSystemClsPath
import neteaseBattleScript.battleCommon.apiUtil as apiUtil

def LoadJsonConfig():
	import apolloCommon.commonNetgameApi as commonNetgameApi
	config = commonNetgameApi.GetModJsonConfig("neteaseBattleScript")
	if not config:
		return
	config = apiUtil.UnicodeConvert(config)
	import neteaseBattleScript.battleCommon.battleConsts as battleConsts
	for keyword, pyname in battleConsts.ConfigurableDefineDict.iteritems():
		if config.has_key(keyword):
			setattr(battleConsts, pyname, config[keyword])
			logout.info("change %s to %s" % (pyname, getattr(battleConsts, pyname)))
	# 属性类型列表配置
	findHpKey = False
	extraAttrMap = {}
	for idx, single in enumerate(config.get("extra_attrs", [])):
		key = single.get("key", None)
		if (not key):
			logout.error("extra_attrs wrong with index[%d], key不能为空" % idx)
			continue
		if key == battleConsts.HpKey:
			findHpKey = True
		name = single.get("name", None)
		if (not name):
			logout.error("extra_attrs wrong with index[%d], key[%s], name不能为空" % (idx, key))
			continue
		style = single.get("style", None)
		if (style not in ("float", "int")):
			logout.error("extra_attrs wrong with index[%d], key[%s], style必须是【float】或【int】" % (idx, key))
			continue
		icon = single.get("icon", "icon_attribute_02@3x")
		data = {
			"key": key,
			"name": name,
			"icon": icon,
			"style": style,
		}
		if style == "float":
			view = single.get("view", None)
			if (view not in ("百分数", "小数")):
				logout.error("extra_attrs wrong with index[%d], key[%s], view必须是【百分数】或【小数】" % (idx, key))
				continue
			viewAcc = single.get("view_acc", None)
			if type(viewAcc) != int or viewAcc < 0:
				logout.error("extra_attrs wrong with index[%d], key[%s], view_acc必须是正整数或0" % (idx, key))
				continue
			data["view"] = view
			data["view_acc"] = viewAcc
		battleConsts.ExtraAttrs.append(data)
		battleConsts.ExtraAttrNames[data["key"]] = data
		extraAttrMap[key] = style
	if not findHpKey:
		logout.error("extra_attrs wrong with no hp key defined")
	# 配置实体的初始属性
	battleConsts.EntityAttrs = {}
	entityAttrs = config.get("entity_attrs", {})
	battleConsts.EntityAttrs["default"] = {}
	for key, style in extraAttrMap.iteritems():
		battleConsts.EntityAttrs["default"][key] = apiUtil.GetFormatValue(0, style)
	if entityAttrs.has_key("default"):
		for key, value in entityAttrs["default"].iteritems():
			style = extraAttrMap.get(key, None)
			if not style:	# 无视属性列表之外的属性
				logout.error("entity_attrs[default] error, key[%s] 在属性列表中不存在" % (key, ))
				continue
			suc, error = apiUtil.CheckFormatValue(value, style)
			if not suc:
				logout.error("entity_attrs[default] error, key[%s] %s" % (key, error))
				continue
			battleConsts.EntityAttrs["default"][key] = apiUtil.GetFormatValue(value, style)
	for entityName, attrMap in entityAttrs.iteritems():
		if entityName in ("_comment", "default"):
			continue
		battleConsts.EntityAttrs[entityName] = {}
		for attrName, style in extraAttrMap.iteritems():
			attrValue = attrMap.get(attrName, None)
			if attrValue is None:
				continue
			suc, error = apiUtil.CheckFormatValue(attrValue, style)
			if not suc:
				logout.error("entity_attrs[%s] error, key[%s] %s" % (entityName, attrName, error))
				continue
			attrValue = apiUtil.GetFormatValue(attrValue, style)
			battleConsts.EntityAttrs[entityName][attrName] = attrValue
	# 装备提供的属性配置
	battleConsts.EquipAttrs = {}
	equipAttrs = config.get("equip_attrs", {})
	battleConsts.EquipAttrs["default"] = {}
	for key, style in extraAttrMap.iteritems():
		battleConsts.EquipAttrs["default"][key] = apiUtil.GetFormatValue(0, style)
	for equipName, attrMap in equipAttrs.iteritems():
		if equipName in ("_comment", "default"):
			continue
		battleConsts.EquipAttrs[equipName] = {}
		# 保存装备的自定义名
		battleConsts.EquipAttrs[equipName]["name"] = attrMap.get("name", "自定义装备")
		for attrName, style in extraAttrMap.iteritems():
			attrValue = attrMap.get(attrName, None)
			if attrValue is None:
				continue
			suc, error = apiUtil.CheckFormatValue(attrValue, style)
			if not suc:
				logout.error("equip_attrs[%s] error, key[%s] %s" % (equipName, attrName, error))
				continue
			attrValue = apiUtil.GetFormatValue(attrValue, style)
			battleConsts.EquipAttrs[equipName][attrName] = attrValue
	# 格式化提示文字
	battleConsts.ReloadErrorText()
	# 调试用代码，打印配置
	print "HpKey=%s" % battleConsts.HpKey
	for data in battleConsts.ExtraAttrs:
		print "new attr %s" % str(data)
	#
	for entityName, data in battleConsts.EntityAttrs.iteritems():
		print "hacked entity[%s] attrs" % entityName
		for k, v in data.iteritems():
			print "attr=%s value=%s" % (k, str(v))
	#
	for equipName, data in battleConsts.EquipAttrs.iteritems():
		print "hacked equip[%s] attrs" % equipName
		for k, v in data.iteritems():
			print "attr=%s value=%s" % (k, str(v))

@Mod.Binding(name=ModNameSpace, version=ModVersion)
class NeteaseBattleServer(object):
	def __init__(self):
		LoadJsonConfig()

	@Mod.InitServer()
	def initServer(self):
		print '===========================NeteaseBattle initServer==============================='
		import server.extraServerApi as extraServerApi
		self.mServerSystem = extraServerApi.RegisterSystem(ModNameSpace, ServerSystemName, ServerSystemClsPath)
		self.mServerSystem.Init()

	@Mod.DestroyServer()
	def destroyService(self):
		print '===========================NeteaseBattle destroyServer==============================='