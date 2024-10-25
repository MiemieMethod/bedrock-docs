# `/effect`

> 文档版本：1.21.50.25

`/effect`命令command.effect.description

/// settings | 执行条件
该命令需要权限等级：`gamedirectors`|`1`。该命令需要开启作弊。
///

## 用法

/// tab | 重载1
```mcfunction
/effect <player:target> clear [effect:Effect]
```

//// html | div.result
command.effect.1.description

///// define
`player`：<!-- md:samp target -->

- 基本类型。command.effect.player.description

`Mode`：<!-- md:samp ClearEffects -->

- 枚举类型。command.enum.cleareffects.description单值枚举，请直接使用`clear`。

`effect`：<!-- md:samp Effect -->

- 枚举类型，可选。command.enum.effect.description枚举值如下：

  |值|描述|
  |---|---|
  |`wither`|command.enum.effect.wither|
  |`speed`|command.enum.effect.speed|
  |`slowness`|command.enum.effect.slowness|
  |`haste`|command.enum.effect.haste|
  |`mining_fatigue`|command.enum.effect.mining_fatigue|
  |`strength`|command.enum.effect.strength|
  |`instant_health`|command.enum.effect.instant_health|
  |`instant_damage`|command.enum.effect.instant_damage|
  |`jump_boost`|command.enum.effect.jump_boost|
  |`nausea`|command.enum.effect.nausea|
  |`regeneration`|command.enum.effect.regeneration|
  |`resistance`|command.enum.effect.resistance|
  |`fire_resistance`|command.enum.effect.fire_resistance|
  |`water_breathing`|command.enum.effect.water_breathing|
  |`invisibility`|command.enum.effect.invisibility|
  |`blindness`|command.enum.effect.blindness|
  |`night_vision`|command.enum.effect.night_vision|
  |`hunger`|command.enum.effect.hunger|
  |`weakness`|command.enum.effect.weakness|
  |`poison`|command.enum.effect.poison|
  |`health_boost`|command.enum.effect.health_boost|
  |`absorption`|command.enum.effect.absorption|
  |`saturation`|command.enum.effect.saturation|
  |`levitation`|command.enum.effect.levitation|
  |`fatal_poison`|command.enum.effect.fatal_poison|
  |`conduit_power`|command.enum.effect.conduit_power|
  |`slow_falling`|command.enum.effect.slow_falling|
  |`bad_omen`|command.enum.effect.bad_omen|
  |`village_hero`|command.enum.effect.village_hero|
  |`darkness`|command.enum.effect.darkness|
  |`trial_omen`|command.enum.effect.trial_omen|
  |`wind_charged`|command.enum.effect.wind_charged|
  |`weaving`|command.enum.effect.weaving|
  |`oozing`|command.enum.effect.oozing|
  |`infested`|command.enum.effect.infested|
  |`raid_omen`|command.enum.effect.raid_omen|



/////

////

///

/// tab | 重载2
```mcfunction
/effect <player:target> <effect:Effect> [seconds:int] [amplifier:int] [hideParticles:Boolean]
```

//// html | div.result
command.effect.2.description

///// define
`player`：<!-- md:samp target -->

- 基本类型。command.effect.player.description

`effect`：<!-- md:samp Effect -->

