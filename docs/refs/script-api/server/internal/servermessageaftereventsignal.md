# `ServerMessageAfterEventSignal`

> 文档版本：1.21.0.24

`ServerMessageAfterEventSignal`类。script_api.@minecraft/server.servermessageaftereventsignal.description

## 方法

/// define
`subscribe`


///

script_api.@minecraft/server.servermessageaftereventsignal.subscribe.description

```js
subscribe(callback: (arg: MessageReceiveAfterEvent) => void): (arg: MessageReceiveAfterEvent) => void
```

/// html | div.result
//// define
`callback`：<code>(<a href="../messagereceiveafterevent/">MessageReceiveAfterEvent</a>) =&gt; void</code>

- script_api.@minecraft/server.servermessageaftereventsignal.subscribe.callback.description


////

//// define
返回值：<code>(<a href="../messagereceiveafterevent/">MessageReceiveAfterEvent</a>) =&gt; void</code>

- script_api.@minecraft/server.servermessageaftereventsignal.subscribe.return


////

///


/// define
`unsubscribe`


///

script_api.@minecraft/server.servermessageaftereventsignal.unsubscribe.description

```js
unsubscribe(callback: (arg: MessageReceiveAfterEvent) => void): void
```

/// html | div.result
//// define
`callback`：<code>(<a href="../messagereceiveafterevent/">MessageReceiveAfterEvent</a>) =&gt; void</code>

- script_api.@minecraft/server.servermessageaftereventsignal.unsubscribe.callback.description


////

//// define
返回值：`void`

- script_api.@minecraft/server.servermessageaftereventsignal.unsubscribe.return


////

///

