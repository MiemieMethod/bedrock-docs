# `EntityHitEventSignal`

> 文档版本：1.21.0.20

`EntityHitEventSignal`类。

## 方法

/// define
`subscribe`


///

```js
subscribe(callback: (arg: EntityHitEvent) => void, options?: EntityEventOptions): (arg: EntityHitEvent) => void
```

/// html | div.result
//// define
`callback`：<code>(<a href="../entityhitevent/">EntityHitEvent</a>) =&gt; void</code>

- 参数1。


////

//// define
`options`：[`EntityEventOptions`](./entityeventoptions.md)|`undefined`

- 参数2。


////

//// define
返回值：<code>(<a href="../entityhitevent/">EntityHitEvent</a>) =&gt; void</code>

- 返回值。


////

///


/// define
`unsubscribe`


///

```js
unsubscribe(callback: (arg: EntityHitEvent) => void): void
```

/// html | div.result
//// define
`callback`：<code>(<a href="../entityhitevent/">EntityHitEvent</a>) =&gt; void</code>

- 参数1。


////

//// define
返回值：`void`

- 返回值。


////

///

