# `/locate`

> 文档版本：1.20.80.24

`/locate`命令Displays the coordinates for the closest structure or biome of a given type.

/// settings | 执行条件
该命令需要权限等级：`gamedirectors`|`1`。该命令需要开启作弊。
///

## 用法

/// tab | 重载1
```mcfunction
/locate <feature:Structure> [useNewChunksOnly:Boolean]
```

//// html | div.result
<!-- md:versionrange * 21 true true -->
///// define
`feature`: <!-- md:samp Structure -->

- 枚举类型。枚举值如下：

|值|描述|
|---|---|
|`end_city`||
|`fortress`||
|`mineshaft`||
|`monument`||
|`stronghold`||
|`temple`||
|`village`||
|`mansion`||
|`shipwreck`||
|`buried_treasure`||
|`ruins`||
|`pillager_outpost`||
|`ruined_portal`||
|`bastion_remnant`||
|`ancient_city`||
|`trail_ruins`||
|`trial_chambers`||
|`ancientcity`||
|`bastionremnant`||
|`buriedtreasure`||
|`endcity`||
|`pillageroutpost`||
|`ruinedportal`||


`useNewChunksOnly`: <!-- md:samp Boolean -->

- 枚举类型。枚举值如下：

|值|描述|
|---|---|
|`true`||
|`false`||



/////

////

///

/// tab | 重载2
```mcfunction
/locate structure <structure:Structure> [useNewChunksOnly:Boolean]
```

//// html | div.result
<!-- md:versionrange 21 * true true -->
///// define
`subcommand`: <!-- md:samp LocateSubcommandStructure -->

- 枚举类型。单值枚举，请直接使用`structure`。

`structure`: <!-- md:samp Structure -->

- 枚举类型。枚举值如下：

|值|描述|
|---|---|
|`end_city`||
|`fortress`||
|`mineshaft`||
|`monument`||
|`stronghold`||
|`temple`||
|`village`||
|`mansion`||
|`shipwreck`||
|`buried_treasure`||
|`ruins`||
|`pillager_outpost`||
|`ruined_portal`||
|`bastion_remnant`||
|`ancient_city`||
|`trail_ruins`||
|`trial_chambers`||
|`ancientcity`||
|`bastionremnant`||
|`buriedtreasure`||
|`endcity`||
|`pillageroutpost`||
|`ruinedportal`||


`useNewChunksOnly`: <!-- md:samp Boolean -->

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
/locate biome <biome:Biome>
```

//// html | div.result
<!-- md:versionrange 21 * true true -->
///// define
`subcommand`: <!-- md:samp LocateSubcommandBiome -->

- 枚举类型。单值枚举，请直接使用`biome`。

`biome`: <!-- md:samp Biome -->

- 枚举类型。枚举值如下：

|值|描述|
|---|---|
|`the_end`||
|`ocean`||
|`plains`||
|`desert`||
|`extreme_hills`||
|`forest`||
|`taiga`||
|`swampland`||
|`river`||
|`hell`||
|`legacy_frozen_ocean`||
|`frozen_river`||
|`ice_plains`||
|`ice_mountains`||
|`mushroom_island`||
|`mushroom_island_shore`||
|`beach`||
|`desert_hills`||
|`forest_hills`||
|`taiga_hills`||
|`extreme_hills_edge`||
|`jungle`||
|`jungle_hills`||
|`jungle_edge`||
|`deep_ocean`||
|`stone_beach`||
|`cold_beach`||
|`birch_forest`||
|`birch_forest_hills`||
|`roofed_forest`||
|`cold_taiga`||
|`cold_taiga_hills`||
|`mega_taiga`||
|`mega_taiga_hills`||
|`extreme_hills_plus_trees`||
|`savanna`||
|`savanna_plateau`||
|`mesa`||
|`mesa_plateau_stone`||
|`mesa_plateau`||
|`warm_ocean`||
|`lukewarm_ocean`||
|`deep_lukewarm_ocean`||
|`cold_ocean`||
|`deep_cold_ocean`||
|`frozen_ocean`||
|`deep_frozen_ocean`||
|`bamboo_jungle`||
|`bamboo_jungle_hills`||
|`sunflower_plains`||
|`desert_mutated`||
|`extreme_hills_mutated`||
|`flower_forest`||
|`taiga_mutated`||
|`swampland_mutated`||
|`ice_plains_spikes`||
|`jungle_mutated`||
|`jungle_edge_mutated`||
|`birch_forest_mutated`||
|`birch_forest_hills_mutated`||
|`roofed_forest_mutated`||
|`cold_taiga_mutated`||
|`redwood_taiga_mutated`||
|`redwood_taiga_hills_mutated`||
|`extreme_hills_plus_trees_mutated`||
|`savanna_mutated`||
|`savanna_plateau_mutated`||
|`mesa_bryce`||
|`mesa_plateau_stone_mutated`||
|`mesa_plateau_mutated`||
|`soulsand_valley`||
|`crimson_forest`||
|`warped_forest`||
|`basalt_deltas`||
|`jagged_peaks`||
|`frozen_peaks`||
|`snowy_slopes`||
|`grove`||
|`meadow`||
|`lush_caves`||
|`dripstone_caves`||
|`stony_peaks`||
|`deep_dark`||
|`mangrove_swamp`||
|`cherry_grove`||



/////

////

///
