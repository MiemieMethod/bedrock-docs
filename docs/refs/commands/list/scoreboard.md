# `/scoreboard`

> 文档版本：1.21.50.25

`/scoreboard`命令command.scoreboard.description

/// settings | 执行条件
该命令需要权限等级：`gamedirectors`|`1`。该命令需要开启作弊。
///

## 用法

/// tab | 重载1
```mcfunction
/scoreboard objectives add <objective:string> dummy [displayName:string]
```

//// html | div.result
command.scoreboard.1.description

///// define
`category`：<!-- md:samp ScoreboardObjectivesCategory -->

- 枚举类型。command.enum.scoreboardobjectivescategory.description单值枚举，请直接使用`objectives`。

`action`：<!-- md:samp ScoreboardAddAction -->

- 枚举类型。command.enum.scoreboardaddaction.description单值枚举，请直接使用`add`。

`objective`：<!-- md:samp ScoreboardObjectives -->

- 软枚举类型。command.scoreboard.objective.description

`criteria`：<!-- md:samp ScoreboardCriteria -->

- 枚举类型。command.enum.scoreboardcriteria.description单值枚举，请直接使用`dummy`。

`displayName`：<!-- md:samp string -->

- 基本类型，可选。command.scoreboard.displayName.description


/////

////

///

/// tab | 重载2
```mcfunction
/scoreboard objectives remove <objective:string>
```

//// html | div.result
command.scoreboard.2.description

///// define
`category`：<!-- md:samp ScoreboardObjectivesCategory -->

- 枚举类型。command.enum.scoreboardobjectivescategory.description单值枚举，请直接使用`objectives`。

`action`：<!-- md:samp ScoreboardRemoveAction -->

- 枚举类型。command.enum.scoreboardremoveaction.description单值枚举，请直接使用`remove`。

`objective`：<!-- md:samp ScoreboardObjectives -->

- 软枚举类型。command.scoreboard.objective.description


/////

////

///

/// tab | 重载3
```mcfunction
/scoreboard objectives list
```

//// html | div.result
command.scoreboard.3.description

///// define
`category`：<!-- md:samp ScoreboardObjectivesCategory -->

- 枚举类型。command.enum.scoreboardobjectivescategory.description单值枚举，请直接使用`objectives`。

`action`：<!-- md:samp ScoreboardListAction -->

- 枚举类型。command.enum.scoreboardlistaction.description单值枚举，请直接使用`list`。


/////

////

///

/// tab | 重载4
```mcfunction
/scoreboard objectives setdisplay <displaySlot:ScoreboardDisplaySlotSortable> [objective:string] [sortOrder:ScoreboardSortOrder]
```

//// html | div.result
command.scoreboard.4.description

///// define
`category`：<!-- md:samp ScoreboardObjectivesCategory -->

- 枚举类型。command.enum.scoreboardobjectivescategory.description单值枚举，请直接使用`objectives`。

`action`：<!-- md:samp ScoreboardSetDisplayAction -->

- 枚举类型。command.enum.scoreboardsetdisplayaction.description单值枚举，请直接使用`setdisplay`。

`displaySlot`：<!-- md:samp ScoreboardDisplaySlotSortable -->

- 枚举类型。command.enum.scoreboarddisplayslotsortable.description枚举值如下：

  |值|描述|
  |---|---|
  |`list`|command.enum.scoreboarddisplayslotsortable.list|
  |`sidebar`|command.enum.scoreboarddisplayslotsortable.sidebar|


`objective`：<!-- md:samp ScoreboardObjectives -->

- 软枚举类型，可选。command.scoreboard.objective.description

`sortOrder`：<!-- md:samp ScoreboardSortOrder -->

- 枚举类型，可选。command.enum.scoreboardsortorder.description枚举值如下：

  |值|描述|
  |---|---|
  |`ascending`|command.enum.scoreboardsortorder.ascending|
  |`descending`|command.enum.scoreboardsortorder.descending|



/////

////

///

/// tab | 重载5
```mcfunction
/scoreboard objectives setdisplay belowname [objective:string]
```

//// html | div.result
command.scoreboard.5.description

///// define
`category`：<!-- md:samp ScoreboardObjectivesCategory -->

- 枚举类型。command.enum.scoreboardobjectivescategory.description单值枚举，请直接使用`objectives`。

`action`：<!-- md:samp ScoreboardSetDisplayAction -->

- 枚举类型。command.enum.scoreboardsetdisplayaction.description单值枚举，请直接使用`setdisplay`。

`displaySlot`：<!-- md:samp ScoreboardDisplaySlotNonSortable -->

- 枚举类型。command.enum.scoreboarddisplayslotnonsortable.description单值枚举，请直接使用`belowname`。

`objective`：<!-- md:samp ScoreboardObjectives -->

- 软枚举类型，可选。command.scoreboard.objective.description


/////

////

///

/// tab | 重载6
```mcfunction
/scoreboard players list [playername:target]
```

//// html | div.result
command.scoreboard.6.description

///// define
`category`：<!-- md:samp ScoreboardPlayersCategory -->

- 枚举类型。command.enum.scoreboardplayerscategory.description单值枚举，请直接使用`players`。

