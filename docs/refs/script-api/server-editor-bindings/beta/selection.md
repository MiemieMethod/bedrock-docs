# `Selection`

> 文档版本：1.21.0.20

`Selection`类。script_api.@minecraft/server-editor-bindings.selection.description

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

- script_api.@minecraft/server-editor-bindings.selection.isempty.description


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

- script_api.@minecraft/server-editor-bindings.selection.visible.description


////

///


## 方法

/// define
`clear`


///

script_api.@minecraft/server-editor-bindings.selection.clear.description

```js
clear(): void
```

/// html | div.result
//// define
返回值：`void`

- script_api.@minecraft/server-editor-bindings.selection.clear.return


////

///


/// define
`getBlockLocationIterator`


///

script_api.@minecraft/server-editor-bindings.selection.getblocklocationiterator.description

```js
getBlockLocationIterator(): BlockLocationIterator
```

/// html | div.result
//// define
返回值：[`BlockLocationIterator`](../../server/beta/blocklocationiterator.md)

- script_api.@minecraft/server-editor-bindings.selection.getblocklocationiterator.return


////

///


/// define
`getBoundingBox`


///

script_api.@minecraft/server-editor-bindings.selection.getboundingbox.description

```js
getBoundingBox(): BoundingBox
```

/// html | div.result
//// define
返回值：[`BoundingBox`](../../server/beta/boundingbox.md)

- script_api.@minecraft/server-editor-bindings.selection.getboundingbox.return


////

///


/// define
`getFillColor`


///

script_api.@minecraft/server-editor-bindings.selection.getfillcolor.description

```js
getFillColor(): RGBA
```

/// html | div.result
//// define
返回值：[`RGBA`](../../server/beta/rgba.md)

- script_api.@minecraft/server-editor-bindings.selection.getfillcolor.return


////

///


/// define
`getOutlineColor`


///

script_api.@minecraft/server-editor-bindings.selection.getoutlinecolor.description

```js
getOutlineColor(): RGBA
```

/// html | div.result
//// define
返回值：[`RGBA`](../../server/beta/rgba.md)

- script_api.@minecraft/server-editor-bindings.selection.getoutlinecolor.return


////

///


/// define
`getVolumeOrigin`


///

script_api.@minecraft/server-editor-bindings.selection.getvolumeorigin.description

```js
getVolumeOrigin(): Vector3
```

/// html | div.result
//// define
返回值：[`Vector3`](../../server/beta/vector3.md)

- script_api.@minecraft/server-editor-bindings.selection.getvolumeorigin.return


////

///


/// define
`moveBy`


///

script_api.@minecraft/server-editor-bindings.selection.moveby.description

```js
moveBy(delta: Vector3): Vector3
```

/// html | div.result
//// define
`delta`：[`Vector3`](../../server/beta/vector3.md)

- script_api.@minecraft/server-editor-bindings.selection.delta.moveby.description


////

//// define
返回值：[`Vector3`](../../server/beta/vector3.md)

- script_api.@minecraft/server-editor-bindings.selection.moveby.return


////

///


/// define
`moveTo`


///

script_api.@minecraft/server-editor-bindings.selection.moveto.description

```js
moveTo(location: Vector3): Vector3
```

/// html | div.result
//// define
`location`：[`Vector3`](../../server/beta/vector3.md)

- script_api.@minecraft/server-editor-bindings.selection.location.moveto.description


////

//// define
返回值：[`Vector3`](../../server/beta/vector3.md)

- script_api.@minecraft/server-editor-bindings.selection.moveto.return


////

///


/// define
`peekLastVolume`


///

script_api.@minecraft/server-editor-bindings.selection.peeklastvolume.description

```js
peekLastVolume(forceRelativity?: CompoundBlockVolumePositionRelativity): CompoundBlockVolumeItem | undefined
```

/// html | div.result
//// define
`forceRelativity`：[`CompoundBlockVolumePositionRelativity`](../../server/beta/compoundblockvolumepositionrelativity.md)|`undefined`

- script_api.@minecraft/server-editor-bindings.selection.forcerelativity.peeklastvolume.description


////

//// define
返回值：[`CompoundBlockVolumeItem`](../../server/beta/compoundblockvolumeitem.md)|`undefined`

- script_api.@minecraft/server-editor-bindings.selection.peeklastvolume.return


////

///


/// define
`popVolume`


///

script_api.@minecraft/server-editor-bindings.selection.popvolume.description

```js
popVolume(): void
```

/// html | div.result
//// define
返回值：`void`

- script_api.@minecraft/server-editor-bindings.selection.popvolume.return


////

///


/// define
`pushVolume`


///

script_api.@minecraft/server-editor-bindings.selection.pushvolume.description

```js
pushVolume(item: CompoundBlockVolumeItem): void
```

/// html | div.result
//// define
`item`：[`CompoundBlockVolumeItem`](../../server/beta/compoundblockvolumeitem.md)

- script_api.@minecraft/server-editor-bindings.selection.item.pushvolume.description


////

//// define
返回值：`void`

- script_api.@minecraft/server-editor-bindings.selection.pushvolume.return


////

///


/// define
`set`


///

script_api.@minecraft/server-editor-bindings.selection.set.description

```js
set(other: CompoundBlockVolume | Selection): void
```

/// html | div.result
//// define
`other`：[`CompoundBlockVolume`](../../server/beta/compoundblockvolume.md)|[`Selection`](./selection.md)

- script_api.@minecraft/server-editor-bindings.selection.other.set.description


////

//// define
返回值：`void`

- script_api.@minecraft/server-editor-bindings.selection.set.return


////

///


/// define
`setFillColor`


///

script_api.@minecraft/server-editor-bindings.selection.setfillcolor.description

```js
setFillColor(color: RGBA): void
```

/// html | div.result
//// define
`color`：[`RGBA`](../../server/beta/rgba.md)

- script_api.@minecraft/server-editor-bindings.selection.color.setfillcolor.description


////

//// define
返回值：`void`

- script_api.@minecraft/server-editor-bindings.selection.setfillcolor.return


////

///


/// define
`setOutlineColor`


///

script_api.@minecraft/server-editor-bindings.selection.setoutlinecolor.description

```js
setOutlineColor(color: RGBA): void
```

/// html | div.result
//// define
`color`：[`RGBA`](../../server/beta/rgba.md)

- script_api.@minecraft/server-editor-bindings.selection.color.setoutlinecolor.description


////

//// define
返回值：`void`

- script_api.@minecraft/server-editor-bindings.selection.setoutlinecolor.return


////

///

