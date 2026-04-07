# -*- coding: utf-8 -*-

import json
import lobbyGame.netgameApi as netgameApi
import server.extraServerApi as serverApi

ServerSystem = serverApi.GetServerSystemCls()


class BagServerSystem(ServerSystem):
	def __init__(self, namespace, systemName):
		ServerSystem.__init__(self, namespace, systemName)

	def sos(self, uid, f, t):
		"""
		交换物品放置的格子，修改物品堆叠状态
		Swap or Stack
		"""
		player_id = netgameApi.GetPlayerIdByUid(uid)
		if not player_id:
			return False
		if not (isinstance(f, int) and isinstance(t, int) and -1 < f < 36 and -1 < t < 36):
			return False
		comp = self.CreateComponent(player_id, 'Minecraft', 'item')
		if not comp:
			return False
		comp.SetInvItemExchange(f, t)
		return self.sync(uid)

	def sync(self, uid):
		"""
		向client同步背包中物品的信息
		"""
		player_id = netgameApi.GetPlayerIdByUid(uid)
		if not player_id:
			return False
		comp = self.CreateComponent(player_id, 'Minecraft', 'item')
		if not comp:
			return False
		inv = serverApi.GetMinecraftEnum().ItemPosType.INVENTORY
		self.NotifyToClient(player_id, 'SyncPlayerInventoryEvent', {
			'inventory': [json.dumps(comp.GetPlayerItem(inv, i)) for i in xrange(36)]
		})
		return True
