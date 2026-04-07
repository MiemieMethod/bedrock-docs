# -*- coding: utf-8 -*-
import weakref
import time

import client.extraClientApi as clientApi
ViewBinder = clientApi.GetViewBinderCls()
ViewRequest = clientApi.GetViewViewRequestCls()
ScreenNode = clientApi.GetScreenNodeCls()
TouchEvent = clientApi.GetMinecraftEnum().TouchEvent
from mod_log import engine_logger as logger

from neteaseAddupScript.addupConsts import ClientEvent
import neteaseAddupScript.addupConsts as addupConsts

Qual2ImageMap = {
	1: "textures/ui/netease_addup/img01",
	2: "textures/ui/netease_addup/img02",
	3: "textures/ui/netease_addup/img03",
	4: "textures/ui/netease_addup/img04",
	5: "textures/ui/netease_addup/img05",
	6: "textures/ui/netease_addup/img06",
}

class BonusScreen(ScreenNode):
	def __init__(self, namespace, name, param):
		ScreenNode.__init__(self, namespace, name, param)
		self.mUiKey = "bonus"
		self.mSystem = None
		#
		self.mAddupKey = None
		self.mTimer = None
		self.mShowHintLeftSec = 0

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
		if flag:
			if not self.mTimer:
				comp = clientApi.GetEngineCompFactory().CreateGame(clientApi.GetLevelId())
				self.mTimer = comp.AddRepeatedTimer(1.0, self.OnTick)
		else:
			if self.mTimer:
				comp = clientApi.GetEngineCompFactory().CreateGame(clientApi.GetLevelId())
				comp.CancelTimer(self.mTimer)
				self.mTimer = None
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
		self.AddTouchEventHandler("/main_pnl/img_base_dialog/btn_close", self.OnButtonClose)
		self.AddTouchEventHandler("/main_pnl/img_base_dialog/btn_consume", self.OnButtonConsume)
		#
		self.HideGetBonusSuc()
		# 奖励列表
		scrollInfo = {}
		scrollBase = "/main_pnl/img_base_dialog/scroll_rewards"
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
		scrollInfo["base"] = scrollInfo["parent"] + "/single_quest"
		scrollInfo["base_size"] = self.GetSize(scrollInfo["base"])
		scrollInfo["base_pos"] = self.GetPosition(scrollInfo["base"])
		scrollInfo["grid_offset"] = 2
		scrollInfo["size"] = 0
		self.SetVisible(scrollInfo["base"], False)
		self.mQuestInstList = []
		self.mQuestScrollInfo = scrollInfo
		self.ResizeQuests(0)

	def ResizeQuests(self, size):
		# 假如resize的尺寸刚好和之前的尺寸相同，那么不需要做任何事，直接return
		# 某些全局刷新操作也会触发这个函数
		scrollInfo = self.mQuestScrollInfo
		if size == scrollInfo["size"]:
			return
		# 记录下最新的列表尺寸
		scrollInfo["size"] = size
		# 计算一下需要新生成的单个控件数量
		lackNum = size - len(self.mQuestInstList)
		# 控件不够用，创建一些
		if lackNum > 0:
			beginIndex = len(self.mQuestInstList)
			for idx in xrange(lackNum):
				self.CloneSingleQuest(beginIndex + idx, scrollInfo)
		# 控件多余了，那么隐藏多余不用的控件
		for idx, part in enumerate(self.mQuestInstList):
			if idx < size:
				self.SetVisible(part, True)
			else:
				self.SetVisible(part, False)
		# 重设滚动区域的大小
		height_size = size
		height = scrollInfo["base_pos"][1] + height_size * (scrollInfo["base_size"][1] + scrollInfo["grid_offset"])
		height = max(height, scrollInfo["parent_size"][1])
		self.SetSize(scrollInfo["parent"], (scrollInfo["parent_size"][0], height))
	
	def CloneSingleQuest(self, idx, scrollInfo):
		name = "single_quest_%d" % idx
		self.Clone(scrollInfo["base"], scrollInfo["parent"], name)
		fullName = "%s/%s" % (scrollInfo["parent"], name)
		self.mQuestInstList.append(fullName)
		#
		height_idx = idx
		width = scrollInfo["base_pos"][0]
		height = scrollInfo["base_pos"][1] + height_idx * (scrollInfo["base_size"][1] + scrollInfo["grid_offset"])
		self.SetPosition(fullName, (width, height))
		#
		self.AddTouchEventHandler("%s/btn_get_bonus" % fullName, self.OnTryGetBonus)
		for i in xrange(5):
			button = "%s/item_%d/btn_qual_%d" % (fullName, i, i)
			self.AddTouchEventHandler(button, self.OnClickReward)
	#---------------------------------------------------------------------------------------------------------------------------------
	def Show(self, addupKey):
		self.mAddupKey = addupKey
		self.mAddupConfig = addupConsts.AllActivityData[addupKey]
		self.ChangeScreenVisible(True)
		self.DrawAddupAll()
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

	def OnButtonConsume(self, args):
		event = args["TouchEvent"]
		if event == TouchEvent.TouchUp:
			self.OnClickSpecButton()
		elif event == TouchEvent.TouchDown:
			pass
		elif event == TouchEvent.TouchMove:
			pass
		elif event == TouchEvent.TouchCancel:
			pass
	
	def OnTryGetBonus(self, args):
		ButtonPath = args["ButtonPath"].split("/")
		line = ButtonPath[-2].split("_")
		questIdx = int(line[-1])
		#
		event = args["TouchEvent"]
		if event == TouchEvent.TouchUp:
			self.OnClickGetBonus(questIdx)
		elif event == TouchEvent.TouchDown:
			pass
		elif event == TouchEvent.TouchMove:
			pass
		elif event == TouchEvent.TouchCancel:
			pass
	
	def OnClickReward(self, args):
		ButtonPath = args["ButtonPath"].split("/")
		line = ButtonPath[-3].split("_")
		questIdx = int(line[-1])
		line = ButtonPath[-1].split("_")
		itemIdx = int(line[-1])
		x, y = args['TouchPosX'], args['TouchPosY']
		#
		event = args["TouchEvent"]
		if event == TouchEvent.TouchUp:
			self.OnOpenPreview(questIdx, itemIdx, x, y)
		elif event == TouchEvent.TouchDown:
			pass
		elif event == TouchEvent.TouchMove:
			pass
		elif event == TouchEvent.TouchCancel:
			pass
	#---------------------------------------------------------------------------------------------------------------------------------
	def OnClickSpecButton(self):
		# print "OnClickSpecButton"
		self.ChangeScreenVisible(False)
		cbFunc = self.mSystem.GetGotoButtonCallback()
		if cbFunc and callable(cbFunc):
			cbFunc()

	def OnClickGetBonus(self, questIdx):
		# print "OnClickGetBonus", questIdx
		questData = self.mRecentQuestList[questIdx]
		eventData = {
			"playerId": self.mSystem.mPlayerId,
			"addupKey": self.mAddupKey,
			"bonuskey": questData["questKey"],
		}
		self.mSystem.NotifyToServer(ClientEvent.GetAddupBonus, eventData)
	
	def OnOpenPreview(self, questIdx, itemIdx, x, y):
		# print "OnOpenPreview", questIdx, itemIdx
		questData = self.mRecentQuestList[questIdx]
		singleReward = questData["reward"][itemIdx]
		itemDict = singleReward["item"]
		attrsSystem = clientApi.GetSystem("neteaseAttrs", "neteaseAttrsBeh")
		if not attrsSystem:
			return
		comp = clientApi.GetEngineCompFactory().CreateItem(clientApi.GetLevelId())
		pretty = comp.GetItemFormattedHoverText(itemDict['itemName'], itemDict['auxValue'], True, itemDict.get('userData')).split('\n')
		if '' in pretty:
			pretty = pretty[:pretty.index('')]
		name = pretty[0]
		part = pretty[1]
		enchantData = map(lambda s: '§7{}'.format(s), pretty[2:])
		detail = {
			'name': "{}x{}".format(name, itemDict["count"]),
		#	'pinzhi': ("", part),
		#	'fumo': enchantData,
		}
		attrsSystem.Detail(detail, x, y)
	#---------------------------------------------------------------------------------------------------------------------------------
	def OnTick(self):
		if self.mShowHintLeftSec <= 0:
			return
		self.mShowHintLeftSec -= 1
		if self.mShowHintLeftSec <= 0:
			self.HideGetBonusSuc()

	def ShowGetBonusSuc(self):
		self.SetVisible("/main_pnl/img_base_dialog/img_toast_receiveSucceed", True)
		self.mShowHintLeftSec = 3

	def HideGetBonusSuc(self):
		self.SetVisible("/main_pnl/img_base_dialog/img_toast_receiveSucceed", False)
		self.mShowHintLeftSec = 0

	def DrawGotoButton(self):
		text = self.mSystem.GetGotoButtonText()
		self.SetText("/main_pnl/img_base_dialog/btn_consume/button_label", text)

	def DrawAddupAll(self):
		if not self.mBShow:
			return
		player = self.mSystem.mMe
		addupInfo = player.GetAddupInfoByKey(self.mAddupKey)
		bonusList = addupInfo.get("bonusList", [])
		#
		title = self.mAddupConfig["title"]
		self.SetText("/main_pnl/img_base_dialog/lb_title", title)
		desc = self.mAddupConfig["desc"]
		self.SetText("/main_pnl/img_base_dialog/img_toast_upper/lb_desc", desc)
		startTp, endTp = self.mAddupConfig["startTp"], self.mAddupConfig["endTp"]
		startStr = time.strftime("%Y.%m.%d", time.localtime(startTp))
		endStr = time.strftime("%Y.%m.%d", time.localtime(endTp-1))
		dateStr = "有效期:%s~%s" % (startStr, endStr)
		self.SetText("/main_pnl/img_base_dialog/lb_indate", dateStr)
		process = addupInfo.get("process", 0)
		self.SetText("/main_pnl/img_base_dialog/lb_accumulation/img_tatolAccumulation/lb_200", "%d" % process)
		self.DrawGotoButton()
		#
		self.mRecentQuestList = []
		for questKey, questConf in self.mAddupConfig.get("quests", {}).iteritems():
			questConf["questKey"] = questKey
			self.mRecentQuestList.append(questConf)
		self.mRecentQuestList.sort(self.CmpQuest)
		length = len(self.mRecentQuestList)
		self.ResizeQuests(length)
		for idx in xrange(length):
			self.DrawSingleQuest(self.mRecentQuestList[idx], self.mQuestInstList[idx], process, bonusList)
	
	def CmpQuest(self, a, b):
		return cmp(a["showIdx"], b["showIdx"])

	def DrawSingleQuest(self, questData, inst, process, alreadyGetBonusList):
		rewardList = questData.get("reward", [])
		for i in xrange(5):
			if i >= len(rewardList):
				self.SetVisible("%s/item_%d" % (inst, i), False)
				continue
			qual = rewardList[i]["qual"]
			itemDict = rewardList[i]["item"]
			self.SetVisible("%s/item_%d" % (inst, i), True)
			image = Qual2ImageMap[qual]
			self.SetSprite("%s/item_%d/img_qual_%d" % (inst, i, i), image)
			if itemDict.get("enchantData", []):
				isEnchanted = True
			else:
				isEnchanted = False
			self.SetUiItem("%s/item_%d/item_renderer_%d" % (inst, i, i), itemDict["itemName"], itemDict["auxValue"], isEnchanted)
			self.SetVisible("%s/item_%d/img_gray_%d" % (inst, i, i), False)
			self.SetText("%s/item_%d/lb_count_%d" % (inst, i, i), "%d" % itemDict["count"])
		if questData["questKey"] in alreadyGetBonusList:
			self.SetVisible("%s/pnl_doing" % inst, False)
			self.SetVisible("%s/btn_get_bonus" % inst, False)
			self.SetVisible("%s/pnl_already_get" % inst, True)
		elif process >= questData["process"]:
			self.SetVisible("%s/pnl_doing" % inst, False)
			self.SetVisible("%s/btn_get_bonus" % inst, True)
			self.SetVisible("%s/pnl_already_get" % inst, False)
		else:
			self.SetVisible("%s/pnl_doing" % inst, True)
			self.SetText("%s/pnl_doing/lb_process" % inst, "%d/%d" % (process, questData["process"]))
			self.SetVisible("%s/btn_get_bonus" % inst, False)
			self.SetVisible("%s/pnl_already_get" % inst, False)

