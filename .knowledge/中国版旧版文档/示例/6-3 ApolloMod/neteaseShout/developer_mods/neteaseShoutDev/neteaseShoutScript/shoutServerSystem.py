# -*- coding: utf-8 -*-

import lobbyGame.netgameApi as netgameApi
import apolloCommon.commonNetgameApi as commonNetgameApi
import logout
import neteaseShoutScript.shoutConst as shoutConst
import server.extraServerApi as serverApi

ServerSystem = serverApi.GetServerSystemCls()


class ShoutServerSystem(ServerSystem):
	def __init__(self, namespace, systemName):
		ServerSystem.__init__(self, namespace, systemName)
		self.mDebut = False
		if not self.InitShoutCfg():
			return

		self.ListenForEvent(serverApi.GetEngineNamespace(), serverApi.GetEngineSystemName(), 'AddServerPlayerEvent', self, self.OnAddServerPlayer)
		self.ListenForEvent(shoutConst.ModName, shoutConst.ClientSystemName, shoutConst.PlayerAiringEvent, self, self.OnPlayerAiring)

		self.ListenForEvent(shoutConst.ModName, shoutConst.ServiceSystemName, shoutConst.NewMsgEvent, self, self.OnNewMsg)

	def Debut(self):
		self.mDebut = True

	def InitShoutCfg(self):
		cfg = commonNetgameApi.GetModJsonConfig("neteaseShoutScript")
		if not cfg:
			logout.error("nothing in InitShoutCfg")
			return False
		self.mContentFrameTextures = cfg['kinds']
		self.mContentWordCountLimit = cfg['wc']
		return True

	def Destroy(self):
		self.UnListenForEvent(serverApi.GetEngineNamespace(), serverApi.GetEngineSystemName(), 'AddServerPlayerEvent', self, self.OnAddServerPlayer)
		self.UnListenForEvent(shoutConst.ModName, shoutConst.ClientSystemName, shoutConst.PlayerAiringEvent, self, self.OnPlayerAiring)

		self.UnListenForEvent(shoutConst.ModName, shoutConst.ServiceSystemName, shoutConst.NewMsgEvent, self, self.OnNewMsg)

	def OnAddServerPlayer(self, data):
		"""
		第一个玩家登陆时，向service发送一条特殊的【发送喇叭消息】的事件，用于向service声明自己是个有效server进程，需要接受来自service的喇叭推送事件
		"""
		if not self.mDebut:
			self.RequestToService(
				shoutConst.ModName,
				shoutConst.PlayerAiringEvent,
				{'activate': 1},
				lambda rtn, data: rtn and self.Debut(),
			)

	def ShoutServerRender(self, playerId, eventName, respData):
		"""
		来自service的发送喇叭消息的回应，失败时显示失败理由
		"""
		print playerId, eventName, respData
		if eventName == shoutConst.PlayerAiringEvent:
			if respData['code'] == shoutConst.RespCodeSuccess:
				pass
			elif respData['message']:
				comp = self.CreateComponent(playerId, 'Minecraft', 'command')
				comp.SetCommand('tellraw @s {"rawtext": [{"text": "%s"}]}' % '§c{}'.format(respData['message']), playerId)

	def OnNewMsg(self, msg):
		"""
		来自service的群体推送的一条喇叭消息，需要转发给client
		"""
		print 'OnNewMsg', msg
		msg['bg'] = self.mContentFrameTextures[msg.get('bg', 0)]
		self.BroadcastToAllClient(shoutConst.NewMsgEvent, msg)

	def OnPlayerAiring(self, data):
		"""
		来自客户端的操作：【发送一条喇叭消息】，检查是否被禁言后转发给service
		"""
		print 'OnPlayerAiring', data
		playerId = data.get("playerId", "-1")
		uid = netgameApi.GetPlayerUid(playerId)
		if not uid:
			print 'can not get uid by playerId: %s' % playerId
			return
		comp = self.CreateComponent(playerId, "Minecraft", "name")
		name = comp.GetName()
		content = data['content']
		if netgameApi.GetUidIsSilent(uid) != 2:
			comp = self.CreateComponent(playerId, 'Minecraft', 'command')
			comp.SetCommand('tellraw @s {"rawtext": [{"text": "%s"}]}' % '§当前处于禁言状态', playerId)
			return
		if not isinstance(content, str) or len(content.decode('utf-8')) > self.mContentWordCountLimit:
			return
		priority = 1
		self.RequestToService(
			shoutConst.ModName,
			shoutConst.PlayerAiringEvent,
			{'uid': uid, 'content': content, 'priority': priority, 'name': name},
			lambda rtn, data: rtn and self.ShoutServerRender(playerId, shoutConst.PlayerAiringEvent, data),
		)

	def OpenShoutBoard(self, uid):
		"""
		驱动指定uid的client，显示输入喇叭信息的界面
		"""
		print 'OpenShoutBoard', uid
		playerId = netgameApi.GetPlayerIdByUid(uid)
		if not playerId:
			print 'can not get playerId by uid: %s' % uid
			return
		if netgameApi.GetUidIsSilent(uid) != 2:
			comp = self.CreateComponent(playerId, 'Minecraft', 'command')
			comp.SetCommand('tellraw @s {"rawtext": [{"text": "%s"}]}' % '§当前处于禁言状态', playerId)
			return
		self.NotifyToClient(playerId, shoutConst.DisplayShoutBoardEvent, {
			'wc': self.mContentWordCountLimit,
		})
