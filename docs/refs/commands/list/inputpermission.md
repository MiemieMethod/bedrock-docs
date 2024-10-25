# `/inputpermission`

> 文档版本：1.21.50.25

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
  |`camera`|command.enum.permission.camera|
  |`movement`|command.enum.permission.movement|
  |`jump`|command.enum.permission.jump|
  |`lateral_movement`|command.enum.permission.lateral_movement|
  |`sneak`|command.enum.permission.sneak|
  |`dismount`|command.enum.permission.dismount|
  |`mount`|command.enum.permission.mount|
  |`move_backward`|command.enum.permission.move_backward|
  |`move_forward`|command.enum.permission.move_forward|
  |`move_left`|command.enum.permission.move_left|
  |`move_right`|command.enum.permission.move_right|


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
  |`camera`|command.enum.permission.camera|
  |`movement`|command.enum.permission.movement|
  |`jump`|command.enum.permission.jump|
  |`lateral_movement`|command.enum.permission.lateral_movement|
  |`sneak`|command.enum.permission.sneak|
  |`dismount`|command.enum.permission.dismount|
  |`mount`|command.enum.permission.mount|
  |`move_backward`|command.enum.permission.move_backward|
  |`move_forward`|command.enum.permission.move_forward|
  |`move_left`|command.enum.permission.move_left|
  |`move_right`|command.enum.permission.move_right|


`state`：<!-- md:samp state -->

- 枚举类型，可选。command.enum.state.description枚举值如下：

  |值|描述|
  |---|---|
  |`enabled`|command.enum.state.enabled|
  |`disabled`|command.enum.state.disabled|



/////

////

///
