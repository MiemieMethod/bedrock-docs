# `CompoundBlockVolume`

> 文档版本：1.21.0.20

`CompoundBlockVolume`类。

## 属性

/// define
`capacity`


///

```js
read-only capacity: uint64;
```

/// html | div.result
//// define
`capacity`：`uint64`

- 属性。


////

///


/// define
`volumeCount`


///

```js
read-only volumeCount: uint64;
```

/// html | div.result
//// define
`volumeCount`：`uint64`

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
`constructor`


///

```js
new constructor(origin?: Vector3): CompoundBlockVolume
```

/// html | div.result
//// define
`origin`：[`Vector3`](./vector3.md)|`undefined`

- 参数1。


////

//// define
返回值：[`CompoundBlockVolume`](./compoundblockvolume.md)

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
返回值：[`BlockLocationIterator`](./blocklocationiterator.md)

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
返回值：[`BoundingBox`](./boundingbox.md)

- 返回值。


////

///


/// define
`getMax`


///

```js
getMax(): Vector3
```

/// html | div.result
//// define
返回值：[`Vector3`](./vector3.md)

- 返回值。


////

///


/// define
`getMin`


///

```js
getMin(): Vector3
```

/// html | div.result
//// define
返回值：[`Vector3`](./vector3.md)

- 返回值。


////

///


/// define
`getOrigin`


///

```js
getOrigin(): Vector3
```

/// html | div.result
//// define
返回值：[`Vector3`](./vector3.md)

- 返回值。


////

///


/// define
`isEmpty`


///

```js
isEmpty(): boolean
```

/// html | div.result
//// define
返回值：`boolean`

- 返回值。


////

///


/// define
`isInside`


///

```js
isInside(worldLocation: Vector3): boolean
```

/// html | div.result
//// define
`worldLocation`：[`Vector3`](./vector3.md)

- 参数1。


////

//// define
返回值：`boolean`

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
`forceRelativity`：[`CompoundBlockVolumePositionRelativity`](./compoundblockvolumepositionrelativity.md)|`undefined`

- 参数1。


////

//// define
返回值：[`CompoundBlockVolumeItem`](./compoundblockvolumeitem.md)|`undefined`

- 返回值。


////

///


/// define
`popVolume`


///

```js
popVolume(): boolean
```

/// html | div.result
//// define
返回值：`boolean`

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
`item`：[`CompoundBlockVolumeItem`](./compoundblockvolumeitem.md)

- 参数1。


////

//// define
返回值：`void`

- 返回值。


////

///


/// define
`replaceOrAddLastVolume`


///

```js
replaceOrAddLastVolume(item: CompoundBlockVolumeItem): boolean
```

/// html | div.result
//// define
`item`：[`CompoundBlockVolumeItem`](./compoundblockvolumeitem.md)

- 参数1。


////

//// define
返回值：`boolean`

- 返回值。


////

///


/// define
`setOrigin`


///

```js
setOrigin(position: Vector3, preserveExistingVolumes?: boolean): void
```

/// html | div.result
//// define
`position`：[`Vector3`](./vector3.md)

- 参数1。


////

//// define
`preserveExistingVolumes`：`boolean`|`undefined`

- 参数2。


////

//// define
返回值：`void`

- 返回值。


////

///


/// define
`translateOrigin`


///

```js
translateOrigin(delta: Vector3, preserveExistingVolumes?: boolean): void
```

/// html | div.result
//// define
`delta`：[`Vector3`](./vector3.md)

- 参数1。


////

//// define
`preserveExistingVolumes`：`boolean`|`undefined`

- 参数2。


////

//// define
返回值：`void`

- 返回值。


////

///

