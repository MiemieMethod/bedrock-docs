# `/gamemode`

> 文档版本：1.21.60.21

`/gamemode`命令command.gamemode.description

/// settings | 执行条件
该命令需要权限等级：`gamedirectors`|`1`。该命令需要开启作弊。
///

## 用法

/// tab | 重载1
```mcfunction
/gamemode <gameMode:GameMode> [player:target]
```

//// html | div.result
command.gamemode.1.description

///// define
`gameMode`：<!-- md:samp GameMode -->

- 枚举类型。command.enum.gamemode.description枚举值如下：

  |值|描述|
  |---|---|
  |`default`|command.enum.gamemode.default|
  |`creative`|command.enum.gamemode.creative|
  |`spectator`|command.enum.gamemode.spectator|
  |`survival`|command.enum.gamemode.survival|
  |`adventure`|command.enum.gamemode.adventure|
  |`d`|command.enum.gamemode.d|
  |`c`|command.enum.gamemode.c|
  |`s`|command.enum.gamemode.s|
  |`a`|command.enum.gamemode.a|


`player`：<!-- md:samp target -->

- 基本类型，可选。command.gamemode.player.description


/////

////

///

/// tab | 重载2
```mcfunction
/gamemode <gameMode:int> [player:target]
```

//// html | div.result
command.gamemode.2.description

///// define
`gameMode`：<!-- md:samp int -->

- 基本类型。command.gamemode.gameMode.description

`player`：<!-- md:samp target -->

- 基本类型，可选。command.gamemode.player.description


/////

////

///
