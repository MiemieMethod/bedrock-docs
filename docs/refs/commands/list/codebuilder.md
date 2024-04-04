# `/codebuilder`

> 文档版本：1.20.80.24

`/codebuilder`命令commands.codebuilder.description

/// settings | 执行条件
该命令需要权限等级：`gamedirectors`|`1`。该命令需要开启作弊。
///

## 用法

/// tab | 重载1
```mcfunction
/codebuilder navigate <player:target> <openCodeBuilderWindow:Boolean> <URL:text>
```

//// html | div.result
///// define
`navigate`：<!-- md:samp CodeBuilderNavigateAction -->

- 枚举类型。单值枚举，请直接使用`navigate`。

`player`：<!-- md:samp target -->

- 基本类型。

`openCodeBuilderWindow`：<!-- md:samp Boolean -->

- 枚举类型。枚举值如下：

  |值|描述|
  |---|---|
  |`true`||
  |`false`||


`URL`：<!-- md:samp text -->

- 基本类型。


/////

////

///

/// tab | 重载2
```mcfunction
/codebuilder reset <player:target>
```

//// html | div.result
///// define
`reset`：<!-- md:samp CodeBuilderResetAction -->

- 枚举类型。单值枚举，请直接使用`reset`。

`player`：<!-- md:samp target -->

- 基本类型。


/////

////

///

/// tab | 重载3
```mcfunction
/codebuilder subscribe scoreboard <player:target> <objective:string>
```

//// html | div.result
///// define
`subscribe`：<!-- md:samp CodeBuilderSubscribeAction -->

- 枚举类型。单值枚举，请直接使用`subscribe`。

`type`：<!-- md:samp CodeBuilderEventTypeScoreboard -->

- 枚举类型。单值枚举，请直接使用`scoreboard`。

`player`：<!-- md:samp target -->

- 基本类型。

`objective`：<!-- md:samp string -->

- 基本类型。


/////

////

///

/// tab | 重载4
```mcfunction
/codebuilder unsubscribe scoreboard <player:target> <objective:string>
```

//// html | div.result
///// define
`unsubscribe`：<!-- md:samp CodeBuilderUnsubscribeAction -->

- 枚举类型。单值枚举，请直接使用`unsubscribe`。

`type`：<!-- md:samp CodeBuilderEventTypeScoreboard -->

- 枚举类型。单值枚举，请直接使用`scoreboard`。

`player`：<!-- md:samp target -->

- 基本类型。

`objective`：<!-- md:samp string -->

- 基本类型。


/////

////

///

/// tab | 重载5
```mcfunction
/codebuilder code check code_status <status:CodeBuilderCodeStatus> <player:target>
```

//// html | div.result
///// define
`code`：<!-- md:samp CodeBuilderCodeStateCategory -->

- 枚举类型。单值枚举，请直接使用`code`。

`check`：<!-- md:samp CodeBuilderCheckAction -->

- 枚举类型。单值枚举，请直接使用`check`。

`codeStatus`：<!-- md:samp CodeBuilderCodeStatusProperty -->

- 枚举类型。单值枚举，请直接使用`code_status`。

`status`：<!-- md:samp CodeBuilderCodeStatus -->

- 枚举类型。枚举值如下：

  |值|描述|
  |---|---|
  |`not_started`||
  |`in_progress`||
  |`paused`||
  |`error`||
  |`succeeded`||


`player`：<!-- md:samp target -->

- 基本类型。


/////

////

///

/// tab | 重载6
```mcfunction
/codebuilder runtime <action:CodeBuilderRuntime> <player:target>
```

//// html | div.result
///// define
`runtime`：<!-- md:samp CodeBuilderRuntimeAction -->

- 枚举类型。单值枚举，请直接使用`runtime`。

`action`：<!-- md:samp CodeBuilderRuntime -->

- 枚举类型。枚举值如下：

  |值|描述|
  |---|---|
  |`stop`||
  |`start`||
  |`pause`||


`player`：<!-- md:samp target -->

- 基本类型。


/////

////

///
