# `/time`

> 文档版本：1.20.80.24

`/time`命令Changes or queries the world's game time.

/// note | 执行条件
该命令需要权限等级：`gamedirectors`|`1`。该命令需要开启作弊。
///

## 用法

/// tab | 重载1
```mcfunction
/time add <amount:int>
```

//// html | div.result
///// define
`mode`: <!-- md:samp TimeModeAdd -->

- 枚举类型。枚举值如下：

|值|描述|
|---|---|
|`add`||


`amount`: <!-- md:samp int -->

- 基本类型。


/////

////

///

/// tab | 重载2
```mcfunction
/time set <amount:int>
```

//// html | div.result
///// define
`mode`: <!-- md:samp TimeModeSet -->

- 枚举类型。枚举值如下：

|值|描述|
|---|---|
|`set`||


`amount`: <!-- md:samp int -->

- 基本类型。


/////

////

///

/// tab | 重载3
```mcfunction
/time set <time:TimeSpec>
```

//// html | div.result
///// define
`mode`: <!-- md:samp TimeModeSet -->

- 枚举类型。枚举值如下：

|值|描述|
|---|---|
|`set`||


`time`: <!-- md:samp TimeSpec -->

- 枚举类型。枚举值如下：

|值|描述|
|---|---|
|`day`||
|`sunrise`||
|`noon`||
|`sunset`||
|`night`||
|`midnight`||



/////

////

///

/// tab | 重载4
```mcfunction
/time query <time:TimeQuery>
```

//// html | div.result
///// define
`mode`: <!-- md:samp TimeModeQuery -->

- 枚举类型。枚举值如下：

|值|描述|
|---|---|
|`query`||


`time`: <!-- md:samp TimeQuery -->

- 枚举类型。枚举值如下：

|值|描述|
|---|---|
|`daytime`||
|`gametime`||
|`day`||



/////

////

///
