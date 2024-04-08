# `mojang-minecraft`

> 文档版本：1.21.0.20

`mojang-minecraft`模块的`0.1.0`版本，UUID为`b26a4d4c-afdf-4690-88f8-931846312678`。

/// info | 依赖
该模块依赖于以下模块：

- `@minecraft/common`|`1.0.0`|`77ec12b4-1b2b-4c98-8d34-d1cd63f849d5`
///

## 常量

/// define
`TicksPerSecond`


///

```js
static read-only TicksPerSecond = 20;
```


## 对象

/// define
`world`


///

```js
static read-only world: World;
```

/// html | div.result
//// define
`world`：[`World`](./world.md)

- 属性。


////

///


## 类

|类|描述|
|---|---|
|[`BeforeChatEvent`](./beforechatevent.md)||
|[`BeforeChatEventSignal`](./beforechateventsignal.md)||
|[`BeforeItemUseEvent`](./beforeitemuseevent.md)||
|[`BeforeItemUseEventSignal`](./beforeitemuseeventsignal.md)||
|[`BeforeItemUseOnEvent`](./beforeitemuseonevent.md)||
|[`BeforeItemUseOnEventSignal`](./beforeitemuseoneventsignal.md)||
|[`Block`](./block.md)||
|[`BlockAreaSize`](./blockareasize.md)||
|[`BlockComponent`](./blockcomponent.md)||
|[`BlockEvent`](./blockevent.md)||
|[`BlockInventoryComponent`](./blockinventorycomponent.md)||
|[`BlockInventoryComponentContainer`](./blockinventorycomponentcontainer.md)||
|[`BlockLavaContainerComponent`](./blocklavacontainercomponent.md)||
|[`BlockLiquidContainerComponent`](./blockliquidcontainercomponent.md)||
|[`BlockLocation`](./blocklocation.md)||
|[`BlockPermutation`](./blockpermutation.md)||
|[`BlockPistonComponent`](./blockpistoncomponent.md)||
|[`BlockPotionContainerComponent`](./blockpotioncontainercomponent.md)||
|[`BlockRaycastOptions`](./blockraycastoptions.md)||
|[`BlockRecordPlayerComponent`](./blockrecordplayercomponent.md)||
|[`BlockSnowContainerComponent`](./blocksnowcontainercomponent.md)||
|[`BlockType`](./blocktype.md)||
|[`BlockWaterContainerComponent`](./blockwatercontainercomponent.md)||
|[`BoolBlockProperty`](./boolblockproperty.md)||
|[`ChatEvent`](./chatevent.md)||
|[`Color`](./color.md)||
|[`Component`](./component.md)||
|[`Container`](./container.md)||
|[`DataDrivenEntityTriggerEvent`](./datadrivenentitytriggerevent.md)||
|[`DataDrivenEntityTriggerEventSignal`](./datadrivenentitytriggereventsignal.md)||
|[`DefinitionModifier`](./definitionmodifier.md)||
|[`Dimension`](./dimension.md)||
|[`DynamicPropertiesDefinition`](./dynamicpropertiesdefinition.md)||
|[`Effect`](./effect.md)||
|[`EffectType`](./effecttype.md)||
|[`Entity`](./entity.md)||
|[`EntityAddRiderComponent`](./entityaddridercomponent.md)||
|[`EntityAgeableComponent`](./entityageablecomponent.md)||
|[`EntityAttributeComponent`](./entityattributecomponent.md)||
|[`EntityBaseMovementComponent`](./entitybasemovementcomponent.md)||
|[`EntityBreathableComponent`](./entitybreathablecomponent.md)||
|[`EntityCanClimbComponent`](./entitycanclimbcomponent.md)||
|[`EntityCanFlyComponent`](./entitycanflycomponent.md)||
|[`EntityCanPowerJumpComponent`](./entitycanpowerjumpcomponent.md)||
|[`EntityColorComponent`](./entitycolorcomponent.md)||
|[`EntityCreateEvent`](./entitycreateevent.md)||
|[`EntityCreateEventSignal`](./entitycreateeventsignal.md)||
|[`EntityDataDrivenTriggerEventOptions`](./entitydatadriventriggereventoptions.md)||
|[`EntityDefinitionFeedItem`](./entitydefinitionfeeditem.md)||
|[`EntityEventOptions`](./entityeventoptions.md)||
|[`EntityFireImmuneComponent`](./entityfireimmunecomponent.md)||
|[`EntityFloatsInLiquidComponent`](./entityfloatsinliquidcomponent.md)||
|[`EntityFlyingSpeedComponent`](./entityflyingspeedcomponent.md)||
|[`EntityFrictionModifierComponent`](./entityfrictionmodifiercomponent.md)||
|[`EntityGroundOffsetComponent`](./entitygroundoffsetcomponent.md)||
|[`EntityHealableComponent`](./entityhealablecomponent.md)||
|[`EntityHealthComponent`](./entityhealthcomponent.md)||
|[`EntityHitEvent`](./entityhitevent.md)||
|[`EntityHitEventSignal`](./entityhiteventsignal.md)||
|[`EntityHurtEvent`](./entityhurtevent.md)||
|[`EntityHurtEventSignal`](./entityhurteventsignal.md)||
|[`EntityInventoryComponent`](./entityinventorycomponent.md)||
|[`EntityIsBabyComponent`](./entityisbabycomponent.md)||
|[`EntityIsChargedComponent`](./entityischargedcomponent.md)||
|[`EntityIsChestedComponent`](./entityischestedcomponent.md)||
|[`EntityIsDyableComponent`](./entityisdyablecomponent.md)||
|[`EntityIsHiddenWhenInvisibleComponent`](./entityishiddenwheninvisiblecomponent.md)||
|[`EntityIsIgnitedComponent`](./entityisignitedcomponent.md)||
|[`EntityIsIllagerCaptainComponent`](./entityisillagercaptaincomponent.md)||
|[`EntityIsSaddledComponent`](./entityissaddledcomponent.md)||
|[`EntityIsShakingComponent`](./entityisshakingcomponent.md)||
|[`EntityIsShearedComponent`](./entityisshearedcomponent.md)||
|[`EntityIsStackableComponent`](./entityisstackablecomponent.md)||
|[`EntityIsStunnedComponent`](./entityisstunnedcomponent.md)||
|[`EntityIsTamedComponent`](./entityistamedcomponent.md)||
|[`EntityItemComponent`](./entityitemcomponent.md)||
|[`EntityIterator`](./entityiterator.md)||
|[`EntityLavaMovementComponent`](./entitylavamovementcomponent.md)||
|[`EntityLeashableComponent`](./entityleashablecomponent.md)||
|[`EntityMarkVariantComponent`](./entitymarkvariantcomponent.md)||
|[`EntityMovementAmphibiousComponent`](./entitymovementamphibiouscomponent.md)||
|[`EntityMovementBasicComponent`](./entitymovementbasiccomponent.md)||
|[`EntityMovementComponent`](./entitymovementcomponent.md)||
|[`EntityMovementFlyComponent`](./entitymovementflycomponent.md)||
|[`EntityMovementGenericComponent`](./entitymovementgenericcomponent.md)||
|[`EntityMovementGlideComponent`](./entitymovementglidecomponent.md)||
|[`EntityMovementHoverComponent`](./entitymovementhovercomponent.md)||
|[`EntityMovementJumpComponent`](./entitymovementjumpcomponent.md)||
|[`EntityMovementSkipComponent`](./entitymovementskipcomponent.md)||
|[`EntityMovementSwayComponent`](./entitymovementswaycomponent.md)||
|[`EntityNavigationClimbComponent`](./entitynavigationclimbcomponent.md)||
|[`EntityNavigationComponent`](./entitynavigationcomponent.md)||
|[`EntityNavigationFloatComponent`](./entitynavigationfloatcomponent.md)||
|[`EntityNavigationFlyComponent`](./entitynavigationflycomponent.md)||
|[`EntityNavigationGenericComponent`](./entitynavigationgenericcomponent.md)||
|[`EntityNavigationHoverComponent`](./entitynavigationhovercomponent.md)||
|[`EntityNavigationWalkComponent`](./entitynavigationwalkcomponent.md)||
|[`EntityPushThroughComponent`](./entitypushthroughcomponent.md)||
|[`EntityQueryOptions`](./entityqueryoptions.md)||
|[`EntityQueryScoreOptions`](./entityqueryscoreoptions.md)||
|[`EntityRaycastOptions`](./entityraycastoptions.md)||
|[`EntityRideableComponent`](./entityrideablecomponent.md)||
|[`EntityScaleComponent`](./entityscalecomponent.md)||
|[`EntitySkinIdComponent`](./entityskinidcomponent.md)||
|[`EntityStrengthComponent`](./entitystrengthcomponent.md)||
|[`EntityTameableComponent`](./entitytameablecomponent.md)||
|[`EntityTameMountComponent`](./entitytamemountcomponent.md)||
|[`EntityType`](./entitytype.md)||
|[`EntityTypeIterator`](./entitytypeiterator.md)||
|[`EntityTypes`](./entitytypes.md)||
|[`EntityUnderwaterMovementComponent`](./entityunderwatermovementcomponent.md)||
|[`EntityVariantComponent`](./entityvariantcomponent.md)||
|[`EntityWantsJockeyComponent`](./entitywantsjockeycomponent.md)||
|[`Events`](./events.md)||
|[`ExplosionOptions`](./explosionoptions.md)||
|[`FeedItem`](./feeditem.md)||
|[`FeedItemEffect`](./feeditemeffect.md)||
|[`FilterGroup`](./filtergroup.md)||
|[`FluidContainer`](./fluidcontainer.md)||
|[`IBlockProperty`](./iblockproperty.md)||
|[`IEntityComponent`](./ientitycomponent.md)||
|[`IntBlockProperty`](./intblockproperty.md)||
|[`InventoryComponentContainer`](./inventorycomponentcontainer.md)||
|[`ItemCompleteChargeEvent`](./itemcompletechargeevent.md)||
|[`ItemCompleteChargeEventSignal`](./itemcompletechargeeventsignal.md)||
|[`ItemComponent`](./itemcomponent.md)||
|[`ItemCooldownComponent`](./itemcooldowncomponent.md)||
|[`ItemDurabilityComponent`](./itemdurabilitycomponent.md)||
|[`ItemFoodComponent`](./itemfoodcomponent.md)||
|[`ItemReleaseChargeEvent`](./itemreleasechargeevent.md)||
|[`ItemReleaseChargeEventSignal`](./itemreleasechargeeventsignal.md)||
|[`Items`](./items.md)||
|[`ItemStack`](./itemstack.md)||
|[`ItemStartChargeEvent`](./itemstartchargeevent.md)||
|[`ItemStartChargeEventSignal`](./itemstartchargeeventsignal.md)||
|[`ItemStopChargeEvent`](./itemstopchargeevent.md)||
|[`ItemStopChargeEventSignal`](./itemstopchargeeventsignal.md)||
|[`ItemType`](./itemtype.md)||
|[`ItemUseEvent`](./itemuseevent.md)||
|[`ItemUseOnEvent`](./itemuseonevent.md)||
|[`ItemUseOnEventSignal`](./itemuseoneventsignal.md)||
|[`Location`](./location.md)||
|[`MinecraftBlockTypes`](./minecraftblocktypes.md)||
|[`MinecraftDimensionTypes`](./minecraftdimensiontypes.md)||
|[`MinecraftEffectTypes`](./minecrafteffecttypes.md)||
|[`MinecraftItemTypes`](./minecraftitemtypes.md)||
|[`MolangVariableMap`](./molangvariablemap.md)||
|[`MusicOptions`](./musicoptions.md)||
|[`NumberRange`](./numberrange.md)||
|[`Player`](./player.md)||
|[`PlayerInventoryComponentContainer`](./playerinventorycomponentcontainer.md)||
|[`PlayerIterator`](./playeriterator.md)||
|[`PlayerJoinEvent`](./playerjoinevent.md)||
|[`PlayerJoinEventSignal`](./playerjoineventsignal.md)||
|[`PlayerLeaveEvent`](./playerleaveevent.md)||
|[`PlayerLeaveEventSignal`](./playerleaveeventsignal.md)||
|[`PropertyRegistry`](./propertyregistry.md)||
|[`Scoreboard`](./scoreboard.md)||
|[`ScoreboardIdentity`](./scoreboardidentity.md)||
|[`ScoreboardObjective`](./scoreboardobjective.md)||
|[`ScoreboardScoreInfo`](./scoreboardscoreinfo.md)||
|[`Seat`](./seat.md)||
|[`SoundOptions`](./soundoptions.md)||
|[`StringBlockProperty`](./stringblockproperty.md)||
|[`TickEvent`](./tickevent.md)||
|[`TickEventSignal`](./tickeventsignal.md)||
|[`Trigger`](./trigger.md)||
|[`Vector`](./vector.md)||
|[`WeatherChangeEvent`](./weatherchangeevent.md)||
|[`WeatherChangeEventSignal`](./weatherchangeeventsignal.md)||
|[`World`](./world.md)||
|[`WorldInitializeEvent`](./worldinitializeevent.md)||
|[`WorldInitializeEventSignal`](./worldinitializeeventsignal.md)||
|[`XYRotation`](./xyrotation.md)||

## 枚举

|枚举|描述|
|---|---|
|[`Direction`](./direction.md)||
|[`EntityDamageCause`](./entitydamagecause.md)||
|[`GameMode`](./gamemode.md)||
|[`ScoreboardIdentityType`](./scoreboardidentitytype.md)||
