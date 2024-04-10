# `EntityRemoveAfterEventSignal`

> 文档版本：1.21.0.20

`EntityRemoveAfterEventSignal`类。script_api.@minecraft/server.entityremoveaftereventsignal.description

## 方法

/// define
`subscribe`


///

script_api.@minecraft/server.entityremoveaftereventsignal.subscribe.description

```js
subscribe(callback: (arg: EntityRemoveAfterEvent) => void, options?: EntityEventOptions): (arg: EntityRemoveAfterEvent) => void
```

/// html | div.result
//// define
`callback`：<code>(<a href="../entityremoveafterevent/">EntityRemoveAfterEvent</a>) =&gt; void</code>

- script_api.@minecraft/server.entityremoveaftereventsignal.subscribe.callback.description


////

//// define
`options`：[`EntityEventOptions`](./entityeventoptions.md)|`undefined`

- script_api.@minecraft/server.entityremoveaftereventsignal.subscribe.options.description


////

//// define
返回值：<code>(<a href="../entityremoveafterevent/">EntityRemoveAfterEvent</a>) =&gt; void</code>

- script_api.@minecraft/server.entityremoveaftereventsignal.subscribe.return


////

///


/// define
`unsubscribe`


///

script_api.@minecraft/server.entityremoveaftereventsignal.unsubscribe.description

```js
unsubscribe(callback: (arg: EntityRemoveAfterEvent) => void): void
```

/// html | div.result
//// define
`callback`：<code>(<a href="../entityremoveafterevent/">EntityRemoveAfterEvent</a>) =&gt; void</code>

- script_api.@minecraft/server.entityremoveaftereventsignal.unsubscribe.callback.description


////

//// define
返回值：`void`

- script_api.@minecraft/server.entityremoveaftereventsignal.unsubscribe.return


////

///

