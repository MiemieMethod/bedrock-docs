# `EntityHealthChangedAfterEventSignal`

> 文档版本：1.21.0.20

`EntityHealthChangedAfterEventSignal`类。script_api.@minecraft/server.entityhealthchangedaftereventsignal.description

## 方法

/// define
`subscribe`


///

script_api.@minecraft/server.entityhealthchangedaftereventsignal.subscribe.description

```js
subscribe(callback: (arg: EntityHealthChangedAfterEvent) => void, options?: EntityEventOptions): (arg: EntityHealthChangedAfterEvent) => void
```

/// html | div.result
//// define
`callback`：<code>(<a href="../entityhealthchangedafterevent/">EntityHealthChangedAfterEvent</a>) =&gt; void</code>

- script_api.@minecraft/server.entityhealthchangedaftereventsignal.callback.subscribe.description


////

//// define
`options`：[`EntityEventOptions`](./entityeventoptions.md)|`undefined`

- script_api.@minecraft/server.entityhealthchangedaftereventsignal.options.subscribe.description


////

//// define
返回值：<code>(<a href="../entityhealthchangedafterevent/">EntityHealthChangedAfterEvent</a>) =&gt; void</code>

- script_api.@minecraft/server.entityhealthchangedaftereventsignal.subscribe.return


////

///


/// define
`unsubscribe`


///

script_api.@minecraft/server.entityhealthchangedaftereventsignal.unsubscribe.description

```js
unsubscribe(callback: (arg: EntityHealthChangedAfterEvent) => void): void
```

/// html | div.result
//// define
`callback`：<code>(<a href="../entityhealthchangedafterevent/">EntityHealthChangedAfterEvent</a>) =&gt; void</code>

- script_api.@minecraft/server.entityhealthchangedaftereventsignal.callback.unsubscribe.description


////

//// define
返回值：`void`

- script_api.@minecraft/server.entityhealthchangedaftereventsignal.unsubscribe.return


////

///

