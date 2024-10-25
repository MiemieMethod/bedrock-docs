# `Cursor`

> 文档版本：1.21.50.25

`Cursor`类。script_api.@minecraft/server-editor-bindings.cursor.description

## 属性

/// define
`faceDirection`


///

```js
read-only faceDirection: uint8;
```

/// html | div.result
//// define
`faceDirection`：`uint8`

- script_api.@minecraft/server-editor-bindings.cursor.facedirection.description


////

///


/// define
`isVisible`


///

```js
read-only isVisible: boolean;
```

/// html | div.result
//// define
`isVisible`：`boolean`

- script_api.@minecraft/server-editor-bindings.cursor.isvisible.description


////

///


## 方法

/// define
`attachClipboardItem`


///

script_api.@minecraft/server-editor-bindings.cursor.attachclipboarditem.description

```js
attachClipboardItem(item: ClipboardItem): void
```

/// html | div.result
//// define
`item`：[`ClipboardItem`](./clipboarditem.md)

- script_api.@minecraft/server-editor-bindings.cursor.attachclipboarditem.item.description


////

//// define
返回值：`void`

- script_api.@minecraft/server-editor-bindings.cursor.attachclipboarditem.return


////

///


/// define
`clearAttachment`


///

script_api.@minecraft/server-editor-bindings.cursor.clearattachment.description

```js
clearAttachment(): void
```

/// html | div.result
//// define
返回值：`void`

- script_api.@minecraft/server-editor-bindings.cursor.clearattachment.return


////

///


/// define
`getAttachmentProperties`


///

script_api.@minecraft/server-editor-bindings.cursor.getattachmentproperties.description

```js
getAttachmentProperties(): CursorAttachmentProperties
```

/// html | div.result
//// define
返回值：[`CursorAttachmentProperties`](./cursorattachmentproperties.md)

- script_api.@minecraft/server-editor-bindings.cursor.getattachmentproperties.return


////

///


/// define
`getPosition`


///

script_api.@minecraft/server-editor-bindings.cursor.getposition.description

```js
getPosition(): Vector3
```

/// html | div.result
//// define
返回值：[`Vector3`](../../server/beta/vector3.md)

- script_api.@minecraft/server-editor-bindings.cursor.getposition.return


////

///


/// define
`getProperties`


///

script_api.@minecraft/server-editor-bindings.cursor.getproperties.description

```js
getProperties(): CursorProperties
```

/// html | div.result
//// define
返回值：[`CursorProperties`](./cursorproperties.md)

- script_api.@minecraft/server-editor-bindings.cursor.getproperties.return


////

///


/// define
`hide`


///

script_api.@minecraft/server-editor-bindings.cursor.hide.description

```js
hide(): void
```

/// html | div.result
//// define
返回值：`void`

- script_api.@minecraft/server-editor-bindings.cursor.hide.return


////

///


/// define
`moveBy`


///

script_api.@minecraft/server-editor-bindings.cursor.moveby.description

```js
moveBy(offset: Vector3): Vector3
```

/// html | div.result
//// define
`offset`：[`Vector3`](../../server/beta/vector3.md)

- script_api.@minecraft/server-editor-bindings.cursor.moveby.offset.description


////

//// define
返回值：[`Vector3`](../../server/beta/vector3.md)

- script_api.@minecraft/server-editor-bindings.cursor.moveby.return


////

///


/// define
`resetToDefaultState`


///

script_api.@minecraft/server-editor-bindings.cursor.resettodefaultstate.description

```js
resetToDefaultState(): void
```

/// html | div.result
//// define
返回值：`void`

- script_api.@minecraft/server-editor-bindings.cursor.resettodefaultstate.return


////

///


/// define
`setAttachmentProperties`


///

script_api.@minecraft/server-editor-bindings.cursor.setattachmentproperties.description

```js
setAttachmentProperties(properties: CursorAttachmentProperties): void
```

/// html | div.result
//// define
`properties`：[`CursorAttachmentProperties`](./cursorattachmentproperties.md)

- script_api.@minecraft/server-editor-bindings.cursor.setattachmentproperties.properties.description


////

//// define
返回值：`void`

- script_api.@minecraft/server-editor-bindings.cursor.setattachmentproperties.return


////

///


/// define
`setProperties`


///

script_api.@minecraft/server-editor-bindings.cursor.setproperties.description

```js
setProperties(properties: CursorProperties): void
```

/// html | div.result
//// define
`properties`：[`CursorProperties`](./cursorproperties.md)

- script_api.@minecraft/server-editor-bindings.cursor.setproperties.properties.description


////

//// define
返回值：`void`

- script_api.@minecraft/server-editor-bindings.cursor.setproperties.return


////

///


/// define
`show`


///

script_api.@minecraft/server-editor-bindings.cursor.show.description

```js
show(): void
```

/// html | div.result
//// define
返回值：`void`

- script_api.@minecraft/server-editor-bindings.cursor.show.return


////

///

