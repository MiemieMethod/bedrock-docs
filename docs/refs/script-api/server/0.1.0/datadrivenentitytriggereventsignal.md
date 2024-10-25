# `DataDrivenEntityTriggerEventSignal`

> 文档版本：1.21.50.25

`DataDrivenEntityTriggerEventSignal`类。script_api.mojang-minecraft.datadrivenentitytriggereventsignal.description

## 方法

/// define
`subscribe`


///

script_api.mojang-minecraft.datadrivenentitytriggereventsignal.subscribe.description

```js
subscribe(callback: (arg: DataDrivenEntityTriggerEvent) => void, options?: EntityDataDrivenTriggerEventOptions): (arg: DataDrivenEntityTriggerEvent) => void
```

/// html | div.result
//// define
`callback`：<code>(<a href="../datadrivenentitytriggerevent/">DataDrivenEntityTriggerEvent</a>) =&gt; void</code>

- script_api.mojang-minecraft.datadrivenentitytriggereventsignal.subscribe.callback.description


////

//// define
`options`?：[`EntityDataDrivenTriggerEventOptions`](./entitydatadriventriggereventoptions.md)＝`null`

- script_api.mojang-minecraft.datadrivenentitytriggereventsignal.subscribe.options.description


////

//// define
返回值：<code>(<a href="../datadrivenentitytriggerevent/">DataDrivenEntityTriggerEvent</a>) =&gt; void</code>

- script_api.mojang-minecraft.datadrivenentitytriggereventsignal.subscribe.return


////

///


/// define
`unsubscribe`


///

script_api.mojang-minecraft.datadrivenentitytriggereventsignal.unsubscribe.description

```js
unsubscribe(callback: (arg: DataDrivenEntityTriggerEvent) => void): void
```

/// html | div.result
//// define
`callback`：<code>(<a href="../datadrivenentitytriggerevent/">DataDrivenEntityTriggerEvent</a>) =&gt; void</code>

- script_api.mojang-minecraft.datadrivenentitytriggereventsignal.unsubscribe.callback.description


////

//// define
返回值：`void`

- script_api.mojang-minecraft.datadrivenentitytriggereventsignal.unsubscribe.return


////

///

