# `System`

> 文档版本：1.21.0.20

`System`类。script_api.@minecraft/server.system.description

## 属性

/// define
`afterEvents`


///

```js
read-only afterEvents: SystemAfterEvents;
```

/// html | div.result
//// define
`afterEvents`：[`SystemAfterEvents`](./systemafterevents.md)

- script_api.@minecraft/server.system.afterevents.description


////

///


/// define
`beforeEvents`


///

```js
read-only beforeEvents: SystemBeforeEvents;
```

/// html | div.result
//// define
`beforeEvents`：[`SystemBeforeEvents`](./systembeforeevents.md)

- script_api.@minecraft/server.system.beforeevents.description


////

///


/// define
`currentTick`


///

```js
read-only currentTick: uint32;
```

/// html | div.result
//// define
`currentTick`：`uint32`

- script_api.@minecraft/server.system.currenttick.description


////

///


## 方法

/// define
`clearJob`


///

script_api.@minecraft/server.system.clearjob.description

```js
clearJob(jobId: uint32): void
```

/// html | div.result
//// define
`jobId`：`uint32`

- script_api.@minecraft/server.system.jobid.clearjob.description


////

//// define
返回值：`void`

- script_api.@minecraft/server.system.clearjob.return


////

///


/// define
`clearRun`


///

script_api.@minecraft/server.system.clearrun.description

```js
clearRun(runId: uint32): void
```

/// html | div.result
//// define
`runId`：`uint32`

- script_api.@minecraft/server.system.runid.clearrun.description


////

//// define
返回值：`void`

- script_api.@minecraft/server.system.clearrun.return


////

///


/// define
`run`


///

script_api.@minecraft/server.system.run.description

```js
run(callback: () => void): uint32
```

/// html | div.result
//// define
`callback`：<code>() =&gt; void</code>

- script_api.@minecraft/server.system.callback.run.description


////

//// define
返回值：`uint32`

- script_api.@minecraft/server.system.run.return


////

///


/// define
`runInterval`


///

script_api.@minecraft/server.system.runinterval.description

```js
runInterval(callback: () => void, tickInterval?: uint32): uint32
```

/// html | div.result
//// define
`callback`：<code>() =&gt; void</code>

- script_api.@minecraft/server.system.callback.runinterval.description


////

//// define
`tickInterval`：`uint32`|`undefined`

- script_api.@minecraft/server.system.tickinterval.runinterval.description


////

//// define
返回值：`uint32`

- script_api.@minecraft/server.system.runinterval.return


////

///


/// define
`runJob`


///

script_api.@minecraft/server.system.runjob.description

```js
runJob(generator: Generator<void, void, void>): uint32
```

/// html | div.result
//// define
`generator`：`Generator<void, void, void>`

- script_api.@minecraft/server.system.generator.runjob.description


////

//// define
返回值：`uint32`

- script_api.@minecraft/server.system.runjob.return


////

///


/// define
`runTimeout`


///

script_api.@minecraft/server.system.runtimeout.description

```js
runTimeout(callback: () => void, tickDelay?: uint32): uint32
```

/// html | div.result
//// define
`callback`：<code>() =&gt; void</code>

- script_api.@minecraft/server.system.callback.runtimeout.description


////

//// define
`tickDelay`：`uint32`|`undefined`

- script_api.@minecraft/server.system.tickdelay.runtimeout.description


////

//// define
返回值：`uint32`

- script_api.@minecraft/server.system.runtimeout.return


////

///

