# `DataDrivenEntityTriggerAfterEventSignal`

> 文档版本：1.21.0.20

`DataDrivenEntityTriggerAfterEventSignal`类。

## 方法

/// define
`subscribe`


///

```js
subscribe(callback: (arg: DataDrivenEntityTriggerAfterEvent) => void, options?: EntityDataDrivenTriggerEventOptions): (arg: DataDrivenEntityTriggerAfterEvent) => void
```

/// html | div.result
//// define
`callback`：(arg: DataDrivenEntityTriggerAfterEvent) => void

- 参数1。


////

//// define
`options`：[`EntityDataDrivenTriggerEventOptions`](../entitydatadriventriggereventoptions.md)|`undefined`

- 参数2。


////

//// define
返回值：(arg: DataDrivenEntityTriggerAfterEvent) => void

- 返回值。


////

///


/// define
`unsubscribe`


///

```js
unsubscribe(callback: (arg: DataDrivenEntityTriggerAfterEvent) => void): void
```

/// html | div.result
//// define
`callback`：(arg: DataDrivenEntityTriggerAfterEvent) => void

- 参数1。


////

//// define
返回值：`void`

- 返回值。


////

///

