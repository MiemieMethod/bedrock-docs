# -*- coding: utf-8 -*-
import client.extraClientApi as extraClientApi
ClientSystem = extraClientApi.GetClientSystemCls()
import neteaseRandomTpScript.randomTpConst as randomTpConst


class RandomTpClientSystem(ClientSystem):
	def __init__(self, namespace, systemName):
		ClientSystem.__init__(self,namespace,systemName)

		# server事件
		self.ListenForEvent(randomTpConst.ModName, randomTpConst.ServerSystemName, randomTpConst.ClientEvent.ReadingStarted, self, self.OnRecvReadingStarted)
		self.ListenForEvent(randomTpConst.ModName, randomTpConst.ServerSystemName, randomTpConst.ClientEvent.ReadingInterrupted, self, self.OnRecvReadingInterrupted)
		self.ListenForEvent(randomTpConst.ModName, randomTpConst.ServerSystemName, randomTpConst.ClientEvent.TpFinished, self, self.OnRecvTpFinished)

	def Destroy(self):
		# server事件
		self.UnListenForEvent(randomTpConst.ModName, randomTpConst.ServerSystemName, randomTpConst.ClientEvent.ReadingStarted, self, self.OnRecvReadingStarted)
		self.UnListenForEvent(randomTpConst.ModName, randomTpConst.ServerSystemName, randomTpConst.ClientEvent.ReadingInterrupted, self, self.OnRecvReadingInterrupted)
		self.UnListenForEvent(randomTpConst.ModName, randomTpConst.ServerSystemName, randomTpConst.ClientEvent.TpFinished, self, self.OnRecvTpFinished)

		ClientSystem.Destroy(self)

	# ----------------------------------------------------------------------------------------

	# 收到服务器事件：开始读秒
	def OnRecvReadingStarted(self, args):
		print 'OnRecvReadingStarted: ', args

	# 收到服务器事件：读秒被打断
	def OnRecvReadingInterrupted(self, args):
		print 'OnRecvReadingInterrupted: ', args

	# 收到服务器事件：完成传送
	def OnRecvTpFinished(self, args):
		print 'OnRecvTpFinished: ', args
