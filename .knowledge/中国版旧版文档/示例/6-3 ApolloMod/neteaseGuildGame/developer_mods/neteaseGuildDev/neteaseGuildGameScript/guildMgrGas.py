# -*- coding:utf-8 -*-
from guildConsts import PlayerAttrType
from playerGas import PlayerGas
from guildGas import GuildGas
from guildConsts import GuildAttrType
import guildConsts

class GuildMgrGas(object):
	'''
	公会管理类
	'''
	def __init__(self):
		self.mGuildDict = {} #{mGuildId:GuildGas类}
		self.mPlayerDict = {}  # {playerUid:PlayerGas# 类}
		self.mPlayerIdToUid = {}# {playerId:playerUid}
		
	def CheckUidByPlayerId(self, playerId):
		return self.mPlayerIdToUid.get(playerId, None)
		
	def OnAddPlayer(self, args):
		"""
		玩家上线
		"""
		playerUid = args.get('uid', None)
		playerId = args.get('id', '-1')
		self.mPlayerIdToUid[playerId] = playerUid
		print "OnAddPlayer", args, self.mPlayerIdToUid
	
	def OnDelPlayer(self, args):
		"""
		玩家下线
		"""
		playerUid = args.get('uid', None)
		playerId = args.get('id', '-1')
		if self.mPlayerIdToUid.has_key(playerId):
			self.mPlayerIdToUid[playerId] = playerUid
		
	def OnSyncGuildAttrs(self, args):
		"""
		公会信息更新
		"""
		print "OnSyncGuildAttrs", args
		guildId = args.get(GuildAttrType.GuildId, None)
		if guildId != -1:
			if self.mGuildDict.has_key(guildId) == False:
				tempGuild = GuildGas()
				tempGuild.SyncAttrsDict(args)
				self.mGuildDict[guildId] = tempGuild
			else:
				self.mGuildDict[guildId].SyncAttrsDict(args)
	
	def OnSyncPlayerAttrs(self, args):
		"""
		公会成员信息更新
		"""
		print "OnSyncPlayerAttrs", args
		playerUid = args.get(PlayerAttrType.Uid, None)
		playerId = args.get("playerId", None)
		if args.get(PlayerAttrType.GuildId, -1) == -1:
			#防止在进入领地切换的时候已经退出公会
			guildConsts.GetServerModSystem().ReturnLobby(playerId)
			return
		if playerUid != None:
			if self.mPlayerDict.has_key(playerUid) == False:
				tempPlayer = PlayerGas()
				tempPlayer.SyncAttrsDict(args)
				self.mPlayerDict[playerUid] = tempPlayer
			else:
				self.mPlayerDict[playerUid].SyncAttrsDict(args)
			if playerId:
				self.mPlayerIdToUid[playerId] = playerUid
				
	def GetSameGuildPlayers(self, playerId):
		"""
		获取指定玩家的公会的其他成员uid列表
		"""
		lst = []
		playerUid = self.mPlayerIdToUid.get(playerId, None)
		if playerUid == None:
			return lst
		playerOne = self.mPlayerDict.get(playerUid)
		for uid, one in self.mPlayerDict.items():
			if playerOne.GetAttr(PlayerAttrType.GuildId) == one.GetAttr(PlayerAttrType.GuildId):
				lst.append(uid)
		return lst
			
	
			
		