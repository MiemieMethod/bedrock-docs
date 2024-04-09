# `MinecraftEditorInternal`

> 文档版本：1.21.0.20

`MinecraftEditorInternal`类。script_api.@minecraft/server-editor-bindings.minecrafteditorinternal.description

## 方法

/// define
`getDataStore`


///

script_api.@minecraft/server-editor-bindings.minecrafteditorinternal.getdatastore.description

```js
getDataStore(player: Player): DataStore
```

/// html | div.result
//// define
`player`：[`Player`](../../server/beta/player.md)

- script_api.@minecraft/server-editor-bindings.minecrafteditorinternal.player.getdatastore.description


////

//// define
返回值：[`DataStore`](./datastore.md)

- script_api.@minecraft/server-editor-bindings.minecrafteditorinternal.getdatastore.return


////

///


/// define
`registerExtension`


///

script_api.@minecraft/server-editor-bindings.minecrafteditorinternal.registerextension.description

```js
registerExtension(extensionName: string, activationFunction: (arg: ExtensionContext) => void, shutdownFunction: (arg: ExtensionContext) => void, options?: ExtensionOptionalParameters): Extension
```

/// html | div.result
//// define
`extensionName`：`string`

- script_api.@minecraft/server-editor-bindings.minecrafteditorinternal.extensionname.registerextension.description


////

//// define
`activationFunction`：<code>(<a href="../extensioncontext/">ExtensionContext</a>) =&gt; void</code>

- script_api.@minecraft/server-editor-bindings.minecrafteditorinternal.activationfunction.registerextension.description


////

//// define
`shutdownFunction`：<code>(<a href="../extensioncontext/">ExtensionContext</a>) =&gt; void</code>

- script_api.@minecraft/server-editor-bindings.minecrafteditorinternal.shutdownfunction.registerextension.description


////

//// define
`options`：[`ExtensionOptionalParameters`](./extensionoptionalparameters.md)|`undefined`

- script_api.@minecraft/server-editor-bindings.minecrafteditorinternal.options.registerextension.description


////

//// define
返回值：[`Extension`](./extension.md)

- script_api.@minecraft/server-editor-bindings.minecrafteditorinternal.registerextension.return


////

///

