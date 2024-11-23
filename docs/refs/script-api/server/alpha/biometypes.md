# `BiomeTypes`

> 文档版本：1.21.60.21

`BiomeTypes`类。Minecraft中可用生物群系的集合。

## 方法

/// define
`get`


///

获取一个指定的生物群系类型。

```js
static get(typeName: string): BiomeType | undefined
```

/// html | div.result
//// define
`typeName`：`string`

- 生物群系的标识符。


////

//// define
返回值：[`BiomeType`](./biometype.md)|`undefined`

- 如果该生物群系存在，返回该生物群系的`BiomeType`对象，否则返回`undefined`。


////

///


/// define
`getAll`


///

获取Minecraft中已注册的所有生物群系类型。

```js
static getAll(): BiomeType[]
```

/// html | div.result
//// define
返回值：<code><a href="../biometype/">BiomeType</a>[]</code>

- 一个包含所有生物群系的`BiomeType`对象数组。


////

///

