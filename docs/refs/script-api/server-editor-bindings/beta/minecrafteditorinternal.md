# `MinecraftEditorInternal`

> 文档版本：1.21.0.20

`MinecraftEditorInternal`类。

## 方法

/// define
`getDataStore`


///

```js
getDataStore(player: Player): DataStore
```

/// html | div.result
//// define
`player`：[`Player`](../../server/beta/player.md)

- 参数1。


////

//// define
返回值：[`DataStore`](./datastore.md)

- 返回值。


////

///


/// define
`registerExtension`


///

```js
registerExtension(extensionName: string, activationFunction: (arg: ExtensionContext) => void, shutdownFunction: (arg: ExtensionContext) => void, options?: ExtensionOptionalParameters): Extension
```

/// html | div.result
//// define
`extensionName`：`string`

- 参数1。


////

//// define
`activationFunction`：<code>(<a href="../extensioncontext/">ExtensionContext</a>) =&gt; void</code>

- 参数2。


////

//// define
`shutdownFunction`：<code>(<a href="../extensioncontext/">ExtensionContext</a>) =&gt; void</code>

- 参数3。


////

//// define
`options`：[`ExtensionOptionalParameters`](./extensionoptionalparameters.md)|`undefined`

- 参数4。


////

//// define
返回值：[`Extension`](./extension.md)

- 返回值。


////

///

