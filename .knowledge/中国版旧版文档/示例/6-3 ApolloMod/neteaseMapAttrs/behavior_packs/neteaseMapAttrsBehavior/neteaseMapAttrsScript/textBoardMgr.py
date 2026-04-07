# -*- coding: utf-8 -*-

import client.extraClientApi as extraClientApi
import neteaseMapAttrsScript.util as util
from neteaseMapAttrsScript.mapAttrsConsts import DimensionIdOverWorld

class TextBoardMgr(object):
	def __init__(self, playerId, offset=5.0):
		self.mPlayerId = playerId
		self.mCheckOffset = offset
		self.mAddTimer = None
		self.mTextWithPlaceMap = {}
		self.mTextIdxToEntityId = {}

	def Init(self, configData):
		textWithPlaceList = configData.get("text_with_place_list", None)
		if not textWithPlaceList:
			return
		idx = 0
		for conf in textWithPlaceList:
			text = conf.get("text", None)
			pos = conf.get("pos", None)
			if text is None or pos is None:
				continue
			idx += 1
			self.mTextWithPlaceMap[idx] = {
				"text": text,
				"pos": tuple(pos),
				"dim": conf.get("dim", DimensionIdOverWorld),
				"textColor": conf.get("textColor", (1.0, 0.0, 0.0, 1.0)),
				"tagColor": conf.get("tagColor", (0.0, 0.0, 1.0, 0.3)),
				"size": conf.get("size", 1.0),
				"depthTest": conf.get("depthTest", True),
			}
		comp = extraClientApi.CreateComponent(extraClientApi.GetLevelId(), "Minecraft", "game")
		self.mAddTimer = comp.AddRepeatedTimer(3.0, self.CheckAddTextBoard)

	def Destroy(self):
		if self.mAddTimer:
			comp = extraClientApi.CreateComponent(extraClientApi.GetLevelId(), "Minecraft", "game")
			comp.CancelTimer(self.mAddTimer)
			self.mAddTimer = None
		for idx, entityId in self.mTextIdxToEntityId.iteritems():
			util.GetSystem().DestroyEntity(entityId)
		self.mTextIdxToEntityId.clear()

	def OnDimChange(self, data):
		needRemoveList = []
		dim = util.GetSystem().GetLocalPlayerDim()
		for idx, entityId in self.mTextIdxToEntityId.iteritems():
			if self.mTextWithPlaceMap[idx]["dim"] == dim:
				continue
			util.GetSystem().DestroyEntity(entityId)
			needRemoveList.append(idx)
		if needRemoveList:
			print "OnDimChange needRemoveList=%s"%str(needRemoveList)
			for idx in needRemoveList:
				del self.mTextIdxToEntityId[idx]

	def IsFar(self, pos, otherPos):
		for i in xrange(3):
			if abs(pos[i] - otherPos[i]) > self.mCheckOffset:
				return True
		return False

	def CheckAddTextBoard(self):
		pos = util.GetEntityPos(self.mPlayerId)
		dim = util.GetSystem().GetLocalPlayerDim()
		if not pos:
			return
		for idx, conf in self.mTextWithPlaceMap.iteritems():
			if self.mTextIdxToEntityId.has_key(idx):
				continue
			if dim != conf["dim"]:
				continue
			if self.IsFar(pos, conf["pos"]):
				continue
			#print "try create idx=%s pos=%s player=%s" % (idx, conf["pos"], pos)
			entityId = util.GetSystem().CreateEngineTextboard(
				conf["text"], self.mPlayerId, conf["pos"], conf["textColor"],
				conf["tagColor"], conf["size"], conf["depthTest"])
			#print "create result entityId=%s type=%s" % (entityId, type(entityId))
			if entityId is None or entityId <= 0:
				continue
			self.mTextIdxToEntityId[idx] = entityId


