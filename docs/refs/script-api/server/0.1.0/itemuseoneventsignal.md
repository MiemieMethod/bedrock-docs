# `ItemUseOnEventSignal`

> 文档版本：1.21.0.24

`ItemUseOnEventSignal`类。script_api.mojang-minecraft.itemuseoneventsignal.description

## 方法

/// define
`subscribe`


///

script_api.mojang-minecraft.itemuseoneventsignal.subscribe.description

```js
subscribe(callback: (arg: ItemUseOnEvent) => void): (arg: ItemUseOnEvent) => void
```

/// html | div.result
//// define
`callback`：<code>(<a href="../itemuseonevent/">ItemUseOnEvent</a>) =&gt; void</code>

- script_api.mojang-minecraft.itemuseoneventsignal.subscribe.callback.description


////

//// define
返回值：<code>(<a href="../itemuseonevent/">ItemUseOnEvent</a>) =&gt; void</code>

- script_api.mojang-minecraft.itemuseoneventsignal.subscribe.return


////

///


/// define
`unsubscribe`


///

script_api.mojang-minecraft.itemuseoneventsignal.unsubscribe.description

```js
unsubscribe(callback: (arg: ItemUseOnEvent) => void): void
```

/// html | div.result
//// define
`callback`：<code>(<a href="../itemuseonevent/">ItemUseOnEvent</a>) =&gt; void</code>

- script_api.mojang-minecraft.itemuseoneventsignal.unsubscribe.callback.description


////

//// define
返回值：`void`

- script_api.mojang-minecraft.itemuseoneventsignal.unsubscribe.return


////

///

