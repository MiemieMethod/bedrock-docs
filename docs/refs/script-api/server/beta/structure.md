# `Structure`

> 文档版本：1.21.0.20

`Structure`类。

## 属性

/// define
`id`


///

```js
read-only id: string;
```


/// define
`size`


///

```js
read-only size: Vector3;
```


## 方法

/// define
`getBlockPermutation`


///

```js
getBlockPermutation(location: Vector3): BlockPermutation | undefined
```

/// html | div.result
//// define
`location`：[`Vector3`](./vector3.md)

- 参数1。


////

//// define
返回值：[`BlockPermutation`](./blockpermutation.md)|`undefined`

- 返回值。


////

///


/// define
`getIsWaterlogged`


///

```js
getIsWaterlogged(location: Vector3): boolean
```

/// html | div.result
//// define
`location`：[`Vector3`](./vector3.md)

- 参数1。


////

//// define
返回值：`boolean`

- 返回值。


////

///


/// define
`isValid`


///

```js
isValid(): boolean
```

/// html | div.result

///


/// define
`saveAs`


///

```js
saveAs(identifier: string, saveMode: StructureSaveMode): Structure
```

/// html | div.result
//// define
`identifier`：`string`

- 参数1。


////

//// define
`saveMode`：[`StructureSaveMode`](./structuresavemode.md)

- 参数2。


////

//// define
返回值：[`Structure`](./structure.md)

- 返回值。


////

///


/// define
`saveToWorld`


///

```js
saveToWorld(): void
```

/// html | div.result

///


/// define
`setBlockPermutation`


///

```js
setBlockPermutation(location: Vector3, blockPermutation?: BlockPermutation, waterlogged: boolean): void
```

/// html | div.result
//// define
`location`：[`Vector3`](./vector3.md)

- 参数1。


////

//// define
`blockPermutation`：[`BlockPermutation`](./blockpermutation.md)|`undefined`

- 参数2。


////

//// define
`waterlogged`：`boolean`

- 参数3。


////

//// define
返回值：`void`

- 返回值。


////

///

