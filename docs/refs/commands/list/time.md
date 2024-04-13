# `/time`

> 文档版本：1.21.0.21

`/time`命令command.time.description

/// settings | 执行条件
该命令需要权限等级：`gamedirectors`|`1`。该命令需要开启作弊。
///

## 用法

/// tab | 重载1
```mcfunction
/time add <amount:int>
```

//// html | div.result
command.time.1.description

///// define
`mode`：<!-- md:samp TimeModeAdd -->

- 枚举类型。command.enum.timemodeadd.description单值枚举，请直接使用`add`。

`amount`：<!-- md:samp int -->

- 基本类型。command.time.amount.description


/////

////

///

/// tab | 重载2
```mcfunction
/time set <amount:int>
```

//// html | div.result
command.time.2.description

///// define
`mode`：<!-- md:samp TimeModeSet -->

- 枚举类型。command.enum.timemodeset.description单值枚举，请直接使用`set`。

`amount`：<!-- md:samp int -->

- 基本类型。command.time.amount.description


/////

////

///

/// tab | 重载3
```mcfunction
/time set <time:TimeSpec>
```

//// html | div.result
command.time.3.description

///// define
`mode`：<!-- md:samp TimeModeSet -->

- 枚举类型。command.enum.timemodeset.description单值枚举，请直接使用`set`。

`time`：<!-- md:samp TimeSpec -->

- 枚举类型。command.enum.timespec.description枚举值如下：

  |值|描述|
  |---|---|
  |`day`|command.enum.timespec.day|
  |`sunrise`|command.enum.timespec.sunrise|
  |`noon`|command.enum.timespec.noon|
  |`sunset`|command.enum.timespec.sunset|
  |`night`|command.enum.timespec.night|
  |`midnight`|command.enum.timespec.midnight|



/////

////

///

/// tab | 重载4
```mcfunction
/time query <time:TimeQuery>
```

//// html | div.result
command.time.4.description

///// define
`mode`：<!-- md:samp TimeModeQuery -->

- 枚举类型。command.enum.timemodequery.description单值枚举，请直接使用`query`。

`time`：<!-- md:samp TimeQuery -->

- 枚举类型。command.enum.timequery.description枚举值如下：

  |值|描述|
  |---|---|
  |`daytime`|command.enum.timequery.daytime|
  |`gametime`|command.enum.timequery.gametime|
  |`day`|command.enum.timequery.day|



/////

////

///
