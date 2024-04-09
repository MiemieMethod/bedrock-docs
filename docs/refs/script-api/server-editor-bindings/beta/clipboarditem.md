# `ClipboardItem`

> 文档版本：1.21.0.20

`ClipboardItem`类。script_api.@minecraft/server-editor-bindings.clipboarditem.description

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

- script_api.@minecraft/server-editor-bindings.clipboarditem.isempty.description


////

///


## 方法

/// define
`clear`


///

script_api.@minecraft/server-editor-bindings.clipboarditem.clear.description

```js
clear(): void
```

/// html | div.result
//// define
返回值：`void`

- script_api.@minecraft/server-editor-bindings.clipboarditem.clear.return


////

///


/// define
`getPredictedWriteAsCompoundBlockVolume`


///

script_api.@minecraft/server-editor-bindings.clipboarditem.getpredictedwriteascompoundblockvolume.description

```js
getPredictedWriteAsCompoundBlockVolume(location: Vector3, options?: ClipboardWriteOptions): CompoundBlockVolume
```

/// html | div.result
//// define
`location`：[`Vector3`](../../server/beta/vector3.md)

- script_api.@minecraft/server-editor-bindings.clipboarditem.location.getpredictedwriteascompoundblockvolume.description


////

//// define
`options`：[`ClipboardWriteOptions`](./clipboardwriteoptions.md)|`undefined`

- script_api.@minecraft/server-editor-bindings.clipboarditem.options.getpredictedwriteascompoundblockvolume.description


////

//// define
返回值：[`CompoundBlockVolume`](../../server/beta/compoundblockvolume.md)

- script_api.@minecraft/server-editor-bindings.clipboarditem.getpredictedwriteascompoundblockvolume.return


////

///


/// define
`getPredictedWriteAsSelection`


///

script_api.@minecraft/server-editor-bindings.clipboarditem.getpredictedwriteasselection.description

```js
getPredictedWriteAsSelection(location: Vector3, options?: ClipboardWriteOptions): Selection
```

/// html | div.result
//// define
`location`：[`Vector3`](../../server/beta/vector3.md)

- script_api.@minecraft/server-editor-bindings.clipboarditem.location.getpredictedwriteasselection.description


////

//// define
`options`：[`ClipboardWriteOptions`](./clipboardwriteoptions.md)|`undefined`

- script_api.@minecraft/server-editor-bindings.clipboarditem.options.getpredictedwriteasselection.description


////

//// define
返回值：[`Selection`](./selection.md)

- script_api.@minecraft/server-editor-bindings.clipboarditem.getpredictedwriteasselection.return


////

///


/// define
`getSize`


///

script_api.@minecraft/server-editor-bindings.clipboarditem.getsize.description

```js
getSize(): Vector3
```

/// html | div.result
//// define
返回值：[`Vector3`](../../server/beta/vector3.md)

- script_api.@minecraft/server-editor-bindings.clipboarditem.getsize.return


////

///


/// define
`readFromSelection`


///

script_api.@minecraft/server-editor-bindings.clipboarditem.readfromselection.description

```js
readFromSelection(selection: Selection): void
```

/// html | div.result
//// define
`selection`：[`Selection`](./selection.md)

- script_api.@minecraft/server-editor-bindings.clipboarditem.selection.readfromselection.description


////

//// define
返回值：`void`

- script_api.@minecraft/server-editor-bindings.clipboarditem.readfromselection.return


////

///


/// define
`readFromWorld`


///

script_api.@minecraft/server-editor-bindings.clipboarditem.readfromworld.description

```js
readFromWorld(from: Vector3, to: Vector3): void
```

/// html | div.result
//// define
`from`：[`Vector3`](../../server/beta/vector3.md)

- script_api.@minecraft/server-editor-bindings.clipboarditem.from.readfromworld.description


////

//// define
`to`：[`Vector3`](../../server/beta/vector3.md)

- script_api.@minecraft/server-editor-bindings.clipboarditem.to.readfromworld.description


////

//// define
返回值：`void`

- script_api.@minecraft/server-editor-bindings.clipboarditem.readfromworld.return


////

///


/// define
`writeToWorld`


///

script_api.@minecraft/server-editor-bindings.clipboarditem.writetoworld.description

```js
writeToWorld(location: Vector3, options?: ClipboardWriteOptions): boolean
```

/// html | div.result
//// define
`location`：[`Vector3`](../../server/beta/vector3.md)

- script_api.@minecraft/server-editor-bindings.clipboarditem.location.writetoworld.description


////

//// define
`options`：[`ClipboardWriteOptions`](./clipboardwriteoptions.md)|`undefined`

- script_api.@minecraft/server-editor-bindings.clipboarditem.options.writetoworld.description


////

//// define
返回值：`boolean`

- script_api.@minecraft/server-editor-bindings.clipboarditem.writetoworld.return


////

///

