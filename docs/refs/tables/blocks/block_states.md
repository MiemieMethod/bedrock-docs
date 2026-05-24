# 原版方块状态

本页列出Microsoft Learn“Intrinsic Block States”参考中公开的原版方块状态名称、值类型、有效值和关联原版方块。该表适用于命令、方块置换条件、方块萃取启用状态以及旧内容迁移时核对方块状态名称。

/// warning | 适用范围
原版方块状态由游戏引擎定义。并非所有状态都适合由自定义方块直接声明；自定义方块应优先使用自己的命名空间，或通过[方块萃取](../../addon/block-trait.md)启用官方允许复用的状态。
///

| 方块状态 | 类型 | 有效值 | 关联原版方块（官方名称） |
| --- | --- | --- | --- |
| `active` | 布尔值 | `true`、`false` | `sculk shrieker` |
| `age` | 整数 | `0-15` | `fire`<br/>`cactus`<br/>`reeds`<br/>`nether wart block`<br/>`chorus flower`<br/>`frosted ice`<br/>`soul fire` |
| `age_bit` | 布尔值 | `true`、`false` | `sapling`<br/>`bamboo sapling` |
| `allow_underwater_bit` | 布尔值 | `true`、`false` | 未列出 |
| `attached_bit` | 布尔值 | `true`、`false` | `trip wire block`<br/>`trip wire hook` |
| `attachment` | 字符串 | `standing`、`hanging`、`side`、`multiple` | `bell`<br/>`grindstone` |
| `bamboo_leaf_size` | 字符串 | `no_leaves`、`small_leaves`、`large_leaves` | `bamboo` |
| `bamboo_stalk_thickness` | 字符串 | `thin`、`thick` | `bamboo` |
| `big_dripleaf_tilt` | 字符串 | `none`、`unstable`、`partial_tilt`、`full_tilt` | `big dripleaf` |
| `bite_counter` | 整数 | `0-6` | `cake` |
| `block_face` | 字符串 | `down`、`up`、`north`、`south`、`east`、`west` | 未列出 |
| `block_light_level` | 整数 | `0-15` | `light block` |
| `brewing_stand_slot_a_bit` | 布尔值 | `true`、`false` | `brewing stand` |
| `brewing_stand_slot_b_bit` | 布尔值 | `true`、`false` | `brewing stand` |
| `brewing_stand_slot_c_bit` | 布尔值 | `true`、`false` | `brewing stand` |
| `button_pressed_bit` | 布尔值 | `true`、`false` | `acacia button`<br/>`birch button`<br/>`crimson button`<br/>`dark oak button`<br/>`jungle button`<br/>`mangrove button`<br/>`polished blackstone button`<br/>`spruce button`<br/>`stone button`<br/>`warped button`<br/>`wood button` |
| `candles` | 整数 | `0-3` | `black candle`<br/>`blue candle`<br/>`brown candle`<br/>`candle`<br/>`cyan candle`<br/>`gray candle`<br/>`green candle`<br/>`light blue candle`<br/>`light gray candle`<br/>`lime candle`<br/>`magenta candle`<br/>`orange candle`<br/>`pink candle`<br/>`purple candle`<br/>`red candle`<br/>`white candle`<br/>`yellow candle` |
| `cardinal_direction` | 字符串 | `north`、`south`、`east`、`west` | 未列出 |
| `cauldron_liquid` | 字符串 | `water`、`lava` | `cauldron`<br/>`lava cauldron` |
| `chemistry_table_type` | 字符串 | `compound_creator`、`material_reducer`、`element_constructor`、`lab_table` | `chemistry table` |
| `chisel_type` | 字符串 | `default`、`chiseled`、`lines`、`smooth` | `purpur block`<br/>`quartz block` |
| `cluster_count` | 整数 | `0-3` | `sea pickle` |
| `color` | 字符串 | `white`、`orange`、`magenta`、`light_blue`、`yellow`、`lime`、`pink`、`gray`、`silver`、`cyan`、`purple`、`blue`、`brown`、`green`、`red`、`black` | `cloth`<br/>`concrete`<br/>`concrete powder block`<br/>`hard stained glass`<br/>`shulker box`<br/>`stained glass`<br/>`stained glass pane`<br/>`stained hardened clay`<br/>`wool carpet` |
| `color_bit` | 布尔值 | `true`、`false` | `blue colored torch` |
| `composter_fill_level` | 整数 | `0-8` | `composter` |
| `conditional_bit` | 布尔值 | `true`、`false` | `chain command block`<br/>`repeating command block` |
| `coral_color` | 字符串 | `blue`、`pink`、`purple`、`red`、`yellow`、`blue dead`、`pink dead`、`red dead`、`yellow dead` | `coral fan`<br/>`coral fan dead`<br/>`coral`<br/>`coral block` |
| `coral_direction` | 整数 | `0-3` | `coral fan hang`<br/>`coral fan hang 2`<br/>`coral fan hang 3` |
| `coral_fan_direction` | 整数 | `0, 1` | `coral fan`<br/>`coral fan dead` |
| `coral_hang_type_bit` | 布尔值 | `true`、`false` | `coral fan hang`<br/>`coral fan hang 2`<br/>`coral fan hang 3` |
| `covered_bit` | 布尔值 | `true`、`false` | `top snow` |
| `cracked_state` | 字符串 | `no_cracks`、`cracked`、`max_cracked` | `turtle egg` |
| `damage` | 字符串 | `undamaged`、`slightly_damaged`、`very_damaged`、`broken` | `anvil` |
| `deprecated` | 无 | 无 | 未列出 |
| `dead_bit` | 布尔值 | `true`、`false` | `coral fan hang`<br/>`coral fan hang 2`<br/>`coral fan hang 3` |
| `direction` | 整数 | `0-3` | `acacia door`<br/>`acacia fence gate`<br/>`acacia trapdoor`<br/>`anvil`<br/>`bed`<br/>`bell`<br/>`birch door`<br/>`birch fence gate`<br/>`birch trapdoor`<br/>`campfire`<br/>`carved pumpkin`<br/>`chalkboard`<br/>`chemistry table`<br/>`cocoa`<br/>`crimson door`<br/>`crimson fence gate`<br/>`crimson trapdoor`<br/>`dark oak door`<br/>`dark oak fence gate`<br/>`dark oak trapdoor`<br/>`end portal frame`<br/>`fence gate`<br/>`iron door`<br/>`iron trapdoor`<br/>`jungle door`<br/>`jungle fence gate`<br/>`jungle trapdoor`<br/>`lectern`<br/>`loom`<br/>`mangrove door`<br/>`mangrove fence gate`<br/>`mangrove trapdoor`<br/>`powered comparator`<br/>`powered repeater`<br/>`pumpkin`<br/>`soul campfire`<br/>`spruce door`<br/>`spruce fence gate`<br/>`spruce trapdoor`<br/>`trapdoor`<br/>`trip wire hook`<br/>`unpowered comparator`<br/>`unpowered repeater`<br/>`warped door`<br/>`warped fence gate`<br/>`warped trapdoor`<br/>`wooden door` |
| `dirt_type` | 字符串 | `normal`、`coarse` | `dirt` |
| `disarmed_bit` | 布尔值 | `true`、`false` | `trip wire block` |
| `door_hinge_bit` | 布尔值 | `true`、`false` | `acacia door`<br/>`birch door`<br/>`crimson door`<br/>`dark oak door`<br/>`iron door`<br/>`jungle door`<br/>`mangrove door`<br/>`spruce door`<br/>`warped door`<br/>`wooden door` |
| `double_plant_type` | 字符串 | `sunflower`、`syringa`、`grass`、`fern`、`rose`、`peony` | `double plant` |
| `drag_down` | 布尔值 | `true`、`false` | `bubble column` |
| `dripstone_thickness` | 字符串 | `tip`、`frustum`、`base`、`middle`、`merge` | `pointed dripstone` |
| `end_portal_eye_bit` | 布尔值 | `true`、`false` | `end portal frame` |
| `explode_bit` | 布尔值 | `true`、`false` | 未列出 |
| `extinguished` | 布尔值 | `true`、`false` | `magma`<br/>`netherrack` |
| `facing_direction` | 字符串 | `down`、`up`、`north`、`south`、`east`、`west` | `acacia button`<br/>`birch button`<br/>`crimson button`<br/>`dark oak button`<br/>`jungle button`<br/>`mangrove button`<br/>`polished blackstone button`<br/>`spruce button`<br/>`stone button`<br/>`warped button`<br/>`wood button` |
| `fill_level` | 整数 | `0-6` | `cauldron`<br/>`lava cauldron` |
| `flower_type` | 字符串 | `poppy`、`orchid`、`allium`、`houstonia`、`tulip_red`、`tulip_orange`、`tulip_white`、`tulip_pink`、`oxeye`、`cornflower`、`lily_of_the_valley` | `red flower` |
| `growth` | 整数 | `0-7` | `pumpkin stem`<br/>`beetroot`<br/>`carrot`<br/>`crop`<br/>`potato`<br/>`sweet berry bush` |
| `hanging_bit` | 布尔值 | `true`、`false` | `lantern`<br/>`soul lantern` |
| `head_piece_bit` | 布尔值 | `true`、`false` | `bed` |
| `height` | 整数 | `0-7` | `top snow` |
| `honey_level` | 整数 | `0-5` | `Beehive` |
| `huge_mushroom_bits` | 整数 | `0-15` | `brown mushroom block`<br/>`red mushroom block`<br/>`huge mushroom block` |
| `infiniburn_bit` | 布尔值 | `true`、`false` | `bedrock` |
| `in_wall_bit` | 布尔值 | `true`、`false` | `birch fence gate`<br/>`crimson fence gate`<br/>`dark oak fence gate`<br/>`fence gate`<br/>`jungle fence gate`<br/>`mangrove fence gate`<br/>`spruce fence gate`<br/>`warped fence gate` |
| `item_frame_map_bit` | 布尔值 | `true`、`false` | `glow item frame`<br/>`item frame` |
| `item_frame_photo_bit` | 布尔值 | `true`、`false` | `glow item frame`<br/>`item frame` |
| `kelp_age` | 整数 | `0-24` | `kelp` |
| `lever_direction` | 字符串 | `down_east_west`、`east`、`west`、`south`、`north`、`up_north_south`、`up_east_west`、`down_north_south` | `lever` |
| `liquid_depth` | 整数 | `0-15` | `lava`<br/>`water`<br/>`flowing lava`<br/>`flowing water` |
| `lit` | 布尔值 | `true`、`false` | `candle`<br/>`candle cake`<br/>`black candle`<br/>`black candle cake`<br/>`blue candle`<br/>`blue candle cake`<br/>`brown candle`<br/>`brown candle cake`<br/>`cyan candle`<br/>`cyan candle cake`<br/>`gray candle`<br/>`gray candle cake`<br/>`green candle`<br/>`green candle cake`<br/>`light blue candle`<br/>`light blue candle cake`<br/>`light gray candle`<br/>`light gray candle cake`<br/>`lime candle`<br/>`lime candle cake`<br/>`magenta candle`<br/>`magenta candle cake`<br/>`orange candle`<br/>`orange candle cake`<br/>`pink candle`<br/>`pink candle cake`<br/>`purple candle`<br/>`purple candle cake`<br/>`red candle`<br/>`red candle cake`<br/>`white candle`<br/>`white candle cake`<br/>`yellow candle`<br/>`yellow candle cake` |
| `moisturized_amount` | 整数 | `0-7` | `farm` |
| `monster_egg_stone_type` | 字符串 | `stone`、`cobblestone`、`stone_brick`、`mossy_stone_brick`、`cracked_stone_brick`、`chiseled_stone_brick` | `monster stone egg`<br/>`monster egg` |
| `multi_face_direction_bits` | 整数 | `0-63` | `glow lichen`<br/>`sculk vein` |
| `new_leaf_type` | 字符串 | `acacia`、`dark_oak` | `new leaf` |
| `new_log_type` | 字符串 | `acacia`、`dark_oak` | `new log` |
| `occupied_bit` | 布尔值 | `true`、`false` | `bed` |
| `old_leaf_type` | 字符串 | `oak`、`spruce`、`birch`、`jungle` | `old leaf`<br/>`leaves` |
| `old_log_type` | 字符串 | `oak`、`spruce`、`birch`、`jungle` | `log` |
| `ominous` | 布尔值 | `true`、`false` | 未列出 |
| `open_bit` | 布尔值 | `true`、`false` | `acacia door`<br/>`acacia fence gate`<br/>`barrel`<br/>`birch door`<br/>`birch fence gate`<br/>`crimson door`<br/>`crimson fence gate`<br/>`dark oak door`<br/>`dark oak fence gate`<br/>`fence gate`<br/>`iron door`<br/>`jungle door`<br/>`jungle fence gate`<br/>`mangrove door`<br/>`mangrove fence gate`<br/>`spruce door`<br/>`spruce fence gate`<br/>`warped door`<br/>`warped fence gate`<br/>`wooden door`<br/>`lever` |
| `output_lit_bit` | 布尔值 | `true`、`false` | `powered comparator`<br/>`unpowered comparator` |
| `output_subtract_bit` | 布尔值 | `true`、`false` | `powered comparator`<br/>`unpowered comparator` |
| `persistent_bit` | 布尔值 | `true`、`false` | `azalea leaves`<br/>`azalea leaves flowered`<br/>`leaves`<br/>`mangrove leaves`<br/>`new leaf`<br/>`old leaf` |
| `pillar_axis` | 字符串 | `x`、`y`、`z` | `basalt`<br/>`bone_block`<br/>`chain`<br/>`crimson stem`<br/>`mangrove log`<br/>`mangrove wood`<br/>`muddy mangrove roots`<br/>`stripped crimson hyphae`<br/>`stripped crimson stem`<br/>`stripped mangrove wood`<br/>`stripped warped hyphae`<br/>`stripped warped stem`<br/>`polished basalt`<br/>`warped hyphae`<br/>`warped stem` |
| `portal_axis` | 字符串 | `unknown`、`x`、`z` | `portal` |
| `powered_bit` | 布尔值 | `true`、`false` | `lectern`<br/>`observer`<br/>`sculk sensor`<br/>`trip wire block`<br/>`trip wire hook` |
| `prismarine_block_type` | 字符串 | `default`、`dark`、`bricks` | `prismarine` |
| `rail_data_bit` | 布尔值 | `true`、`false` | `activator rail`<br/>`detector rail block`<br/>`powered rail block` |
| `rail_direction` | 整数 | `0-8` | `activator rail`<br/>`detector rail block`<br/>`powered rail block`<br/>`rail` |
| `redstone_signal` | 整数 | `0-15` | `crimson pressure plate`<br/>`daylight detector`<br/>`daylight detector inverted`<br/>`heavy weighted pressure plate`<br/>`light weighted pressure plate`<br/>`mangrove pressure plate`<br/>`polished blackstone pressure plate`<br/>`pressure plate acacia`<br/>`pressure plate birch`<br/>`pressure plate dark oak`<br/>`pressure plate jungle`<br/>`pressure plate spruce`<br/>`redstone dust`<br/>`stone pressure plate`<br/>`warped pressure plate`<br/>`wood pressure plate` |
| `repeater_delay` | 整数 | `0-3` | `powered repeater`<br/>`unpowered repeater` |
| `respawn_anchor_charge` | 整数 | `0-4` | `respawn anchor` |
| `rotation` | 整数 | `0-15` | `jigsaw` |
| `sandstone_type` | 字符串 | `default`、`hieroglyphs`、`cut`、`smooth` | `sandstone`<br/>`red sandstone` |
| `sand_type` | 字符串 | `normal`、`red` | `sand` |
| `sapling_type` | 字符串 | `evergreen`、`birch`、`jungle`、`acacia`、`roofed_oak` | `bamboo sapling`<br/>`sapling` |
| `sculk_sensor_phase` | 字符串 | `inactive`、`active`、`cooldown` | 未列出 |
| `sea_grass_type` | 字符串 | `default`、`double_top`、`double_bot` | `sea grass` |
| `sponge_type` | 字符串 | `dry`、`wet` | `sponge` |
| `stability` | 整数 | `0-7` | `scaffolding` |
| `stability_check` | 布尔值 | `true`、`false` | `scaffolding` |
| `stone_brick_type` | 字符串 | `default`、`mossy`、`cracked`、`chiseled`、`smooth` | `stone brick` |
| `stone_slab_type` | 字符串 | `smooth_stone`、`sandstone`、`wood`、`cobblestone`、`brick`、`stone_brick`、`quartz`、`nether_brick` | `double stone slab`<br/>`stone slab` |
| `stone_slab_type_2` | 字符串 | `red_sandstone`、`purpur`、`prismarine_rough`、`prismarine_dark`、`prismarine_brick`、`mossy_cobblestone`、`smooth_sandstone`、`red_nether_brick` | `double stone slab 2`<br/>`stone slab 2` |
| `stone_slab_type_3` | 字符串 | `end_stone_brick`、`smooth_red_sandstone`、`polished_andesite`、`andesite`、`diorite`、`polished_diorite`、`granite`、`polished_granite` | `double stone slab 3`<br/>`stone slab 3` |
| `stone_slab_type_4` | 字符串 | `mossy_stone_brick`、`smooth_quartz`、`stone`、`cut_sandstone`、`cut_red_sandstone` | `double stone slab 4`<br/>`stone slab 4` |
| `stone_type` | 字符串 | `stone`、`granite`、`granite_smooth`、`diorite`、`diorite_smooth`、`andesite`、`andesite_smooth` | `stone`<br/>`granite`<br/>`smooth granite`<br/>`diorite`<br/>`smooth diorite`<br/>`andesite`<br/>`smooth andesite` |
| `stripped_bit` | 布尔值 | `true`、`false` | `mangrove wood`<br/>`wood` |
| `structure_block_type` | 字符串 | `data`、`save`、`load`、`corner`、`invalid`、`export` | `structure block` |
| `structure_void_type` | 字符串 | `void`、`air` | `structure void` |
| `suspended_bit` | 布尔值 | `true`、`false` | `trip wire block` |
| `tall_grass_type` | 字符串 | `default`、`tall`、`fern`、`snow` | `tall grass` |
| `toggle_bit` | 布尔值 | `true`、`false` | `bell`<br/>`hopper` |
| `top_slot_bit` | 布尔值 | `true`、`false` | `blackstone double slab`<br/>`blackstone slab`<br/>`cobbled deepslate double slab`<br/>`cobbled deepslate slab`<br/>`crimson double slab`<br/>`crimson slab`<br/>`cut copper slab`<br/>`deepslate brick double slab`<br/>`deepslate brick slab`<br/>`deepslate tile double slab`<br/>`deepslate tile slab`<br/>`double cut copper slab`<br/>`double stone slab`<br/>`double stone slab 2`<br/>`double stone slab 3`<br/>`double stone slab 4`<br/>`double wooden slab`<br/>`exposed cut copper slab`<br/>`exposed double cut copper slab`<br/>`mangrove double slab`<br/>`mangrove slab`<br/>`mud brick double slab`<br/>`mud brick slab`<br/>`oxidized cut copper slab`<br/>`oxidized double cut copper slab`<br/>`polished blackstone brick double slab`<br/>`polished blackstone brick slab`<br/>`polished blackstone double slab`<br/>`polished blackstone slab`<br/>`polished deepslate double slab`<br/>`polished deepslate slab`<br/>`stone slab`<br/>`stone slab 2`<br/>`stone slab 3`<br/>`stone slab 4`<br/>`warped double slab`<br/>`warped slab`<br/>`waxed cut copper slab`<br/>`waxed double cut copper slab`<br/>`waxed exposed cut copper slab`<br/>`waxed exposed double cut copper slab`<br/>`waxed oxidized cut copper slab`<br/>`waxed oxidized double cut copper slab`<br/>`waxed weathered cut copper slab`<br/>`waxed weathered double cut copper slab`<br/>`weathered cut copper slab`<br/>`weathered double cut copper slab`<br/>`wooden slab` |
| `torch_facing_direction` | 字符串 | `unknown`、`west`、`east`、`north`、`south`、`top` | `red colored torch`<br/>`redstone torch`<br/>`soul torch`<br/>`torch`<br/>`underwater torch`<br/>`unlit redstone torch` |
| `triggered_bit` | 布尔值 | `true`、`false` | `dispenser`<br/>`dropper` |
| `turtle_egg_count` | 字符串 | `one_egg`、`two_egg`、`three_egg`、`four_egg` | `turtle egg` |
| `twisting_vines_age` | 整数 | `0-25` | `twisting vines` |
| `update_bit` | 布尔值 | `true`、`false` | `azalea leaves`<br/>`azalea leaves flowered`<br/>`leaves`<br/>`mangrove leaves`<br/>`flower pot`<br/>`new leaf`<br/>`old leaf` |
| `upper_block_bit` | 布尔值 | `true`、`false` | `acacia door`<br/>`birch door`<br/>`crimson door`<br/>`double plant`<br/>`dark oak door`<br/>`iron door`<br/>`jungle door`<br/>`mangrove door`<br/>`small dripleaf`<br/>`spruce door`<br/>`warped door`<br/>`wooden door` |
| `upside_down_bit` | 布尔值 | `true`、`false` | `acacia stairs`<br/>`acacia trapdoor`<br/>`andesite stairs`<br/>`blackstone stairs`<br/>`birch stairs`<br/>`birch trapdoor`<br/>`brick stairs`<br/>`cobbled deepslate stairs`<br/>`cobblestone stairs`<br/>`crimson stairs`<br/>`crimson trapdoor`<br/>`cut copper stairs`<br/>`dark oak stairs`<br/>`dark oak trapdoor`<br/>`dark prismarine stairs`<br/>`deepslate brick stairs`<br/>`deepslate tile stairs`<br/>`diorite stairs`<br/>`end brick stairs`<br/>`exposed cut copper stairs`<br/>`granite stairs`<br/>`iron trapdoor`<br/>`jungle stairs`<br/>`jungle trapdoor`<br/>`mangrove stairs`<br/>`mangrove trapdoor`<br/>`mossy cobblestone stairs`<br/>`mossy stone brick stairs`<br/>`mud brick stairs`<br/>`nether brick stairs`<br/>`normal stone stairs`<br/>`oak stairs`<br/>`oxidized cut copper stairs`<br/>`polished andesite stairs`<br/>`polished blackstone brick stairs`<br/>`polished blackstone stairs`<br/>`polished deepslate stairs`<br/>`polished diorite stairs`<br/>`polished granite stairs`<br/>`prismarine bricks stairs`<br/>`prismarine stairs`<br/>`purpur stairs`<br/>`quartz stairs`<br/>`red sandstone stairs`<br/>`sandstone stairs`<br/>`smooth quartz stairs`<br/>`smooth red sandstone stairs`<br/>`smooth sandstone stairs`<br/>`spruce stairs`<br/>`spruce trapdoor`<br/>`stone brick stairs`<br/>`trapdoor`<br/>`warped stairs`<br/>`warped trapdoor`<br/>`waxed cut copper stairs`<br/>`waxed exposed cut copper stairs`<br/>`waxed oxidized cut copper stairs`<br/>`waxed weathered cut copper stairs`<br/>`weathered cut copper stairs` |
| `vertical_half` | 字符串 | `bottom`、`top` | 未列出 |
| `vine_direction_bits` | 整数 | `0-15` | `vine` |
| `wall_block_type` | 字符串 | `cobblestone`、`mossy_cobblestone`、`granite`、`diorite`、`andesite`、`sandstone`、`brick`、`stone_brick`、`mossy_stone_brick`、`nether_brick`、`end_brick`、`prismarine`、`red_sandstone`、`red_nether_brick` | `cobblestone`<br/>`mossy cobblestone`<br/>`granite`<br/>`diorite`<br/>`andesite`<br/>`sandstone`<br/>`brick`<br/>`stone brick`<br/>`mossy stone brick`<br/>`nether brick`<br/>`end brick`<br/>`prismarine`<br/>`red sandstone`<br/>`red nether brick` |
| `wall_connection_type_east` | 字符串 | `none`、`short`、`tall` | `blackstone wall`<br/>`border`<br/>`cobbled deepslate wall`<br/>`cobblestone wall`<br/>`deepslate brick wall`<br/>`deepslate tile wall`<br/>`mud brick wall`<br/>`polished blackstone brick wall`<br/>`polished blackstone wall`<br/>`polished deepslate wall` |
| `wall_connection_type_north` | 字符串 | `none`、`short`、`tall` | `blackstone wall`<br/>`border`<br/>`cobbled deepslate wall`<br/>`cobblestone wall`<br/>`deepslate brick wall`<br/>`deepslate tile wall`<br/>`mud brick wall`<br/>`polished blackstone brick wall`<br/>`polished blackstone wall`<br/>`polished deepslate wall` |
| `wall_connection_type_south` | 字符串 | `none`、`short`、`tall` | `blackstone wall`<br/>`border`<br/>`cobbled deepslate wall`<br/>`cobblestone wall`<br/>`deepslate brick wall`<br/>`deepslate tile wall`<br/>`mud brick wall`<br/>`polished blackstone brick wall`<br/>`polished blackstone wall`<br/>`polished deepslate wall` |
| `wall_connection_type_west` | 字符串 | `none`、`short`、`tall` | `blackstone wall`<br/>`border`<br/>`cobbled deepslate wall`<br/>`cobblestone wall`<br/>`deepslate brick wall`<br/>`deepslate tile wall`<br/>`mud brick wall`<br/>`polished blackstone brick wall`<br/>`polished blackstone wall`<br/>`polished deepslate wall` |
| `wall_post_bit` | 布尔值 | `true`、`false` | `blackstone wall`<br/>`border`<br/>`cobbled deepslate wall`<br/>`cobblestone wall`<br/>`deepslate brick wall`<br/>`deepslate tile wall`<br/>`mud brick wall`<br/>`polished blackstone brick wall`<br/>`polished blackstone wall`<br/>`polished deepslate wall` |
| `weeping_vines_age` | 整数 | `0-15` | `weeping vines` |
| `weirdo_direction` | 整数 | `0-3` | `acacia stairs`<br/>`acacia trapdoor`<br/>`andesite stairs`<br/>`blackstone stairs`<br/>`birch stairs`<br/>`birch trapdoor`<br/>`brick stairs`<br/>`cobbled deepslate stairs`<br/>`cobblestone stairs`<br/>`crimson stairs`<br/>`crimson trapdoor`<br/>`cut copper stairs`<br/>`dark oak stairs`<br/>`dark oak trapdoor`<br/>`dark prismarine stairs`<br/>`deepslate brick stairs`<br/>`deepslate tile stairs`<br/>`diorite stairs`<br/>`end brick stairs`<br/>`exposed cut copper stairs`<br/>`granite stairs`<br/>`iron trapdoor`<br/>`jungle stairs`<br/>`jungle trapdoor`<br/>`mangrove stairs`<br/>`mangrove trapdoor`<br/>`mossy cobblestone stairs`<br/>`mossy stone brick stairs`<br/>`mud brick stairs`<br/>`nether brick stairs`<br/>`normal stone stairs`<br/>`oak stairs`<br/>`oxidized cut copper stairs`<br/>`polished andesite stairs`<br/>`polished blackstone brick stairs`<br/>`polished blackstone stairs`<br/>`polished deepslate stairs`<br/>`polished diorite stairs`<br/>`polished granite stairs`<br/>`prismarine bricks stairs`<br/>`prismarine stairs`<br/>`purpur stairs`<br/>`quartz stairs`<br/>`red sandstone stairs`<br/>`sandstone stairs`<br/>`smooth quartz stairs`<br/>`smooth red sandstone stairs`<br/>`smooth sandstone stairs`<br/>`spruce stairs`<br/>`spruce trapdoor`<br/>`stone brick stairs`<br/>`trapdoor`<br/>`warped stairs`<br/>`warped trapdoor`<br/>`waxed cut copper stairs`<br/>`waxed exposed cut copper stairs`<br/>`waxed oxidized cut copper stairs`<br/>`waxed weathered cut copper stairs`<br/>`weathered cut copper stairs` |
| `wood_type` | 字符串 | `oak`、`spruce`、`birch`、`jungle`、`acacia`、`dark_oak` | `fence`<br/>`double wooden slab`<br/>`planks`<br/>`wood`<br/>`wooden slab` |

<!-- md:sortable -->