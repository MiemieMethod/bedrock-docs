# `BeforeItemUseOnEventSignal`

> 文档版本：1.21.0.24

`BeforeItemUseOnEventSignal`类。script_api.mojang-minecraft.beforeitemuseoneventsignal.description

## 方法

/// define
`subscribe`


///

script_api.mojang-minecraft.beforeitemuseoneventsignal.subscribe.description

```js
subscribe(callback: (arg: BeforeItemUseOnEvent) => void): (arg: BeforeItemUseOnEvent) => void
```

/// html | div.result
//// define
`callback`：<code>(<a href="../beforeitemuseonevent/">BeforeItemUseOnEvent</a>) =&gt; void</code>

- script_api.mojang-minecraft.beforeitemuseoneventsignal.subscribe.callback.description


////

//// define
返回值：<code>(<a href="../beforeitemuseonevent/">BeforeItemUseOnEvent</a>) =&gt; void</code>

- script_api.mojang-minecraft.beforeitemuseoneventsignal.subscribe.return


////

///


/// define
`unsubscribe`


///

script_api.mojang-minecraft.beforeitemuseoneventsignal.unsubscribe.description

```js
unsubscribe(callback: (arg: BeforeItemUseOnEvent) => void): void
```

/// html | div.result
//// define
`callback`：<code>(<a href="../beforeitemuseonevent/">BeforeItemUseOnEvent</a>) =&gt; void</code>

- script_api.mojang-minecraft.beforeitemuseoneventsignal.unsubscribe.callback.description


////

//// define
返回值：`void`

- script_api.mojang-minecraft.beforeitemuseoneventsignal.unsubscribe.return


////

///

