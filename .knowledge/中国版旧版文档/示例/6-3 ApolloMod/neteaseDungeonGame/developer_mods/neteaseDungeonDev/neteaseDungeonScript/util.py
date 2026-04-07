# -*- coding: utf-8 -*-
def IsInArea(minPos, maxPos, pos):
	for i in xrange(3):
		if not (minPos[i] <= pos[i] <= maxPos[i]):
			return False
	return True

#mod.json配置相关
class DungeonTypeData(object):
	def __init__(self, dungeonType, name, num, minPos, maxPos, born):
		self.mType = dungeonType
		self.mName = name
		self.mMaxNum = num
		self.mMinVertex = minPos
		self.mMaxVertex = maxPos
		self.mBornPos = born

class OneGameDungeonData(object):
	def __init__(self, dungeonType, offset):
		self.mDungeonType = dungeonType
		self.mOffset = offset

class DungeonsData(object):
	def __init__(self):
		self.mType2GameDungeonDataList = {}
		self.mDungeonType2TypeData = {}
		self.Init()

	def Init(self):
		import netgame.apolloCommon.commonNetgameApi as commonNetgameApi
		confDict = commonNetgameApi.GetModJsonConfig("neteaseDungeonScript")
		dungeonTypeList = confDict['dungeon_type_list']
		self.InitDungeonTypeData(dungeonTypeList)
		gameDungeonList = confDict['game_dungeon_list']
		self.InitDungeon(gameDungeonList)

	def InitDungeonTypeData(self, dungeonTypeList):
		self.mDungeonType2TypeData = {}
		for info in dungeonTypeList:
			dungeonType = info['unique_type']
			data = DungeonTypeData(dungeonType, info['name'], info['max_players'], info['area_min_vertex'],
								info['area_max_vertex'], info['born_pos'])
			self.mDungeonType2TypeData[dungeonType] = data

	def InitDungeon(self, dungeonList):
		for gameType, gameDungeonList in dungeonList.iteritems():
			if '_comment' == gameType:
				continue
			self.InitGameDungeon(gameType, gameDungeonList)

	def InitGameDungeon(self, gameType, dungeonList):
		self.mType2GameDungeonDataList[gameType] = []
		for oneDungeon in dungeonList:
			dungeonType = oneDungeon['dungeon_type']
			offset = oneDungeon['area_offset']
			if dungeonType not in self.mDungeonType2TypeData:
				raise Exception("%s not found in dungeon_type_list of the mod.json" % dungeonType)
			data = OneGameDungeonData(self.mDungeonType2TypeData[dungeonType], offset)
			self.mType2GameDungeonDataList[gameType].append(data)

	def GetGameDungeonList(self, gameType):
		return self.mType2GameDungeonDataList.get(gameType, None)

	def GetOneGameDungeon(self, gameType, dungeonId):
		gameDungeonList = self.GetGameDungeonList(gameType)
		if gameDungeonList is None:
			return  None
		if dungeonId >= len(gameDungeonList):
			return None
		return gameDungeonList[dungeonId]

	def GetDungeonDataByPos(self, gameType, pos):
		gameDungeonList = self.GetGameDungeonList(gameType)
		if gameDungeonList is None:
			return None
		posDungeonData = None
		for idx, oneGameData in enumerate(gameDungeonList):
			offset = oneGameData.mOffset
			typeData = oneGameData.mDungeonType
			minPos = [offset[i] + typeData.mMinVertex[i] for i in xrange(3)]
			maxPos = [offset[i] + typeData.mMaxVertex[i] for i in xrange(3)]
			if IsInArea(minPos, maxPos, pos):
				posDungeonData = {}
				posDungeonData['offset'] = offset
				posDungeonData['type'] = typeData.mType
				posDungeonData['name'] = typeData.mName
				posDungeonData['maxNum'] = typeData.mMaxNum
				posDungeonData['minPos'] = typeData.mMinVertex
				posDungeonData['maxPos'] = typeData.mMaxVertex
				posDungeonData['bornPos'] = typeData.mBornPos
				posDungeonData['dungeonId'] = idx
				break
		return posDungeonData


dungeonData = DungeonsData()
# 获取副本配置的api
def GetOneGameDungeon(gameType, dungeonId):
	global dungeonData
	return dungeonData.GetOneGameDungeon(gameType, dungeonId)

def GetDungeonDataByPos(gameType, pos):
	global dungeonData
	return dungeonData.GetDungeonDataByPos(gameType, pos)