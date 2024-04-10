# `EntityHurtAfterEventSignal`

> 文档版本：1.21.0.20

`EntityHurtAfterEventSignal`类。script_api.@minecraft/server.entityhurtaftereventsignal.description

## 方法

/// define
`subscribe`


///

script_api.@minecraft/server.entityhurtaftereventsignal.subscribe.description

```js
subscribe(callback: (arg: EntityHurtAfterEvent) => void, options?: EntityEventOptions): (arg: EntityHurtAfterEvent) => void
```

/// html | div.result
//// define
`callback`：<code>(<a href="../entityhurtafterevent/">EntityHurtAfterEvent</a>) =&gt; void</code>

- script_api.@minecraft/server.entityhurtaftereventsignal.subscribe.callback.description


////

//// define
`options`：[`EntityEventOptions`](./entityeventoptions.md)|`undefined`

- script_api.@minecraft/server.entityhurtaftereventsignal.subscribe.options.description


////

//// define
返回值：<code>(<a href="../entityhurtafterevent/">EntityHurtAfterEvent</a>) =&gt; void</code>

- script_api.@minecraft/server.entityhurtaftereventsignal.subscribe.return


////

///


/// define
`unsubscribe`


///

script_api.@minecraft/server.entityhurtaftereventsignal.unsubscribe.description

```js
unsubscribe(callback: (arg: EntityHurtAfterEvent) => void): void
```

/// html | div.result
//// define
`callback`：<code>(<a href="../entityhurtafterevent/">EntityHurtAfterEvent</a>) =&gt; void</code>

- script_api.@minecraft/server.entityhurtaftereventsignal.unsubscribe.callback.description


////

//// define
返回值：`void`

- script_api.@minecraft/server.entityhurtaftereventsignal.unsubscribe.return


////

///

