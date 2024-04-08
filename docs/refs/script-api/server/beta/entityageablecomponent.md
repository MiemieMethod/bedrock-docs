# `EntityAgeableComponent`

> 文档版本：1.21.0.20

`EntityAgeableComponent`类，扩展自`[`EntityComponent`](./entitycomponent.md)`。

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

- 属性。


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

- 属性。


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

- 属性。


////

///


## 方法

/// define
`getDropItems`


///

```js
getDropItems(): string[]
```

/// html | div.result
//// define
返回值：`string[]`

- 返回值。


////

///


/// define
`getFeedItems`


///

```js
getFeedItems(): EntityDefinitionFeedItem[]
```

/// html | div.result
//// define
返回值：<code><a href="../entitydefinitionfeeditem/">EntityDefinitionFeedItem</a>[]</code>

- 返回值。


////

///

