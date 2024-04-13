# `/locate`

> 文档版本：1.21.0.21

`/locate`命令command.locate.description

/// settings | 执行条件
该命令需要权限等级：`gamedirectors`|`1`。该命令需要开启作弊。
///

## 用法

/// tab | 重载1
```mcfunction
/locate <feature:Structure> [useNewChunksOnly:Boolean]
```

//// html | div.result
<!-- md:version command * 21 true true -->
command.locate.1.description

///// define
`feature`：<!-- md:samp Structure -->

- 枚举类型。command.enum.structure.description枚举值如下：

  |值|描述|
  |---|---|
  |`end_city`|command.enum.structure.end_city|
  |`fortress`|command.enum.structure.fortress|
  |`mineshaft`|command.enum.structure.mineshaft|
  |`monument`|command.enum.structure.monument|
  |`stronghold`|command.enum.structure.stronghold|
  |`temple`|command.enum.structure.temple|
  |`village`|command.enum.structure.village|
  |`mansion`|command.enum.structure.mansion|
  |`shipwreck`|command.enum.structure.shipwreck|
  |`buried_treasure`|command.enum.structure.buried_treasure|
  |`ruins`|command.enum.structure.ruins|
  |`pillager_outpost`|command.enum.structure.pillager_outpost|
  |`ruined_portal`|command.enum.structure.ruined_portal|
  |`bastion_remnant`|command.enum.structure.bastion_remnant|
  |`ancient_city`|command.enum.structure.ancient_city|
  |`trail_ruins`|command.enum.structure.trail_ruins|
  |`trial_chambers`|command.enum.structure.trial_chambers|
  |`ancientcity`|command.enum.structure.ancientcity|
  |`bastionremnant`|command.enum.structure.bastionremnant|
  |`buriedtreasure`|command.enum.structure.buriedtreasure|
  |`endcity`|command.enum.structure.endcity|
  |`pillageroutpost`|command.enum.structure.pillageroutpost|
  |`ruinedportal`|command.enum.structure.ruinedportal|


`useNewChunksOnly`：<!-- md:samp Boolean -->

- 枚举类型，可选。command.enum.boolean.description枚举值如下：

  |值|描述|
  |---|---|
  |`true`|是|
  |`false`|否|



/////

////

///

/// tab | 重载2
```mcfunction
/locate structure <structure:Structure> [useNewChunksOnly:Boolean]
```

//// html | div.result
<!-- md:version command 21 * true true -->
command.locate.2.description

///// define
`subcommand`：<!-- md:samp LocateSubcommandStructure -->

- 枚举类型。command.enum.locatesubcommandstructure.description单值枚举，请直接使用`structure`。

`structure`：<!-- md:samp Structure -->

- 枚举类型。command.enum.structure.description枚举值如下：

  |值|描述|
  |---|---|
  |`end_city`|command.enum.structure.end_city|
  |`fortress`|command.enum.structure.fortress|
  |`mineshaft`|command.enum.structure.mineshaft|
  |`monument`|command.enum.structure.monument|
  |`stronghold`|command.enum.structure.stronghold|
  |`temple`|command.enum.structure.temple|
  |`village`|command.enum.structure.village|
  |`mansion`|command.enum.structure.mansion|
  |`shipwreck`|command.enum.structure.shipwreck|
  |`buried_treasure`|command.enum.structure.buried_treasure|
  |`ruins`|command.enum.structure.ruins|
  |`pillager_outpost`|command.enum.structure.pillager_outpost|
  |`ruined_portal`|command.enum.structure.ruined_portal|
  |`bastion_remnant`|command.enum.structure.bastion_remnant|
  |`ancient_city`|command.enum.structure.ancient_city|
  |`trail_ruins`|command.enum.structure.trail_ruins|
  |`trial_chambers`|command.enum.structure.trial_chambers|
  |`ancientcity`|command.enum.structure.ancientcity|
  |`bastionremnant`|command.enum.structure.bastionremnant|
  |`buriedtreasure`|command.enum.structure.buriedtreasure|
  |`endcity`|command.enum.structure.endcity|
  |`pillageroutpost`|command.enum.structure.pillageroutpost|
  |`ruinedportal`|command.enum.structure.ruinedportal|


