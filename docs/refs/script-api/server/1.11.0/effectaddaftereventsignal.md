# `EffectAddAfterEventSignal`

> 文档版本：1.21.0.21

`EffectAddAfterEventSignal`类。script_api.@minecraft/server.effectaddaftereventsignal.description

## 方法

/// define
`subscribe`


///

script_api.@minecraft/server.effectaddaftereventsignal.subscribe.description

```js
subscribe(callback: (arg: EffectAddAfterEvent) => void, options?: EntityEventOptions): (arg: EffectAddAfterEvent) => void
```

/// html | div.result
//// define
`callback`：<code>(<a href="../effectaddafterevent/">EffectAddAfterEvent</a>) =&gt; void</code>

- script_api.@minecraft/server.effectaddaftereventsignal.subscribe.callback.description


////

//// define
`options`：[`EntityEventOptions`](./entityeventoptions.md)|`undefined`

- script_api.@minecraft/server.effectaddaftereventsignal.subscribe.options.description


////

//// define
返回值：<code>(<a href="../effectaddafterevent/">EffectAddAfterEvent</a>) =&gt; void</code>

- script_api.@minecraft/server.effectaddaftereventsignal.subscribe.return


////

///


/// define
`unsubscribe`


///

script_api.@minecraft/server.effectaddaftereventsignal.unsubscribe.description

```js
unsubscribe(callback: (arg: EffectAddAfterEvent) => void): void
```

/// html | div.result
//// define
`callback`：<code>(<a href="../effectaddafterevent/">EffectAddAfterEvent</a>) =&gt; void</code>

- script_api.@minecraft/server.effectaddaftereventsignal.unsubscribe.callback.description


////

//// define
返回值：`void`

- script_api.@minecraft/server.effectaddaftereventsignal.unsubscribe.return


////

///

