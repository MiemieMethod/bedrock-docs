# `/script`

> 文档版本：1.21.0.21

`/script`命令command.script.description

/// settings | 执行条件
该命令需要权限等级：`admin`|`2`。该命令需要开启作弊。
///

## 用法

/// tab | 重载1
```mcfunction
/script profiler start
```

//// html | div.result
command.script.1.description

///// define
`mode`：<!-- md:samp ScriptDebugModeProfiler -->

- 枚举类型。command.enum.scriptdebugmodeprofiler.description单值枚举，请直接使用`profiler`。

`action`：<!-- md:samp ScriptProfilerStart -->

- 枚举类型。command.enum.scriptprofilerstart.description单值枚举，请直接使用`start`。


/////

////

///

/// tab | 重载2
```mcfunction
/script profiler stop
```

//// html | div.result
command.script.2.description

///// define
`mode`：<!-- md:samp ScriptDebugModeProfiler -->

- 枚举类型。command.enum.scriptdebugmodeprofiler.description单值枚举，请直接使用`profiler`。

`action`：<!-- md:samp ScriptProfilerStop -->

- 枚举类型。command.enum.scriptprofilerstop.description单值枚举，请直接使用`stop`。


/////

////

///

/// tab | 重载3
```mcfunction
/script watchdog exportstats
```

//// html | div.result
command.script.3.description

///// define
`mode`：<!-- md:samp ScriptDebugModeWatchdog -->

- 枚举类型。command.enum.scriptdebugmodewatchdog.description单值枚举，请直接使用`watchdog`。

`action`：<!-- md:samp ScriptWatchdogDumpMemory -->

- 枚举类型。command.enum.scriptwatchdogdumpmemory.description单值枚举，请直接使用`exportstats`。


/////

////

///