`action`：<!-- md:samp ScoreboardListAction -->

- 枚举类型。command.enum.scoreboardlistaction.description单值枚举，请直接使用`list`。

`playername`：<!-- md:samp target -->

- 基本类型，可选。command.scoreboard.playername.description


/////

////

///

/// tab | 重载7
```mcfunction
/scoreboard players reset <player:target> [objective:string]
```

//// html | div.result
command.scoreboard.7.description

///// define
`category`：<!-- md:samp ScoreboardPlayersCategory -->

- 枚举类型。command.enum.scoreboardplayerscategory.description单值枚举，请直接使用`players`。

`action`：<!-- md:samp ScoreboardResetAction -->

- 枚举类型。command.enum.scoreboardresetaction.description单值枚举，请直接使用`reset`。

`player`：<!-- md:samp target -->

- 基本类型。command.scoreboard.player.description

`objective`：<!-- md:samp ScoreboardObjectives -->

- 软枚举类型，可选。command.scoreboard.objective.description


/////

////

///

/// tab | 重载8
```mcfunction
/scoreboard players test <player:target> <objective:string> <min:wildcard int> [max:wildcard int]
```

//// html | div.result
command.scoreboard.8.description

///// define
`category`：<!-- md:samp ScoreboardPlayersCategory -->

- 枚举类型。command.enum.scoreboardplayerscategory.description单值枚举，请直接使用`players`。

`action`：<!-- md:samp ScoreboardTestAction -->

- 枚举类型。command.enum.scoreboardtestaction.description单值枚举，请直接使用`test`。

`player`：<!-- md:samp target -->

- 基本类型。command.scoreboard.player.description

`objective`：<!-- md:samp ScoreboardObjectives -->

- 软枚举类型。command.scoreboard.objective.description

`min`：<!-- md:samp wildcard int -->

- 基本类型。command.scoreboard.min.description

`max`：<!-- md:samp wildcard int -->

- 基本类型，可选。command.scoreboard.max.description


/////

////

///

/// tab | 重载9
```mcfunction
/scoreboard players random <player:target> <objective:string> <min:int> <max:int>
```

//// html | div.result
command.scoreboard.9.description

///// define
`category`：<!-- md:samp ScoreboardPlayersCategory -->

- 枚举类型。command.enum.scoreboardplayerscategory.description单值枚举，请直接使用`players`。

`action`：<!-- md:samp ScoreboardRandomAction -->

- 枚举类型。command.enum.scoreboardrandomaction.description单值枚举，请直接使用`random`。

`player`：<!-- md:samp target -->

- 基本类型。command.scoreboard.player.description

`objective`：<!-- md:samp ScoreboardObjectives -->

- 软枚举类型。command.scoreboard.objective.description

`min`：<!-- md:samp int -->

- 基本类型。command.scoreboard.min.description

`max`：<!-- md:samp int -->

- 基本类型。command.scoreboard.max.description


/////

////

///

/// tab | 重载10
```mcfunction
/scoreboard players <action:ScoreboardPlayersNumAction> <player:target> <objective:string> <count:int>
```

//// html | div.result
command.scoreboard.10.description

///// define
`category`：<!-- md:samp ScoreboardPlayersCategory -->

- 枚举类型。command.enum.scoreboardplayerscategory.description单值枚举，请直接使用`players`。

`action`：<!-- md:samp ScoreboardPlayersNumAction -->

- 枚举类型。command.enum.scoreboardplayersnumaction.description枚举值如下：

  |值|描述|
  |---|---|
  |`set`|command.enum.scoreboardplayersnumaction.set|
  |`add`|command.enum.scoreboardplayersnumaction.add|
  |`remove`|command.enum.scoreboardplayersnumaction.remove|


`player`：<!-- md:samp target -->

- 基本类型。command.scoreboard.player.description

`objective`：<!-- md:samp ScoreboardObjectives -->

- 软枚举类型。command.scoreboard.objective.description

`count`：<!-- md:samp int -->

- 基本类型。command.scoreboard.count.description


/////

////

///

/// tab | 重载11
```mcfunction
/scoreboard players operation <targetName:target> <targetObjective:string> <operation:operator> <selector:target> <objective:string>
```

//// html | div.result
command.scoreboard.11.description

///// define
`category`：<!-- md:samp ScoreboardPlayersCategory -->

- 枚举类型。command.enum.scoreboardplayerscategory.description单值枚举，请直接使用`players`。

`action`：<!-- md:samp ScoreboardOperationAction -->

- 枚举类型。command.enum.scoreboardoperationaction.description单值枚举，请直接使用`operation`。

`targetName`：<!-- md:samp target -->

- 基本类型。command.scoreboard.targetName.description

`targetObjective`：<!-- md:samp ScoreboardObjectives -->

- 软枚举类型。command.scoreboard.targetObjective.description

`operation`：<!-- md:samp operator -->

- 基本类型。command.scoreboard.operation.description

`selector`：<!-- md:samp target -->

- 基本类型。command.scoreboard.selector.description

`objective`：<!-- md:samp ScoreboardObjectives -->

- 软枚举类型。command.scoreboard.objective.description


/////

////

///
