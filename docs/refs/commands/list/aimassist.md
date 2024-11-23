# `/aimassist`

> 文档版本：1.21.60.21

`/aimassist`命令command.aimassist.description

/// settings | 执行条件
该命令需要权限等级：`gamedirectors`|`1`。该命令需要开启作弊。
///

## 用法

/// tab | 重载1
```mcfunction
/aimassist <players:target> set [x angle:float] [y angle:float] [max distance:float] [target mode:AimAssistTargetMode] [preset id:string]
```

//// html | div.result
command.aimassist.1.description

///// define
`players`：<!-- md:samp target -->

- 基本类型。command.aimassist.players.description

`set`：<!-- md:samp AimAssistActionSet -->

- 枚举类型。command.enum.aimassistactionset.description单值枚举，请直接使用`set`。

`x angle`：<!-- md:samp float -->

- 基本类型，可选。command.aimassist.x angle.description

`y angle`：<!-- md:samp float -->

- 基本类型，可选。command.aimassist.y angle.description

`max distance`：<!-- md:samp float -->

- 基本类型，可选。command.aimassist.max distance.description

`target mode`：<!-- md:samp AimAssistTargetMode -->

- 枚举类型，可选。command.enum.aimassisttargetmode.description枚举值如下：

  |值|描述|
  |---|---|
  |`distance`|command.enum.aimassisttargetmode.distance|
  |`angle`|command.enum.aimassisttargetmode.angle|


`preset id`：<!-- md:samp string -->

- 基本类型，可选。command.aimassist.preset id.description


/////

////

///

/// tab | 重载2
```mcfunction
/aimassist <players:target> clear
```

//// html | div.result
command.aimassist.2.description

///// define
`players`：<!-- md:samp target -->

- 基本类型。command.aimassist.players.description

`clear`：<!-- md:samp AimAssistActionClear -->

- 枚举类型。command.enum.aimassistactionclear.description单值枚举，请直接使用`clear`。


/////

////

///
