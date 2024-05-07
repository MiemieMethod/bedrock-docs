# `@minecraft/server`

> 文档版本：1.21.0.24

`@minecraft/server`模块的`1.1.0`版本，UUID为`b26a4d4c-afdf-4690-88f8-931846312678`。该模块是服务端的基础模块。

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
|[`BlockPermutation`](./blockpermutation.md)||
|[`CommandResult`](./commandresult.md)||
|[`Dimension`](./dimension.md)||
|[`Entity`](./entity.md)||
|[`MinecraftDimensionTypes`](./minecraftdimensiontypes.md)||
|[`Player`](./player.md)||
|[`System`](./system.md)||
|[`World`](./world.md)||

## 接口

|接口|描述|
|---|---|
|[`EntityFilter`](./entityfilter.md)||
|[`EntityQueryOptions`](./entityqueryoptions.md)||
|[`EntityQueryScoreOptions`](./entityqueryscoreoptions.md)||
|[`RawMessage`](./rawmessage.md)||
|[`RawMessageScore`](./rawmessagescore.md)||
|[`Vector3`](./vector3.md)||

## 枚举

|枚举|描述|
|---|---|
|[`GameMode`](./gamemode.md)||

## 错误

|错误|描述|
|---|---|
|[`LocationInUnloadedChunkError`](./locationinunloadedchunkerror.md)||
|[`LocationOutOfWorldBoundariesError`](./locationoutofworldboundarieserror.md)||
