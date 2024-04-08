# `System`

> 文档版本：1.21.0.20

`System`类。

## 属性

/// define
`afterEvents`


///

```js
read-only afterEvents: SystemAfterEvents;
```


/// define
`beforeEvents`


///

```js
read-only beforeEvents: SystemBeforeEvents;
```


/// define
`currentTick`


///

```js
read-only currentTick: uint32;
```


## 方法

/// define
`clearJob`


///

```js
clearJob(jobId: uint32): void
```

/// html | div.result
//// define
`jobId`：`uint32`

- 参数1。


////

//// define
返回值：`void`

- 返回值。


////

///


/// define
`clearRun`


///

```js
clearRun(runId: uint32): void
```

/// html | div.result
//// define
`runId`：`uint32`

- 参数1。


////

//// define
返回值：`void`

- 返回值。


////

///


/// define
`run`


///

```js
run(callback: () => void): uint32
```

/// html | div.result
//// define
`callback`：<code>() =&gt; void</code>

- 参数1。


////

//// define
返回值：`uint32`

- 返回值。


////

///


/// define
`runInterval`


///

```js
runInterval(callback: () => void, tickInterval?: uint32): uint32
```

/// html | div.result
//// define
`callback`：<code>() =&gt; void</code>

- 参数1。


////

//// define
`tickInterval`：`uint32`|`undefined`

- 参数2。


////

//// define
返回值：`uint32`

- 返回值。


////

///


/// define
`runJob`


///

```js
runJob(generator: Generator<void, void, void>): uint32
```

/// html | div.result
//// define
`generator`：`Generator<void, void, void>`

- 参数1。


////

//// define
返回值：`uint32`

- 返回值。


////

///


/// define
`runTimeout`


///

```js
runTimeout(callback: () => void, tickDelay?: uint32): uint32
```

/// html | div.result
//// define
`callback`：<code>() =&gt; void</code>

- 参数1。


////

//// define
`tickDelay`：`uint32`|`undefined`

- 参数2。


////

//// define
返回值：`uint32`

- 返回值。


////

///

