# `ItemDurabilityComponent`

> 文档版本：1.21.0.24

`ItemDurabilityComponent`类，扩展自[`ItemComponent`](./itemcomponent.md)。script_api.mojang-minecraft.itemdurabilitycomponent.description

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

- script_api.mojang-minecraft.itemdurabilitycomponent.damage.description


////

///


/// define
`damageRange`


///

```js
read-only damageRange: NumberRange;
```

/// html | div.result
//// define
`damageRange`：[`NumberRange`](./numberrange.md)

- script_api.mojang-minecraft.itemdurabilitycomponent.damagerange.description


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

- script_api.mojang-minecraft.itemdurabilitycomponent.maxdurability.description


////

///


## 方法

/// define
`getDamageChance`


///

script_api.mojang-minecraft.itemdurabilitycomponent.getdamagechance.description

```js
getDamageChance(unbreakingEnchantmentLevel: int32): int32
```

/// html | div.result
//// define
`unbreakingEnchantmentLevel`：`int32`＝`0`∈[`0`, `3`]

- script_api.mojang-minecraft.itemdurabilitycomponent.getdamagechance.unbreakingenchantmentlevel.description


////

//// define
返回值：`int32`

- script_api.mojang-minecraft.itemdurabilitycomponent.getdamagechance.return


////

///

