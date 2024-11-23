# `EditorStructureManager`

> 文档版本：1.21.60.21

`EditorStructureManager`类。script_api.@minecraft/server-editor-bindings.editorstructuremanager.description

## 方法

/// define
`createFromClipboardItem`


///

script_api.@minecraft/server-editor-bindings.editorstructuremanager.createfromclipboarditem.description

```js
createFromClipboardItem(item: ClipboardItem, structureName: string): EditorStructure
```

/// html | div.result
//// define
`item`：[`ClipboardItem`](./clipboarditem.md)

- script_api.@minecraft/server-editor-bindings.editorstructuremanager.createfromclipboarditem.item.description


////

//// define
`structureName`：`string`

- script_api.@minecraft/server-editor-bindings.editorstructuremanager.createfromclipboarditem.structurename.description


////

//// define
返回值：[`EditorStructure`](./editorstructure.md)

- script_api.@minecraft/server-editor-bindings.editorstructuremanager.createfromclipboarditem.return


////

///


/// define
`getExistingTags`


///

script_api.@minecraft/server-editor-bindings.editorstructuremanager.getexistingtags.description

```js
getExistingTags(): string[]
```

/// html | div.result
//// define
返回值：`string[]`

- script_api.@minecraft/server-editor-bindings.editorstructuremanager.getexistingtags.return


////

///


/// define
`loadStructure`


///

script_api.@minecraft/server-editor-bindings.editorstructuremanager.loadstructure.description

```js
loadStructure(location: string, id: string): EditorStructure
```

/// html | div.result
//// define
`location`：`string`

- script_api.@minecraft/server-editor-bindings.editorstructuremanager.loadstructure.location.description


////

//// define
`id`：`string`

- script_api.@minecraft/server-editor-bindings.editorstructuremanager.loadstructure.id.description


////

//// define
返回值：[`EditorStructure`](./editorstructure.md)

- script_api.@minecraft/server-editor-bindings.editorstructuremanager.loadstructure.return


////

///


/// define
`saveStructure`


///

script_api.@minecraft/server-editor-bindings.editorstructuremanager.savestructure.description

```js
saveStructure(structure: EditorStructure): void
```

/// html | div.result
//// define
`structure`：[`EditorStructure`](./editorstructure.md)

- script_api.@minecraft/server-editor-bindings.editorstructuremanager.savestructure.structure.description


////

//// define
返回值：`void`

- script_api.@minecraft/server-editor-bindings.editorstructuremanager.savestructure.return


////

///


/// define
`searchStructures`


///

script_api.@minecraft/server-editor-bindings.editorstructuremanager.searchstructures.description

```js
searchStructures(options?: EditorStructureSearchOptions): EditorStructure[]
```

/// html | div.result
//// define
`options`?：[`EditorStructureSearchOptions`](./editorstructuresearchoptions.md)＝`null`

- script_api.@minecraft/server-editor-bindings.editorstructuremanager.searchstructures.options.description


////

//// define
返回值：<code><a href="../editorstructure/">EditorStructure</a>[]</code>

- script_api.@minecraft/server-editor-bindings.editorstructuremanager.searchstructures.return


////

///

