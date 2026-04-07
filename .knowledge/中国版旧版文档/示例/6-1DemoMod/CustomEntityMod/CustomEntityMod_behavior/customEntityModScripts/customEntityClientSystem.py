# -*- coding: utf-8 -*-
#
import mod.client.extraClientApi as clientApi

compFactory = clientApi.GetEngineCompFactory()

class CustomEntityClientSystem(clientApi.GetClientSystemCls()):

	def __init__(self, namespace, name):
		super(CustomEntityClientSystem, self).__init__(namespace, name)
		self.mRotatingDict = {} # entityId:boolean
		self.mUseCustomMaterialDict = {} # entityId:boolean
		# 控制玩家材质切换的变量
		self.queryIsCustomMaterial = 'query.mod.is_custom_material'
		comp = compFactory.CreateQueryVariable(clientApi.GetLevelId())
		result = comp.Register(self.queryIsCustomMaterial, 0.0)
		# 控制松鼠动画切换的变量
		self.queryIsMoving = 'query.mod.is_moving'
		result = comp.Register(self.queryIsMoving, 0.0)
		# 控制松鼠渲染控制器变化的变量
		self.queryIsEnchanted = 'query.mod.is_enchanted'
		result = comp.Register(self.queryIsEnchanted, 0.0)
		# 注册玩家move.legs和move.arms动作控制变量
		comp.Register("query.mod.rn_anim_index", 0)

		self.DefineEvent("ShowMsgEvent")
		self.ListenEvent()
		self.alreadyChangePlayerMaterialDict = {} # playerId:boolean
		self.mReset = False
		self.mIsTranform = False
	
	def ListenEvent(self):
		self.ListenForEvent('customEntityMod', 'customEntityServerSystem', "ChangeMaterial",
		                    self, self.OnChangeMaterial)
		self.ListenForEvent(clientApi.GetEngineNamespace(), clientApi.GetEngineSystemName(), 
			"ClientItemUseOnEvent", self, self.OnClientItemUseOnEvent)

	def OnChangeMaterial(self, args):
		entityId = args['entityId']
		comp = compFactory.CreateEngineType(entityId)
		strType = comp.GetEngineTypeStr()
		if strType == 'minecraft:player':
			if entityId not in self.alreadyChangePlayerMaterialDict:
				self.alreadyChangePlayerMaterialDict[entityId] = True
				self.ModifyPlayerMaterialDemo(entityId)
				comp = compFactory.CreateQueryVariable(entityId)
				comp.Set(self.queryIsCustomMaterial, 1.0)
			else:
				del self.alreadyChangePlayerMaterialDict[entityId]
				comp = compFactory.CreateQueryVariable(entityId)
				result = comp.Set(self.queryIsCustomMaterial, 0.0)
				self.ResetPlayerMaterial(entityId)
		elif strType == 'netease:squirrel':
			if entityId not in self.mRotatingDict:
				self.mRotatingDict[entityId] = True
				self.ModifySquirrelRender(entityId)
				comp = compFactory.CreateQueryVariable(entityId)
				result = comp.Set(self.queryIsMoving, 1.0)
				result = comp.Set(self.queryIsEnchanted, 1.0)
			else:
				self.ResetSquirrelRender(entityId)
				del self.mRotatingDict[entityId]
				comp = compFactory.CreateQueryVariable(entityId)
				result = comp.Set(self.queryIsMoving, 0.0)
				result = comp.Set(self.queryIsEnchanted, 0.0)
	
	# 修改玩家的渲染控制器
	def ModifyPlayerMaterialDemo(self, entityId):
		comp = compFactory.CreateActorRender(entityId)
		# 删除存在的渲染控制器，定义在player.entity.json和player.render_controllers.json中
		comp.RemovePlayerRenderController('controller.render.player.third_person')
		comp.RemovePlayerRenderController('controller.render.player.map')
		comp.RemovePlayerRenderController('controller.render.player.first_person_bloom')
		comp.RemovePlayerRenderController('controller.render.player.third_person_bloom')
		# 增加自定义的材质
		result = comp.AddPlayerRenderMaterial('custom_player_key', 'custom_player_bloom')
		
		# 增加自定义的渲染控制器，定义在player_custom.render_controllers.json和player_custom1.render_controllers.json中
		# query.mod.is_custom_material需要提前通过queryVariable组件进行注册
		result = comp.AddPlayerRenderController('controller.render.player_custom', '!variable.is_first_person && query.mod.is_custom_material')
		result = comp.AddPlayerRenderController('controller.render.player_custom1', '!variable.is_first_person && !query.mod.is_custom_material')
		# 重建渲染控制器，调用RemovePlayerRenderController、AddPlayerRenderMaterial、AddPlayerRenderController
		# 任意一个函数之后需要调用RebuildPlayerRender才能使修改生效
		result = comp.RebuildPlayerRender()

	# 重置玩家的渲染控制器
	def ResetPlayerMaterial(self, entityId):
		comp = compFactory.CreateActorRender(entityId)
		# 删除自定义的渲染控制器
		result = comp.RemovePlayerRenderController('controller.render.player_custom')
		result = comp.RemovePlayerRenderController('controller.render.player_custom1')

		# 增加vanilla定义的渲染控制器
		result = comp.AddPlayerRenderController('controller.render.player.third_person', '!variable.is_first_person && !variable.map_face_icon')
		result = comp.AddPlayerRenderController('controller.render.player.map', 'variable.map_face_icon')
		result = comp.AddPlayerRenderController('controller.render.player.first_person_bloom', 'variable.is_first_person')
		result = comp.AddPlayerRenderController('controller.render.player.third_person_bloom', '!variable.is_first_person && !variable.map_face_icon')
		# 重建渲染控制器
		result = comp.RebuildPlayerRender()
	
	# 修改松鼠（对该类生物都生效）的渲染控制
	def ModifySquirrelRender(self, entityId):
		comp = compFactory.CreateActorRender(entityId)
		actorIdentifier = 'netease:squirrel'
		# 删除默认的渲染控制器
		result = comp.RemoveActorRenderController(actorIdentifier, 'controller.render.squirrel')
		# 增加squirrel.render_controllers.json中定义的但是没有被使用的渲染控制器
		result = comp.AddActorRenderController(actorIdentifier, 'controller.render.squirrel_more')
		# 重建渲染控制器
		result = comp.RebuildActorRender(actorIdentifier)
	
	# 重置松鼠（对该类生物都生效）的渲染控制位默认值
	def ResetSquirrelRender(self, entityId):
		comp = compFactory.CreateActorRender(entityId)
		actorIdentifier = 'netease:squirrel'
		# 增加默认的渲染控制器
		result = comp.AddActorRenderController(actorIdentifier, 'controller.render.squirrel')
		# 删除新增的渲染控制器
		result = comp.RemoveActorRenderController(actorIdentifier, 'controller.render.squirrel_more')
		# 重建渲染控制器
		result = comp.RebuildActorRender(actorIdentifier)
	
	# 通过使用不同的物品来展示不同的效果
	def OnClientItemUseOnEvent(self, args):
		if self.mIsTranform:
			self.ShowMsg("切换中，请稍后再试")
			return

		if args["itemName"] == "minecraft:apple":
			self.ChangePlayerRenderMaterial(args["entityId"])
			args["ret"] = True
		elif args["itemName"] == "minecraft:egg":
			self.ChangePlayerAnimationMoveLegs(args["entityId"])
			args["ret"] = True
		elif args["itemName"] == "minecraft:snowball":
			self.ChangePlayerAnimationMoveArms(args["entityId"])
			args["ret"] = True
		elif args["itemName"] == "minecraft:diamond":
			self.ChangePlayerRenderGeometry(args["entityId"])
			args["ret"] = True
		elif args["itemName"] == "minecraft:stick":
			self.ChangePlayerAnimation(args["entityId"])
			args["ret"] = True

	# 改变本地玩家的渲染几何体（把玩家变身定身僵尸，因为动作与几何体有关，只改变几何体和贴图会导致原来的动画失效）
	def ChangePlayerRenderGeometry(self, entityId):
		actorRenderComp = compFactory.CreateActorRender(entityId)
		actorRenderComp.AddPlayerGeometry("default", "geometry.zombie.v1.8")
		actorRenderComp.AddPlayerTexture("default", "textures/entity/zombie/zombie")
		actorRenderComp.RebuildPlayerRender()
		def reset():
			actorRenderComp.AddPlayerGeometry("default", "geometry.humanoid.custom")
			actorRenderComp.AddPlayerTexture("default", "textures/entity/steve")
			actorRenderComp.RebuildPlayerRender()
			self.mIsTranform = False
			self.ShowMsg("恢复默认玩家渲染几何体")

		comp = compFactory.CreateGame(clientApi.GetLevelId())
		comp.AddTimer(3.0, reset)
		self.mIsTranform = True
		self.ShowMsg("切换玩家渲染几何体中")

	
	# 改变本地玩家的渲染材质
	def ChangePlayerRenderMaterial(self, entityId):
		actorRenderComp = compFactory.CreateActorRender(entityId)
		actorRenderComp.AddPlayerRenderMaterial("default", "custom_entity")
		actorRenderComp.RebuildPlayerRender()
		def reset():
			actorRenderComp.AddPlayerRenderMaterial("default", "entity_alphatest")
			actorRenderComp.RebuildPlayerRender()
			self.mIsTranform = False
			self.ShowMsg("恢复默认玩家渲染材质")

		comp = compFactory.CreateGame(clientApi.GetLevelId())
		comp.AddTimer(3.0, reset)
		self.mIsTranform = True
		self.ShowMsg("切换玩家渲染材质中")
	
	# 改变玩家的动画控制流程move.arms
	# 正常情况下玩家行走就会播放move.arms动画，目前通过在json中增加了query.mod.rn_anim_index控制该动作
	def ChangePlayerAnimationMoveArms(self, entityId):
		comp = compFactory.CreateQueryVariable(entityId)
		comp.Set("query.mod.rn_anim_index", 1)
		self.ShowMsg("运行播放动作move.arms")

	# 改变玩家的动画控制流程move.legs
	# 正常情况下玩家行走就会播放move.legs动画，目前通过在json中增加了query.mod.rn_anim_index控制该动作
	def ChangePlayerAnimationMoveLegs(self, entityId):
		comp = compFactory.CreateQueryVariable(entityId)
		comp.Set("query.mod.rn_anim_index", 2)
		self.ShowMsg("允许播放动作move.legs")
	
	# 改变move.arms动作的幅度
	def ChangePlayerAnimation(self, entityId):
		actorRenderComp = compFactory.CreateActorRender(entityId)
		actorRenderComp.AddPlayerAnimation("move.arms", "animation.player.custom.move.arms")
		self.ShowMsg("修改动作move.arms左右手的rotation值，详见player.custom.animation.json")
	
	def ShowMsg(self, msg):
		self.NotifyToServer("ShowMsgEvent", {"msg": msg, "playerId": clientApi.GetLocalPlayerId()})

	# 初始化玩家的特效设置（第三人称下）
	def InitPlayerParticleEffect(self):
		actorRenderComp = compFactory.CreateActorRender(clientApi.GetLocalPlayerId())
		actorRenderComp.AddPlayerParticleEffect("nectar_dripping", "minecraft:nectar_drip_particle")
		actorRenderComp.AddPlayerAnimationController("controller__drip", "controller.animation.player.drip")
		actorRenderComp.AddPlayerAnimationIntoState("root", "third_person", "controller__drip")
		actorRenderComp.RebuildPlayerRender()
		comp = clientApi.GetEngineCompFactory().CreateQueryVariable(clientApi.GetLocalPlayerId())
		comp.Register('query.mod.play_drip', 0.0)

	# 初始化生物的特效设置
	def InitActorParticleEffect(self, entityId, actorIdentifier):
		actorRenderComp = compFactory.CreateActorRender(entityId)
		actorRenderComp.AddActorParticleEffect(actorIdentifier, "nectar_dripping", "minecraft:nectar_drip_particle")
		actorRenderComp.AddActorAnimationController(actorIdentifier, "controller__drip", "controller.animation.player.drip")
		actorRenderComp.AddActorScriptAnimate(actorIdentifier, "controller__drip")
		comp = clientApi.GetEngineCompFactory().CreateQueryVariable(entityId)
		comp.Register('query.mod.play_drip', 0.0)

	# 播放动态添加的特效nectar_dripping
	def PlayParticleEffect(self):
		comp = clientApi.GetEngineCompFactory().CreateQueryVariable(clientApi.GetLocalPlayerId())
		comp.Set('query.mod.play_drip', 1.0)

	# 停止播放动态添加的特效nectar_dripping
	def StopParticleEffect(self):
		comp = clientApi.GetEngineCompFactory().CreateQueryVariable(clientApi.GetLocalPlayerId())
		comp.Set('query.mod.play_drip', 0.0)