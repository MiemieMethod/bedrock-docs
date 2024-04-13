# `System`

> 文档版本：1.21.0.21

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
`clearRun`


///

script_api.@minecraft/server.system.clearrun.description

```js
clearRun(runId: uint32): void
```

/// html | div.result
//// define
`runId`：`uint32`

- script_api.@minecraft/server.system.clearrun.runid.description


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

- script_api.@minecraft/server.system.run.callback.description


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

- script_api.@minecraft/server.system.runinterval.callback.description


////

//// define
`tickInterval`：`uint32`|`undefined`

- script_api.@minecraft/server.system.runinterval.tickinterval.description


////

//// define
返回值：`uint32`

- script_api.@minecraft/server.system.runinterval.return


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

- script_api.@minecraft/server.system.runtimeout.callback.description


////

//// define
`tickDelay`：`uint32`|`undefined`

- script_api.@minecraft/server.system.runtimeout.tickdelay.description


////

//// define
返回值：`uint32`

- script_api.@minecraft/server.system.runtimeout.return


////

///

