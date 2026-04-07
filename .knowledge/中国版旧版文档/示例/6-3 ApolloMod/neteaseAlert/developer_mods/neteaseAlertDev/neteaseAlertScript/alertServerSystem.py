# -*- coding: utf-8 -*-

# import lobbyGame.netgameApi as netgameApi
# import apolloCommon.commonNetgameApi as commonNetgameApi
import logout
import neteaseAlertScript.alertConst as alertConst
import server.extraServerApi as serverApi
import netgame.apolloCommon.commonNetgameApi as commonNetgameApi
import lobbyGame.netgameApi as netgameApi

ServerSystem = serverApi.GetServerSystemCls()

class AlertServerSystem(ServerSystem):
	def __init__(self, namespace, systemName):
		ServerSystem.__init__(self, namespace, systemName)
		self.ListenForEvent(alertConst.ModName, alertConst.ClientSystemName, alertConst.ClientUiInitFinished, self, self.OnClientUiInitFinished)

		self.modConfig = commonNetgameApi.GetModJsonConfig('neteaseAlertScript')
		self.mDefaultShowTime = self.modConfig["default_show_time"]
		self.mXRatio = self.modConfig["default_xratio"]
		self.mYRatio = self.modConfig["default_yratio"]

	def Destroy(self):
		pass

	def Update(self):
		pass

	def OnClientUiInitFinished(self, args):
		playerId = args.get("entityId")
		self.NotifyToClient(playerId, alertConst.ModConfigResponseFromServerEvent, self.modConfig)

	def Alert(self, playerId, text, seconds=None, xratio=None, yratio=None, priority=-1):
		"""
		提供一个函数供外部调用
		用于调用客户端的提示文本UI弹出并显示一些提示文字于指定的位置
		:param playerId: 玩家的playerId
		:param text: 提示文本字符串
		:param seconds: 需要停留的秒数
		:param xratio: 文本框中心点于屏幕横轴方向的偏移百分比，取值为0到1间的小数
		:param yratio: 文本框中心点于屏幕纵轴方向的偏移百分比，取值为0到1间的小数
		:param priority: 显示优先级
		"""
		seconds = seconds if seconds != None else self.mDefaultShowTime
		xratio = xratio if xratio != None else self.mXRatio
		yratio = yratio if yratio != None else self.mYRatio
		if isinstance(seconds, int) and seconds > 0:
			self.NotifyToClient(playerId, alertConst.NewAlertEvent, {  # 通知该玩家的客户端创建一个弹出提示文本的任务
				'text': text,
				'seconds': seconds,
				'xratio': xratio,
				'yratio': yratio,
				'priority': priority
			})
