# `/titleraw`

> 文档版本：1.21.60.21

`/titleraw`命令command.titleraw.description

/// settings | 执行条件
该命令需要权限等级：`gamedirectors`|`1`。该命令需要开启作弊。
///

## 用法

/// tab | 重载1
```mcfunction
/titleraw <player:target> clear
```

//// html | div.result
command.titleraw.1.description

///// define
`player`：<!-- md:samp target -->

- 基本类型。command.titleraw.player.description

`clear`：<!-- md:samp TitleRawClear -->

- 枚举类型。command.enum.titlerawclear.description单值枚举，请直接使用`clear`。


/////

////

///

/// tab | 重载2
```mcfunction
/titleraw <player:target> reset
```

//// html | div.result
command.titleraw.2.description

///// define
`player`：<!-- md:samp target -->

- 基本类型。command.titleraw.player.description

`reset`：<!-- md:samp TitleRawReset -->

- 枚举类型。command.enum.titlerawreset.description单值枚举，请直接使用`reset`。


/////

////

///

/// tab | 重载3
```mcfunction
/titleraw <player:target> <titleLocation:TitleRawSet> <raw json titleText:json>
```

//// html | div.result
command.titleraw.3.description

///// define
`player`：<!-- md:samp target -->

- 基本类型。command.titleraw.player.description

`titleLocation`：<!-- md:samp TitleRawSet -->

- 枚举类型。command.enum.titlerawset.description枚举值如下：

  |值|描述|
  |---|---|
  |`title`|command.enum.titlerawset.title|
  |`subtitle`|command.enum.titlerawset.subtitle|
  |`actionbar`|command.enum.titlerawset.actionbar|


`raw json titleText`：<!-- md:samp json -->

- 基本类型。command.titleraw.raw json titleText.description


/////

////

///

/// tab | 重载4
```mcfunction
/titleraw <player:target> times <fadeIn:int> <stay:int> <fadeOut:int>
```

//// html | div.result
command.titleraw.4.description

///// define
`player`：<!-- md:samp target -->

- 基本类型。command.titleraw.player.description

`times`：<!-- md:samp TitleRawTimes -->

- 枚举类型。command.enum.titlerawtimes.description单值枚举，请直接使用`times`。

`fadeIn`：<!-- md:samp int -->

- 基本类型。command.titleraw.fadeIn.description

`stay`：<!-- md:samp int -->

- 基本类型。command.titleraw.stay.description

`fadeOut`：<!-- md:samp int -->

- 基本类型。command.titleraw.fadeOut.description


/////

////

///
