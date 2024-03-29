# /titleraw

> 文档版本：1.20.80.24

`/titleraw`命令Controls screen titles with JSON messages.

/// note | 执行条件
该命令需要权限等级：`gamedirectors`|`1`。该命令需要开启作弊。
///

## 用法

/// tab | `重载1`
```mcfunction
/titleraw <player:target> clear
```

//// html | div.result
///// define
`player`: <!-- md:samp target -->

- 基本类型。

`clear`: <!-- md:samp TitleRawClear -->

- 枚举类型。枚举值如下：

|值|描述|
|---|---|
|`clear`||



/////

////

///

/// tab | `重载2`
```mcfunction
/titleraw <player:target> reset
```

//// html | div.result
///// define
`player`: <!-- md:samp target -->

- 基本类型。

`reset`: <!-- md:samp TitleRawReset -->

- 枚举类型。枚举值如下：

|值|描述|
|---|---|
|`reset`||



/////

////

///

/// tab | `重载3`
```mcfunction
/titleraw <player:target> <titleLocation:TitleRawSet> <raw json titleText:json>
```

//// html | div.result
///// define
`player`: <!-- md:samp target -->

- 基本类型。

`titleLocation`: <!-- md:samp TitleRawSet -->

- 枚举类型。枚举值如下：

|值|描述|
|---|---|
|`title`||
|`subtitle`||
|`actionbar`||


`raw json titleText`: <!-- md:samp json -->

- 基本类型。


/////

////

///

/// tab | `重载4`
```mcfunction
/titleraw <player:target> times <fadeIn:int> <stay:int> <fadeOut:int>
```

//// html | div.result
///// define
`player`: <!-- md:samp target -->

- 基本类型。

`times`: <!-- md:samp TitleRawTimes -->

- 枚举类型。枚举值如下：

|值|描述|
|---|---|
|`times`||


`fadeIn`: <!-- md:samp int -->

- 基本类型。

`stay`: <!-- md:samp int -->

- 基本类型。

`fadeOut`: <!-- md:samp int -->

- 基本类型。


/////

////

///
