# `ItemDurabilityComponent`

> 文档版本：1.21.0.20

`ItemDurabilityComponent`类，扩展自[`ItemComponent`](./itemcomponent.md)。script_api.@minecraft/server.itemdurabilitycomponent.description

## 常量

/// define
`componentId`


///

```js
static read-only componentId = "minecraft:durability";
```


## 属性

/// define
`damage`


///

```js
damage: int32;
```

/// html | div.result
//// define
`damage`：`int32`

- script_api.@minecraft/server.itemdurabilitycomponent.damage.description


////

///


/// define
`maxDurability`


///

```js
read-only maxDurability: int32;
```

/// html | div.result
//// define
`maxDurability`：`int32`

- script_api.@minecraft/server.itemdurabilitycomponent.maxdurability.description


////

///


## 方法

/// define
`getDamageChance`


///

script_api.@minecraft/server.itemdurabilitycomponent.getdamagechance.description

```js
getDamageChance(unbreakingEnchantmentLevel: int32): int32
```

/// html | div.result
//// define
`unbreakingEnchantmentLevel`：`int32`

- script_api.@minecraft/server.itemdurabilitycomponent.unbreakingenchantmentlevel.getdamagechance.description


////

//// define
返回值：`int32`

- script_api.@minecraft/server.itemdurabilitycomponent.getdamagechance.return


////

///


/// define
`getDamageChanceRange`


///

script_api.@minecraft/server.itemdurabilitycomponent.getdamagechancerange.description

```js
getDamageChanceRange(): NumberRange
```

/// html | div.result
//// define
返回值：[`NumberRange`](../../common/1.1.0/numberrange.md)

- script_api.@minecraft/server.itemdurabilitycomponent.getdamagechancerange.return


////

///