- 枚举类型。command.enum.effect.description枚举值如下：

  |值|描述|
  |---|---|
  |`wither`|command.enum.effect.wither|
  |`speed`|command.enum.effect.speed|
  |`slowness`|command.enum.effect.slowness|
  |`haste`|command.enum.effect.haste|
  |`mining_fatigue`|command.enum.effect.mining_fatigue|
  |`strength`|command.enum.effect.strength|
  |`instant_health`|command.enum.effect.instant_health|
  |`instant_damage`|command.enum.effect.instant_damage|
  |`jump_boost`|command.enum.effect.jump_boost|
  |`nausea`|command.enum.effect.nausea|
  |`regeneration`|command.enum.effect.regeneration|
  |`resistance`|command.enum.effect.resistance|
  |`fire_resistance`|command.enum.effect.fire_resistance|
  |`water_breathing`|command.enum.effect.water_breathing|
  |`invisibility`|command.enum.effect.invisibility|
  |`blindness`|command.enum.effect.blindness|
  |`night_vision`|command.enum.effect.night_vision|
  |`hunger`|command.enum.effect.hunger|
  |`weakness`|command.enum.effect.weakness|
  |`poison`|command.enum.effect.poison|
  |`health_boost`|command.enum.effect.health_boost|
  |`absorption`|command.enum.effect.absorption|
  |`saturation`|command.enum.effect.saturation|
  |`levitation`|command.enum.effect.levitation|
  |`fatal_poison`|command.enum.effect.fatal_poison|
  |`conduit_power`|command.enum.effect.conduit_power|
  |`slow_falling`|command.enum.effect.slow_falling|
  |`bad_omen`|command.enum.effect.bad_omen|
  |`village_hero`|command.enum.effect.village_hero|
  |`darkness`|command.enum.effect.darkness|
  |`trial_omen`|command.enum.effect.trial_omen|
  |`wind_charged`|command.enum.effect.wind_charged|
  |`weaving`|command.enum.effect.weaving|
  |`oozing`|command.enum.effect.oozing|
  |`infested`|command.enum.effect.infested|
  |`raid_omen`|command.enum.effect.raid_omen|


`seconds`：<!-- md:samp int -->

- 基本类型，可选。command.effect.seconds.description

`amplifier`：<!-- md:samp int -->

- 基本类型，可选。command.effect.amplifier.description

`hideParticles`：<!-- md:samp Boolean -->

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
/effect <player:target> <effect:Effect> infinite [amplifier:int] [hideParticles:Boolean]
```

//// html | div.result
command.effect.3.description

///// define
`player`：<!-- md:samp target -->

- 基本类型。command.effect.player.description

`effect`：<!-- md:samp Effect -->

- 枚举类型。command.enum.effect.description枚举值如下：

  |值|描述|
  |---|---|
  |`wither`|command.enum.effect.wither|
  |`speed`|command.enum.effect.speed|
  |`slowness`|command.enum.effect.slowness|
  |`haste`|command.enum.effect.haste|
  |`mining_fatigue`|command.enum.effect.mining_fatigue|
  |`strength`|command.enum.effect.strength|
  |`instant_health`|command.enum.effect.instant_health|
  |`instant_damage`|command.enum.effect.instant_damage|
  |`jump_boost`|command.enum.effect.jump_boost|
  |`nausea`|command.enum.effect.nausea|
  |`regeneration`|command.enum.effect.regeneration|
  |`resistance`|command.enum.effect.resistance|
  |`fire_resistance`|command.enum.effect.fire_resistance|
  |`water_breathing`|command.enum.effect.water_breathing|
  |`invisibility`|command.enum.effect.invisibility|
  |`blindness`|command.enum.effect.blindness|
  |`night_vision`|command.enum.effect.night_vision|
  |`hunger`|command.enum.effect.hunger|
  |`weakness`|command.enum.effect.weakness|
  |`poison`|command.enum.effect.poison|
  |`health_boost`|command.enum.effect.health_boost|
  |`absorption`|command.enum.effect.absorption|
  |`saturation`|command.enum.effect.saturation|
  |`levitation`|command.enum.effect.levitation|
  |`fatal_poison`|command.enum.effect.fatal_poison|
  |`conduit_power`|command.enum.effect.conduit_power|
  |`slow_falling`|command.enum.effect.slow_falling|
  |`bad_omen`|command.enum.effect.bad_omen|
  |`village_hero`|command.enum.effect.village_hero|
  |`darkness`|command.enum.effect.darkness|
  |`trial_omen`|command.enum.effect.trial_omen|
  |`wind_charged`|command.enum.effect.wind_charged|
  |`weaving`|command.enum.effect.weaving|
  |`oozing`|command.enum.effect.oozing|
  |`infested`|command.enum.effect.infested|
  |`raid_omen`|command.enum.effect.raid_omen|


`Mode`：<!-- md:samp AddInfiniteEffect -->

- 枚举类型。command.enum.addinfiniteeffect.description单值枚举，请直接使用`infinite`。

`amplifier`：<!-- md:samp int -->

- 基本类型，可选。command.effect.amplifier.description

`hideParticles`：<!-- md:samp Boolean -->

- 枚举类型，可选。command.enum.boolean.description枚举值如下：

  |值|描述|
  |---|---|
  |`true`|是|
  |`false`|否|



/////

////

///
