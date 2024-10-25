# `BeforeChatEventSignal`

> 文档版本：1.21.50.25

`BeforeChatEventSignal`类。script_api.mojang-minecraft.beforechateventsignal.description

## 方法

/// define
`subscribe`


///

script_api.mojang-minecraft.beforechateventsignal.subscribe.description

```js
subscribe(callback: (arg: BeforeChatEvent) => void): (arg: BeforeChatEvent) => void
```

/// html | div.result
//// define
`callback`：<code>(<a href="../beforechatevent/">BeforeChatEvent</a>) =&gt; void</code>

- script_api.mojang-minecraft.beforechateventsignal.subscribe.callback.description


////

//// define
返回值：<code>(<a href="../beforechatevent/">BeforeChatEvent</a>) =&gt; void</code>

- script_api.mojang-minecraft.beforechateventsignal.subscribe.return


////

///


/// define
`unsubscribe`


///

script_api.mojang-minecraft.beforechateventsignal.unsubscribe.description

```js
unsubscribe(callback: (arg: BeforeChatEvent) => void): void
```

/// html | div.result
//// define
`callback`：<code>(<a href="../beforechatevent/">BeforeChatEvent</a>) =&gt; void</code>

- script_api.mojang-minecraft.beforechateventsignal.unsubscribe.callback.description


////

//// define
返回值：`void`

- script_api.mojang-minecraft.beforechateventsignal.unsubscribe.return


////

///

