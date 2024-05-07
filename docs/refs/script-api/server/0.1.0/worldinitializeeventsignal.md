# `WorldInitializeEventSignal`

> 文档版本：1.21.0.24

`WorldInitializeEventSignal`类。script_api.mojang-minecraft.worldinitializeeventsignal.description

## 方法

/// define
`subscribe`


///

script_api.mojang-minecraft.worldinitializeeventsignal.subscribe.description

```js
subscribe(callback: (arg: WorldInitializeEvent) => void): (arg: WorldInitializeEvent) => void
```

/// html | div.result
//// define
`callback`：<code>(<a href="../worldinitializeevent/">WorldInitializeEvent</a>) =&gt; void</code>

- script_api.mojang-minecraft.worldinitializeeventsignal.subscribe.callback.description


////

//// define
返回值：<code>(<a href="../worldinitializeevent/">WorldInitializeEvent</a>) =&gt; void</code>

- script_api.mojang-minecraft.worldinitializeeventsignal.subscribe.return


////

///


/// define
`unsubscribe`


///

script_api.mojang-minecraft.worldinitializeeventsignal.unsubscribe.description

```js
unsubscribe(callback: (arg: WorldInitializeEvent) => void): void
```

/// html | div.result
//// define
`callback`：<code>(<a href="../worldinitializeevent/">WorldInitializeEvent</a>) =&gt; void</code>

- script_api.mojang-minecraft.worldinitializeeventsignal.unsubscribe.callback.description


////

//// define
返回值：`void`

- script_api.mojang-minecraft.worldinitializeeventsignal.unsubscribe.return


////

///

