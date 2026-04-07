# -*- coding: utf-8 -*-
#
import random

import mod.server.extraServerApi as serverApi
import common.system.eventConf as conf
import json

minecraftEnum = serverApi.GetMinecraftEnum()
compFactory = serverApi.GetEngineCompFactory()

class CustomRangedWeaponServer(serverApi.GetServerSystemCls()):
	def __init__(self, namespace, name):
		super(CustomRangedWeaponServer, self).__init__(namespace, name)
		self.DefineEvent('ProjectileDoHitEffectClientEvent')
		self.ListenEvent()

	def ListenEvent(self):
		self.ListenForEvent(serverApi.GetEngineNamespace(), serverApi.GetEngineSystemName(), "ProjectileDoHitEffectEvent",
		                    self, self.OnProjectileDoHitEffectEvent)
		self.ListenForEvent(serverApi.GetEngineNamespace(), serverApi.GetEngineSystemName(), "ItemReleaseUsingServerEvent",
		                    self, self.OnRangedWeaponReleaseUsingServerEvent)

	def OnRangedWeaponReleaseUsingServerEvent(self, args):
		playerId = args["playerId"]
		count, slotIndex = self.GetCustomProjectileItemInfo(playerId)
		# 物品栏中customrangedweapon:projectile数量大于0时才能发射抛射物
		if count > 0:
			comp = compFactory.CreatePos(playerId)
			pos = comp.GetPos()
			comp = compFactory.CreateProjectile(serverApi.GetLevelId())
			power = self.getLaunchPower(args['durationLeft'], args['maxUseDuration'])
			# 这里可以通过修改customrangedweapon:custom_arrow来切换不同的抛射物
			param = {
				'power': 1.6 * power
			}
			projectile_entity_id = comp.CreateProjectileEntity(playerId, "customrangedweapon:custom_arrow", param)
			if projectile_entity_id != '-1':
				self.DecreaseCustomProjectileItemCount(slotIndex, count - 1, playerId)
		else:
			print '没有足够弹药发射抛射物'
			
	def OnProjectileDoHitEffectEvent(self, args):
		# 这里可以加击中生物的特效
		self.BroadcastToAllClient('ProjectileDoHitEffectClientEvent', args)

	def GetCustomProjectileItemInfo(self, playerId):
		"""
		获取物品customrangedweapon:projectile的<数量, slotIndex>
		"""
		comp = compFactory.CreateItem(playerId)
		for i in xrange(0, 9):
			data = comp.GetPlayerItem(serverApi.GetMinecraftEnum().ItemPosType.INVENTORY, i)
			if data and data['itemName'] == 'customrangedweapon:projectile':
				return data['count'], i
		return 0, 0
	
	def DecreaseCustomProjectileItemCount(self, slotIndex, num, playerId):
		"""
		减少物品customrangedweapon:projectile的数量
		"""
		comp = compFactory.CreateItem(playerId)
		comp.SetInvItemNum(slotIndex, num)

	def getLaunchPower(self, durationLeft, maxUseDuration):
		timeHeld = maxUseDuration - durationLeft
		pow = timeHeld / 20.0
		pow = ((pow * pow) + pow * 2) / 3
		return min(pow, 1.0)