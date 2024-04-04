# `/title`

> 文档版本：1.20.80.24

`/title`命令Controls screen titles.

/// settings | 执行条件
该命令需要权限等级：`gamedirectors`|`1`。该命令需要开启作弊。
///

## 用法

/// tab | 重载1
```mcfunction
/title <player:target> clear
```

//// html | div.result
///// define
`player`：<!-- md:samp target -->

- 基本类型。

`clear`：<!-- md:samp TitleClear -->

- 枚举类型。单值枚举，请直接使用`clear`。


/////

////

///

/// tab | 重载2
```mcfunction
/title <player:target> reset
```

//// html | div.result
///// define
`player`：<!-- md:samp target -->

- 基本类型。

`reset`：<!-- md:samp TitleReset -->

- 枚举类型。单值枚举，请直接使用`reset`。


/////

////

///

/// tab | 重载3
```mcfunction
/title <player:target> <titleLocation:TitleSet> <titleText:message>
```

//// html | div.result
///// define
`player`：<!-- md:samp target -->

- 基本类型。

`titleLocation`：<!-- md:samp TitleSet -->

- 枚举类型。枚举值如下：

  |值|描述|
  |---|---|
  |`title`||
  |`subtitle`||
  |`actionbar`||


`titleText`：<!-- md:samp message -->

- 基本类型。


/////

////

///

/// tab | 重载4
```mcfunction
/title <player:target> times <fadeIn:int> <stay:int> <fadeOut:int>
```

//// html | div.result
///// define
`player`：<!-- md:samp target -->

- 基本类型。

`times`：<!-- md:samp TitleTimes -->

- 枚举类型。单值枚举，请直接使用`times`。

`fadeIn`：<!-- md:samp int -->

- 基本类型。

`stay`：<!-- md:samp int -->

- 基本类型。

`fadeOut`：<!-- md:samp int -->

- 基本类型。


/////

////

///
