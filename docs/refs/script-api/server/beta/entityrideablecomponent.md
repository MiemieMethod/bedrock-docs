# `EntityRideableComponent`

> 文档版本：1.21.0.21

`EntityRideableComponent`类，扩展自[`EntityComponent`](./entitycomponent.md)。script_api.@minecraft/server.entityrideablecomponent.description

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

- script_api.@minecraft/server.entityrideablecomponent.controllingseat.description


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

- script_api.@minecraft/server.entityrideablecomponent.crouchingskipinteract.description


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

- script_api.@minecraft/server.entityrideablecomponent.interacttext.description


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

- script_api.@minecraft/server.entityrideablecomponent.passengermaxwidth.description


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

- script_api.@minecraft/server.entityrideablecomponent.pullinentities.description


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

- script_api.@minecraft/server.entityrideablecomponent.ridercaninteract.description


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

- script_api.@minecraft/server.entityrideablecomponent.seatcount.description


////

///


## 方法

/// define
`addRider`


///

script_api.@minecraft/server.entityrideablecomponent.addrider.description

```js
addRider(rider: Entity): boolean
```

/// html | div.result
//// define
`rider`：[`Entity`](./entity.md)

- script_api.@minecraft/server.entityrideablecomponent.addrider.rider.description


////

//// define
返回值：`boolean`

- script_api.@minecraft/server.entityrideablecomponent.addrider.return


////

///


/// define
`ejectRider`


///

script_api.@minecraft/server.entityrideablecomponent.ejectrider.description

```js
ejectRider(rider: Entity): void
```

/// html | div.result
//// define
`rider`：[`Entity`](./entity.md)

- script_api.@minecraft/server.entityrideablecomponent.ejectrider.rider.description


////

//// define
返回值：`void`

- script_api.@minecraft/server.entityrideablecomponent.ejectrider.return


////

///


/// define
`ejectRiders`


///

script_api.@minecraft/server.entityrideablecomponent.ejectriders.description

```js
ejectRiders(): void
```

/// html | div.result
//// define
返回值：`void`

- script_api.@minecraft/server.entityrideablecomponent.ejectriders.return


////

///


/// define
`getFamilyTypes`


///

script_api.@minecraft/server.entityrideablecomponent.getfamilytypes.description

```js
getFamilyTypes(): string[]
```

/// html | div.result
//// define
返回值：`string[]`

- script_api.@minecraft/server.entityrideablecomponent.getfamilytypes.return


////

///


/// define
`getRiders`


///

script_api.@minecraft/server.entityrideablecomponent.getriders.description

```js
getRiders(): Entity[]
```

/// html | div.result
//// define
返回值：<code><a href="../entity/">Entity</a>[]</code>

- script_api.@minecraft/server.entityrideablecomponent.getriders.return


////

///


/// define
`getSeats`


///

script_api.@minecraft/server.entityrideablecomponent.getseats.description

```js
getSeats(): Seat[]
```

/// html | div.result
//// define
返回值：<code><a href="../seat/">Seat</a>[]</code>

- script_api.@minecraft/server.entityrideablecomponent.getseats.return


////

///

