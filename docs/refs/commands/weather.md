# `/weather`

> 文档版本：1.20.80.24

`/weather`命令Sets the weather.

/// note | 执行条件
该命令需要权限等级：`gamedirectors`|`1`。该命令需要开启作弊。
///

## 用法

/// tab | 重载1
```mcfunction
/weather <type:WeatherType> [duration:int]
```

//// html | div.result
///// define
`type`: <!-- md:samp WeatherType -->

- 枚举类型。枚举值如下：

|值|描述|
|---|---|
|`clear`||
|`rain`||
|`thunder`||


`duration`: <!-- md:samp int -->

- 基本类型。


/////

////

///

/// tab | 重载2
```mcfunction
/weather query
```

//// html | div.result
///// define
`query`: <!-- md:samp WeatherQuery -->

- 枚举类型。单值枚举，请直接使用`query`。


/////

////

///
