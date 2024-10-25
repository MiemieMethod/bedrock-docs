# `/codebuilder`

> 文档版本：1.21.50.25

`/codebuilder`命令command.codebuilder.description

/// settings | 执行条件
该命令需要权限等级：`gamedirectors`|`1`。该命令需要开启作弊。
///

## 用法

/// tab | 重载1
```mcfunction
/codebuilder navigate <player:target> <openCodeBuilderWindow:Boolean> <URL:text>
```

//// html | div.result
command.codebuilder.1.description

///// define
`navigate`：<!-- md:samp CodeBuilderNavigateAction -->

- 枚举类型。command.enum.codebuildernavigateaction.description单值枚举，请直接使用`navigate`。

`player`：<!-- md:samp target -->

- 基本类型。command.codebuilder.player.description

`openCodeBuilderWindow`：<!-- md:samp Boolean -->

- 枚举类型。command.enum.boolean.description枚举值如下：

  |值|描述|
  |---|---|
  |`true`|是|
  |`false`|否|


`URL`：<!-- md:samp text -->

- 基本类型。command.codebuilder.URL.description


/////

////

///

/// tab | 重载2
```mcfunction
/codebuilder reset <player:target>
```

//// html | div.result
command.codebuilder.2.description

///// define
`reset`：<!-- md:samp CodeBuilderResetAction -->

- 枚举类型。command.enum.codebuilderresetaction.description单值枚举，请直接使用`reset`。

`player`：<!-- md:samp target -->

- 基本类型。command.codebuilder.player.description


/////

////

///

/// tab | 重载3
```mcfunction
/codebuilder subscribe scoreboard <player:target> <objective:string>
```

//// html | div.result
command.codebuilder.3.description

///// define
`subscribe`：<!-- md:samp CodeBuilderSubscribeAction -->

- 枚举类型。command.enum.codebuildersubscribeaction.description单值枚举，请直接使用`subscribe`。

`type`：<!-- md:samp CodeBuilderEventTypeScoreboard -->

- 枚举类型。command.enum.codebuildereventtypescoreboard.description单值枚举，请直接使用`scoreboard`。

`player`：<!-- md:samp target -->

- 基本类型。command.codebuilder.player.description

`objective`：<!-- md:samp string -->

- 基本类型。command.codebuilder.objective.description


/////

////

///

/// tab | 重载4
```mcfunction
/codebuilder unsubscribe scoreboard <player:target> <objective:string>
```

//// html | div.result
command.codebuilder.4.description

///// define
`unsubscribe`：<!-- md:samp CodeBuilderUnsubscribeAction -->

- 枚举类型。command.enum.codebuilderunsubscribeaction.description单值枚举，请直接使用`unsubscribe`。

`type`：<!-- md:samp CodeBuilderEventTypeScoreboard -->

- 枚举类型。command.enum.codebuildereventtypescoreboard.description单值枚举，请直接使用`scoreboard`。

`player`：<!-- md:samp target -->

- 基本类型。command.codebuilder.player.description

`objective`：<!-- md:samp string -->

- 基本类型。command.codebuilder.objective.description


/////

////

///

/// tab | 重载5
```mcfunction
/codebuilder code check code_status <status:CodeBuilderCodeStatus> <player:target>
```

//// html | div.result
command.codebuilder.5.description

///// define
`code`：<!-- md:samp CodeBuilderCodeStateCategory -->

- 枚举类型。command.enum.codebuildercodestatecategory.description单值枚举，请直接使用`code`。

`check`：<!-- md:samp CodeBuilderCheckAction -->

- 枚举类型。command.enum.codebuildercheckaction.description单值枚举，请直接使用`check`。

`codeStatus`：<!-- md:samp CodeBuilderCodeStatusProperty -->

- 枚举类型。command.enum.codebuildercodestatusproperty.description单值枚举，请直接使用`code_status`。

`status`：<!-- md:samp CodeBuilderCodeStatus -->

- 枚举类型。command.enum.codebuildercodestatus.description枚举值如下：

  |值|描述|
  |---|---|
  |`not_started`|command.enum.codebuildercodestatus.not_started|
  |`in_progress`|command.enum.codebuildercodestatus.in_progress|
  |`paused`|command.enum.codebuildercodestatus.paused|
  |`error`|command.enum.codebuildercodestatus.error|
  |`succeeded`|command.enum.codebuildercodestatus.succeeded|


`player`：<!-- md:samp target -->

- 基本类型。command.codebuilder.player.description


/////

////

///

/// tab | 重载6
```mcfunction
/codebuilder runtime <action:CodeBuilderRuntime> <player:target>
```

//// html | div.result
command.codebuilder.6.description

///// define
`runtime`：<!-- md:samp CodeBuilderRuntimeAction -->

- 枚举类型。command.enum.codebuilderruntimeaction.description单值枚举，请直接使用`runtime`。

`action`：<!-- md:samp CodeBuilderRuntime -->

- 枚举类型。command.enum.codebuilderruntime.description枚举值如下：

  |值|描述|
  |---|---|
  |`start`|command.enum.codebuilderruntime.start|
  |`stop`|command.enum.codebuilderruntime.stop|
  |`pause`|command.enum.codebuilderruntime.pause|


`player`：<!-- md:samp target -->

- 基本类型。command.codebuilder.player.description


/////

////

///
