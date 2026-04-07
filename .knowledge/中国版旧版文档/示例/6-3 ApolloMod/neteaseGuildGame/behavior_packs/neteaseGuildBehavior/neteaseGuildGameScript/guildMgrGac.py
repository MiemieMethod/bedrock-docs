# -*- coding:utf-8 -*-
from guildConsts import PlayerAttrType
from playerGac import PlayerGac
from guildGac import GuildGac
from guildConsts import GuildAttrType
import guildConsts
import client.extraClientApi as clientApi
from guildConsts import UIDef
from guildConsts import NotifyDef

class GuildMgrGac(object):
	'''
	公会管理类
	'''
	def __init__(self):
		self.mGuildDict = {} #{mGuildId:GuildGac类}
		self.mPlayerDict = {}  # {playerId:PlayerGac类}
		self.mPlayerIdToUid = {}# {playerId:Uid}
		self.mPlayerId = clientApi.GetLocalPlayerId()
		
	def CheckUidByPlayerId(self, playerId):
		return self.mPlayerIdToUid.get(playerId, None)
		
	def OnAddPlayer(self, args):
		"""
		玩家上线，需要刷新公会界面
		"""
		playerUid = args.get('uid', None)
		playerId = args.get('id', '-1')
		self.mPlayerIdToUid[playerId] = playerUid
		print "OnAddPlayer", args, self.mPlayerIdToUid
		self.SetMyGuildUI()
	
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
		公会信息修改，需要刷新公会界面
		"""
		print "OnSyncGuildAttrs", args
		guildId = args.get(GuildAttrType.GuildId, None)
		if guildId != -1:
			if self.mGuildDict.has_key(guildId) == False:
				tempGuild = GuildGac()
				tempGuild.SyncAttrsDict(args)
				self.mGuildDict[guildId] = tempGuild
			else:
				self.mGuildDict[guildId].SyncAttrsDict(args)
			self.SetMyGuildUI()
	
	def OnSyncPlayerAttrs(self, args):
		"""
		公会成员信息修改，需要刷新公会界面
		"""
		print "OnSyncPlayerAttrs", args
		playerUid = args.get(PlayerAttrType.Uid, None)
		playerId = args.get("playerId", None)
		if playerUid != None:
			if self.mPlayerDict.has_key(playerUid) == False:
				tempPlayer = PlayerGac()
				tempPlayer.SyncAttrsDict(args)
				self.mPlayerDict[playerUid] = tempPlayer
			else:
				self.mPlayerDict[playerUid].SyncAttrsDict(args)
			if playerId:
				self.mPlayerIdToUid[playerId] = playerUid
				
	def OnShowUI(self, args):
		'''
		显示UI
		'''
		UIDefine = args.get('UIDef')
		UIOne = guildConsts.GetClientModSystem().GetUIMgr().GetUI(UIDefine)
		if UIOne:
			UIOne.ShowPanel(True)
			# if UIDefine == UIDef.UI_APPLY:
			# 	#playerId = clientApi.GetLocalPlayerId()
			# 	playerUid = self.mPlayerIdToUid.get(self.mPlayerId)
			# 	playerOne = self.mPlayerDict.get(playerUid, None)
			# 	if playerOne == None:
			# 		return
			# 	playerAtGuildId = playerOne.GetAttr(PlayerAttrType.GuildId)
			# 	if playerAtGuildId != -1 and self.mGuildDict.get(playerAtGuildId, None) != None:
			# 		guildOne = self.mGuildDict.get(playerAtGuildId, None)
			# 		UIOne.OnShowApplication(guildOne.GetAttr(GuildAttrType.ApplicationQueue))
			# 		UIOne.ShowPanel(True)
			# elif UIDefine == UIDef.UI_CREATEGUILD:
			# 	UIOne.ShowPanel(True)
		
	def OnShowTips(self, args):
		"""
		显示来自服务端的提示信息
		"""
		print "OnShowTips", args
		def ClickSureCancelCB():
			code = args['code']
			if code != guildConsts.CodeSuc and code!= guildConsts.CodeApplicationMaxNum:
				guildConsts.GetClientModSystem().GetUIMgr().UnShowAllUI()
		
		UIOne = guildConsts.GetClientModSystem().GetUIMgr().GetUI(UIDef.UI_QUIT)
		if UIOne:
			messageData = args['message']
			UIOne.SetNotifyPanel(NotifyDef.TIPS, ClickSureCancelCB, ClickSureCancelCB, messageData)
				
	def SetMyGuildUI(self):
		"""
		刷新公会详情界面
		"""
		playerUid = self.mPlayerIdToUid.get(self.mPlayerId)
		playerOne = self.mPlayerDict.get(playerUid, None)
		if playerOne == None:
			print "SetMyGuildUI", playerUid, "is None"
			return
		playerAtGuildId = playerOne.GetAttr(PlayerAttrType.GuildId)
		guildOne = self.mGuildDict.get(playerAtGuildId, None)
		if playerAtGuildId == -1 or self.mGuildDict.get(playerAtGuildId, None) == None:
			print "SetMyGuildUI", playerUid, "没公会"
			return
		UIMyGuild = guildConsts.GetClientModSystem().GetUIMgr().GetUI(UIDef.UI_MYGUILD)
		if UIMyGuild == None:
			return
		UIMyGuild.OnShowGuild(guildOne.GetAttrsDictCurrent())
		UIApply = guildConsts.GetClientModSystem().GetUIMgr().GetUI(UIDef.UI_APPLY)
		if UIApply == None:
			return
		UIApply.OnShowApplication(guildOne.GetAttr(GuildAttrType.ApplicationQueue))
		if guildOne.GetAttr(GuildAttrType.ApplicationQueue) != None and len(guildOne.GetAttr(GuildAttrType.ApplicationQueue)) > 0:
			#申请队列有玩家，更新一下UI
			UIMyGuild.ShowTipsNewImg(True)
		else:
			UIMyGuild.ShowTipsNewImg(False)
			
	def OnShowGuild(self):
		'''
		显示公会
		'''
		#playerId = clientApi.GetLocalPlayerId()
		playerUid = self.mPlayerIdToUid.get(self.mPlayerId)
		print "OnShowGuild", playerUid
		playerOne = self.mPlayerDict.get(playerUid, None)
		if playerOne:
			playerAtGuildId = playerOne.GetAttr(PlayerAttrType.GuildId)
			if playerAtGuildId != -1 and self.mGuildDict.get(playerAtGuildId, None) != None:
				#guildOne = self.mGuildDict.get(playerAtGuildId, None)
				UIMyGuild = guildConsts.GetClientModSystem().GetUIMgr().GetUI(UIDef.UI_MYGUILD)
				#UIMyGuild.OnShowGuild(guildOne.GetAttrsDictCurrent())
				UIMyGuild.ShowPanel(True)
				#TODO 显示所在公会详细信息
		
			
		