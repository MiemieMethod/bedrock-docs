# -*- coding: utf-8 -*-

# 从客户端API中拿到我们需要的ViewBinder / ViewRequest / ScreenNode
import client.extraClientApi as clientApi
ViewBinder = clientApi.GetViewBinderCls()
ViewRequest = clientApi.GetViewViewRequestCls()
ScreenNode = clientApi.GetScreenNodeCls()
from functools import wraps


def touch_filter(touchType):
	def touchFilter(func):
		@wraps(func)
		def decorated(*args, **kwargs):
			touchEventEnum = clientApi.GetMinecraftEnum().TouchEvent
			touchEvent = args[1]["TouchEvent"]
			if touchType == "up":
				if touchEvent == touchEventEnum.TouchUp:
					value = func(*args, **kwargs)
					return value
			if touchType == "down":
				if touchEvent == touchEventEnum.TouchDown:
					value = func(*args, **kwargs)
					return value
			if touchType == "cancel":
				if touchEvent == touchEventEnum.TouchCancel:
					value = func(*args, **kwargs)
					return value
			if touchType == "move":
				if touchEvent == touchEventEnum.TouchMove:
					value = func(*args, **kwargs)
					return value
		return decorated
	return touchFilter


# 所有的UI类需要继承自引擎的ScreenNode类
class UIDemoScreen(ScreenNode):
	def __init__(self, namespace, name, param):
		ScreenNode.__init__(self, namespace, name, param)
		# 欢迎面板
		self.welcomePanel = "/welcomePanel"
		# 教程面板
		self.demoPanel = "/demoPanel"
		# 文本+文本输入框示例
		self.demoText = ""
		# 纸娃娃示例
		self.demoDoll_doll = self.demoPanel + "/dollPanel/paper_doll0"
		# 滚动列表示例
		# 网格示例
		self.demoGrid_grid = self.demoPanel + "/gridPanel/grid1"
		self.currentGridItemShowNum = -1
		self.maxGridItemShowNum = 0
		# 进度条示例
		self.currentProgress = 0.0
		# 开关示例
		self.currentToggleShow = True
		# 道具渲染控件示例
		self.demoItemRenderer_renderer = self.demoPanel + "/itemRendererPanel/itemRendererWidget"
		# InputPanel
		# 富文本示例
		self.demoRichText_richTextItem = self.demoPanel + "/RichTextPanel/richTextPanel"
		self.richTextItem = None
		# 滑动条示例
		self.sliderValue = 0
		self.sliderAbsValue = 0.5

	# Create函数是继承自ScreenNode，会在UI创建完成后被调用
	def Create(self):
		print("===== UIDemoScreen Create =====")
		self.welcomePanelItem = self.GetBaseUIControl(self.welcomePanel)
		self.demoPanelItem = self.GetBaseUIControl(self.demoPanel)
		# 主界面按钮对象
		self.demoExitButton = self.demoPanelItem.GetChildByPath("/ExitButton").asButton()

		self.welcomeLabelItem = self.welcomePanelItem.GetChildByPath("/labelDemo").asButton()
		self.welcomeImageItem = self.welcomePanelItem.GetChildByPath("/imageDemo").asButton()
		self.welcomeButtonItem = self.welcomePanelItem.GetChildByPath("/buttonDemo").asButton()
		self.welcomeTextEditItem = self.welcomePanelItem.GetChildByPath("/textEditorDemo").asButton()
		self.welcomeDollItem = self.welcomePanelItem.GetChildByPath("/dollDemo").asButton()
		self.welcomeScrollViewItem = self.welcomePanelItem.GetChildByPath("/scrollViewDemo").asButton()
		self.welcomeProgressBarItem = self.welcomePanelItem.GetChildByPath("/progressBarDemo").asButton()
		self.welcomeToggleItem = self.welcomePanelItem.GetChildByPath("/toggleDemo").asButton()
		self.welcomeGridItem = self.welcomePanelItem.GetChildByPath("/gridDemo").asButton()
		self.welcomeItemRendererItem = self.welcomePanelItem.GetChildByPath("/itemRendererDemo").asButton()
		self.welcomeInputPanelItem = self.welcomePanelItem.GetChildByPath("/inputPanelDemo").asButton()
		self.welcomeRichTextItem = self.welcomePanelItem.GetChildByPath("/RichTextDemo").asButton()
		self.welcomePushScreenItem = self.welcomePanelItem.GetChildByPath("/pushScreenBtn").asButton()
		self.welcomeToggleRadioItem = self.welcomePanelItem.GetChildByPath("/toggleRadioBtn").asButton()
		self.welcomeSliderItem = self.welcomePanelItem.GetChildByPath("/sliderBtn").asButton()
		# 文本示例对象
		self.demoLabelTextItem = self.demoPanelItem.GetChildByPath("/labelTextPanel")
		# 图片-按钮示例对象
		self.demoImageButtonItem = self.demoPanelItem.GetChildByPath("/imageButtonPanel")
		self.demoImageButton0Item = self.demoImageButtonItem.GetChildByName("button0").asButton()
		self.demoImageButton1Item = self.demoImageButtonItem.GetChildByName("button1").asButton()
		# 纸娃娃示例对象
		self.demoDollItem = self.demoPanelItem.GetChildByPath("/dollPanel")
		self.demoDollButton0Item = self.demoDollItem.GetChildByName("button2").asButton()
		self.demoDollButton1Item = self.demoDollItem.GetChildByName("button3").asButton()
		# 滚动列表示例对象
		self.demoScrollViewItem = self.demoPanelItem.GetChildByPath("/scrollViewPanel")
		# 进度条示例对象
		self.demoProgressBarItem = self.demoPanelItem.GetChildByPath("/progressBarPanel")
		self.demoProgressBarValueItem = self.demoProgressBarItem.GetChildByPath("/progress_bar0").asProgressBar("/filled_progress_bar")
		self.demoProgressBarButtonAddItem = self.demoProgressBarItem.GetChildByName("button5").asButton()
		self.demoProgressBarButtonReduceItem = self.demoProgressBarItem.GetChildByName("button4").asButton()
		# 开关示例对象
		self.demoToggleItem = self.demoPanelItem.GetChildByPath("/togglePanel")
		self.demoToggleLabelItem = self.demoToggleItem.GetChildByPath("/label1")
		# 网格示例对象
		self.demoGridItem = self.demoPanelItem.GetChildByPath("/gridPanel")
		self.demoGridAddButton = self.demoGridItem.GetChildByName("addBtn").asButton()
		self.demoGridReduceButton = self.demoGridItem.GetChildByName("reduceBtn").asButton()
		# 道具渲染示例对象
		self.demoItemRendererItem = self.demoPanelItem.GetChildByPath("/itemRendererPanel")
		self.demoItemRendererWoolButton = self.demoItemRendererItem.GetChildByName("woolRender").asButton()
		self.demoItemRendererWoodButton = self.demoItemRendererItem.GetChildByName("woodRender").asButton()
		# inputPanel示例对象
		self.demoInputPanelItem = self.demoPanelItem.GetChildByPath("/inputPanelPanel")
		self.demoInputPanelOpenButton = self.demoInputPanelItem.GetChildByName("inputPanelOpenBtn").asButton()
		self.demoInputPanelPanel = self.demoInputPanelItem.GetChildByName("inputPanel")
		self.demoInputPanelCloseButton = self.demoInputPanelPanel.GetChildByName("inputPanelCloseBtn").asButton()
		# 富文本示例对象
		self.demoRichTextItem = self.demoPanelItem.GetChildByPath("/RichTextPanel")
		# 复选按钮示例对象
		self.demoToggleRatioItem = self.demoPanelItem.GetChildByPath("/toggleRadioPanel")
		# 滑动条示例对象
		self.demoSliderItem = self.demoPanelItem.GetChildByPath("/SliderPanel")
		self.demoAbsSlider = self.demoSliderItem.GetChildByPath("/slider0").asSlider()
		self.demoSlider = self.demoSliderItem.GetChildByPath("/slider1").asSlider()
		self.demoSliderAbsLabelItem = self.demoSliderItem.GetChildByPath("/slider_label0").asLabel()
		self.demoSliderLabelItem = self.demoSliderItem.GetChildByPath("/slider_label1").asLabel()
		# 欢迎界面按钮注册
		self.welcomeLabelItem.AddTouchEventParams({"isSwallow": True})
		self.welcomeLabelItem.SetButtonTouchUpCallback(self.OnWelcomeLabelTouch)
		self.welcomeButtonItem.AddTouchEventParams({"isSwallow": True})
		self.welcomeButtonItem.SetButtonTouchUpCallback(self.OnWelcomeButtonTouch)
		self.welcomeImageItem.AddTouchEventParams({"isSwallow": True})
		self.welcomeImageItem.SetButtonTouchUpCallback(self.OnWelcomeImageTouch)
		self.welcomeTextEditItem.AddTouchEventParams({"isSwallow": True})
		self.welcomeTextEditItem.SetButtonTouchUpCallback(self.OnWelcomeTextEditorTouch)
		self.welcomeDollItem.AddTouchEventParams({"isSwallow": True})
		self.welcomeDollItem.SetButtonTouchUpCallback(self.OnWelcomeDollTouch)
		self.welcomeScrollViewItem.AddTouchEventParams({"isSwallow": True})
		self.welcomeScrollViewItem.SetButtonTouchUpCallback(self.OnWelcomeScrollViewTouch)
		self.welcomeProgressBarItem.AddTouchEventParams({"isSwallow": True})
		self.welcomeProgressBarItem.SetButtonTouchUpCallback(self.OnWelcomeProgressBarTouch)
		self.welcomeToggleItem.AddTouchEventParams({"isSwallow": True})
		self.welcomeToggleItem.SetButtonTouchUpCallback(self.OnWelcomeToggleTouch)
		self.welcomeGridItem.AddTouchEventParams({"isSwallow": True})
		self.welcomeGridItem.SetButtonTouchUpCallback(self.OnWelcomeGridTouch)
		self.welcomeItemRendererItem.AddTouchEventParams({"isSwallow": True})
		self.welcomeItemRendererItem.SetButtonTouchUpCallback(self.OnWelcomeItemRendererTouch)
		self.welcomeInputPanelItem.AddTouchEventParams({"isSwallow": True})
		self.welcomeInputPanelItem.SetButtonTouchUpCallback(self.OnWelcomeInputPanel)
		self.welcomeRichTextItem.AddTouchEventParams({"isSwallow": True})
		self.welcomeRichTextItem.SetButtonTouchUpCallback(self.OnWelcomeRichText)
		self.welcomePushScreenItem.AddTouchEventParams({"isSwallow": True})
		self.welcomePushScreenItem.SetButtonTouchUpCallback(self.OnPushScreen)
		self.welcomeToggleRadioItem.AddTouchEventParams({"isSwallow": True})
		self.welcomeToggleRadioItem.SetButtonTouchUpCallback(self.OnToggleRadioBtn)
		self.welcomeSliderItem.AddTouchEventParams({"isSwallow": True})
		self.welcomeSliderItem.SetButtonTouchUpCallback(self.OnSliderBtn)
		# 示例界面按钮注册
		self.demoExitButton.AddTouchEventParams({"isSwallow": True})
		self.demoExitButton.SetButtonTouchUpCallback(self.OnBackToWelcomeTouch)
		# 图片-按钮示例
		self.demoImageButton0Item.AddTouchEventParams({"isSwallow": True})
		self.demoImageButton0Item.SetButtonTouchUpCallback(self.OnDemoImageButtonFirstImageTouch)
		self.demoImageButton1Item.AddTouchEventParams({"isSwallow": True})
		self.demoImageButton1Item.SetButtonTouchUpCallback(self.OnDemoImageButtonSecondImageTouch)
		# 纸娃娃示例
		self.demoDollButton0Item.AddTouchEventParams({"isSwallow": True})
		self.demoDollButton0Item.SetButtonTouchUpCallback(self.OnDemoDollFirstDollTouch)
		self.demoDollButton1Item.AddTouchEventParams({"isSwallow": True})
		self.demoDollButton1Item.SetButtonTouchUpCallback(self.OnDemoDollSecondDollTouch)
		# 网格示例
		self.demoGridAddButton.AddTouchEventParams({"isSwallow": True})
		self.demoGridAddButton.SetButtonTouchUpCallback(self.OnDemoGridAddItemTouch)
		self.demoGridReduceButton.AddTouchEventParams({"isSwallow": True})
		self.demoGridReduceButton.SetButtonTouchUpCallback(self.OnDemoGridReduceItemTouch)
		# 进度条示例
		self.demoProgressBarButtonAddItem.AddTouchEventParams({"isSwallow": True})
		self.demoProgressBarButtonAddItem.SetButtonTouchUpCallback(self.OnDemoProgressBarAddTouch)
		self.demoProgressBarButtonReduceItem.AddTouchEventParams({"isSwallow": True})
		self.demoProgressBarButtonReduceItem.SetButtonTouchUpCallback(self.OnDemoProgressBarReduceTouch)
		# 道具渲染示例
		self.demoItemRendererWoolButton.AddTouchEventParams({"isSwallow": True})
		self.demoItemRendererWoolButton.SetButtonTouchUpCallback(self.OnDemoItemRendererWoolTouch)
		self.demoItemRendererWoodButton.AddTouchEventParams({"isSwallow": True})
		self.demoItemRendererWoodButton.SetButtonTouchUpCallback(self.OnDemoItemRendererWoodTouch)
		# InputPanel
		self.demoInputPanelOpenButton.AddTouchEventParams({"isSwallow": True})
		self.demoInputPanelOpenButton.SetButtonTouchUpCallback(self.OnDemoInputPanelOpenBtn)
		self.demoInputPanelCloseButton.AddTouchEventParams({"isSwallow": True})
		self.demoInputPanelCloseButton.SetButtonTouchUpCallback(self.OnDemoInputPanelCloseBtn)
		# 富文本示例
		self.richTextItem = self.GetRichTextItem(self.demoRichText_richTextItem)
		self.richTextItem.registerLinkItemClickCallback(self.OnLinkItemClickCallback)
		self.richTextItem.registerButtonItemClickCallback(self.OnButtonItemClickCallback)
		self.richTextItem.registerRichTextFinishCallback(self.OnRichTextCreateFinishCallback)
		# 滑动条示例

	# 界面的一些初始化操作
	def Init(self):
		# 隐藏瞄准界面
		clientApi.SetInputMode(1)
		clientApi.SetResponse(False)
		clientApi.HideSlotBarGui(True)
		self.changeToWelcomePanel(True)

	# 继承自ScreenNode的方法，会被引擎自动调用，1秒钟30帧
	def Update(self):
		"""
		node tick function
		"""
		pass

	# 欢迎界面按钮回调
	def changeToWelcomePanel(self, toWelcome):
		if toWelcome:
			self.welcomePanelItem.SetVisible(True)
			self.demoPanelItem.SetVisible(False)
		else:
			self.welcomePanelItem.SetVisible(False)
			self.demoPanelItem.SetVisible(True)

	def OnWelcomeLabelTouch(self, args):
		self.changeToWelcomePanel(False)
		self.demoLabelTextItem.SetVisible(True)

	def OnWelcomeImageTouch(self, args):
		self.changeToWelcomePanel(False)
		self.demoImageButtonItem.SetVisible(True)

	def OnWelcomeButtonTouch(self, args):
		self.changeToWelcomePanel(False)
		self.demoImageButtonItem.SetVisible(True)

	def OnWelcomeTextEditorTouch(self, args):
		self.changeToWelcomePanel(False)
		self.demoLabelTextItem.SetVisible(True)

	def OnWelcomeDollTouch(self, args):
		self.changeToWelcomePanel(False)
		self.demoDollItem.SetVisible(True)

	def OnWelcomeScrollViewTouch(self, args):
		self.changeToWelcomePanel(False)
		self.demoScrollViewItem.SetVisible(True)

	def OnWelcomeProgressBarTouch(self, args):
		self.changeToWelcomePanel(False)
		self.demoProgressBarItem.SetVisible(True)
		self.demoProgressBarValueItem.SetValue(self.currentProgress)

	def OnWelcomeToggleTouch(self, args):
		self.changeToWelcomePanel(False)
		self.demoToggleItem.SetVisible(True)

	def OnWelcomeGridTouch(self,args):
		self.changeToWelcomePanel(False)
		self.demoGridItem.SetVisible(True)

	def OnWelcomeItemRendererTouch(self, args):
		self.changeToWelcomePanel(False)
		self.demoItemRendererItem.SetVisible(True)

	def OnWelcomeInputPanel(self,args):
		self.changeToWelcomePanel(False)
		self.demoInputPanelItem.SetVisible(True)

	def OnWelcomeRichText(self, args):
		self.changeToWelcomePanel(False)
		self.demoRichTextItem.SetVisible(True)
		self.richTextItem.readRichText('[玩家]玩家一<button>{"press_texture" : "textures/ui/btn_pressed","hover_texture" : "textures/ui/btn_hover","default_texture" : "textures/ui/btn_light_default","x":20, "y":20}</button>:恭喜！<image>{"texture":"textures/ui/skin/ty_yuanshenghuli_0_0", "x":30, "y":30}</image>击杀了<link>{"text" : "末影人", "format_code":"§2"}</link><sfx>{"texture": "textures/ui/my_eating_apple","x":30, "y":30,"uv_x": 64,"uv_y": 64,"frame_count": 36,"fps": 10}</sfx>')

	def OnPushScreen(self, *args):
		from uidemoScripts.modCommon import modConfig
		clientApi.RegisterUI(modConfig.ModName, modConfig.MainScreenUIName, modConfig.MainScreenPyClsPath, modConfig.MainScreenScreenDef)
		clientApi.PushScreen(modConfig.ModName, modConfig.MainScreenUIName)

	def OnToggleRadioBtn(self, *args):
		self.changeToWelcomePanel(False)
		self.demoToggleRatioItem.SetVisible(True)

	def OnSliderBtn(self, *args):
		self.changeToWelcomePanel(False)
		self.demoSliderItem.SetVisible(True)
		self.sliderAbsValue = 5.0
		self.demoAbsSlider.SetSliderValue(self.sliderAbsValue)

	# 示例场景按钮回调
	def OnBackToWelcomeTouch(self,args):
		self.changeToWelcomePanel(True)
		self.demoLabelTextItem.SetVisible(False)
		self.demoImageButtonItem.SetVisible(False)
		self.demoDollItem.SetVisible(False)
		self.demoScrollViewItem.SetVisible(False)
		self.demoProgressBarItem.SetVisible(False)
		self.demoToggleItem.SetVisible(False)
		self.demoGridItem.SetVisible(False)
		self.demoItemRendererItem.SetVisible(False)
		self.demoInputPanelItem.SetVisible(False)
		self.demoRichTextItem.SetVisible(False)
		self.demoToggleRatioItem.SetVisible(False)
		self.demoSliderItem.SetVisible(False)

	# 文本-文本输入框示例
	@ViewBinder.binding(ViewBinder.BF_EditChanged | ViewBinder.BF_EditFinished)
	def OnDemoLabelTextOnTextEditCallback(self,args):
		self.demoText = args["Text"]
		labelItem = self.demoLabelTextItem.GetChildByName("label0").asLabel()
		if labelItem:
			labelItem.SetText(self.demoText)
		return ViewRequest.Refresh

	@ViewBinder.binding(ViewBinder.BF_BindString)
	def ReturnTextString(self):
		return self.demoText

	# 图片-按钮示例
	def OnDemoImageButtonFirstImageTouch(self, args):
		imageItem = self.demoImageButtonItem.GetChildByName("image0").asImage()
		if imageItem:
			imageItem.SetSprite("textures/ui/aim")

	def OnDemoImageButtonSecondImageTouch(self, args):
		imageItem = self.demoImageButtonItem.GetChildByName("image0").asImage()
		if imageItem:
			imageItem.SetSprite("textures/ui/my_cross_hair")

	# 纸娃娃示例
	def OnDemoDollFirstDollTouch(self,args):
		self.SetUiModel(self.demoDoll_doll,"Steve")

	def OnDemoDollSecondDollTouch(self,args):
		self.SetUiModel(self.demoDoll_doll,"datiangou")

	# 网格示例
	def OnDemoGridAddItemTouch(self,args):
		gridItemsList = self.GetChildrenName(self.demoGrid_grid)
		if self.maxGridItemShowNum == 0:
			self.maxGridItemShowNum = len(gridItemsList)
		if self.currentGridItemShowNum == -1:
			self.currentGridItemShowNum = self.maxGridItemShowNum
		if self.currentGridItemShowNum < self.maxGridItemShowNum:
			self.currentGridItemShowNum += 1
			self.SetVisible(self.demoGrid_grid + "/" + gridItemsList[self.currentGridItemShowNum-1],True)

	def OnDemoGridReduceItemTouch(self,args):
		gridItemsList = self.GetChildrenName(self.demoGrid_grid)
		if self.maxGridItemShowNum == 0:
			self.maxGridItemShowNum = len(gridItemsList)
		if self.currentGridItemShowNum == -1:
			self.currentGridItemShowNum = self.maxGridItemShowNum
		if self.currentGridItemShowNum > 0:
			self.SetVisible(self.demoGrid_grid + "/" + gridItemsList[self.currentGridItemShowNum-1], False)
			self.currentGridItemShowNum -= 1

	# 进度条示例
	def OnDemoProgressBarAddTouch(self,args):
		if self.currentProgress >= 1.0:
			return
		self.currentProgress += 0.1
		self.demoProgressBarValueItem.SetValue(self.currentProgress)

	def OnDemoProgressBarReduceTouch(self,args):
		if self.currentProgress <= 0.0:
			return
		self.currentProgress -= 0.1
		self.demoProgressBarValueItem.SetValue(self.currentProgress)

	def OnDemoItemRendererWoolTouch(self, args):
		self.SetUiItem(self.demoItemRenderer_renderer, 'minecraft:wool', 0)

	def OnDemoItemRendererWoodTouch(self, args):
		self.SetUiItem(self.demoItemRenderer_renderer, 'minecraft:wood', 0)

	# 开关示例
	@ViewBinder.binding(ViewBinder.BF_ToggleChanged)
	def OnDemoToggleChangeCallback(self,args):
		self.currentToggleShow = args["state"]
		self.demoToggleLabelItem.SetVisible(self.currentToggleShow)
		return ViewRequest.Refresh

	@ViewBinder.binding(ViewBinder.BF_BindBool)
	def ReturnToggleState(self):
		return self.currentToggleShow

	# InputPanel
	def OnDemoInputPanelOpenBtn(self,args):
		self.demoInputPanelPanel.SetVisible(True)

	def OnDemoInputPanelCloseBtn(self,args):
		self.demoInputPanelPanel.SetVisible(False)

	def OnButtonItemClickCallback(self, data, touchX, touchY):
		print("---OnButtonItemClickCallback---", data, touchX, touchY)

	def OnLinkItemClickCallback(self, data, touchX, touchY):
		print("---OnLinkItemClickCallback---", data, touchX, touchY)

	def OnRichTextCreateFinishCallback(self):
		print("---OnRichTextCreateFinishCallback---")

	# toggle radio panel 单选分页示例
	@ViewBinder.binding(ViewBinder.BF_ToggleChanged, "#toggle_radio_tab")
	def OnToggleChecked(self, args):
		toggleIndex = args["index"]
		if toggleIndex == 0:
			self.demoLabelTextItem.SetVisible(True)
			self.demoImageButtonItem.SetVisible(False)
			self.demoDollItem.SetVisible(False)
		elif toggleIndex == 1:
			self.demoLabelTextItem.SetVisible(False)
			self.demoImageButtonItem.SetVisible(True)
			self.demoDollItem.SetVisible(False)
		elif toggleIndex == 2:
			self.demoLabelTextItem.SetVisible(False)
			self.demoImageButtonItem.SetVisible(False)
			self.demoDollItem.SetVisible(True)

	# 滑动条示例
	@ViewBinder.binding(ViewBinder.BF_SliderChanged | ViewBinder.BF_SliderFinished)
	def OnSliderChange(self, value, isFinish, _unused):
		self.sliderValue = value
		text = str(self.sliderValue)
		if isFinish:
			text += " Finish!"
		self.demoSliderLabelItem.SetText(text)
		return ViewRequest.Refresh

	@ViewBinder.binding(ViewBinder.BF_BindFloat)
	def ReturnSliderValue(self):
		return self.sliderValue

	@ViewBinder.binding(ViewBinder.BF_BindInt)
	def ReturnSliderStep(self):
		return 1

	@ViewBinder.binding(ViewBinder.BF_SliderChanged | ViewBinder.BF_SliderFinished)
	def OnAbsSliderChange(self, value, isFinish, _unused):
		self.sliderAbsValue = value
		text = str(self.sliderAbsValue)
		if isFinish:
			text += " Finish!"
		self.demoSliderAbsLabelItem.SetText(text)
		return ViewRequest.Refresh

	@ViewBinder.binding(ViewBinder.BF_BindFloat)
	def ReturnAbsSliderValue(self):
		return self.sliderAbsValue

	@ViewBinder.binding(ViewBinder.BF_BindInt)
	def ReturnAbsSliderStep(self):
		return 10
