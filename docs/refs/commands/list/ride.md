# `/ride`

> 文档版本：1.21.0.24

`/ride`命令command.ride.description

/// settings | 执行条件
该命令需要权限等级：`gamedirectors`|`1`。该命令需要开启作弊。
///

## 用法

/// tab | 重载1
```mcfunction
/ride <riders:target> start_riding <ride:target> [teleportRules:TeleportRules] [howToFill:FillType]
```

//// html | div.result
command.ride.1.description

///// define
`riders`：<!-- md:samp target -->

- 基本类型。command.ride.riders.description

`mode`：<!-- md:samp RideModeStart -->

- 枚举类型。command.enum.ridemodestart.description单值枚举，请直接使用`start_riding`。

`ride`：<!-- md:samp target -->

- 基本类型。command.ride.ride.description

`teleportRules`：<!-- md:samp TeleportRules -->

- 枚举类型，可选。command.enum.teleportrules.description枚举值如下：

  |值|描述|
  |---|---|
  |`teleport_rider`|command.enum.teleportrules.teleport_rider|
  |`teleport_ride`|command.enum.teleportrules.teleport_ride|


`howToFill`：<!-- md:samp FillType -->

- 枚举类型，可选。command.enum.filltype.description枚举值如下：

  |值|描述|
  |---|---|
  |`until_full`|command.enum.filltype.until_full|
  |`if_group_fits`|command.enum.filltype.if_group_fits|



/////

////

///

/// tab | 重载2
```mcfunction
/ride <riders:target> stop_riding
```

//// html | div.result
command.ride.2.description

///// define
`riders`：<!-- md:samp target -->

- 基本类型。command.ride.riders.description

`mode`：<!-- md:samp RideModeStop -->

- 枚举类型。command.enum.ridemodestop.description单值枚举，请直接使用`stop_riding`。


/////

////

///

/// tab | 重载3
```mcfunction
/ride <rides:target> evict_riders
```

//// html | div.result
command.ride.3.description

///// define
`rides`：<!-- md:samp target -->

- 基本类型。command.ride.rides.description

`mode`：<!-- md:samp RideModeEvict -->

- 枚举类型。command.enum.ridemodeevict.description单值枚举，请直接使用`evict_riders`。


/////

////

///

/// tab | 重载4
```mcfunction
/ride <rides:target> summon_rider <entityType:EntityType> [spawnEvent:string] [nameTag:string]
```

//// html | div.result
command.ride.4.description

///// define
`rides`：<!-- md:samp target -->

- 基本类型。command.ride.rides.description

`mode`：<!-- md:samp RideModeSummonRider -->

- 枚举类型。command.enum.ridemodesummonrider.description单值枚举，请直接使用`summon_rider`。

`entityType`：<!-- md:samp EntityType -->

