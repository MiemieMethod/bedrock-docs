# `MinecraftEditorInternal`

> 文档版本：1.21.50.25

`MinecraftEditorInternal`类。script_api.@minecraft/server-editor-bindings.minecrafteditorinternal.description

## 方法

/// define
`getMapColorUnsafe`


///

script_api.@minecraft/server-editor-bindings.minecrafteditorinternal.getmapcolorunsafe.description

```js
getMapColorUnsafe(player: Player, coordinate: Vector3): RGBA
```

/// html | div.result
//// define
`player`：[`Player`](../../server/beta/player.md)

- script_api.@minecraft/server-editor-bindings.minecrafteditorinternal.getmapcolorunsafe.player.description


////

//// define
`coordinate`：[`Vector3`](../../server/beta/vector3.md)

- script_api.@minecraft/server-editor-bindings.minecrafteditorinternal.getmapcolorunsafe.coordinate.description


////

//// define
返回值：[`RGBA`](../../server/beta/rgba.md)

- script_api.@minecraft/server-editor-bindings.minecrafteditorinternal.getmapcolorunsafe.return


////

///


/// define
`getPlayerServices`


///

script_api.@minecraft/server-editor-bindings.minecrafteditorinternal.getplayerservices.description

```js
getPlayerServices(player: Player): InternalPlayerServiceContext
```

/// html | div.result
//// define
`player`：[`Player`](../../server/beta/player.md)

- script_api.@minecraft/server-editor-bindings.minecrafteditorinternal.getplayerservices.player.description


////

//// define
返回值：[`InternalPlayerServiceContext`](./internalplayerservicecontext.md)

- script_api.@minecraft/server-editor-bindings.minecrafteditorinternal.getplayerservices.return


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

- script_api.@minecraft/server-editor-bindings.minecrafteditorinternal.registerextension.extensionname.description


////

//// define
`activationFunction`：<code>(<a href="../extensioncontext/">ExtensionContext</a>) =&gt; void</code>

- script_api.@minecraft/server-editor-bindings.minecrafteditorinternal.registerextension.activationfunction.description


////

//// define
`shutdownFunction`：<code>(<a href="../extensioncontext/">ExtensionContext</a>) =&gt; void</code>

- script_api.@minecraft/server-editor-bindings.minecrafteditorinternal.registerextension.shutdownfunction.description


////

//// define
`options`?：[`ExtensionOptionalParameters`](./extensionoptionalparameters.md)＝`null`

- script_api.@minecraft/server-editor-bindings.minecrafteditorinternal.registerextension.options.description


////

//// define
返回值：[`Extension`](./extension.md)

- script_api.@minecraft/server-editor-bindings.minecrafteditorinternal.registerextension.return


////

///

