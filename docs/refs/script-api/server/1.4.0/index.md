# `@minecraft/server`

> 文档版本：1.21.0.20

`@minecraft/server`模块的`1.4.0`版本，UUID为`b26a4d4c-afdf-4690-88f8-931846312678`。该模块是服务端的基础模块。

/// info | 依赖
该模块依赖于以下模块：

- `@minecraft/common`|`1.0.0`|`77ec12b4-1b2b-4c98-8d34-d1cd63f849d5`
///

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

- script_api.@minecraft/server.locationoutofworldboundarieserror.system.description


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

- script_api.@minecraft/server.locationoutofworldboundarieserror.world.description


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
|[`ButtonPushAfterEvent`](./buttonpushafterevent.md)||
|[`ButtonPushAfterEventSignal`](./buttonpushaftereventsignal.md)||
|[`CommandResult`](./commandresult.md)||
|[`Component`](./component.md)||
|[`Container`](./container.md)||
|[`Dimension`](./dimension.md)||
|[`Effect`](./effect.md)||
|[`EffectType`](./effecttype.md)||
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
|[`EntityMarkVariantComponent`](./entitymarkvariantcomponent.md)||
|[`EntityMovementAmphibiousComponent`](./entitymovementamphibiouscomponent.md)||
|[`EntityMovementBasicComponent`](./entitymovementbasiccomponent.md)||
|[`EntityMovementFlyComponent`](./entitymovementflycomponent.md)||
|[`EntityMovementGenericComponent`](./entitymovementgenericcomponent.md)||
|[`EntityMovementHoverComponent`](./entitymovementhovercomponent.md)||
|[`EntityMovementJumpComponent`](./entitymovementjumpcomponent.md)||
|[`EntityMovementSkipComponent`](./entitymovementskipcomponent.md)||
|[`EntityPushThroughComponent`](./entitypushthroughcomponent.md)||
|[`EntityScaleComponent`](./entityscalecomponent.md)||
|[`EntitySkinIdComponent`](./entityskinidcomponent.md)||
|[`EntityVariantComponent`](./entityvariantcomponent.md)||
|[`EntityWantsJockeyComponent`](./entitywantsjockeycomponent.md)||
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
|[`Player`](./player.md)||
|[`PlayerJoinAfterEvent`](./playerjoinafterevent.md)||
|[`PlayerJoinAfterEventSignal`](./playerjoinaftereventsignal.md)||
|[`PlayerLeaveAfterEvent`](./playerleaveafterevent.md)||
|[`PlayerLeaveAfterEventSignal`](./playerleaveaftereventsignal.md)||
|[`PlayerSpawnAfterEvent`](./playerspawnafterevent.md)||
|[`PlayerSpawnAfterEventSignal`](./playerspawnaftereventsignal.md)||
|[`PressurePlatePopAfterEvent`](./pressureplatepopafterevent.md)||
|[`PressurePlatePopAfterEventSignal`](./pressureplatepopaftereventsignal.md)||
|[`PressurePlatePushAfterEvent`](./pressureplatepushafterevent.md)||
|[`PressurePlatePushAfterEventSignal`](./pressureplatepushaftereventsignal.md)||
|[`Scoreboard`](./scoreboard.md)||
|[`ScoreboardIdentity`](./scoreboardidentity.md)||
|[`ScoreboardObjective`](./scoreboardobjective.md)||
|[`ScoreboardScoreInfo`](./scoreboardscoreinfo.md)||
|[`ScreenDisplay`](./screendisplay.md)||
|[`ScriptEventCommandMessageAfterEvent`](./scripteventcommandmessageafterevent.md)||
|[`ScriptEventCommandMessageAfterEventSignal`](./scripteventcommandmessageaftereventsignal.md)||
|[`System`](./system.md)||
|[`SystemAfterEvents`](./systemafterevents.md)||
|[`TargetBlockHitAfterEvent`](./targetblockhitafterevent.md)||
|[`TargetBlockHitAfterEventSignal`](./targetblockhitaftereventsignal.md)||
|[`TripWireTripAfterEvent`](./tripwiretripafterevent.md)||
|[`TripWireTripAfterEventSignal`](./tripwiretripaftereventsignal.md)||
|[`World`](./world.md)||
|[`WorldAfterEvents`](./worldafterevents.md)||
|[`WorldBeforeEvents`](./worldbeforeevents.md)||

## 接口

|接口|描述|
|---|---|
|[`BlockFilter`](./blockfilter.md)||
|[`BlockRaycastHit`](./blockraycasthit.md)||
|[`BlockRaycastOptions`](./blockraycastoptions.md)||
|[`DimensionLocation`](./dimensionlocation.md)||
|[`EntityApplyDamageByProjectileOptions`](./entityapplydamagebyprojectileoptions.md)||
|[`EntityApplyDamageOptions`](./entityapplydamageoptions.md)||
|[`EntityDamageSource`](./entitydamagesource.md)||
|[`EntityEffectOptions`](./entityeffectoptions.md)||
|[`EntityEventOptions`](./entityeventoptions.md)||
|[`EntityFilter`](./entityfilter.md)||
|[`EntityQueryOptions`](./entityqueryoptions.md)||
|[`EntityQueryScoreOptions`](./entityqueryscoreoptions.md)||
|[`EntityRaycastHit`](./entityraycasthit.md)||
|[`EntityRaycastOptions`](./entityraycastoptions.md)||
|[`MusicOptions`](./musicoptions.md)||
|[`PlayerSoundOptions`](./playersoundoptions.md)||
|[`RawMessage`](./rawmessage.md)||
|[`RawMessageScore`](./rawmessagescore.md)||
|[`ScoreboardObjectiveDisplayOptions`](./scoreboardobjectivedisplayoptions.md)||
|[`ScriptEventMessageFilterOptions`](./scripteventmessagefilteroptions.md)||
|[`TeleportOptions`](./teleportoptions.md)||
|[`TitleDisplayOptions`](./titledisplayoptions.md)||
|[`Vector2`](./vector2.md)||
|[`Vector3`](./vector3.md)||
|[`WorldSoundOptions`](./worldsoundoptions.md)||

## 枚举

|枚举|描述|
|---|---|
|[`Direction`](./direction.md)||
|[`DisplaySlotId`](./displayslotid.md)||
|[`EntityDamageCause`](./entitydamagecause.md)||
|[`GameMode`](./gamemode.md)||
|[`ItemLockMode`](./itemlockmode.md)||
|[`ObjectiveSortOrder`](./objectivesortorder.md)||
|[`ScoreboardIdentityType`](./scoreboardidentitytype.md)||
|[`ScriptEventSource`](./scripteventsource.md)||
|[`TimeOfDay`](./timeofday.md)||

## 错误

|错误|描述|
|---|---|
|[`CommandError`](./commanderror.md)||
|[`LocationInUnloadedChunkError`](./locationinunloadedchunkerror.md)||
|[`LocationOutOfWorldBoundariesError`](./locationoutofworldboundarieserror.md)||
