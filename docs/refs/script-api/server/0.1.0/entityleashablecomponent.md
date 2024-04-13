# `EntityLeashableComponent`

> 文档版本：1.21.0.21

`EntityLeashableComponent`类，扩展自[`IEntityComponent`](./ientitycomponent.md)。script_api.mojang-minecraft.entityleashablecomponent.description

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

- script_api.mojang-minecraft.entityleashablecomponent.softdistance.description


////

///


## 方法

/// define
`leash`


///

script_api.mojang-minecraft.entityleashablecomponent.leash.description

```js
leash(leashHolder: Entity): void
```

/// html | div.result
//// define
`leashHolder`：[`Entity`](./entity.md)

- script_api.mojang-minecraft.entityleashablecomponent.leash.leashholder.description


////

//// define
返回值：`void`

- script_api.mojang-minecraft.entityleashablecomponent.leash.return


////

///


/// define
`unleash`


///

script_api.mojang-minecraft.entityleashablecomponent.unleash.description

```js
unleash(): void
```

/// html | div.result
//// define
返回值：`void`

- script_api.mojang-minecraft.entityleashablecomponent.unleash.return


////

///

