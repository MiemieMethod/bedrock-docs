# `ItemDurabilityComponent`

> 文档版本：1.21.0.20

`ItemDurabilityComponent`类，扩展自`ItemComponent`。

## 常量

/// define
`componentId`


///

```js
static read-only componentId = minecraft:durability;
```


## 属性

/// define
`damage`


///

```js
damage: int32;
```


/// define
`maxDurability`


///

```js
read-only maxDurability: int32;
```


## 方法

/// define
`getDamageChance`


///

```js
getDamageChance(unbreakingEnchantmentLevel: int32): int32
```


/// define
`getDamageChanceRange`


///

```js
getDamageChanceRange(): NumberRange
```

