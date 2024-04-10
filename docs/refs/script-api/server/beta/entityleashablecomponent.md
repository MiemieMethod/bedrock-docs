# `EntityLeashableComponent`

> 文档版本：1.21.0.20

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
`leash`


///

script_api.@minecraft/server.entityleashablecomponent.leash.description

```js
leash(leashHolder: Entity): void
```

/// html | div.result
//// define
`leashHolder`：[`Entity`](./entity.md)

- script_api.@minecraft/server.entityleashablecomponent.leash.leashholder.description


////

//// define
返回值：`void`

- script_api.@minecraft/server.entityleashablecomponent.leash.return


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

