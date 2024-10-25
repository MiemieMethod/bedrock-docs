# `PlayerBreakBlockAfterEventSignal`

> 文档版本：1.21.50.25

`PlayerBreakBlockAfterEventSignal`类。script_api.@minecraft/server.playerbreakblockaftereventsignal.description

## 方法

/// define
`subscribe`


///

script_api.@minecraft/server.playerbreakblockaftereventsignal.subscribe.description

```js
subscribe(callback: (arg: PlayerBreakBlockAfterEvent) => void, options?: BlockEventOptions): (arg: PlayerBreakBlockAfterEvent) => void
```

/// html | div.result
//// define
`callback`：<code>(<a href="../playerbreakblockafterevent/">PlayerBreakBlockAfterEvent</a>) =&gt; void</code>

- script_api.@minecraft/server.playerbreakblockaftereventsignal.subscribe.callback.description


////

//// define
`options`?：[`BlockEventOptions`](./blockeventoptions.md)＝`null`

- script_api.@minecraft/server.playerbreakblockaftereventsignal.subscribe.options.description


////

//// define
返回值：<code>(<a href="../playerbreakblockafterevent/">PlayerBreakBlockAfterEvent</a>) =&gt; void</code>

- script_api.@minecraft/server.playerbreakblockaftereventsignal.subscribe.return


////

///


/// define
`unsubscribe`


///

script_api.@minecraft/server.playerbreakblockaftereventsignal.unsubscribe.description

```js
unsubscribe(callback: (arg: PlayerBreakBlockAfterEvent) => void): void
```

/// html | div.result
//// define
`callback`：<code>(<a href="../playerbreakblockafterevent/">PlayerBreakBlockAfterEvent</a>) =&gt; void</code>

- script_api.@minecraft/server.playerbreakblockaftereventsignal.unsubscribe.callback.description


////

//// define
返回值：`void`

- script_api.@minecraft/server.playerbreakblockaftereventsignal.unsubscribe.return


////

///

