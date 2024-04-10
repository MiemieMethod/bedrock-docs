# `ItemCooldownComponent`

> 文档版本：1.21.0.20

`ItemCooldownComponent`类，扩展自[`ItemComponent`](./itemcomponent.md)。script_api.@minecraft/server.itemcooldowncomponent.description

## 常量

/// define
`componentId`


///

```js
static read-only componentId = "minecraft:cooldown";
```


## 属性

/// define
`cooldownCategory`


///

```js
read-only cooldownCategory: string;
```

/// html | div.result
//// define
`cooldownCategory`：`string`

- script_api.@minecraft/server.itemcooldowncomponent.cooldowncategory.description


////

///


/// define
`cooldownTicks`


///

```js
read-only cooldownTicks: int32;
```

/// html | div.result
//// define
`cooldownTicks`：`int32`

- script_api.@minecraft/server.itemcooldowncomponent.cooldownticks.description


////

///


## 方法

/// define
`getCooldownTicksRemaining`


///

script_api.@minecraft/server.itemcooldowncomponent.getcooldownticksremaining.description

```js
getCooldownTicksRemaining(player: Player): int32
```

/// html | div.result
//// define
`player`：[`Player`](./player.md)

- script_api.@minecraft/server.itemcooldowncomponent.getcooldownticksremaining.player.description


////

//// define
返回值：`int32`

- script_api.@minecraft/server.itemcooldowncomponent.getcooldownticksremaining.return


////

///


/// define
`isCooldownCategory`


///

script_api.@minecraft/server.itemcooldowncomponent.iscooldowncategory.description

```js
isCooldownCategory(cooldownCategory: string): boolean
```

/// html | div.result
//// define
`cooldownCategory`：`string`

- script_api.@minecraft/server.itemcooldowncomponent.iscooldowncategory.cooldowncategory.description


////

//// define
返回值：`boolean`

- script_api.@minecraft/server.itemcooldowncomponent.iscooldowncategory.return


////

///


/// define
`startCooldown`


///

script_api.@minecraft/server.itemcooldowncomponent.startcooldown.description

```js
startCooldown(player: Player): void
```

/// html | div.result
//// define
`player`：[`Player`](./player.md)

- script_api.@minecraft/server.itemcooldowncomponent.startcooldown.player.description


////

//// define
返回值：`void`

- script_api.@minecraft/server.itemcooldowncomponent.startcooldown.return


////

///

