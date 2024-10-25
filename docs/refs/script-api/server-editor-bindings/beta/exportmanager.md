# `ExportManager`

> 文档版本：1.21.50.25

`ExportManager`类。script_api.@minecraft/server-editor-bindings.exportmanager.description

## 方法

/// define
`beginExportProject`


///

script_api.@minecraft/server-editor-bindings.exportmanager.beginexportproject.description

```js
beginExportProject(options: GameOptions): Promise<ExportResult>
```

/// html | div.result
//// define
`options`：[`GameOptions`](./gameoptions.md)

- script_api.@minecraft/server-editor-bindings.exportmanager.beginexportproject.options.description


////

//// define
返回值：<code>Promise&lt;<a href="../exportresult/">ExportResult</a>&gt;</code>

- script_api.@minecraft/server-editor-bindings.exportmanager.beginexportproject.return


////

///


/// define
`canExportProject`


///

script_api.@minecraft/server-editor-bindings.exportmanager.canexportproject.description

```js
canExportProject(): boolean
```

/// html | div.result
//// define
返回值：`boolean`

- script_api.@minecraft/server-editor-bindings.exportmanager.canexportproject.return


////

///


/// define
`getGameOptions`


///

script_api.@minecraft/server-editor-bindings.exportmanager.getgameoptions.description

```js
getGameOptions(useDefault?: boolean): GameOptions
```

/// html | div.result
//// define
`useDefault`?：`boolean`＝`null`

- script_api.@minecraft/server-editor-bindings.exportmanager.getgameoptions.usedefault.description


////

//// define
返回值：[`GameOptions`](./gameoptions.md)

- script_api.@minecraft/server-editor-bindings.exportmanager.getgameoptions.return


////

///


/// define
`getGameVersion`


///

script_api.@minecraft/server-editor-bindings.exportmanager.getgameversion.description

```js
getGameVersion(): string
```

/// html | div.result
//// define
返回值：`string`

- script_api.@minecraft/server-editor-bindings.exportmanager.getgameversion.return


////

///

