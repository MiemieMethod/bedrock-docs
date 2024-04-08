# `EntityLeashableComponent`

> 文档版本：1.21.0.20

`EntityLeashableComponent`类，扩展自`EntityComponent`。

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


## 方法

/// define
`leash`


///

```js
leash(leashHolder: Entity): void
```

/// html | div.result
//// define
`leashHolder`：[`Entity`](./entity.md)

- 参数1。


////

//// define
返回值：`void`

- 返回值。


////

///


/// define
`unleash`


///

```js
unleash(): void
```

/// html | div.result
//// define
返回值：`void`

- 返回值。


////

///

