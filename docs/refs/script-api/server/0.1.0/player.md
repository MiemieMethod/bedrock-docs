# `Player`

> 文档版本：1.21.0.20

`Player`类，扩展自[`Entity`](./entity.md)。

## 属性

/// define
`name`


///

```js
read-only name: string;
```

/// html | div.result
//// define
`name`：`string`

- 属性。


////

///


/// define
`selectedSlot`


///

```js
selectedSlot: int32;
```

/// html | div.result
//// define
`selectedSlot`：`int32`

- 属性。


////

///


## 方法

/// define
`getItemCooldown`


///

```js
getItemCooldown(cooldownCategory: string): int32
```

/// html | div.result
//// define
`cooldownCategory`：`string`

- 参数1。


////

//// define
返回值：`int32`

- 返回值。


////

///


/// define
`playSound`


///

```js
playSound(soundId: string, soundOptions?: SoundOptions): void
```

/// html | div.result
//// define
`soundId`：`string`

- 参数1。


////

//// define
`soundOptions`：[`SoundOptions`](./soundoptions.md)|`undefined`

- 参数2。


////

//// define
返回值：`void`

- 返回值。


////

///


/// define
`postClientMessage`


///

```js
postClientMessage(id: string, value: string): void
```

/// html | div.result
//// define
`id`：`string`

- 参数1。


////

//// define
`value`：`string`

- 参数2。


////

//// define
返回值：`void`

- 返回值。


////

///


/// define
`startItemCooldown`


///

```js
startItemCooldown(cooldownCategory: string, tickDuration: int32): void
```

/// html | div.result
//// define
`cooldownCategory`：`string`

- 参数1。


////

//// define
`tickDuration`：`int32`

- 参数2。


////

//// define
返回值：`void`

- 返回值。


////

///

