# `@minecraft/server`

> 文档版本：1.21.50.25

`@minecraft/server`模块的`1.17.0-internal`版本，UUID为`b26a4d4c-afdf-4690-88f8-931846312678`。该模块是服务端的基础模块。

/// info | 依赖
该模块依赖于以下模块：

- `@minecraft/common`|`1.1.0`|`77ec12b4-1b2b-4c98-8d34-d1cd63f849d5`
///

## 常量

/// define
`HudElementsCount`


///

```js
static read-only HudElementsCount = 13;
```


/// define
`HudVisibilityCount`


///

```js
static read-only HudVisibilityCount = 2;
```


/// define
`isInternal`


///

```js
static read-only isInternal = True;
```


/// define
`MoonPhaseCount`


///

```js
static read-only MoonPhaseCount = 8;
```


/// define
`TicksPerDay`


///

```js
static read-only TicksPerDay = 24000;
```


/// define
`TicksPerSecond`


///

```js
static read-only TicksPerSecond = 20;
```


## 对象

/// define
`system`


///

```js
static read-only system: System;
```

/// html | div.result
//// define
`system`：[`System`](./system.md)

- script_api.@minecraft/server.system.description


////

///


/// define
`world`


///

```js
static read-only world: World;
```

/// html | div.result
//// define
`world`：[`World`](./world.md)

- script_api.@minecraft/server.world.description


////

///


## 类

