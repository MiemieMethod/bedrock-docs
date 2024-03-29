# /changesetting

> 文档版本：1.20.80.24

`/changesetting`命令Changes a setting on the dedicated server while it's running.

/// note | 执行条件
该命令需要权限等级：`internal`|`4`。该命令需要开启作弊。
///

## 用法

/// tab | `重载1`
```mcfunction
/changesetting allow-cheats <value:Boolean>
```

//// html | div.result
///// define
`setting`: <!-- md:samp BoolSettingName -->

- 枚举类型。枚举值如下：

|值|描述|
|---|---|
|`allow-cheats`||


`value`: <!-- md:samp Boolean -->

- 枚举类型。枚举值如下：

|值|描述|
|---|---|
|`true`||
|`false`||



/////

////

///

/// tab | `重载2`
```mcfunction
/changesetting difficulty <value:Difficulty>
```

//// html | div.result
///// define
`setting`: <!-- md:samp DifficultySettingName -->

- 枚举类型。枚举值如下：

|值|描述|
|---|---|
|`difficulty`||


`value`: <!-- md:samp Difficulty -->

- 枚举类型。枚举值如下：

|值|描述|
|---|---|
|`normal`||
|`peaceful`||
|`easy`||
|`hard`||
|`p`||
|`e`||
|`n`||
|`h`||



/////

////

///

/// tab | `重载3`
```mcfunction
/changesetting difficulty <value:int>
```

//// html | div.result
///// define
`setting`: <!-- md:samp DifficultySettingName -->

- 枚举类型。枚举值如下：

|值|描述|
|---|---|
|`difficulty`||


`value`: <!-- md:samp int -->

- 基本类型。


/////

////

///