- 枚举类型。command.enum.entitytype.description枚举值如下：

  |值|描述|
  |---|---|
  |`minecraft:slime`|command.enum.entitytype.minecraft:slime|
  |`slime`|command.enum.entitytype.slime|
  |`minecraft:tnt`|command.enum.entitytype.minecraft:tnt|
  |`tnt`|command.enum.entitytype.tnt|
  |`minecraft:camel`|command.enum.entitytype.minecraft:camel|
  |`camel`|command.enum.entitytype.camel|
  |`minecraft:turtle`|command.enum.entitytype.minecraft:turtle|
  |`turtle`|command.enum.entitytype.turtle|
  |`minecraft:chicken`|command.enum.entitytype.minecraft:chicken|
  |`chicken`|command.enum.entitytype.chicken|
  |`minecraft:bee`|command.enum.entitytype.minecraft:bee|
  |`bee`|command.enum.entitytype.bee|
  |`minecraft:axolotl`|command.enum.entitytype.minecraft:axolotl|
  |`axolotl`|command.enum.entitytype.axolotl|
  |`minecraft:breeze`|command.enum.entitytype.minecraft:breeze|
  |`breeze`|command.enum.entitytype.breeze|
  |`minecraft:pig`|command.enum.entitytype.minecraft:pig|
  |`pig`|command.enum.entitytype.pig|
  |`minecraft:hoglin`|command.enum.entitytype.minecraft:hoglin|
  |`hoglin`|command.enum.entitytype.hoglin|
  |`minecraft:sniffer`|command.enum.entitytype.minecraft:sniffer|
  |`sniffer`|command.enum.entitytype.sniffer|
  |`minecraft:cat`|command.enum.entitytype.minecraft:cat|
  |`cat`|command.enum.entitytype.cat|
  |`minecraft:cow`|command.enum.entitytype.minecraft:cow|
  |`cow`|command.enum.entitytype.cow|
  |`minecraft:sheep`|command.enum.entitytype.minecraft:sheep|
  |`sheep`|command.enum.entitytype.sheep|
  |`minecraft:armadillo`|command.enum.entitytype.minecraft:armadillo|
  |`armadillo`|command.enum.entitytype.armadillo|
  |`minecraft:wolf`|command.enum.entitytype.minecraft:wolf|
  |`wolf`|command.enum.entitytype.wolf|
  |`minecraft:villager`|command.enum.entitytype.minecraft:villager|
  |`villager`|command.enum.entitytype.villager|
  |`minecraft:wandering_trader`|command.enum.entitytype.minecraft:wandering_trader|
  |`wandering_trader`|command.enum.entitytype.wandering_trader|
  |`minecraft:bogged`|command.enum.entitytype.minecraft:bogged|
  |`bogged`|command.enum.entitytype.bogged|
  |`minecraft:mooshroom`|command.enum.entitytype.minecraft:mooshroom|
  |`mooshroom`|command.enum.entitytype.mooshroom|
  |`minecraft:squid`|command.enum.entitytype.minecraft:squid|
  |`squid`|command.enum.entitytype.squid|
  |`minecraft:glow_squid`|command.enum.entitytype.minecraft:glow_squid|
  |`glow_squid`|command.enum.entitytype.glow_squid|
  |`minecraft:strider`|command.enum.entitytype.minecraft:strider|
  |`strider`|command.enum.entitytype.strider|
  |`minecraft:rabbit`|command.enum.entitytype.minecraft:rabbit|
  |`rabbit`|command.enum.entitytype.rabbit|
  |`minecraft:bat`|command.enum.entitytype.minecraft:bat|
  |`bat`|command.enum.entitytype.bat|
  |`minecraft:iron_golem`|command.enum.entitytype.minecraft:iron_golem|
  |`iron_golem`|command.enum.entitytype.iron_golem|
  |`minecraft:snow_golem`|command.enum.entitytype.minecraft:snow_golem|
  |`snow_golem`|command.enum.entitytype.snow_golem|
  |`minecraft:ocelot`|command.enum.entitytype.minecraft:ocelot|
  |`ocelot`|command.enum.entitytype.ocelot|
  |`minecraft:horse`|command.enum.entitytype.minecraft:horse|
  |`horse`|command.enum.entitytype.horse|
  |`minecraft:trader_llama`|command.enum.entitytype.minecraft:trader_llama|
  |`trader_llama`|command.enum.entitytype.trader_llama|
  |`minecraft:llama`|command.enum.entitytype.minecraft:llama|
  |`llama`|command.enum.entitytype.llama|
  |`minecraft:polar_bear`|command.enum.entitytype.minecraft:polar_bear|
  |`polar_bear`|command.enum.entitytype.polar_bear|
  |`minecraft:parrot`|command.enum.entitytype.minecraft:parrot|
  |`parrot`|command.enum.entitytype.parrot|
  |`minecraft:dolphin`|command.enum.entitytype.minecraft:dolphin|
  |`dolphin`|command.enum.entitytype.dolphin|
  |`minecraft:panda`|command.enum.entitytype.minecraft:panda|
  |`panda`|command.enum.entitytype.panda|
  |`minecraft:fox`|command.enum.entitytype.minecraft:fox|
  |`fox`|command.enum.entitytype.fox|
  |`minecraft:goat`|command.enum.entitytype.minecraft:goat|
  |`goat`|command.enum.entitytype.goat|
  |`minecraft:frog`|command.enum.entitytype.minecraft:frog|
  |`frog`|command.enum.entitytype.frog|
  |`minecraft:tadpole`|command.enum.entitytype.minecraft:tadpole|
  |`tadpole`|command.enum.entitytype.tadpole|
  |`minecraft:allay`|command.enum.entitytype.minecraft:allay|
  |`allay`|command.enum.entitytype.allay|
  |`minecraft:tropicalfish`|command.enum.entitytype.minecraft:tropicalfish|
  |`tropicalfish`|command.enum.entitytype.tropicalfish|
  |`minecraft:cod`|command.enum.entitytype.minecraft:cod|
  |`cod`|command.enum.entitytype.cod|
  |`minecraft:zombie_villager`|command.enum.entitytype.minecraft:zombie_villager|
  |`zombie_villager`|command.enum.entitytype.zombie_villager|
  |`minecraft:pufferfish`|command.enum.entitytype.minecraft:pufferfish|
  |`pufferfish`|command.enum.entitytype.pufferfish|
  |`minecraft:witch`|command.enum.entitytype.minecraft:witch|
  |`witch`|command.enum.entitytype.witch|
  |`minecraft:salmon`|command.enum.entitytype.minecraft:salmon|
  |`salmon`|command.enum.entitytype.salmon|
  |`minecraft:donkey`|command.enum.entitytype.minecraft:donkey|
  |`donkey`|command.enum.entitytype.donkey|
  |`minecraft:mule`|command.enum.entitytype.minecraft:mule|
  |`mule`|command.enum.entitytype.mule|
  |`minecraft:skeleton_horse`|command.enum.entitytype.minecraft:skeleton_horse|
  |`skeleton_horse`|command.enum.entitytype.skeleton_horse|
  |`minecraft:zombie_horse`|command.enum.entitytype.minecraft:zombie_horse|
  |`zombie_horse`|command.enum.entitytype.zombie_horse|
  |`minecraft:zombie`|command.enum.entitytype.minecraft:zombie|
  |`zombie`|command.enum.entitytype.zombie|
  |`minecraft:drowned`|command.enum.entitytype.minecraft:drowned|
  |`drowned`|command.enum.entitytype.drowned|
  |`minecraft:creeper`|command.enum.entitytype.minecraft:creeper|
  |`creeper`|command.enum.entitytype.creeper|
  |`minecraft:skeleton`|command.enum.entitytype.minecraft:skeleton|
  |`skeleton`|command.enum.entitytype.skeleton|
  |`minecraft:spider`|command.enum.entitytype.minecraft:spider|
  |`spider`|command.enum.entitytype.spider|
  |`minecraft:zombie_pigman`|command.enum.entitytype.minecraft:zombie_pigman|
  |`zombie_pigman`|command.enum.entitytype.zombie_pigman|
  |`minecraft:enderman`|command.enum.entitytype.minecraft:enderman|
  |`enderman`|command.enum.entitytype.enderman|
  |`minecraft:silverfish`|command.enum.entitytype.minecraft:silverfish|
  |`silverfish`|command.enum.entitytype.silverfish|
  |`minecraft:cave_spider`|command.enum.entitytype.minecraft:cave_spider|
  |`cave_spider`|command.enum.entitytype.cave_spider|
  |`minecraft:ghast`|command.enum.entitytype.minecraft:ghast|
  |`ghast`|command.enum.entitytype.ghast|
  |`minecraft:magma_cube`|command.enum.entitytype.minecraft:magma_cube|
  |`magma_cube`|command.enum.entitytype.magma_cube|
  |`minecraft:blaze`|command.enum.entitytype.minecraft:blaze|
  |`blaze`|command.enum.entitytype.blaze|
  |`minecraft:warden`|command.enum.entitytype.minecraft:warden|
  |`warden`|command.enum.entitytype.warden|
  |`minecraft:stray`|command.enum.entitytype.minecraft:stray|
  |`stray`|command.enum.entitytype.stray|
  |`minecraft:husk`|command.enum.entitytype.minecraft:husk|
  |`husk`|command.enum.entitytype.husk|
  |`minecraft:wither_skeleton`|command.enum.entitytype.minecraft:wither_skeleton|
  |`wither_skeleton`|command.enum.entitytype.wither_skeleton|
  |`minecraft:guardian`|command.enum.entitytype.minecraft:guardian|
  |`guardian`|command.enum.entitytype.guardian|
  |`minecraft:elder_guardian`|command.enum.entitytype.minecraft:elder_guardian|
  |`elder_guardian`|command.enum.entitytype.elder_guardian|
  |`minecraft:elder_guardian_ghost`|command.enum.entitytype.minecraft:elder_guardian_ghost|
  |`elder_guardian_ghost`|command.enum.entitytype.elder_guardian_ghost|
  |`minecraft:wither`|command.enum.entitytype.minecraft:wither|
  |`wither`|command.enum.entitytype.wither|
  |`minecraft:ender_dragon`|command.enum.entitytype.minecraft:ender_dragon|
  |`ender_dragon`|command.enum.entitytype.ender_dragon|
  |`minecraft:shulker`|command.enum.entitytype.minecraft:shulker|
  |`shulker`|command.enum.entitytype.shulker|
  |`minecraft:endermite`|command.enum.entitytype.minecraft:endermite|
  |`endermite`|command.enum.entitytype.endermite|
  |`minecraft:vindicator`|command.enum.entitytype.minecraft:vindicator|
  |`vindicator`|command.enum.entitytype.vindicator|
  |`minecraft:evocation_illager`|command.enum.entitytype.minecraft:evocation_illager|
  |`evocation_illager`|command.enum.entitytype.evocation_illager|
  |`minecraft:vex`|command.enum.entitytype.minecraft:vex|
  |`vex`|command.enum.entitytype.vex|
  |`minecraft:phantom`|command.enum.entitytype.minecraft:phantom|
  |`phantom`|command.enum.entitytype.phantom|
  |`minecraft:pillager`|command.enum.entitytype.minecraft:pillager|
  |`pillager`|command.enum.entitytype.pillager|
  |`minecraft:ravager`|command.enum.entitytype.minecraft:ravager|
  |`ravager`|command.enum.entitytype.ravager|
  |`minecraft:piglin_brute`|command.enum.entitytype.minecraft:piglin_brute|
  |`piglin_brute`|command.enum.entitytype.piglin_brute|
  |`minecraft:piglin`|command.enum.entitytype.minecraft:piglin|
  |`piglin`|command.enum.entitytype.piglin|
  |`minecraft:zoglin`|command.enum.entitytype.minecraft:zoglin|
  |`zoglin`|command.enum.entitytype.zoglin|
  |`minecraft:minecart`|command.enum.entitytype.minecraft:minecart|
  |`minecart`|command.enum.entitytype.minecart|
  |`minecraft:hopper_minecart`|command.enum.entitytype.minecraft:hopper_minecart|
  |`hopper_minecart`|command.enum.entitytype.hopper_minecart|
  |`minecraft:tnt_minecart`|command.enum.entitytype.minecraft:tnt_minecart|
  |`tnt_minecart`|command.enum.entitytype.tnt_minecart|
  |`minecraft:chest_minecart`|command.enum.entitytype.minecraft:chest_minecart|
  |`chest_minecart`|command.enum.entitytype.chest_minecart|
  |`minecraft:command_block_minecart`|command.enum.entitytype.minecraft:command_block_minecart|
  |`command_block_minecart`|command.enum.entitytype.command_block_minecart|
  |`minecraft:xp_bottle`|command.enum.entitytype.minecraft:xp_bottle|
  |`xp_bottle`|command.enum.entitytype.xp_bottle|
  |`minecraft:xp_orb`|command.enum.entitytype.minecraft:xp_orb|
  |`xp_orb`|command.enum.entitytype.xp_orb|
  |`minecraft:ender_crystal`|command.enum.entitytype.minecraft:ender_crystal|
  |`ender_crystal`|command.enum.entitytype.ender_crystal|
  |`minecraft:arrow`|command.enum.entitytype.minecraft:arrow|
  |`arrow`|command.enum.entitytype.arrow|
  |`minecraft:snowball`|command.enum.entitytype.minecraft:snowball|
  |`snowball`|command.enum.entitytype.snowball|
  |`minecraft:egg`|command.enum.entitytype.minecraft:egg|
  |`egg`|command.enum.entitytype.egg|
  |`minecraft:splash_potion`|command.enum.entitytype.minecraft:splash_potion|
  |`splash_potion`|command.enum.entitytype.splash_potion|
  |`minecraft:leash_knot`|command.enum.entitytype.minecraft:leash_knot|
  |`leash_knot`|command.enum.entitytype.leash_knot|
  |`minecraft:boat`|command.enum.entitytype.minecraft:boat|
  |`boat`|command.enum.entitytype.boat|
  |`minecraft:chest_boat`|command.enum.entitytype.minecraft:chest_boat|
  |`chest_boat`|command.enum.entitytype.chest_boat|
  |`minecraft:lightning_bolt`|command.enum.entitytype.minecraft:lightning_bolt|
  |`lightning_bolt`|command.enum.entitytype.lightning_bolt|
  |`minecraft:evocation_fang`|command.enum.entitytype.minecraft:evocation_fang|
  |`evocation_fang`|command.enum.entitytype.evocation_fang|
  |`minecraft:armor_stand`|command.enum.entitytype.minecraft:armor_stand|
  |`armor_stand`|command.enum.entitytype.armor_stand|
  |`minecraft:fireworks_rocket`|command.enum.entitytype.minecraft:fireworks_rocket|
  |`fireworks_rocket`|command.enum.entitytype.fireworks_rocket|
  |`minecraft:npc`|command.enum.entitytype.minecraft:npc|
  |`npc`|command.enum.entitytype.npc|
  |`editor:map_marker`|command.enum.entitytype.editor:map_marker|


