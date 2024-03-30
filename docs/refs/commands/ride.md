# `/ride`

> 文档版本：1.20.80.24

`/ride`命令Makes entities ride other entities, stops entities from riding, makes rides evict their riders, or summons rides or riders.

/// note | 执行条件
该命令需要权限等级：`gamedirectors`|`1`。该命令需要开启作弊。
///

## 用法

/// tab | 重载1
```mcfunction
/ride <riders:target> start_riding <ride:target> [teleportRules:TeleportRules] [howToFill:FillType]
```

//// html | div.result
///// define
`riders`: <!-- md:samp target -->

- 基本类型。

`mode`: <!-- md:samp RideModeStart -->

- 枚举类型。单值枚举，请直接使用`start_riding`。

`ride`: <!-- md:samp target -->

- 基本类型。

`teleportRules`: <!-- md:samp TeleportRules -->

- 枚举类型。枚举值如下：

|值|描述|
|---|---|
|`teleport_rider`||
|`teleport_ride`||


`howToFill`: <!-- md:samp FillType -->

- 枚举类型。枚举值如下：

|值|描述|
|---|---|
|`until_full`||
|`if_group_fits`||



/////

////

///

/// tab | 重载2
```mcfunction
/ride <riders:target> stop_riding
```

//// html | div.result
///// define
`riders`: <!-- md:samp target -->

- 基本类型。

`mode`: <!-- md:samp RideModeStop -->

- 枚举类型。单值枚举，请直接使用`stop_riding`。


/////

////

///

/// tab | 重载3
```mcfunction
/ride <rides:target> evict_riders
```

//// html | div.result
///// define
`rides`: <!-- md:samp target -->

- 基本类型。

`mode`: <!-- md:samp RideModeEvict -->

- 枚举类型。单值枚举，请直接使用`evict_riders`。


/////

////

///

/// tab | 重载4
```mcfunction
/ride <rides:target> summon_rider <entityType:EntityType> [spawnEvent:string] [nameTag:string]
```

//// html | div.result
///// define
`rides`: <!-- md:samp target -->

- 基本类型。

`mode`: <!-- md:samp RideModeSummonRider -->

- 枚举类型。单值枚举，请直接使用`summon_rider`。

`entityType`: <!-- md:samp EntityType -->

- 枚举类型。枚举值如下：

