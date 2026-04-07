# -*- coding: utf-8 -*-

import json
import weakref
from collections import Counter

import neteaseJewelScript.jewelConst as jewelConst
import client.extraClientApi as clientApi
from mod_log import engine_logger as logger

ViewBinder = clientApi.GetViewBinderCls()
ViewRequest = clientApi.GetViewViewRequestCls()
ScreenNode = clientApi.GetScreenNodeCls()
TouchEvent = clientApi.GetMinecraftEnum().TouchEvent


class JewelScreen(ScreenNode):
	"""
	宝石镶嵌的弹出界面
	"""
	def __init__(self, namespace, name, param):
		ScreenNode.__init__(self, namespace, name, param)
		self.mUiKey = jewelConst.jewelUIName
		self.mClientSystem = None
		self.mBShow = True
		#
		self.mGemConfig = {}
		self.mEquipConfig = {}
		self.mBagEquipList = []
		self.mBagGemList = []
		self.mSelectEquip = None
		self.mFreeSlot = None
		self.mStuffCache = None
		print '==== %s ====' % 'init JewelScreen'

	def ChangeScreenVisible(self, flag):
		self.mBShow = flag
		if flag:
			if self.mClientSystem:
				self.mClientSystem.RegisterUIOpen(self.mUiKey)
		else:
			if self.mClientSystem:
				self.mClientSystem.RegisterUIClose(self.mUiKey)
		self.SetVisible("", flag)

	def GetIsShow(self):
		return self.mBShow

	# Create函数是继承自ScreenNode，会在UI创建完成后被调用
	def Create(self):
		print '==== %s ====' % 'JewelScreen Create'

		self.AddTouchEventHandler("/main_pnl/img_base/img_base_title/btn_close", self.OnClose)
		self.AddTouchEventHandler("/main_pnl/img_base/img_inset/btn_equip", self.OnClaimEquip)
		self.AddTouchEventHandler("/main_pnl/img_base/img_inset/btn_gem_0", self.OnClaimGem0)
		self.AddTouchEventHandler("/main_pnl/img_base/img_inset/btn_gem_1", self.OnClaimGem1)
		self.AddTouchEventHandler("/main_pnl/img_base/img_inset/btn_gem_2", self.OnClaimGem2)
		# 背包
		scrollInfo = {}
		scrollBase = "/main_pnl/img_base/img_base_bag/scroll_bag"
		scrollBaseTouch = scrollBase + "/scroll_touch/scroll_view/panel/background_and_viewport/scrolling_view_port/scrolling_content"
		size = self.GetSize(scrollBaseTouch)
		if size:
			scrollInfo["parent"] = scrollBaseTouch
			scrollInfo["parent_size"] = size
		else:
			scrollBaseMouse = scrollBase + "/scroll_mouse/scroll_view/stack_panel/background_and_viewport/scrolling_view_port/scrolling_content"
			size = self.GetSize(scrollBaseMouse)
			scrollInfo["parent"] = scrollBaseMouse
			scrollInfo["parent_size"] = size
		scrollWidth = int(size[0])
		ScrollHeight = 0
		# 装备格
		labelEquip = scrollInfo["parent"] + "/lb_equip"
		labelEquipSize = self.GetSize(labelEquip)
		labelEquipPos = self.GetPosition(labelEquip)
		ScrollHeight = labelEquipPos[1] + labelEquipSize[1] + 2
		self.mEquipGridList = []
		equipBase = scrollInfo["parent"] + "/btn_equip_base"
		baseSize = self.GetSize(equipBase)
		baseWidth = int(baseSize[0])
		grid = scrollWidth // baseWidth
		if scrollWidth % baseWidth < (baseWidth/2):
			grid -= 1
		basePos = self.GetPosition(equipBase)
		for idx in xrange(36):
			name = "btn_equip_%d" % idx
			self.Clone(equipBase, scrollInfo["parent"], name)
			fullName = "%s/%s" % (scrollInfo["parent"], name)
			self.mEquipGridList.append(fullName)
			#
			gridX = idx % grid
			gridY = idx // grid
			width = basePos[0] + baseSize[0] * gridX
			height = ScrollHeight + baseSize[1] * gridY
			self.SetPosition(fullName, (width, height))
			#
			self.SetTouchEnable(fullName, True)
			self.AddTouchEventHandler(fullName, self.OnClickEquip)
		self.SetVisible(equipBase, False)
		ScrollHeight = ScrollHeight + (36 // grid) * baseSize[1] + baseSize[1] + 4
		# 宝石格
		labelGem = scrollInfo["parent"] + "/lb_gem"
		labelGemSize = self.GetSize(labelGem)
		labelGemPos = self.GetPosition(labelGem)
		self.SetPosition(labelGem, (labelGemPos[0], ScrollHeight))
		ScrollHeight = ScrollHeight + labelGemSize[1] + 2
		self.mGemGridList = []
		gemBase = scrollInfo["parent"] + "/btn_gem_base"
		baseSize = self.GetSize(gemBase)
		baseWidth = int(baseSize[0])
		grid = scrollWidth // baseWidth
		if scrollWidth % baseWidth < (baseWidth/2):
			grid -= 1
		basePos = self.GetPosition(gemBase)
		for idx in xrange(36):
			name = "btn_gem_%d" % idx
			self.Clone(gemBase, scrollInfo["parent"], name)
			fullName = "%s/%s" % (scrollInfo["parent"], name)
			self.mGemGridList.append(fullName)
			#
			gridX = idx % grid
			gridY = idx // grid
			width = basePos[0] + baseSize[0] * gridX
			height = ScrollHeight + baseSize[1] * gridY
			self.SetPosition(fullName, (width, height))
			#
			self.SetTouchEnable(fullName, True)
			self.AddTouchEventHandler(fullName, self.OnClickGem)
		self.SetVisible(gemBase, False)
		ScrollHeight = ScrollHeight + (36 // grid) * baseSize[1] + baseSize[1] + 10
		self.SetSize(scrollInfo["parent"], (scrollWidth, ScrollHeight))
		# 装备属性
		scrollInfo = {}
		scrollBase = "/main_pnl/img_base/img_base_attribute/scroll_attribute"
		scrollBaseTouch = scrollBase + "/scroll_touch/scroll_view/panel/background_and_viewport/scrolling_view_port/scrolling_content"
		size = self.GetSize(scrollBaseTouch)
		if size:
			scrollInfo["parent"] = scrollBaseTouch
			scrollInfo["parent_size"] = size
		else:
			scrollBaseMouse = scrollBase + "/scroll_mouse/scroll_view/stack_panel/background_and_viewport/scrolling_view_port/scrolling_content"
			size = self.GetSize(scrollBaseMouse)
			scrollInfo["parent"] = scrollBaseMouse
			scrollInfo["parent_size"] = size
		scrollInfo["base"] = scrollInfo["parent"] + "/img_base_attr"
		scrollInfo["base_size"] = self.GetSize(scrollInfo["base"])
		scrollInfo["base_pos"] = self.GetPosition(scrollInfo["base"])
		scrollInfo["size"] = 0
		self.SetVisible(scrollInfo["base"], False)
		self.mAttrGridList = []
		self.mAttrGridScrollInfo = scrollInfo
		self.AttrListResize(0)
	
	def AttrListResize(self, size):
		scrollInfo = self.mAttrGridScrollInfo
		if size == scrollInfo["size"]:
			return
		scrollInfo["size"] = size
		lackNum = size - len(self.mAttrGridList)
		# 控件不够用，创建一些
		if lackNum > 0:
			beginIndex = len(self.mAttrGridList)
			for idx in xrange(lackNum):
				self.CloneSingleAttr(beginIndex + idx, scrollInfo)
		# 控件多余了，那么隐藏多余不用的控件
		for idx, part in enumerate(self.mAttrGridList):
			if idx < size:
				self.SetVisible(part, True)
			else:
				self.SetVisible(part, False)
		# 重设滚动区域的大小
		height = scrollInfo["base_pos"][1] + size * scrollInfo["base_size"][1]
		height = max(height, scrollInfo["parent_size"][1])
		self.SetSize(scrollInfo["parent"], (scrollInfo["parent_size"][0], height))

	def CloneSingleAttr(self, idx, scrollInfo):
		name = "btn_attr_%d" % idx
		self.Clone(scrollInfo["base"], scrollInfo["parent"], name)
		fullName = "%s/%s" % (scrollInfo["parent"], name)
		self.mAttrGridList.append(fullName)
		height = scrollInfo["base_pos"][1] + idx * scrollInfo["base_size"][1]
		self.SetPosition(fullName, (scrollInfo["base_pos"][0], height))

	def InitScreen(self):
		print '==== %s ====' % 'JewelScreen Init'
		self.ChangeScreenVisible(False)

	def InitSystem(self, system):
		self.mClientSystem = weakref.proxy(system)
		self.mItemComp = clientApi.GetEngineCompFactory().CreateItem(clientApi.GetLevelId())

	# 继承自ScreenNode的方法，会被引擎自动调用，1秒钟30帧
	def Update(self):
		pass

	# -------------------------------------------------------------------------------------------------------------------------------------------
	def Show(self, data):
		# print "jewel show"
		self.ChangeScreenVisible(True)
		# 加载/更新可镶嵌宝石配置
		self.LoadGemConfig(data)
		# 加载/更新装备可镶嵌孔配置
		self.LoadEquipConfig(data)
		# 更新背包物品信息，缓存可镶嵌装备和宝石
		inventory = data.get("inventory", {})
		self.mBagEquipList = []
		self.mBagGemList = []
		for idx, itemStr in enumerate(inventory):
			if not itemStr or itemStr == "null":
				continue
			itemDict = json.loads(itemStr)
			slot = self.GetEquipSlotNum(itemDict)
			if slot > 0:
				self.mBagEquipList.append((idx, itemDict, itemStr))
				continue
			if self.IsGem(itemDict):
				self.mBagGemList.append((idx, itemDict, itemStr))
				continue
		self.DrawBagInventory()
		# 更新镶嵌台上的装备信息
		self.mStuffCache = data["stuff"]
		if self.mStuffCache:
			self.mSelectEquip = json.loads(self.mStuffCache)
			self.mFreeSlot = None
		else:
			self.mSelectEquip = None
			self.mFreeSlot = None
		self.DrawSelectEquip()
		
	def Refresh(self, data):
		# print "jewel refresh"
		# 更新背包物品信息
		inventory = data.get("inventory", {})
		self.mBagEquipList = []
		self.mBagGemList = []
		for idx, itemStr in enumerate(inventory):
			if not itemStr or itemStr == "null":
				continue
			itemDict = json.loads(itemStr)
			slot = self.GetEquipSlotNum(itemDict)
			if slot > 0:
				self.mBagEquipList.append((idx, itemDict, itemStr))
				continue
			if self.IsGem(itemDict):
				self.mBagGemList.append((idx, itemDict, itemStr))
				continue
		self.DrawBagInventory()
	# --------------------------------------------------------------------------------------------------------------------------------------------
	def LoadGemConfig(self, data):
		gems = data.get("gems", None)
		if not gems:
			return
		self.mGemConfig = gems
	
	def IsGem(self, itemDict):
		itemName, auxValue = itemDict.get("itemName", "minecraft:air"), itemDict.get("auxValue", 0)
		name = "{}:{}".format(itemName, auxValue)
		if self.mGemConfig.has_key(name):
			return True 
		if self.mGemConfig.has_key(itemName):
			return True 
		return False

	def LoadEquipConfig(self, data):
		equips = data.get("arms", None)
		if not equips:
			return
		self.mEquipConfig = equips

	def GetEquipSlotNum(self, itemDict):
		itemName, auxValue = itemDict.get("itemName", "minecraft:air"), itemDict.get("auxValue", 0)
		name = "{}:{}".format(itemName, auxValue)
		if self.mEquipConfig.has_key(name):
			return self.mEquipConfig[name]
		if self.mEquipConfig.has_key(itemName):
			return self.mEquipConfig[itemName]
		return 0
	# --------------------------------------------------------------------------------------------------------------------------------------------
	def DrawBagInventory(self):
		for i in xrange(36):
			part = self.mEquipGridList[i]
			if i >= len(self.mBagEquipList):
				self.DrawSingleBagEquip(part, None)
			else:
				self.DrawSingleBagEquip(part, self.mBagEquipList[i])
		for i in xrange(36):
			part = self.mGemGridList[i]
			if i >= len(self.mBagGemList):
				self.DrawSingleBagGem(part, None)
			else:
				self.DrawSingleBagGem(part, self.mBagGemList[i])
	
	def DrawSingleBagEquip(self, part, data):
		if not data:
			self.SetVisible("%s/equip_renderer" % part, False)
			self.SetText("%s/lb_equip_name" % part, "")
			return
		slotNum, itemDict, itemStr = data
		itemName, auxValue, count = itemDict["itemName"], itemDict.get("auxValue", 0), itemDict.get("count", 1)
		self.SetVisible("%s/equip_renderer" % part, True)
		self.SetUiItem("%s/equip_renderer" % part, itemName, auxValue)
		self.SetText("%s/lb_equip_name" % part, "%d" % count)

	def DrawSingleBagGem(self, part, data):
		if not data:
			self.SetVisible("%s/gem_renderer" % part, False)
			self.SetText("%s/lb_gem_name" % part, "")
			return
		slotNum, itemDict, itemStr = data
		itemName, auxValue, count = itemDict["itemName"], itemDict.get("auxValue", 0), itemDict.get("count", 1)
		self.SetVisible("%s/gem_renderer" % part, True)
		self.SetUiItem("%s/gem_renderer" % part, itemName, auxValue)
		self.SetText("%s/lb_gem_name" % part, "%d" % count)

	def DrawSelectEquip(self):
		if not self.mSelectEquip:
			self.DrawEmptySelectEquip()
			return
		# for k, v in self.mSelectEquip.iteritems():
		#	print "selectEquip k={} v={}".format(k, v)
		itemName, auxValue = self.mSelectEquip["itemName"], self.mSelectEquip.get("auxValue", 0)	
		info = self.mItemComp.GetItemBasicInfo(itemName, auxValue)
		if info:
			self.SetText("/main_pnl/img_base/img_inset/lb_inset_equipment", info["itemName"])
		else:
			self.SetText("/main_pnl/img_base/img_inset/lb_inset_equipment", "")
		self.SetVisible("/main_pnl/img_base/img_inset/btn_equip/equip", True)
		self.SetUiItem("/main_pnl/img_base/img_inset/btn_equip/equip", itemName, auxValue)
		#
		slotNum = self.GetEquipSlotNum(self.mSelectEquip)
		print "equip slotNum={}".format(slotNum)
		data = json.loads(self.mSelectEquip['extraId'].strip() or '{}')
		dataKey = 'calculator:{}'.format(jewelConst.ModName)
		gemData = data.get(dataKey, [None, None, None])
		for slot, gemDict in enumerate(gemData):
			print "slot={} type={} gemDict={}".format(slot, type(gemDict), gemDict)
		for slot in xrange(3):
			if slot < slotNum:
				if slot < len(gemData):
					gemDict = gemData[slot]
					if not gemDict and self.mFreeSlot is None:
						self.mFreeSlot = slot
					self.DrawSingleEquipSlot(slot, False, gemDict)
				else:
					if self.mFreeSlot is None:
						self.mFreeSlot = slot
					self.DrawSingleEquipSlot(slot, False, None)
			else:
				self.DrawSingleEquipSlot(slot, True, None)
		#
		battleSystem = clientApi.GetSystem("neteaseBattle", "neteaseBattleBeh")
		if not battleSystem:
			logger.error("cannot find battleSystem.")
			self.AttrListResize(0)
			return	
		attrs = Counter()
		attrs.update(battleSystem.GetEquipAttrDict(self.mSelectEquip['itemName'], self.mSelectEquip['auxValue']))
		for gemDict in gemData:
			if gemDict:
				attrs.update(battleSystem.GetEquipAttrDict(gemDict['itemName'], gemDict['auxValue']))
		import neteaseBattleScript.battleCommon.battleConsts as battleConsts
		iconData = {cfg['key']: "textures/ui/netease_battle/{}".format(cfg['icon']) for cfg in battleConsts.ExtraAttrs}
		size = len(attrs)
		self.AttrListResize(size)
		idx = -1
		for cfg in battleConsts.ExtraAttrs:
			k, icon = cfg["key"], "textures/ui/netease_battle/{}".format(cfg["icon"])
			if not attrs.has_key(k):
				continue
			idx += 1
			part = self.mAttrGridList[idx]
			v = attrs[k]
			desc, pretty = battleSystem.GetFormatAttr(k, v)
			self.SetSprite("%s/img_attr_icon" % part, icon)
			self.SetText("%s/lb_attr_name" % part, desc)
			self.SetText("%s/lb_attr_value" % part, pretty)

	def DrawEmptySelectEquip(self):
		self.SetText("/main_pnl/img_base/img_inset/lb_inset_equipment", "")
		self.SetVisible("/main_pnl/img_base/img_inset/btn_equip/equip", False)
		for slot in xrange(3):
			self.DrawSingleEquipSlot(slot, True, None)
		self.AttrListResize(0)
	
	def DrawSingleEquipSlot(self, slot, isLock, itemDict):
		lbName = "/main_pnl/img_base/img_inset/lb_inset_gem0%d" % (slot+1, )
		buttonName = "/main_pnl/img_base/img_inset/btn_gem_%d" % slot
		renderName = "/main_pnl/img_base/img_inset/btn_gem_%d/gem_%d" % (slot, slot)
		if isLock:
			self.SetSprite("%s/default" % buttonName, "textures/ui/netease_jewel/img02")
			self.SetSprite("%s/hover" % buttonName, "textures/ui/netease_jewel/img02")
			self.SetSprite("%s/pressed" % buttonName, "textures/ui/netease_jewel/img02")
		else:
			self.SetSprite("%s/default" % buttonName, "textures/ui/netease_jewel/empty01")
			self.SetSprite("%s/hover" % buttonName, "textures/ui/netease_jewel/empty01")
			self.SetSprite("%s/pressed" % buttonName, "textures/ui/netease_jewel/empty01")
		if itemDict:
			itemName, auxValue = itemDict["itemName"], itemDict.get("auxValue", 0)
			self.SetVisible(renderName, True)
			self.SetUiItem(renderName, itemName, auxValue)
			info = self.mItemComp.GetItemBasicInfo(itemName, auxValue)
			if info:
				self.SetText(lbName, info["itemName"])
			else:
				self.SetText(lbName, "")
		else:
			self.SetVisible(renderName, False)
			self.SetText(lbName, "")
	# --------------------------------------------------------------------------------------------------------------------------------------------
	def OnRealClaimEquip(self):
		print "OnRealClaimEquip"
		eventData = {
			"playerId": clientApi.GetLocalPlayerId(),
		}
		self.mClientSystem.NotifyToServer(jewelConst.PlayerClaimArmEvent, eventData)

	def OnRealClaimGem(self, slot):
		print "OnRealClaimGem", slot
		eventData = {
			"playerId": clientApi.GetLocalPlayerId(),
			"p": slot,
		}
		self.mClientSystem.NotifyToServer(jewelConst.PlayerClaimGemEvent, eventData)

	def OnRealClickEquip(self, idx):
		print "OnRealClickEquip", idx
		if idx >= len(self.mBagEquipList):
			return
		slotPos, itemDict, itemStr = self.mBagEquipList[idx]
		eventData = {
			"playerId": clientApi.GetLocalPlayerId(),
			"slot": slotPos,
			"stuff": itemStr,
		}
		self.mClientSystem.NotifyToServer(jewelConst.PlayerOfferArmEvent, eventData)
	
	def OnRealClickGem(self, idx):
		print "OnRealClickGem", idx
		if idx >= len(self.mBagGemList):
			return
		print "mFreeSlot={}".format(self.mFreeSlot)
		slotPos, itemDict, itemStr = self.mBagGemList[idx]
		if self.mFreeSlot is None:
			return
		eventData = {
			"playerId": clientApi.GetLocalPlayerId(),
			"slot": slotPos,
			"stuff": itemStr,
			"p": self.mFreeSlot,
		}
		self.mClientSystem.NotifyToServer(jewelConst.PlayerOfferGemEvent, eventData)
	# --------------------------------------------------------------------------------------------------------------------------------------------
	def OnClose(self, args):
		event = args["TouchEvent"]
		if event == TouchEvent.TouchUp:
			self.ChangeScreenVisible(False)
		elif event == TouchEvent.TouchDown:
			pass
		elif event == TouchEvent.TouchMove:
			pass
		elif event == TouchEvent.TouchCancel:
			pass
	
	def OnClaimEquip(self, args):
		event = args["TouchEvent"]
		if event == TouchEvent.TouchUp:
			self.OnRealClaimEquip()
		elif event == TouchEvent.TouchDown:
			pass
		elif event == TouchEvent.TouchMove:
			pass
		elif event == TouchEvent.TouchCancel:
			pass
	
	def OnClaimGem0(self, args):
		event = args["TouchEvent"]
		if event == TouchEvent.TouchUp:
			self.OnRealClaimGem(0)
		elif event == TouchEvent.TouchDown:
			pass
		elif event == TouchEvent.TouchMove:
			pass
		elif event == TouchEvent.TouchCancel:
			pass
	
	def OnClaimGem1(self, args):
		event = args["TouchEvent"]
		if event == TouchEvent.TouchUp:
			self.OnRealClaimGem(1)
		elif event == TouchEvent.TouchDown:
			pass
		elif event == TouchEvent.TouchMove:
			pass
		elif event == TouchEvent.TouchCancel:
			pass

	def OnClaimGem2(self, args):
		event = args["TouchEvent"]
		if event == TouchEvent.TouchUp:
			self.OnRealClaimGem(2)
		elif event == TouchEvent.TouchDown:
			pass
		elif event == TouchEvent.TouchMove:
			pass
		elif event == TouchEvent.TouchCancel:
			pass
	
	def OnClickEquip(self, args):
		line = args["ButtonPath"].split("/")
		line = line[-1]
		line = line.split("_")
		idx = int(line[-1])
		event = args["TouchEvent"]
		if event == TouchEvent.TouchUp:
			self.OnRealClickEquip(idx)
		elif event == TouchEvent.TouchDown:
			pass
		elif event == TouchEvent.TouchMove:
			pass
		elif event == TouchEvent.TouchCancel:
			pass
	
	def OnClickGem(self, args):
		line = args["ButtonPath"].split("/")
		line = line[-1]
		line = line.split("_")
		idx = int(line[-1])
		event = args["TouchEvent"]
		if event == TouchEvent.TouchUp:
			self.OnRealClickGem(idx)
		elif event == TouchEvent.TouchDown:
			pass
		elif event == TouchEvent.TouchMove:
			pass
		elif event == TouchEvent.TouchCancel:
			pass