# `PlayerBreakBlockBeforeEventSignal`

> 文档版本：1.21.60.21

`PlayerBreakBlockBeforeEventSignal`类。script_api.@minecraft/server.playerbreakblockbeforeeventsignal.description

## 方法

/// define
`subscribe`


///

script_api.@minecraft/server.playerbreakblockbeforeeventsignal.subscribe.description

```js
subscribe(callback: (arg: PlayerBreakBlockBeforeEvent) => void, options?: BlockEventOptions): (arg: PlayerBreakBlockBeforeEvent) => void
```

/// html | div.result
//// define
`callback`：<code>(<a href="../playerbreakblockbeforeevent/">PlayerBreakBlockBeforeEvent</a>) =&gt; void</code>

- script_api.@minecraft/server.playerbreakblockbeforeeventsignal.subscribe.callback.description


////

//// define
`options`?：[`BlockEventOptions`](./blockeventoptions.md)＝`null`

- script_api.@minecraft/server.playerbreakblockbeforeeventsignal.subscribe.options.description


////

//// define
返回值：<code>(<a href="../playerbreakblockbeforeevent/">PlayerBreakBlockBeforeEvent</a>) =&gt; void</code>

- script_api.@minecraft/server.playerbreakblockbeforeeventsignal.subscribe.return


////

///


/// define
`unsubscribe`


///

script_api.@minecraft/server.playerbreakblockbeforeeventsignal.unsubscribe.description

```js
unsubscribe(callback: (arg: PlayerBreakBlockBeforeEvent) => void): void
```

/// html | div.result
//// define
`callback`：<code>(<a href="../playerbreakblockbeforeevent/">PlayerBreakBlockBeforeEvent</a>) =&gt; void</code>

- script_api.@minecraft/server.playerbreakblockbeforeeventsignal.unsubscribe.callback.description


////

//// define
返回值：`void`

- script_api.@minecraft/server.playerbreakblockbeforeeventsignal.unsubscribe.return


////

///

