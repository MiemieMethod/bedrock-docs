# /inputpermission

> 文档版本：1.20.80.24

`/inputpermission`命令Sets whether or not a player's input can affect their character.

/// note | 执行条件
该命令需要权限等级：`gamedirectors`|`1`。该命令需要开启作弊。
///

## 用法

/// tab | `重载1`
```mcfunction
/inputpermission set <targets:target> <permission:permission> <state:state>
```

//// html | div.result
///// define
`option`: <!-- md:samp Option_Set -->

- 枚举类型。枚举值如下：

|值|描述|
|---|---|
|`set`||


`targets`: <!-- md:samp target -->

- 基本类型。

`permission`: <!-- md:samp permission -->

- 枚举类型。枚举值如下：

|值|描述|
|---|---|
|`movement`||
|`camera`||


`state`: <!-- md:samp state -->

- 枚举类型。枚举值如下：

|值|描述|
|---|---|
|`enabled`||
|`disabled`||



/////

////

///

/// tab | `重载2`
```mcfunction
/inputpermission query <targets:target> <permission:permission> [state:state]
```

//// html | div.result
///// define
`option`: <!-- md:samp Option_Query -->

- 枚举类型。枚举值如下：

|值|描述|
|---|---|
|`query`||


`targets`: <!-- md:samp target -->

- 基本类型。

`permission`: <!-- md:samp permission -->

- 枚举类型。枚举值如下：

|值|描述|
|---|---|
|`movement`||
|`camera`||


`state`: <!-- md:samp state -->

- 枚举类型。枚举值如下：

|值|描述|
|---|---|
|`enabled`||
|`disabled`||



/////

////

///
