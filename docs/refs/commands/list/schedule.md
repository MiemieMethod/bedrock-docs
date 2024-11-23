# `/schedule`

> 文档版本：1.21.60.21

`/schedule`命令command.schedule.description

/// settings | 执行条件
该命令需要权限等级：`gamedirectors`|`1`。该命令需要开启作弊。
///

## 用法

/// tab | 重载1
```mcfunction
/schedule delay add <function:filepath> <time:int> [DelayMode:DelayMode]
```

//// html | div.result
command.schedule.1.description

///// define
`mode`：<!-- md:samp ScheduleActionDelay -->

- 枚举类型。command.enum.scheduleactiondelay.description单值枚举，请直接使用`delay`。

`condition`：<!-- md:samp RequestActionAdd -->

- 枚举类型。command.enum.requestactionadd.description单值枚举，请直接使用`add`。

`function`：<!-- md:samp filepath -->

- 基本类型。command.schedule.function.description

`time`：<!-- md:samp int -->

- 基本类型。command.schedule.time.description

`DelayMode`：<!-- md:samp DelayMode -->

- 枚举类型，可选。command.enum.delaymode.description枚举值如下：

  |值|描述|
  |---|---|
  |`replace`|command.enum.delaymode.replace|
  |`append`|command.enum.delaymode.append|



/////

////

///

/// tab | 重载2
```mcfunction
/schedule delay add <function:filepath> <time:postfix_t> [DelayMode:DelayMode]
```

//// html | div.result
command.schedule.2.description

///// define
`mode`：<!-- md:samp ScheduleActionDelay -->

- 枚举类型。command.enum.scheduleactiondelay.description单值枚举，请直接使用`delay`。

`condition`：<!-- md:samp RequestActionAdd -->

- 枚举类型。command.enum.requestactionadd.description单值枚举，请直接使用`add`。

`function`：<!-- md:samp filepath -->

- 基本类型。command.schedule.function.description

`time`：<!-- md:samp postfix_t -->

- 基本类型。command.schedule.time.description

`DelayMode`：<!-- md:samp DelayMode -->

- 枚举类型，可选。command.enum.delaymode.description枚举值如下：

  |值|描述|
  |---|---|
  |`replace`|command.enum.delaymode.replace|
  |`append`|command.enum.delaymode.append|



/////

////

///

/// tab | 重载3
```mcfunction
/schedule delay add <function:filepath> <time:postfix_s> [DelayMode:DelayMode]
```

//// html | div.result
command.schedule.3.description

///// define
`mode`：<!-- md:samp ScheduleActionDelay -->

- 枚举类型。command.enum.scheduleactiondelay.description单值枚举，请直接使用`delay`。

`condition`：<!-- md:samp RequestActionAdd -->

- 枚举类型。command.enum.requestactionadd.description单值枚举，请直接使用`add`。

`function`：<!-- md:samp filepath -->

- 基本类型。command.schedule.function.description

`time`：<!-- md:samp postfix_s -->

- 基本类型。command.schedule.time.description

`DelayMode`：<!-- md:samp DelayMode -->

- 枚举类型，可选。command.enum.delaymode.description枚举值如下：

  |值|描述|
  |---|---|
  |`replace`|command.enum.delaymode.replace|
  |`append`|command.enum.delaymode.append|



/////

////

///

/// tab | 重载4
```mcfunction
/schedule delay add <function:filepath> <time:postfix_d> [DelayMode:DelayMode]
```

//// html | div.result
command.schedule.4.description

///// define
`mode`：<!-- md:samp ScheduleActionDelay -->

- 枚举类型。command.enum.scheduleactiondelay.description单值枚举，请直接使用`delay`。

`condition`：<!-- md:samp RequestActionAdd -->

- 枚举类型。command.enum.requestactionadd.description单值枚举，请直接使用`add`。

`function`：<!-- md:samp filepath -->

- 基本类型。command.schedule.function.description

`time`：<!-- md:samp postfix_d -->

- 基本类型。command.schedule.time.description

`DelayMode`：<!-- md:samp DelayMode -->

- 枚举类型，可选。command.enum.delaymode.description枚举值如下：

  |值|描述|
  |---|---|
  |`replace`|command.enum.delaymode.replace|
  |`append`|command.enum.delaymode.append|



/////

////

///

/// tab | 重载5
```mcfunction
/schedule delay clear <function:filepath>
```

//// html | div.result
command.schedule.5.description

///// define
`mode`：<!-- md:samp ScheduleActionDelay -->

- 枚举类型。command.enum.scheduleactiondelay.description单值枚举，请直接使用`delay`。

`condition`：<!-- md:samp RequestActionClear -->

- 枚举类型。command.enum.requestactionclear.description单值枚举，请直接使用`clear`。

`function`：<!-- md:samp filepath -->

