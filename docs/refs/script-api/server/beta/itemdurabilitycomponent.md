# `ItemDurabilityComponent`

> 文档版本：1.21.0.20

`ItemDurabilityComponent`类，扩展自`ItemComponent`。

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

/// html | div.result
//// define
`unbreakingEnchantmentLevel`：`int32`

- 参数1。


////

//// define
返回值：`int32`

- 返回值。


////

///


/// define
`getDamageChanceRange`


///

```js
getDamageChanceRange(): NumberRange
```

/// html | div.result
//// define
返回值：[`NumberRange`](../../common/1.1.0/numberrange.md)

- 返回值。


////

///

