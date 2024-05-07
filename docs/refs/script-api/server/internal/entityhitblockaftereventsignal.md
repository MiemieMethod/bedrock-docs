# `EntityHitBlockAfterEventSignal`

> 文档版本：1.21.0.24

`EntityHitBlockAfterEventSignal`类。script_api.@minecraft/server.entityhitblockaftereventsignal.description

## 方法

/// define
`subscribe`


///

script_api.@minecraft/server.entityhitblockaftereventsignal.subscribe.description

```js
subscribe(callback: (arg: EntityHitBlockAfterEvent) => void, options?: EntityEventOptions): (arg: EntityHitBlockAfterEvent) => void
```

/// html | div.result
//// define
`callback`：<code>(<a href="../entityhitblockafterevent/">EntityHitBlockAfterEvent</a>) =&gt; void</code>

- script_api.@minecraft/server.entityhitblockaftereventsignal.subscribe.callback.description


////

//// define
`options`?：[`EntityEventOptions`](./entityeventoptions.md)＝`null`

- script_api.@minecraft/server.entityhitblockaftereventsignal.subscribe.options.description


////

//// define
返回值：<code>(<a href="../entityhitblockafterevent/">EntityHitBlockAfterEvent</a>) =&gt; void</code>

- script_api.@minecraft/server.entityhitblockaftereventsignal.subscribe.return


////

///


/// define
`unsubscribe`


///

script_api.@minecraft/server.entityhitblockaftereventsignal.unsubscribe.description

```js
unsubscribe(callback: (arg: EntityHitBlockAfterEvent) => void): void
```

/// html | div.result
//// define
`callback`：<code>(<a href="../entityhitblockafterevent/">EntityHitBlockAfterEvent</a>) =&gt; void</code>

- script_api.@minecraft/server.entityhitblockaftereventsignal.unsubscribe.callback.description


////

//// define
返回值：`void`

- script_api.@minecraft/server.entityhitblockaftereventsignal.unsubscribe.return


////

///

