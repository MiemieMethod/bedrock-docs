# `/gamerule`

> 文档版本：1.20.80.24

`/gamerule`命令Sets or queries a game rule value.

/// settings | 执行条件
该命令需要权限等级：`gamedirectors`|`1`。
///

## 用法

/// tab | 重载1
```mcfunction
/gamerule
```

//// html | div.result
///// define

/////

////

///

/// tab | 重载2
```mcfunction
/gamerule <rule:BoolGameRule> [value:Boolean]
```

//// html | div.result
///// define
`rule`: <!-- md:samp BoolGameRule -->

- 枚举类型。枚举值如下：

|值|描述|
|---|---|
|`commandblockoutput`||
|`dodaylightcycle`||
|`doentitydrops`||
|`dofiretick`||
|`recipesunlock`||
|`dolimitedcrafting`||
|`domobloot`||
|`domobspawning`||
|`dotiledrops`||
|`doweathercycle`||
|`drowningdamage`||
|`falldamage`||
|`firedamage`||
|`keepinventory`||
|`mobgriefing`||
|`pvp`||
|`showcoordinates`||
|`naturalregeneration`||
|`tntexplodes`||
|`sendcommandfeedback`||
|`doinsomnia`||
|`commandblocksenabled`||
|`doimmediaterespawn`||
|`showdeathmessages`||
|`showtags`||
|`freezedamage`||
|`respawnblocksexplode`||
|`showbordereffect`||
|`showrecipemessages`||
|`projectilescanbreakblocks`||


`value`: <!-- md:samp Boolean -->

- 枚举类型。枚举值如下：

|值|描述|
|---|---|
|`true`||
|`false`||



/////

////

///

/// tab | 重载3
```mcfunction
/gamerule <rule:IntGameRule> [value:int]
```

//// html | div.result
///// define
`rule`: <!-- md:samp IntGameRule -->

- 枚举类型。枚举值如下：

|值|描述|
|---|---|
|`maxcommandchainlength`||
|`randomtickspeed`||
|`functioncommandlimit`||
|`spawnradius`||
|`playerssleepingpercentage`||


`value`: <!-- md:samp int -->

- 基本类型。


/////

////

///
