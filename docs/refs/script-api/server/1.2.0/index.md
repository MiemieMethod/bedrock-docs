# `@minecraft/server`

> 文档版本：1.21.60.21

`@minecraft/server`模块的`1.2.0`版本，UUID为`b26a4d4c-afdf-4690-88f8-931846312678`。该模块是服务端的基础模块。

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
|[`BlockInventoryComponent`](./blockinventorycomponent.md)||
|[`BlockPermutation`](./blockpermutation.md)||
|[`CommandResult`](./commandresult.md)||
|[`Component`](./component.md)||
|[`Container`](./container.md)||
|[`Dimension`](./dimension.md)||
|[`Entity`](./entity.md)||
|[`EntityBaseMovementComponent`](./entitybasemovementcomponent.md)||
|[`EntityCanClimbComponent`](./entitycanclimbcomponent.md)||
|[`EntityCanFlyComponent`](./entitycanflycomponent.md)||
|[`EntityCanPowerJumpComponent`](./entitycanpowerjumpcomponent.md)||
|[`EntityColorComponent`](./entitycolorcomponent.md)||
|[`EntityComponent`](./entitycomponent.md)||
|[`EntityFireImmuneComponent`](./entityfireimmunecomponent.md)||
|[`EntityFloatsInLiquidComponent`](./entityfloatsinliquidcomponent.md)||
|[`EntityFlyingSpeedComponent`](./entityflyingspeedcomponent.md)||
|[`EntityFrictionModifierComponent`](./entityfrictionmodifiercomponent.md)||
|[`EntityGroundOffsetComponent`](./entitygroundoffsetcomponent.md)||
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
|[`ItemComponent`](./itemcomponent.md)||
|[`ItemStack`](./itemstack.md)||
|[`ItemType`](./itemtype.md)||
|[`MinecraftDimensionTypes`](./minecraftdimensiontypes.md)||
|[`Player`](./player.md)||
|[`System`](./system.md)||
|[`World`](./world.md)||

## 接口

|接口|描述|
|---|---|
|[`EntityApplyDamageByProjectileOptions`](./entityapplydamagebyprojectileoptions.md)||
|[`EntityApplyDamageOptions`](./entityapplydamageoptions.md)||
|[`EntityFilter`](./entityfilter.md)||
|[`EntityQueryOptions`](./entityqueryoptions.md)||
|[`EntityQueryScoreOptions`](./entityqueryscoreoptions.md)||
|[`MusicOptions`](./musicoptions.md)||
|[`PlayerSoundOptions`](./playersoundoptions.md)||
|[`RawMessage`](./rawmessage.md)||
|[`RawMessageScore`](./rawmessagescore.md)||
|[`Vector3`](./vector3.md)||
|[`WorldSoundOptions`](./worldsoundoptions.md)||

## 枚举

|枚举|描述|
|---|---|
|[`EntityDamageCause`](./entitydamagecause.md)||
|[`GameMode`](./gamemode.md)||
|[`ItemLockMode`](./itemlockmode.md)||

## 错误

|错误|描述|
|---|---|
|[`CommandError`](./commanderror.md)||
|[`LocationInUnloadedChunkError`](./locationinunloadedchunkerror.md)||
|[`LocationOutOfWorldBoundariesError`](./locationoutofworldboundarieserror.md)||
