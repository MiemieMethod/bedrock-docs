# `IPlayerJoinAfterEventSignal`

> 文档版本：1.21.0.21

`IPlayerJoinAfterEventSignal`类。script_api.@minecraft/server.iplayerjoinaftereventsignal.description

## 方法

/// define
`subscribe`


///

script_api.@minecraft/server.iplayerjoinaftereventsignal.subscribe.description

```js
subscribe(callback: (arg: PlayerJoinAfterEvent) => void): (arg: PlayerJoinAfterEvent) => void
```

/// html | div.result
//// define
`callback`：<code>(<a href="../playerjoinafterevent/">PlayerJoinAfterEvent</a>) =&gt; void</code>

- script_api.@minecraft/server.iplayerjoinaftereventsignal.subscribe.callback.description


////

//// define
返回值：<code>(<a href="../playerjoinafterevent/">PlayerJoinAfterEvent</a>) =&gt; void</code>

- script_api.@minecraft/server.iplayerjoinaftereventsignal.subscribe.return


////

///


/// define
`unsubscribe`


///

script_api.@minecraft/server.iplayerjoinaftereventsignal.unsubscribe.description

```js
unsubscribe(callback: (arg: PlayerJoinAfterEvent) => void): void
```

/// html | div.result
//// define
`callback`：<code>(<a href="../playerjoinafterevent/">PlayerJoinAfterEvent</a>) =&gt; void</code>

- script_api.@minecraft/server.iplayerjoinaftereventsignal.unsubscribe.callback.description


////

//// define
返回值：`void`

- script_api.@minecraft/server.iplayerjoinaftereventsignal.unsubscribe.return


////

///

