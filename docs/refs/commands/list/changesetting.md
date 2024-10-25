# `/changesetting`

> 文档版本：1.21.50.25

`/changesetting`命令command.changesetting.description

/// settings | 执行条件
该命令需要权限等级：`owner`|`4`。该命令需要开启作弊。
///

## 用法

/// tab | 重载1
```mcfunction
/changesetting allow-cheats <value:Boolean>
```

//// html | div.result
command.changesetting.1.description

///// define
`setting`：<!-- md:samp BoolSettingName -->

- 枚举类型。command.enum.boolsettingname.description单值枚举，请直接使用`allow-cheats`。

`value`：<!-- md:samp Boolean -->

- 枚举类型。command.enum.boolean.description枚举值如下：

  |值|描述|
  |---|---|
  |`true`|是|
  |`false`|否|



/////

////

///

/// tab | 重载2
```mcfunction
/changesetting difficulty <value:Difficulty>
```

//// html | div.result
command.changesetting.2.description

///// define
`setting`：<!-- md:samp DifficultySettingName -->

- 枚举类型。command.enum.difficultysettingname.description单值枚举，请直接使用`difficulty`。

`value`：<!-- md:samp Difficulty -->

- 枚举类型。command.enum.difficulty.description枚举值如下：

  |值|描述|
  |---|---|
  |`normal`|command.enum.difficulty.normal|
  |`peaceful`|command.enum.difficulty.peaceful|
  |`easy`|command.enum.difficulty.easy|
  |`hard`|command.enum.difficulty.hard|
  |`p`|command.enum.difficulty.p|
  |`e`|command.enum.difficulty.e|
  |`n`|command.enum.difficulty.n|
  |`h`|command.enum.difficulty.h|



/////

////

///

/// tab | 重载3
```mcfunction
/changesetting difficulty <value:int>
```

//// html | div.result
command.changesetting.3.description

///// define
`setting`：<!-- md:samp DifficultySettingName -->

- 枚举类型。command.enum.difficultysettingname.description单值枚举，请直接使用`difficulty`。

`value`：<!-- md:samp int -->

- 基本类型。command.changesetting.value.description


/////

////

///
