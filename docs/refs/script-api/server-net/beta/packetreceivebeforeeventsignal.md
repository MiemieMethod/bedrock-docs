# `PacketReceiveBeforeEventSignal`

> 文档版本：1.21.60.21

`PacketReceiveBeforeEventSignal`类。script_api.@minecraft/server-net.packetreceivebeforeeventsignal.description

## 方法

/// define
`subscribe`


///

script_api.@minecraft/server-net.packetreceivebeforeeventsignal.subscribe.description

```js
subscribe(callback: (arg: PacketReceivedBeforeEvent) => void, options?: PacketEventOptions): (arg: PacketReceivedBeforeEvent) => void
```

/// html | div.result
//// define
`callback`：<code>(<a href="../packetreceivedbeforeevent/">PacketReceivedBeforeEvent</a>) =&gt; void</code>

- script_api.@minecraft/server-net.packetreceivebeforeeventsignal.subscribe.callback.description


////

//// define
`options`?：[`PacketEventOptions`](./packeteventoptions.md)＝`null`

- script_api.@minecraft/server-net.packetreceivebeforeeventsignal.subscribe.options.description


////

//// define
返回值：<code>(<a href="../packetreceivedbeforeevent/">PacketReceivedBeforeEvent</a>) =&gt; void</code>

- script_api.@minecraft/server-net.packetreceivebeforeeventsignal.subscribe.return


////

///


/// define
`unsubscribe`


///

script_api.@minecraft/server-net.packetreceivebeforeeventsignal.unsubscribe.description

```js
unsubscribe(callback: (arg: PacketReceivedBeforeEvent) => void): void
```

/// html | div.result
//// define
`callback`：<code>(<a href="../packetreceivedbeforeevent/">PacketReceivedBeforeEvent</a>) =&gt; void</code>

- script_api.@minecraft/server-net.packetreceivebeforeeventsignal.unsubscribe.callback.description


////

//// define
返回值：`void`

- script_api.@minecraft/server-net.packetreceivebeforeeventsignal.unsubscribe.return


////

///

