# `/schedule`

> 文档版本：1.20.80.24

`/schedule`命令Schedules an action to be executed once an area is loaded, or after a certain amount of time.

/// settings | 执行条件
该命令需要权限等级：`gamedirectors`|`1`。该命令需要开启作弊。
///

## 用法

/// tab | 重载1
```mcfunction
/schedule on_area_loaded add <from:x y z> <to:x y z> <function:filepath>
```

//// html | div.result
///// define
`mode`：<!-- md:samp ScheduleActionOnAreaLoaded -->

- 枚举类型。单值枚举，请直接使用`on_area_loaded`。

`condition`：<!-- md:samp RequestAction -->

- 枚举类型。单值枚举，请直接使用`add`。

`from`：<!-- md:samp x y z -->

- 基本类型。

`to`：<!-- md:samp x y z -->

- 基本类型。

`function`：<!-- md:samp filepath -->

- 基本类型。


/////

////

///

/// tab | 重载2
```mcfunction
/schedule on_area_loaded add circle <center:x y z> <radius:int> <function:filepath>
```

//// html | div.result
///// define
`mode`：<!-- md:samp ScheduleActionOnAreaLoaded -->

- 枚举类型。单值枚举，请直接使用`on_area_loaded`。

`condition`：<!-- md:samp RequestAction -->

- 枚举类型。单值枚举，请直接使用`add`。

`type`：<!-- md:samp CircleArea -->

- 枚举类型。单值枚举，请直接使用`circle`。

`center`：<!-- md:samp x y z -->

- 基本类型。

`radius`：<!-- md:samp int -->

- 基本类型。

`function`：<!-- md:samp filepath -->

- 基本类型。


/////

////

///

/// tab | 重载3
```mcfunction
/schedule on_area_loaded add tickingarea <name:string> <function:filepath>
```

//// html | div.result
///// define
`mode`：<!-- md:samp ScheduleActionOnAreaLoaded -->

- 枚举类型。单值枚举，请直接使用`on_area_loaded`。

`condition`：<!-- md:samp RequestAction -->

- 枚举类型。单值枚举，请直接使用`add`。

`type`：<!-- md:samp TickingArea -->

- 枚举类型。单值枚举，请直接使用`tickingarea`。

`name`：<!-- md:samp string -->

- 基本类型。

`function`：<!-- md:samp filepath -->

- 基本类型。


/////

////

///
