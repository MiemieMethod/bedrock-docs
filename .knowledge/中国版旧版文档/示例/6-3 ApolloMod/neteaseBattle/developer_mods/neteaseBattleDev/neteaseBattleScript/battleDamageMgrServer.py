# -*- coding: utf-8 -*-

import random
import logout
import server.extraServerApi as extraServerApi
from neteaseBattleScript.battleCommon.battleConsts import SInterEvent
import neteaseBattleScript.battleCommon.battleConsts as battleConsts
import neteaseBattleScript.battleCommon.apiUtil as apiUtil
from neteaseBattleScript.battleCommon.battleConsts import GameObjType

class DamageMgrServer(object):
	"""
	该mod的伤害计算系统
	有自定义计算伤害的规则
	监听了引擎的伤害事件和弹射物命中事件
	根据一些规则修改伤害，且增加一些逻辑，例如暴击、击退等
	死亡和生命值改变均分摊到其他tick执行
	避免了1tick同时处理过多逻辑导致卡顿
	"""
	def __init__(self):
		super(DamageMgrServer, self).__init__()
		self.mBulletDamageCauseList = (
			extraServerApi.GetMinecraftEnum().ActorDamageCause.Projectile,
		)
		self.mDirtyMobs = set()

	def Init(self):
		apiUtil.GetServerSystem().RegisterEventServer("DamageEvent", self, self.OnDamage)
		apiUtil.GetServerSystem().RegisterEventServer("ProjectileDoHitEffectEvent", self, self.OnBulletDamage)

	def Destroy(self):
		apiUtil.GetServerSystem().UnRegisterEventServer("DamageEvent", self, self.OnDamage)
		apiUtil.GetServerSystem().UnRegisterEventServer("ProjectileDoHitEffectEvent", self, self.OnBulletDamage)

	def Tick(self, frame):
		if self.mDirtyMobs:
			for guid in self.mDirtyMobs:
				mob = apiUtil.GetServerSystem().GetObjMgr().GetObject(guid)
				if not mob:
					continue
				self.CheckHpZero(mob)
			self.mDirtyMobs = set()
	#---------------------------------------------------------------------------------------
	# 自定义伤害计算
	# 伤害 = Max ( 攻击方攻击 - 防御方防御， 1 ) × 暴击影响因子 × 命中影响因子
	# 暴击时，暴击影响因子=2；非暴击时，暴击影响因子= 1。暴击的判定方式为， rand() < 攻击方暴击率时，判定暴击。
	# 命中时，命中影响因子=1；未命中时，命中影响因子=0。命中的判定方式为，rand() < ( 攻击方命中 - 防守方闪避 ) 时，判定命中，否则闪避。
	def ComputeDamage(self, actor, target):
		foe = None
		if target.GetGameObjType() == GameObjType.Player and (actor.GetGameObjType() == GameObjType.Player or actor.GetGameObjType() == GameObjType.Bullet):
			bullet = None
			if actor.GetGameObjType() == GameObjType.Bullet:
				bullet = actor
				actor = apiUtil.GetServerSystem().GetObjMgr().GetBulletSource(bullet.GetId())
			import server.extraServerApi as serverApi
			peaceSystem = serverApi.GetSystem("neteasePeace", "neteasePeaceDev")  # PVP插件对一些过滤列表内的实体需要免疫伤害
			if peaceSystem:
				import lobbyGame.netgameApi as netgameApi
				f = netgameApi.GetPlayerUid(actor.GetId())
				t = netgameApi.GetPlayerUid(target.GetId())
				if f and t:
					if peaceSystem.GetPVPMode():
						if peaceSystem.GetPVPStatus(f) or peaceSystem.GetPVPStatus(t):
							if peaceSystem.CancelDamage(actor.GetId(), f, t):
								return False, 0
						else:
							return False, 0
					elif peaceSystem.GetPVPStatus(f) and peaceSystem.GetPVPStatus(t):
						if peaceSystem.CancelDamage(actor.GetId(), f, t):
							return False, 0
					else:
						return False, 0
					foe = actor.GetId()
			if bullet is not None:
				actor = bullet

		# rand() >= (攻击方命中 - 防守方闪避)时，攻击被闪避
		if random.random() >= (actor.hit - target.dodge):
			return False, 0
		# rand() < 攻击方暴击率时，判定暴击。
		if random.random() < actor.crit:
			crit = 2.0
		else:
			crit = 1.0
		damage = max(actor.attack-target.defence, 1) * crit
		damage = int(damage)
		# 考虑到并发，治疗，同步等问题，允许短时间内Hp小于零，且死亡判定放到帧循环逻辑中处理
		target.propRecentHp -= damage
		if foe:
			setattr(target, 'foe', foe)
		elif hasattr(target, 'foe'):
			delattr(target, 'foe')
		target.SetKnockBack(power=0.5)
		self.mDirtyMobs.add(target.GetId())
		# print "%s attack %s damage=%s" % (actor, target, damage)
		apiUtil.GetServerSystem().GetObjMgr().DeclearDirty(target.GetId())
		return True, int(damage)
	#---------------------------------------------------------------------------------------
	# 普通伤害判定
	def DoDamageDefined(self, actorId, targetId):
		# 某些伤害是没有制造者的，比如说僵尸在白天被烧
		if actorId == "-1":
			return
		actor = apiUtil.GetServerSystem().GetObjMgr().GetObject(actorId)
		target = apiUtil.GetServerSystem().GetObjMgr().GetObject(targetId)
		if (not actor) or (not actor.HasHp()) or (not target) or (not target.HasHp()):
			logout.error("DoDamageDefined fail actor[id=%s obj=%s] target[id=%s, obj=%s]" % (actorId, actor, targetId, target))
			return
		isHit, damage = self.ComputeDamage(actor, target)

	# 飞射物伤害判定
	def DoBulletDamageDefined(self, actorId, bulletId, targetId):
		actor = apiUtil.GetServerSystem().GetObjMgr().GetObject(bulletId)
		target = apiUtil.GetServerSystem().GetObjMgr().GetObject(targetId)
		if (not actor) or (not target) or (not target.HasHp()):
			logout.error("DoBulletDamageDefined fail actor[id=%s obj=%s] target[id=%s, obj=%s]" % (actorId, actor, targetId, target))
			return
		isHit, damage = self.ComputeDamage(actor, target)

	# 检查Hp是否归零
	def CheckHpZero(self, mob):
		if mob.propRecentHp > 0:
			return
		# print "%s Hp is Zero" % mob
		if battleConsts.DestroyWhenHp0:
			# 默认的生命值归零事件处理  -- 死亡
			mob.SetDie()
		else:
			self.DoHpZeroDefined(mob)

	# 自定义的生命值归零事件处理 -- 需要重新实现
	def DoHpZeroDefined(self, mob):
		logout.info("mob [%s] Hp is 0" % str(mob))
	#---------------------------------------------------------------------------------------
	def OnDamage(self, data):
		# 非战斗场景
		if battleConsts.IsPeaceMode:
			data["damage"] = 0
			data["knock"] = False
			data["ignite"] = False
			return
		data["damage"] = 0
		data["knock"] = True
		actorId, targetId, cause = data["srcId"], data["entityId"], data["cause"]
		# 飞射物的伤害计算需要特殊处理
		if cause in self.mBulletDamageCauseList:
			return
		#print "OnDamage actorId=%s targetId=%s cause=%s" % (actorId, targetId, cause)
		self.DoDamageDefined(actorId, targetId)

	# 飞射物命中，用于触发飞射物伤害计算
	def OnBulletDamage(self, data):
		if data["hitTargetType"] != "ENTITY":
			return
		actorId, bulletId, targetId = data["srcId"], data["id"], data["targetId"]
		# print "OnBulletDamage actorId=%s targetId=%s bulletId=%s" % (actorId, targetId, bulletId)
		self.DoBulletDamageDefined(actorId, bulletId, targetId)


