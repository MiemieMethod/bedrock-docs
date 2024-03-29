# `/sendshowstoreoffer`

> 文档版本：1.20.80.24

`/sendshowstoreoffer`命令Sends a request to show a store offer to the target player.

/// note | 执行条件
该命令需要权限等级：`internal`|`4`。该命令需要开启作弊。
///

## 用法

/// tab | 重载1
```mcfunction
/sendshowstoreoffer <player:target> <redirectType:RedirectLocation> <offerId:string>
```

//// html | div.result
///// define
`player`: <!-- md:samp target -->

- 基本类型。

`redirectType`: <!-- md:samp RedirectLocation -->

- 枚举类型。枚举值如下：

|值|描述|
|---|---|
|`marketplace`||
|`character`||


`offerId`: <!-- md:samp string -->

- 基本类型。


/////

////

///

/// tab | 重载2
```mcfunction
/sendshowstoreoffer <player:target> server
```

//// html | div.result
///// define
`player`: <!-- md:samp target -->

- 基本类型。

`redirectType`: <!-- md:samp 3PServerOfferList -->

- 枚举类型。枚举值如下：

|值|描述|
|---|---|
|`server`||



/////

////

///
