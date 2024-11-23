# `/ability`

> 文档版本：1.21.60.21

`/ability`命令可以设置一个玩家的能力。

/// settings | 执行条件
该命令需要权限等级：`gamedirectors`|`1`。该命令需要开启作弊。
///

## 用法

/// tab | 重载1
```mcfunction
/ability <player:target> <ability:Ability> <value:Boolean>
```

//// html | div.result
授予或撤回目标玩家的某一项能力。

///// define
`player`：<!-- md:samp target -->

- 基本类型。目标玩家的目标选择器。

`ability`：<!-- md:samp Ability -->

- 枚举类型。一项能力。枚举值如下：

  |值|描述|
  |---|---|
  |`mayfly`|能够飞行|
  |`mute`|禁言|
  |`worldbuilder`|世界建造者|


`value`：<!-- md:samp Boolean -->

- 枚举类型。授予能力（是）还是撤回能力（否）。枚举值如下：

  |值|描述|
  |---|---|
  |`true`|是|
  |`false`|否|



/////

////

///

/// tab | 重载2
```mcfunction
/ability <player:target> [ability:Ability]
```

//// html | div.result
查询目标玩家的能力。

///// define
`player`：<!-- md:samp target -->

- 基本类型。目标玩家的目标选择器。

`ability`：<!-- md:samp Ability -->

- 枚举类型，可选。一项能力。枚举值如下：

  |值|描述|
  |---|---|
  |`mayfly`|能够飞行|
  |`mute`|禁言|
  |`worldbuilder`|世界建造者|



/////

////

///
