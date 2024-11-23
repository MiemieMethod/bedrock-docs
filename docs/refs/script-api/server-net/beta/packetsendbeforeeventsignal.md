# `PacketSendBeforeEventSignal`

> 文档版本：1.21.60.21

`PacketSendBeforeEventSignal`类。script_api.@minecraft/server-net.packetsendbeforeeventsignal.description

## 方法

/// define
`subscribe`


///

script_api.@minecraft/server-net.packetsendbeforeeventsignal.subscribe.description

```js
subscribe(callback: (arg: PacketSendBeforeEvent) => void, options?: PacketEventOptions): (arg: PacketSendBeforeEvent) => void
```

/// html | div.result
//// define
`callback`：<code>(<a href="../packetsendbeforeevent/">PacketSendBeforeEvent</a>) =&gt; void</code>

- script_api.@minecraft/server-net.packetsendbeforeeventsignal.subscribe.callback.description


////

//// define
`options`?：[`PacketEventOptions`](./packeteventoptions.md)＝`null`

- script_api.@minecraft/server-net.packetsendbeforeeventsignal.subscribe.options.description


////

//// define
返回值：<code>(<a href="../packetsendbeforeevent/">PacketSendBeforeEvent</a>) =&gt; void</code>

- script_api.@minecraft/server-net.packetsendbeforeeventsignal.subscribe.return


////

///


/// define
`unsubscribe`


///

script_api.@minecraft/server-net.packetsendbeforeeventsignal.unsubscribe.description

```js
unsubscribe(callback: (arg: PacketSendBeforeEvent) => void): void
```

/// html | div.result
//// define
`callback`：<code>(<a href="../packetsendbeforeevent/">PacketSendBeforeEvent</a>) =&gt; void</code>

- script_api.@minecraft/server-net.packetsendbeforeeventsignal.unsubscribe.callback.description


////

//// define
返回值：`void`

- script_api.@minecraft/server-net.packetsendbeforeeventsignal.unsubscribe.return


////

///

