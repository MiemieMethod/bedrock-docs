# -*- coding: utf-8 -*-

import math
import neteaseMenusScript.menusConst as menusConst
import client.extraClientApi as clientApi

ScreenNode = clientApi.GetScreenNodeCls()


class MenusScreen(ScreenNode):
	"""
	主菜单界面
	"""

	def __init__(self, namespace, name, param):
		ScreenNode.__init__(self, namespace, name, param)
		print '==== init MenusScreen ===='
		self.mImgBoard = '/main_pnl/btn_fold/img_mainMenu' # 主菜单的背景板
		self.mButtonFold = '/main_pnl/btn_fold' # 折叠按钮
		self.mButtonMenuBase = '/btn_menu_%d' # 菜单按钮，挂接在背景板下面
		self.mLabelMenuBase = '/lb_menu' # 菜单按钮文字，挂接在菜单按钮下面
		self.mButtonFoldUp = 'textures/ui/netease_menu/icon02@3x' # 折叠按钮向上图片
		self.mButtonFoldDown = 'textures/ui/netease_menu/icon03@3x' # 折叠按钮向下图片
		# 以下参数需要初始化的时候从UI中读取计算出来
		self.mLineSpacing = 0 # 行距
		self.mColumnSpacing = 0 # 列距
		self.mCellWidth = 0 # 单元宽度
		self.mCellHeight = 0 # 单元高度
		self.mSubHeight = 0 # 由于面板不包含最下面那层label，所以后面计算的时候需要把这部分减掉

		self.mFoldStatus = True # 折叠状态：True为折叠，False为放开
		self.mMenuRealNum = 0 # 显示出来的菜单数量
		self.mMaxColumnNum = 4 # 最大列数

		self.mMenuCallback = None # 设置按钮被点击时的回调

	def Create(self):
		print '==== MenusScreen Create ===='

		# 根据UI计算相关参数
		menuBaseButtonUIControl = self.GetBaseUIControl((self.mImgBoard + self.mButtonMenuBase) % 1).asButton()
		self.mCellWidth, imgHeight = menuBaseButtonUIControl.GetSize()
		self.mColumnSpacing, self.mLineSpacing = menuBaseButtonUIControl.GetPosition()
		menuLabelBaseUIControl = menuBaseButtonUIControl.GetChildByName(self.mLabelMenuBase)
		width, height = menuLabelBaseUIControl.GetSize()
		x, y = menuLabelBaseUIControl.GetPosition()
		self.mLineSpacing += y - imgHeight
		self.mCellHeight = y + height
		self.mSubHeight = self.mCellHeight - imgHeight
		print "cell width={}, cell height={}, line space={}, column space={}, sub height={}".format(self.mCellWidth, self.mCellHeight, self.mLineSpacing, self.mColumnSpacing, self.mSubHeight)
		# 初始化的时候先设置为不可见
		menuBaseButtonUIControl.SetVisible(False)
		menuBaseButtonUIControl.AddTouchEventParams({"isSwallow": True})
		menuBaseButtonUIControl.SetButtonTouchUpCallback(self.OnMenuTouchCallback)

		# 设置收起按钮回调
		foldButtonUIControl = self.GetBaseUIControl(self.mButtonFold).asButton()
		foldButtonUIControl.AddTouchEventParams({"isSwallow": True})
		foldButtonUIControl.SetButtonTouchUpCallback(self.OnFoldButtonTouch)

		# 设置为折叠状态
		self.SetFold(True)

	# 折叠按钮的回调处理
	def OnFoldButtonTouch(self, args):
		print 'OnFoldButtonTouch: {}'.format(args)
		self.SetFold(not self.mFoldStatus)

	# 设置折叠状态
	def SetFold(self, isFold):
		self.mFoldStatus = isFold
		# 设置按钮贴图
		foldButtonUIControl = self.GetBaseUIControl(self.mButtonFold).asButton()
		foldButtonDefaultUIControl = foldButtonUIControl.GetChildByName('default').asImage()
		foldButtonHoverUIControl = foldButtonUIControl.GetChildByName('hover').asImage()
		foldButtonPressedUIControl = foldButtonUIControl.GetChildByName('pressed').asImage()
		if self.mFoldStatus:
			foldButtonDefaultUIControl.SetSprite(self.mButtonFoldDown)
			foldButtonHoverUIControl.SetSprite(self.mButtonFoldDown)
			foldButtonPressedUIControl.SetSprite(self.mButtonFoldUp)
		else:
			foldButtonDefaultUIControl.SetSprite(self.mButtonFoldUp)
			foldButtonHoverUIControl.SetSprite(self.mButtonFoldUp)
			foldButtonPressedUIControl.SetSprite(self.mButtonFoldDown)

		# 调整背景板大小
		boardImageUIControl = self.GetBaseUIControl(self.mImgBoard).asImage()
		width = min(self.mMaxColumnNum, self.mMenuRealNum) * (self.mCellWidth + self.mColumnSpacing) + self.mColumnSpacing
		row = 1 if self.mFoldStatus else math.ceil(float(self.mMenuRealNum) / self.mMaxColumnNum)
		height = row * (self.mCellHeight + self.mLineSpacing) - self.mLineSpacing
		if row == 1:
			height -= self.mSubHeight
		boardImageUIControl.SetSize((width, height))
		boardImageUIControl.SetPosition((-width, 0))
		x, y = boardImageUIControl.GetPosition()
		# 调整菜单按钮
		for i in xrange(self.mMaxColumnNum+1, self.mMenuRealNum+1):
			menuButtonUIControl = boardImageUIControl.GetChildByName(self.mButtonMenuBase % i)
			if not menuButtonUIControl:
				continue
			menuButtonUIControl.SetVisible(not self.mFoldStatus)

	# 根据传入配置更新主菜单
	def Refresh(self, configData):
		# 最大行列数
		self.mMaxColumnNum = configData['maxColumnNum']
		# 菜单
		boardImageUIControl = self.GetBaseUIControl(self.mImgBoard).asImage()
		count = 1
		for menuData in configData['menusConfig']:
			menuButtonUIControl = boardImageUIControl.GetChildByName(self.mButtonMenuBase % count)
			if not menuButtonUIControl:
				# 该按钮没有创建，则创建
				if not self.Clone((self.mImgBoard + self.mButtonMenuBase) % 1, self.mImgBoard, (self.mButtonMenuBase % count)[1:]):
					logger.error("menusClientUI Refresh: clone {} failed".format(self.mButtonMenuBase % count))
					return False
				menuButtonUIControl = boardImageUIControl.GetChildByName(self.mButtonMenuBase % count).asButton()
				menuButtonUIControl.AddTouchEventParams({"isSwallow": True})
			else:
				menuButtonUIControl = menuButtonUIControl.asButton()
			# 根据配置重置该按钮
			menuLabelUIControl = menuButtonUIControl.GetChildByName(self.mLabelMenuBase).asLabel()
			menuButtonDefaultUIControl = menuButtonUIControl.GetChildByName('default').asImage()
			menuButtonHoverUIControl = menuButtonUIControl.GetChildByName('hover').asImage()
			menuButtonPressedUIControl = menuButtonUIControl.GetChildByName('pressed').asImage()
			if menuData['enabled']:
				# 开启状态
				menuLabelUIControl.SetText(menuData['normal_text'])
				menuButtonDefaultUIControl.SetSprite(menuData['normal_icon'])
				menuButtonHoverUIControl.SetSprite(menuData['normal_hover'])
				menuButtonPressedUIControl.SetSprite(menuData['normal_pressed'])
			else:
				# 禁用状态
				menuLabelUIControl.SetText(menuData['disabled_text'])
				menuButtonDefaultUIControl.SetSprite(menuData['disabled_icon'])
				menuButtonHoverUIControl.SetSprite(menuData['disabled_hover'])
				menuButtonPressedUIControl.SetSprite(menuData['disabled_pressed'])

			menuButtonUIControl.SetVisible(True)
			# 计算坐标
			x = ((count-1) % self.mMaxColumnNum) * (self.mCellWidth + self.mColumnSpacing) + self.mColumnSpacing
			y = ((count-1) / self.mMaxColumnNum) * (self.mCellHeight + self.mLineSpacing)
			menuButtonUIControl.SetPosition((x, y))
			count += 1
		self.mMenuRealNum = count - 1
		# 继续往后遍历，将多余的菜单节点隐藏
		while True:
			menuButtonUIControl = boardImageUIControl.GetChildByName(self.mButtonMenuBase % count)
			if not menuButtonUIControl:
				break
			menuButtonUIControl.SetVisible(False)
			count += 1
		# 重刷是否展开/折叠
		self.SetFold(self.mFoldStatus)
		return True

	# 菜单按钮被点击时的回调
	def OnMenuTouchCallback(self, args):
		# 只能通过控件路径名来区分
		tmps = args['ButtonPath'].split('_')
		index = int(tmps[len(tmps)-1]) - 1
		# 计算出是第几个按钮返回
		if self.mMenuCallback:
			self.mMenuCallback(index)

	# 设置菜单点击回调
	def SetMenuCallback(self, callback):
		self.mMenuCallback = callback