`spawnEvent`：<!-- md:samp string -->

- 基本类型，可选。command.ride.spawnEvent.description

`nameTag`：<!-- md:samp string -->

- 基本类型，可选。command.ride.nameTag.description


/////

////

///

/// tab | 重载5
```mcfunction
/ride <riders:target> summon_ride <entityType:EntityType> [rideRules:RideRules] [spawnEvent:string] [nameTag:string]
```

//// html | div.result
command.ride.5.description

///// define
`riders`：<!-- md:samp target -->

- 基本类型。command.ride.riders.description

`mode`：<!-- md:samp RideModeSummonRide -->

- 枚举类型。command.enum.ridemodesummonride.description单值枚举，请直接使用`summon_ride`。

`entityType`：<!-- md:samp EntityType -->

- 枚举类型。command.enum.entitytype.description枚举值如下：

  |值|描述|
  |---|---|
  |`minecraft:slime`|command.enum.entitytype.minecraft:slime|
  |`slime`|command.enum.entitytype.slime|
  |`minecraft:tnt`|command.enum.entitytype.minecraft:tnt|
  |`tnt`|command.enum.entitytype.tnt|
  |`minecraft:camel`|command.enum.entitytype.minecraft:camel|
  |`camel`|command.enum.entitytype.camel|
  |`minecraft:turtle`|command.enum.entitytype.minecraft:turtle|
  |`turtle`|command.enum.entitytype.turtle|
  |`minecraft:chicken`|command.enum.entitytype.minecraft:chicken|
  |`chicken`|command.enum.entitytype.chicken|
  |`minecraft:bee`|command.enum.entitytype.minecraft:bee|
  |`bee`|command.enum.entitytype.bee|
  |`minecraft:axolotl`|command.enum.entitytype.minecraft:axolotl|
  |`axolotl`|command.enum.entitytype.axolotl|
  |`minecraft:breeze`|command.enum.entitytype.minecraft:breeze|
  |`breeze`|command.enum.entitytype.breeze|
  |`minecraft:pig`|command.enum.entitytype.minecraft:pig|
  |`pig`|command.enum.entitytype.pig|
  |`minecraft:hoglin`|command.enum.entitytype.minecraft:hoglin|
  |`hoglin`|command.enum.entitytype.hoglin|
  |`minecraft:sniffer`|command.enum.entitytype.minecraft:sniffer|
  |`sniffer`|command.enum.entitytype.sniffer|
  |`minecraft:cat`|command.enum.entitytype.minecraft:cat|
  |`cat`|command.enum.entitytype.cat|
  |`minecraft:cow`|command.enum.entitytype.minecraft:cow|
  |`cow`|command.enum.entitytype.cow|
  |`minecraft:sheep`|command.enum.entitytype.minecraft:sheep|
  |`sheep`|command.enum.entitytype.sheep|
  |`minecraft:armadillo`|command.enum.entitytype.minecraft:armadillo|
  |`armadillo`|command.enum.entitytype.armadillo|
  |`minecraft:wolf`|command.enum.entitytype.minecraft:wolf|
  |`wolf`|command.enum.entitytype.wolf|
  |`minecraft:villager`|command.enum.entitytype.minecraft:villager|
  |`villager`|command.enum.entitytype.villager|
  |`minecraft:wandering_trader`|command.enum.entitytype.minecraft:wandering_trader|
  |`wandering_trader`|command.enum.entitytype.wandering_trader|
  |`minecraft:bogged`|command.enum.entitytype.minecraft:bogged|
  |`bogged`|command.enum.entitytype.bogged|
  |`minecraft:mooshroom`|command.enum.entitytype.minecraft:mooshroom|
  |`mooshroom`|command.enum.entitytype.mooshroom|
  |`minecraft:squid`|command.enum.entitytype.minecraft:squid|
  |`squid`|command.enum.entitytype.squid|
  |`minecraft:glow_squid`|command.enum.entitytype.minecraft:glow_squid|
  |`glow_squid`|command.enum.entitytype.glow_squid|
  |`minecraft:strider`|command.enum.entitytype.minecraft:strider|
  |`strider`|command.enum.entitytype.strider|
  |`minecraft:rabbit`|command.enum.entitytype.minecraft:rabbit|
  |`rabbit`|command.enum.entitytype.rabbit|
  |`minecraft:bat`|command.enum.entitytype.minecraft:bat|
  |`bat`|command.enum.entitytype.bat|
  |`minecraft:iron_golem`|command.enum.entitytype.minecraft:iron_golem|
  |`iron_golem`|command.enum.entitytype.iron_golem|
  |`minecraft:snow_golem`|command.enum.entitytype.minecraft:snow_golem|
  |`snow_golem`|command.enum.entitytype.snow_golem|
  |`minecraft:ocelot`|command.enum.entitytype.minecraft:ocelot|
  |`ocelot`|command.enum.entitytype.ocelot|
  |`minecraft:horse`|command.enum.entitytype.minecraft:horse|
  |`horse`|command.enum.entitytype.horse|
  |`minecraft:trader_llama`|command.enum.entitytype.minecraft:trader_llama|
  |`trader_llama`|command.enum.entitytype.trader_llama|
  |`minecraft:llama`|command.enum.entitytype.minecraft:llama|
  |`llama`|command.enum.entitytype.llama|
  |`minecraft:polar_bear`|command.enum.entitytype.minecraft:polar_bear|
  |`polar_bear`|command.enum.entitytype.polar_bear|
  |`minecraft:parrot`|command.enum.entitytype.minecraft:parrot|
  |`parrot`|command.enum.entitytype.parrot|
  |`minecraft:dolphin`|command.enum.entitytype.minecraft:dolphin|
  |`dolphin`|command.enum.entitytype.dolphin|
  |`minecraft:panda`|command.enum.entitytype.minecraft:panda|
  |`panda`|command.enum.entitytype.panda|
  |`minecraft:fox`|command.enum.entitytype.minecraft:fox|
  |`fox`|command.enum.entitytype.fox|
  |`minecraft:goat`|command.enum.entitytype.minecraft:goat|
  |`goat`|command.enum.entitytype.goat|
  |`minecraft:frog`|command.enum.entitytype.minecraft:frog|
  |`frog`|command.enum.entitytype.frog|
  |`minecraft:tadpole`|command.enum.entitytype.minecraft:tadpole|
  |`tadpole`|command.enum.entitytype.tadpole|
  |`minecraft:allay`|command.enum.entitytype.minecraft:allay|
  |`allay`|command.enum.entitytype.allay|
  |`minecraft:tropicalfish`|command.enum.entitytype.minecraft:tropicalfish|
  |`tropicalfish`|command.enum.entitytype.tropicalfish|
  |`minecraft:cod`|command.enum.entitytype.minecraft:cod|
  |`cod`|command.enum.entitytype.cod|
  |`minecraft:zombie_villager`|command.enum.entitytype.minecraft:zombie_villager|
  |`zombie_villager`|command.enum.entitytype.zombie_villager|
  |`minecraft:pufferfish`|command.enum.entitytype.minecraft:pufferfish|
  |`pufferfish`|command.enum.entitytype.pufferfish|
  |`minecraft:witch`|command.enum.entitytype.minecraft:witch|
  |`witch`|command.enum.entitytype.witch|
  |`minecraft:salmon`|command.enum.entitytype.minecraft:salmon|
  |`salmon`|command.enum.entitytype.salmon|
  |`minecraft:donkey`|command.enum.entitytype.minecraft:donkey|
  |`donkey`|command.enum.entitytype.donkey|
  |`minecraft:mule`|command.enum.entitytype.minecraft:mule|
  |`mule`|command.enum.entitytype.mule|
  |`minecraft:skeleton_horse`|command.enum.entitytype.minecraft:skeleton_horse|
  |`skeleton_horse`|command.enum.entitytype.skeleton_horse|
  |`minecraft:zombie_horse`|command.enum.entitytype.minecraft:zombie_horse|
  |`zombie_horse`|command.enum.entitytype.zombie_horse|
  |`minecraft:zombie`|command.enum.entitytype.minecraft:zombie|
  |`zombie`|command.enum.entitytype.zombie|
  |`minecraft:drowned`|command.enum.entitytype.minecraft:drowned|
  |`drowned`|command.enum.entitytype.drowned|
  |`minecraft:creeper`|command.enum.entitytype.minecraft:creeper|
  |`creeper`|command.enum.entitytype.creeper|
  |`minecraft:skeleton`|command.enum.entitytype.minecraft:skeleton|
  |`skeleton`|command.enum.entitytype.skeleton|
  |`minecraft:spider`|command.enum.entitytype.minecraft:spider|
  |`spider`|command.enum.entitytype.spider|
  |`minecraft:zombie_pigman`|command.enum.entitytype.minecraft:zombie_pigman|
  |`zombie_pigman`|command.enum.entitytype.zombie_pigman|
  |`minecraft:enderman`|command.enum.entitytype.minecraft:enderman|
  |`enderman`|command.enum.entitytype.enderman|
  |`minecraft:silverfish`|command.enum.entitytype.minecraft:silverfish|
  |`silverfish`|command.enum.entitytype.silverfish|
  |`minecraft:cave_spider`|command.enum.entitytype.minecraft:cave_spider|
  |`cave_spider`|command.enum.entitytype.cave_spider|
  |`minecraft:ghast`|command.enum.entitytype.minecraft:ghast|
  |`ghast`|command.enum.entitytype.ghast|
  |`minecraft:magma_cube`|command.enum.entitytype.minecraft:magma_cube|
  |`magma_cube`|command.enum.entitytype.magma_cube|
  |`minecraft:blaze`|command.enum.entitytype.minecraft:blaze|
  |`blaze`|command.enum.entitytype.blaze|
  |`minecraft:warden`|command.enum.entitytype.minecraft:warden|
  |`warden`|command.enum.entitytype.warden|
  |`minecraft:stray`|command.enum.entitytype.minecraft:stray|
  |`stray`|command.enum.entitytype.stray|
  |`minecraft:husk`|command.enum.entitytype.minecraft:husk|
  |`husk`|command.enum.entitytype.husk|
  |`minecraft:wither_skeleton`|command.enum.entitytype.minecraft:wither_skeleton|
  |`wither_skeleton`|command.enum.entitytype.wither_skeleton|
  |`minecraft:guardian`|command.enum.entitytype.minecraft:guardian|
  |`guardian`|command.enum.entitytype.guardian|
  |`minecraft:elder_guardian`|command.enum.entitytype.minecraft:elder_guardian|
  |`elder_guardian`|command.enum.entitytype.elder_guardian|
  |`minecraft:elder_guardian_ghost`|command.enum.entitytype.minecraft:elder_guardian_ghost|
  |`elder_guardian_ghost`|command.enum.entitytype.elder_guardian_ghost|
  |`minecraft:wither`|command.enum.entitytype.minecraft:wither|
  |`wither`|command.enum.entitytype.wither|
  |`minecraft:ender_dragon`|command.enum.entitytype.minecraft:ender_dragon|
  |`ender_dragon`|command.enum.entitytype.ender_dragon|
  |`minecraft:shulker`|command.enum.entitytype.minecraft:shulker|
  |`shulker`|command.enum.entitytype.shulker|
  |`minecraft:endermite`|command.enum.entitytype.minecraft:endermite|
  |`endermite`|command.enum.entitytype.endermite|
  |`minecraft:vindicator`|command.enum.entitytype.minecraft:vindicator|
  |`vindicator`|command.enum.entitytype.vindicator|
  |`minecraft:evocation_illager`|command.enum.entitytype.minecraft:evocation_illager|
  |`evocation_illager`|command.enum.entitytype.evocation_illager|
  |`minecraft:vex`|command.enum.entitytype.minecraft:vex|
  |`vex`|command.enum.entitytype.vex|
  |`minecraft:phantom`|command.enum.entitytype.minecraft:phantom|
  |`phantom`|command.enum.entitytype.phantom|
  |`minecraft:pillager`|command.enum.entitytype.minecraft:pillager|
  |`pillager`|command.enum.entitytype.pillager|
  |`minecraft:ravager`|command.enum.entitytype.minecraft:ravager|
  |`ravager`|command.enum.entitytype.ravager|
  |`minecraft:piglin_brute`|command.enum.entitytype.minecraft:piglin_brute|
  |`piglin_brute`|command.enum.entitytype.piglin_brute|
  |`minecraft:piglin`|command.enum.entitytype.minecraft:piglin|
  |`piglin`|command.enum.entitytype.piglin|
  |`minecraft:zoglin`|command.enum.entitytype.minecraft:zoglin|
  |`zoglin`|command.enum.entitytype.zoglin|
  |`minecraft:minecart`|command.enum.entitytype.minecraft:minecart|
  |`minecart`|command.enum.entitytype.minecart|
  |`minecraft:hopper_minecart`|command.enum.entitytype.minecraft:hopper_minecart|
  |`hopper_minecart`|command.enum.entitytype.hopper_minecart|
  |`minecraft:tnt_minecart`|command.enum.entitytype.minecraft:tnt_minecart|
  |`tnt_minecart`|command.enum.entitytype.tnt_minecart|
  |`minecraft:chest_minecart`|command.enum.entitytype.minecraft:chest_minecart|
  |`chest_minecart`|command.enum.entitytype.chest_minecart|
  |`minecraft:command_block_minecart`|command.enum.entitytype.minecraft:command_block_minecart|
  |`command_block_minecart`|command.enum.entitytype.command_block_minecart|
  |`minecraft:xp_bottle`|command.enum.entitytype.minecraft:xp_bottle|
  |`xp_bottle`|command.enum.entitytype.xp_bottle|
  |`minecraft:xp_orb`|command.enum.entitytype.minecraft:xp_orb|
  |`xp_orb`|command.enum.entitytype.xp_orb|
  |`minecraft:ender_crystal`|command.enum.entitytype.minecraft:ender_crystal|
  |`ender_crystal`|command.enum.entitytype.ender_crystal|
  |`minecraft:arrow`|command.enum.entitytype.minecraft:arrow|
  |`arrow`|command.enum.entitytype.arrow|
  |`minecraft:snowball`|command.enum.entitytype.minecraft:snowball|
  |`snowball`|command.enum.entitytype.snowball|
  |`minecraft:egg`|command.enum.entitytype.minecraft:egg|
  |`egg`|command.enum.entitytype.egg|
  |`minecraft:splash_potion`|command.enum.entitytype.minecraft:splash_potion|
  |`splash_potion`|command.enum.entitytype.splash_potion|
  |`minecraft:leash_knot`|command.enum.entitytype.minecraft:leash_knot|
  |`leash_knot`|command.enum.entitytype.leash_knot|
  |`minecraft:boat`|command.enum.entitytype.minecraft:boat|
  |`boat`|command.enum.entitytype.boat|
  |`minecraft:chest_boat`|command.enum.entitytype.minecraft:chest_boat|
  |`chest_boat`|command.enum.entitytype.chest_boat|
  |`minecraft:lightning_bolt`|command.enum.entitytype.minecraft:lightning_bolt|
  |`lightning_bolt`|command.enum.entitytype.lightning_bolt|
  |`minecraft:evocation_fang`|command.enum.entitytype.minecraft:evocation_fang|
  |`evocation_fang`|command.enum.entitytype.evocation_fang|
  |`minecraft:armor_stand`|command.enum.entitytype.minecraft:armor_stand|
  |`armor_stand`|command.enum.entitytype.armor_stand|
  |`minecraft:fireworks_rocket`|command.enum.entitytype.minecraft:fireworks_rocket|
  |`fireworks_rocket`|command.enum.entitytype.fireworks_rocket|
  |`minecraft:npc`|command.enum.entitytype.minecraft:npc|
  |`npc`|command.enum.entitytype.npc|
  |`editor:map_marker`|command.enum.entitytype.editor:map_marker|


`rideRules`：<!-- md:samp RideRules -->

- 枚举类型，可选。command.enum.riderules.description枚举值如下：

  |值|描述|
  |---|---|
  |`no_ride_change`|command.enum.riderules.no_ride_change|
  |`reassign_rides`|command.enum.riderules.reassign_rides|
  |`skip_riders`|command.enum.riderules.skip_riders|


`spawnEvent`：<!-- md:samp string -->

- 基本类型，可选。command.ride.spawnEvent.description

`nameTag`：<!-- md:samp string -->

- 基本类型，可选。command.ride.nameTag.description


/////

////

///
