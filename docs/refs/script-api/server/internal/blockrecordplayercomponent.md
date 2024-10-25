# `BlockRecordPlayerComponent`

> 文档版本：1.21.50.25

`BlockRecordPlayerComponent`类，扩展自[`BlockComponent`](./blockcomponent.md)。script_api.@minecraft/server.blockrecordplayercomponent.description

## 常量

/// define
`componentId`


///

```js
static read-only componentId = "minecraft:record_player";
```


## 方法

/// define
`ejectRecord`


///

script_api.@minecraft/server.blockrecordplayercomponent.ejectrecord.description

```js
ejectRecord(): void
```

/// html | div.result
//// define
返回值：`void`

- script_api.@minecraft/server.blockrecordplayercomponent.ejectrecord.return


////

///


/// define
`getRecord`


///

script_api.@minecraft/server.blockrecordplayercomponent.getrecord.description

```js
getRecord(): ItemStack | undefined
```

/// html | div.result
//// define
返回值：[`ItemStack`](./itemstack.md)|`undefined`

- script_api.@minecraft/server.blockrecordplayercomponent.getrecord.return


////

///


/// define
`isPlaying`


///

script_api.@minecraft/server.blockrecordplayercomponent.isplaying.description

```js
isPlaying(): boolean
```

/// html | div.result
//// define
返回值：`boolean`

- script_api.@minecraft/server.blockrecordplayercomponent.isplaying.return


////

///


/// define
`pauseRecord`


///

script_api.@minecraft/server.blockrecordplayercomponent.pauserecord.description

```js
pauseRecord(): void
```

/// html | div.result
//// define
返回值：`void`

- script_api.@minecraft/server.blockrecordplayercomponent.pauserecord.return


////

///


/// define
`playRecord`


///

script_api.@minecraft/server.blockrecordplayercomponent.playrecord.description

```js
playRecord(): void
```

/// html | div.result
//// define
返回值：`void`

- script_api.@minecraft/server.blockrecordplayercomponent.playrecord.return


////

///


/// define
`setRecord`


///

script_api.@minecraft/server.blockrecordplayercomponent.setrecord.description

```js
setRecord(recordItemType?: ItemType | string, startPlaying: boolean): void
```

/// html | div.result
//// define
`recordItemType`?：[`ItemType`](./itemtype.md)|`string`＝`null`

- script_api.@minecraft/server.blockrecordplayercomponent.setrecord.recorditemtype.description


////

//// define
`startPlaying`：`boolean`＝`True`

- script_api.@minecraft/server.blockrecordplayercomponent.setrecord.startplaying.description


////

//// define
返回值：`void`

- script_api.@minecraft/server.blockrecordplayercomponent.setrecord.return


////

///

