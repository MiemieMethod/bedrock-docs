# `TickEventSignal`

> 文档版本：1.21.60.21

`TickEventSignal`类。script_api.mojang-minecraft.tickeventsignal.description

## 方法

/// define
`subscribe`


///

script_api.mojang-minecraft.tickeventsignal.subscribe.description

```js
subscribe(callback: (arg: TickEvent) => void): (arg: TickEvent) => void
```

/// html | div.result
//// define
`callback`：<code>(<a href="../tickevent/">TickEvent</a>) =&gt; void</code>

- script_api.mojang-minecraft.tickeventsignal.subscribe.callback.description


////

//// define
返回值：<code>(<a href="../tickevent/">TickEvent</a>) =&gt; void</code>

- script_api.mojang-minecraft.tickeventsignal.subscribe.return


////

///


/// define
`unsubscribe`


///

script_api.mojang-minecraft.tickeventsignal.unsubscribe.description

```js
unsubscribe(callback: (arg: TickEvent) => void): void
```

/// html | div.result
//// define
`callback`：<code>(<a href="../tickevent/">TickEvent</a>) =&gt; void</code>

- script_api.mojang-minecraft.tickeventsignal.unsubscribe.callback.description


////

//// define
返回值：`void`

- script_api.mojang-minecraft.tickeventsignal.unsubscribe.return


////

///

