# -*- coding: utf-8 -*-

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

dungeonData = DungeonsData()

#公共配置
def GetServerTypeByServerId(serverId):
	import service.netgameApi as netServiceApi
	conf = netServiceApi.GetCommonConfig()
	serverList = conf['serverlist']
	for serverInfo in serverList:
		if serverInfo['serverid'] == serverId:
			return serverInfo['type']
	return None