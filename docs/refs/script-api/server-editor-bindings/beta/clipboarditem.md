# `ClipboardItem`

> 文档版本：1.21.0.20

`ClipboardItem`类。

## 属性

/// define
`isEmpty`


///

```js
read-only isEmpty: boolean;
```

/// html | div.result
//// define
`isEmpty`：`boolean`

- 属性。


////

///


## 方法

/// define
`clear`


///

```js
clear(): void
```

/// html | div.result
//// define
返回值：`void`

- 返回值。


////

///


/// define
`getPredictedWriteAsCompoundBlockVolume`


///

```js
getPredictedWriteAsCompoundBlockVolume(location: Vector3, options?: ClipboardWriteOptions): CompoundBlockVolume
```

/// html | div.result
//// define
`location`：[`Vector3`](../../server/beta/vector3.md)

- 参数1。


////

//// define
`options`：[`ClipboardWriteOptions`](./clipboardwriteoptions.md)|`undefined`

- 参数2。


////

//// define
返回值：[`CompoundBlockVolume`](../../server/beta/compoundblockvolume.md)

- 返回值。


////

///


/// define
`getPredictedWriteAsSelection`


///

```js
getPredictedWriteAsSelection(location: Vector3, options?: ClipboardWriteOptions): Selection
```

/// html | div.result
//// define
`location`：[`Vector3`](../../server/beta/vector3.md)

- 参数1。


////

//// define
`options`：[`ClipboardWriteOptions`](./clipboardwriteoptions.md)|`undefined`

- 参数2。


////

//// define
返回值：[`Selection`](./selection.md)

- 返回值。


////

///


/// define
`getSize`


///

```js
getSize(): Vector3
```

/// html | div.result
//// define
返回值：[`Vector3`](../../server/beta/vector3.md)

- 返回值。


////

///


/// define
`readFromSelection`


///

```js
readFromSelection(selection: Selection): void
```

/// html | div.result
//// define
`selection`：[`Selection`](./selection.md)

- 参数1。


////

//// define
返回值：`void`

- 返回值。


////

///


/// define
`readFromWorld`


///

```js
readFromWorld(from: Vector3, to: Vector3): void
```

/// html | div.result
//// define
`from`：[`Vector3`](../../server/beta/vector3.md)

- 参数1。


////

//// define
`to`：[`Vector3`](../../server/beta/vector3.md)

- 参数2。


////

//// define
返回值：`void`

- 返回值。


////

///


/// define
`writeToWorld`


///

```js
writeToWorld(location: Vector3, options?: ClipboardWriteOptions): boolean
```

/// html | div.result
//// define
`location`：[`Vector3`](../../server/beta/vector3.md)

- 参数1。


////

//// define
`options`：[`ClipboardWriteOptions`](./clipboardwriteoptions.md)|`undefined`

- 参数2。


////

//// define
返回值：`boolean`

- 返回值。


////

///

