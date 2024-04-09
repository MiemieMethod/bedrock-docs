# `/camerashake`

> 文档版本：1.21.0.20

`/camerashake`命令command.camerashake.description

/// settings | 执行条件
该命令需要权限等级：`gamedirectors`|`1`。该命令需要开启作弊。
///

## 用法

/// tab | 重载1
```mcfunction
/camerashake add <player:target> [intensity:float] [seconds:float] [shakeType:CameraShakeType]
```

//// html | div.result
command.camerashake.1.description

///// define
`action`：<!-- md:samp CameraShakeActionAdd -->

- 枚举类型。command.enum.camerashakeactionadd.description单值枚举，请直接使用`add`。

`player`：<!-- md:samp target -->

- 基本类型。command.camerashake.player.description

`intensity`：<!-- md:samp float -->

- 基本类型，可选。command.camerashake.intensity.description

`seconds`：<!-- md:samp float -->

- 基本类型，可选。command.camerashake.seconds.description

`shakeType`：<!-- md:samp CameraShakeType -->

- 枚举类型，可选。command.enum.camerashaketype.description枚举值如下：

  |值|描述|
  |---|---|
  |`positional`|command.enum.camerashaketype.positional|
  |`rotational`|command.enum.camerashaketype.rotational|



/////

////

///

/// tab | 重载2
```mcfunction
/camerashake stop [player:target]
```

//// html | div.result
command.camerashake.2.description

///// define
`action`：<!-- md:samp CameraShakeActionStop -->

- 枚举类型。command.enum.camerashakeactionstop.description单值枚举，请直接使用`stop`。

`player`：<!-- md:samp target -->

- 基本类型，可选。command.camerashake.player.description


/////

////

///
