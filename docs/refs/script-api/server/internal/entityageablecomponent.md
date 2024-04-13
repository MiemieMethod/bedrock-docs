# `EntityAgeableComponent`

> 文档版本：1.21.0.21

`EntityAgeableComponent`类，扩展自[`EntityComponent`](./entitycomponent.md)。script_api.@minecraft/server.entityageablecomponent.description

## 常量

/// define
`componentId`


///

```js
static read-only componentId = "minecraft:ageable";
```


## 属性

/// define
`duration`


///

```js
read-only duration: float;
```

/// html | div.result
//// define
`duration`：`float`

- script_api.@minecraft/server.entityageablecomponent.duration.description


////

///


/// define
`growUp`


///

```js
read-only growUp: Trigger;
```

/// html | div.result
//// define
`growUp`：[`Trigger`](./trigger.md)

- script_api.@minecraft/server.entityageablecomponent.growup.description


////

///


/// define
`transformToItem`


///

```js
read-only transformToItem: string;
```

/// html | div.result
//// define
`transformToItem`：`string`

- script_api.@minecraft/server.entityageablecomponent.transformtoitem.description


////

///


## 方法

/// define
`getDropItems`


///

script_api.@minecraft/server.entityageablecomponent.getdropitems.description

```js
getDropItems(): string[]
```

/// html | div.result
//// define
返回值：`string[]`

- script_api.@minecraft/server.entityageablecomponent.getdropitems.return


////

///


/// define
`getFeedItems`


///

script_api.@minecraft/server.entityageablecomponent.getfeeditems.description

```js
getFeedItems(): EntityDefinitionFeedItem[]
```

/// html | div.result
//// define
返回值：<code><a href="../entitydefinitionfeeditem/">EntityDefinitionFeedItem</a>[]</code>

- script_api.@minecraft/server.entityageablecomponent.getfeeditems.return


////

///

