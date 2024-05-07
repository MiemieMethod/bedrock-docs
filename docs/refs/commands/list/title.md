# `/title`

> 文档版本：1.21.0.24

`/title`命令command.title.description

/// settings | 执行条件
该命令需要权限等级：`gamedirectors`|`1`。该命令需要开启作弊。
///

## 用法

/// tab | 重载1
```mcfunction
/title <player:target> clear
```

//// html | div.result
command.title.1.description

///// define
`player`：<!-- md:samp target -->

- 基本类型。command.title.player.description

`clear`：<!-- md:samp TitleClear -->

- 枚举类型。command.enum.titleclear.description单值枚举，请直接使用`clear`。


/////

////

///

/// tab | 重载2
```mcfunction
/title <player:target> reset
```

//// html | div.result
command.title.2.description

///// define
`player`：<!-- md:samp target -->

- 基本类型。command.title.player.description

`reset`：<!-- md:samp TitleReset -->

- 枚举类型。command.enum.titlereset.description单值枚举，请直接使用`reset`。


/////

////

///

/// tab | 重载3
```mcfunction
/title <player:target> <titleLocation:TitleSet> <titleText:message>
```

//// html | div.result
command.title.3.description

///// define
`player`：<!-- md:samp target -->

- 基本类型。command.title.player.description

`titleLocation`：<!-- md:samp TitleSet -->

- 枚举类型。command.enum.titleset.description枚举值如下：

  |值|描述|
  |---|---|
  |`title`|command.enum.titleset.title|
  |`subtitle`|command.enum.titleset.subtitle|
  |`actionbar`|command.enum.titleset.actionbar|


`titleText`：<!-- md:samp message -->

- 基本类型。command.title.titleText.description


/////

////

///

/// tab | 重载4
```mcfunction
/title <player:target> times <fadeIn:int> <stay:int> <fadeOut:int>
```

//// html | div.result
command.title.4.description

///// define
`player`：<!-- md:samp target -->

- 基本类型。command.title.player.description

`times`：<!-- md:samp TitleTimes -->

- 枚举类型。command.enum.titletimes.description单值枚举，请直接使用`times`。

`fadeIn`：<!-- md:samp int -->

- 基本类型。command.title.fadeIn.description

`stay`：<!-- md:samp int -->

- 基本类型。command.title.stay.description

`fadeOut`：<!-- md:samp int -->

- 基本类型。command.title.fadeOut.description


/////

////

///