|值|描述|
|---|---|
|`minecraft:slime`||
|`slime`||
|`minecraft:tnt`||
|`tnt`||
|`minecraft:camel`||
|`camel`||
|`minecraft:turtle`||
|`turtle`||
|`minecraft:chicken`||
|`chicken`||
|`minecraft:bee`||
|`bee`||
|`minecraft:axolotl`||
|`axolotl`||
|`minecraft:breeze`||
|`breeze`||
|`minecraft:pig`||
|`pig`||
|`minecraft:hoglin`||
|`hoglin`||
|`minecraft:sniffer`||
|`sniffer`||
|`minecraft:cat`||
|`cat`||
|`minecraft:cow`||
|`cow`||
|`minecraft:sheep`||
|`sheep`||
|`minecraft:armadillo`||
|`armadillo`||
|`minecraft:wolf`||
|`wolf`||
|`minecraft:villager`||
|`villager`||
|`minecraft:wandering_trader`||
|`wandering_trader`||
|`minecraft:bogged`||
|`bogged`||
|`minecraft:mooshroom`||
|`mooshroom`||
|`minecraft:squid`||
|`squid`||
|`minecraft:glow_squid`||
|`glow_squid`||
|`minecraft:strider`||
|`strider`||
|`minecraft:rabbit`||
|`rabbit`||
|`minecraft:bat`||
|`bat`||
|`minecraft:iron_golem`||
|`iron_golem`||
|`minecraft:snow_golem`||
|`snow_golem`||
|`minecraft:ocelot`||
|`ocelot`||
|`minecraft:horse`||
|`horse`||
|`minecraft:trader_llama`||
|`trader_llama`||
|`minecraft:llama`||
|`llama`||
|`minecraft:polar_bear`||
|`polar_bear`||
|`minecraft:parrot`||
|`parrot`||
|`minecraft:dolphin`||
|`dolphin`||
|`minecraft:panda`||
|`panda`||
|`minecraft:fox`||
|`fox`||
|`minecraft:goat`||
|`goat`||
|`minecraft:frog`||
|`frog`||
|`minecraft:tadpole`||
|`tadpole`||
|`minecraft:allay`||
|`allay`||
|`minecraft:tropicalfish`||
|`tropicalfish`||
|`minecraft:cod`||
|`cod`||
|`minecraft:zombie_villager`||
|`zombie_villager`||
|`minecraft:pufferfish`||
|`pufferfish`||
|`minecraft:witch`||
|`witch`||
|`minecraft:salmon`||
|`salmon`||
|`minecraft:donkey`||
|`donkey`||
|`minecraft:mule`||
|`mule`||
|`minecraft:skeleton_horse`||
|`skeleton_horse`||
|`minecraft:zombie_horse`||
|`zombie_horse`||
|`minecraft:zombie`||
|`zombie`||
|`minecraft:drowned`||
|`drowned`||
|`minecraft:creeper`||
|`creeper`||
|`minecraft:skeleton`||
|`skeleton`||
|`minecraft:spider`||
|`spider`||
|`minecraft:zombie_pigman`||
|`zombie_pigman`||
|`minecraft:enderman`||
|`enderman`||
|`minecraft:silverfish`||
|`silverfish`||
|`minecraft:cave_spider`||
|`cave_spider`||
|`minecraft:ghast`||
|`ghast`||
|`minecraft:magma_cube`||
|`magma_cube`||
|`minecraft:blaze`||
|`blaze`||
|`minecraft:warden`||
|`warden`||
|`minecraft:stray`||
|`stray`||
|`minecraft:husk`||
|`husk`||
|`minecraft:wither_skeleton`||
|`wither_skeleton`||
|`minecraft:guardian`||
|`guardian`||
|`minecraft:elder_guardian`||
|`elder_guardian`||
|`minecraft:elder_guardian_ghost`||
|`elder_guardian_ghost`||
|`minecraft:wither`||
|`wither`||
|`minecraft:ender_dragon`||
|`ender_dragon`||
|`minecraft:shulker`||
|`shulker`||
|`minecraft:endermite`||
|`endermite`||
|`minecraft:vindicator`||
|`vindicator`||
|`minecraft:evocation_illager`||
|`evocation_illager`||
|`minecraft:vex`||
|`vex`||
|`minecraft:phantom`||
|`phantom`||
|`minecraft:pillager`||
|`pillager`||
|`minecraft:ravager`||
|`ravager`||
|`minecraft:piglin_brute`||
|`piglin_brute`||
|`minecraft:piglin`||
|`piglin`||
|`minecraft:zoglin`||
|`zoglin`||
|`minecraft:minecart`||
|`minecart`||
|`minecraft:hopper_minecart`||
|`hopper_minecart`||
|`minecraft:tnt_minecart`||
|`tnt_minecart`||
|`minecraft:chest_minecart`||
|`chest_minecart`||
|`minecraft:command_block_minecart`||
|`command_block_minecart`||
|`minecraft:xp_bottle`||
|`xp_bottle`||
|`minecraft:xp_orb`||
|`xp_orb`||
|`minecraft:ender_crystal`||
|`ender_crystal`||
|`minecraft:arrow`||
|`arrow`||
|`minecraft:snowball`||
|`snowball`||
|`minecraft:egg`||
|`egg`||
|`minecraft:splash_potion`||
|`splash_potion`||
|`minecraft:leash_knot`||
|`leash_knot`||
|`minecraft:boat`||
|`boat`||
|`minecraft:chest_boat`||
|`chest_boat`||
|`minecraft:lightning_bolt`||
|`lightning_bolt`||
|`minecraft:evocation_fang`||
|`evocation_fang`||
|`minecraft:armor_stand`||
|`armor_stand`||
|`minecraft:fireworks_rocket`||
|`fireworks_rocket`||
|`minecraft:npc`||
|`npc`||
|`editor:map_marker`||


`spawnEvent`: <!-- md:samp string -->

- 基本类型。

`nameTag`: <!-- md:samp string -->

- 基本类型。


/////

////

///

/// tab | 重载5
```mcfunction
/ride <riders:target> summon_ride <entityType:EntityType> [rideRules:RideRules] [spawnEvent:string] [nameTag:string]
```

//// html | div.result
///// define
`riders`: <!-- md:samp target -->

- 基本类型。

`mode`: <!-- md:samp RideModeSummonRide -->

- 枚举类型。单值枚举，请直接使用`summon_ride`。

`entityType`: <!-- md:samp EntityType -->

- 枚举类型。枚举值如下：