|类|描述|
|---|---|
|[`BiomeType`](./biometype.md)||
|[`BiomeTypes`](./biometypes.md)||
|[`Block`](./block.md)||
|[`BlockComponent`](./blockcomponent.md)||
|[`BlockComponentEntityFallOnEvent`](./blockcomponententityfallonevent.md)||
|[`BlockComponentOnPlaceEvent`](./blockcomponentonplaceevent.md)||
|[`BlockComponentPlayerDestroyEvent`](./blockcomponentplayerdestroyevent.md)||
|[`BlockComponentPlayerInteractEvent`](./blockcomponentplayerinteractevent.md)||
|[`BlockComponentPlayerPlaceBeforeEvent`](./blockcomponentplayerplacebeforeevent.md)||
|[`BlockComponentRandomTickEvent`](./blockcomponentrandomtickevent.md)||
|[`BlockComponentRegistry`](./blockcomponentregistry.md)||
|[`BlockComponentStepOffEvent`](./blockcomponentstepoffevent.md)||
|[`BlockComponentStepOnEvent`](./blockcomponentsteponevent.md)||
|[`BlockComponentTickEvent`](./blockcomponenttickevent.md)||
|[`BlockEvent`](./blockevent.md)||
|[`BlockExplodeAfterEvent`](./blockexplodeafterevent.md)||
|[`BlockExplodeAfterEventSignal`](./blockexplodeaftereventsignal.md)||
|[`BlockFluidContainerComponent`](./blockfluidcontainercomponent.md)||
|[`BlockInventoryComponent`](./blockinventorycomponent.md)||
|[`BlockLocationIterator`](./blocklocationiterator.md)||
|[`BlockPermutation`](./blockpermutation.md)||
|[`BlockPistonComponent`](./blockpistoncomponent.md)||
|[`BlockRecordPlayerComponent`](./blockrecordplayercomponent.md)||
|[`BlockSignComponent`](./blocksigncomponent.md)||
|[`BlockStates`](./blockstates.md)||
|[`BlockStateType`](./blockstatetype.md)||
|[`BlockType`](./blocktype.md)||
|[`BlockTypes`](./blocktypes.md)||
|[`BlockVolume`](./blockvolume.md)||
|[`BlockVolumeBase`](./blockvolumebase.md)||
|[`BoundingBoxUtils`](./boundingboxutils.md)||
|[`ButtonPushAfterEvent`](./buttonpushafterevent.md)||
|[`ButtonPushAfterEventSignal`](./buttonpushaftereventsignal.md)||
|[`Camera`](./camera.md)||
|[`ChatSendAfterEvent`](./chatsendafterevent.md)||
|[`ChatSendAfterEventSignal`](./chatsendaftereventsignal.md)||
|[`ChatSendBeforeEvent`](./chatsendbeforeevent.md)||
|[`ChatSendBeforeEventSignal`](./chatsendbeforeeventsignal.md)||
|[`ClientSystemInfo`](./clientsysteminfo.md)||
|[`CommandResult`](./commandresult.md)||
|[`Component`](./component.md)||
|[`CompoundBlockVolume`](./compoundblockvolume.md)||
|[`Container`](./container.md)||
|[`ContainerSlot`](./containerslot.md)||
|[`DataDrivenEntityTriggerAfterEvent`](./datadrivenentitytriggerafterevent.md)||
|[`DataDrivenEntityTriggerAfterEventSignal`](./datadrivenentitytriggeraftereventsignal.md)||
|[`Dimension`](./dimension.md)||
|[`DimensionType`](./dimensiontype.md)||
|[`DimensionTypes`](./dimensiontypes.md)||
|[`Effect`](./effect.md)||
|[`EffectAddAfterEvent`](./effectaddafterevent.md)||
|[`EffectAddAfterEventSignal`](./effectaddaftereventsignal.md)||
|[`EffectAddBeforeEvent`](./effectaddbeforeevent.md)||
|[`EffectAddBeforeEventSignal`](./effectaddbeforeeventsignal.md)||
|[`EffectType`](./effecttype.md)||
|[`EffectTypes`](./effecttypes.md)||
|[`EnchantmentType`](./enchantmenttype.md)||
|[`EnchantmentTypes`](./enchantmenttypes.md)||
|[`Entity`](./entity.md)||
|[`EntityAddRiderComponent`](./entityaddridercomponent.md)||
|[`EntityAgeableComponent`](./entityageablecomponent.md)||
|[`EntityAttributeComponent`](./entityattributecomponent.md)||
|[`EntityBaseMovementComponent`](./entitybasemovementcomponent.md)||
|[`EntityBreathableComponent`](./entitybreathablecomponent.md)||
|[`EntityCanClimbComponent`](./entitycanclimbcomponent.md)||
|[`EntityCanFlyComponent`](./entitycanflycomponent.md)||
|[`EntityCanPowerJumpComponent`](./entitycanpowerjumpcomponent.md)||
|[`EntityColor2Component`](./entitycolor2component.md)||
|[`EntityColorComponent`](./entitycolorcomponent.md)||
|[`EntityComponent`](./entitycomponent.md)||
|[`EntityDefinitionFeedItem`](./entitydefinitionfeeditem.md)||
|[`EntityDieAfterEvent`](./entitydieafterevent.md)||
|[`EntityDieAfterEventSignal`](./entitydieaftereventsignal.md)||
|[`EntityEquippableComponent`](./entityequippablecomponent.md)||
|[`EntityFireImmuneComponent`](./entityfireimmunecomponent.md)||
|[`EntityFloatsInLiquidComponent`](./entityfloatsinliquidcomponent.md)||
|[`EntityFlyingSpeedComponent`](./entityflyingspeedcomponent.md)||
|[`EntityFrictionModifierComponent`](./entityfrictionmodifiercomponent.md)||
|[`EntityGroundOffsetComponent`](./entitygroundoffsetcomponent.md)||
|[`EntityHealableComponent`](./entityhealablecomponent.md)||
|[`EntityHealthChangedAfterEvent`](./entityhealthchangedafterevent.md)||
|[`EntityHealthChangedAfterEventSignal`](./entityhealthchangedaftereventsignal.md)||
|[`EntityHealthComponent`](./entityhealthcomponent.md)||
|[`EntityHitBlockAfterEvent`](./entityhitblockafterevent.md)||
|[`EntityHitBlockAfterEventSignal`](./entityhitblockaftereventsignal.md)||
|[`EntityHitEntityAfterEvent`](./entityhitentityafterevent.md)||
|[`EntityHitEntityAfterEventSignal`](./entityhitentityaftereventsignal.md)||
|[`EntityHurtAfterEvent`](./entityhurtafterevent.md)||
|[`EntityHurtAfterEventSignal`](./entityhurtaftereventsignal.md)||
|[`EntityInventoryComponent`](./entityinventorycomponent.md)||
|[`EntityIsBabyComponent`](./entityisbabycomponent.md)||
|[`EntityIsChargedComponent`](./entityischargedcomponent.md)||
|[`EntityIsChestedComponent`](./entityischestedcomponent.md)||
|[`EntityIsDyeableComponent`](./entityisdyeablecomponent.md)||
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
|[`EntityLoadAfterEvent`](./entityloadafterevent.md)||
|[`EntityLoadAfterEventSignal`](./entityloadaftereventsignal.md)||
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
|[`EntityNpcComponent`](./entitynpccomponent.md)||
|[`EntityOnFireComponent`](./entityonfirecomponent.md)||
|[`EntityProjectileComponent`](./entityprojectilecomponent.md)||
|[`EntityPushThroughComponent`](./entitypushthroughcomponent.md)||
|[`EntityRemoveAfterEvent`](./entityremoveafterevent.md)||
|[`EntityRemoveAfterEventSignal`](./entityremoveaftereventsignal.md)||
|[`EntityRemoveBeforeEvent`](./entityremovebeforeevent.md)||
|[`EntityRemoveBeforeEventSignal`](./entityremovebeforeeventsignal.md)||
|[`EntityRideableComponent`](./entityrideablecomponent.md)||
|[`EntityRidingComponent`](./entityridingcomponent.md)||
|[`EntityScaleComponent`](./entityscalecomponent.md)||
|[`EntitySkinIdComponent`](./entityskinidcomponent.md)||
|[`EntitySpawnAfterEvent`](./entityspawnafterevent.md)||
|[`EntitySpawnAfterEventSignal`](./entityspawnaftereventsignal.md)||
|[`EntityStrengthComponent`](./entitystrengthcomponent.md)||
|[`EntityTameableComponent`](./entitytameablecomponent.md)||
|[`EntityTameMountComponent`](./entitytamemountcomponent.md)||
|[`EntityType`](./entitytype.md)||
|[`EntityTypeFamilyComponent`](./entitytypefamilycomponent.md)||
|[`EntityTypeIterator`](./entitytypeiterator.md)||
|[`EntityTypes`](./entitytypes.md)||
|[`EntityUnderwaterMovementComponent`](./entityunderwatermovementcomponent.md)||
|[`EntityVariantComponent`](./entityvariantcomponent.md)||
|[`EntityWantsJockeyComponent`](./entitywantsjockeycomponent.md)||
|[`ExplosionAfterEvent`](./explosionafterevent.md)||
|[`ExplosionAfterEventSignal`](./explosionaftereventsignal.md)||
|[`ExplosionBeforeEvent`](./explosionbeforeevent.md)||
|[`ExplosionBeforeEventSignal`](./explosionbeforeeventsignal.md)||
|[`FeedItem`](./feeditem.md)||
|[`FeedItemEffect`](./feeditemeffect.md)||
|[`FilterGroup`](./filtergroup.md)||
|[`FluidContainer`](./fluidcontainer.md)||
|[`GameRuleChangeAfterEvent`](./gamerulechangeafterevent.md)||
|[`GameRuleChangeAfterEventSignal`](./gamerulechangeaftereventsignal.md)||
|[`GameRules`](./gamerules.md)||
|[`IButtonPushAfterEventSignal`](./ibuttonpushaftereventsignal.md)||
|[`ILeverActionAfterEventSignal`](./ileveractionaftereventsignal.md)||
|[`InputInfo`](./inputinfo.md)||
|[`IPlayerJoinAfterEventSignal`](./iplayerjoinaftereventsignal.md)||
|[`IPlayerLeaveAfterEventSignal`](./iplayerleaveaftereventsignal.md)||
|[`IPlayerSpawnAfterEventSignal`](./iplayerspawnaftereventsignal.md)||
|[`ItemCompleteUseAfterEvent`](./itemcompleteuseafterevent.md)||
|[`ItemCompleteUseAfterEventSignal`](./itemcompleteuseaftereventsignal.md)||
|[`ItemCompleteUseEvent`](./itemcompleteuseevent.md)||
|[`ItemComponent`](./itemcomponent.md)||
|[`ItemComponentBeforeDurabilityDamageEvent`](./itemcomponentbeforedurabilitydamageevent.md)||
|[`ItemComponentCompleteUseEvent`](./itemcomponentcompleteuseevent.md)||
|[`ItemComponentConsumeEvent`](./itemcomponentconsumeevent.md)||
|[`ItemComponentHitEntityEvent`](./itemcomponenthitentityevent.md)||
|[`ItemComponentMineBlockEvent`](./itemcomponentmineblockevent.md)||
|[`ItemComponentRegistry`](./itemcomponentregistry.md)||
|[`ItemComponentUseEvent`](./itemcomponentuseevent.md)||
|[`ItemComponentUseOnEvent`](./itemcomponentuseonevent.md)||
|[`ItemCooldownComponent`](./itemcooldowncomponent.md)||
|[`ItemDurabilityComponent`](./itemdurabilitycomponent.md)||
|[`ItemDyeableComponent`](./itemdyeablecomponent.md)||
|[`ItemEnchantableComponent`](./itemenchantablecomponent.md)||
|[`ItemFoodComponent`](./itemfoodcomponent.md)||
|[`ItemPotionComponent`](./itempotioncomponent.md)||
|[`ItemReleaseUseAfterEvent`](./itemreleaseuseafterevent.md)||
|[`ItemReleaseUseAfterEventSignal`](./itemreleaseuseaftereventsignal.md)||
|[`ItemStack`](./itemstack.md)||
|[`ItemStartUseAfterEvent`](./itemstartuseafterevent.md)||
|[`ItemStartUseAfterEventSignal`](./itemstartuseaftereventsignal.md)||
|[`ItemStartUseOnAfterEvent`](./itemstartuseonafterevent.md)||
|[`ItemStartUseOnAfterEventSignal`](./itemstartuseonaftereventsignal.md)||
|[`ItemStopUseAfterEvent`](./itemstopuseafterevent.md)||
|[`ItemStopUseAfterEventSignal`](./itemstopuseaftereventsignal.md)||
|[`ItemStopUseOnAfterEvent`](./itemstopuseonafterevent.md)||
|[`ItemStopUseOnAfterEventSignal`](./itemstopuseonaftereventsignal.md)||
|[`ItemType`](./itemtype.md)||
|[`ItemTypes`](./itemtypes.md)||
|[`ItemUseAfterEvent`](./itemuseafterevent.md)||
|[`ItemUseAfterEventSignal`](./itemuseaftereventsignal.md)||
|[`ItemUseBeforeEvent`](./itemusebeforeevent.md)||
|[`ItemUseBeforeEventSignal`](./itemusebeforeeventsignal.md)||
|[`ItemUseOnAfterEvent`](./itemuseonafterevent.md)||
|[`ItemUseOnAfterEventSignal`](./itemuseonaftereventsignal.md)||
|[`ItemUseOnBeforeEvent`](./itemuseonbeforeevent.md)||
|[`ItemUseOnBeforeEventSignal`](./itemuseonbeforeeventsignal.md)||
|[`ItemUseOnEvent`](./itemuseonevent.md)||
|[`LeverActionAfterEvent`](./leveractionafterevent.md)||
|[`LeverActionAfterEventSignal`](./leveractionaftereventsignal.md)||
|[`ListBlockVolume`](./listblockvolume.md)||
|[`MessageReceiveAfterEvent`](./messagereceiveafterevent.md)||
|[`MinecraftDimensionTypes`](./minecraftdimensiontypes.md)||
|[`MolangVariableMap`](./molangvariablemap.md)||
|[`PistonActivateAfterEvent`](./pistonactivateafterevent.md)||
|[`PistonActivateAfterEventSignal`](./pistonactivateaftereventsignal.md)||
|[`Player`](./player.md)||
|[`PlayerBreakBlockAfterEvent`](./playerbreakblockafterevent.md)||
|[`PlayerBreakBlockAfterEventSignal`](./playerbreakblockaftereventsignal.md)||
|[`PlayerBreakBlockBeforeEvent`](./playerbreakblockbeforeevent.md)||
|[`PlayerBreakBlockBeforeEventSignal`](./playerbreakblockbeforeeventsignal.md)||
|[`PlayerButtonInputAfterEvent`](./playerbuttoninputafterevent.md)||
|[`PlayerButtonInputAfterEventSignal`](./playerbuttoninputaftereventsignal.md)||
|[`PlayerCursorInventoryComponent`](./playercursorinventorycomponent.md)||
|[`PlayerDimensionChangeAfterEvent`](./playerdimensionchangeafterevent.md)||
|[`PlayerDimensionChangeAfterEventSignal`](./playerdimensionchangeaftereventsignal.md)||
|[`PlayerEmoteAfterEvent`](./playeremoteafterevent.md)||
|[`PlayerEmoteAfterEventSignal`](./playeremoteaftereventsignal.md)||
|[`PlayerGameModeChangeAfterEvent`](./playergamemodechangeafterevent.md)||
|[`PlayerGameModeChangeAfterEventSignal`](./playergamemodechangeaftereventsignal.md)||
|[`PlayerGameModeChangeBeforeEvent`](./playergamemodechangebeforeevent.md)||
|[`PlayerGameModeChangeBeforeEventSignal`](./playergamemodechangebeforeeventsignal.md)||
|[`PlayerInputModeChangeAfterEvent`](./playerinputmodechangeafterevent.md)||
|[`PlayerInputModeChangeAfterEventSignal`](./playerinputmodechangeaftereventsignal.md)||
|[`PlayerInputPermissionCategoryChangeAfterEvent`](./playerinputpermissioncategorychangeafterevent.md)||
|[`PlayerInputPermissionCategoryChangeAfterEventSignal`](./playerinputpermissioncategorychangeaftereventsignal.md)||
|[`PlayerInputPermissions`](./playerinputpermissions.md)||
|[`PlayerInteractWithBlockAfterEvent`](./playerinteractwithblockafterevent.md)||
|[`PlayerInteractWithBlockAfterEventSignal`](./playerinteractwithblockaftereventsignal.md)||
|[`PlayerInteractWithBlockBeforeEvent`](./playerinteractwithblockbeforeevent.md)||
|[`PlayerInteractWithBlockBeforeEventSignal`](./playerinteractwithblockbeforeeventsignal.md)||
|[`PlayerInteractWithEntityAfterEvent`](./playerinteractwithentityafterevent.md)||
|[`PlayerInteractWithEntityAfterEventSignal`](./playerinteractwithentityaftereventsignal.md)||
|[`PlayerInteractWithEntityBeforeEvent`](./playerinteractwithentitybeforeevent.md)||
|[`PlayerInteractWithEntityBeforeEventSignal`](./playerinteractwithentitybeforeeventsignal.md)||
|[`PlayerIterator`](./playeriterator.md)||
|[`PlayerJoinAfterEvent`](./playerjoinafterevent.md)||
|[`PlayerJoinAfterEventSignal`](./playerjoinaftereventsignal.md)||
|[`PlayerLeaveAfterEvent`](./playerleaveafterevent.md)||
|[`PlayerLeaveAfterEventSignal`](./playerleaveaftereventsignal.md)||
|[`PlayerLeaveBeforeEvent`](./playerleavebeforeevent.md)||
|[`PlayerLeaveBeforeEventSignal`](./playerleavebeforeeventsignal.md)||
|[`PlayerPlaceBlockAfterEvent`](./playerplaceblockafterevent.md)||
|[`PlayerPlaceBlockAfterEventSignal`](./playerplaceblockaftereventsignal.md)||
|[`PlayerPlaceBlockBeforeEvent`](./playerplaceblockbeforeevent.md)||
|[`PlayerPlaceBlockBeforeEventSignal`](./playerplaceblockbeforeeventsignal.md)||
|[`PlayerSpawnAfterEvent`](./playerspawnafterevent.md)||
|[`PlayerSpawnAfterEventSignal`](./playerspawnaftereventsignal.md)||
|[`PotionEffectType`](./potioneffecttype.md)||
|[`PotionLiquidType`](./potionliquidtype.md)||
|[`PotionModifierType`](./potionmodifiertype.md)||
|[`Potions`](./potions.md)||
|[`PressurePlatePopAfterEvent`](./pressureplatepopafterevent.md)||
|[`PressurePlatePopAfterEventSignal`](./pressureplatepopaftereventsignal.md)||
|[`PressurePlatePushAfterEvent`](./pressureplatepushafterevent.md)||
|[`PressurePlatePushAfterEventSignal`](./pressureplatepushaftereventsignal.md)||
|[`ProjectileHitBlockAfterEvent`](./projectilehitblockafterevent.md)||
|[`ProjectileHitBlockAfterEventSignal`](./projectilehitblockaftereventsignal.md)||
|[`ProjectileHitEntityAfterEvent`](./projectilehitentityafterevent.md)||
|[`ProjectileHitEntityAfterEventSignal`](./projectilehitentityaftereventsignal.md)||
|[`Scoreboard`](./scoreboard.md)||
|[`ScoreboardIdentity`](./scoreboardidentity.md)||
|[`ScoreboardObjective`](./scoreboardobjective.md)||
|[`ScoreboardScoreInfo`](./scoreboardscoreinfo.md)||
|[`ScreenDisplay`](./screendisplay.md)||
|[`ScriptEventCommandMessageAfterEvent`](./scripteventcommandmessageafterevent.md)||
|[`ScriptEventCommandMessageAfterEventSignal`](./scripteventcommandmessageaftereventsignal.md)||
|[`Seat`](./seat.md)||
|[`ServerMessageAfterEventSignal`](./servermessageaftereventsignal.md)||
|[`Structure`](./structure.md)||
|[`StructureManager`](./structuremanager.md)||
|[`System`](./system.md)||
|[`SystemAfterEvents`](./systemafterevents.md)||
|[`SystemBeforeEvents`](./systembeforeevents.md)||
|[`SystemInfo`](./systeminfo.md)||
|[`TargetBlockHitAfterEvent`](./targetblockhitafterevent.md)||
|[`TargetBlockHitAfterEventSignal`](./targetblockhitaftereventsignal.md)||
|[`Trigger`](./trigger.md)||
|[`TripWireTripAfterEvent`](./tripwiretripafterevent.md)||
|[`TripWireTripAfterEventSignal`](./tripwiretripaftereventsignal.md)||
|[`WatchdogTerminateBeforeEvent`](./watchdogterminatebeforeevent.md)||
|[`WatchdogTerminateBeforeEventSignal`](./watchdogterminatebeforeeventsignal.md)||
|[`WeatherChangeAfterEvent`](./weatherchangeafterevent.md)||
|[`WeatherChangeAfterEventSignal`](./weatherchangeaftereventsignal.md)||
|[`WeatherChangeBeforeEvent`](./weatherchangebeforeevent.md)||
|[`WeatherChangeBeforeEventSignal`](./weatherchangebeforeeventsignal.md)||
|[`World`](./world.md)||
|[`WorldAfterEvents`](./worldafterevents.md)||
|[`WorldBeforeEvents`](./worldbeforeevents.md)||
|[`WorldInitializeAfterEvent`](./worldinitializeafterevent.md)||
|[`WorldInitializeAfterEventSignal`](./worldinitializeaftereventsignal.md)||
|[`WorldInitializeBeforeEvent`](./worldinitializebeforeevent.md)||
|[`WorldInitializeBeforeEventSignal`](./worldinitializebeforeeventsignal.md)||

