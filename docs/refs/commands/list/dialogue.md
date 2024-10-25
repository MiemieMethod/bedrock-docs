# `/dialogue`

> 文档版本：1.21.50.25

`/dialogue`命令command.dialogue.description

/// settings | 执行条件
该命令需要权限等级：`gamedirectors`|`1`。该命令需要开启作弊。
///

## 用法

/// tab | 重载1
```mcfunction
/dialogue open <npc:target> <player:target> [sceneName:string]
```

//// html | div.result
command.dialogue.1.description

///// define
`open`：<!-- md:samp DialogueOpenAction -->

- 枚举类型。command.enum.dialogueopenaction.description单值枚举，请直接使用`open`。

`npc`：<!-- md:samp target -->

- 基本类型。command.dialogue.npc.description

`player`：<!-- md:samp target -->

- 基本类型。command.dialogue.player.description

`sceneName`：<!-- md:samp string -->

- 基本类型，可选。command.dialogue.sceneName.description


/////

////

///

/// tab | 重载2
```mcfunction
/dialogue change <npc:target> <sceneName:string> [players:target]
```

//// html | div.result
command.dialogue.2.description

///// define
`change`：<!-- md:samp DialogueChangeAction -->

- 枚举类型。command.enum.dialoguechangeaction.description单值枚举，请直接使用`change`。

`npc`：<!-- md:samp target -->

- 基本类型。command.dialogue.npc.description

`sceneName`：<!-- md:samp string -->

- 基本类型。command.dialogue.sceneName.description

`players`：<!-- md:samp target -->

- 基本类型，可选。command.dialogue.players.description


/////

////

///
