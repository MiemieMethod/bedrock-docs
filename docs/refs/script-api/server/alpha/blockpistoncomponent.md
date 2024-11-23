# `BlockPistonComponent`

> 文档版本：1.21.60.21

`BlockPistonComponent`类，扩展自[`BlockComponent`](./blockcomponent.md)。script_api.@minecraft/server.blockpistoncomponent.description

## 常量

/// define
`componentId`


///

```js
static read-only componentId = "minecraft:piston";
```


## 属性

/// define
`isMoving`


///

```js
read-only isMoving: boolean;
```

/// html | div.result
//// define
`isMoving`：`boolean`

- script_api.@minecraft/server.blockpistoncomponent.ismoving.description


////

///


/// define
`state`


///

```js
read-only state: BlockPistonState;
```

/// html | div.result
//// define
`state`：[`BlockPistonState`](./blockpistonstate.md)

- script_api.@minecraft/server.blockpistoncomponent.state.description


////

///


## 方法

/// define
`getAttachedBlocks`


///

script_api.@minecraft/server.blockpistoncomponent.getattachedblocks.description

```js
getAttachedBlocks(): Block[]
```

/// html | div.result
//// define
返回值：<code><a href="../block/">Block</a>[]</code>

- script_api.@minecraft/server.blockpistoncomponent.getattachedblocks.return


////

///


/// define
`getAttachedBlocksLocations`


///

script_api.@minecraft/server.blockpistoncomponent.getattachedblockslocations.description

```js
getAttachedBlocksLocations(): Vector3[]
```

/// html | div.result
//// define
返回值：<code><a href="../vector3/">Vector3</a>[]</code>

- script_api.@minecraft/server.blockpistoncomponent.getattachedblockslocations.return


////

///

