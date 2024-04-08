# `EntityRideableComponent`

> 文档版本：1.21.0.20

`EntityRideableComponent`类，扩展自`[`EntityComponent`](./entitycomponent.md)`。

## 常量

/// define
`componentId`


///

```js
static read-only componentId = "minecraft:rideable";
```


## 属性

/// define
`controllingSeat`


///

```js
read-only controllingSeat: int32;
```

/// html | div.result
//// define
`controllingSeat`：`int32`

- 属性。


////

///


/// define
`crouchingSkipInteract`


///

```js
read-only crouchingSkipInteract: boolean;
```

/// html | div.result
//// define
`crouchingSkipInteract`：`boolean`

- 属性。


////

///


/// define
`interactText`


///

```js
read-only interactText: string;
```

/// html | div.result
//// define
`interactText`：`string`

- 属性。


////

///


/// define
`passengerMaxWidth`


///

```js
read-only passengerMaxWidth: float;
```

/// html | div.result
//// define
`passengerMaxWidth`：`float`

- 属性。


////

///


/// define
`pullInEntities`


///

```js
read-only pullInEntities: boolean;
```

/// html | div.result
//// define
`pullInEntities`：`boolean`

- 属性。


////

///


/// define
`riderCanInteract`


///

```js
read-only riderCanInteract: boolean;
```

/// html | div.result
//// define
`riderCanInteract`：`boolean`

- 属性。


////

///


/// define
`seatCount`


///

```js
read-only seatCount: int32;
```

/// html | div.result
//// define
`seatCount`：`int32`

- 属性。


////

///


## 方法

/// define
`addRider`


///

```js
addRider(rider: Entity): boolean
```

/// html | div.result
//// define
`rider`：[`Entity`](./entity.md)

- 参数1。


////

//// define
返回值：`boolean`

- 返回值。


////

///


/// define
`ejectRider`


///

```js
ejectRider(rider: Entity): void
```

/// html | div.result
//// define
`rider`：[`Entity`](./entity.md)

- 参数1。


////

//// define
返回值：`void`

- 返回值。


////

///


/// define
`ejectRiders`


///

```js
ejectRiders(): void
```

/// html | div.result
//// define
返回值：`void`

- 返回值。


////

///


/// define
`getFamilyTypes`


///

```js
getFamilyTypes(): string[]
```

/// html | div.result
//// define
返回值：`string[]`

- 返回值。


////

///


/// define
`getRiders`


///

```js
getRiders(): Entity[]
```

/// html | div.result
//// define
返回值：<code><a href="../entity/">Entity</a>[]</code>

- 返回值。


////

///


/// define
`getSeats`


///

```js
getSeats(): Seat[]
```

/// html | div.result
//// define
返回值：<code><a href="../seat/">Seat</a>[]</code>

- 返回值。


////

///

