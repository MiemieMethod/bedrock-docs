# -*- coding:utf-8 -*-
from guildGas import GuildGas
from guildConsts import GuildAttrType
from guildConsts import PlayerAttrType
from guildConsts import DutyType
import guildConsts as guildConsts
from playerGas import PlayerGas
from mapGas import MapGas
import time
import timer
import datetime
import logout
import netgame.apolloCommon.commonNetgameApi as commonNetgameApi

class GuildMgrGas(object):
	'''
	公会管理类
	'''
	def __init__(self):
		self.mGuildDict = {} #{mGuildId:GuildGas类}
		self.mBaseGuildId = 0
		self.mPlayerDict = {} #{mUid:PlayerGas类}
		self.mMapDict = {} #{mMapId:MapGas类}
		
		self.mGuildLimitNum = 0 #服务器上限公会个数
		self.mDismissActivity = 0 #自动解散的活跃度
		self.mDismissDay = 0 #自动解散的天数
		self.mGuildMaxPeopleNum = 0 #公会上限人数
		
		self.mFrame = 0
		self.mCheckActivityTimer = None
		self.mRepeatedCheckActivityTimer = None
		#记录清除活跃度的时间
		self.mClearActivityBaseTime = datetime.datetime.now()
		#用于检测重复的公会名字
		self.mAllGuildNameList = {} #name:id
		
	def SetParam(self, modConfig):
		"""
		加载mod.json的配置
		"""
		self.mGuildLimitNum = modConfig.get("GuildLimitNum", 0)  # 服务器上限公会个数
		self.mDismissActivity = modConfig.get("DismissActivity", 0)  # 自动解散的活跃度
		self.mDismissDay = modConfig.get("DismissDay", 0)  # 自动解散的天数
		self.mGuildMaxPeopleNum = modConfig.get("GuildMaxPeopleNum", 0)  # 公会上限人数
		self.mAllMapDict = modConfig.get('map', {})
		self.mAllMapDict.pop("_comment")
		i = 0
		for serverType, oneServerMapDict in self.mAllMapDict.items():
			for posMes in oneServerMapDict:
				mapData = {'mapId': i, 'serverType': serverType, 'pos1': posMes.get('pos1'), 'pos2': posMes.get('pos2'), 'used':False ,'tranPos':posMes.get('tranPos')}
				self.mMapDict[i] = MapGas(mapData)
				i = i + 1
				
		print "SetParam", self.mMapDict
		
	def GenerateGuildId(self):
		"""
		返回一个唯一的公会ID
		"""
		self.mBaseGuildId += 1
		return self.mBaseGuildId
	
	def GenerateMapId(self):
		"""
		返回一个空闲的mapId
		"""
		reMapId = -1
		for mapId, mapOne in self.mMapDict.items():
			if mapOne.GetMapUsed() == False:
				reMapId = mapOne.GetMapId()
				return reMapId
		return reMapId
	
	def CreateGuild(self, initParam):
		'''
		创建公会
		'''
		guildId = self.GenerateGuildId()
		initParam[GuildAttrType.GuildId] = guildId
		initParam[GuildAttrType.Activity] = 0
		initParam[GuildAttrType.MaxNum] = self.mGuildMaxPeopleNum
		initParam[GuildAttrType.UnActivityDay] = 0
		self.mGuildDict[guildId] = GuildGas(initParam)
		self.mGuildDict[guildId].DoSave()
		# self.mGuildDict[guildId].SetDirty(True)
		return self.mGuildDict[guildId]
	
	def SyncGuildAttrsToClient(self, guildOne, attrsToSync):
		'''
		同步公会属性至客户端
		'''
		playerList = dict(guildOne.GetAttr(GuildAttrType.PresidentPlayerDict).items() + \
		             guildOne.GetAttr(GuildAttrType.ElderPlayerDict).items() + \
		             guildOne.GetAttr(GuildAttrType.CommonPlayerDict).items())
		attrsToSync[GuildAttrType.GuildId] = guildOne.GetAttr(GuildAttrType.GuildId)
		print "SyncGuildAttrsToClient", attrsToSync
		for playerUid in playerList:
			playerGas = self.mPlayerDict.get(playerUid, None)
			if playerGas:
				online = playerGas.GetAttr(PlayerAttrType.Online)
				duty = playerGas.GetAttr(PlayerAttrType.Duty)
				if online:
					attrsToSend = attrsToSync.copy()
					if duty not in (DutyType.President, DutyType.Elder) and attrsToSend.has_key(GuildAttrType.ApplicationQueue):
						#不是会长或长老，不发给客户端申请队列
						attrsToSend.pop(GuildAttrType.ApplicationQueue)
					if not attrsToSend:
						continue
					serverId = playerGas.GetAttr(PlayerAttrType.ServerId)
					attrsToSend['uid'] = playerUid #带上uid，同步到对应的客户端
					guildConsts.GetServiceModSystem().NotifyToServerNode(serverId, guildConsts.SyncGuildAttrsFromServiceEvent, attrsToSend)
				
	def OnAddPlayerFromServer(self, serverId, callbackId, args):
		"""
		玩家上限，加载（或者新建）此玩家的公会相关信息
		"""
		print "OnAddPlayerFromServer", args
		playerUid = args.get('uid', None)
		playerId = args.get('id', None)
		playerNickName = args.get('nickName', "")
		playerLevel = args.get('playerLevel', 0)
		def checkPlayerCb(sqlResult, usemysql):
			print "checkPlayerCb", sqlResult
			# 数据库没有, 则新建一个默认值；2.数据库有，以数据库为准新建一个玩家
			if len(sqlResult) <= 0:
					#新建一个默认值
				initParam = {
					PlayerAttrType.Uid: playerUid,
					PlayerAttrType.Online: True,
					PlayerAttrType.ServerId: serverId,
					PlayerAttrType.Duty: DutyType.Common,
					PlayerAttrType.GuildId: -1,
					PlayerAttrType.Activity: 0,
					PlayerAttrType.Name: playerNickName,
					PlayerAttrType.Level: playerLevel,
					PlayerAttrType.LastLoginTime: 0,
				}
			else:
				# activity = sqlResult[0][4]
				# playerAtGuild = sqlResult[0][2]
				# lastLoginTime = sqlResult[0][6]
				#以数据库数据，新建一个玩家
				initParam = {
					PlayerAttrType.Uid: playerUid,
					PlayerAttrType.Online: True,
					PlayerAttrType.ServerId: serverId,
					PlayerAttrType.Duty: sqlResult[0][3],
					PlayerAttrType.GuildId: sqlResult[0][2],
					PlayerAttrType.Activity: sqlResult[0][4],
					PlayerAttrType.Name: playerNickName,
					PlayerAttrType.Level: playerLevel,
					PlayerAttrType.LastLoginTime: sqlResult[0][6],
				}
			if usemysql == True:
				tempPlayer = PlayerGas(initParam)
				self.mPlayerDict[playerUid] = tempPlayer
			else:
				self.mPlayerDict[playerUid].InitPlayer(initParam)
			# self.mPlayerDict[playerUid].DoSave()
			# self.mPlayerDict[playerUid].SetDirty(True)
			playerAtGuild = self.mPlayerDict[playerUid].GetAttr(PlayerAttrType.GuildId)
			lastLoginTime = self.mPlayerDict[playerUid].GetAttr(PlayerAttrType.LastLoginTime)
			currentTime = time.time()
			#活跃度
			self.AddActivity(playerUid, playerAtGuild, currentTime, lastLoginTime)
			self.mPlayerDict[playerUid].SetAttrCurrent(PlayerAttrType.LastLoginTime, currentTime)
			#直接保存
			self.mPlayerDict[playerUid].DoSave()
			#改变一下在公会列表的信息
			self.ChangeAttrsInGuild(playerUid, playerAtGuild)
			# 登陆的时候，推一下玩家和公会的信息
			self.AddPlayerSync(serverId, playerUid, playerAtGuild)
		if self.mPlayerDict.has_key(playerUid):
			# playerAtGuild = self.mPlayerDict[playerUid].GetAttr(PlayerAttrType.GuildId)
			# lastLoginTime = self.mPlayerDict[playerUid].GetAttr(PlayerAttrType.LastLoginTime)
			# #登陆时活跃度增加
			# currentTime = int(time.time())
			# self.AddActivity(playerUid, playerAtGuild, currentTime, lastLoginTime)
			# self.mPlayerDict[playerUid].SetAttrCurrent(PlayerAttrType.LastLoginTime, currentTime)
			# self.mPlayerDict[playerUid].SetAttrCurrent(PlayerAttrType.ServerId, serverId)
			# self.mPlayerDict[playerUid].DoSave()
			# self.mPlayerDict[playerUid].SetDirty(True)
			# #登陆的时候，推一下玩家和公会的信息
			# self.AddPlayerSync(serverId, playerUid, playerAtGuild)
			name = self.mPlayerDict[playerUid].GetAttr(PlayerAttrType.Name)
			guildId = self.mPlayerDict[playerUid].GetAttr(PlayerAttrType.GuildId)
			duty = self.mPlayerDict[playerUid].GetAttr(PlayerAttrType.Duty)
			activity = self.mPlayerDict[playerUid].GetAttr(PlayerAttrType.Activity)
			level = self.mPlayerDict[playerUid].GetAttr(PlayerAttrType.Level)
			lastLoginTime = self.mPlayerDict[playerUid].GetAttr(PlayerAttrType.LastLoginTime)
			checkPlayerCb(((playerUid, name, guildId, duty, activity, level, lastLoginTime),), False)
		else:
			guildConsts.GetServiceModSystem().GetMysqlMgr().CheckPlayerByUid(playerUid, lambda sqlResult:checkPlayerCb(sqlResult, True))
			
	def ChangeAttrsInGuild(self, playerUid, playerAtGuild):
		'''
		改变保存在公会的属性
		'''
		playerOne = self.mPlayerDict.get(playerUid, None)
		if playerOne == None:
			return
		playerAttrs = playerOne.GetAttrsSaveInGuild()
		duty = playerOne.GetAttr(PlayerAttrType.Duty)
		guildOne = self.mGuildDict.get(playerAtGuild, None)
		if guildOne == None:
			return
		for attrType, attrValues in playerAttrs.items():
			guildOne.ChangePlayerAttr(playerUid, duty, attrType, attrValues)
			
	
	def AddPlayerSync(self, serverId, playerUid, playerAtGuild):
		#logout.info("AddPlayerSync", self.mGuildDict)
		self.mPlayerDict[playerUid].AddPlayerSync()
		guildOne = self.mGuildDict.get(playerAtGuild, None)
		if guildOne:
			attrsToSync = guildOne.GetAttrsToSyncWhenAddPlayer()
			attrsToSync['uid'] = playerUid  # 带上uid，同步到对应的客户端
			logout.info("AddPlayerSync Guild", attrsToSync)
			guildConsts.GetServiceModSystem().NotifyToServerNode(serverId, guildConsts.SyncGuildAttrsFromServiceEvent, attrsToSync)
			
	def AddActivity(self, playerUid, guildId, currentTime, lastLoginTime):
		"""
		修改玩家活跃度
		"""
		playerOne = self.mPlayerDict.get(playerUid, None)
		guildOne = self.mGuildDict.get(guildId, None)
		if playerOne == None or guildOne == None:
			#没有公会，不增加活跃度
			return
		playerActivity = playerOne.GetAttr(PlayerAttrType.Activity)
		guildActivity = guildOne.GetAttr(GuildAttrType.Activity)
		#是一天，则增加活跃度
		if guildConsts.IsOneDay(currentTime, lastLoginTime) == False:
			playerOne.SetAttrCurrent(PlayerAttrType.Activity, playerActivity + 1)
			guildOne.SetAttrCurrent(GuildAttrType.Activity, guildActivity + 1, True)
			
	def OnDelPlayerFromServer(self, serverId, callbackId, args):
		"""
		玩家下线，触发强制存档
		"""
		print "OnDelPlayerFromServer", args
		playerUid = args.get('uid', None)
		playerId = args.get('id', None)
		if playerUid != None:
			if self.mPlayerDict.has_key(playerUid):
				self.mPlayerDict[playerUid].SetAttrCurrent(PlayerAttrType.Online, False)
				self.mPlayerDict[playerUid].SetAttrCurrent(PlayerAttrType.ServerId, None)
				# #离线存档一次，并关闭自动存档
				self.mPlayerDict[playerUid].DoSave()
				# self.mPlayerDict[playerUid].SetDirty(False)
				playerAtGuild = self.mPlayerDict[playerUid].GetAttr(PlayerAttrType.GuildId)
				# 改变一下在公会列表的信息
				self.ChangeAttrsInGuild(playerUid, playerAtGuild)
				
	def OnCreateGuildFromServer(self, serverId, callbackId, args):
		"""
		新建公会
		"""
		playerUid = args.get('uid')
		playerOne = self.mPlayerDict.get(playerUid)
		guildName = guildConsts.UnicodeConvert(args.get('guildName'))
		logout.info("OnCreateGuildFromServer", args)
		if guildName == "" or commonNetgameApi.CheckNameValid(guildName) == 0:
			logout.info("OnCreateGuildFromServer", "创建失败, 公会名字不合法", args)
			self.SendResponse(serverId, callbackId, guildConsts.CodeGuildNameNotLegal, playerUid)
			self.ResponseSuc(serverId, callbackId, playerUid, guildName, False)
			return
		if guildName in self.mAllGuildNameList:
			logout.info("OnCreateGuildFromServer", "创建失败, 公会名字重复", args)
			self.SendResponse(serverId, callbackId, guildConsts.CodeGuildNameRepeated, playerUid)
			self.ResponseSuc(serverId, callbackId, playerUid, guildName, False)
			return
		if len(self.mGuildDict) >= self.mGuildLimitNum:
			logout.info("OnCreateGuildFromServer", "创建失败，公会已达最大数量", args)
			#TODO 返回公会已经达到最大数量
			self.SendResponse(serverId, callbackId, guildConsts.CodeServiceGuildNumOutOfLimit, playerUid)
			self.ResponseSuc(serverId, callbackId, playerUid, guildName, False)
			return
		if playerOne == None:
			logout.info("OnCreateGuildFromServer", "创建失败，玩家不存在", args)
			# TODO 返回玩家不存在
			self.SendResponse(serverId, callbackId, guildConsts.CodePlayerNone, playerUid)
			self.ResponseSuc(serverId, callbackId, playerUid, guildName, False)
			return
		playerAtguildId = playerOne.GetAttr(PlayerAttrType.GuildId)
		if playerAtguildId != -1:
			logout.info("OnCreateGuildFromServer", "创建失败，玩家已经有公会", args)
			#TODO 返回已有公会
			self.SendResponse(serverId, callbackId, guildConsts.CodePlayerHasGuild, playerUid)
			self.ResponseSuc(serverId, callbackId, playerUid, guildName, False)
			return
		else:
			# initParam = {
			# 	GuildAttrType.Name :guildName,
			# }
			# guildOne = self.CreateGuild(initParam)
			# guildId = guildOne.GetAttr(GuildAttrType.GuildId)
			# # self.mPlayerDict[playerUid].SetAttrCurrent(PlayerAttrType.Duty, DutyType.President)#创建成功，创建者是会长
			# # self.mPlayerDict[playerUid].SetAttrCurrent(PlayerAttrType.GuildId, guildId)#创建成功，假如该公会
			# self.AddPlayerToGuildPlayerList(playerOne, guildOne, DutyType.President, True)
			# logout.info("创建成功！", self.mGuildDict)
			#
			# self.GetBriefGuildMes(serverId, callbackId, {"uid": playerUid})
			# #TODO 返回创建公会成功
			# self.SendResponse(serverId, callbackId, guildConsts.CodeCreateSuccess, playerUid)
			#回调，让lobbygame去扣钻石
			mapId = self.GenerateMapId()
			if mapId == -1:
				self.SendResponse(serverId, callbackId, guildConsts.CodeServiceGuildNumOutOfLimit, playerUid)
				self.ResponseSuc(serverId, callbackId, playerUid, guildName, False)
				return
			self.ResponseSuc(serverId, callbackId, playerUid, guildName, True, mapId)
			logout.info("OnCreateGuildFromServer", "创建成功， 请lobygame扣除钻石", args)
			return
		
	def OnCreateGuildSuccessFromServer(self, serverId, callbackId, args):
		"""
		公会创建成功通知，来自server
		"""
		playerUid = args.get('uid')
		guildName = args.get('guildName')
		mapId = args.get('mapId')
		initParam = {
			GuildAttrType.Name: guildName,
			GuildAttrType.MapId: mapId
		}
		guildOne = self.CreateGuild(initParam)
		guildId = guildOne.GetAttr(GuildAttrType.GuildId)
		# self.mPlayerDict[playerUid].SetAttrCurrent(PlayerAttrType.Duty, DutyType.President)#创建成功，创建者是会长
		# self.mPlayerDict[playerUid].SetAttrCurrent(PlayerAttrType.GuildId, guildId)#创建成功，假如该公会
		playerOne = self.mPlayerDict.get(playerUid, None)
		if playerOne == None:
			self.SendResponse(serverId, callbackId, guildConsts.CodePlayerNone, playerUid)
			return
		self.mMapDict[mapId].SetMapUsed(True)
		self.AddPlayerToGuildPlayerList(playerOne, guildOne, DutyType.President, True, True)
		logout.info("OnCreateGuildSuccessFromServer", "创建成功！", args)

		self.GetBriefGuildMes(serverId, callbackId, {"uid": playerUid})
		#TODO 返回创建公会成功
		self.SendResponse(serverId, callbackId, guildConsts.CodeCreateSuccess, playerUid)
		
		#记录一下公会名字
		self.mAllGuildNameList[guildName] = guildId
		
	def ResponseSuc(self, serverId, callbackId, playerUid, guildName, suc, mapId = -1):
		response = {'suc': suc, 'uid':playerUid, 'guildName': guildName, 'mapId': mapId}
		guildConsts.GetServiceModSystem().ResponseToServer(serverId, callbackId, response)
	
	def OnApplication(self, serverId, callbackId, args):
		'''
		申请加入公会
		'''
		logout.info("OnApplication", args)
		playerUid = args.get('uid')
		guildId = args.get('guildId')
		playerOne = self.mPlayerDict.get(playerUid)
		if playerOne:
			playerAtguildId = playerOne.GetAttr(PlayerAttrType.GuildId)
			playerLevel = playerOne.GetAttr(PlayerAttrType.Level)
			playerName = playerOne.GetAttr(PlayerAttrType.Name)
			if playerAtguildId != -1:
				# TODO 返回已有公会
				logout.info("OnApplication", "已有公会", args)
				self.SendResponse(serverId, callbackId, guildConsts.CodePlayerHasGuild, playerUid)
				return
			else:
				guildOne = self.mGuildDict.get(guildId, None)
				if guildOne:
					if guildOne.GetPlayerNum() >= guildOne.GetAttr(GuildAttrType.MaxNum):
						self.SendResponse(serverId, callbackId, guildConsts.CodeApplicationMaxNum, playerUid)
						return
					else:
						data = {'uid': playerUid, 'level': playerLevel, 'name': playerName}
						guildOne.PutUidToApplicationQueue(data)
						self.SendResponse(serverId, callbackId, guildConsts.CodeApplicationSuccess, playerUid)
	
	def OnAppointPlayer(self, serverId, callbackId, args):
		'''
		调整职务
		'''
		operatorUid = args.get('operatorUid') #操作者Uid
		appointerUid = args.get('beAppointUid') #被任命者Uid
		desDuty = args.get('desDuty')
		operatorOne = self.mPlayerDict.get(operatorUid)
		apponiterOne = self.mPlayerDict.get(appointerUid)
		if operatorOne == None and apponiterOne == None:
			#TODO 玩家不存在
			logout.info("参数错误", "operatorUid", operatorUid)
			logout.info("参数错误", "appointerUid", appointerUid)
			self.SendResponse(serverId, callbackId, guildConsts.CodeParamError,operatorUid)
			return
		operatorAtguildId = operatorOne.GetAttr(PlayerAttrType.GuildId)
		apponiterAtguildId = apponiterOne.GetAttr(PlayerAttrType.GuildId)
		operatorDuty = operatorOne.GetAttr(PlayerAttrType.Duty)
		apponiterDuty = apponiterOne.GetAttr(PlayerAttrType.Duty)
		if operatorAtguildId != apponiterAtguildId or operatorAtguildId == -1:
			#TODO 返回公会不同
			logout.info("OnAppointPlayer", "返回公会不同", args)
			self.SendResponse(serverId, callbackId, guildConsts.CodeGuildDiff,  operatorUid)
			return
		guildOne = self.mGuildDict.get(operatorAtguildId, None)
		if operatorDuty != DutyType.President: #不是会长
			# TODO 返回权限不足
			logout.info("OnAppointPlayer", "权限不足", args)
			self.SendResponse(serverId, callbackId, guildConsts.CodeDutyNotEnough,  operatorUid)
			return
		if guildOne == None:
			# TODO
			self.SendResponse(serverId, callbackId, guildConsts.CodeGuildNone, operatorUid)
			return
		if desDuty == DutyType.President:#会长
			#转让会长
			operatorOne.SetAttrCurrent(PlayerAttrType.Duty, DutyType.Common, True)
			apponiterOne.SetAttrCurrent(PlayerAttrType.Duty, desDuty, True)
			guildOne.ChangePlayerDuty(operatorUid, operatorDuty, DutyType.Common)
			guildOne.ChangePlayerDuty(appointerUid, apponiterDuty, desDuty)
			self.SendGuildAttr(apponiterOne, guildOne, GuildAttrType.ApplicationQueue)
			self.SendGuildAttr(operatorOne, guildOne, GuildAttrType.ApplicationQueue, False)
		elif desDuty == DutyType.Elder:
			# if len(guildOne.GetAttr(GuildAttrType.ElderPlayerDict)) >= 3:
			# 	# TODO 返回位置已满
			# 	logout.info("位置已满")
			# 	return
			# else:
			apponiterOne.SetAttrCurrent(PlayerAttrType.Duty, desDuty, True)
			guildOne.ChangePlayerDuty(appointerUid, apponiterDuty, desDuty)
			self.SendGuildAttr(apponiterOne, guildOne, GuildAttrType.ApplicationQueue)
		elif desDuty == DutyType.Common:
			apponiterOne.SetAttrCurrent(PlayerAttrType.Duty, desDuty, True)
			guildOne.ChangePlayerDuty(appointerUid, apponiterDuty, desDuty)
			self.SendGuildAttr(apponiterOne, guildOne, GuildAttrType.ApplicationQueue, False)
	
	def SendGuildAttr(self, playerOne, guildOne, attr, needsToSync = True):
		serverId = playerOne.GetAttr(PlayerAttrType.ServerId)
		attrsToSend = {}
		attrsToSend['uid'] = playerOne.GetAttr(PlayerAttrType.Uid)  # 带上uid，同步到对应的客户端
		attrsToSend[GuildAttrType.GuildId] = guildOne.GetAttr(GuildAttrType.GuildId)
		attrsToSend[GuildAttrType.ApplicationQueue] = guildOne.GetAttr(attr) if needsToSync else {}
		guildConsts.GetServiceModSystem().NotifyToServerNode(serverId, guildConsts.SyncGuildAttrsFromServiceEvent,
		                                                     attrsToSend)
	
	def OnAgreePlayer(self, serverId, callbackId, args):
		'''
		同意加入公会的申请
		'''
		logout.info("OnAgreePlayer", args)
		operatorUid = args.get('operatorUid')
		applicantUid = args.get('applicantUid')
		applicantOne = self.mPlayerDict.get(applicantUid, None)
		operatorOne = self.mPlayerDict.get(operatorUid, None)
		isAdd = args.get('isAdd')
		if applicantOne == None or operatorOne == None:
			# TODO 玩家不存在了
			logout.info("参数错误", "operatorUid", operatorUid)
			logout.info("参数错误", "applicantUid", applicantUid)
			self.SendResponse(serverId, callbackId, guildConsts.CodeParamError, operatorUid)
			return
		applicantAtguildId = applicantOne.GetAttr(PlayerAttrType.GuildId)
		operatorAtGuild = operatorOne.GetAttr(PlayerAttrType.GuildId)
		if operatorOne.GetAttr(PlayerAttrType.Duty) not in (DutyType.President, DutyType.Elder):
			#TODO 返回权限不足
			logout.info("OnAgreePlayer", "权限不足", args)
			self.SendResponse(serverId, callbackId, guildConsts.CodeDutyNotEnough, operatorUid)
			return
		if applicantAtguildId != -1:
			#TODO 返回有公会了
			logout.info("OnAgreePlayer", "已有公会", args)
			self.SendResponse(serverId, callbackId, guildConsts.CodePlayerHasGuild, operatorUid)
			isAdd = False
		guildOne = self.mGuildDict.get(operatorAtGuild, None)
		if guildOne == None:
			# TODO 公会不存在
			logout.info("OnAgreePlayer", "公会不存在", args)
			self.SendResponse(serverId, callbackId, guildConsts.CodeGuildNone, operatorUid)
			return
		if guildOne.GetPlayerNum() >= guildOne.GetAttr(GuildAttrType.MaxNum) and isAdd == True:
			# TODO 人数已满
			logout.info("OnAgreePlayer", "人数已满", args)
			self.SendResponse(serverId, callbackId, guildConsts.CodeGuildPeopleMaxNum, operatorUid)
			isAdd = False
		#进来默认职位是普通
		self.AddPlayerToGuildPlayerList(applicantOne, guildOne, DutyType.Common, isAdd)
		
	def OnKickPlayer(self, serverId, callbackId, args):
		"""
		公会管理层踢掉指定的成员
		"""
		operatorUid = args.get('operatorUid')
		knickUid = args.get('kickUid')
		operatorOne = self.mPlayerDict.get(operatorUid)
		kickerOne = self.mPlayerDict.get(knickUid)
		if operatorOne == None or kickerOne == None:
			# TODO 返回玩家不存在了
			logout.info("参数错误", "operatorUid", operatorUid)
			logout.info("参数错误", "knickUid", knickUid)
			self.SendResponse(serverId, callbackId, guildConsts.CodeParamError, operatorUid)
			return
		operatorAtGuildId = operatorOne.GetAttr(PlayerAttrType.GuildId)
		kickerAtGuildId = kickerOne.GetAttr(PlayerAttrType.GuildId)
		guildOne = self.mGuildDict.get(operatorAtGuildId, None)
		if operatorAtGuildId != kickerAtGuildId or kickerAtGuildId == -1:
			# TODO 返回玩家已不在公会
			logout.info("OnKickPlayer", "玩家已不在公会", args)
			self.SendResponse(serverId, callbackId, guildConsts.CodePlayerNotInGuild,  operatorUid)
			return
		if (operatorOne.GetAttr(PlayerAttrType.Duty) > kickerOne.GetAttr(PlayerAttrType.Duty)) == False:
			#只能踢职位比自己低的
			#TODO 返回权限不足
			logout.info("OnKickPlayer", "权限不足", args)
			self.SendResponse(serverId, callbackId, guildConsts.CodeDutyNotEnough, operatorUid)
			return
		if guildOne == None:
			#TODO 返回公会已经没了
			self.SendResponse(serverId, callbackId, guildConsts.CodeGuildNone, operatorUid)
			return
		#踢出操作
		logout.info("OnKickPlayer", "踢出公会", args)
		kickerOne.SetAttrCurrent(PlayerAttrType.GuildId, -1, True)
		kickerOne.SetAttrCurrent(PlayerAttrType.Activity, 0, True)
		guildOne.KickPlayer(knickUid)
		self.SendResponse(kickerOne.GetAttr(PlayerAttrType.ServerId), callbackId, guildConsts.CodeKick, knickUid)
		
	def OnPlayerLeaveGuild(self, serverId, callbackId, args):
		'''
		玩家离开公会
		'''
		playerUid = args.get('uid')
		playerOne = self.mPlayerDict.get(playerUid)
		if playerOne == None:
			# TODO 返回玩家不存在了
			logout.info("参数错误", "playerUid", playerUid)
			self.SendResponse(serverId, callbackId, guildConsts.CodeParamError, playerUid)
			return
		playerAtGuildId = playerOne.GetAttr(PlayerAttrType.GuildId)
		if playerAtGuildId == -1:
			# TODO 返回玩家已不在公会
			logout.info("OnPlayerLeaveGuild", "玩家已不在公会", args)
			self.SendResponse(serverId, callbackId, guildConsts.CodePlayerNotInGuild, playerUid)
			return
		guildOne = self.mGuildDict.get(playerAtGuildId, None)
		if guildOne == None:
			# TODO 返回公会已经没了
			self.SendResponse(serverId, callbackId, guildConsts.CodeGuildNone, playerUid)
			logout.info("OnPlayerLeaveGuild", "公会已经没了", args)
			return
		playerDuty = playerOne.GetAttr(PlayerAttrType.Duty)
		if playerDuty == DutyType.President:
			#self.DismissGuild({'guildId': playerAtGuildId})
			playerList = dict(guildOne.GetAttr(GuildAttrType.PresidentPlayerDict).items() + \
			                  guildOne.GetAttr(GuildAttrType.ElderPlayerDict).items() + \
			                  guildOne.GetAttr(GuildAttrType.CommonPlayerDict).items())
			if len(playerList) >= 2:
				self.SendResponse(serverId, callbackId, guildConsts.CodePresidentCannotLeaveGuild, playerUid)
				return
			else:
				def deleteGuildCb(suc):
					if suc:
						logout.info("OnPlayerLeaveGuild", playerAtGuildId, "解散")
				self.DisMissGuildDetail(playerAtGuildId, deleteGuildCb)
				# # 删除数据库的信息
				# guildConsts.GetServiceModSystem().GetMysqlMgr().DeleteGuild(playerAtGuildId, deleteGuildCb)
				#self.SendResponse(serverId, callbackId, guildConsts.CodeGuildDisMiss, playerUid)
				return
		playerOne.SetAttrCurrent(PlayerAttrType.GuildId, -1, True)
		playerOne.SetAttrCurrent(PlayerAttrType.Activity, 0, True)
		guildOne.KickPlayer(playerUid)
		self.SendResponse(serverId, callbackId, guildConsts.CodeKick, playerUid)
		
	def OnReturnGuildMap(self, serverId, callbackId, args):
		'''
		返回公会驻地
		'''
		playerUid = args.get('uid')
		playerOne = self.mPlayerDict.get(playerUid)
		if playerOne == None:
			# TODO 返回玩家不存在了
			logout.info("参数错误", "playerUid", playerUid)
			self.SendResponse(serverId, callbackId, guildConsts.CodeParamError, playerUid)
			return
		playerAtGuildId = playerOne.GetAttr(PlayerAttrType.GuildId)
		if playerAtGuildId == -1:
			# TODO 返回玩家已不在公会
			logout.info("OnReturnGuildMap", "玩家已不在公会", args)
			self.SendResponse(serverId, callbackId, guildConsts.CodePlayerNotInGuild, playerUid)
			return
		guildOne = self.mGuildDict.get(playerAtGuildId, None)
		if guildOne == None:
			# TODO 返回公会已经没了
			self.SendResponse(serverId, callbackId, guildConsts.CodeGuildNone, playerUid)
			logout.info("OnReturnGuildMap", "公会已经没了", args)
			return
		mapId = guildOne.GetAttr(GuildAttrType.MapId)
		if mapId == -1:
			# TODO 返回公会已经没了
			self.SendResponse(serverId, callbackId, guildConsts.CodeGuildNone, playerUid)
			logout.info("OnReturnGuildMap", "地图没有", args)
			return
		serverType = self.mMapDict[mapId].GetServerType()
		bornPos = self.mMapDict[mapId].GetBornPos()
		args["bornPos"] = bornPos
		args["serverType"] = serverType
		guildConsts.GetServiceModSystem().ResponseToServer(serverId, callbackId, args)
		
		
		
	def OnDismissGuild(self, serverId, callbackId, args):
		'''
		解散公会
		'''
		print "OnDismissGuild", serverId, callbackId, args
		guildId = args.get('guildId', -1)
		if guildId == -1:
			guildName = args.get('guildName', None)
			if guildName and guildName in self.mAllGuildNameList:
				guildId = self.mAllGuildNameList[guildName]
			else:
				self.SendResponseToMaster(serverId, callbackId, guildConsts.CodeGuildNone)
				return
		guildOne = self.mGuildDict.get(guildId, None)
		if guildOne == None:
			#TODO 返回公会已经解散
			self.SendResponseToMaster(serverId, callbackId, guildConsts.CodeGuildNone)
			return
		def deleteGuildCb(suc):
			if suc != None:
				self.SendResponseToMaster(serverId, callbackId, guildConsts.CodeGuildDisMiss)
			else:
				self.SendResponseToMaster(serverId, callbackId, guildConsts.CodeDBError)
		self.DisMissGuildDetail(guildId, deleteGuildCb)
		#self.mGuildDict.pop(guildId)
		
	def AddPlayerToGuildPlayerList(self, playerOne, guildOne, duty, isAdd = True, isCreate = False):
		'''
		接受/拒绝玩家的加入公会申请
		'''
		playerAttrs = playerOne.GetAttrsSaveInGuild()
		uid = playerOne.GetAttr(PlayerAttrType.Uid)
		guildId = guildOne.GetAttr(GuildAttrType.GuildId)
		if isAdd:
			playerOne.SetAttrCurrent(PlayerAttrType.GuildId, guildId, True)
			playerOne.SetAttrCurrent(PlayerAttrType.Duty, duty, True)
			if not isCreate:
				self.SendResponse(playerOne.GetAttr(PlayerAttrType.ServerId), None, guildConsts.CodeAddSuccess, uid)
		guildOne.AddPlayerToGuildPlayerList(uid, playerAttrs, duty, isAdd)
		
	def OnLoadServerAddonScriptsAfter(self, args = None):
		'''
		服务器开启的时候调用，从数据库加载公会信息
		'''
		def checkAllGuildCb(sqlResult):
			logout.info("OnLoadServerAddonScriptsAfter", sqlResult)
			for guildOneMes in sqlResult:
				if guildOneMes != None:
					guildId = guildOneMes[0]
					#获取最大的ID
					self.mBaseGuildId = max(guildId, self.mBaseGuildId)
					initParam = {
						GuildAttrType.GuildId: guildId,
						GuildAttrType.Name: guildConsts.UnicodeConvert(guildOneMes[1]),
						GuildAttrType.MapId: guildOneMes[2],
						GuildAttrType.MaxNum: guildOneMes[3],
						GuildAttrType.Activity: guildOneMes[4],
						GuildAttrType.UnActivityDay: guildOneMes[5],
					}
					tempGuild = GuildGas(initParam)
					#tempGuild.SetDirty(True)
					self.mGuildDict[guildId] = tempGuild
					
					#设置地图以及用了
					if self.mMapDict.has_key(guildOneMes[2]):
						self.mMapDict[guildOneMes[2]].SetMapUsed()
					
					self.mAllGuildNameList[guildConsts.UnicodeConvert(guildOneMes[1])] = guildId
					
			self.LoadAllPlayer()
		guildConsts.GetServiceModSystem().GetMysqlMgr().CheckAllGuild(checkAllGuildCb)
		#self.CheckCheckActivityDetail()
		#计算到零点时间的间隔
		dayZeroTime = guildConsts.CalNextFuncTime(guildConsts.CHECK_ACTIVITY_TIME)
		self.mCheckActivityTimer = timer.TimerManager.addTimer(dayZeroTime, self.CheckActivity)
		self.mClearActivityBaseTime = datetime.datetime.now()
		
	def LoadAllPlayer(self):
		def checkAllPlayerCb(sqlResult):
			for playerOneMes in sqlResult:
				if playerOneMes != None:
					playerUid = playerOneMes[0]
					playerAtGuildId = playerOneMes[2]
					playerDuty = playerOneMes[3]
					initParam = {
						PlayerAttrType.Uid: playerUid,
						PlayerAttrType.Online: False,
						PlayerAttrType.ServerId: -1,
						PlayerAttrType.Duty: playerDuty,
						PlayerAttrType.GuildId: playerAtGuildId,
						PlayerAttrType.Activity: playerOneMes[4],
						PlayerAttrType.Name: playerOneMes[1],
						PlayerAttrType.Level: playerOneMes[5],
						PlayerAttrType.LastLoginTime: playerOneMes[6],
					}
					tempPlayer = PlayerGas(initParam)
					#tempPlayer.SetDirty(True)
					self.mPlayerDict[playerUid] = tempPlayer
					guildOne = self.mGuildDict.get(playerAtGuildId, None)
					if guildOne:
						self.AddPlayerToGuildPlayerList(tempPlayer, guildOne, playerDuty, True)
			for guildId, guildOne in self.mGuildDict.items():
				self.LoadAllApplication(guildId)
		guildConsts.GetServiceModSystem().GetMysqlMgr().CheckAllPlayer(checkAllPlayerCb)
	
	def LoadAllApplication(self, guildId):
		def checkApplicationCb(sqlResult):
			if sqlResult == None:
				return
			for applicationOne in sqlResult:
				playerUid = applicationOne[1]
				applicationTime = applicationOne[2]
				if self.mPlayerDict.has_key(playerUid):
					playerLevel = self.mPlayerDict[playerUid].GetAttr(PlayerAttrType.Level)
					playerName = self.mPlayerDict[playerUid].GetAttr(PlayerAttrType.Name)
					data = {'uid': playerUid, 'level': playerLevel, 'name': playerName,
					        'applicationTime': applicationTime, 'needSave': False}
					print "LoadAllApplication", guildId
					self.mGuildDict[guildId].PutUidToApplicationQueue(data)
		guildConsts.GetServiceModSystem().GetMysqlMgr().CheckApplicationByGuildId(guildId, checkApplicationCb)
	
	def CheckActivity(self):
		'''
		检查公会活跃度
		'''
		if self.mRepeatedCheckActivityTimer == None:
			self.mRepeatedCheckActivityTimer = timer.TimerManager.addRepeatTimer(guildConsts.ONE_DAY_TIME, self.CheckActivity)
			self.mCheckActivityTimer.cancel()
			self.mCheckActivityTimer = None
		self.CheckCheckActivityDetail()
					
	def CheckCheckActivityDetail(self):
		logout.info("CheckCheckActivityDetail ing.....")
		nowTime = datetime.datetime.now()
		if nowTime.month != self.mClearActivityBaseTime.month:
			# 每个月底12点清除活跃度
			self.ClearActivity()
			self.mClearActivityBaseTime = nowTime
		for guildId in list(self.mGuildDict):
			if self.mGuildDict[guildId].GetAttr(GuildAttrType.Activity) < self.mDismissActivity:
				unActivityDay = self.mGuildDict[guildId].GetAttr(GuildAttrType.UnActivityDay)
				unActivityDay = unActivityDay + 1
				if unActivityDay > self.mDismissDay:
					# 解散公会
					# self.DismissGuild({"guildId": guildId})
					def deleteGuildCb(suc):
						if suc:
							logout.info(guildId, "解散")
					self.DisMissGuildDetail(guildId, deleteGuildCb)
				else:
					self.mGuildDict[guildId].SetAttrCurrent(GuildAttrType.UnActivityDay, unActivityDay, True)
			else:
				self.mGuildDict[guildId].SetAttrCurrent(GuildAttrType.UnActivityDay, 0, True)
	
	def DisMissGuildDetail(self, guildId, deleteGuildCb = None):
		guildOne = self.mGuildDict[guildId]
		playerList = dict(guildOne.GetAttr(GuildAttrType.PresidentPlayerDict).items() + \
		                  guildOne.GetAttr(GuildAttrType.ElderPlayerDict).items() + \
		                  guildOne.GetAttr(GuildAttrType.CommonPlayerDict).items())
		guildMapId = guildOne.GetAttr(GuildAttrType.MapId)
		guildName = guildOne.GetAttr(GuildAttrType.Name)
		if guildName in self.mAllGuildNameList:
			self.mAllGuildNameList.pop(guildName)
		#TODO 判断存在不
		if self.mMapDict.has_key(guildMapId):
			self.mMapDict[guildMapId].SetMapUsed(False)
		self.mGuildDict.pop(guildId)
		for playerUid in playerList:
			playerOne = self.mPlayerDict.get(playerUid, None)
			if playerOne:
				playerOne.SetAttrCurrent(PlayerAttrType.GuildId, -1, True)
				playerOne.SetAttrCurrent(PlayerAttrType.Activity, 0, True)
				serverId = playerOne.GetAttr(PlayerAttrType.ServerId)
				if serverId:
					self.SendResponse(serverId, None, guildConsts.CodeGuildDisMiss, playerUid)
		
		# 删除数据库的信息
		guildConsts.GetServiceModSystem().GetMysqlMgr().DeleteGuild(guildId, deleteGuildCb)
	
	
	def ClearActivity(self):
		'''
		清除活跃度，月底12点调用
		'''
		for guildId, guildOne in self.mGuildDict.iteritems():
			guildOne.SetAttrCurrent(GuildAttrType.Activity, 0, True)
		for playerUid, playerOne in self.mPlayerDict.iteritems():
			playerOne.SetAttrCurrent(GuildAttrType.Activity, 0, True)
	
	def SendResponse(self, serverId, callbackId, code, uid = None):
		'''
		返回消息给lobby/game
		'''
		response = {}
		response['code'] = code
		response['message'] = guildConsts.ResponseText[code]
		if uid:
			response['uid'] = uid
		if serverId != None:
			guildConsts.GetServiceModSystem().NotifyToServerNode(serverId, guildConsts.ShowTipsFromServiceEvent, response)
	
	def SendResponseToMaster(self, serverId, callbackId, code):
		'''
		返回消息给master
		'''
		print "SendResponseToMaster", serverId, callbackId, code
		response = {}
		response['code'] = code
		response['message'] = guildConsts.ResponseText[code]
		guildConsts.GetServiceModSystem().ResponseToServer(serverId, callbackId, response)
	
	def Tick(self):
		'''
		引擎驱动，1s30帧
		'''
		for uid, playerOne in self.mPlayerDict.iteritems():
			playerOne.Tick()
		for guildId, guildOne in self.mGuildDict.iteritems():
			guildOne.Tick()
			attrsToSync = guildOne.GetAttrsToSync()
			if attrsToSync:
				self.SyncGuildAttrsToClient(guildOne, attrsToSync)
				guildOne.ResetAttrs()
	
	def SavePlayerAndGuild(self):
		for playerOne in self.mPlayerDict.itervalues():
			playerOne.DoSave()
		for guildOne in self.mGuildDict.itervalues():
			guildOne.DoSave()
			
	def GetBriefGuildMes(self, serverId, callbackId, args):
		"""
		获取公会快照
		"""
		playerUid = args.get('uid')
		data = {}
		data['uid'] = playerUid  # 带上uid，同步到对应的客户端
		data['guildBrief'] = {}
		for guildId, guildOne in self.mGuildDict.items():
			data['guildBrief'][guildId] = guildOne.GetGuildBrief()
		guildConsts.GetServiceModSystem().NotifyToServerNode(serverId, guildConsts.GetGuildBriefFromServiceEvent, data)
	
	def Destroy(self):
		self.SavePlayerAndGuild()
		