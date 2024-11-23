# `/gamerule`

> 文档版本：1.21.60.21

`/gamerule`命令command.gamerule.description

/// settings | 执行条件
该命令需要权限等级：`gamedirectors`|`1`。
///

## 用法

/// tab | 重载1
```mcfunction
/gamerule
```

//// html | div.result
command.gamerule.1.description

///// define

/////

////

///

/// tab | 重载2
```mcfunction
/gamerule <rule:BoolGameRule> [value:Boolean]
```

//// html | div.result
command.gamerule.2.description

///// define
`rule`：<!-- md:samp BoolGameRule -->

- 枚举类型。command.enum.boolgamerule.description枚举值如下：

  |值|描述|
  |---|---|
  |`commandblockoutput`|command.enum.boolgamerule.commandblockoutput|
  |`dodaylightcycle`|command.enum.boolgamerule.dodaylightcycle|
  |`doentitydrops`|command.enum.boolgamerule.doentitydrops|
  |`dofiretick`|command.enum.boolgamerule.dofiretick|
  |`recipesunlock`|command.enum.boolgamerule.recipesunlock|
  |`dolimitedcrafting`|command.enum.boolgamerule.dolimitedcrafting|
  |`domobloot`|command.enum.boolgamerule.domobloot|
  |`domobspawning`|command.enum.boolgamerule.domobspawning|
  |`dotiledrops`|command.enum.boolgamerule.dotiledrops|
  |`doweathercycle`|command.enum.boolgamerule.doweathercycle|
  |`drowningdamage`|command.enum.boolgamerule.drowningdamage|
  |`falldamage`|command.enum.boolgamerule.falldamage|
  |`firedamage`|command.enum.boolgamerule.firedamage|
  |`keepinventory`|command.enum.boolgamerule.keepinventory|
  |`mobgriefing`|command.enum.boolgamerule.mobgriefing|
  |`pvp`|command.enum.boolgamerule.pvp|
  |`showcoordinates`|command.enum.boolgamerule.showcoordinates|
  |`showdaysplayed`|command.enum.boolgamerule.showdaysplayed|
  |`naturalregeneration`|command.enum.boolgamerule.naturalregeneration|
  |`tntexplodes`|command.enum.boolgamerule.tntexplodes|
  |`sendcommandfeedback`|command.enum.boolgamerule.sendcommandfeedback|
  |`doinsomnia`|command.enum.boolgamerule.doinsomnia|
  |`commandblocksenabled`|command.enum.boolgamerule.commandblocksenabled|
  |`doimmediaterespawn`|command.enum.boolgamerule.doimmediaterespawn|
  |`showdeathmessages`|command.enum.boolgamerule.showdeathmessages|
  |`showtags`|command.enum.boolgamerule.showtags|
  |`freezedamage`|command.enum.boolgamerule.freezedamage|
  |`respawnblocksexplode`|command.enum.boolgamerule.respawnblocksexplode|
  |`showbordereffect`|command.enum.boolgamerule.showbordereffect|
  |`showrecipemessages`|command.enum.boolgamerule.showrecipemessages|
  |`projectilescanbreakblocks`|command.enum.boolgamerule.projectilescanbreakblocks|
  |`tntexplosiondropdecay`|command.enum.boolgamerule.tntexplosiondropdecay|


`value`：<!-- md:samp Boolean -->

- 枚举类型，可选。command.enum.boolean.description枚举值如下：

  |值|描述|
  |---|---|
  |`true`|是|
  |`false`|否|



/////

////

///

/// tab | 重载3
```mcfunction
/gamerule <rule:IntGameRule> [value:int]
```

//// html | div.result
command.gamerule.3.description

///// define
`rule`：<!-- md:samp IntGameRule -->

- 枚举类型。command.enum.intgamerule.description枚举值如下：

  |值|描述|
  |---|---|
  |`maxcommandchainlength`|command.enum.intgamerule.maxcommandchainlength|
  |`randomtickspeed`|command.enum.intgamerule.randomtickspeed|
  |`functioncommandlimit`|command.enum.intgamerule.functioncommandlimit|
  |`spawnradius`|command.enum.intgamerule.spawnradius|
  |`playerssleepingpercentage`|command.enum.intgamerule.playerssleepingpercentage|


`value`：<!-- md:samp int -->

- 基本类型，可选。command.gamerule.value.description


/////

////

///
