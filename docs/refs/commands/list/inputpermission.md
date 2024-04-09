# `/inputpermission`

> 文档版本：1.21.0.20

`/inputpermission`命令command.inputpermission.description

/// settings | 执行条件
该命令需要权限等级：`gamedirectors`|`1`。该命令需要开启作弊。
///

## 用法

/// tab | 重载1
```mcfunction
/inputpermission set <targets:target> <permission:permission> <state:state>
```

//// html | div.result
command.inputpermission.1.description

///// define
`option`：<!-- md:samp Option_Set -->

- 枚举类型。command.enum.option_set.description单值枚举，请直接使用`set`。

`targets`：<!-- md:samp target -->

- 基本类型。command.inputpermission.targets.description

`permission`：<!-- md:samp permission -->

- 枚举类型。command.enum.permission.description枚举值如下：

  |值|描述|
  |---|---|
  |`movement`|command.enum.permission.movement|
  |`camera`|command.enum.permission.camera|


`state`：<!-- md:samp state -->

- 枚举类型。command.enum.state.description枚举值如下：

  |值|描述|
  |---|---|
  |`enabled`|command.enum.state.enabled|
  |`disabled`|command.enum.state.disabled|



/////

////

///

/// tab | 重载2
```mcfunction
/inputpermission query <targets:target> <permission:permission> [state:state]
```

//// html | div.result
command.inputpermission.2.description

///// define
`option`：<!-- md:samp Option_Query -->

- 枚举类型。command.enum.option_query.description单值枚举，请直接使用`query`。

`targets`：<!-- md:samp target -->

- 基本类型。command.inputpermission.targets.description

`permission`：<!-- md:samp permission -->

- 枚举类型。command.enum.permission.description枚举值如下：

  |值|描述|
  |---|---|
  |`movement`|command.enum.permission.movement|
  |`camera`|command.enum.permission.camera|


`state`：<!-- md:samp state -->

- 枚举类型，可选。command.enum.state.description枚举值如下：

  |值|描述|
  |---|---|
  |`enabled`|command.enum.state.enabled|
  |`disabled`|command.enum.state.disabled|



/////

////

///
