# -*- coding: utf-8 -*-
import client.extraClientApi as extraClientApi
ViewBinder = extraClientApi.GetViewBinderCls()
ViewRequest = extraClientApi.GetViewViewRequestCls()
ScreenNode = extraClientApi.GetScreenNodeCls()
TouchEvent = extraClientApi.GetMinecraftEnum().TouchEvent
import weakref
import neteaseRankScript.rankConsts as  rankConsts

class RankUIScreen(ScreenNode):
	def __init__(self, namespace, name, param):
		ScreenNode.__init__(self, namespace, name, param)
		self.mClientSystem = None
		
		self.mIsShow = False
		self.mCurrentPage = 1 #当前的页面
		self.mMaxPage = 1 #最大的页面
		self.tempRankData = []
		
		self.mRankPanel = "/rankPanel"
		self.mRankImage = self.mRankPanel + "/rankImage"
		self.mCloseBtn = self.mRankImage + "/closeButton"
		self.mRankBack = self.mRankImage + "/rankBack"
		self.mRankLabel = self.mRankBack + "/ranklabel"
		self.mMessageLabelList = ["{0}/messagelabel{1}".format(self.mRankBack, i) for i in range(1, 7)]#排行的数据信息名
		self.mRankNumImgList = ["{0}/rankNum{1}".format(self.mRankBack, i) for i in range(1, 11)] #10行的背景图
		self.mRankTagList = ["{0}/rankNum{1}/ranktag{2}".format(self.mRankBack, i, i) for i in range(1, 4)]#123名的图标
		self.mRankTextList = ["{0}/rankNum{1}/rankText{2}".format(self.mRankBack, i, i) for i in range(1, 11)] #排名的文字
		self.mRankMessage1List = ["{0}/rankNum{1}/rank{2}Message1".format(self.mRankBack, i, i) for i in range(1, 11)] #数据1的信息
		self.mRankMessage2List = ["{0}/rankNum{1}/rank{2}Message2".format(self.mRankBack, i, i) for i in range(1, 11)] #数据2的信息
		self.mRankMessage3List = ["{0}/rankNum{1}/rank{2}Message3".format(self.mRankBack, i, i) for i in range(1, 11)] #数据3的信息
		self.mRankMessage4List = ["{0}/rankNum{1}/rank{2}Message4".format(self.mRankBack, i, i) for i in range(1, 11)] #数据4的信息
		self.mRankMessage5List = ["{0}/rankNum{1}/rank{2}Message5".format(self.mRankBack, i, i) for i in range(1, 11)] #数据5的信息
		self.mRankMessage6List = ["{0}/rankNum{1}/rank{2}Message6".format(self.mRankBack, i, i) for i in range(1, 11)] #数据6的信息
		self.mAllRankMessageList = [
			self.mRankMessage1List, self.mRankMessage2List,
			self.mRankMessage3List, self.mRankMessage4List,
			self.mRankMessage5List, self.mRankMessage6List
		]
		self.mNextBtn = self.mRankImage + "/nextBtn"#下一页
		self.mBeforeBtn = self.mRankImage + "/beforeBtn"#上一页
		self.mRemarksText = self.mRankImage + "/remarksText"#备注信息
		self.mRankName = self.mRankImage + "/rankTitleText"#备注信息
		self.mPageNumText = self.mRankImage + "/pageNum"#翻页
	
	def Create(self):
		pass
		
	def InitSystem(self, system):
		self.mClientSystem = weakref.proxy(system)
		self.AddTouchEventHandler(self.mCloseBtn, self.OnButtonClose)
		self.AddTouchEventHandler(self.mBeforeBtn, self.OnButtonBefore)
		self.AddTouchEventHandler(self.mNextBtn, self.OnButtonNext)
		
	def OnButtonNext(self, args):
		event = args["TouchEvent"]
		if event == TouchEvent.TouchUp:
			if self.mCurrentPage < self.mMaxPage:
				self.mCurrentPage += 1
			self.ShowRankPage()
		elif event == TouchEvent.TouchDown:
			pass
		elif event == TouchEvent.TouchMove:
			pass
		elif event == TouchEvent.TouchCancel:
			pass
	
	def OnButtonBefore(self, args):
		event = args["TouchEvent"]
		if event == TouchEvent.TouchUp:
			if self.mCurrentPage > 1:
				self.mCurrentPage -= 1
			self.ShowRankPage()
		elif event == TouchEvent.TouchDown:
			pass
		elif event == TouchEvent.TouchMove:
			pass
		elif event == TouchEvent.TouchCancel:
			pass
		
	def InitScreen(self):
		self.ChangeScreenVisible(False)
		
	def ChangeScreenVisible(self, flag):
		self.SetVisible("", flag)
		self.mIsShow = flag
		if flag:
			extraClientApi.SetInputMode(1)
		else:
			extraClientApi.SetInputMode(0)
		
		
	def ShowScreen(self, flag):
		self.ChangeScreenVisible(flag)
		
		
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
		
	def ShowRankPanel(self):
		self.ShowScreen(True)
		self.tempRankData = self.mClientSystem.GetRankDataManager().GetRankData()
		self.tempRankCol = self.mClientSystem.GetRankDataManager().GetRankColList()
		self.tempRankTiletleList = self.mClientSystem.GetRankDataManager().GetRankColTitleList()
		self.remarksContent = self.mClientSystem.GetRankDataManager().GetRemarksContent()
		self.rankName = self.mClientSystem.GetRankDataManager().GetRankName()
		print "remarksContent", self.remarksContent
		self.SetText(self.mRemarksText, self.remarksContent)
		self.SetText(self.mRankName, self.rankName)
		for colIndex, colName in enumerate(self.tempRankTiletleList):
			self.SetText(self.mMessageLabelList[colIndex], colName)
		unShonMessageLabelStartIndex = len(self.tempRankCol)
		if unShonMessageLabelStartIndex < len(self.mMessageLabelList):
			for unShowMessageLabelIndex in range(unShonMessageLabelStartIndex, len(self.mMessageLabelList)):
				self.SetVisible(self.mMessageLabelList[unShowMessageLabelIndex], False)
				self.SetRankMessageListVisible(unShowMessageLabelIndex, False)
		else:
			for showMessageLabelIndex in range(0, 6):
				self.SetVisible(self.mMessageLabelList[showMessageLabelIndex], True)
				self.SetRankMessageListVisible(showMessageLabelIndex, True)
		
		self.mMaxPage = len(self.tempRankData) / 10 + 1
		if len(self.tempRankData) % 10 == 0:
			self.mMaxPage = self.mMaxPage - 1 if (self.mMaxPage - 1) > 0 else 1
		if self.mCurrentPage > self.mMaxPage:
			self.mCurrentPage = 1
		
		self.ShowRankPage()
			
	def SetRankTagListVisible(self, flag):
		for rankTag in self.mRankTagList:
			self.SetVisible(rankTag, flag)
			
	def SetRankMessageListVisible(self, index, flag):
		for messageList in self.mAllRankMessageList[index]:
			self.SetVisible(messageList, flag)
	
			
	def ShowRankPage(self):
		self.SetText(self.mPageNumText, str(self.mCurrentPage) + "/" + str(self.mMaxPage))
		self.SetRankTagListVisible(self.mCurrentPage == 1)#不是第一页，取消显示123名的图标
		unShowRankNumStartIndex = 10 - (self.mCurrentPage * 10 - len(self.tempRankData))
		unShowRankNumEndIndex = 9
		#数据不够，不显示全
		if unShowRankNumStartIndex <= unShowRankNumEndIndex:
			for index in range(0, 10):
				if index < unShowRankNumStartIndex:
					self.SetVisible(self.mRankNumImgList[index], True)
				else:
					self.SetVisible(self.mRankNumImgList[index], False)
		else:
			for index in range(0, 10):
				self.SetVisible(self.mRankNumImgList[index], True)
				
		startShowRankIndex = (self.mCurrentPage - 1) * 10
		endShowRankIndex = min(self.mCurrentPage * 10 - 1, len(self.tempRankData) - 1)
		print "self.tempRankData", len(self.tempRankData), endShowRankIndex
		for colIndex, colName in enumerate(self.tempRankCol):
			for showRankIndex in range(startShowRankIndex, endShowRankIndex + 1):
				oneRankData = self.tempRankData[showRankIndex]
				showMessageIndex = showRankIndex % 10
				oneColData = oneRankData.get(colName)
				dataType = rankConsts.typeof(oneColData)
				self.SetText(self.mAllRankMessageList[colIndex][showMessageIndex], oneColData if dataType == "str" else str(oneColData))
				self.SetText(self.mRankTextList[showMessageIndex], str(showRankIndex + 1))
			
			
		
		
		
		
		
		
		
	

