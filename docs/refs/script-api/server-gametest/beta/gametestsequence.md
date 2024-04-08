# `GameTestSequence`

> 文档版本：1.21.0.20

`GameTestSequence`类。

## 方法

/// define
`thenExecute`


///

```js
thenExecute(callback: () => void): GameTestSequence
```

/// html | div.result
//// define
`callback`：<code>() =&gt; void</code>

- 参数1。


////

//// define
返回值：[`GameTestSequence`](./gametestsequence.md)

- 返回值。


////

///


/// define
`thenExecuteAfter`


///

```js
thenExecuteAfter(delayTicks: int32, callback: () => void): GameTestSequence
```

/// html | div.result
//// define
`delayTicks`：`int32`

- 参数1。


////

//// define
`callback`：<code>() =&gt; void</code>

- 参数2。


////

//// define
返回值：[`GameTestSequence`](./gametestsequence.md)

- 返回值。


////

///


/// define
`thenExecuteFor`


///

```js
thenExecuteFor(tickCount: int32, callback: () => void): GameTestSequence
```

/// html | div.result
//// define
`tickCount`：`int32`

- 参数1。


////

//// define
`callback`：<code>() =&gt; void</code>

- 参数2。


////

//// define
返回值：[`GameTestSequence`](./gametestsequence.md)

- 返回值。


////

///


/// define
`thenFail`


///

```js
thenFail(errorMessage: string): void
```

/// html | div.result
//// define
`errorMessage`：`string`

- 参数1。


////

//// define
返回值：`void`

- 返回值。


////

///


/// define
`thenIdle`


///

```js
thenIdle(delayTicks: int32): GameTestSequence
```

/// html | div.result
//// define
`delayTicks`：`int32`

- 参数1。


////

//// define
返回值：[`GameTestSequence`](./gametestsequence.md)

- 返回值。


////

///


/// define
`thenSucceed`


///

```js
thenSucceed(): void
```

/// html | div.result
//// define
返回值：`void`

- 返回值。


////

///


/// define
`thenWait`


///

```js
thenWait(callback: () => void): GameTestSequence
```

/// html | div.result
//// define
`callback`：<code>() =&gt; void</code>

- 参数1。


////

//// define
返回值：[`GameTestSequence`](./gametestsequence.md)

- 返回值。


////

///


/// define
`thenWaitAfter`


///

```js
thenWaitAfter(delayTicks: int32, callback: () => void): GameTestSequence
```

/// html | div.result
//// define
`delayTicks`：`int32`

- 参数1。


////

//// define
`callback`：<code>() =&gt; void</code>

- 参数2。


////

//// define
返回值：[`GameTestSequence`](./gametestsequence.md)

- 返回值。


////

///

