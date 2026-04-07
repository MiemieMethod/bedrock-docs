# -*- coding: utf-8 -*-
import time
import server.extraServerApi as extraServerApi
ServerSystem = extraServerApi.GetServerSystemCls()
import lobbyGame.netgameApi as netgameApi
import apolloCommon.commonNetgameApi as commonNetgameApi
import logout
import neteaseBattleScript.battleCommon.battleConsts as battleConsts
from neteaseBattleScript.battleCommon.battleConsts import  GameObjType
from neteaseBattleScript.battleCommon.battleConsts import ModNameSpace, ClientSystemName
from neteaseBattleScript.battleCommon.battleConsts import ClientSpecEvent, ServerSpecEvent
from neteaseBattleScript.serverNetwork.rpcServer import RpcServer
from neteaseBattleScript.battleCommon.eventMgr import EventManger
from neteaseBattleScript.battleGameObjMgrServer import GameObjMgrServer
from neteaseBattleScript.battleDamageMgrServer import DamageMgrServer

class BattleServerSystem(ServerSystem):
	"""
	该mod的服务端类
	战斗插件有大量的属性需要从服务端同步至客户端
	主要由GameObjMgr进行游戏对象（实体、弹射物等）的管理
	还使用rpc的封装与本地的事件系统EventManger来各自进行与客户端的交互和本地其他模块的交互
	战斗插件还有自己独立的伤害系统
	监听了引擎的伤害和弹射物命中事件以处理后续伤害逻辑
	监听了装备切换事件来处理玩家属性切换
	"""
	def __init__(self, namespace, systemName):
		ServerSystem.__init__(self, namespace, systemName)
		self.mFrame = 0
		self.mRpcServer = RpcServer()  # rpc工具
		self.mEventMgr = EventManger()  # 事件系统
		self.mGameObjMgr = GameObjMgrServer()
		self.mDamageMgr = DamageMgrServer()  # 伤害系统
		self.mEquipChangeCbIndex = 1
		self.mEquipChangeCbDict = {}

	def Init(self):
		self.mGameObjMgr.Init()
		self.mDamageMgr.Init()
		# self.RegisterEventServer("ServerChatEvent", self, self.OnChat)
		self.RegisterModClientEvent(ClientSpecEvent.RpcEvent, self, self.OnClientRpc)

	def Destroy(self):
		self.mEventMgr.Destroy()
		self.mGameObjMgr.Destroy()
		self.mDamageMgr.Destroy()
		# self.UnRegisterEventServer("ServerChatEvent", self, self.OnChat)
		self.UnRegisterModClientEvent(ClientSpecEvent.RpcEvent, self, self.OnClientRpc)
		ServerSystem.Destroy(self)

	def Update(self):
		self.mFrame += 1
		self.mGameObjMgr.Tick(self.mFrame)
		self.mDamageMgr.Tick(self.mFrame)
	# ----------------------------------------------------------------------------------------
	def RegisterPlayerAttrBaseWithLevelCallback(self, func):
		"""
		设置返回玩家指定等级属性的回调函数
		详见readme
		"""
		battleConsts.PlayerAttrBaseWithLevelCallback = func
		return True
	
	def SetPlayerAttrBaseWithLevel(self, level, extraAttrs):
		"""
		设置玩家指定等级的属性
		详见readme
		"""
		return battleConsts.SetPlayerAttrBase(level, extraAttrs)

	def SetPeaceMode(self, isPease):
		"""
		设置为和平模式
		详见readme
		"""
		battleConsts.IsPeaceMode = isPease
		return True

	def GetEquipAttrDict(self, itemName, auxValue):
		"""
		获取物品属性字典
		详见readme
		"""
		return battleConsts.GetEquipCustomAttr(itemName, auxValue)

	def GetFormatAttr(self, attrName, attrValue):
		"""
		获取属性格式化字符
		详见readme
		"""
		ret = battleConsts.FormatSingleAttr(attrName, attrValue, plus="", zero=1)
		if ret is None:
			return "", ""
		return ret

	def DeclareBagChanged(self, playerId):
		"""
		通知控件刷新背包界面物品显示
		详见readme
		"""
		if self.mGameObjMgr:
			self.mGameObjMgr.DeclareBagChanged(playerId)
		else:
			print "DeclareBagChanged with no mGameObjMgr"

	def RegisterExtraEquipChangeCallback(self, func):
		"""
		注册新增装备位装备被替换的侦听事件
		详见readme
		"""
		idx = self.mEquipChangeCbIndex
		self.mEquipChangeCbIndex += 1
		self.mEquipChangeCbDict[idx] = func
		return idx

	def CancelExtraEquipChangeCallback(self, idx):
		"""
		通知控件刷新背包界面物品显示
		详见readme
		"""
		if idx not in self.mEquipChangeCbDict:
			return
		del self.mEquipChangeCbDict[idx]

	def OnExtraEquipChanged(self, playerId, slot, oldItemDict, newItemDict):
		eventData = {
			"playerId": playerId,
			"slot": slot,
		}
		if oldItemDict:
			eventData["oldItemName"] = oldItemDict["itemName"]
			eventData["oldItemAuxValue"] = oldItemDict["auxValue"]
			eventData["oldItemModExtralId"] = oldItemDict["extraId"]
		else:
			eventData["oldItemName"] = "minecraft:air"
		if newItemDict:
			eventData["newItemName"] = newItemDict["itemName"]
			eventData["newItemAuxValue"] = newItemDict["auxValue"]
			eventData["newItemModExtralId"] = newItemDict["extraId"]
		else:
			eventData["newItemName"] = "minecraft:air"
		for idx, func in self.mEquipChangeCbDict.iteritems():
			try:
				func(eventData)
			except Exception as e:
				print "OnExtraEquipChanged call func {} failed error={}".format(func, e)
	# ------------------------------------------------------------------------------------------
	def RegisterEventServer(self, eventName, instance, func):
		self.ListenForEvent(extraServerApi.GetEngineNamespace(), extraServerApi.GetEngineSystemName(), eventName, instance, func)

	def RegisterModClientEvent(self, eventName, instance, func):
		self.ListenForEvent(ModNameSpace, ClientSystemName, eventName, instance, func)

	def RegisterInterEvent(self, eventId, func):
		self.mEventMgr.RegisterEvent(eventId, func)

	def UnRegisterEventServer(self, eventName, instance, func):
		self.UnListenForEvent(extraServerApi.GetEngineNamespace(), extraServerApi.GetEngineSystemName(), eventName, instance, func)

	def UnRegisterModClientEvent(self, eventName, instance, func):
		self.UnListenForEvent(ModNameSpace, ClientSystemName, eventName, instance, func)

	def UnRegisterInterEvent(self, eventId, func):
		self.mEventMgr.UnRegisterEvent(eventId, func)
	# ------------------------------------------------------------------------------------------
	def GetRpcUtil(self):
		"""
		RPC工具，发送rpc只需要 GetRpcUtil().RPGClientRpc(targetId).func() 就可以调用客户端的rpcHandler的func()
		:return:
		"""
		return self.mRpcServer

	def GetEventMgr(self):
		"""
		返回事件管理器
		:return:
		:rtype: neteaseBattleScript.battleCommon.eventMgr.EventManger
		"""
		return self.mEventMgr

	def GetObjMgr(self):
		"""
		返回脚本对象管理器
		:return:
		:rtype: neteaseBattleScript.battleGameObjMgrServer.GameObjMgrServer
		"""
		return self.mGameObjMgr

	def GetDamageMgr(self):
		"""
		返回伤害管理器
		:return:
		:rtype: neteaseBattleScript.battleDamageMgrServer.DamageMgrServer
		"""
		return self.mDamageMgr
	# ------------------------------------------------------------------------------------------
	def OnClientRpc(self, data):
		methodName = data['method']
		args = data['args']
		self.mRpcServer.Handle(methodName, args)

	# 调试用
	def OnChat(self, data):
		playerId = data["playerId"]
		messages = data['message'].split()
		command = messages[0]
		params = messages[1:]
		print "OnChat", command, params
		if command == "additem":
			self.DoAddItem(playerId, params[0], auxValue=int(params[1]))
		if command == "@op":
			if battleConsts.CanUseShowInfo and params[0] == "showinfo":
				self.DoScanEntityAttrs(playerId)

	# 把物品放进背包
	def DoAddItem(self, playerId, name, count=1, auxValue=0):
		comp = extraServerApi.CreateComponent(playerId, 'Minecraft', 'item')
		if not comp:
			return
		slot = self.GetEmptySlot(playerId)
		if slot is None:
			return
		itemDict = {
			'itemName': name,
			'count': count,
			'enchantData': [],
			'auxValue': auxValue,
			'customTips': '',
			'extraId': ''
		}
		comp.SpawnItemToPlayerInv(itemDict, playerId, slot)
		self.mRpcServer.ClientRpc(playerId).DoAddItemFromCommand(itemDict)

	def DoScanEntityAttrs(self, playerId):
		posComp = self.CreateComponent(playerId, "Minecraft", "pos")
		if not posComp:
			self.ResponseEntityAttrs(playerId, [])
			return
		pos = posComp.GetPos()
		if not pos or pos == (0,0,0):
			self.ResponseEntityAttrs(playerId, [])
			return
		startPos = (pos[0]-5, pos[1]-5, pos[2]-5)
		endPos = (pos[0]+5, pos[1]+5, pos[2]+5)
		ret = []
		comp = self.CreateComponent(playerId, "Minecraft", "game")
		if not comp:
			self.ResponseEntityAttrs(playerId, [])
			return
		eneityList = comp.GetEntitiesInSquareArea(playerId, startPos, endPos)
		if not eneityList:
			self.ResponseEntityAttrs(playerId, [])
			return
		self.ResponseEntityAttrs(playerId, eneityList)

	def ResponseEntityAttrs(self, playerId, eneityList):
		nameComp = self.CreateComponent(playerId, "Minecraft", "name")
		playerName = nameComp.GetName()
		comp = self.CreateComponent(playerId, "Minecraft", "msg")
		comp.SendMsg(playerName, "输出范围5以内生物属性 -- 开始")
		for guid in eneityList:
			obj = self.mGameObjMgr.GetObject(guid)
			if not obj:
				continue
			if obj.GetGameObjType() not in (GameObjType.Player, GameObjType.Mob):
				continue
			comp.SendMsg(playerName, "%s[ID:%s]的属性 -------" % (obj.mEntityName, obj.GetId()))
			propAttrs = obj.FormatStatus(trans=False)
			for name, value in propAttrs:
				comp.SendMsg(playerName, "-- %s:%s" % (name, value))
		comp.SendMsg(playerName, "输出范围5以内生物属性 -- 结束")

	# 获取一个空闲的背包位置
	def GetEmptySlot(self, playerId):
		comp = self.CreateComponent(playerId, 'Minecraft', 'item')
		for slot in xrange(36):
			item = comp.GetPlayerItem(extraServerApi.GetMinecraftEnum().ItemPosType.INVENTORY, slot)
			if not item:
				return slot
		return None

