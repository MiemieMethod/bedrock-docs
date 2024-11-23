# `@minecraft/server`

> 文档版本：1.21.60.21

`@minecraft/server`模块的`1.10.0`版本，UUID为`b26a4d4c-afdf-4690-88f8-931846312678`。该模块是服务端的基础模块。

/// info | 依赖
该模块依赖于以下模块：

- `@minecraft/common`|`1.1.0`|`77ec12b4-1b2b-4c98-8d34-d1cd63f849d5`
///

## 常量

/// define
`MoonPhaseCount`


///

```js
static read-only MoonPhaseCount = 8;
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
|[`Block`](./block.md)||
|[`BlockComponent`](./blockcomponent.md)||
|[`BlockEvent`](./blockevent.md)||
|[`BlockInventoryComponent`](./blockinventorycomponent.md)||
|[`BlockPermutation`](./blockpermutation.md)||
|[`BlockPistonComponent`](./blockpistoncomponent.md)||
|[`BlockSignComponent`](./blocksigncomponent.md)||
|[`BlockStates`](./blockstates.md)||
|[`BlockStateType`](./blockstatetype.md)||
|[`BlockType`](./blocktype.md)||
|[`ButtonPushAfterEvent`](./buttonpushafterevent.md)||
|[`ButtonPushAfterEventSignal`](./buttonpushaftereventsignal.md)||
|[`Camera`](./camera.md)||
|[`CommandResult`](./commandresult.md)||
|[`Component`](./component.md)||
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
|[`Entity`](./entity.md)||
|[`EntityAttributeComponent`](./entityattributecomponent.md)||
|[`EntityBaseMovementComponent`](./entitybasemovementcomponent.md)||
|[`EntityCanClimbComponent`](./entitycanclimbcomponent.md)||
|[`EntityCanFlyComponent`](./entitycanflycomponent.md)||
|[`EntityCanPowerJumpComponent`](./entitycanpowerjumpcomponent.md)||
|[`EntityColorComponent`](./entitycolorcomponent.md)||
|[`EntityComponent`](./entitycomponent.md)||
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
|[`EntityLoadAfterEvent`](./entityloadafterevent.md)||
|[`EntityLoadAfterEventSignal`](./entityloadaftereventsignal.md)||
|[`EntityMarkVariantComponent`](./entitymarkvariantcomponent.md)||
|[`EntityMovementAmphibiousComponent`](./entitymovementamphibiouscomponent.md)||
|[`EntityMovementBasicComponent`](./entitymovementbasiccomponent.md)||
|[`EntityMovementFlyComponent`](./entitymovementflycomponent.md)||
|[`EntityMovementGenericComponent`](./entitymovementgenericcomponent.md)||
|[`EntityMovementHoverComponent`](./entitymovementhovercomponent.md)||
|[`EntityMovementJumpComponent`](./entitymovementjumpcomponent.md)||
|[`EntityMovementSkipComponent`](./entitymovementskipcomponent.md)||
|[`EntityOnFireComponent`](./entityonfirecomponent.md)||
|[`EntityProjectileComponent`](./entityprojectilecomponent.md)||
|[`EntityPushThroughComponent`](./entitypushthroughcomponent.md)||
|[`EntityRemoveAfterEvent`](./entityremoveafterevent.md)||
|[`EntityRemoveAfterEventSignal`](./entityremoveaftereventsignal.md)||
|[`EntityRemoveBeforeEvent`](./entityremovebeforeevent.md)||
|[`EntityRemoveBeforeEventSignal`](./entityremovebeforeeventsignal.md)||
|[`EntityScaleComponent`](./entityscalecomponent.md)||
|[`EntitySkinIdComponent`](./entityskinidcomponent.md)||
|[`EntitySpawnAfterEvent`](./entityspawnafterevent.md)||
|[`EntitySpawnAfterEventSignal`](./entityspawnaftereventsignal.md)||
|[`EntityType`](./entitytype.md)||
|[`EntityTypeFamilyComponent`](./entitytypefamilycomponent.md)||
|[`EntityTypes`](./entitytypes.md)||
|[`EntityVariantComponent`](./entityvariantcomponent.md)||
|[`EntityWantsJockeyComponent`](./entitywantsjockeycomponent.md)||
|[`ExplosionAfterEvent`](./explosionafterevent.md)||
|[`ExplosionAfterEventSignal`](./explosionaftereventsignal.md)||
|[`ExplosionBeforeEvent`](./explosionbeforeevent.md)||
|[`ExplosionBeforeEventSignal`](./explosionbeforeeventsignal.md)||
|[`FeedItem`](./feeditem.md)||
|[`FeedItemEffect`](./feeditemeffect.md)||
|[`IButtonPushAfterEventSignal`](./ibuttonpushaftereventsignal.md)||
|[`ILeverActionAfterEventSignal`](./ileveractionaftereventsignal.md)||
|[`IPlayerJoinAfterEventSignal`](./iplayerjoinaftereventsignal.md)||
|[`IPlayerLeaveAfterEventSignal`](./iplayerleaveaftereventsignal.md)||
|[`IPlayerSpawnAfterEventSignal`](./iplayerspawnaftereventsignal.md)||
|[`ItemCompleteUseAfterEvent`](./itemcompleteuseafterevent.md)||
|[`ItemCompleteUseAfterEventSignal`](./itemcompleteuseaftereventsignal.md)||
|[`ItemComponent`](./itemcomponent.md)||
|[`ItemCooldownComponent`](./itemcooldowncomponent.md)||
|[`ItemDurabilityComponent`](./itemdurabilitycomponent.md)||
|[`ItemFoodComponent`](./itemfoodcomponent.md)||
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
|[`ItemUseAfterEvent`](./itemuseafterevent.md)||
|[`ItemUseAfterEventSignal`](./itemuseaftereventsignal.md)||
|[`ItemUseBeforeEvent`](./itemusebeforeevent.md)||
|[`ItemUseBeforeEventSignal`](./itemusebeforeeventsignal.md)||
|[`ItemUseOnAfterEvent`](./itemuseonafterevent.md)||
|[`ItemUseOnAfterEventSignal`](./itemuseonaftereventsignal.md)||
|[`ItemUseOnBeforeEvent`](./itemuseonbeforeevent.md)||
|[`ItemUseOnBeforeEventSignal`](./itemuseonbeforeeventsignal.md)||
|[`LeverActionAfterEvent`](./leveractionafterevent.md)||
|[`LeverActionAfterEventSignal`](./leveractionaftereventsignal.md)||
|[`MinecraftDimensionTypes`](./minecraftdimensiontypes.md)||
|[`MolangVariableMap`](./molangvariablemap.md)||
|[`PistonActivateAfterEvent`](./pistonactivateafterevent.md)||
|[`PistonActivateAfterEventSignal`](./pistonactivateaftereventsignal.md)||
|[`Player`](./player.md)||
|[`PlayerBreakBlockAfterEvent`](./playerbreakblockafterevent.md)||
|[`PlayerBreakBlockAfterEventSignal`](./playerbreakblockaftereventsignal.md)||
|[`PlayerBreakBlockBeforeEvent`](./playerbreakblockbeforeevent.md)||
|[`PlayerBreakBlockBeforeEventSignal`](./playerbreakblockbeforeeventsignal.md)||
|[`PlayerDimensionChangeAfterEvent`](./playerdimensionchangeafterevent.md)||
|[`PlayerDimensionChangeAfterEventSignal`](./playerdimensionchangeaftereventsignal.md)||
|[`PlayerInteractWithBlockAfterEvent`](./playerinteractwithblockafterevent.md)||
|[`PlayerInteractWithBlockAfterEventSignal`](./playerinteractwithblockaftereventsignal.md)||
|[`PlayerInteractWithBlockBeforeEvent`](./playerinteractwithblockbeforeevent.md)||
|[`PlayerInteractWithBlockBeforeEventSignal`](./playerinteractwithblockbeforeeventsignal.md)||
|[`PlayerInteractWithEntityAfterEvent`](./playerinteractwithentityafterevent.md)||
|[`PlayerInteractWithEntityAfterEventSignal`](./playerinteractwithentityaftereventsignal.md)||
|[`PlayerInteractWithEntityBeforeEvent`](./playerinteractwithentitybeforeevent.md)||
|[`PlayerInteractWithEntityBeforeEventSignal`](./playerinteractwithentitybeforeeventsignal.md)||
|[`PlayerJoinAfterEvent`](./playerjoinafterevent.md)||
|[`PlayerJoinAfterEventSignal`](./playerjoinaftereventsignal.md)||
|[`PlayerLeaveAfterEvent`](./playerleaveafterevent.md)||
|[`PlayerLeaveAfterEventSignal`](./playerleaveaftereventsignal.md)||
|[`PlayerLeaveBeforeEvent`](./playerleavebeforeevent.md)||
|[`PlayerLeaveBeforeEventSignal`](./playerleavebeforeeventsignal.md)||
|[`PlayerPlaceBlockAfterEvent`](./playerplaceblockafterevent.md)||
|[`PlayerPlaceBlockAfterEventSignal`](./playerplaceblockaftereventsignal.md)||
|[`PlayerSpawnAfterEvent`](./playerspawnafterevent.md)||
|[`PlayerSpawnAfterEventSignal`](./playerspawnaftereventsignal.md)||
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
|[`Structure`](./structure.md)||
|[`StructureManager`](./structuremanager.md)||
|[`System`](./system.md)||
|[`SystemAfterEvents`](./systemafterevents.md)||
|[`TargetBlockHitAfterEvent`](./targetblockhitafterevent.md)||
|[`TargetBlockHitAfterEventSignal`](./targetblockhitaftereventsignal.md)||
|[`TripWireTripAfterEvent`](./tripwiretripafterevent.md)||
|[`TripWireTripAfterEventSignal`](./tripwiretripaftereventsignal.md)||
|[`WeatherChangeAfterEvent`](./weatherchangeafterevent.md)||
|[`WeatherChangeAfterEventSignal`](./weatherchangeaftereventsignal.md)||
|[`World`](./world.md)||
|[`WorldAfterEvents`](./worldafterevents.md)||
|[`WorldBeforeEvents`](./worldbeforeevents.md)||
|[`WorldInitializeAfterEvent`](./worldinitializeafterevent.md)||
|[`WorldInitializeAfterEventSignal`](./worldinitializeaftereventsignal.md)||

## 接口

|接口|描述|
|---|---|
|[`BlockEventOptions`](./blockeventoptions.md)||
|[`BlockFilter`](./blockfilter.md)||
|[`BlockHitInformation`](./blockhitinformation.md)||
|[`BlockRaycastHit`](./blockraycasthit.md)||
|[`BlockRaycastOptions`](./blockraycastoptions.md)||
|[`CameraDefaultOptions`](./cameradefaultoptions.md)||
|[`CameraEaseOptions`](./cameraeaseoptions.md)||
|[`CameraFadeOptions`](./camerafadeoptions.md)||
|[`CameraFadeTimeOptions`](./camerafadetimeoptions.md)||
|[`CameraSetFacingOptions`](./camerasetfacingoptions.md)||
|[`CameraSetLocationOptions`](./camerasetlocationoptions.md)||
|[`CameraSetPosOptions`](./camerasetposoptions.md)||
|[`CameraSetRotOptions`](./camerasetrotoptions.md)||
|[`DefinitionModifier`](./definitionmodifier.md)||
|[`DimensionLocation`](./dimensionlocation.md)||
|[`EntityApplyDamageByProjectileOptions`](./entityapplydamagebyprojectileoptions.md)||
|[`EntityApplyDamageOptions`](./entityapplydamageoptions.md)||
|[`EntityDamageSource`](./entitydamagesource.md)||
|[`EntityDataDrivenTriggerEventOptions`](./entitydatadriventriggereventoptions.md)||
|[`EntityEffectOptions`](./entityeffectoptions.md)||
|[`EntityEventOptions`](./entityeventoptions.md)||
|[`EntityFilter`](./entityfilter.md)||
|[`EntityHitInformation`](./entityhitinformation.md)||
|[`EntityQueryOptions`](./entityqueryoptions.md)||
|[`EntityQueryScoreOptions`](./entityqueryscoreoptions.md)||
|[`EntityRaycastHit`](./entityraycasthit.md)||
|[`EntityRaycastOptions`](./entityraycastoptions.md)||
|[`ExplosionOptions`](./explosionoptions.md)||
|[`MusicOptions`](./musicoptions.md)||
|[`PlayAnimationOptions`](./playanimationoptions.md)||
|[`PlayerSoundOptions`](./playersoundoptions.md)||
|[`ProjectileShootOptions`](./projectileshootoptions.md)||
|[`RawMessage`](./rawmessage.md)||
|[`RawMessageScore`](./rawmessagescore.md)||
|[`RawText`](./rawtext.md)||
|[`RGB`](./rgb.md)||
|[`RGBA`](./rgba.md)||
|[`ScoreboardObjectiveDisplayOptions`](./scoreboardobjectivedisplayoptions.md)||
|[`ScriptEventMessageFilterOptions`](./scripteventmessagefilteroptions.md)||
|[`StructureCreateOptions`](./structurecreateoptions.md)||
|[`StructurePlaceOptions`](./structureplaceoptions.md)||
|[`TeleportOptions`](./teleportoptions.md)||
|[`TitleDisplayOptions`](./titledisplayoptions.md)||
|[`Vector2`](./vector2.md)||
|[`Vector3`](./vector3.md)||
|[`WorldSoundOptions`](./worldsoundoptions.md)||

## 枚举

|枚举|描述|
|---|---|
|[`BlockComponentTypes`](./blockcomponenttypes.md)||
|[`BlockPistonState`](./blockpistonstate.md)||
|[`Direction`](./direction.md)||
|[`DisplaySlotId`](./displayslotid.md)||
|[`DyeColor`](./dyecolor.md)||
|[`EasingType`](./easingtype.md)||
|[`EntityComponentTypes`](./entitycomponenttypes.md)||
|[`EntityDamageCause`](./entitydamagecause.md)||
|[`EntityInitializationCause`](./entityinitializationcause.md)||
|[`EquipmentSlot`](./equipmentslot.md)||
|[`FluidType`](./fluidtype.md)||
|[`GameMode`](./gamemode.md)||
|[`ItemComponentTypes`](./itemcomponenttypes.md)||
|[`ItemLockMode`](./itemlockmode.md)||
|[`MoonPhase`](./moonphase.md)||
|[`ObjectiveSortOrder`](./objectivesortorder.md)||
|[`ScoreboardIdentityType`](./scoreboardidentitytype.md)||
|[`ScriptEventSource`](./scripteventsource.md)||
|[`SignSide`](./signside.md)||
|[`StructureAnimationMode`](./structureanimationmode.md)||
|[`StructureMirrorAxis`](./structuremirroraxis.md)||
|[`StructureRotation`](./structurerotation.md)||
|[`StructureSaveMode`](./structuresavemode.md)||
|[`TimeOfDay`](./timeofday.md)||
|[`WeatherType`](./weathertype.md)||

## 错误

|错误|描述|
|---|---|
|[`CommandError`](./commanderror.md)||
|[`InvalidContainerSlotError`](./invalidcontainersloterror.md)||
|[`InvalidStructureError`](./invalidstructureerror.md)||
|[`LocationInUnloadedChunkError`](./locationinunloadedchunkerror.md)||
|[`LocationOutOfWorldBoundariesError`](./locationoutofworldboundarieserror.md)||
