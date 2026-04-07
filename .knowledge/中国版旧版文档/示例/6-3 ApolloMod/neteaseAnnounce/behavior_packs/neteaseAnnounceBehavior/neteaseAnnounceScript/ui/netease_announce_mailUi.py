# -*- coding: utf-8 -*-
import time
import client.extraClientApi as extraClientApi
ViewBinder = extraClientApi.GetViewBinderCls()
ViewRequest = extraClientApi.GetViewViewRequestCls()
ScreenNode = extraClientApi.GetScreenNodeCls()
TouchEvent = extraClientApi.GetMinecraftEnum().TouchEvent
import neteaseAnnounceScript.apiUtil as apiUtil
from neteaseAnnounceScript.ui.uiDef import UIDef


class MailScreen(ScreenNode):
	def __init__(self, namespace, name, param):
		ScreenNode.__init__(self, namespace, name, param)
		self.mUiKey = UIDef.UIMail
		self.mFrame = 0
		self.mRecentSize = 0
		self.mSelectMailId = None
		self.mOldSelectMailButtons = []

	def ChangeScreenVisible(self, flag):
		self.mBShow = flag
		if flag:
			apiUtil.GetUiMgr().RegisterUIOpen(self.mUiKey)
		else:
			apiUtil.GetUiMgr().RegisterUIClose(self.mUiKey)
		self.SetVisible("", flag)

	# Create函数是继承自ScreenNode，会在UI创建完成后被调用
	def Create(self):
		scrollBase = "/mail_pnl/mail_bg/boardbg/separator/mail_scroll_base"
		scrollBaseTouch = scrollBase + "/scroll_touch/scroll_view/panel/background_and_viewport/scrolling_view_port/scrolling_content"
		size = self.GetSize(scrollBaseTouch)
		if size:
			self.mMailBtnParent = scrollBaseTouch
			self.mMailBtnParentSize = size
		else:
			scrollBaseMouse = scrollBase + "/scroll_mouse/scroll_view/stack_panel/background_and_viewport/scrolling_view_port/scrolling_content"
			size = self.GetSize(scrollBaseMouse)
			self.mMailBtnParent = scrollBaseMouse
			self.mMailBtnParentSize = size
		# print "Create", self.mMailBtnParentSize, self.mMailBtnParent
		self.mMailBtnBase = self.mMailBtnParent + "/btn_mail"
		self.mMailBtnBaseSize = self.GetSize(self.mMailBtnBase)
		self.mMailBtnBasePos = self.GetPosition(self.mMailBtnBase)
		self.mMailBtnOffset = 5
		# print "MailBtnBase", self.mMailBtnBaseSize, self.mMailBtnBasePos
		self.SetVisible(self.mMailBtnBase, False)
		self.mMailBtnList = []
		self.Resize(4)
		self.mMailItemBase = "/mail_pnl/mail_bg/mail_annex_bg"
		size = self.GetSize(self.mMailItemBase)
		pos = self.GetPosition(self.mMailItemBase)
		self.SetVisible(self.mMailItemBase, False)
		self.mMailItemList =[]
		for idx in xrange(10):
			name = "item_%d"%idx
			self.Clone(self.mMailItemBase, "/mail_pnl/mail_bg", name)
			name = "%s/%s" % ("/mail_pnl/mail_bg", name)
			self.SetPosition(name, (pos[0]+idx*(size[0]+0), pos[1]))
			self.mMailItemList.append(name)
		#
		self.AddTouchEventHandler("/mail_pnl/mail_bg/headbar/btn_continue", self.OnClose)
		self.AddTouchEventHandler("/mail_pnl/mail_bg/mail_title_bg/mail_del_btn", self.OnDel)
		self.AddTouchEventHandler("/mail_pnl/mail_bg/mail_annex_get", self.OnGetBonus)
		#
		scrollBase = "/mail_pnl/mail_bg/scroll_content"
		scrollBaseTouch = scrollBase + "/scroll_touch/scroll_view/panel/background_and_viewport/scrolling_view_port/scrolling_content"
		scrollBaseControl = self.GetBaseUIControl(scrollBaseTouch)
		if scrollBaseControl:
			self.mScrollContent = "%s/lb_content" % scrollBaseTouch
		else:
			scrollBaseMouse = scrollBase + "/scroll_mouse/scroll_view/stack_panel/background_and_viewport/scrolling_view_port/scrolling_content"
			self.mScrollContent = "%s/lb_content" % scrollBaseMouse

	def Resize(self, size):
		if size == self.mRecentSize:
			return
		self.mRecentSize = size
		if size == 0:
			self.SetVisible("/mail_pnl/mail_bg/boardbg/separator/mail_hint_label", True)
		else:
			self.SetVisible("/mail_pnl/mail_bg/boardbg/separator/mail_hint_label", False)
		lackNum = size - len(self.mMailBtnList)
		# 控件不够用，创建一些
		if lackNum > 0:
			beginIndex = len(self.mMailBtnList)
			for idx in xrange(lackNum):
				self.CloneSingleMailButton(beginIndex+idx)
		# 隐藏多余不用的控件
		for idx, btn in enumerate(self.mMailBtnList):
			if idx < size:
				self.SetVisible(btn, True)
			else:
				self.SetVisible(btn, False)
		# 重设滚动区域的大小
		height = self.mMailBtnBasePos[1] + size * (self.mMailBtnBaseSize[1] + self.mMailBtnOffset)
		height = max(height, self.mMailBtnParentSize[1])
		# print "Resize", self.mMailBtnParentSize, height
		self.SetSize(self.mMailBtnParent, (self.mMailBtnParentSize[0], height))

	def CloneSingleMailButton(self, idx):
		name = "mail_btn_%d" % idx
		self.Clone(self.mMailBtnBase, self.mMailBtnParent, name)
		name = "%s/%s" % (self.mMailBtnParent, name)
		self.mMailBtnList.append(name)
		height = self.mMailBtnBasePos[1] + idx * (self.mMailBtnBaseSize[1] + self.mMailBtnOffset)
		self.SetPosition(name, (self.mMailBtnBasePos[0], height))
		self.AddTouchEventHandler(name, self.OnMailBtnEvent)

	def InitScreen(self):
		self.ChangeScreenVisible(False)

	def Destroy(self):
		pass

	# 继承自ScreenNode的方法，会被引擎自动调用，1秒钟30帧
	def Update(self):
		self.mFrame += 1
		if self.mBShow and self.mFrame % 30 == 0:
			self.DoRefreshMailExpirt()
			changed = apiUtil.GetMailMgr().InspectExpiredMails()
			if changed:
				self.DoDrawAll()
	#---------------------------------------------------------------------------------
	def Show(self):
		self.ChangeScreenVisible(True)
		self.DoDrawAll()

	def DoDrawAll(self):
		if not self.mBShow:
			return
		count, idList, mailDict = apiUtil.GetMailMgr().GetMailOverview()
		self.DrawMailButtons(count, idList, mailDict)
		mail = self.GetSelectMail()
		self.DrawMailContent(mail)

	def DrawMailButtons(self, count, idList, mailDict):
		size = max(count, len(idList))
		self.Resize(size)
		for idx in xrange(size):
			name = self.mMailBtnList[idx]
			txt = "正在获取中..."
			if idx < len(idList):
				mail = mailDict.get(idList[idx], None)
				if mail:
					txt = mail["title"]
			self.SetText("%s/lb_title_mail"%name, txt)

	def DrawMailButtonSelect(self, mailId):
		for idx in self.mOldSelectMailButtons:
			name = self.mMailBtnList[idx]
			self.SetButtonImage(name, "textures/ui/netease_announce/btn01@3x")
		self.mOldSelectMailButtons = []
		for idx in xrange(self.mRecentSize):
			mail = apiUtil.GetMailMgr().GetMailByIndex(idx)
			if mail and mail["_id"] == mailId:
				name = self.mMailBtnList[idx]
				self.SetButtonImage(name, "textures/ui/netease_announce/btn01_select@3x")
				self.mOldSelectMailButtons.append(idx)

	def SetButtonImage(self, componentPath, pic):
		self.SetSprite('%s/default' % (componentPath), pic)
		self.SetSprite('%s/hover' % (componentPath), pic)
		self.SetSprite('%s/pressed' % (componentPath), pic)

	def DoRefreshMailContent(self):
		if not self.mBShow:
			return
		mail = self.GetSelectMail()
		self.DrawMailContent(mail)

	def DoRefreshMailExpirt(self):
		mail = self.GetSelectMail()
		if not mail:
			return
		now = int(time.time())
		expire = apiUtil.GetLeftTimeString(mail["expire"] - now)
		self.SetText("/mail_pnl/mail_bg/mail_timeleft", expire)
		# print "DoRefreshMailExpirt", expire

	def DrawMailContent(self, mail):
		if mail:
			title, content, itemList, getBonus = mail["title"], mail["content"], mail["itemList"], mail["getBonus"]
			now = int(time.time())
			expire = apiUtil.GetLeftTimeString(mail["expire"] - now)
			self.DrawMailButtonSelect(mail["_id"])
		else:
			title, content, itemList, getBonus = "", "", [], 1
			expire = ""
			self.DrawMailButtonSelect(None)
		self.SetText("/mail_pnl/mail_bg/mail_title_bg/mail_title", title)
		self.SetText("/mail_pnl/mail_bg/mail_timeleft", expire)
		self.SetText(self.mScrollContent, content)
		for idx in xrange(10):
			self.SetVisible(self.mMailItemList[idx], False)
			if idx >= len(itemList):
				continue
			item = apiUtil.SpiltSingleItem(itemList[idx])
			if not item:
				print "user defined item [%s]" % str(itemList[idx])
				continue
			self.SetVisible(self.mMailItemList[idx], True)
			self.SetUiItem("%s/mail_annex_pic"%self.mMailItemList[idx], item["itemName"], item["auxValue"])
			self.SetText("%s/mail_annex_num"%self.mMailItemList[idx], "%d"%item["count"])
		if itemList:	# 有奖励
			self.SetVisible("/mail_pnl/mail_bg/mail_annex_get", True)
			if getBonus:	# 奖励已经领取
				self.SetVisible("/mail_pnl/mail_bg/mail_title_bg/mail_del_btn", True)
				self.SetText("/mail_pnl/mail_bg/mail_annex_get/button_label", "已领取")
				self.SetTouchEnable("/mail_pnl/mail_bg/mail_annex_get", False)
			elif apiUtil.ForbidGetBonus():
				self.SetVisible("/mail_pnl/mail_bg/mail_title_bg/mail_del_btn", True)
				self.SetText("/mail_pnl/mail_bg/mail_annex_get/button_label", "当前无法领取")
				self.SetTouchEnable("/mail_pnl/mail_bg/mail_annex_get", False)
			else:
				self.SetVisible("/mail_pnl/mail_bg/mail_title_bg/mail_del_btn", False)
				self.SetText("/mail_pnl/mail_bg/mail_annex_get/button_label", "领取奖励")
				self.SetTouchEnable("/mail_pnl/mail_bg/mail_annex_get", True)
		else:    # 没有奖励
			self.SetVisible("/mail_pnl/mail_bg/mail_annex_get", False)
			self.SetVisible("/mail_pnl/mail_bg/mail_title_bg/mail_del_btn", True)
	#---------------------------------------------------------------------------------
	def GetSelectMail(self):
		if self.mSelectMailId is None:
			return None
		return apiUtil.GetMailMgr().GetMail(self.mSelectMailId)

	def OnMailBtnEvent(self, args):
		line = args["ButtonPath"].split("_")
		idx = int(line[-1])
		event = args["TouchEvent"]
		if event == TouchEvent.TouchUp:
			extraClientApi.SetResponse(True)
			self.DoChangeSelectMail(idx)
		elif event == TouchEvent.TouchDown:
			extraClientApi.SetResponse(False)
		elif event == TouchEvent.TouchMove:
			pass
		elif event == TouchEvent.TouchCancel:
			extraClientApi.SetResponse(True)

	def DoChangeSelectMail(self, idx):
		mail = apiUtil.GetMailMgr().GetMailByIndex(idx)
		if mail:
			self.mSelectMailId = mail["_id"]
			self.DrawMailContent(mail)
			if not mail["hasRead"]:
				apiUtil.GetMailMgr().SendSetRead(mail["_id"])
		else:
			self.mSelectMailId = None
			self.DrawMailContent(None)

	def OnClose(self, args):
		event = args["TouchEvent"]
		if event == TouchEvent.TouchUp:
			extraClientApi.SetResponse(True)
			self.ChangeScreenVisible(False)
			apiUtil.GetMailButtonUI().OnMailMainClose()
		elif event == TouchEvent.TouchDown:
			extraClientApi.SetResponse(False)
		elif event == TouchEvent.TouchMove:
			pass
		elif event == TouchEvent.TouchCancel:
			extraClientApi.SetResponse(True)

	def OnDel(self, args):
		event = args["TouchEvent"]
		if event == TouchEvent.TouchUp:
			extraClientApi.SetResponse(True)
			if not self.mSelectMailId:
				return
			apiUtil.GetMailMgr().SendDelFix(self.mSelectMailId)
		elif event == TouchEvent.TouchDown:
			extraClientApi.SetResponse(False)
		elif event == TouchEvent.TouchMove:
			pass
		elif event == TouchEvent.TouchCancel:
			extraClientApi.SetResponse(True)

	def OnGetBonus(self, args):
		event = args["TouchEvent"]
		if event == TouchEvent.TouchUp:
			extraClientApi.SetResponse(True)
			if not self.mSelectMailId:
				return
			apiUtil.GetMailMgr().SendGetBonus(self.mSelectMailId)
		elif event == TouchEvent.TouchDown:
			extraClientApi.SetResponse(False)
		elif event == TouchEvent.TouchMove:
			pass
		elif event == TouchEvent.TouchCancel:
			extraClientApi.SetResponse(True)

