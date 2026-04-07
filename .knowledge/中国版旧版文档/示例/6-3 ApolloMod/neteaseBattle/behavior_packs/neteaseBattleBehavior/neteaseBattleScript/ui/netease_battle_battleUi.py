# -*- coding: utf-8 -*-

import re, json
import client.extraClientApi as extraClientApi
ViewBinder = extraClientApi.GetViewBinderCls()
ViewRequest = extraClientApi.GetViewViewRequestCls()
ScreenNode = extraClientApi.GetScreenNodeCls()
TouchEvent = extraClientApi.GetMinecraftEnum().TouchEvent
from neteaseBattleScript.battleCommon.battleConsts import CInterEvent, GameEquipPart, GameObjType
import neteaseBattleScript.battleCommon.apiUtil as apiUtil
import neteaseBattleScript.battleCommon.battleConsts as battleConsts
from neteaseBattleScript.ui.uiDef import UIDef

try:
	import neteaseBattleScript.fmt as fmt
	FMT = fmt.FMT
except:
	FMT = {}


class BattleMobScreen(ScreenNode):
	"""
	玩家的战斗插件操作面板UI
	"""

	def __init__(self, namespace, name, param):
		ScreenNode.__init__(self, namespace, name, param)
		self.mUIKey = UIDef.UIBattle
		self.mFirstOpen = True
		self.mRecentSize = 0
		self.mBShow = False
		self.mLinkedEntityId = None
		self.mLastSelectNode = None

	def ChangeScreenVisible(self, flag):
		self.mBShow = flag
		if flag:
			apiUtil.GetClientSystem().GetUIMgr().RegisterUIOpen(self.mUIKey)  # 告知UIMgr该界面处于打开的状态
		else:
			apiUtil.GetClientSystem().GetUIMgr().RegisterUIClose(self.mUIKey)  # 告知UIMgr该界面处于关闭的状态
		self.SetVisible("", flag)

	# Create函数是继承自ScreenNode，会在UI创建完成后被调用
	def Create(self):
		# 初始化背包道具格
		singleItem = "/main_pnl/img_base_bag/item_bag/single_item_base"
		size = self.GetSize(singleItem)
		pos = self.GetPosition(singleItem)
		#
		begin = (-2, 0)
		offset = (0, 0)
		parent = "/main_pnl/img_base_bag/item_bag"
		self.mItemPanelList = []
		for idx in xrange(36):
			# 背包格子
			name = "single_item_%d" % idx
			self.Clone(singleItem, parent, name)
			fullName = "%s/%s" % (parent, name)
			self.mItemPanelList.append(fullName)
			w, h = idx % 7, idx // 7
			self.SetPosition(fullName, (pos[0]+begin[0]+offset[0]*w+size[0]*w, pos[1]+begin[1]+offset[1]*h+size[1]*h))
			self.AddTouchEventHandler("%s/btn_item" % fullName, self.OnSingleItemClick)
			self.SetVisible("%s/img_select" % fullName, False)
		self.SetVisible(singleItem, False)
		# 注册装备栏
		for idx in xrange(9):
			name = "/main_pnl/img_base_equip/btn_part_%d" % idx
			self.AddTouchEventHandler(name, self.OnEquipClick)
		self.AddTouchEventHandler("/main_pnl/img_close/btn_close", self.OnCloseBtn)
		# 属性栏
		scrollBase = "/main_pnl/img_base_equip/img_attr_bg/scroll_avatar"
		scrollBaseTouch = scrollBase + "/scroll_touch/scroll_view/panel/background_and_viewport/scrolling_view_port/scrolling_content"
		size = self.GetSize(scrollBaseTouch)
		if size:
			self.mSingleAttrParent = scrollBaseTouch
			self.mSingleAttrParentSize = size
		else:
			scrollBaseMouse = scrollBase + "/scroll_mouse/scroll_view/stack_panel/background_and_viewport/scrolling_view_port/scrolling_content"
			size = self.GetSize(scrollBaseMouse)
			self.mSingleAttrParent = scrollBaseMouse
			self.mSingleAttrParentSize = size
		# print "Create", self.mSingleAttrParent, self.mSingleAttrParentSize
		self.mSingleAttrBase = self.mSingleAttrParent + "/img_attr_base"
		self.mSingleAttrBaseSize = self.GetSize(self.mSingleAttrBase)
		self.mSingleAttrBasePos = self.GetPosition(self.mSingleAttrBase)
		self.mSingleAttrOffset = 0
		# print "MailBtnBase", self.mSingleAttrBaseSize, self.mSingleAttrBasePos
		self.SetVisible(self.mSingleAttrBase, False)
		self.mSingleAttrList = []
		self.Resize(0)
		print "AddTouchEventHandler finish"

	def Resize(self, size):
		if size == self.mRecentSize:
			return
		self.mRecentSize = size
		lackNum = size - len(self.mSingleAttrList)
		# 控件不够用，创建一些
		if lackNum > 0:
			beginIndex = len(self.mSingleAttrList)
			for idx in xrange(lackNum):
				self.CloneSingleAttr(beginIndex + idx)
		# 隐藏多余不用的控件
		for idx, btn in enumerate(self.mSingleAttrList):
			if idx < size:
				self.SetVisible(btn, True)
			else:
				self.SetVisible(btn, False)
		# 重设滚动区域的大小
		height = self.mSingleAttrBasePos[1] + size * (self.mSingleAttrBaseSize[1] + self.mSingleAttrOffset)
		height = max(height, self.mSingleAttrParentSize[1])
		# print "Resize", self.mSingleAttrParentSize, height
		self.SetSize(self.mSingleAttrParent, (self.mSingleAttrParentSize[0], height))

	def CloneSingleAttr(self, idx):
		# 复制一个属性条
		name = "single_attr_%d" % idx
		self.Clone(self.mSingleAttrBase, self.mSingleAttrParent, name)
		name = "%s/%s" % (self.mSingleAttrParent, name)
		self.mSingleAttrList.append(name)
		height = self.mSingleAttrBasePos[1] + idx * (self.mSingleAttrBaseSize[1] + self.mSingleAttrOffset)
		self.SetPosition(name, (self.mSingleAttrBasePos[0], height))
		# 实现颜色间隔
		if idx % 2 == 0:
			self.SetSprite(name, "textures/ui/netease_battle/form_02@3x")
		else:
			self.SetSprite(name, "textures/ui/netease_battle/form_01@3x")

	def InitScreen(self):
		self.ChangeScreenVisible(False)
		apiUtil.GetClientSystem().RegisterInterEvent(CInterEvent.UIStatusOpen, self.OnOpen)  # 通知打开该界面
		apiUtil.GetClientSystem().RegisterInterEvent(CInterEvent.UIStatusDraw, self.OnDraw)  # 玩家属性或背包有同步
		apiUtil.GetClientSystem().RegisterInterEvent(CInterEvent.UIClosePopup, self.OnClose)  # 暂未使用，可作其余界面调用关闭该界面用

	def Destroy(self):
		apiUtil.GetClientSystem().UnRegisterInterEvent(CInterEvent.UIStatusOpen, self.OnOpen)
		apiUtil.GetClientSystem().UnRegisterInterEvent(CInterEvent.UIStatusDraw, self.OnDraw)
		apiUtil.GetClientSystem().UnRegisterInterEvent(CInterEvent.UIClosePopup, self.OnClose)

	# 继承自ScreenNode的方法，会被引擎自动调用，1秒钟30帧
	def Update(self):
		pass
	# ---------------------------------------------------------------------------------
	def CancelLastSelect(self):
		# 点了别的，取消上一次点的
		if not self.mLastSelectNode:
			return
		isBag, lastIdx = self.mLastSelectNode
		if isBag:
			self.DrawBagItemSelect(lastIdx, False)
		else:
			self.DrawEquipItemSelect(lastIdx, False)
		self.mLastSelectNode = None

	def TransEquipIdxToPart(self, idx):
		# 根据点击格子的id得到player装备数据结构里的key
		if idx in (0, 1, 2, 3):  # 0, 1, 2, 3分别对应了头、胸、腿、鞋
			return idx
		else:
			return idx + 1  # 除了主手后面的部分

	def GetBagItem(self, idx):
		# 按照序号得到背包物品，0-35
		if self.mLinkedEntityId != extraClientApi.GetLocalPlayerId():
			return None
		player = apiUtil.GetClientSystem().GetObjMgr().GetObject(self.mLinkedEntityId)
		if not player:
			return None
		bagsInfo = player.GetBagsInfo()
		return bagsInfo.get(idx, None)

	def GetEquipItem(self, idx):
		# 按照点击格子的序号得到装备着的物品数据
		if self.mLinkedEntityId != extraClientApi.GetLocalPlayerId():
			return None
		player = apiUtil.GetClientSystem().GetObjMgr().GetObject(self.mLinkedEntityId)
		if not player:
			return None
		part = self.TransEquipIdxToPart(idx)
		return player.GetEquipByPart(part)
	#---------------------------------------------------------------------------------
	def OnOpen(self, data):
		# 打开界面
		size = len(battleConsts.ExtraAttrs) + 1
		self.Resize(size)  # 根据配置显示属性
		self.ChangeScreenVisible(True)
		if self.mFirstOpen:
			# 首次打开界面要通知服务端刷背包下来
			playerId = apiUtil.GetClientSystem().GetLocalPlayer()
			apiUtil.GetClientSystem().GetRpcUtil().ServerRpc().NotifyPlayerBagRefresh(playerId)
			self.mFirstOpen = False
		self.OnDraw(data)

	def OnClose(self, data):
		self.ChangeScreenVisible(False)

	def OnClickSingleItem(self, idx, x, y):
		# 点击背包格子
		# print "OnClickSingleItem", idx
		if self.mLinkedEntityId != extraClientApi.GetLocalPlayerId():
			return
		if self.mLastSelectNode:
			isBag, lastIdx = self.mLastSelectNode
			self.CancelLastSelect()
			if isBag:	# 上次选中的是背包物品，这次选中的还是背包物品
				if lastIdx == idx:	# 点击同一个物品，取消选中
					self.mLastSelectNode = None
				else:	# 点击另外一个物品，交换背包格
					self.mLastSelectNode = None
					apiUtil.GetClientSystem().GetRpcUtil().ServerRpc().ExChangeBagSlot(self.mLinkedEntityId, lastIdx, idx)
					#newItem = self.GetBagItem(idx)
					#if newItem: # 如果格子里有物品，切换选中
					#	self.mLastSelectNode = (True, idx)
					#	self.DrawBagItemSelect(idx, True)
					#else:	# 格子是空的，取消选中
					#	self.mLastSelectNode = None
			else:	# 上次选中的是装备位，发送给服务器处理，同时清理选中
				self.mLastSelectNode = None
				part = self.TransEquipIdxToPart(lastIdx)
				apiUtil.GetClientSystem().GetRpcUtil().ServerRpc().ChangeEquipAction(self.mLinkedEntityId, part, idx)
		else:
			newItem = self.GetBagItem(idx)
			if newItem:
				self.mLastSelectNode = (True, idx)

				self.ShowDetail({
					'itemName': newItem[0],
					'auxValue': newItem[1],
					'count': newItem[2],
					'durability': newItem[3],
					'userData': newItem[4],
					'extraId': newItem[5],
				}, x, y)

				self.DrawBagItemSelect(idx, True)

	def OnClickEquip(self, idx, x, y):
		# 点击装备槽位
		# print "OnClickEquip", idx
		if self.mLinkedEntityId != extraClientApi.GetLocalPlayerId():
			return
		if self.mLastSelectNode:
			isBag, lastIdx = self.mLastSelectNode
			self.CancelLastSelect()
			if isBag:  # 上次选中的是背包物品，这次选中的装备栏
				# 发送给服务器处理，同时清理选中
				self.mLastSelectNode = None
				part = self.TransEquipIdxToPart(idx)
				apiUtil.GetClientSystem().GetRpcUtil().ServerRpc().ChangeEquipAction(self.mLinkedEntityId, part, lastIdx)
			else:	# 上次选中的是背包位置
				if lastIdx == idx:	# 选中的是同一个位置，取消选中
					self.mLastSelectNode = None
				else:	# 选中的是不同位置，切换选中
					self.mLastSelectNode = (False, idx)
					self.DrawEquipItemSelect(idx, True)
		else:	# 无法选中空的背包格，但是可以选中空的装备格
			self.mLastSelectNode = (False, idx)

			equip = self.GetEquipItem(idx)
			if equip:
				self.ShowDetail(equip.GetItemDict(), x, y)

			self.DrawEquipItemSelect(idx, True)

	def OnDraw(self, data):
		# ui显示相关逻辑
		# 绘制属性、背包和装备区
		if not self.mBShow:
			return
		self.mLinkedEntityId = data["guid"]
		entity = apiUtil.GetClientSystem().GetObjMgr().GetObject(data["guid"])
		self.DrawEntityAttr(entity)
		if self.mLinkedEntityId == extraClientApi.GetLocalPlayerId():
			self.DrawEquip(entity)
			self.DrawBagItems(entity)
		else:
			self.CancelLastSelect()
			self.DrawEmptyEquip()
			self.DrawEmptyBag()

	def DrawBagItems(self, player):
		bagsInfo = player.GetBagsInfo()
		for idx in xrange(36):
			name = self.mItemPanelList[idx]
			singleItem = bagsInfo.get(idx, None)
			if singleItem:
				itemName, auxValue, count = singleItem[:3]
				self.SetVisible("%s/item_render" % name, True)
				self.SetUiItem("%s/item_render" % name, itemName, auxValue)
				self.SetText("%s/lb_item_num" % name, "%d" % count)
			else:
				self.SetVisible("%s/item_render" % name, False)
				self.SetText("%s/lb_item_num" % name, "")

	def DrawEmptyBag(self):
		for idx in xrange(36):
			name = self.mItemPanelList[idx]
			self.SetVisible("%s/item_render" % name, False)
			self.SetText("%s/lb_item_num" % name, "")

	def DrawBagItemSelect(self, idx, isSelect):
		# 统一入口显示格子被点击时的状态贴图
		name = self.mItemPanelList[idx]
		if isSelect:
			self.SetVisible("%s/img_select" % name, True)
		else:
			self.SetVisible("%s/img_select" % name, False)

	def DrawEquipItemSelect(self, idx, isSelect):
		name = "/main_pnl/img_base_equip/btn_part_%d/img_select_%d" % (idx, idx)
		if isSelect:
			self.SetVisible(name, True)
		else:
			self.SetVisible(name, False)

	def DrawEquip(self, player):
		for idx in xrange(9):
			emptyName = "/main_pnl/img_base_equip/btn_part_%d/empty_%d" % (idx, idx)
			equipName = "/main_pnl/img_base_equip/btn_part_%d/equip_%d" % (idx, idx)
			part = self.TransEquipIdxToPart(idx)
			item = player.GetEquipByPart(part)
			if item:
				self.SetVisible(emptyName, False)
				self.SetVisible(equipName, True)
				self.SetUiItem(equipName, item.mMcName, item.mAuxValue)
			else:
				self.SetVisible(emptyName, True)
				self.SetVisible(equipName, False)

	def DrawEmptyEquip(self):
		for idx in xrange(9):
			emptyName = "/main_pnl/img_base_equip/btn_part_%d/empty_%d" % (idx, idx)
			self.SetVisible(emptyName, True)
			equipName = "/main_pnl/img_base_equip/btn_part_%d/equip_%d" % (idx, idx)
			self.SetVisible(equipName, False)

	def DrawEntityAttr(self, entity):
		if entity:
			propAttrs = entity.FormatStatusWithIcon(zero=1)
		else:
			propAttrs = []
		for idx in xrange(self.mRecentSize):
			if idx in (0, 1):
				color = (0.0, 1.0, 0.0, 1.0)
			else:
				color = (1.0, 1.0, 1.0, 1.0)
			if idx >= len(propAttrs):
				self.DrawSingleAttr(self.mSingleAttrList[idx], "", "", "", color)
			else:
				self.DrawSingleAttr(self.mSingleAttrList[idx], propAttrs[idx][0], propAttrs[idx][1], propAttrs[idx][2], color)

	def DrawSingleAttr(self, panel, attrName, attrValue, attrIcon, color):
		self.SetSprite("%s/img_attr_icon" % panel, "textures/ui/netease_battle/%s" % attrIcon)
		self.SetText("%s/lb_attr_name" % panel, attrName)
		self.SetTextColor("%s/lb_attr_name" % panel, color)
		self.SetText("%s/lb_attr_value" % panel, attrValue)
		self.SetTextColor("%s/lb_attr_value" % panel, color)
	#-----------------------------------------------------------------------------------
	def OnCloseBtn(self, args):
		#print "OnCloseBtn", args
		event = args["TouchEvent"]
		if event == TouchEvent.TouchUp:
			self.OnClose({})

	def OnSingleItemClick(self, args):
		#print "OnSingleItemClick", args
		line = args["ButtonPath"]
		line = line.split("/")[-2]
		line = line.split("_")
		idx = int(line[-1])
		event = args["TouchEvent"]
		x, y = args['TouchPosX'], args['TouchPosY']
		if event == TouchEvent.TouchUp:
			if idx in xrange(18, 36):
				y -= 80.0
			self.OnClickSingleItem(idx, x, y)

	def OnEquipClick(self, args):
		#print "OnEquipClick", args
		line = args["ButtonPath"]
		line = line.split("/")[-1]
		line = line.split("_")
		idx = int(line[-1])
		event = args["TouchEvent"]
		x, y = args['TouchPosX'], args['TouchPosY']
		if event == TouchEvent.TouchUp:
			if idx in xrange(5, 9):
				x -= 100.0
			self.OnClickEquip(idx, x, y)

	def ShowDetail(self, itemDict, x, y):
		# 如果有物品面板插件存在，点击格子时需要展示物品属性
		attrsSystem = extraClientApi.GetSystem("neteaseAttrs", "neteaseAttrsBeh")
		if not attrsSystem:
			return
		detail = {}
		_system = apiUtil.GetClientSystem()
		splitName = itemDict['itemName'].split(":")
		if splitName and len(splitName) >= 2:
			defaultNamespace = "{}:default".format(splitName[0])
		else:
			defaultNamespace = ""
		withAux = '{}:{}'.format(itemDict['itemName'], itemDict['auxValue'])
		if withAux in FMT:
			spec = FMT[withAux]
		elif itemDict['itemName'] in FMT:
			spec = FMT[itemDict['itemName']]
		elif defaultNamespace and defaultNamespace in FMT:
			spec = FMT[defaultNamespace]
		elif "default" in FMT:
			spec = FMT["default"]
		else:
			spec = {}
		data = json.loads(itemDict['extraId'].strip() or '{}')  # type: dict
		slotList = []
		jewelSystem = extraClientApi.GetSystem("neteaseJewel", "neteaseJewelBeh")
		if jewelSystem:
			slotNum = jewelSystem.GetAvailableSlot(itemDict['itemName'], itemDict['auxValue'])
			for i in xrange(slotNum):
				slotList.append(None)
		gems = []
		for p, item in enumerate(data.get('calculator:neteaseJewel', slotList)):
			if item:
				gems.extend(_system.GetFormatAttr(k, v) for k, v in _system.GetEquipAttrDict(
					item['itemName'], item['auxValue']).iteritems())
			else:
				gems.append(p + 1)
		comp = extraClientApi.CreateComponent('', "Minecraft", "item")
		pretty = comp.GetItemFormattedHoverText(
			itemDict['itemName'], itemDict['auxValue'], True, itemDict.get('userData')).split('\n')
		if '' in pretty:
			pretty = pretty[:pretty.index('')]
		name = pretty[0]
		part = pretty[1]
		attrs = []
		for k, v in _system.GetEquipAttrDict(itemDict['itemName'], itemDict['auxValue']).iteritems():
			if abs(v) <= 0.01:
				continue
			attrs.append(_system.GetFormatAttr(k, v))
		enchantData = map(lambda s: '§7{}'.format(s), pretty[2:])

		# 名字
		if 'name' in spec:
			detail['name'] = spec['name']
		else:
			detail['name'] = name
		# 品质
		if ('part' in spec or 'quality' in spec) if spec else True:
			pair = [None, None]
			if 'quality' in spec:
				pair[0] = spec['quality']
			else:
				pair[0] = ''
			if 'part' in spec:
				pair[1] = spec['part']
			else:
				pair[1] = part
			detail['pinzhi'] = pair
		# 描述
		if 'desc' in spec:
			detail['desc'] = spec['desc']
		# 耐久
		if 'durability' in itemDict:
			if 'durability' in spec if spec else True:
				if not spec:
					detail['naijiu'] = ('耐久', str(itemDict['durability']))
				else:
					detail['naijiu'] = (
						spec['durability'][0],
						'{}{}'.format(spec['durability'][1], itemDict['durability'])
					)
		# 属性
		if 'attrs' in spec:
			if isinstance(spec['attrs'][0], str):
				detail['shuxing'] = map(
					lambda pair: ('{}{}'.format(spec['attrs'][0], pair[0]), '{}{}'.format(spec['attrs'][1], pair[1])),
					attrs)
			else:
				l = []
				attrs = _system.GetEquipAttrDict(itemDict['itemName'], itemDict['auxValue']).copy()
				for duo in spec['attrs']:
					pair = []
					results = re.findall(r'\(.*?\)', duo[0])
					if results:
						k = results[0][1:-1]
						repl = (_system.GetFormatAttr(k, 0) or ('未知',))[0]
						pair.append(re.sub(r'\(.*?\)', repl, duo[0]))
					else:
						pair.append(duo[0])
					results = re.findall(r'\(.*?\)', duo[1])
					if results:
						k = results[0][1:-1]
						if k not in attrs:
							repl = '未知'
						else:
							repl = _system.GetFormatAttr(k, attrs[k])[1]
						pair.append(re.sub(r'\(.*?\)', repl, duo[1]))
					else:
						pair.append(duo[1])
					l.append(pair)
				if l:
					detail['shuxing'] = l
		elif not spec and attrs:
			detail['shuxing'] = attrs
		# 宝石
		if gems and not (spec and 'gem' not in spec):
			pair = ('', '')
			if 'gem' in spec:
				pair = spec['gem']
			for i in xrange(len(gems)):
				if isinstance(gems[i], int):
					gems[i] = ('§7槽位{}未镶嵌'.format(gems[i]), '')
				else:
					gems[i] = ('{}{}'.format(pair[0], gems[i][0]), '{}{}'.format(pair[1], gems[i][1]))
			detail['baoshi'] = gems
		# 附魔
		# if enchantData:
		# 	if 'enchantment' in spec if spec else True:
		# 		detail['fumo'] = enchantData

		attrsSystem.Detail(detail, x, y)
