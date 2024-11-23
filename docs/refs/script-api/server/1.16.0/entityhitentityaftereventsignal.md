# `EntityHitEntityAfterEventSignal`

> 文档版本：1.21.60.21

`EntityHitEntityAfterEventSignal`类。script_api.@minecraft/server.entityhitentityaftereventsignal.description

## 方法

/// define
`subscribe`


///

script_api.@minecraft/server.entityhitentityaftereventsignal.subscribe.description

```js
subscribe(callback: (arg: EntityHitEntityAfterEvent) => void, options?: EntityEventOptions): (arg: EntityHitEntityAfterEvent) => void
```

/// html | div.result
//// define
`callback`：<code>(<a href="../entityhitentityafterevent/">EntityHitEntityAfterEvent</a>) =&gt; void</code>

- script_api.@minecraft/server.entityhitentityaftereventsignal.subscribe.callback.description


////

//// define
`options`?：[`EntityEventOptions`](./entityeventoptions.md)＝`null`

- script_api.@minecraft/server.entityhitentityaftereventsignal.subscribe.options.description


////

//// define
返回值：<code>(<a href="../entityhitentityafterevent/">EntityHitEntityAfterEvent</a>) =&gt; void</code>

- script_api.@minecraft/server.entityhitentityaftereventsignal.subscribe.return


////

///


/// define
`unsubscribe`


///

script_api.@minecraft/server.entityhitentityaftereventsignal.unsubscribe.description

```js
unsubscribe(callback: (arg: EntityHitEntityAfterEvent) => void): void
```

/// html | div.result
//// define
`callback`：<code>(<a href="../entityhitentityafterevent/">EntityHitEntityAfterEvent</a>) =&gt; void</code>

- script_api.@minecraft/server.entityhitentityaftereventsignal.unsubscribe.callback.description


////

//// define
返回值：`void`

- script_api.@minecraft/server.entityhitentityaftereventsignal.unsubscribe.return


////

///

