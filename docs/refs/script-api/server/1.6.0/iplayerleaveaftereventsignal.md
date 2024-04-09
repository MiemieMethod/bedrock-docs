# `IPlayerLeaveAfterEventSignal`

> 文档版本：1.21.0.20

`IPlayerLeaveAfterEventSignal`类。script_api.@minecraft/server.iplayerleaveaftereventsignal.description

## 方法

/// define
`subscribe`


///

script_api.@minecraft/server.iplayerleaveaftereventsignal.subscribe.description

```js
subscribe(callback: (arg: PlayerLeaveAfterEvent) => void): (arg: PlayerLeaveAfterEvent) => void
```

/// html | div.result
//// define
`callback`：<code>(<a href="../playerleaveafterevent/">PlayerLeaveAfterEvent</a>) =&gt; void</code>

- script_api.@minecraft/server.iplayerleaveaftereventsignal.callback.subscribe.description


////

//// define
返回值：<code>(<a href="../playerleaveafterevent/">PlayerLeaveAfterEvent</a>) =&gt; void</code>

- script_api.@minecraft/server.iplayerleaveaftereventsignal.subscribe.return


////

///


/// define
`unsubscribe`


///

script_api.@minecraft/server.iplayerleaveaftereventsignal.unsubscribe.description

```js
unsubscribe(callback: (arg: PlayerLeaveAfterEvent) => void): void
```

/// html | div.result
//// define
`callback`：<code>(<a href="../playerleaveafterevent/">PlayerLeaveAfterEvent</a>) =&gt; void</code>

- script_api.@minecraft/server.iplayerleaveaftereventsignal.callback.unsubscribe.description


////

//// define
返回值：`void`

- script_api.@minecraft/server.iplayerleaveaftereventsignal.unsubscribe.return


////

///

