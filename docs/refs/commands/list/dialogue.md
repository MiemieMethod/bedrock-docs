# `/dialogue`

> 文档版本：1.20.80.24

`/dialogue`命令Opens NPC dialogue for a player.

/// settings | 执行条件
该命令需要权限等级：`gamedirectors`|`1`。该命令需要开启作弊。
///

## 用法

/// tab | 重载1
```mcfunction
/dialogue open <npc:target> <player:target> [sceneName:string]
```

//// html | div.result
///// define
`open`: <!-- md:samp DialogueOpenAction -->

- 枚举类型。单值枚举，请直接使用`open`。

`npc`: <!-- md:samp target -->

- 基本类型。

`player`: <!-- md:samp target -->

- 基本类型。

`sceneName`: <!-- md:samp string -->

- 基本类型。


/////

////

///

/// tab | 重载2
```mcfunction
/dialogue change <npc:target> <sceneName:string> [players:target]
```

//// html | div.result
///// define
`change`: <!-- md:samp DialogueChangeAction -->

- 枚举类型。单值枚举，请直接使用`change`。

`npc`: <!-- md:samp target -->

- 基本类型。

`sceneName`: <!-- md:samp string -->

- 基本类型。

`players`: <!-- md:samp target -->

- 基本类型。


/////

////

///
