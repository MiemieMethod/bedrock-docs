# `ItemCooldownComponent`

> 文档版本：1.21.60.21

`ItemCooldownComponent`类，扩展自[`ItemComponent`](./itemcomponent.md)。script_api.mojang-minecraft.itemcooldowncomponent.description

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

- script_api.mojang-minecraft.itemcooldowncomponent.cooldowncategory.description


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

- script_api.mojang-minecraft.itemcooldowncomponent.cooldownticks.description


////

///


## 方法

/// define
`startCooldown`


///

script_api.mojang-minecraft.itemcooldowncomponent.startcooldown.description

```js
startCooldown(player: Player): void
```

/// html | div.result
//// define
`player`：[`Player`](./player.md)

- script_api.mojang-minecraft.itemcooldowncomponent.startcooldown.player.description


////

//// define
返回值：`void`

- script_api.mojang-minecraft.itemcooldowncomponent.startcooldown.return


////

///

