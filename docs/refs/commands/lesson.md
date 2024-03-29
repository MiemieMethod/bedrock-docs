# /lesson

> 文档版本：1.20.80.24

`/lesson`命令Handle Educational Lesson reporting.

/// note | 执行条件
该命令需要权限等级：`gamedirectors`|`1`。该命令需要开启作弊。
///

## 用法

/// tab | `重载1`
```mcfunction
/lesson <player:target>
```

//// html | div.result
///// define
`player`: <!-- md:samp target -->

- 基本类型。


/////

////

///

/// tab | `重载2`
```mcfunction
/lesson <player:target> lesson <action:LessonAction> [score:int]
```

//// html | div.result
///// define
`player`: <!-- md:samp target -->

- 基本类型。

`resource`: <!-- md:samp LessonType -->

- 枚举类型。枚举值如下：

|值|描述|
|---|---|
|`lesson`||


`action`: <!-- md:samp LessonAction -->

- 枚举类型。枚举值如下：

|值|描述|
|---|---|
|`complete`||
|`restart`||


`score`: <!-- md:samp int -->

- 基本类型。


/////

////

///

/// tab | `重载3`
```mcfunction
/lesson <player:target> activity <id:string> <action:LessonAction> [score:int]
```

//// html | div.result
///// define
`player`: <!-- md:samp target -->

- 基本类型。

`resource`: <!-- md:samp LessonActivityType -->

- 枚举类型。枚举值如下：

|值|描述|
|---|---|
|`activity`||


`id`: <!-- md:samp string -->

- 基本类型。

`action`: <!-- md:samp LessonAction -->

- 枚举类型。枚举值如下：

|值|描述|
|---|---|
|`complete`||
|`restart`||


`score`: <!-- md:samp int -->

- 基本类型。


/////

////

///
