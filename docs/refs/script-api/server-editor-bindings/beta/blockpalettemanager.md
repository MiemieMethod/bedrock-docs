# `BlockPaletteManager`

> 文档版本：1.21.50.25

`BlockPaletteManager`类。script_api.@minecraft/server-editor-bindings.blockpalettemanager.description

## 方法

/// define
`addOrReplacePalette`


///

script_api.@minecraft/server-editor-bindings.blockpalettemanager.addorreplacepalette.description

```js
addOrReplacePalette(paletteId: string, palette: BlockPalette): void
```

/// html | div.result
//// define
`paletteId`：`string`

- script_api.@minecraft/server-editor-bindings.blockpalettemanager.addorreplacepalette.paletteid.description


////

//// define
`palette`：[`BlockPalette`](./blockpalette.md)

- script_api.@minecraft/server-editor-bindings.blockpalettemanager.addorreplacepalette.palette.description


////

//// define
返回值：`void`

- script_api.@minecraft/server-editor-bindings.blockpalettemanager.addorreplacepalette.return


////

///


/// define
`getPalette`


///

script_api.@minecraft/server-editor-bindings.blockpalettemanager.getpalette.description

```js
getPalette(paletteId: string): BlockPalette | undefined
```

/// html | div.result
//// define
`paletteId`：`string`

- script_api.@minecraft/server-editor-bindings.blockpalettemanager.getpalette.paletteid.description


////

//// define
返回值：[`BlockPalette`](./blockpalette.md)|`undefined`

- script_api.@minecraft/server-editor-bindings.blockpalettemanager.getpalette.return


////

///


/// define
`getPaletteIdList`


///

script_api.@minecraft/server-editor-bindings.blockpalettemanager.getpaletteidlist.description

```js
getPaletteIdList(): string[]
```

/// html | div.result
//// define
返回值：`string[]`

- script_api.@minecraft/server-editor-bindings.blockpalettemanager.getpaletteidlist.return


////

///


/// define
`getPaletteItem`


///

script_api.@minecraft/server-editor-bindings.blockpalettemanager.getpaletteitem.description

```js
getPaletteItem(paletteId: string, index: int32): IBlockPaletteItem
```

/// html | div.result
//// define
`paletteId`：`string`

- script_api.@minecraft/server-editor-bindings.blockpalettemanager.getpaletteitem.paletteid.description


////

//// define
`index`：`int32`

- script_api.@minecraft/server-editor-bindings.blockpalettemanager.getpaletteitem.index.description


////

//// define
返回值：[`IBlockPaletteItem`](./iblockpaletteitem.md)

- script_api.@minecraft/server-editor-bindings.blockpalettemanager.getpaletteitem.return


////

///


/// define
`getPrimaryPalette`


///

script_api.@minecraft/server-editor-bindings.blockpalettemanager.getprimarypalette.description

```js
getPrimaryPalette(): BlockPalette
```

/// html | div.result
//// define
返回值：[`BlockPalette`](./blockpalette.md)

- script_api.@minecraft/server-editor-bindings.blockpalettemanager.getprimarypalette.return


////

///


/// define
`getSelectedBlockType`


///

script_api.@minecraft/server-editor-bindings.blockpalettemanager.getselectedblocktype.description

```js
getSelectedBlockType(): BlockType
```

/// html | div.result
//// define
返回值：[`BlockType`](../../server/beta/blocktype.md)

- script_api.@minecraft/server-editor-bindings.blockpalettemanager.getselectedblocktype.return


////

///


/// define
`getSelectedItem`


///

script_api.@minecraft/server-editor-bindings.blockpalettemanager.getselecteditem.description

```js
getSelectedItem(): IBlockPaletteItem
```

/// html | div.result
//// define
返回值：[`IBlockPaletteItem`](./iblockpaletteitem.md)

- script_api.@minecraft/server-editor-bindings.blockpalettemanager.getselecteditem.return


////

///


/// define
`removePalette`


///

script_api.@minecraft/server-editor-bindings.blockpalettemanager.removepalette.description

```js
removePalette(paletteId: string): void
```

/// html | div.result
//// define
`paletteId`：`string`

- script_api.@minecraft/server-editor-bindings.blockpalettemanager.removepalette.paletteid.description


////

//// define
返回值：`void`

- script_api.@minecraft/server-editor-bindings.blockpalettemanager.removepalette.return


////

///


/// define
`setPaletteItem`


///

script_api.@minecraft/server-editor-bindings.blockpalettemanager.setpaletteitem.description

```js
setPaletteItem(paletteId: string, index: int32, item: IBlockPaletteItem): void
```

/// html | div.result
//// define
`paletteId`：`string`

- script_api.@minecraft/server-editor-bindings.blockpalettemanager.setpaletteitem.paletteid.description


////

//// define
`index`：`int32`

- script_api.@minecraft/server-editor-bindings.blockpalettemanager.setpaletteitem.index.description


////

//// define
`item`：[`IBlockPaletteItem`](./iblockpaletteitem.md)

- script_api.@minecraft/server-editor-bindings.blockpalettemanager.setpaletteitem.item.description


////

//// define
返回值：`void`

- script_api.@minecraft/server-editor-bindings.blockpalettemanager.setpaletteitem.return


////

///


/// define
`setPrimaryPalette`


///

script_api.@minecraft/server-editor-bindings.blockpalettemanager.setprimarypalette.description

```js
setPrimaryPalette(paletteId: string): void
```

/// html | div.result
//// define
`paletteId`：`string`

- script_api.@minecraft/server-editor-bindings.blockpalettemanager.setprimarypalette.paletteid.description


////

//// define
返回值：`void`

- script_api.@minecraft/server-editor-bindings.blockpalettemanager.setprimarypalette.return


////

///


/// define
`setSelectedItem`


///

script_api.@minecraft/server-editor-bindings.blockpalettemanager.setselecteditem.description

```js
setSelectedItem(item: IBlockPaletteItem): void
```

/// html | div.result
//// define
`item`：[`IBlockPaletteItem`](./iblockpaletteitem.md)

- script_api.@minecraft/server-editor-bindings.blockpalettemanager.setselecteditem.item.description


////

//// define
返回值：`void`

- script_api.@minecraft/server-editor-bindings.blockpalettemanager.setselecteditem.return


////

///