`useNewChunksOnly`：<!-- md:samp Boolean -->

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
/locate biome <biome:Biome>
```

//// html | div.result
<!-- md:version command 21 * true true -->
command.locate.3.description

///// define
`subcommand`：<!-- md:samp LocateSubcommandBiome -->

- 枚举类型。command.enum.locatesubcommandbiome.description单值枚举，请直接使用`biome`。

`biome`：<!-- md:samp Biome -->

- 枚举类型。command.enum.biome.description枚举值如下：

  |值|描述|
  |---|---|
  |`the_end`|command.enum.biome.the_end|
  |`ocean`|command.enum.biome.ocean|
  |`plains`|command.enum.biome.plains|
  |`desert`|command.enum.biome.desert|
  |`extreme_hills`|command.enum.biome.extreme_hills|
  |`forest`|command.enum.biome.forest|
  |`taiga`|command.enum.biome.taiga|
  |`swampland`|command.enum.biome.swampland|
  |`river`|command.enum.biome.river|
  |`hell`|command.enum.biome.hell|
  |`legacy_frozen_ocean`|command.enum.biome.legacy_frozen_ocean|
  |`frozen_river`|command.enum.biome.frozen_river|
  |`ice_plains`|command.enum.biome.ice_plains|
  |`ice_mountains`|command.enum.biome.ice_mountains|
  |`mushroom_island`|command.enum.biome.mushroom_island|
  |`mushroom_island_shore`|command.enum.biome.mushroom_island_shore|
  |`beach`|command.enum.biome.beach|
  |`desert_hills`|command.enum.biome.desert_hills|
  |`forest_hills`|command.enum.biome.forest_hills|
  |`taiga_hills`|command.enum.biome.taiga_hills|
  |`extreme_hills_edge`|command.enum.biome.extreme_hills_edge|
  |`jungle`|command.enum.biome.jungle|
  |`jungle_hills`|command.enum.biome.jungle_hills|
  |`jungle_edge`|command.enum.biome.jungle_edge|
  |`deep_ocean`|command.enum.biome.deep_ocean|
  |`stone_beach`|command.enum.biome.stone_beach|
  |`cold_beach`|command.enum.biome.cold_beach|
  |`birch_forest`|command.enum.biome.birch_forest|
  |`birch_forest_hills`|command.enum.biome.birch_forest_hills|
  |`roofed_forest`|command.enum.biome.roofed_forest|
  |`cold_taiga`|command.enum.biome.cold_taiga|
  |`cold_taiga_hills`|command.enum.biome.cold_taiga_hills|
  |`mega_taiga`|command.enum.biome.mega_taiga|
  |`mega_taiga_hills`|command.enum.biome.mega_taiga_hills|
  |`extreme_hills_plus_trees`|command.enum.biome.extreme_hills_plus_trees|
  |`savanna`|command.enum.biome.savanna|
  |`savanna_plateau`|command.enum.biome.savanna_plateau|
  |`mesa`|command.enum.biome.mesa|
  |`mesa_plateau_stone`|command.enum.biome.mesa_plateau_stone|
  |`mesa_plateau`|command.enum.biome.mesa_plateau|
  |`warm_ocean`|command.enum.biome.warm_ocean|
  |`lukewarm_ocean`|command.enum.biome.lukewarm_ocean|
  |`deep_lukewarm_ocean`|command.enum.biome.deep_lukewarm_ocean|
  |`cold_ocean`|command.enum.biome.cold_ocean|
  |`deep_cold_ocean`|command.enum.biome.deep_cold_ocean|
  |`frozen_ocean`|command.enum.biome.frozen_ocean|
  |`deep_frozen_ocean`|command.enum.biome.deep_frozen_ocean|
  |`bamboo_jungle`|command.enum.biome.bamboo_jungle|
  |`bamboo_jungle_hills`|command.enum.biome.bamboo_jungle_hills|
  |`sunflower_plains`|command.enum.biome.sunflower_plains|
  |`desert_mutated`|command.enum.biome.desert_mutated|
  |`extreme_hills_mutated`|command.enum.biome.extreme_hills_mutated|
  |`flower_forest`|command.enum.biome.flower_forest|
  |`taiga_mutated`|command.enum.biome.taiga_mutated|
  |`swampland_mutated`|command.enum.biome.swampland_mutated|
  |`ice_plains_spikes`|command.enum.biome.ice_plains_spikes|
  |`jungle_mutated`|command.enum.biome.jungle_mutated|
  |`jungle_edge_mutated`|command.enum.biome.jungle_edge_mutated|
  |`birch_forest_mutated`|command.enum.biome.birch_forest_mutated|
  |`birch_forest_hills_mutated`|command.enum.biome.birch_forest_hills_mutated|
  |`roofed_forest_mutated`|command.enum.biome.roofed_forest_mutated|
  |`cold_taiga_mutated`|command.enum.biome.cold_taiga_mutated|
  |`redwood_taiga_mutated`|command.enum.biome.redwood_taiga_mutated|
  |`redwood_taiga_hills_mutated`|command.enum.biome.redwood_taiga_hills_mutated|
  |`extreme_hills_plus_trees_mutated`|command.enum.biome.extreme_hills_plus_trees_mutated|
  |`savanna_mutated`|command.enum.biome.savanna_mutated|
  |`savanna_plateau_mutated`|command.enum.biome.savanna_plateau_mutated|
  |`mesa_bryce`|command.enum.biome.mesa_bryce|
  |`mesa_plateau_stone_mutated`|command.enum.biome.mesa_plateau_stone_mutated|
  |`mesa_plateau_mutated`|command.enum.biome.mesa_plateau_mutated|
  |`soulsand_valley`|command.enum.biome.soulsand_valley|
  |`crimson_forest`|command.enum.biome.crimson_forest|
  |`warped_forest`|command.enum.biome.warped_forest|
  |`basalt_deltas`|command.enum.biome.basalt_deltas|
  |`jagged_peaks`|command.enum.biome.jagged_peaks|
  |`frozen_peaks`|command.enum.biome.frozen_peaks|
  |`snowy_slopes`|command.enum.biome.snowy_slopes|
  |`grove`|command.enum.biome.grove|
  |`meadow`|command.enum.biome.meadow|
  |`lush_caves`|command.enum.biome.lush_caves|
  |`dripstone_caves`|command.enum.biome.dripstone_caves|
  |`stony_peaks`|command.enum.biome.stony_peaks|
  |`deep_dark`|command.enum.biome.deep_dark|
  |`mangrove_swamp`|command.enum.biome.mangrove_swamp|
  |`cherry_grove`|command.enum.biome.cherry_grove|



/////

////

///
