# `ShutdownBeforeEventSignal`

> 文档版本：1.21.50.25

`ShutdownBeforeEventSignal`类。script_api.@minecraft/server.shutdownbeforeeventsignal.description

## 方法

/// define
`subscribe`


///

script_api.@minecraft/server.shutdownbeforeeventsignal.subscribe.description

```js
subscribe(callback: (arg: ShutdownEvent) => void): (arg: ShutdownEvent) => void
```

/// html | div.result
//// define
`callback`：<code>(<a href="../shutdownevent/">ShutdownEvent</a>) =&gt; void</code>

- script_api.@minecraft/server.shutdownbeforeeventsignal.subscribe.callback.description


////

//// define
返回值：<code>(<a href="../shutdownevent/">ShutdownEvent</a>) =&gt; void</code>

- script_api.@minecraft/server.shutdownbeforeeventsignal.subscribe.return


////

///


/// define
`unsubscribe`


///

script_api.@minecraft/server.shutdownbeforeeventsignal.unsubscribe.description

```js
unsubscribe(callback: (arg: ShutdownEvent) => void): void
```

/// html | div.result
//// define
`callback`：<code>(<a href="../shutdownevent/">ShutdownEvent</a>) =&gt; void</code>

- script_api.@minecraft/server.shutdownbeforeeventsignal.unsubscribe.callback.description


////

//// define
返回值：`void`

- script_api.@minecraft/server.shutdownbeforeeventsignal.unsubscribe.return


////

///

