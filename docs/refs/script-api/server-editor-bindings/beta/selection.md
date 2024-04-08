# `Selection`

> 文档版本：1.21.0.20

`Selection`类。

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


/// define
`visible`


///

```js
visible: boolean;
```

/// html | div.result
//// define
`visible`：`boolean`

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
`getBlockLocationIterator`


///

```js
getBlockLocationIterator(): BlockLocationIterator
```

/// html | div.result
//// define
返回值：[`BlockLocationIterator`](../../server/beta/blocklocationiterator.md)

- 返回值。


////

///


/// define
`getBoundingBox`


///

```js
getBoundingBox(): BoundingBox
```

/// html | div.result
//// define
返回值：[`BoundingBox`](../../server/beta/boundingbox.md)

- 返回值。


////

///


/// define
`getFillColor`


///

```js
getFillColor(): RGBA
```

/// html | div.result
//// define
返回值：[`RGBA`](../../server/beta/rgba.md)

- 返回值。


////

///


/// define
`getOutlineColor`


///

```js
getOutlineColor(): RGBA
```

/// html | div.result
//// define
返回值：[`RGBA`](../../server/beta/rgba.md)

- 返回值。


////

///


/// define
`getVolumeOrigin`


///

```js
getVolumeOrigin(): Vector3
```

/// html | div.result
//// define
返回值：[`Vector3`](../../server/beta/vector3.md)

- 返回值。


////

///


/// define
`moveBy`


///

```js
moveBy(delta: Vector3): Vector3
```

/// html | div.result
//// define
`delta`：[`Vector3`](../../server/beta/vector3.md)

- 参数1。


////

//// define
返回值：[`Vector3`](../../server/beta/vector3.md)

- 返回值。


////

///


/// define
`moveTo`


///

```js
moveTo(location: Vector3): Vector3
```

/// html | div.result
//// define
`location`：[`Vector3`](../../server/beta/vector3.md)

- 参数1。


////

//// define
返回值：[`Vector3`](../../server/beta/vector3.md)

- 返回值。


////

///


/// define
`peekLastVolume`


///

```js
peekLastVolume(forceRelativity?: CompoundBlockVolumePositionRelativity): CompoundBlockVolumeItem | undefined
```

/// html | div.result
//// define
`forceRelativity`：[`CompoundBlockVolumePositionRelativity`](../../server/beta/compoundblockvolumepositionrelativity.md)|`undefined`

- 参数1。


////

//// define
返回值：[`CompoundBlockVolumeItem`](../../server/beta/compoundblockvolumeitem.md)|`undefined`

- 返回值。


////

///


/// define
`popVolume`


///

```js
popVolume(): void
```

/// html | div.result
//// define
返回值：`void`

- 返回值。


////

///


/// define
`pushVolume`


///

```js
pushVolume(item: CompoundBlockVolumeItem): void
```

/// html | div.result
//// define
`item`：[`CompoundBlockVolumeItem`](../../server/beta/compoundblockvolumeitem.md)

- 参数1。


////

//// define
返回值：`void`

- 返回值。


////

///


/// define
`set`


///

```js
set(other: CompoundBlockVolume | Selection): void
```

/// html | div.result
//// define
`other`：[`CompoundBlockVolume`](../../server/beta/compoundblockvolume.md)|[`Selection`](./selection.md)

- 参数1。


////

//// define
返回值：`void`

- 返回值。


////

///


/// define
`setFillColor`


///

```js
setFillColor(color: RGBA): void
```

/// html | div.result
//// define
`color`：[`RGBA`](../../server/beta/rgba.md)

- 参数1。


////

//// define
返回值：`void`

- 返回值。


////

///


/// define
`setOutlineColor`


///

```js
setOutlineColor(color: RGBA): void
```

/// html | div.result
//// define
`color`：[`RGBA`](../../server/beta/rgba.md)

- 参数1。


////

//// define
返回值：`void`

- 返回值。


////

///

