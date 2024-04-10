# `EntityRideableComponent`

> 文档版本：1.21.0.20

`EntityRideableComponent`类，扩展自[`IEntityComponent`](./ientitycomponent.md)。script_api.mojang-minecraft.entityrideablecomponent.description

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

- script_api.mojang-minecraft.entityrideablecomponent.controllingseat.description


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

- script_api.mojang-minecraft.entityrideablecomponent.crouchingskipinteract.description


////

///


/// define
`familyTypes`


///

```js
read-only familyTypes: string[];
```

/// html | div.result
//// define
`familyTypes`：`string[]`

- script_api.mojang-minecraft.entityrideablecomponent.familytypes.description


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

- script_api.mojang-minecraft.entityrideablecomponent.interacttext.description


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

- script_api.mojang-minecraft.entityrideablecomponent.pullinentities.description


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

- script_api.mojang-minecraft.entityrideablecomponent.ridercaninteract.description


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

- script_api.mojang-minecraft.entityrideablecomponent.seatcount.description


////

///


/// define
`seats`


///

```js
read-only seats: Seat[];
```

/// html | div.result
//// define
`seats`：<code><a href="../seat/">Seat</a>[]</code>

- script_api.mojang-minecraft.entityrideablecomponent.seats.description


////

///


## 方法

/// define
`addRider`


///

script_api.mojang-minecraft.entityrideablecomponent.addrider.description

```js
addRider(rider: Entity): boolean
```

/// html | div.result
//// define
`rider`：[`Entity`](./entity.md)

- script_api.mojang-minecraft.entityrideablecomponent.addrider.rider.description


////

//// define
返回值：`boolean`

- script_api.mojang-minecraft.entityrideablecomponent.addrider.return


////

///


/// define
`ejectRider`


///

script_api.mojang-minecraft.entityrideablecomponent.ejectrider.description

```js
ejectRider(rider: Entity): void
```

/// html | div.result
//// define
`rider`：[`Entity`](./entity.md)

- script_api.mojang-minecraft.entityrideablecomponent.ejectrider.rider.description


////

//// define
返回值：`void`

- script_api.mojang-minecraft.entityrideablecomponent.ejectrider.return


////

///


/// define
`ejectRiders`


///

script_api.mojang-minecraft.entityrideablecomponent.ejectriders.description

```js
ejectRiders(): void
```

/// html | div.result
//// define
返回值：`void`

- script_api.mojang-minecraft.entityrideablecomponent.ejectriders.return


////

///

