# `/fog`

> 文档版本：1.21.0.20

`/fog`命令Add or remove fog settings file

/// settings | 执行条件
该命令需要权限等级：`gamedirectors`|`1`。该命令需要开启作弊。
///

## 用法

/// tab | 重载1
```mcfunction
/fog <victim:target> push <fogId:string> <userProvidedId:string>
```

//// html | div.result
///// define
`victim`：<!-- md:samp target -->

- 基本类型。

`mode`：<!-- md:samp add -->

- 枚举类型。单值枚举，请直接使用`push`。

`fogId`：<!-- md:samp string -->

- 基本类型。

`userProvidedId`：<!-- md:samp string -->

- 基本类型。


/////

////

///

/// tab | 重载2
```mcfunction
/fog <victim:target> <mode:delete> <userProvidedId:string>
```

//// html | div.result
///// define
`victim`：<!-- md:samp target -->

- 基本类型。

`mode`：<!-- md:samp delete -->

- 枚举类型。枚举值如下：

  |值|描述|
  |---|---|
  |`pop`||
  |`remove`||


`userProvidedId`：<!-- md:samp string -->

- 基本类型。


/////

////

///
