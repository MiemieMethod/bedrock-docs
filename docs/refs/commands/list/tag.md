# `/tag`

> 文档版本：1.21.50.25

`/tag`命令command.tag.description

/// settings | 执行条件
该命令需要权限等级：`gamedirectors`|`1`。该命令需要开启作弊。
///

## 用法

/// tab | 重载1
```mcfunction
/tag <entity:target> <action:TagChangeAction> <name:string>
```

//// html | div.result
command.tag.1.description

///// define
`entity`：<!-- md:samp target -->

- 基本类型。command.tag.entity.description

`action`：<!-- md:samp TagChangeAction -->

- 枚举类型。command.enum.tagchangeaction.description枚举值如下：

  |值|描述|
  |---|---|
  |`add`|command.enum.tagchangeaction.add|
  |`remove`|command.enum.tagchangeaction.remove|


`name`：<!-- md:samp TagValues -->

- 软枚举类型。command.tag.name.description


/////

////

///

/// tab | 重载2
```mcfunction
/tag <entity:target> list
```

//// html | div.result
command.tag.2.description

///// define
`entity`：<!-- md:samp target -->

- 基本类型。command.tag.entity.description

`action`：<!-- md:samp TagListAction -->

- 枚举类型。command.enum.taglistaction.description单值枚举，请直接使用`list`。


/////

////

///
