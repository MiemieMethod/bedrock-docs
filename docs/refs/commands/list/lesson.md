# `/lesson`

> 文档版本：1.21.0.21

`/lesson`命令command.lesson.description

/// settings | 执行条件
该命令需要权限等级：`gamedirectors`|`1`。该命令需要开启作弊。
///

## 用法

/// tab | 重载1
```mcfunction
/lesson <player:target>
```

//// html | div.result
command.lesson.1.description

///// define
`player`：<!-- md:samp target -->

- 基本类型。command.lesson.player.description


/////

////

///

/// tab | 重载2
```mcfunction
/lesson <player:target> lesson <action:LessonAction> [score:int]
```

//// html | div.result
command.lesson.2.description

///// define
`player`：<!-- md:samp target -->

- 基本类型。command.lesson.player.description

`resource`：<!-- md:samp LessonType -->

- 枚举类型。command.enum.lessontype.description单值枚举，请直接使用`lesson`。

`action`：<!-- md:samp LessonAction -->

- 枚举类型。command.enum.lessonaction.description枚举值如下：

  |值|描述|
  |---|---|
  |`complete`|command.enum.lessonaction.complete|
  |`restart`|command.enum.lessonaction.restart|


`score`：<!-- md:samp int -->

- 基本类型，可选。command.lesson.score.description


/////

////

///

/// tab | 重载3
```mcfunction
/lesson <player:target> activity <id:string> <action:LessonAction> [score:int]
```

//// html | div.result
command.lesson.3.description

///// define
`player`：<!-- md:samp target -->

- 基本类型。command.lesson.player.description

`resource`：<!-- md:samp LessonActivityType -->

- 枚举类型。command.enum.lessonactivitytype.description单值枚举，请直接使用`activity`。

`id`：<!-- md:samp string -->

- 基本类型。command.lesson.id.description

`action`：<!-- md:samp LessonAction -->

- 枚举类型。command.enum.lessonaction.description枚举值如下：

  |值|描述|
  |---|---|
  |`complete`|command.enum.lessonaction.complete|
  |`restart`|command.enum.lessonaction.restart|


`score`：<!-- md:samp int -->

- 基本类型，可选。command.lesson.score.description


/////

////

///
