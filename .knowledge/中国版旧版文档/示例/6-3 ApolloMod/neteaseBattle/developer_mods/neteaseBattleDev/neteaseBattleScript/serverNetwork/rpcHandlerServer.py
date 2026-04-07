# -*- coding:utf-8 -*-

import neteaseBattleScript.battleCommon.battleConsts as battleConsts
import neteaseBattleScript.battleCommon.apiUtil as apiUtil
from neteaseBattleScript.battleCommon.battleConsts import SInterEvent

class RpcHandlerServer(object):
	def ClientEnter(self, playerId):
		configDict = {}
		for keyname in battleConsts.ConfigurablePostToClient:
			value = getattr(battleConsts, keyname)
			configDict[keyname] = value
		apiUtil.GetServerSystem().GetRpcUtil().ClientRpc(playerId).SyncConfig(battleConsts.ModVersion, configDict)
		# 分包发送entity的静态数据配置
		tmpAttrs = {}
		for name, attrMap in battleConsts.EntityAttrs.iteritems():
			tmpAttrs[name] = attrMap
			if len(tmpAttrs) >= 2:
				apiUtil.GetServerSystem().GetRpcUtil().ClientRpc(playerId).SyncEntityStatic(tmpAttrs)
				tmpAttrs = {}
		if tmpAttrs:
			apiUtil.GetServerSystem().GetRpcUtil().ClientRpc(playerId).SyncEntityStatic(tmpAttrs)
		# 分包发送equip的静态数据配置
		tmpAttrs = {}
		for name, attrMap in battleConsts.EquipAttrs.iteritems():
			tmpAttrs[name] = attrMap
			if len(tmpAttrs) >= 2:
				apiUtil.GetServerSystem().GetRpcUtil().ClientRpc(playerId).SyncEquipStatic(tmpAttrs)
				tmpAttrs = {}
		if tmpAttrs:
			apiUtil.GetServerSystem().GetRpcUtil().ClientRpc(playerId).SyncEquipStatic(tmpAttrs)
		# 客户端登录成功
		apiUtil.GetServerSystem().GetEventMgr().NotifyEvent(SInterEvent.ClientEnter, {"playerId":playerId})

	def NotifyPlayerGetItem(self, playerId, actor):
		apiUtil.GetServerSystem().GetEventMgr().NotifyEvent(SInterEvent.ClientGetItem, {"playerId": playerId, "actor":actor})

	def NotifyPlayerBagRefresh(self, playerId):
		apiUtil.GetServerSystem().DeclareBagChanged(playerId)

	def DeclearInterest(self, playerId, addIds, discardIds):
		apiUtil.GetServerSystem().GetEventMgr().NotifyEvent(SInterEvent.ClientDeclearInterest,
			{"playerId": playerId, "addIds":addIds, "discardIds":discardIds})

	def ChangeEquipAction(self, playerId, part, invSlot):
		apiUtil.GetServerSystem().GetEventMgr().NotifyEvent(SInterEvent.ClientEquipAction,
			{"playerId": playerId, "part":part, "invSlot":invSlot})

	def ExChangeBagSlot(self, playerId, slot1, slot2):
		apiUtil.GetServerSystem().GetEventMgr().NotifyEvent(SInterEvent.ExchangeBagItem,
			{"playerId": playerId, "slot1": slot1, "slot2": slot2})