## 接口

|接口|描述|
|---|---|
|[`BiomeSearchOptions`](./biomesearchoptions.md)||
|[`BlockCustomComponent`](./blockcustomcomponent.md)||
|[`BlockEventOptions`](./blockeventoptions.md)||
|[`BlockFillOptions`](./blockfilloptions.md)||
|[`BlockFilter`](./blockfilter.md)||
|[`BlockHitInformation`](./blockhitinformation.md)||
|[`BlockRaycastHit`](./blockraycasthit.md)||
|[`BlockRaycastOptions`](./blockraycastoptions.md)||
|[`BoundingBox`](./boundingbox.md)||
|[`CameraDefaultOptions`](./cameradefaultoptions.md)||
|[`CameraEaseOptions`](./cameraeaseoptions.md)||
|[`CameraFadeOptions`](./camerafadeoptions.md)||
|[`CameraFadeTimeOptions`](./camerafadetimeoptions.md)||
|[`CameraFixedBoomOptions`](./camerafixedboomoptions.md)||
|[`CameraSetFacingOptions`](./camerasetfacingoptions.md)||
|[`CameraSetLocationOptions`](./camerasetlocationoptions.md)||
|[`CameraSetPosOptions`](./camerasetposoptions.md)||
|[`CameraSetRotOptions`](./camerasetrotoptions.md)||
|[`CompoundBlockVolumeItem`](./compoundblockvolumeitem.md)||
|[`DefinitionModifier`](./definitionmodifier.md)||
|[`DimensionLocation`](./dimensionlocation.md)||
|[`Enchantment`](./enchantment.md)||
|[`EntityApplyDamageByProjectileOptions`](./entityapplydamagebyprojectileoptions.md)||
|[`EntityApplyDamageOptions`](./entityapplydamageoptions.md)||
|[`EntityDamageSource`](./entitydamagesource.md)||
|[`EntityDataDrivenTriggerEventOptions`](./entitydatadriventriggereventoptions.md)||
|[`EntityEffectOptions`](./entityeffectoptions.md)||
|[`EntityEventOptions`](./entityeventoptions.md)||
|[`EntityFilter`](./entityfilter.md)||
|[`EntityHitInformation`](./entityhitinformation.md)||
|[`EntityQueryOptions`](./entityqueryoptions.md)||
|[`EntityQueryPropertyOptions`](./entityquerypropertyoptions.md)||
|[`EntityQueryScoreOptions`](./entityqueryscoreoptions.md)||
|[`EntityRaycastHit`](./entityraycasthit.md)||
|[`EntityRaycastOptions`](./entityraycastoptions.md)||
|[`EqualsComparison`](./equalscomparison.md)||
|[`ExplosionOptions`](./explosionoptions.md)||
|[`GreaterThanComparison`](./greaterthancomparison.md)||
|[`GreaterThanOrEqualsComparison`](./greaterthanorequalscomparison.md)||
|[`InputEventOptions`](./inputeventoptions.md)||
|[`ItemCustomComponent`](./itemcustomcomponent.md)||
|[`JigsawPlaceOptions`](./jigsawplaceoptions.md)||
|[`JigsawStructurePlaceOptions`](./jigsawstructureplaceoptions.md)||
|[`LessThanComparison`](./lessthancomparison.md)||
|[`LessThanOrEqualsComparison`](./lessthanorequalscomparison.md)||
|[`MusicOptions`](./musicoptions.md)||
|[`NotEqualsComparison`](./notequalscomparison.md)||
|[`PlayAnimationOptions`](./playanimationoptions.md)||
|[`PlayerSoundOptions`](./playersoundoptions.md)||
|[`PotionOptions`](./potionoptions.md)||
|[`ProjectileShootOptions`](./projectileshootoptions.md)||
|[`RangeComparison`](./rangecomparison.md)||
|[`RawMessage`](./rawmessage.md)||
|[`RawMessageScore`](./rawmessagescore.md)||
|[`RawText`](./rawtext.md)||
|[`RGB`](./rgb.md)||
|[`RGBA`](./rgba.md)||
|[`ScoreboardObjectiveDisplayOptions`](./scoreboardobjectivedisplayoptions.md)||
|[`ScriptEventMessageFilterOptions`](./scripteventmessagefilteroptions.md)||
|[`SpawnEntityOptions`](./spawnentityoptions.md)||
|[`StructureCreateOptions`](./structurecreateoptions.md)||
|[`StructurePlaceOptions`](./structureplaceoptions.md)||
|[`TeleportOptions`](./teleportoptions.md)||
|[`TitleDisplayOptions`](./titledisplayoptions.md)||
|[`Vector2`](./vector2.md)||
|[`Vector3`](./vector3.md)||
|[`VectorXZ`](./vectorxz.md)||
|[`WorldSoundOptions`](./worldsoundoptions.md)||

