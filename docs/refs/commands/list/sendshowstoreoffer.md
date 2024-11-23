# `/sendshowstoreoffer`

> 文档版本：1.21.60.21

`/sendshowstoreoffer`命令command.sendshowstoreoffer.description

/// settings | 执行条件
该命令需要权限等级：`owner`|`4`。该命令需要开启作弊。
///

## 用法

/// tab | 重载1
```mcfunction
/sendshowstoreoffer <player:target> <redirectType:RedirectLocation> <offerId:string>
```

//// html | div.result
command.sendshowstoreoffer.1.description

///// define
`player`：<!-- md:samp target -->

- 基本类型。command.sendshowstoreoffer.player.description

`redirectType`：<!-- md:samp RedirectLocation -->

- 枚举类型。command.enum.redirectlocation.description枚举值如下：

  |值|描述|
  |---|---|
  |`marketplace`|command.enum.redirectlocation.marketplace|
  |`character`|command.enum.redirectlocation.character|


`offerId`：<!-- md:samp string -->

- 基本类型。command.sendshowstoreoffer.offerId.description


/////

////

///

/// tab | 重载2
```mcfunction
/sendshowstoreoffer <player:target> server
```

//// html | div.result
command.sendshowstoreoffer.2.description

///// define
`player`：<!-- md:samp target -->

- 基本类型。command.sendshowstoreoffer.player.description

`redirectType`：<!-- md:samp 3PServerOfferList -->

- 枚举类型。command.enum.3pserverofferlist.description单值枚举，请直接使用`server`。


/////

////

///
