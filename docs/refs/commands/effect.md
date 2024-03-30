# `/effect`

> 文档版本：1.20.80.24

`/effect`命令Add or remove status effects.

/// note | 执行条件
该命令需要权限等级：`gamedirectors`|`1`。该命令需要开启作弊。
///

## 用法

/// tab | 重载1
```mcfunction
/effect <player:target> clear
```

//// html | div.result
///// define
`player`: <!-- md:samp target -->

- 基本类型。

`clear`: <!-- md:samp ClearEffects -->

- 枚举类型。单值枚举，请直接使用`clear`。


/////

////

///

/// tab | 重载2
```mcfunction
/effect <player:target> <effect:Effect> [seconds:int] [amplifier:int] [hideParticles:Boolean]
```

//// html | div.result
///// define
`player`: <!-- md:samp target -->

- 基本类型。

`effect`: <!-- md:samp Effect -->

- 枚举类型。枚举值如下：

|值|描述|
|---|---|
|`wither`||
|`speed`||
|`slowness`||
|`haste`||
|`mining_fatigue`||
|`strength`||
|`instant_health`||
|`instant_damage`||
|`jump_boost`||
|`nausea`||
|`regeneration`||
|`resistance`||
|`fire_resistance`||
|`water_breathing`||
|`invisibility`||
|`blindness`||
|`night_vision`||
|`hunger`||
|`weakness`||
|`poison`||
|`health_boost`||
|`absorption`||
|`saturation`||
|`levitation`||
|`fatal_poison`||
|`conduit_power`||
|`slow_falling`||
|`bad_omen`||
|`village_hero`||
|`darkness`||


`seconds`: <!-- md:samp int -->

- 基本类型。

`amplifier`: <!-- md:samp int -->

- 基本类型。

`hideParticles`: <!-- md:samp Boolean -->

- 枚举类型。枚举值如下：

|值|描述|
|---|---|
|`true`||
|`false`||



/////

////

///
