# `EntityTameableComponent`

> 文档版本：1.21.0.24

`EntityTameableComponent`类，扩展自[`EntityComponent`](./entitycomponent.md)。script_api.@minecraft/server.entitytameablecomponent.description

## 常量

/// define
`componentId`


///

```js
static read-only componentId = "minecraft:tameable";
```


## 属性

/// define
`getTameItems`


///

```js
read-only getTameItems: ItemStack[];
```

/// html | div.result
//// define
`getTameItems`：<code><a href="../itemstack/">ItemStack</a>[]</code>

- script_api.@minecraft/server.entitytameablecomponent.gettameitems.description


////

///


/// define
`isTamed`


///

```js
read-only isTamed: boolean;
```

/// html | div.result
//// define
`isTamed`：`boolean`

- script_api.@minecraft/server.entitytameablecomponent.istamed.description


////

///


/// define
`probability`


///

```js
read-only probability: float;
```

/// html | div.result
//// define
`probability`：`float`

- script_api.@minecraft/server.entitytameablecomponent.probability.description


////

///


/// define
`tamedToPlayer`


///

```js
read-only tamedToPlayer: Player | undefined;
```

/// html | div.result
//// define
`tamedToPlayer`：[`Player`](./player.md)|`undefined`

- script_api.@minecraft/server.entitytameablecomponent.tamedtoplayer.description


////

///


/// define
`tamedToPlayerId`


///

```js
read-only tamedToPlayerId: string | undefined;
```

/// html | div.result
//// define
`tamedToPlayerId`：`string`|`undefined`

- script_api.@minecraft/server.entitytameablecomponent.tamedtoplayerid.description


////

///


## 方法

/// define
`tame`


///

script_api.@minecraft/server.entitytameablecomponent.tame.description

```js
tame(player: Player): boolean
```

/// html | div.result
//// define
`player`：[`Player`](./player.md)

- script_api.@minecraft/server.entitytameablecomponent.tame.player.description


////

//// define
返回值：`boolean`

- script_api.@minecraft/server.entitytameablecomponent.tame.return


////

///

