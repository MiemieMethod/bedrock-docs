# `PlayerLeaveEventSignal`

> 文档版本：1.21.0.20

`PlayerLeaveEventSignal`类。script_api.mojang-minecraft.playerleaveeventsignal.description

## 方法

/// define
`subscribe`


///

script_api.mojang-minecraft.playerleaveeventsignal.subscribe.description

```js
subscribe(callback: (arg: PlayerLeaveEvent) => void): (arg: PlayerLeaveEvent) => void
```

/// html | div.result
//// define
`callback`：<code>(<a href="../playerleaveevent/">PlayerLeaveEvent</a>) =&gt; void</code>

- script_api.mojang-minecraft.playerleaveeventsignal.callback.subscribe.description


////

//// define
返回值：<code>(<a href="../playerleaveevent/">PlayerLeaveEvent</a>) =&gt; void</code>

- script_api.mojang-minecraft.playerleaveeventsignal.subscribe.return


////

///


/// define
`unsubscribe`


///

script_api.mojang-minecraft.playerleaveeventsignal.unsubscribe.description

```js
unsubscribe(callback: (arg: PlayerLeaveEvent) => void): void
```

/// html | div.result
//// define
`callback`：<code>(<a href="../playerleaveevent/">PlayerLeaveEvent</a>) =&gt; void</code>

- script_api.mojang-minecraft.playerleaveeventsignal.callback.unsubscribe.description


////

//// define
返回值：`void`

- script_api.mojang-minecraft.playerleaveeventsignal.unsubscribe.return


////

///

