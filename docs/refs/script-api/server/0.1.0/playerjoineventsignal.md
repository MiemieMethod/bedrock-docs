# `PlayerJoinEventSignal`

> 文档版本：1.21.0.21

`PlayerJoinEventSignal`类。script_api.mojang-minecraft.playerjoineventsignal.description

## 方法

/// define
`subscribe`


///

script_api.mojang-minecraft.playerjoineventsignal.subscribe.description

```js
subscribe(callback: (arg: PlayerJoinEvent) => void): (arg: PlayerJoinEvent) => void
```

/// html | div.result
//// define
`callback`：<code>(<a href="../playerjoinevent/">PlayerJoinEvent</a>) =&gt; void</code>

- script_api.mojang-minecraft.playerjoineventsignal.subscribe.callback.description


////

//// define
返回值：<code>(<a href="../playerjoinevent/">PlayerJoinEvent</a>) =&gt; void</code>

- script_api.mojang-minecraft.playerjoineventsignal.subscribe.return


////

///


/// define
`unsubscribe`


///

script_api.mojang-minecraft.playerjoineventsignal.unsubscribe.description

```js
unsubscribe(callback: (arg: PlayerJoinEvent) => void): void
```

/// html | div.result
//// define
`callback`：<code>(<a href="../playerjoinevent/">PlayerJoinEvent</a>) =&gt; void</code>

- script_api.mojang-minecraft.playerjoineventsignal.unsubscribe.callback.description


////

//// define
返回值：`void`

- script_api.mojang-minecraft.playerjoineventsignal.unsubscribe.return


////

///

