# `DataDrivenEntityTriggerAfterEventSignal`

> 文档版本：1.21.60.21

`DataDrivenEntityTriggerAfterEventSignal`类。script_api.@minecraft/server.datadrivenentitytriggeraftereventsignal.description

## 方法

/// define
`subscribe`


///

script_api.@minecraft/server.datadrivenentitytriggeraftereventsignal.subscribe.description

```js
subscribe(callback: (arg: DataDrivenEntityTriggerAfterEvent) => void, options?: EntityDataDrivenTriggerEventOptions): (arg: DataDrivenEntityTriggerAfterEvent) => void
```

/// html | div.result
//// define
`callback`：<code>(<a href="../datadrivenentitytriggerafterevent/">DataDrivenEntityTriggerAfterEvent</a>) =&gt; void</code>

- script_api.@minecraft/server.datadrivenentitytriggeraftereventsignal.subscribe.callback.description


////

//// define
`options`?：[`EntityDataDrivenTriggerEventOptions`](./entitydatadriventriggereventoptions.md)＝`null`

- script_api.@minecraft/server.datadrivenentitytriggeraftereventsignal.subscribe.options.description


////

//// define
返回值：<code>(<a href="../datadrivenentitytriggerafterevent/">DataDrivenEntityTriggerAfterEvent</a>) =&gt; void</code>

- script_api.@minecraft/server.datadrivenentitytriggeraftereventsignal.subscribe.return


////

///


/// define
`unsubscribe`


///

script_api.@minecraft/server.datadrivenentitytriggeraftereventsignal.unsubscribe.description

```js
unsubscribe(callback: (arg: DataDrivenEntityTriggerAfterEvent) => void): void
```

/// html | div.result
//// define
`callback`：<code>(<a href="../datadrivenentitytriggerafterevent/">DataDrivenEntityTriggerAfterEvent</a>) =&gt; void</code>

- script_api.@minecraft/server.datadrivenentitytriggeraftereventsignal.unsubscribe.callback.description


////

//// define
返回值：`void`

- script_api.@minecraft/server.datadrivenentitytriggeraftereventsignal.unsubscribe.return


////

///

