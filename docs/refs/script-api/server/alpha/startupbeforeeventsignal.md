# `StartupBeforeEventSignal`

> 文档版本：1.21.50.25

`StartupBeforeEventSignal`类。script_api.@minecraft/server.startupbeforeeventsignal.description

## 方法

/// define
`subscribe`


///

script_api.@minecraft/server.startupbeforeeventsignal.subscribe.description

```js
subscribe(callback: (arg: StartupEvent) => void): (arg: StartupEvent) => void
```

/// html | div.result
//// define
`callback`：<code>(<a href="../startupevent/">StartupEvent</a>) =&gt; void</code>

- script_api.@minecraft/server.startupbeforeeventsignal.subscribe.callback.description


////

//// define
返回值：<code>(<a href="../startupevent/">StartupEvent</a>) =&gt; void</code>

- script_api.@minecraft/server.startupbeforeeventsignal.subscribe.return


////

///


/// define
`unsubscribe`


///

script_api.@minecraft/server.startupbeforeeventsignal.unsubscribe.description

```js
unsubscribe(callback: (arg: StartupEvent) => void): void
```

/// html | div.result
//// define
`callback`：<code>(<a href="../startupevent/">StartupEvent</a>) =&gt; void</code>

- script_api.@minecraft/server.startupbeforeeventsignal.unsubscribe.callback.description


////

//// define
返回值：`void`

- script_api.@minecraft/server.startupbeforeeventsignal.unsubscribe.return


////

///

