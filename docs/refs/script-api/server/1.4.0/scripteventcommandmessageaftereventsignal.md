# `ScriptEventCommandMessageAfterEventSignal`

> 文档版本：1.21.0.21

`ScriptEventCommandMessageAfterEventSignal`类。script_api.@minecraft/server.scripteventcommandmessageaftereventsignal.description

## 方法

/// define
`subscribe`


///

script_api.@minecraft/server.scripteventcommandmessageaftereventsignal.subscribe.description

```js
subscribe(callback: (arg: ScriptEventCommandMessageAfterEvent) => void, options?: ScriptEventMessageFilterOptions): (arg: ScriptEventCommandMessageAfterEvent) => void
```

/// html | div.result
//// define
`callback`：<code>(<a href="../scripteventcommandmessageafterevent/">ScriptEventCommandMessageAfterEvent</a>) =&gt; void</code>

- script_api.@minecraft/server.scripteventcommandmessageaftereventsignal.subscribe.callback.description


////

//// define
`options`：[`ScriptEventMessageFilterOptions`](./scripteventmessagefilteroptions.md)|`undefined`

- script_api.@minecraft/server.scripteventcommandmessageaftereventsignal.subscribe.options.description


////

//// define
返回值：<code>(<a href="../scripteventcommandmessageafterevent/">ScriptEventCommandMessageAfterEvent</a>) =&gt; void</code>

- script_api.@minecraft/server.scripteventcommandmessageaftereventsignal.subscribe.return


////

///


/// define
`unsubscribe`


///

script_api.@minecraft/server.scripteventcommandmessageaftereventsignal.unsubscribe.description

```js
unsubscribe(callback: (arg: ScriptEventCommandMessageAfterEvent) => void): void
```

/// html | div.result
//// define
`callback`：<code>(<a href="../scripteventcommandmessageafterevent/">ScriptEventCommandMessageAfterEvent</a>) =&gt; void</code>

- script_api.@minecraft/server.scripteventcommandmessageaftereventsignal.unsubscribe.callback.description


////

//// define
返回值：`void`

- script_api.@minecraft/server.scripteventcommandmessageaftereventsignal.unsubscribe.return


////

///

