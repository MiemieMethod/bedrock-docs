# -*- coding: utf-8 -*-

import neteaseLabelScript.labelConst as labelConst
import client.extraClientApi as clientApi

ViewBinder = clientApi.GetViewBinderCls()
ScreenNode = clientApi.GetScreenNodeCls()
import neteaseLabelScript.apiUtil as apiUtil

class LabelMainScreen(ScreenNode):
	def __init__(self, namespace, name, param):
		ScreenNode.__init__(self, namespace, name, param)
		print '==== %s ====' % 'init LabelMainScreen'
		self.mBars = []

		self.mLockIcon = '{}/img_lock01'
		self.mName = '{}/lb_name_label'
		self.mUnlockInfoBtn = '{}/btn_unlock01'
		self.mText = '{}/lb_text_label'
		self.mPic = '{}/img_pic'
		self.mDesc = '{}/lb_description_label'
		self.mInUse = '{}/btn_radio'
		self.mOverview = '/label_pnl/img_base/img_title/lb_tiltle'

		self.mCfg = None
		self.mCache = None

	# Create函数是继承自ScreenNode，会在UI创建完成后被调用
	def Create(self):
		print '==== %s ====' % 'LabelMainScreen Create'
		self.AddTouchEventHandler("/label_pnl/img_base/img_title/btn_close", self.OnClose)
		mouse = '/label_pnl/img_base/scroll_main/scroll_mouse/scroll_view/stack_panel/background_and_viewport/scrolling_view_port/scrolling_content'
		touch = '/label_pnl/img_base/scroll_main/scroll_touch/scroll_view/panel/background_and_viewport/scrolling_view_port/scrolling_content'
		self.mLabelView = touch
		self.mLabelViewSize = self.GetSize(self.mLabelView)
		if not self.mLabelViewSize:
			self.mLabelView = mouse
			self.mLabelViewSize = self.GetSize(self.mLabelView)
		self.mBar = self.mLabelView + '/bar0'
		self.mBars.append(self.mBar)
		self.mBarPos = self.GetPosition(self.mBar)
		self.mBarOffset = self.GetSize(self.mBar)[1] + 1
		self.AddTouchEventHandler(self.mUnlockInfoBtn.format(self.mBar), self.OnShowUnlockInfo)
		self.AddTouchEventHandler(self.mInUse.format(self.mBar), self.OnSelect)

	def InitScreen(self):
		self.SetVisible("", False)

	@apiUtil.touch_filter("up")
	def OnShowUnlockInfo(self, args):
		cfg = self.mCfg[int(args["ButtonPath"][::-1].split('/', 2)[1][:-3][::-1])][1]
		popUpUINode = apiUtil.GetPopUpUI()
		popUpUINode.Show(cfg['name'], cfg['lock'])

	@apiUtil.touch_filter("up")
	def OnSelect(self, args):
		order = int(args["ButtonPath"][::-1].split('/', 2)[1][:-3][::-1])
		label_id = self.mCfg[order][0]
		in_use = self.mCache[label_id]['inUse']
		self.mCache[label_id]['inUse'] = not in_use
		clientApi.GetSystem(labelConst.ModName, labelConst.ClientSystemName).NotifyToServer(
			in_use and labelConst.PlayerTakeOffLabelEvent or labelConst.PlayerPutOnLabelEvent,
			{
				'playerId': clientApi.GetLocalPlayerId(),
				'labelId': label_id
			}
		)
		self.SetVisible(args['ButtonPath'] + '/img_radio_selected', not in_use)
		if not in_use:
			for i, item in enumerate(self.mCfg):
				if i == order:
					continue
				if item[1]['part'] == self.mCache[label_id]['part']:
					if item[0] in self.mCache:
						self.mCache[item[0]]['inUse'] = False
					self.SetVisible(self.mInUse.format(self.mBars[i]) + '/img_radio_selected', False)

	@apiUtil.touch_filter("up")
	def OnClose(self, *args):
		self.SetVisible("", False)
		clientApi.SetInputMode(0)
		clientApi.HideSlotBarGui(False)

	def Open(self, data):
		cfg = sorted(data['cfg'].items(), key=lambda item: item[1]['order'])
		self.mCache = data['info']
		if self.mCfg != cfg:
			self.mCfg = cfg
			demand = len(cfg)
			cur = len(self.mBars)
			if demand > cur:
				for i in xrange(cur, demand):
					s = 'bar{}'.format(i)
					self.Clone(self.mBars[0], self.mLabelView, s)
					s = self.mLabelView + '/{}'.format(s)
					self.SetPosition(s, (self.mBarPos[0], self.mBarPos[1] + self.mBarOffset * i))
					self.mBars.append(s)
					self.AddTouchEventHandler(self.mUnlockInfoBtn.format(s), self.OnShowUnlockInfo)
					self.AddTouchEventHandler(self.mInUse.format(s), self.OnSelect)
			self.SetSize(self.mLabelView, (self.mLabelViewSize[0], self.mBarOffset * demand + 10))
		demand = len(self.mCfg)
		for i, s in enumerate(self.mBars):
			if i < demand:
				cfg = self.mCfg[i][1]
				self.SetText(self.mName.format(s), cfg['name'])
				self.SetText(self.mDesc.format(s), cfg['desc'])
				if cfg['part'] and cfg['res']:
					self.SetVisible(self.mText.format(s), False)
					self.SetSprite(self.mPic.format(s), cfg['res'])
					self.SetVisible(self.mPic.format(s), True)
				else:
					self.SetVisible(self.mText.format(s), True)
					self.SetText(self.mPic.format(s), cfg['text'])
					self.SetVisible(self.mPic.format(s), False)

				self.SetVisible(self.mLockIcon.format(s), self.mCfg[i][0] not in self.mCache)
				self.SetVisible(self.mUnlockInfoBtn.format(s), self.mCfg[i][0] not in self.mCache)
				lableId = self.mCfg[i][0]
				self.SetVisible(self.mInUse.format(s), lableId in self.mCache)
				if lableId in self.mCache and self.mCache[lableId]['inUse']:
					self.SetVisible(self.mInUse.format(s) + '/img_radio_selected', True)
				else:
					self.SetVisible(self.mInUse.format(s) + '/img_radio_selected', False)
			self.SetVisible(s, i < demand)
		self.SetText(self.mOverview, "称号（已获得 {} / {}）".format(len(self.mCache), demand))
		self.SetVisible("", True)
		clientApi.SetInputMode(1)
		clientApi.HideSlotBarGui(True)
