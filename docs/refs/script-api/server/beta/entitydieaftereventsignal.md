# `EntityDieAfterEventSignal`

> 文档版本：1.21.0.20

`EntityDieAfterEventSignal`类。

## 方法

/// define
`subscribe`


///

```js
subscribe(callback: (arg: EntityDieAfterEvent) => void, options?: EntityEventOptions): (arg: EntityDieAfterEvent) => void
```

/// html | div.result
//// define
`callback`：(arg: EntityDieAfterEvent) => void

- 参数1。


////

//// define
`options`：[`EntityEventOptions`](../entityeventoptions.md)|`undefined`

- 参数2。


////

//// define
返回值：(arg: EntityDieAfterEvent) => void

- 返回值。


////

///


/// define
`unsubscribe`


///

```js
unsubscribe(callback: (arg: EntityDieAfterEvent) => void): void
```

/// html | div.result
//// define
`callback`：(arg: EntityDieAfterEvent) => void

- 参数1。


////

//// define
返回值：`void`

- 返回值。


////

///

