# `EntityDieAfterEventSignal`

> 文档版本：1.21.0.20

`EntityDieAfterEventSignal`类。script_api.@minecraft/server.entitydieaftereventsignal.description

## 方法

/// define
`subscribe`


///

script_api.@minecraft/server.entitydieaftereventsignal.subscribe.description

```js
subscribe(callback: (arg: EntityDieAfterEvent) => void, options?: EntityEventOptions): (arg: EntityDieAfterEvent) => void
```

/// html | div.result
//// define
`callback`：<code>(<a href="../entitydieafterevent/">EntityDieAfterEvent</a>) =&gt; void</code>

- script_api.@minecraft/server.entitydieaftereventsignal.callback.subscribe.description


////

//// define
`options`：[`EntityEventOptions`](./entityeventoptions.md)|`undefined`

- script_api.@minecraft/server.entitydieaftereventsignal.options.subscribe.description


////

//// define
返回值：<code>(<a href="../entitydieafterevent/">EntityDieAfterEvent</a>) =&gt; void</code>

- script_api.@minecraft/server.entitydieaftereventsignal.subscribe.return


////

///


/// define
`unsubscribe`


///

script_api.@minecraft/server.entitydieaftereventsignal.unsubscribe.description

```js
unsubscribe(callback: (arg: EntityDieAfterEvent) => void): void
```

/// html | div.result
//// define
`callback`：<code>(<a href="../entitydieafterevent/">EntityDieAfterEvent</a>) =&gt; void</code>

- script_api.@minecraft/server.entitydieaftereventsignal.callback.unsubscribe.description


////

//// define
返回值：`void`

- script_api.@minecraft/server.entitydieaftereventsignal.unsubscribe.return


////

///

