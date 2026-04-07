# -*- coding: utf-8 -*-

import client.extraClientApi as extraClientApi
ClientSystem = extraClientApi.GetClientSystemCls()
from neteaseBattleScript.battleCommon.battleConsts import ModNameSpace, ServerSystemName
from neteaseBattleScript.battleCommon.battleConsts import ServerSpecEvent, CInterEvent
import neteaseBattleScript.battleCommon.battleConsts as battleConsts
from neteaseBattleScript.clientNetwork.rpcClient import RpcClient
from neteaseBattleScript.battleCommon.eventMgr import EventManger
from neteaseBattleScript.battleGameObjMgrClient import GameObjMgrClient
from neteaseBattleScript.mgr.uiMgr import UIMgr
from neteaseBattleScript.ui.uiDef import UIDef

class BattleClientSystem(ClientSystem):
	"""
	该mod的客户端类
	战斗插件有大量的属性由服务端同步下来
	主要由GameObjMgr进行游戏对象（实体、弹射物等）的管理
	还使用rpc的封装与本地的事件系统EventManger来各自进行与服务器的交互和本地其他模块的交互
	"""
	def __init__(self, namespace, systemName):
		ClientSystem.__init__(self, namespace, systemName)
		self.mFrameCnt = 0
		self.mPlayerId = extraClientApi.GetLocalPlayerId()  # 获取客户端本地玩家的playerId
		self.mUIMgr = UIMgr()
		self.mRpcClient = RpcClient()  # Rpc工具类
		self.mEventMgr = EventManger()  # 事件系统
		self.mGameObjMgr = GameObjMgrClient()  # 客户端“游戏对象”管理器，是本mod的核心

	def Init(self):
		self.RegisterClientEvent("UiInitFinished", self, self.OnUiInitFinished)  # 在此处可以创建该mod的ui
		self.RegisterModClientEvent(ServerSpecEvent.RpcEvent, self, self.OnServerRpc)  # 其实这是rpc的一个入口，定义一个事件并在modsdk提供的通信中运作，接收方法名与参数即可调用本地的方法
		self.mGameObjMgr.Init()  # 游戏对象管理类初始化

	def Destroy(self):
		self.mUIMgr.Destroy()
		self.mEventMgr.Destroy()
		self.mGameObjMgr.Destroy()
		self.UnRegisterClientEvent("UiInitFinished", self, self.OnUiInitFinished)
		self.UnRegisterModClientEvent(ServerSpecEvent.RpcEvent, self, self.OnServerRpc)
		ClientSystem.Destroy(self)

	# 被引擎直接执行的父类的重写函数，引擎会执行该Update回调，1秒钟30帧
	def Update(self):
		self.mFrameCnt += 1  # 设置一个计数，可用于计算某些逻辑第多少帧可以执行
		self.mGameObjMgr.Tick(self.mFrameCnt)
	#--------------------------------------------------------------------------------------
	def OpenStatusUi(self):
		self.mEventMgr.NotifyEvent(CInterEvent.UIStatusOpen, {"guid":self.mPlayerId})

	def GetEquipAttrDict(self, itemName, auxValue):
		return battleConsts.GetEquipCustomAttr(itemName, auxValue)

	def GetFormatAttr(self, attrName, attrValue):
		ret = battleConsts.FormatSingleAttr(attrName, attrValue, plus="", zero=1)
		if ret is None:
			return "", ""
		return ret
	#--------------------------------------------------------------------------------------
	def HideHealthAndHunger(self):
		pass

	def RegisterClientEvent(self, eventName, instance, func):
		self.ListenForEvent(extraClientApi.GetEngineNamespace(), extraClientApi.GetEngineSystemName(), eventName, instance, func)

	def RegisterModClientEvent(self, eventName, instance, func):
		self.ListenForEvent(ModNameSpace, ServerSystemName, eventName, instance, func)

	def RegisterInterEvent(self, eventId, func):
		self.mEventMgr.RegisterEvent(eventId, func)

	def UnRegisterClientEvent(self, eventName, instance, func):
		self.UnListenForEvent(extraClientApi.GetEngineNamespace(), extraClientApi.GetEngineSystemName(), eventName, instance, func)

	def UnRegisterModClientEvent(self, eventName, instance, func):
		self.UnListenForEvent(ModNameSpace, ServerSystemName, eventName, instance, func)

	def UnRegisterInterEvent(self, eventId, func):
		self.mEventMgr.UnRegisterEvent(eventId, func)
	# --------------------------------------------------------------------------------------
	def GetRpcUtil(self):
		"""
		RPC工具，发送rpc只需要 GetRpcUtil().ServerRpc().func() 就可以调用服务端的rpcHandler的func()
		:return:
		"""
		return self.mRpcClient

	def GetEventMgr(self):
		"""
		返回事件系统
		:return:
		:rtype: neteaseBattleScript.battleCommon.eventMgr.EventManger
		"""
		return self.mEventMgr

	def GetObjMgr(self):
		return self.mGameObjMgr
	# --------------------------------------------------------------------------------------
	def GetUIMgr(self):
		"""
		返回UI管理器
		:return:
		:rtype: neteaseBattleScript.mgr.uiMgr.UIMgr
		"""
		return self.mUIMgr
	# --------------------------------------------------------------------------------------
	def OnUiInitFinished(self, data):
		print "OnUiInitFinished"
		self.mUIMgr.Init()
		self.mRpcClient.ServerRpc().ClientEnter(self.mPlayerId)
		self.mEventMgr.NotifyEvent(CInterEvent.UIInitFinish, {})
		self.HideHealthAndHunger()

	def OnServerRpc(self, data):
		methodName = data['method']
		args = data['args']
		self.mRpcClient.Handle(methodName, args)

