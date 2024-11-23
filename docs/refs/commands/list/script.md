# `/script`

> 文档版本：1.21.60.21

`/script`命令command.script.description

/// settings | 执行条件
该命令需要权限等级：`admin`|`2`。该命令需要开启作弊。
///

## 用法

/// tab | 重载1
```mcfunction
/script debugger listen <port:int>
```

//// html | div.result
command.script.1.description

///// define
`mode`：<!-- md:samp ScriptDebugModeDebugger -->

- 枚举类型。command.enum.scriptdebugmodedebugger.description单值枚举，请直接使用`debugger`。

`action`：<!-- md:samp ScriptDebuggerListen -->

- 枚举类型。command.enum.scriptdebuggerlisten.description单值枚举，请直接使用`listen`。

`port`：<!-- md:samp int -->

- 基本类型。command.script.port.description


/////

////

///

/// tab | 重载2
```mcfunction
/script debugger connect [host:string] [port:int]
```

//// html | div.result
command.script.2.description

///// define
`mode`：<!-- md:samp ScriptDebugModeDebugger -->

- 枚举类型。command.enum.scriptdebugmodedebugger.description单值枚举，请直接使用`debugger`。

`action`：<!-- md:samp ScriptDebuggerConnect -->

- 枚举类型。command.enum.scriptdebuggerconnect.description单值枚举，请直接使用`connect`。

`host`：<!-- md:samp string -->

- 基本类型，可选。command.script.host.description

`port`：<!-- md:samp int -->

- 基本类型，可选。command.script.port.description


/////

////

///

/// tab | 重载3
```mcfunction
/script debugger close
```

//// html | div.result
command.script.3.description

///// define
`mode`：<!-- md:samp ScriptDebugModeDebugger -->

- 枚举类型。command.enum.scriptdebugmodedebugger.description单值枚举，请直接使用`debugger`。

`action`：<!-- md:samp ScriptDebuggerClose -->

- 枚举类型。command.enum.scriptdebuggerclose.description单值枚举，请直接使用`close`。


/////

////

///

/// tab | 重载4
```mcfunction
/script profiler start
```

//// html | div.result
command.script.4.description

///// define
`mode`：<!-- md:samp ScriptDebugModeProfiler -->

- 枚举类型。command.enum.scriptdebugmodeprofiler.description单值枚举，请直接使用`profiler`。

`action`：<!-- md:samp ScriptProfilerStart -->

- 枚举类型。command.enum.scriptprofilerstart.description单值枚举，请直接使用`start`。


/////

////

///

/// tab | 重载5
```mcfunction
/script profiler stop
```

//// html | div.result
command.script.5.description

///// define
`mode`：<!-- md:samp ScriptDebugModeProfiler -->

- 枚举类型。command.enum.scriptdebugmodeprofiler.description单值枚举，请直接使用`profiler`。

`action`：<!-- md:samp ScriptProfilerStop -->

- 枚举类型。command.enum.scriptprofilerstop.description单值枚举，请直接使用`stop`。


/////

////

///

/// tab | 重载6
```mcfunction
/script watchdog exportstats
```

//// html | div.result
command.script.6.description

///// define
`mode`：<!-- md:samp ScriptDebugModeWatchdog -->

- 枚举类型。command.enum.scriptdebugmodewatchdog.description单值枚举，请直接使用`watchdog`。

`action`：<!-- md:samp ScriptWatchdogDumpMemory -->

- 枚举类型。command.enum.scriptwatchdogdumpmemory.description单值枚举，请直接使用`exportstats`。


/////

////

///
