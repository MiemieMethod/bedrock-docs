# `EntityRideableComponent`

> 文档版本：1.21.0.20

`EntityRideableComponent`类，扩展自`EntityComponent`。

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


/// define
`crouchingSkipInteract`


///

```js
read-only crouchingSkipInteract: boolean;
```


/// define
`interactText`


///

```js
read-only interactText: string;
```


/// define
`passengerMaxWidth`


///

```js
read-only passengerMaxWidth: float;
```


/// define
`pullInEntities`


///

```js
read-only pullInEntities: boolean;
```


/// define
`riderCanInteract`


///

```js
read-only riderCanInteract: boolean;
```


/// define
`seatCount`


///

```js
read-only seatCount: int32;
```


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

