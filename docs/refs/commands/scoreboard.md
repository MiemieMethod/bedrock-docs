# `/scoreboard`

> 文档版本：1.20.80.24

`/scoreboard`命令Tracks and displays scores for various objectives.

/// settings | 执行条件
该命令需要权限等级：`gamedirectors`|`1`。该命令需要开启作弊。
///

## 用法

/// tab | 重载1
```mcfunction
/scoreboard objectives add <objective:string> dummy [displayName:string]
```

//// html | div.result
///// define
`category`: <!-- md:samp ScoreboardObjectivesCategory -->

- 枚举类型。单值枚举，请直接使用`objectives`。

`action`: <!-- md:samp ScoreboardAddAction -->

- 枚举类型。单值枚举，请直接使用`add`。

`objective`: <!-- md:samp ScoreboardObjectives -->

- 软枚举类型。

`criteria`: <!-- md:samp ScoreboardCriteria -->

- 枚举类型。单值枚举，请直接使用`dummy`。

`displayName`: <!-- md:samp string -->

- 基本类型。


/////

////

///

/// tab | 重载2
```mcfunction
/scoreboard objectives remove <objective:string>
```

//// html | div.result
///// define
`category`: <!-- md:samp ScoreboardObjectivesCategory -->

- 枚举类型。单值枚举，请直接使用`objectives`。

`action`: <!-- md:samp ScoreboardRemoveAction -->

- 枚举类型。单值枚举，请直接使用`remove`。

`objective`: <!-- md:samp ScoreboardObjectives -->

- 软枚举类型。


/////

////

///

/// tab | 重载3
```mcfunction
/scoreboard objectives list
```

//// html | div.result
///// define
`category`: <!-- md:samp ScoreboardObjectivesCategory -->

- 枚举类型。单值枚举，请直接使用`objectives`。

`action`: <!-- md:samp ScoreboardListAction -->

- 枚举类型。单值枚举，请直接使用`list`。


/////

////

///

/// tab | 重载4
```mcfunction
/scoreboard objectives setdisplay <displaySlot:ScoreboardDisplaySlotSortable> [objective:string] [sortOrder:ScoreboardSortOrder]
```

//// html | div.result
///// define
`category`: <!-- md:samp ScoreboardObjectivesCategory -->

- 枚举类型。单值枚举，请直接使用`objectives`。

`action`: <!-- md:samp ScoreboardSetDisplayAction -->

- 枚举类型。单值枚举，请直接使用`setdisplay`。

`displaySlot`: <!-- md:samp ScoreboardDisplaySlotSortable -->

- 枚举类型。枚举值如下：

|值|描述|
|---|---|
|`list`||
|`sidebar`||


`objective`: <!-- md:samp ScoreboardObjectives -->

- 软枚举类型。

`sortOrder`: <!-- md:samp ScoreboardSortOrder -->

- 枚举类型。枚举值如下：

|值|描述|
|---|---|
|`ascending`||
|`descending`||



/////

////

///

/// tab | 重载5
```mcfunction
/scoreboard objectives setdisplay belowname [objective:string]
```

//// html | div.result
///// define
`category`: <!-- md:samp ScoreboardObjectivesCategory -->

- 枚举类型。单值枚举，请直接使用`objectives`。

`action`: <!-- md:samp ScoreboardSetDisplayAction -->

- 枚举类型。单值枚举，请直接使用`setdisplay`。

`displaySlot`: <!-- md:samp ScoreboardDisplaySlotNonSortable -->

- 枚举类型。单值枚举，请直接使用`belowname`。

`objective`: <!-- md:samp ScoreboardObjectives -->

- 软枚举类型。


/////

////

///

/// tab | 重载6
```mcfunction
/scoreboard players list [playername:target]
```

//// html | div.result
///// define
`category`: <!-- md:samp ScoreboardPlayersCategory -->

- 枚举类型。单值枚举，请直接使用`players`。

`action`: <!-- md:samp ScoreboardListAction -->

- 枚举类型。单值枚举，请直接使用`list`。

`playername`: <!-- md:samp target -->

- 基本类型。


/////

////

///

/// tab | 重载7
```mcfunction
/scoreboard players reset <player:target> [objective:string]
```

//// html | div.result
///// define
`category`: <!-- md:samp ScoreboardPlayersCategory -->

- 枚举类型。单值枚举，请直接使用`players`。

`action`: <!-- md:samp ScoreboardResetAction -->

- 枚举类型。单值枚举，请直接使用`reset`。

`player`: <!-- md:samp target -->

- 基本类型。

`objective`: <!-- md:samp ScoreboardObjectives -->

- 软枚举类型。


/////

////

///

/// tab | 重载8
```mcfunction
/scoreboard players test <player:target> <objective:string> <min:wildcard int> [max:wildcard int]
```

//// html | div.result
///// define
`category`: <!-- md:samp ScoreboardPlayersCategory -->

- 枚举类型。单值枚举，请直接使用`players`。

`action`: <!-- md:samp ScoreboardTestAction -->

- 枚举类型。单值枚举，请直接使用`test`。

`player`: <!-- md:samp target -->

- 基本类型。

`objective`: <!-- md:samp ScoreboardObjectives -->

- 软枚举类型。

`min`: <!-- md:samp wildcard int -->

- 基本类型。

`max`: <!-- md:samp wildcard int -->

- 基本类型。


/////

////

///

/// tab | 重载9
```mcfunction
/scoreboard players random <player:target> <objective:string> <min:int> <max:int>
```

//// html | div.result
///// define
`category`: <!-- md:samp ScoreboardPlayersCategory -->

- 枚举类型。单值枚举，请直接使用`players`。

`action`: <!-- md:samp ScoreboardRandomAction -->

- 枚举类型。单值枚举，请直接使用`random`。

`player`: <!-- md:samp target -->

- 基本类型。

`objective`: <!-- md:samp ScoreboardObjectives -->

- 软枚举类型。

`min`: <!-- md:samp int -->

- 基本类型。

`max`: <!-- md:samp int -->

- 基本类型。


/////

////

///

/// tab | 重载10
```mcfunction
/scoreboard players <action:ScoreboardPlayersNumAction> <player:target> <objective:string> <count:int>
```

//// html | div.result
///// define
`category`: <!-- md:samp ScoreboardPlayersCategory -->

- 枚举类型。单值枚举，请直接使用`players`。

`action`: <!-- md:samp ScoreboardPlayersNumAction -->

- 枚举类型。枚举值如下：

|值|描述|
|---|---|
|`set`||
|`add`||
|`remove`||


`player`: <!-- md:samp target -->

- 基本类型。

`objective`: <!-- md:samp ScoreboardObjectives -->

- 软枚举类型。

`count`: <!-- md:samp int -->

- 基本类型。


/////

////

///

/// tab | 重载11
```mcfunction
/scoreboard players operation <targetName:target> <targetObjective:string> <operation:operator> <selector:target> <objective:string>
```

//// html | div.result
///// define
`category`: <!-- md:samp ScoreboardPlayersCategory -->

- 枚举类型。单值枚举，请直接使用`players`。

`action`: <!-- md:samp ScoreboardOperationAction -->

- 枚举类型。单值枚举，请直接使用`operation`。

`targetName`: <!-- md:samp target -->

- 基本类型。

`targetObjective`: <!-- md:samp ScoreboardObjectives -->

- 软枚举类型。

`operation`: <!-- md:samp operator -->

- 基本类型。

`selector`: <!-- md:samp target -->

- 基本类型。

`objective`: <!-- md:samp ScoreboardObjectives -->

- 软枚举类型。


/////

////

///
