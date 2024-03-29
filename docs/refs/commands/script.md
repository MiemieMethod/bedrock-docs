# `/script`

> 文档版本：1.20.80.24

`/script`命令Debugging options for GameTest Framework.

/// note | 执行条件
该命令需要权限等级：`admin,host`|`2`。该命令需要开启作弊。
///

## 用法

/// tab | 重载1
```mcfunction
/script profiler start
```

//// html | div.result
///// define
`mode`: <!-- md:samp ScriptDebugModeProfiler -->

- 枚举类型。枚举值如下：

|值|描述|
|---|---|
|`profiler`||


`action`: <!-- md:samp ScriptProfilerStart -->

- 枚举类型。枚举值如下：

|值|描述|
|---|---|
|`start`||



/////

////

///

/// tab | 重载2
```mcfunction
/script profiler stop
```

//// html | div.result
///// define
`mode`: <!-- md:samp ScriptDebugModeProfiler -->

- 枚举类型。枚举值如下：

|值|描述|
|---|---|
|`profiler`||


`action`: <!-- md:samp ScriptProfilerStop -->

- 枚举类型。枚举值如下：

|值|描述|
|---|---|
|`stop`||



/////

////

///

/// tab | 重载3
```mcfunction
/script watchdog exportstats
```

//// html | div.result
///// define
`mode`: <!-- md:samp ScriptDebugModeWatchdog -->

- 枚举类型。枚举值如下：

|值|描述|
|---|---|
|`watchdog`||


`action`: <!-- md:samp ScriptWatchdogDumpMemory -->

- 枚举类型。枚举值如下：

|值|描述|
|---|---|
|`exportstats`||



/////

////

///
