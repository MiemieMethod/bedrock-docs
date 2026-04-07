# -*- coding: utf-8 -*-
#
import random
import time

import client.extraClientApi as clientApi
ClientSystem = clientApi.GetClientSystemCls()

from extradata.playerExtraData import PlayerData as PlayerData

class SampleClient(ClientSystem):
	def __init__(self,namespace,systemName):
		ClientSystem.__init__(self,namespace,systemName)
		self.playerDic = {}
		self.waitLogin = 120
		self.in_matching = False
		self.last_close_menu = 0
		self.announce_frame = -1
		#
		self.DefineEvent('PlayerJoin')
		self.DefineEvent('MenuChooseOk')
		self.DefineEvent('PlayerMatchSucRec')
		#
		self.ListenForEvent('Minecraft', 'SampleServer', 'updatePlayerExtraData', self, self.OnUpdateExtraData)
		self.ListenForEvent('Minecraft', 'SampleServer', 'showMenuPanel', self, self.OnShowMenuPanel)
		self.ListenForEvent('Minecraft', 'SampleServer', 'showRanking', self, self.OnShowRanking)
		self.ListenForEvent('Minecraft', 'SampleServer', 'MasterAnnounceEvent', self, self.OnMasterAnnounce)
		self.ListenForEvent('Minecraft', 'SampleServer', 'MasterPlayerMatchingStatus', self, self.OnPlayerMatchingStatus)
		self.ListenForEvent('Minecraft', 'SampleServer', 'MasterPlayerMatchingResult', self, self.OnPlayerMatchingResult)
		self.ListenForEvent(clientApi.GetEngineNamespace(), clientApi.GetEngineSystemName(), 'OnScriptTickClient', self, self.onScriptTick)
		self.ListenForEvent(clientApi.GetEngineNamespace(), clientApi.GetEngineSystemName(), 'UiInitFinished', self, self.onUiInitFinished)
		
		
	def Destroy(self):
		self.UnListenForEvent('Minecraft', 'SampleServer', 'updatePlayerExtraData', self, self.OnUpdateExtraData)
		self.UnListenForEvent('Minecraft', 'SampleServer', 'showMenuPanel', self, self.OnShowMenuPanel)
		self.UnListenForEvent('Minecraft', 'SampleServer', 'MasterAnnounceEvent', self, self.OnMasterAnnounce)
		self.UnListenForEvent('Minecraft', 'SampleServer', 'MasterPlayerMatchingStatus', self, self.OnPlayerMatchingStatus)
		self.UnListenForEvent('Minecraft', 'SampleServer', 'MasterPlayerMatchingResult', self, self.OnPlayerMatchingResult)
		self.UnListenForEvent(clientApi.GetEngineNamespace(), clientApi.GetEngineSystemName(), 'OnScriptTickClient', self, self.onScriptTick)
		self.UnListenForEvent(clientApi.GetEngineNamespace(), clientApi.GetEngineSystemName(), 'UiInitFinished', self, self.onUiInitFinished)
	
	def onUiInitFinished(self, data):
		print "======================================onUiInitFinished"
		clientApi.RegisterUI("mainUi","sample.mainUi.MainUi","mainUi.main")
		clientApi.CreateUI(clientApi.GetScreenDef("mainUi"), {"inputMode": 0})
		mainUi = clientApi.GetUI(clientApi.GetScreenDef("mainUi"))
		if mainUi:
			mainUi.initUi()
	
	def onScriptTick(self):
		if self.waitLogin >= 0:
			self.waitLogin -= 1
			if self.waitLogin == 0:
				self.requestLogin()
		if self.announce_frame >= 0:
			self.announce_frame -= 1
			if self.announce_frame == 0:
				self.OnHideMasterAnnounce()
				
	def requestLogin(self):
		print "===============================requestLogin"
		data  = self.CreateEventData()
		data["id"] = clientApi.GetLocalPlayerId()
		self.NotifyToServer("PlayerJoin", data)
	
	def OnUpdateExtraData(self, data):
		print "OnUpdateExtraData", data
		playerId = data["id"]
		player_data = self.playerDic.get(playerId, None)
		if player_data is None:
			player_data = PlayerData(playerId, data["exp"], data["level"])
			self.playerDic[playerId] = player_data
		else:
			player_data.update_from_server(data["exp"], data["level"])
		print "player extra changed exp=%s level=%s" % (player_data.exp, player_data.level)
	#--------------------------------------------------------------------------------------
	def OnMasterAnnounce(self, args):
		print "=====OnMasterAnnounce", args
		mainUi = clientApi.GetUI(clientApi.GetScreenDef("mainUi"))
		if not mainUi:
			return
		mainUi.show_center_message(args['message'])
		self.announce_frame = 240
	
	def OnHideMasterAnnounce(self):
		mainUi = clientApi.GetUI(clientApi.GetScreenDef("mainUi"))
		if not mainUi:
			return
		mainUi.hide_center_message()
	#--------------------------------------------------------------------------------------
	def OnShowRanking(self, data):
		if time.time() - self.last_close_menu < 2:
			return
		import random
		print "OnShowRanking", data
		mainUi = clientApi.GetUI(clientApi.GetScreenDef("mainUi"))
		if not mainUi:
			return
		if mainUi.IsRankingShow():
			return
		if not data['exist']:
			message = "尚未获取到排行榜信息，请稍后重试！"
			mainUi.show_center_message(message)
			self.announce_frame = 120
			return
		mainUi.show_ranking_panel(self.close_menu, "积分排行榜", data['cache'])
	#--------------------------------------------------------------------------------------
	def OnShowMenuPanel(self, data):
		print "OnShowMenuPanel", data
		if time.time() - self.last_close_menu < 2:
			return
		mainUi = clientApi.GetUI(clientApi.GetScreenDef("mainUi"))
		if not mainUi:
			return
		if mainUi.IsMenuShow():
			return
		if data["menuKey"] == "trans2game":
			self.show_trans2game_menu(mainUi)
		elif data["menuKey"] == "trans2lobby":
			self.show_trans2lobby_menu(mainUi)
		elif data["menuKey"] == "trans2fps":
			self.show_trans2fps_menu(mainUi)
		elif data["menuKey"] == "match":
			self.show_match_menu(mainUi)
	
	def close_menu(self):
		self.last_close_menu = time.time()
	
	def show_trans2game_menu(self, mainUi):
		mainUi.showMenuPanel(self.do_goto_game, self.close_menu, "确定要前往生存服吗？", "前往", "放弃")
	
	def do_goto_game(self):
		print "do_goto_game"
		self.last_close_menu = time.time()
		data  = self.CreateEventData()
		data["id"] = clientApi.GetLocalPlayerId()
		data['menuKey'] = "trans2game"
		self.NotifyToServer("MenuChooseOk", data)
	
	def show_trans2lobby_menu(self, mainUi):
		mainUi.showMenuPanel(self.do_goto_lobby, self.close_menu, "确定要返回主城吗？", "返回主城", "放弃")
	
	def do_goto_lobby(self):
		print "do_goto_lobby"
		self.last_close_menu = time.time()
		data  = self.CreateEventData()
		data["id"] = clientApi.GetLocalPlayerId()
		data['menuKey'] = "trans2lobby"
		self.NotifyToServer("MenuChooseOk", data)
	
	def show_trans2fps_menu(self, mainUi):
		mainUi.showMenuPanel(self.do_goto_fps, self.close_menu, "确定要前往恶魔手套吗？", "前往", "放弃")
	
	def do_goto_fps(self):
		print "do_goto_fps"
		self.last_close_menu = time.time()
		data  = self.CreateEventData()
		data["id"] = clientApi.GetLocalPlayerId()
		data['menuKey'] = "trans2fps"
		self.NotifyToServer("MenuChooseOk", data)
	#--------------------------------------------------------------------------------------
	# 配对
	def show_match_menu(self, mainUi):
		if self.in_matching:
			mainUi.showMenuPanel(self.do_leave_match, self.close_menu, "确定要终止配对吗？", "终止配对", "放弃")
		else:
			mainUi.showMenuPanel(self.do_goto_match, self.close_menu, "确定要开始配对吗？", "开始配对", "放弃")
		
	def do_goto_match(self):
		print "do_goto_match"
		self.last_close_menu = time.time()
		data  = self.CreateEventData()
		data["id"] = clientApi.GetLocalPlayerId()
		data['menuKey'] = "match"
		data['start'] = True
		self.NotifyToServer("MenuChooseOk", data)
	
	def do_leave_match(self):
		print "do_leave_match"
		self.last_close_menu = time.time()
		data  = self.CreateEventData()
		data["id"] = clientApi.GetLocalPlayerId()
		data['menuKey'] = "match"
		data['start'] = False
		self.NotifyToServer("MenuChooseOk", data)
	
	def OnPlayerMatchingStatus(self, args):
		print "=========OnPlayerMatchingStatus", args
		if args['suc']:
			self.in_matching = args['is_start']
			if self.in_matching:
				message = "开始配对，请耐心等待！"
			else:
				message = "配对终止！"
		else:
			message = args['reason']
		mainUi = clientApi.GetUI(clientApi.GetScreenDef("mainUi"))
		if not mainUi:
			return
		mainUi.show_center_message(message)
		self.announce_frame = 120
	
	def OnPlayerMatchingResult(self, args):
		print "=========OnPlayerMatchingResult", args
		if args['suc']:
			self.in_matching = False
			message = "配对成功，即将前往战场。。。"
			data = self.CreateEventData()
			data["id"] = clientApi.GetLocalPlayerId()
			data['serverid'] = args['serverid']
			self.NotifyToServer("PlayerMatchSucRec", data)
		else:
			self.in_matching = False
			message = args['reason']
		mainUi = clientApi.GetUI(clientApi.GetScreenDef("mainUi"))
		if not mainUi:
			return
		mainUi.show_center_message(message)
		self.announce_frame = 120
		
		
		
		