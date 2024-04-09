# `EntityTameableComponent`

> 文档版本：1.21.0.20

`EntityTameableComponent`类，扩展自[`EntityComponent`](./entitycomponent.md)。script_api.@minecraft/server.entitytameablecomponent.description

## 常量

/// define
`componentId`


///

```js
static read-only componentId = "minecraft:tameable";
```


## 属性

/// define
`probability`


///

```js
read-only probability: float;
```

/// html | div.result
//// define
`probability`：`float`

- script_api.@minecraft/server.entitytameablecomponent.probability.description


////

///


## 方法

/// define
`getTameItems`


///

script_api.@minecraft/server.entitytameablecomponent.gettameitems.description

```js
getTameItems(): string[]
```

/// html | div.result
//// define
返回值：`string[]`

- script_api.@minecraft/server.entitytameablecomponent.gettameitems.return


////

///


/// define
`tame`


///

script_api.@minecraft/server.entitytameablecomponent.tame.description

```js
tame(): boolean
```

/// html | div.result
//// define
返回值：`boolean`

- script_api.@minecraft/server.entitytameablecomponent.tame.return


////

///