|值|描述|
|---|---|
|`minecraft:slime`||
|`slime`||
|`minecraft:tnt`||
|`tnt`||
|`minecraft:camel`||
|`camel`||
|`minecraft:turtle`||
|`turtle`||
|`minecraft:chicken`||
|`chicken`||
|`minecraft:bee`||
|`bee`||
|`minecraft:axolotl`||
|`axolotl`||
|`minecraft:breeze`||
|`breeze`||
|`minecraft:pig`||
|`pig`||
|`minecraft:hoglin`||
|`hoglin`||
|`minecraft:sniffer`||
|`sniffer`||
|`minecraft:cat`||
|`cat`||
|`minecraft:cow`||
|`cow`||
|`minecraft:sheep`||
|`sheep`||
|`minecraft:armadillo`||
|`armadillo`||
|`minecraft:wolf`||
|`wolf`||
|`minecraft:villager`||
|`villager`||
|`minecraft:wandering_trader`||
|`wandering_trader`||
|`minecraft:bogged`||
|`bogged`||
|`minecraft:mooshroom`||
|`mooshroom`||
|`minecraft:squid`||
|`squid`||
|`minecraft:glow_squid`||
|`glow_squid`||
|`minecraft:strider`||
|`strider`||
|`minecraft:rabbit`||
|`rabbit`||
|`minecraft:bat`||
|`bat`||
|`minecraft:iron_golem`||
|`iron_golem`||
|`minecraft:snow_golem`||
|`snow_golem`||
|`minecraft:ocelot`||
|`ocelot`||
|`minecraft:horse`||
|`horse`||
|`minecraft:trader_llama`||
|`trader_llama`||
|`minecraft:llama`||
|`llama`||
|`minecraft:polar_bear`||
|`polar_bear`||
|`minecraft:parrot`||
|`parrot`||
|`minecraft:dolphin`||
|`dolphin`||
|`minecraft:panda`||
|`panda`||
|`minecraft:fox`||
|`fox`||
|`minecraft:goat`||
|`goat`||
|`minecraft:frog`||
|`frog`||
|`minecraft:tadpole`||
|`tadpole`||
|`minecraft:allay`||
|`allay`||
|`minecraft:tropicalfish`||
|`tropicalfish`||
|`minecraft:cod`||
|`cod`||
|`minecraft:zombie_villager`||
|`zombie_villager`||
|`minecraft:pufferfish`||
|`pufferfish`||
|`minecraft:witch`||
|`witch`||
|`minecraft:salmon`||
|`salmon`||
|`minecraft:donkey`||
|`donkey`||
|`minecraft:mule`||
|`mule`||
|`minecraft:skeleton_horse`||
|`skeleton_horse`||
|`minecraft:zombie_horse`||
|`zombie_horse`||
|`minecraft:zombie`||
|`zombie`||
|`minecraft:drowned`||
|`drowned`||
|`minecraft:creeper`||
|`creeper`||
|`minecraft:skeleton`||
|`skeleton`||
|`minecraft:spider`||
|`spider`||
|`minecraft:zombie_pigman`||
|`zombie_pigman`||
|`minecraft:enderman`||
|`enderman`||
|`minecraft:silverfish`||
|`silverfish`||
|`minecraft:cave_spider`||
|`cave_spider`||
|`minecraft:ghast`||
|`ghast`||
|`minecraft:magma_cube`||
|`magma_cube`||
|`minecraft:blaze`||
|`blaze`||
|`minecraft:warden`||
|`warden`||
|`minecraft:stray`||
|`stray`||
|`minecraft:husk`||
|`husk`||
|`minecraft:wither_skeleton`||
|`wither_skeleton`||
|`minecraft:guardian`||
|`guardian`||
|`minecraft:elder_guardian`||
|`elder_guardian`||
|`minecraft:elder_guardian_ghost`||
|`elder_guardian_ghost`||
|`minecraft:wither`||
|`wither`||
|`minecraft:ender_dragon`||
|`ender_dragon`||
|`minecraft:shulker`||
|`shulker`||
|`minecraft:endermite`||
|`endermite`||
|`minecraft:vindicator`||
|`vindicator`||
|`minecraft:evocation_illager`||
|`evocation_illager`||
|`minecraft:vex`||
|`vex`||
|`minecraft:phantom`||
|`phantom`||
|`minecraft:pillager`||
|`pillager`||
|`minecraft:ravager`||
|`ravager`||
|`minecraft:piglin_brute`||
|`piglin_brute`||
|`minecraft:piglin`||
|`piglin`||
|`minecraft:zoglin`||
|`zoglin`||
|`minecraft:minecart`||
|`minecart`||
|`minecraft:hopper_minecart`||
|`hopper_minecart`||
|`minecraft:tnt_minecart`||
|`tnt_minecart`||
|`minecraft:chest_minecart`||
|`chest_minecart`||
|`minecraft:command_block_minecart`||
|`command_block_minecart`||
|`minecraft:xp_bottle`||
|`xp_bottle`||
|`minecraft:xp_orb`||
|`xp_orb`||
|`minecraft:ender_crystal`||
|`ender_crystal`||
|`minecraft:arrow`||
|`arrow`||
|`minecraft:snowball`||
|`snowball`||
|`minecraft:egg`||
|`egg`||
|`minecraft:splash_potion`||
|`splash_potion`||
|`minecraft:leash_knot`||
|`leash_knot`||
|`minecraft:boat`||
|`boat`||
|`minecraft:chest_boat`||
|`chest_boat`||
|`minecraft:lightning_bolt`||
|`lightning_bolt`||
|`minecraft:evocation_fang`||
|`evocation_fang`||
|`minecraft:armor_stand`||
|`armor_stand`||
|`minecraft:fireworks_rocket`||
|`fireworks_rocket`||
|`minecraft:npc`||
|`npc`||
|`editor:map_marker`||


`rideRules`: <!-- md:samp RideRules -->

- 枚举类型。枚举值如下：

|值|描述|
|---|---|
|`no_ride_change`||
|`reassign_rides`||
|`skip_riders`||


`spawnEvent`: <!-- md:samp string -->

- 基本类型。

`nameTag`: <!-- md:samp string -->

- 基本类型。


/////

////

///