## 枚举

|枚举|描述|
|---|---|
|[`BlockComponentTypes`](./blockcomponenttypes.md)||
|[`BlockPistonState`](./blockpistonstate.md)||
|[`BlockVolumeIntersection`](./blockvolumeintersection.md)||
|[`ButtonState`](./buttonstate.md)||
|[`CompoundBlockVolumeAction`](./compoundblockvolumeaction.md)||
|[`CompoundBlockVolumePositionRelativity`](./compoundblockvolumepositionrelativity.md)||
|[`CustomComponentNameErrorReason`](./customcomponentnameerrorreason.md)||
|[`Difficulty`](./difficulty.md)||
|[`Direction`](./direction.md)||
|[`DisplaySlotId`](./displayslotid.md)||
|[`DyeColor`](./dyecolor.md)||
|[`EasingType`](./easingtype.md)||
|[`EnchantmentSlot`](./enchantmentslot.md)||
|[`EntityComponentTypes`](./entitycomponenttypes.md)||
|[`EntityDamageCause`](./entitydamagecause.md)||
|[`EntityInitializationCause`](./entityinitializationcause.md)||
|[`EquipmentSlot`](./equipmentslot.md)||
|[`FluidType`](./fluidtype.md)||
|[`GameMode`](./gamemode.md)||
|[`GameRule`](./gamerule.md)||
|[`HudElement`](./hudelement.md)||
|[`HudVisibility`](./hudvisibility.md)||
|[`InputButton`](./inputbutton.md)||
|[`InputMode`](./inputmode.md)||
|[`InputPermissionCategory`](./inputpermissioncategory.md)||
|[`ItemComponentTypes`](./itemcomponenttypes.md)||
|[`ItemLockMode`](./itemlockmode.md)||
|[`MemoryTier`](./memorytier.md)||
|[`MoonPhase`](./moonphase.md)||
|[`ObjectiveSortOrder`](./objectivesortorder.md)||
|[`PaletteColor`](./palettecolor.md)||
|[`PlatformType`](./platformtype.md)||
|[`ScoreboardIdentityType`](./scoreboardidentitytype.md)||
|[`ScriptEventSource`](./scripteventsource.md)||
|[`SignSide`](./signside.md)||
|[`StructureAnimationMode`](./structureanimationmode.md)||
|[`StructureMirrorAxis`](./structuremirroraxis.md)||
|[`StructureRotation`](./structurerotation.md)||
|[`StructureSaveMode`](./structuresavemode.md)||
|[`TimeOfDay`](./timeofday.md)||
|[`WatchdogTerminateReason`](./watchdogterminatereason.md)||
|[`WeatherType`](./weathertype.md)||

