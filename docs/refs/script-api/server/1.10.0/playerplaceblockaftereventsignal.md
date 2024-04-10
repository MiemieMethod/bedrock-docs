# `PlayerPlaceBlockAfterEventSignal`

> 文档版本：1.21.0.20

`PlayerPlaceBlockAfterEventSignal`类。script_api.@minecraft/server.playerplaceblockaftereventsignal.description

## 方法

/// define
`subscribe`


///

script_api.@minecraft/server.playerplaceblockaftereventsignal.subscribe.description

```js
subscribe(callback: (arg: PlayerPlaceBlockAfterEvent) => void, options?: BlockEventOptions): (arg: PlayerPlaceBlockAfterEvent) => void
```

/// html | div.result
//// define
`callback`：<code>(<a href="../playerplaceblockafterevent/">PlayerPlaceBlockAfterEvent</a>) =&gt; void</code>

- script_api.@minecraft/server.playerplaceblockaftereventsignal.subscribe.callback.description


////

//// define
`options`：[`BlockEventOptions`](./blockeventoptions.md)|`undefined`

- script_api.@minecraft/server.playerplaceblockaftereventsignal.subscribe.options.description


////

//// define
返回值：<code>(<a href="../playerplaceblockafterevent/">PlayerPlaceBlockAfterEvent</a>) =&gt; void</code>

- script_api.@minecraft/server.playerplaceblockaftereventsignal.subscribe.return


////

///


/// define
`unsubscribe`


///

script_api.@minecraft/server.playerplaceblockaftereventsignal.unsubscribe.description

```js
unsubscribe(callback: (arg: PlayerPlaceBlockAfterEvent) => void): void
```

/// html | div.result
//// define
`callback`：<code>(<a href="../playerplaceblockafterevent/">PlayerPlaceBlockAfterEvent</a>) =&gt; void</code>

- script_api.@minecraft/server.playerplaceblockaftereventsignal.unsubscribe.callback.description


////

//// define
返回值：`void`

- script_api.@minecraft/server.playerplaceblockaftereventsignal.unsubscribe.return


////

///

