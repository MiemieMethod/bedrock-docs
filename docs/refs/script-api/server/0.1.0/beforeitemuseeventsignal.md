# `BeforeItemUseEventSignal`

> 文档版本：1.21.50.25

`BeforeItemUseEventSignal`类。script_api.mojang-minecraft.beforeitemuseeventsignal.description

## 方法

/// define
`subscribe`


///

script_api.mojang-minecraft.beforeitemuseeventsignal.subscribe.description

```js
subscribe(callback: (arg: BeforeItemUseEvent) => void): (arg: BeforeItemUseEvent) => void
```

/// html | div.result
//// define
`callback`：<code>(<a href="../beforeitemuseevent/">BeforeItemUseEvent</a>) =&gt; void</code>

- script_api.mojang-minecraft.beforeitemuseeventsignal.subscribe.callback.description


////

//// define
返回值：<code>(<a href="../beforeitemuseevent/">BeforeItemUseEvent</a>) =&gt; void</code>

- script_api.mojang-minecraft.beforeitemuseeventsignal.subscribe.return


////

///


/// define
`unsubscribe`


///

script_api.mojang-minecraft.beforeitemuseeventsignal.unsubscribe.description

```js
unsubscribe(callback: (arg: BeforeItemUseEvent) => void): void
```

/// html | div.result
//// define
`callback`：<code>(<a href="../beforeitemuseevent/">BeforeItemUseEvent</a>) =&gt; void</code>

- script_api.mojang-minecraft.beforeitemuseeventsignal.unsubscribe.callback.description


////

//// define
返回值：`void`

- script_api.mojang-minecraft.beforeitemuseeventsignal.unsubscribe.return


////

///

