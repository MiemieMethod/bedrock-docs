# -*- coding: utf-8 -*-

from collections import OrderedDict, Counter
import neteaseLabelScript.labelConst as labelConst
import client.extraClientApi as clientApi
import neteaseLabelScript.apiUtil as apiUtil
ClientSystem = clientApi.GetClientSystemCls()


class LabelClientSystem(ClientSystem):
	def __init__(self, namespace, systemName):
		ClientSystem.__init__(self, namespace, systemName)
		self.mLabelInfoCache = None
		self.mPlayerId = clientApi.GetLocalPlayerId()
		self.mLabelUINode = None
		self.mPopUpUINode = None
		self.mLabelHeadUINodes = OrderedDict()
		apiUtil.SetSystem(self)

		self.ListenForEvent(clientApi.GetEngineNamespace(), clientApi.GetEngineSystemName(), labelConst.UiInitFinishedEvent, self, self.OnUiInitFinished)
		self.ListenForEvent(clientApi.GetEngineNamespace(), clientApi.GetEngineSystemName(), 'AddPlayerEvent', self, self.OnPlayerAppear)
		self.ListenForEvent(labelConst.ModName, labelConst.ServerSystemName, labelConst.DisplayLabelBoardEvent, self, self.OnDisplayLabelBoard)
		self.ListenForEvent(labelConst.ModName, labelConst.ServerSystemName, 'HighlightEvent', self, self.OnHighlight)
		self.ListenForEvent(labelConst.ModName, labelConst.ServerSystemName, 'CacheEvent', self, self.OnCache)

	def Destroy(self):
		apiUtil.Destroy()
		self.UnListenForEvent(clientApi.GetEngineNamespace(), clientApi.GetEngineSystemName(), labelConst.UiInitFinishedEvent, self, self.OnUiInitFinished)
		self.UnListenForEvent(clientApi.GetEngineNamespace(), clientApi.GetEngineSystemName(), 'AddPlayerEvent', self, self.OnPlayerAppear)
		self.UnListenForEvent(labelConst.ModName, labelConst.ServerSystemName, labelConst.DisplayLabelBoardEvent, self, self.OnDisplayLabelBoard)
		self.UnListenForEvent(labelConst.ModName, labelConst.ServerSystemName, 'HighlightEvent', self, self.OnHighlight)
		self.UnListenForEvent(labelConst.ModName, labelConst.ServerSystemName, 'CacheEvent', self, self.OnCache)

	def OnPlayerAppear(self, data):
		self.NotifyToServer('ResumeDisplayEvent', {'playerId': data['id']})

	def OnUiInitFinished(self, *args):
		# 注册UI 详细解释参照《UI API》
		clientApi.RegisterUI(labelConst.ModName, labelConst.labelUIName, labelConst.labelUIClsPath,
		                     labelConst.labelUIScreenDef)
		clientApi.RegisterUI(labelConst.ModName, 'labelHeadUI', "neteaseLabelScript.labelHeadUI.LabelHeadScreen",
		                     'netease_label_headUI.main')
		clientApi.RegisterUI(labelConst.ModName, 'labelPopUI', "neteaseLabelScript.labelPopUI.LabelPopScreen",
		                     'netease_label_popUI.main')
		clientApi.CreateUI(labelConst.ModName, labelConst.labelUIName, {"isHud": 1})
		self.mLabelUINode = clientApi.GetUI(labelConst.ModName, labelConst.labelUIName)
		if self.mLabelUINode:
			self.mLabelUINode.InitScreen()
			self.mLabelUINode.SetLayer("", clientApi.GetMinecraftEnum().UiBaseLayer.PopUpLv1)
		else:
			print '==== %s ====' % 'create UI: %s failed' % labelConst.labelUIScreenDef
		self.mPopUpUINode = clientApi.CreateUI(labelConst.ModName, 'labelPopUI', {"isHud": 1})
		if self.mPopUpUINode:
			self.mPopUpUINode.InitScreen()
			self.mPopUpUINode.SetLayer("", clientApi.GetMinecraftEnum().UiBaseLayer.PopUpLv2)
		else:
			print '==== %s ====' % 'create UI: labelPopUI failed'
		self.NotifyToServer(labelConst.QueryAllLabelsInUseEvent, {'playerId': self.mPlayerId})
		self.Supply()

	def Supply(self):
		labelHeadUINode = clientApi.CreateUI(labelConst.ModName, "labelHeadUI", {
			"bindEntityId": self.mPlayerId,
			"bindOffset": (0, 1.1, 0),
			"autoScale": 1,
			"isHud": 1
		})
		if labelHeadUINode:
			labelHeadUINode.SetLayer("", clientApi.GetMinecraftEnum().UiBaseLayer.Desk)
			self.mLabelHeadUINodes[len(self.mLabelHeadUINodes)] = labelHeadUINode

	def OnHighlight(self, data):
		if not self.mLabelHeadUINodes:
			return
		# print 'OnHighlight', data
		labels = data['labels']
		demand = len(labels)
		for i in range(demand - len(self.mLabelHeadUINodes))[:10]:
			self.Supply()
		total = len(self.mLabelHeadUINodes)
		d = total - demand
		count = 0
		for playerId in labels.keys():
			if playerId in self.mLabelHeadUINodes:
				count += 1
				labelHeadUINode = self.mLabelHeadUINodes.pop(playerId)
				label = labels[playerId]
				if labelHeadUINode.GetLabel() != label:
					labelHeadUINode.SetLabel(label)
				labelHeadUINode.Show()
				self.mLabelHeadUINodes[playerId] = labelHeadUINode
				labels.pop(playerId)
		for playerId in labels.keys():
			count += 1
			if count > total:
				return
			k, labelHeadUINode = self.mLabelHeadUINodes.popitem(0)
			if labelHeadUINode.ChangeBindEntityId(playerId):
				labelHeadUINode.SetLabel(labels[playerId])
				labelHeadUINode.Show()
				self.mLabelHeadUINodes[playerId] = labelHeadUINode
			else:
				print 'abnormal OnHighlight'
				self.mLabelHeadUINodes[k] = labelHeadUINode
		while d > 0:
			d -= 1
			k, labelHeadUINode = self.mLabelHeadUINodes.popitem(0)
			labelHeadUINode.Hide()
			self.mLabelHeadUINodes[k] = labelHeadUINode

	def OnDisplayLabelBoard(self, data):
		print 'OnDisplayLabelBoard', data
		if self.mLabelUINode:
			self.mLabelUINode.Open(data)

	def OnCache(self, data):
		self.mLabelInfoCache = data['cache']

	def GetAttrInfoByPlayerId(self, playerId):
		c = Counter()
		s = clientApi.GetSystem("neteaseBattle", "neteaseBattleBeh")
		if not s:
			return {}
		if not self.mLabelInfoCache:
			return {}
		for k, v in self.mLabelInfoCache.iteritems():
			if v['inUse']:
				c.update(s.GetEquipAttrDict('netease_label:{}'.format(k), 0))
		return dict(c)
