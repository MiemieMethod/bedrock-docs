# `System`

> 文档版本：1.21.0.20

`System`类。

## 属性

/// define
afterEvents

- ```js
read-only afterEvents: SystemAfterEvents
```



///


/// define
beforeEvents

- ```js
read-only beforeEvents: SystemBeforeEvents
```



///


/// define
currentTick

- ```js
read-only currentTick: uint32
```



///


## 方法

/// define
clearJob

- ```js
clearJob(jobId: uint32): void
```



///


/// define
clearRun

- ```js
clearRun(runId: uint32): void
```



///


/// define
run

- ```js
run(callback: () => void): uint32
```



///


/// define
runInterval

- ```js
runInterval(callback: () => void, tickInterval?: uint32): uint32
```



///


/// define
runJob

- ```js
runJob(generator: Generator<void, void, void>): uint32
```



///


/// define
runTimeout

- ```js
runTimeout(callback: () => void, tickDelay?: uint32): uint32
```



///

