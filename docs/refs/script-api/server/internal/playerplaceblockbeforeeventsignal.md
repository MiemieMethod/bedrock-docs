# `PlayerPlaceBlockBeforeEventSignal`

> 文档版本：1.21.50.25

`PlayerPlaceBlockBeforeEventSignal`类。script_api.@minecraft/server.playerplaceblockbeforeeventsignal.description

## 方法

/// define
`subscribe`


///

script_api.@minecraft/server.playerplaceblockbeforeeventsignal.subscribe.description

```js
subscribe(callback: (arg: PlayerPlaceBlockBeforeEvent) => void, options?: BlockEventOptions): (arg: PlayerPlaceBlockBeforeEvent) => void
```

/// html | div.result
//// define
`callback`：<code>(<a href="../playerplaceblockbeforeevent/">PlayerPlaceBlockBeforeEvent</a>) =&gt; void</code>

- script_api.@minecraft/server.playerplaceblockbeforeeventsignal.subscribe.callback.description


////

//// define
`options`?：[`BlockEventOptions`](./blockeventoptions.md)＝`null`

- script_api.@minecraft/server.playerplaceblockbeforeeventsignal.subscribe.options.description


////

//// define
返回值：<code>(<a href="../playerplaceblockbeforeevent/">PlayerPlaceBlockBeforeEvent</a>) =&gt; void</code>

- script_api.@minecraft/server.playerplaceblockbeforeeventsignal.subscribe.return


////

///


/// define
`unsubscribe`


///

script_api.@minecraft/server.playerplaceblockbeforeeventsignal.unsubscribe.description

```js
unsubscribe(callback: (arg: PlayerPlaceBlockBeforeEvent) => void): void
```

/// html | div.result
//// define
`callback`：<code>(<a href="../playerplaceblockbeforeevent/">PlayerPlaceBlockBeforeEvent</a>) =&gt; void</code>

- script_api.@minecraft/server.playerplaceblockbeforeeventsignal.unsubscribe.callback.description


////

//// define
返回值：`void`

- script_api.@minecraft/server.playerplaceblockbeforeeventsignal.unsubscribe.return


////

///

