# `EntityAgeableComponent`

> 文档版本：1.21.0.20

`EntityAgeableComponent`类，扩展自`EntityComponent`。

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


/// define
`growUp`


///

```js
read-only growUp: Trigger;
```


/// define
`transformToItem`


///

```js
read-only transformToItem: string;
```


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
返回值：<code><a href="../entitydefinitionfeeditem.md">EntityDefinitionFeedItem</a>[]</code>

- 返回值。


////

///

