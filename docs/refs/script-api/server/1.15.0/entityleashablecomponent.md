# `EntityLeashableComponent`

> 文档版本：1.21.50.25

`EntityLeashableComponent`类，扩展自[`EntityComponent`](./entitycomponent.md)。script_api.@minecraft/server.entityleashablecomponent.description

## 常量

/// define
`componentId`


///

```js
static read-only componentId = "minecraft:leashable";
```


## 属性

/// define
`canBeStolen`


///

```js
read-only canBeStolen: boolean;
```

/// html | div.result
//// define
`canBeStolen`：`boolean`

- script_api.@minecraft/server.entityleashablecomponent.canbestolen.description


////

///


/// define
`hardDistance`


///

```js
read-only hardDistance: float;
```

/// html | div.result
//// define
`hardDistance`：`float`

- script_api.@minecraft/server.entityleashablecomponent.harddistance.description


////

///


/// define
`isLeashed`


///

```js
read-only isLeashed: boolean;
```

/// html | div.result
//// define
`isLeashed`：`boolean`

- script_api.@minecraft/server.entityleashablecomponent.isleashed.description


////

///


/// define
`leashHolder`


///

```js
read-only leashHolder: Entity | undefined;
```

/// html | div.result
//// define
`leashHolder`：[`Entity`](./entity.md)|`undefined`

- script_api.@minecraft/server.entityleashablecomponent.leashholder.description


////

///


/// define
`leashHolderEntityId`


///

```js
read-only leashHolderEntityId: string | undefined;
```

/// html | div.result
//// define
`leashHolderEntityId`：`string`|`undefined`

- script_api.@minecraft/server.entityleashablecomponent.leashholderentityid.description


////

///


/// define
`maxDistance`


///

```js
read-only maxDistance: float;
```

/// html | div.result
//// define
`maxDistance`：`float`

- script_api.@minecraft/server.entityleashablecomponent.maxdistance.description


////

///


/// define
`softDistance`


///

```js
read-only softDistance: float;
```

/// html | div.result
//// define
`softDistance`：`float`

- script_api.@minecraft/server.entityleashablecomponent.softdistance.description


////

///


## 方法

/// define
`leashTo`


///

script_api.@minecraft/server.entityleashablecomponent.leashto.description

```js
leashTo(leashHolder: Entity): void
```

/// html | div.result
//// define
`leashHolder`：[`Entity`](./entity.md)

- script_api.@minecraft/server.entityleashablecomponent.leashto.leashholder.description


////

//// define
返回值：`void`

- script_api.@minecraft/server.entityleashablecomponent.leashto.return


////

///


/// define
`unleash`


///

script_api.@minecraft/server.entityleashablecomponent.unleash.description

```js
unleash(): void
```

/// html | div.result
//// define
返回值：`void`

- script_api.@minecraft/server.entityleashablecomponent.unleash.return


////

///

