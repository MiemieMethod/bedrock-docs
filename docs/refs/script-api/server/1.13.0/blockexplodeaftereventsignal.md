# `BlockExplodeAfterEventSignal`

> 文档版本：1.21.50.25

`BlockExplodeAfterEventSignal`类。用于管理与方块爆炸后事件有关的回调函数。

## 方法

/// define
`subscribe`


///

订阅方块爆炸后事件并执行给定的回调函数。

```js
subscribe(callback: (arg: BlockExplodeAfterEvent) => void): (arg: BlockExplodeAfterEvent) => void
```

/// html | div.result
//// define
`callback`：<code>(<a href="../blockexplodeafterevent/">BlockExplodeAfterEvent</a>) =&gt; void</code>

- 要执行的回调函数。


////

//// define
返回值：<code>(<a href="../blockexplodeafterevent/">BlockExplodeAfterEvent</a>) =&gt; void</code>

- 订阅此事件的回调函数。


////

///


/// define
`unsubscribe`


///

移除给定回调函数对方块爆炸后事件的订阅。

```js
unsubscribe(callback: (arg: BlockExplodeAfterEvent) => void): void
```

/// html | div.result
//// define
`callback`：<code>(<a href="../blockexplodeafterevent/">BlockExplodeAfterEvent</a>) =&gt; void</code>

- 要移除的回调函数。


////

//// define
返回值：`void`

- script_api.@minecraft/server.blockexplodeaftereventsignal.unsubscribe.return


////

///

