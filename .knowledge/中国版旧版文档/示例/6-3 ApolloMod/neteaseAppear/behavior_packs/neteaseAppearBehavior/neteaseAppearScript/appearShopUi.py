# -*- coding: utf-8 -*-
import weakref
import copy

import client.extraClientApi as clientApi
ViewBinder = clientApi.GetViewBinderCls()
ViewRequest = clientApi.GetViewViewRequestCls()
ScreenNode = clientApi.GetScreenNodeCls()
TouchEvent = clientApi.GetMinecraftEnum().TouchEvent

from neteaseAppearScript.appearConst import ClientEvent
import neteaseAppearScript.appearConst as appearConst

AppearTypeName = {
	appearConst.AppearType.Body: "时装",
	appearConst.AppearType.Mount: "坐骑",
	appearConst.AppearType.Wing: "翅膀",
	appearConst.AppearType.Aura: "法阵",
}

class ShopScreen(ScreenNode):
	def __init__(self, namespace, name, param):
		ScreenNode.__init__(self, namespace, name, param)
		self.mUiKey = "shop"
		self.mSystem = None
		self.mMoneyData = {}
		self.mPropBtns = ("/main_pnl/btn_clothes", "/main_pnl/btn_wing", "/main_pnl/btn_saddle", "/main_pnl/btn_phalanx")
		self.mPropTypes = (appearConst.AppearType.Body, appearConst.AppearType.Wing, appearConst.AppearType.Mount, appearConst.AppearType.Aura)
		self.mSelectAppearType = appearConst.AppearType.Body
		self.mRecentAppears = []
		self.mPreviewAppear = {}
		self.mPreviewExtraDataList = []
		self.mDelaySec = 1.0

	def Destroy(self):
		pass

	def ChangeScreenVisible(self, flag):
		self.mBShow = flag
		if flag:
			if self.mSystem:
				self.mSystem.RegisterUIOpen(self.mUiKey)
		else:
			if self.mSystem:
				self.mSystem.RegisterUIClose(self.mUiKey)
		self.SetVisible("", flag)
		
	def GetIsShow(self):
		return self.mBShow

	def InitScreen(self):
		self.ChangeScreenVisible(False)
		
	def InitSystem(self, system):
		self.mSystem = system
		self.ChangeScreenVisible(False)

	def Create(self):
		# 按钮
		self.AddTouchEventHandler("/main_pnl/btn_close", self.OnButtonClose)
		self.AddTouchEventHandler("/main_pnl/btn_clothes", self.OnButtonPage1)
		self.AddTouchEventHandler("/main_pnl/btn_wing", self.OnButtonPage2)
		self.AddTouchEventHandler("/main_pnl/btn_saddle", self.OnButtonPage3)
		self.AddTouchEventHandler("/main_pnl/btn_phalanx", self.OnButtonPage4)
		self.AddTouchEventHandler("/main_pnl/img_base_right/btn_use", self.OnButtonUse)
		self.SetTouchEnable("/main_pnl/img_base_right/btn_unused", False)
		#self.AddTouchEventHandler("/main_pnl/img_base_right/btn_unused", self.OnButtonUsed)
		self.AddTouchEventHandler("/main_pnl/img_base_right/btn_price", self.OnButtonBuy)
		
		# 商品列表
		scrollInfo = {}
		scrollBase = "/main_pnl/img_base_left/scroll_goods"
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
		scrollInfo["base"] = scrollInfo["parent"] + "/btn_goods"
		scrollInfo["base_size"] = self.GetSize(scrollInfo["base"])
		scrollInfo["base_pos"] = self.GetPosition(scrollInfo["base"])
		scrollInfo["grid_offset"] = (2, 2)
		scrollInfo["size"] = 0
		self.SetVisible(scrollInfo["base"], False)
		self.mGoodsInstList = []
		self.mGoodsScrollInfo = scrollInfo
		self.ResizeGoods(0)

	def ResizeGoods(self, size):
		# 假如resize的尺寸刚好和之前的尺寸相同，那么不需要做任何事，直接return
		# 某些全局刷新操作也会触发这个函数
		scrollInfo = self.mGoodsScrollInfo
		if size == scrollInfo["size"]:
			return
		# 记录下最新的列表尺寸
		scrollInfo["size"] = size
		# 计算一下需要新生成的单个控件数量
		lackNum = size - len(self.mGoodsInstList)
		# 控件不够用，创建一些
		if lackNum > 0:
			beginIndex = len(self.mGoodsInstList)
			for idx in xrange(lackNum):
				self.CloneSingleGood(beginIndex + idx, scrollInfo)
		# 控件多余了，那么隐藏多余不用的控件
		for idx, part in enumerate(self.mGoodsInstList):
			if idx < size:
				self.SetVisible(part, True)
			else:
				self.SetVisible(part, False)
		# 重设滚动区域的大小
		height_size = (size+2) // 3
		height = scrollInfo["base_pos"][1] + height_size * (scrollInfo["base_size"][1] + scrollInfo["grid_offset"][1])
		height = max(height, scrollInfo["parent_size"][1])
		self.SetSize(scrollInfo["parent"], (scrollInfo["parent_size"][0], height))
	
	def CloneSingleGood(self, idx, scrollInfo):
		name = "single_good_%d" % idx
		self.Clone(scrollInfo["base"], scrollInfo["parent"], name)
		fullName = "%s/%s" % (scrollInfo["parent"], name)
		self.mGoodsInstList.append(fullName)
		#
		width_idx = idx % 3
		height_idx = idx // 3
		width = scrollInfo["base_pos"][0] + width_idx * (scrollInfo["base_size"][0] + scrollInfo["grid_offset"][0])
		height = scrollInfo["base_pos"][1] + height_idx * (scrollInfo["base_size"][1] + scrollInfo["grid_offset"][1])
		self.SetPosition(fullName, (width, height))
		#
		self.SetTouchEnable(fullName, True)
		self.AddTouchEventHandler(fullName, self.OnClickSingleGood)
	#---------------------------------------------------------------------------------------------------------------------------------
	def OnChangeUseAppearRet(self):
		self.DrawPreviewRight()

	def OnBuyAppearRet(self):
		self.DrawPreviewRight()

	def OnSyncMoney(self, moneyData):
		self.mMoneyData = moneyData
		self.DrawPreviewRight()
	
	def Show(self, moneyData=None):
		self.mDelaySec = 1.0
		if moneyData:
			self.mMoneyData = moneyData
		else:
			self.moneyData = {}
		self.ChangeScreenVisible(True)
		player = self.mSystem.mMe
		for appearType in self.mPropTypes:
			useAppear = player.GetUseAppear(appearType)
			if not useAppear:
				useAppear = "empty"
			self.mPreviewAppear[appearType] = useAppear
		self.DrawSelectPages()
		self.DrawPreviewRight()
	#---------------------------------------------------------------------------------------------------------------------------------
	def OnButtonClose(self, args):
		event = args["TouchEvent"]
		if event == TouchEvent.TouchUp:
			self.ChangeScreenVisible(False)
		elif event == TouchEvent.TouchDown:
			pass
		elif event == TouchEvent.TouchMove:
			pass
		elif event == TouchEvent.TouchCancel:
			pass
	
	def OnButtonPage1(self, args):
		event = args["TouchEvent"]
		if event == TouchEvent.TouchUp:
			self.ChangePage(appearConst.AppearType.Body)
		elif event == TouchEvent.TouchDown:
			pass
		elif event == TouchEvent.TouchMove:
			pass
		elif event == TouchEvent.TouchCancel:
			pass
	
	def OnButtonPage2(self, args):
		event = args["TouchEvent"]
		if event == TouchEvent.TouchUp:
			self.ChangePage(appearConst.AppearType.Wing)
		elif event == TouchEvent.TouchDown:
			pass
		elif event == TouchEvent.TouchMove:
			pass
		elif event == TouchEvent.TouchCancel:
			pass
	
	def OnButtonPage3(self, args):
		event = args["TouchEvent"]
		if event == TouchEvent.TouchUp:
			self.ChangePage(appearConst.AppearType.Mount)
		elif event == TouchEvent.TouchDown:
			pass
		elif event == TouchEvent.TouchMove:
			pass
		elif event == TouchEvent.TouchCancel:
			pass
	
	def OnButtonPage4(self, args):
		event = args["TouchEvent"]
		if event == TouchEvent.TouchUp:
			self.ChangePage(appearConst.AppearType.Aura)
		elif event == TouchEvent.TouchDown:
			pass
		elif event == TouchEvent.TouchMove:
			pass
		elif event == TouchEvent.TouchCancel:
			pass
	
	def ChangePage(self, appearType):
		if appearType == self.mSelectAppearType:
			return
		self.mSelectAppearType = appearType
		self.DrawSelectPages()
		self.DrawPreviewRight()
	
	def DrawSelectPages(self):
		for idx, button in enumerate(self.mPropBtns):
			if idx == 0:
				imageNormal = "textures/ui/netease_appear/tab01"
				imageClick = "textures/ui/netease_appear/tab01_click"
			else:
				imageNormal = "textures/ui/netease_appear/tab02"
				imageClick = "textures/ui/netease_appear/tab02_click"
			appearType = self.mPropTypes[idx]
			if appearType == self.mSelectAppearType:
				self.SetTouchEnable(button, False)
				self.SetSprite("%s/default" % button, imageClick)
			else:
				self.SetTouchEnable(button, True)
				self.SetSprite("%s/default" % button, imageNormal)
		name = AppearTypeName[self.mSelectAppearType]
		self.SetText("/main_pnl/img_base_left/lb_type", name)
		self.mRecentAppears = []
		for keyName, config in appearConst.PropAppears.iteritems():
			if config["type"] != self.mSelectAppearType:
				continue
			data = copy.deepcopy(config)
			data["key"] = keyName
			self.mRecentAppears.append(data)
		emptyData = appearConst.EmptyAppearData.get(self.mSelectAppearType, None)
		if emptyData:
			self.mRecentAppears.append(emptyData)
		self.mRecentAppears.sort(self.CmpAppear)
		#
		length = len(self.mRecentAppears)
		self.ResizeGoods(length)
		for idx in xrange(length):
			self.DrawSingleGood(self.mGoodsInstList[idx], self.mRecentAppears[idx])
			self.DrawSingleGoodSelect(self.mGoodsInstList[idx], self.mRecentAppears[idx])
	
	def CmpAppear(self, a, b):
		return cmp(a["showIndex"], b["showIndex"])
	
	def DrawGoodsSelect(self):
		length = len(self.mRecentAppears)
		for idx in xrange(length):
			self.DrawSingleGoodSelect(self.mGoodsInstList[idx], self.mRecentAppears[idx])
	
	def DrawSingleGood(self, panel, data):
		self.SetSprite("%s/img_goods_baseup/img_goods" % panel, data["icon"])
		self.SetText("%s/img_goods_basedown/lb_goods" % panel, data["showName"])

	def DrawSingleGoodSelect(self, panel, data):
		selectKey = self.mPreviewAppear[self.mSelectAppearType]
		if data["key"] == selectKey:
			self.SetVisible("%s/img_goods_select" % panel, True)
		else:
			self.SetVisible("%s/img_goods_select" % panel, False)
	
	def DrawPreviewVisible(self, isVisible):
		self.SetText("/main_pnl/img_base_right/lb_texture", "预览")
		paperDoll = "/main_pnl/img_base_right/image_inside/paper_doll_preview"
		self.SetVisible(paperDoll, isVisible)
		self.SetVisible("/main_pnl/img_base_right/lb_goodsname", isVisible)
		self.SetVisible("/main_pnl/img_base_right/lb_unselected", not isVisible)
		self.SetVisible("/main_pnl/img_base_right/btn_use", isVisible)
		self.SetVisible("/main_pnl/img_base_right/btn_unused", isVisible)
		self.SetVisible("/main_pnl/img_base_right/btn_price", isVisible)
	
	def DrawPreviewRight(self):
		find = self.FindSelectAppear()
		if not find:
			self.DrawPreviewVisible(False)
			return
		self.DrawPreviewVisible(True)
		self.SetText("/main_pnl/img_base_right/lb_texture", "预览")
		self.SetText("/main_pnl/img_base_right/lb_goodsname", find["showName"])
		self.SetText("/main_pnl/img_base_right/lb_goodsname/label0", find["desc"])
		#
		player = self.mSystem.mMe
		selectKey = self.mPreviewAppear[self.mSelectAppearType]
		isOpen = player.CheckAppearOpen(selectKey)
		useKey = player.GetUseAppear(self.mSelectAppearType)
		if useKey == selectKey:
			self.SetVisible("/main_pnl/img_base_right/btn_use", False)
			self.SetVisible("/main_pnl/img_base_right/btn_unused", True)
			self.SetVisible("/main_pnl/img_base_right/btn_price", False)
		elif isOpen:
			self.SetVisible("/main_pnl/img_base_right/btn_use", True)
			self.SetVisible("/main_pnl/img_base_right/btn_unused", False)
			self.SetVisible("/main_pnl/img_base_right/btn_price", False)
		else:
			self.SetVisible("/main_pnl/img_base_right/btn_use", False)
			self.SetVisible("/main_pnl/img_base_right/btn_unused", False)
			self.SetVisible("/main_pnl/img_base_right/btn_price", True)
			icon, moneyType, moneyValue = find["cost"]["icon"], find["cost"]["type"], find["cost"]["num"]
			self.SetSprite("/main_pnl/img_base_right/btn_price/img_currency", icon)
			hasMoney = self.mMoneyData.get(moneyType, 0)
			self.SetText("/main_pnl/img_base_right/btn_price/lb_price", "%d" % moneyValue)
			if hasMoney >= moneyValue:
				self.SetTextColor("/main_pnl/img_base_right/btn_price/lb_price", (1, 1, 1, 1))
			else:
				self.SetTextColor("/main_pnl/img_base_right/btn_price/lb_price", (1, 0, 0, 1))
		# 
		self.DrawPaperDoll(self.mSelectAppearType, find)
	#----------------------------------------------------------------------------------------------------------------------------------------
	# 渲染NeteasePapelDoll
	def DrawPaperDoll(self, appearType, data):
		self.CleanAddonEffects()
		# 坐骑类，仅显示坐骑
		if self.mSelectAppearType == appearConst.AppearType.Mount:
			if data["key"] == "empty":
				modelName = "v_unvisible_bind"
				aniName = "idle"
			else:
				model = data["src"][1]
				modelConfig = appearConst.PropModels[model]
				modelName = modelConfig["modelName"]
				aniName = modelConfig["idle"]
			self.DrawPaperDollByModel(modelName, aniName)
			return
		# 非坐骑类，先渲染人物
		bodyValue = self.mPreviewAppear[appearConst.AppearType.Body]
		appearConfig = appearConst.PropAppears[bodyValue]
		model = appearConfig["src"][1]
		modelConfig = appearConst.PropModels[model]
		modelName = modelConfig["modelName"]
		aniName = modelConfig["idle"]
		self.DrawPaperDollByModel(modelName, aniName)
		# 需要延时之后才能够获得真实的modelId
		comp = clientApi.GetEngineCompFactory().CreateGame(clientApi.GetLevelId())
		comp.AddTimer(self.mDelaySec, self.DrawOtherAddonEffects)
		# 每次重新打开界面时，首次渲染模型需要更久的delay
		self.mDelaySec = 0.1

	def DrawOtherAddonEffects(self):
		paperDoll = "/main_pnl/img_base_right/image_inside/paper_doll_preview"
		modelId = self.GetNeteasePaperDollModelId(paperDoll)
		# print "DrawPaperDollByModel modelId={}".format(modelId)
		# 统计其他特效
		extraAddon = []
		for appearType in (appearConst.AppearType.Wing, appearConst.AppearType.Aura):
			appearValue = self.mPreviewAppear.get(appearType, "empty")
			if appearValue == "empty":
				continue
			extraAddon.append(appearValue)
		# print "draw extraAddon={}".format(extraAddon)
		for appearValue in extraAddon:
			self.DrawAddonEffect(modelId, appearValue)

	def CleanAddonEffects(self):
		if not self.mPreviewExtraDataList:
			return
		for idData in self.mPreviewExtraDataList:
			style = idData[0]
			if style == "model":
				effectId, modelId = idData[1], idData[2]
				otherModelComp = clientApi.GetEngineCompFactory().CreateModel(modelId)
				otherModelComp.UnBindModelToModel(effectId)
			else:
				effectId = idData[1]
				self.mSystem.DestroyEntity(effectId)
				# print "paper doll destroy effect id={}".format(effectId)
		self.mPreviewExtraDataList = []
	
	def DrawAddonEffect(self, modelId, appearValue):
		appearConfig = appearConst.PropAppears[appearValue]
		length = len(appearConfig["src"]) // 2
		for i in xrange(length):
			srcType, srcName = appearConfig["src"][i*2], appearConfig["src"][i*2+1]
			idData = None 
			if srcType == "model":
				srcConfig = appearConst.PropModels[srcName]
				idData = self.DoAddModelEffect(modelId, srcConfig)
			elif srcType == "effect":
				srcConfig = appearConst.PropEffects[srcName]
				if srcConfig["type"] == "sfx":
					idData = self.DoAddSfxEffect(modelId, srcConfig)
				else:
					idData = self.DoAddParticleEffect(modelId, srcConfig)
			if idData:
				self.mPreviewExtraDataList.append(idData)
	
	def DrawPaperDollByModel(self, modelName, aniName):
		paperDoll = "/main_pnl/img_base_right/image_inside/paper_doll_preview"
		params = {
			"skeleton_model_name": modelName,
			"scale": 1.0,
			"animation": aniName,
			"animation_looped": True,
		}
		self.RenderPaperDoll(paperDoll, params)
		return self.GetNeteasePaperDollModelId(paperDoll)

	def DoAddModelEffect(self, modelId, srcConfig):
		bindBone, pos, rot = srcConfig["bindBone"], tuple(srcConfig["pos"]), tuple(srcConfig["rot"])
		modelName, aniName = srcConfig["modelName"], srcConfig["aniName"]

		otherModelComp = clientApi.GetEngineCompFactory().CreateModel(modelId)
		effectId = otherModelComp.BindModelToModel(bindBone, modelName, pos, rot)
		#print "paper doll DoAddModelEffect effectId={}".format(effectId)
		otherModelComp.ModelPlayAni(effectId, aniName, True)

		return "model", effectId, modelId

	def DoAddSfxEffect(self, modelId, srcConfig):
		bindBone, pos, rot = srcConfig["bindBone"], tuple(srcConfig["pos4ui"]), tuple(srcConfig["rot4ui"])
		path = srcConfig["path"]

		effectId = self.mSystem.CreateEngineSfxFromEditor(path)
		# print "paper doll DoAddSfxEffect effectId={}".format(effectId)
		bindComp = clientApi.GetEngineCompFactory().CreateFrameAniSkeletonBind(effectId)
		bindComp.Bind(modelId, bindBone, pos, rot)
		controlComp = clientApi.GetEngineCompFactory().CreateFrameAniControl(effectId)
		controlComp.Play()

		return "sfx", effectId

	def DoAddParticleEffect(self, modelId, srcConfig):
		bindBone, pos, rot = srcConfig["bindBone"], tuple(srcConfig["pos4ui"]), tuple(srcConfig["rot4ui"])
		path = srcConfig["path"]

		effectId = self.mSystem.CreateEngineParticle(path, (0,0,0))
		# print "paper doll DoAddParticleEffect effectId={}".format(effectId)
		bindComp = clientApi.GetEngineCompFactory().CreateParticleSkeletonBind(effectId)
		bindComp.Bind(modelId, bindBone, pos, rot)
		controlComp = clientApi.GetEngineCompFactory().CreateParticleControl(effectId)
		controlComp.Play()
		
		return "particle", effectId
	#---------------------------------------------------------------------------------------------------------------------------------
	def FindSelectAppear(self):
		selectKey = self.mPreviewAppear[self.mSelectAppearType]
		for data in self.mRecentAppears:
			if data["key"] == selectKey:
				return data
		return None

	def OnButtonUse(self, args):
		event = args["TouchEvent"]
		if event == TouchEvent.TouchUp:
			find = self.FindSelectAppear()
			if not find:
				return
			appearKey = find["key"]
			if appearKey == "empty":
				appearKey = None
			eventData = {
				"playerId": self.mSystem.mPlayerId,
				"appearType": self.mSelectAppearType,
				"appearKey": appearKey,
			}
			self.mSystem.NotifyToServer(ClientEvent.ChangeUseAppear, eventData)
		elif event == TouchEvent.TouchDown:
			pass
		elif event == TouchEvent.TouchMove:
			pass
		elif event == TouchEvent.TouchCancel:
			pass
	
	def OnButtonBuy(self, args):
		event = args["TouchEvent"]
		if event == TouchEvent.TouchUp:
			find = self.FindSelectAppear()
			if not find:
				return
			appearKey = find["key"]
			if appearKey == "empty":
				return
			eventData = {
				"playerId": self.mSystem.mPlayerId,
				"appearKey": appearKey,
			}
			self.mSystem.NotifyToServer(ClientEvent.BuyAppear, eventData)
		elif event == TouchEvent.TouchDown:
			pass
		elif event == TouchEvent.TouchMove:
			pass
		elif event == TouchEvent.TouchCancel:
			pass
	
	def OnClickSingleGood(self, args):
		line = args["ButtonPath"].split("/")
		line = line[-1]
		line = line.split("_")
		idx = int(line[-1])
		event = args["TouchEvent"]
		if event == TouchEvent.TouchUp:
			self.OnChangePreviewSelect(idx)
		elif event == TouchEvent.TouchDown:
			pass
		elif event == TouchEvent.TouchMove:
			pass
		elif event == TouchEvent.TouchCancel:
			pass
	
	def OnChangePreviewSelect(self, idx):
		if idx >= len(self.mRecentAppears):
			return
		data = self.mRecentAppears[idx]
		oldKey = self.mPreviewAppear[self.mSelectAppearType]
		if oldKey == data["key"]:
			return
		self.mPreviewAppear[self.mSelectAppearType] = data["key"]
		self.DrawGoodsSelect()
		self.DrawPreviewRight()

