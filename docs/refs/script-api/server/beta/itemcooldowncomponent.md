# `ItemCooldownComponent`

> 文档版本：1.21.0.20

`ItemCooldownComponent`类，扩展自[`ItemComponent`](./itemcomponent.md)。

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

- 属性。


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

- 属性。


////

///


## 方法

/// define
`getCooldownTicksRemaining`


///

```js
getCooldownTicksRemaining(player: Player): int32
```

/// html | div.result
//// define
`player`：[`Player`](./player.md)

- 参数1。


////

//// define
返回值：`int32`

- 返回值。


////

///


/// define
`isCooldownCategory`


///

```js
isCooldownCategory(cooldownCategory: string): boolean
```

/// html | div.result
//// define
`cooldownCategory`：`string`

- 参数1。


////

//// define
返回值：`boolean`

- 返回值。


////

///


/// define
`startCooldown`


///

```js
startCooldown(player: Player): void
```

/// html | div.result
//// define
`player`：[`Player`](./player.md)

- 参数1。


////

//// define
返回值：`void`

- 返回值。


////

///

