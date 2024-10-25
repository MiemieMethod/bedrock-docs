# `CompoundBlockVolume`

> 文档版本：1.21.50.25

`CompoundBlockVolume`类。script_api.@minecraft/server.compoundblockvolume.description

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

- script_api.@minecraft/server.compoundblockvolume.capacity.description


////

///


/// define
`items`


///

```js
read-only items: CompoundBlockVolumeItem[];
```

/// html | div.result
//// define
`items`：<code><a href="../compoundblockvolumeitem/">CompoundBlockVolumeItem</a>[]</code>

- script_api.@minecraft/server.compoundblockvolume.items.description


////

///


/// define
`itemsAbsolute`


///

```js
read-only itemsAbsolute: CompoundBlockVolumeItem[];
```

/// html | div.result
//// define
`itemsAbsolute`：<code><a href="../compoundblockvolumeitem/">CompoundBlockVolumeItem</a>[]</code>

- script_api.@minecraft/server.compoundblockvolume.itemsabsolute.description


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

- script_api.@minecraft/server.compoundblockvolume.volumecount.description


////

///


## 方法

/// define
`clear`


///

script_api.@minecraft/server.compoundblockvolume.clear.description

```js
clear(): void
```

/// html | div.result
//// define
返回值：`void`

- script_api.@minecraft/server.compoundblockvolume.clear.return


////

///


/// define
`constructor`


///

script_api.@minecraft/server.compoundblockvolume.constructor.description

```js
new constructor(origin?: Vector3): CompoundBlockVolume
```

/// html | div.result
//// define
`origin`?：[`Vector3`](./vector3.md)＝`null`

- script_api.@minecraft/server.compoundblockvolume.constructor.origin.description


////

//// define
返回值：[`CompoundBlockVolume`](./compoundblockvolume.md)

- script_api.@minecraft/server.compoundblockvolume.constructor.return


////

///


/// define
`getBlockLocationIterator`


///

script_api.@minecraft/server.compoundblockvolume.getblocklocationiterator.description

```js
getBlockLocationIterator(): BlockLocationIterator
```

/// html | div.result
//// define
返回值：[`BlockLocationIterator`](./blocklocationiterator.md)

- script_api.@minecraft/server.compoundblockvolume.getblocklocationiterator.return


////

///


/// define
`getBoundingBox`


///

script_api.@minecraft/server.compoundblockvolume.getboundingbox.description

```js
getBoundingBox(): BoundingBox
```

/// html | div.result
//// define
返回值：[`BoundingBox`](./boundingbox.md)

- script_api.@minecraft/server.compoundblockvolume.getboundingbox.return


////

///


/// define
`getMax`


///

script_api.@minecraft/server.compoundblockvolume.getmax.description

```js
getMax(): Vector3
```

/// html | div.result
//// define
返回值：[`Vector3`](./vector3.md)

- script_api.@minecraft/server.compoundblockvolume.getmax.return


////

///


/// define
`getMin`


///

script_api.@minecraft/server.compoundblockvolume.getmin.description

```js
getMin(): Vector3
```

/// html | div.result
//// define
返回值：[`Vector3`](./vector3.md)

- script_api.@minecraft/server.compoundblockvolume.getmin.return


////

///


/// define
`getOrigin`


///

script_api.@minecraft/server.compoundblockvolume.getorigin.description

```js
getOrigin(): Vector3
```

/// html | div.result
//// define
返回值：[`Vector3`](./vector3.md)

- script_api.@minecraft/server.compoundblockvolume.getorigin.return


////

///


/// define
`isEmpty`


///

script_api.@minecraft/server.compoundblockvolume.isempty.description

```js
isEmpty(): boolean
```

/// html | div.result
//// define
返回值：`boolean`

- script_api.@minecraft/server.compoundblockvolume.isempty.return


////

///


/// define
`isInside`


///

script_api.@minecraft/server.compoundblockvolume.isinside.description

```js
isInside(worldLocation: Vector3): boolean
```

/// html | div.result
//// define
`worldLocation`：[`Vector3`](./vector3.md)

- script_api.@minecraft/server.compoundblockvolume.isinside.worldlocation.description


////

//// define
返回值：`boolean`

- script_api.@minecraft/server.compoundblockvolume.isinside.return


////

///


/// define
`peekLastVolume`


///

script_api.@minecraft/server.compoundblockvolume.peeklastvolume.description

```js
peekLastVolume(forceRelativity?: CompoundBlockVolumePositionRelativity): CompoundBlockVolumeItem | undefined
```

/// html | div.result
//// define
`forceRelativity`?：[`CompoundBlockVolumePositionRelativity`](./compoundblockvolumepositionrelativity.md)＝`null`

- script_api.@minecraft/server.compoundblockvolume.peeklastvolume.forcerelativity.description


////

//// define
返回值：[`CompoundBlockVolumeItem`](./compoundblockvolumeitem.md)|`undefined`

- script_api.@minecraft/server.compoundblockvolume.peeklastvolume.return


////

///


/// define
`popVolume`


///

script_api.@minecraft/server.compoundblockvolume.popvolume.description

```js
popVolume(): boolean
```

/// html | div.result
//// define
返回值：`boolean`

- script_api.@minecraft/server.compoundblockvolume.popvolume.return


////

///


/// define
`pushVolume`


///

script_api.@minecraft/server.compoundblockvolume.pushvolume.description

```js
pushVolume(item: CompoundBlockVolumeItem): void
```

/// html | div.result
//// define
`item`：[`CompoundBlockVolumeItem`](./compoundblockvolumeitem.md)

- script_api.@minecraft/server.compoundblockvolume.pushvolume.item.description


////

//// define
返回值：`void`

- script_api.@minecraft/server.compoundblockvolume.pushvolume.return


////

///


/// define
`replaceOrAddLastVolume`


///

script_api.@minecraft/server.compoundblockvolume.replaceoraddlastvolume.description

```js
replaceOrAddLastVolume(item: CompoundBlockVolumeItem): boolean
```

/// html | div.result
//// define
`item`：[`CompoundBlockVolumeItem`](./compoundblockvolumeitem.md)

- script_api.@minecraft/server.compoundblockvolume.replaceoraddlastvolume.item.description


////

//// define
返回值：`boolean`

- script_api.@minecraft/server.compoundblockvolume.replaceoraddlastvolume.return


////

///


/// define
`setOrigin`


///

script_api.@minecraft/server.compoundblockvolume.setorigin.description

```js
setOrigin(position: Vector3, preserveExistingVolumes?: boolean): void
```

/// html | div.result
//// define
`position`：[`Vector3`](./vector3.md)

- script_api.@minecraft/server.compoundblockvolume.setorigin.position.description


////

//// define
`preserveExistingVolumes`?：`boolean`＝`null`

- script_api.@minecraft/server.compoundblockvolume.setorigin.preserveexistingvolumes.description


////

//// define
返回值：`void`

- script_api.@minecraft/server.compoundblockvolume.setorigin.return


////

///


/// define
`translateOrigin`


///

script_api.@minecraft/server.compoundblockvolume.translateorigin.description

```js
translateOrigin(delta: Vector3, preserveExistingVolumes?: boolean): void
```

/// html | div.result
//// define
`delta`：[`Vector3`](./vector3.md)

- script_api.@minecraft/server.compoundblockvolume.translateorigin.delta.description


////

//// define
`preserveExistingVolumes`?：`boolean`＝`null`

- script_api.@minecraft/server.compoundblockvolume.translateorigin.preserveexistingvolumes.description


////

//// define
返回值：`void`

- script_api.@minecraft/server.compoundblockvolume.translateorigin.return


////

///

