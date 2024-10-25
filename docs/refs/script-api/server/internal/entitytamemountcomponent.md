# `EntityTameMountComponent`

> 文档版本：1.21.50.25

`EntityTameMountComponent`类，扩展自[`EntityComponent`](./entitycomponent.md)。script_api.@minecraft/server.entitytamemountcomponent.description

## 常量

/// define
`componentId`


///

```js
static read-only componentId = "minecraft:tamemount";
```


## 属性

/// define
`isTamed`


///

```js
read-only isTamed: boolean;
```

/// html | div.result
//// define
`isTamed`：`boolean`

- script_api.@minecraft/server.entitytamemountcomponent.istamed.description


////

///


/// define
`isTamedToPlayer`


///

```js
read-only isTamedToPlayer: boolean;
```

/// html | div.result
//// define
`isTamedToPlayer`：`boolean`

- script_api.@minecraft/server.entitytamemountcomponent.istamedtoplayer.description


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

- script_api.@minecraft/server.entitytamemountcomponent.tamedtoplayer.description


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

- script_api.@minecraft/server.entitytamemountcomponent.tamedtoplayerid.description


////

///


## 方法

/// define
`tame`


///

script_api.@minecraft/server.entitytamemountcomponent.tame.description

```js
tame(showParticles: boolean): void
```

/// html | div.result
//// define
`showParticles`：`boolean`

- script_api.@minecraft/server.entitytamemountcomponent.tame.showparticles.description


////

//// define
返回值：`void`

- script_api.@minecraft/server.entitytamemountcomponent.tame.return


////

///


/// define
`tameToPlayer`


///

script_api.@minecraft/server.entitytamemountcomponent.tametoplayer.description

```js
tameToPlayer(showParticles: boolean, player: Player): boolean
```

/// html | div.result
//// define
`showParticles`：`boolean`

- script_api.@minecraft/server.entitytamemountcomponent.tametoplayer.showparticles.description


////

//// define
`player`：[`Player`](./player.md)

- script_api.@minecraft/server.entitytamemountcomponent.tametoplayer.player.description


////

//// define
返回值：`boolean`

- script_api.@minecraft/server.entitytamemountcomponent.tametoplayer.return


////

///