- 基本类型。command.schedule.function.description


/////

////

///

/// tab | 重载6
```mcfunction
/schedule clear <function:filepath>
```

//// html | div.result
command.schedule.6.description

///// define
`mode`：<!-- md:samp ScheduleActionClear -->

- 枚举类型。command.enum.scheduleactionclear.description单值枚举，请直接使用`clear`。

`function`：<!-- md:samp filepath -->

- 基本类型。command.schedule.function.description


/////

////

///

/// tab | 重载7
```mcfunction
/schedule on_area_loaded add <from:x y z> <to:x y z> <function:filepath>
```

//// html | div.result
command.schedule.7.description

///// define
`mode`：<!-- md:samp ScheduleActionOnAreaLoaded -->

- 枚举类型。command.enum.scheduleactiononarealoaded.description单值枚举，请直接使用`on_area_loaded`。

`condition`：<!-- md:samp RequestActionAdd -->

- 枚举类型。command.enum.requestactionadd.description单值枚举，请直接使用`add`。

`from`：<!-- md:samp x y z -->

- 基本类型。command.schedule.from.description

`to`：<!-- md:samp x y z -->

- 基本类型。command.schedule.to.description

`function`：<!-- md:samp filepath -->

- 基本类型。command.schedule.function.description


/////

////

///

/// tab | 重载8
```mcfunction
/schedule on_area_loaded add circle <center:x y z> <radius:int> <function:filepath>
```

//// html | div.result
command.schedule.8.description

///// define
`mode`：<!-- md:samp ScheduleActionOnAreaLoaded -->

- 枚举类型。command.enum.scheduleactiononarealoaded.description单值枚举，请直接使用`on_area_loaded`。

`condition`：<!-- md:samp RequestActionAdd -->

- 枚举类型。command.enum.requestactionadd.description单值枚举，请直接使用`add`。

`type`：<!-- md:samp CircleArea -->

- 枚举类型。command.enum.circlearea.description单值枚举，请直接使用`circle`。

`center`：<!-- md:samp x y z -->

- 基本类型。command.schedule.center.description

`radius`：<!-- md:samp int -->

- 基本类型。command.schedule.radius.description

`function`：<!-- md:samp filepath -->

- 基本类型。command.schedule.function.description


/////

////

///

/// tab | 重载9
```mcfunction
/schedule on_area_loaded add tickingarea <name:string> <function:filepath>
```

//// html | div.result
command.schedule.9.description

///// define
`mode`：<!-- md:samp ScheduleActionOnAreaLoaded -->

- 枚举类型。command.enum.scheduleactiononarealoaded.description单值枚举，请直接使用`on_area_loaded`。

`condition`：<!-- md:samp RequestActionAdd -->

- 枚举类型。command.enum.requestactionadd.description单值枚举，请直接使用`add`。

`type`：<!-- md:samp TickingArea -->

- 枚举类型。command.enum.tickingarea.description单值枚举，请直接使用`tickingarea`。

`name`：<!-- md:samp string -->

- 基本类型。command.schedule.name.description

`function`：<!-- md:samp filepath -->

- 基本类型。command.schedule.function.description


/////

////

///

/// tab | 重载10
```mcfunction
/schedule on_area_loaded clear tickingarea <name:string> [function:filepath]
```

//// html | div.result
command.schedule.10.description

///// define
`mode`：<!-- md:samp ScheduleActionOnAreaLoaded -->

- 枚举类型。command.enum.scheduleactiononarealoaded.description单值枚举，请直接使用`on_area_loaded`。

`condition`：<!-- md:samp RequestActionClear -->

- 枚举类型。command.enum.requestactionclear.description单值枚举，请直接使用`clear`。

`cleartype`：<!-- md:samp TickingAreaName -->

- 枚举类型。command.enum.tickingareaname.description单值枚举，请直接使用`tickingarea`。

`name`：<!-- md:samp string -->

- 基本类型。command.schedule.name.description

`function`：<!-- md:samp filepath -->

- 基本类型，可选。command.schedule.function.description


/////

////

///

/// tab | 重载11
```mcfunction
/schedule on_area_loaded clear function <function:filepath>
```

//// html | div.result
command.schedule.11.description

///// define
`mode`：<!-- md:samp ScheduleActionOnAreaLoaded -->

- 枚举类型。command.enum.scheduleactiononarealoaded.description单值枚举，请直接使用`on_area_loaded`。

`condition`：<!-- md:samp RequestActionClear -->

- 枚举类型。command.enum.requestactionclear.description单值枚举，请直接使用`clear`。

`cleartype`：<!-- md:samp FunctionName -->

- 枚举类型。command.enum.functionname.description单值枚举，请直接使用`function`。

`function`：<!-- md:samp filepath -->

- 基本类型。command.schedule.function.description


/////

////

///
