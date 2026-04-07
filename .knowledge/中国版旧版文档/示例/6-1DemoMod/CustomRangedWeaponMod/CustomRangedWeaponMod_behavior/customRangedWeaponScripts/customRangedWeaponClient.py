# -*- coding: utf-8 -*-
#

import mod.client.extraClientApi as clientApi 
import common.system.eventConf as conf

compFactory = clientApi.GetEngineCompFactory()

class CustomRangedWeaponClient(clientApi.GetClientSystemCls()):
	def __init__(self, namespace, name):
		super(CustomRangedWeaponClient, self).__init__(namespace, name)
		self.ExceededTime = 60 # 特效播放时长
		self.tickCnt = 0
		self.startUsingTick = 0
		self.isUsingItem = False # 是否正在使用物品
		self.initFov = 60 # 摄像机初始视野大小
		self.cameraComp = None
		self.particleIdDict = {} # effectId:timestand，用来定时销毁特效粒子
		self.ListenEvent()
		self.Init()

	def ListenEvent(self):
		self.ListenForEvent(conf.EngineNamespace, conf.EngineSystemName, 'OnScriptTickClient', self,
		                    self.OnScriptTickClient)
		self.ListenForEvent(conf.EngineNamespace, conf.EngineSystemName, 'ClientItemTryUseEvent', self,
		                    self.OnClientItemTryUseEvent)
		self.ListenForEvent(conf.EngineNamespace, conf.EngineSystemName, "ItemReleaseUsingClientEvent",
		                    self, self.OnRangedWeaponReleaseUsingClientEvent)
		self.ListenForEvent('CustomRangedWeapon', 'CustomRangedWeaponServer', 'ProjectileDoHitEffectClientEvent', self, 
							self.OnProjectileDoHitEffectClientEvent)

	def Init(self):
		# 初始化摄像机视野
		self.cameraComp = compFactory.CreateCamera(clientApi.GetLevelId())
		self.cameraComp.SetFov(self.initFov)
		
	def OnScriptTickClient(self):
		self.tickCnt += 1
		if self.particleIdDict:
			removeIds = []
			for id in self.particleIdDict:
				if self.tickCnt - self.particleIdDict[id] > self.ExceededTime:
					self.DestroyEntity(id)
					removeIds.append(id)
			for id in removeIds:
				del self.particleIdDict[id]

		offset = self.tickCnt - self.startUsingTick
		if self.isUsingItem:
			# 拉近摄像机镜头，可以修改speed改变拉近的速度
			speed = 0.15
			self.cameraComp.SetFov(self.initFov - offset * speed)

	def OnRangedWeaponReleaseUsingClientEvent(self, args):
		self.isUsingItem = False
		if self.initFov:
			# 恢复摄像机镜头视野
			self.cameraComp.SetFov(self.initFov)

	def OnClientItemTryUseEvent(self, args):
		if args["itemName"] == "customrangedweapon:bow" or args["itemName"] == "customrangedweapon_cross:bow":
			# control camera
			self.isUsingItem = True
			self.startUsingTick = self.tickCnt

	def OnProjectileDoHitEffectClientEvent(self, args):
		if args['hitTargetType'] == "ENTITY":
			self.CreateSfx(args)
		elif args['hitTargetType'] == "BLOCK":
			self.createParticle(args)

	def CreateSfx(self, args):
		# 播放序列帧动画，60 tick销毁
		pos = (args['x'], args['y'], args['z'])
		frameEntityId = self.CreateEngineSfx("textures/sfxs/buff_hongse")
		self.particleIdDict[frameEntityId] = self.tickCnt
		frameAniTransComp = compFactory.CreateFrameAniTrans(frameEntityId)
		frameAniTransComp.SetPos(pos)
		frameAniTransComp.SetRot((0,0,0))
		frameAniTransComp.SetScale((1,1,1))
		frameAniControlComp = compFactory.CreateFrameAniControl(frameEntityId)
		frameAniControlComp.Play()

	def createParticle(self, args):
		# 播放粒子特效，60 tick销毁
		pos = (args['x'], args['y'], args['z'])
		particleEntityId = self.CreateEngineParticle("effects/equip_fire.json", pos)
		self.particleIdDict[particleEntityId] = self.tickCnt
		particleControlComp = compFactory.CreateParticleControl(particleEntityId)
		particleControlComp.Play()
