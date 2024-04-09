# `EntityHurtEventSignal`

> 文档版本：1.21.0.20

`EntityHurtEventSignal`类。script_api.mojang-minecraft.entityhurteventsignal.description

## 方法

/// define
`subscribe`


///

script_api.mojang-minecraft.entityhurteventsignal.subscribe.description

```js
subscribe(callback: (arg: EntityHurtEvent) => void, options?: EntityEventOptions): (arg: EntityHurtEvent) => void
```

/// html | div.result
//// define
`callback`：<code>(<a href="../entityhurtevent/">EntityHurtEvent</a>) =&gt; void</code>

- script_api.mojang-minecraft.entityhurteventsignal.callback.subscribe.description


////

//// define
`options`：[`EntityEventOptions`](./entityeventoptions.md)|`undefined`

- script_api.mojang-minecraft.entityhurteventsignal.options.subscribe.description


////

//// define
返回值：<code>(<a href="../entityhurtevent/">EntityHurtEvent</a>) =&gt; void</code>

- script_api.mojang-minecraft.entityhurteventsignal.subscribe.return


////

///


/// define
`unsubscribe`


///

script_api.mojang-minecraft.entityhurteventsignal.unsubscribe.description

```js
unsubscribe(callback: (arg: EntityHurtEvent) => void): void
```

/// html | div.result
//// define
`callback`：<code>(<a href="../entityhurtevent/">EntityHurtEvent</a>) =&gt; void</code>

- script_api.mojang-minecraft.entityhurteventsignal.callback.unsubscribe.description


////

//// define
返回值：`void`

- script_api.mojang-minecraft.entityhurteventsignal.unsubscribe.return


////

///

