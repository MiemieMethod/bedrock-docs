# `/allowlist`

> 文档版本：1.21.60.21

`/allowlist`命令command.allowlist.description

/// settings | 执行条件
该命令需要权限等级：`owner`|`4`。该命令需要开启作弊。
///

/// info | 别名
该命令还可以使用以下别名：`/whitelist`。
///

## 用法

/// tab | 重载1
```mcfunction
/allowlist <action:AllowListAction> [name:string]
```

//// html | div.result
command.allowlist.1.description

///// define
`action`：<!-- md:samp AllowListAction -->

- 枚举类型。command.enum.allowlistaction.description枚举值如下：

  |值|描述|
  |---|---|
  |`add`|command.enum.allowlistaction.add|
  |`remove`|command.enum.allowlistaction.remove|
  |`list`|command.enum.allowlistaction.list|
  |`reload`|command.enum.allowlistaction.reload|
  |`on`|command.enum.allowlistaction.on|
  |`off`|command.enum.allowlistaction.off|


`name`：<!-- md:samp string -->

- 基本类型，可选。command.allowlist.name.description


/////

////

///
