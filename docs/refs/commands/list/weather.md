# `/weather`

> 文档版本：1.21.0.24

`/weather`命令command.weather.description

/// settings | 执行条件
该命令需要权限等级：`gamedirectors`|`1`。该命令需要开启作弊。
///

## 用法

/// tab | 重载1
```mcfunction
/weather <type:WeatherType> [duration:int]
```

//// html | div.result
command.weather.1.description

///// define
`type`：<!-- md:samp WeatherType -->

- 枚举类型。command.enum.weathertype.description枚举值如下：

  |值|描述|
  |---|---|
  |`clear`|command.enum.weathertype.clear|
  |`rain`|command.enum.weathertype.rain|
  |`thunder`|command.enum.weathertype.thunder|


`duration`：<!-- md:samp int -->

- 基本类型，可选。command.weather.duration.description


/////

////

///

/// tab | 重载2
```mcfunction
/weather query
```

//// html | div.result
command.weather.2.description

///// define
`query`：<!-- md:samp WeatherQuery -->

- 枚举类型。command.enum.weatherquery.description单值枚举，请直接使用`query`。


/////

////

///
