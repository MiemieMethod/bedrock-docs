# `/fog`

> 文档版本：1.21.0.20

`/fog`命令command.fog.description

/// settings | 执行条件
该命令需要权限等级：`gamedirectors`|`1`。该命令需要开启作弊。
///

## 用法

/// tab | 重载1
```mcfunction
/fog <victim:target> push <fogId:string> <userProvidedId:string>
```

//// html | div.result
command.fog.1.description

///// define
`victim`：<!-- md:samp target -->

- 基本类型。command.fog.victim.description

`mode`：<!-- md:samp add -->

- 枚举类型。command.enum.add.description单值枚举，请直接使用`push`。

`fogId`：<!-- md:samp string -->

- 基本类型。command.fog.fogId.description

`userProvidedId`：<!-- md:samp string -->

- 基本类型。command.fog.userProvidedId.description


/////

////

///

/// tab | 重载2
```mcfunction
/fog <victim:target> <mode:delete> <userProvidedId:string>
```

//// html | div.result
command.fog.2.description

///// define
`victim`：<!-- md:samp target -->

- 基本类型。command.fog.victim.description

`mode`：<!-- md:samp delete -->

- 枚举类型。command.enum.delete.description枚举值如下：

  |值|描述|
  |---|---|
  |`pop`|command.enum.delete.pop|
  |`remove`|command.enum.delete.remove|


`userProvidedId`：<!-- md:samp string -->

- 基本类型。command.fog.userProvidedId.description


/////

////

///
