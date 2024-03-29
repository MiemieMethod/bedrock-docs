# `/tag`

> 文档版本：1.20.80.24

`/tag`命令Manages tags stored in entities.

/// note | 执行条件
该命令需要权限等级：`gamedirectors`|`1`。该命令需要开启作弊。
///

## 用法

/// tab | `重载1`
```mcfunction
/tag <entity:target> <action:TagChangeAction> <name:TagValues>
```

//// html | div.result
///// define
`entity`: <!-- md:samp target -->

- 基本类型。

`action`: <!-- md:samp TagChangeAction -->

- 枚举类型。枚举值如下：

|值|描述|
|---|---|
|`add`||
|`remove`||


`name`: <!-- md:samp TagValues -->

- 基本类型。


/////

////

///

/// tab | `重载2`
```mcfunction
/tag <entity:target> list
```

//// html | div.result
///// define
`entity`: <!-- md:samp target -->

- 基本类型。

`action`: <!-- md:samp TagListAction -->

- 枚举类型。枚举值如下：

|值|描述|
|---|---|
|`list`||



/////

////

///
