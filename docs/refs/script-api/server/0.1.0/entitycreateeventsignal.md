# `EntityCreateEventSignal`

> 文档版本：1.21.50.25

`EntityCreateEventSignal`类。script_api.mojang-minecraft.entitycreateeventsignal.description

## 方法

/// define
`subscribe`


///

script_api.mojang-minecraft.entitycreateeventsignal.subscribe.description

```js
subscribe(callback: (arg: EntityCreateEvent) => void): (arg: EntityCreateEvent) => void
```

/// html | div.result
//// define
`callback`：<code>(<a href="../entitycreateevent/">EntityCreateEvent</a>) =&gt; void</code>

- script_api.mojang-minecraft.entitycreateeventsignal.subscribe.callback.description


////

//// define
返回值：<code>(<a href="../entitycreateevent/">EntityCreateEvent</a>) =&gt; void</code>

- script_api.mojang-minecraft.entitycreateeventsignal.subscribe.return


////

///


/// define
`unsubscribe`


///

script_api.mojang-minecraft.entitycreateeventsignal.unsubscribe.description

```js
unsubscribe(callback: (arg: EntityCreateEvent) => void): void
```

/// html | div.result
//// define
`callback`：<code>(<a href="../entitycreateevent/">EntityCreateEvent</a>) =&gt; void</code>

- script_api.mojang-minecraft.entitycreateeventsignal.unsubscribe.callback.description


////

//// define
返回值：`void`

- script_api.mojang-minecraft.entitycreateeventsignal.unsubscribe.return


////

///