## 类型别名

|类型别名|描述|
|---|---|
|[`BlockComponentTypeMap`](./blockcomponenttypemap.md)||
|[`EntityComponentTypeMap`](./entitycomponenttypemap.md)||
|[`ItemComponentTypeMap`](./itemcomponenttypemap.md)||

## 错误

|错误|描述|
|---|---|
|[`BlockCustomComponentAlreadyRegisteredError`](./blockcustomcomponentalreadyregisterederror.md)||
|[`BlockCustomComponentReloadNewComponentError`](./blockcustomcomponentreloadnewcomponenterror.md)||
|[`BlockCustomComponentReloadNewEventError`](./blockcustomcomponentreloadneweventerror.md)||
|[`BlockCustomComponentReloadVersionError`](./blockcustomcomponentreloadversionerror.md)||
|[`CommandError`](./commanderror.md)||
|[`CustomComponentInvalidRegistryError`](./customcomponentinvalidregistryerror.md)||
|[`CustomComponentNameError`](./customcomponentnameerror.md)||
|[`EnchantmentLevelOutOfBoundsError`](./enchantmentleveloutofboundserror.md)||
|[`EnchantmentTypeNotCompatibleError`](./enchantmenttypenotcompatibleerror.md)||
|[`EnchantmentTypeUnknownIdError`](./enchantmenttypeunknowniderror.md)||
|[`InvalidContainerSlotError`](./invalidcontainersloterror.md)||
|[`InvalidEntityError`](./invalidentityerror.md)||
|[`InvalidIteratorError`](./invaliditeratorerror.md)||
|[`InvalidStructureError`](./invalidstructureerror.md)||
|[`ItemCustomComponentAlreadyRegisteredError`](./itemcustomcomponentalreadyregisterederror.md)||
|[`ItemCustomComponentReloadNewComponentError`](./itemcustomcomponentreloadnewcomponenterror.md)||
|[`ItemCustomComponentReloadNewEventError`](./itemcustomcomponentreloadneweventerror.md)||
|[`ItemCustomComponentReloadVersionError`](./itemcustomcomponentreloadversionerror.md)||
|[`LocationInUnloadedChunkError`](./locationinunloadedchunkerror.md)||
|[`LocationOutOfWorldBoundariesError`](./locationoutofworldboundarieserror.md)||
|[`PlaceJigsawError`](./placejigsawerror.md)||
|[`UnloadedChunksError`](./unloadedchunkserror.md)||
