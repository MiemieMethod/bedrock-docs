# `StructureManager`

> 文档版本：1.21.0.20

`StructureManager`类。

## 方法

/// define
`createEmpty`


///

```js
createEmpty(identifier: string, size: Vector3, saveMode: StructureSaveMode): Structure
```

/// html | div.result
//// define
`identifier`：`string`

- 参数1。


////

//// define
`size`：[`Vector3`](./vector3.md)

- 参数2。


////

//// define
`saveMode`：[`StructureSaveMode`](./structuresavemode.md)

- 参数3。


////

//// define
返回值：[`Structure`](./structure.md)

- 返回值。


////

///


/// define
`delete`


///

```js
delete(structure: string | Structure): boolean
```

/// html | div.result
//// define
`structure`：`string`|[`Structure`](./structure.md)

- 参数1。


////

//// define
返回值：`boolean`

- 返回值。


////

///


/// define
`get`


///

```js
get(identifier: string): Structure | undefined
```

/// html | div.result
//// define
`identifier`：`string`

- 参数1。


////

//// define
返回值：[`Structure`](./structure.md)|`undefined`

- 返回值。


////

///


/// define
`place`


///

```js
place(structure: string | Structure, dimension: Dimension, location: Vector3, options?: StructurePlaceOptions): void
```

/// html | div.result
//// define
`structure`：`string`|[`Structure`](./structure.md)

- 参数1。


////

//// define
`dimension`：[`Dimension`](./dimension.md)

- 参数2。


////

//// define
`location`：[`Vector3`](./vector3.md)

- 参数3。


////

//// define
`options`：[`StructurePlaceOptions`](./structureplaceoptions.md)|`undefined`

- 参数4。


////

//// define
返回值：`void`

- 返回值。


////

///

