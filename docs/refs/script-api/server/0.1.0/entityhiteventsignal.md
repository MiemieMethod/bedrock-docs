# `EntityHitEventSignal`

> 文档版本：1.21.0.21

`EntityHitEventSignal`类。script_api.mojang-minecraft.entityhiteventsignal.description

## 方法

/// define
`subscribe`


///

script_api.mojang-minecraft.entityhiteventsignal.subscribe.description

```js
subscribe(callback: (arg: EntityHitEvent) => void, options?: EntityEventOptions): (arg: EntityHitEvent) => void
```

/// html | div.result
//// define
`callback`：<code>(<a href="../entityhitevent/">EntityHitEvent</a>) =&gt; void</code>

- script_api.mojang-minecraft.entityhiteventsignal.subscribe.callback.description


////

//// define
`options`：[`EntityEventOptions`](./entityeventoptions.md)|`undefined`

- script_api.mojang-minecraft.entityhiteventsignal.subscribe.options.description


////

//// define
返回值：<code>(<a href="../entityhitevent/">EntityHitEvent</a>) =&gt; void</code>

- script_api.mojang-minecraft.entityhiteventsignal.subscribe.return


////

///


/// define
`unsubscribe`


///

script_api.mojang-minecraft.entityhiteventsignal.unsubscribe.description

```js
unsubscribe(callback: (arg: EntityHitEvent) => void): void
```

/// html | div.result
//// define
`callback`：<code>(<a href="../entityhitevent/">EntityHitEvent</a>) =&gt; void</code>

- script_api.mojang-minecraft.entityhiteventsignal.unsubscribe.callback.description


////

//// define
返回值：`void`

- script_api.mojang-minecraft.entityhiteventsignal.unsubscribe.return


////

///

