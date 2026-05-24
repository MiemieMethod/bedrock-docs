# 原版粒子列表

本页汇总可在国际版客户端中观察到的原版粒子标识符，并按`/particle`命令下的可用性进行分类。

/// warning | 版本边界
本页数据来自EaseCation Wiki粒子资料快照，主要反映旧版社区实测结果。基岩版更新后，粒子可见性、上下文依赖和日志行为可能变化。实际项目中应以目标版本实测与内容日志为准。
///

## 使用说明

- `/particle`命令通常需要完整赋命名空间标识符，例如`minecraft:basic_flame_particle`。
- 部分粒子依赖实体上下文变量或特定环境，命令可触发发射器但可能显示异常或记录错误。
- 部分粒子仅在水下等条件下可见。

## 可直接使用的粒子

| 粒子标识符 |
| --- |
| `minecraft:basic_flame_particle` |
| `minecraft:basic_portal_particle` |
| `minecraft:basic_smoke_particle` |
| `minecraft:bleach` |
| `minecraft:blue_flame_particle` |
| `minecraft:camera_shoot_explosion` |
| `minecraft:campfire_smoke_particle` |
| `minecraft:campfire_tall_smoke_particle` |
| `minecraft:candle_flame_particle` |
| `minecraft:critical_hit_emitter` |
| `minecraft:crop_growth_emitter` |
| `minecraft:dragon_breath_trail` |
| `minecraft:dragon_death_explosion_emitter` |
| `minecraft:dragon_destroy_block` |
| `minecraft:dragon_dying_explosion` |
| `minecraft:endrod` |
| `minecraft:end_chest` |
| `minecraft:evocation_fang_particle` |
| `minecraft:evoker_spell` |
| `minecraft:cauldron_explosion_emitter` |
| `minecraft:egg_destroy_emitter` |
| `minecraft:falling_border_dust_particle` |
| `minecraft:falling_dust_dragon_egg_particle` |
| `minecraft:falling_dust_gravel_particle` |
| `minecraft:falling_dust_red_sand_particle` |
| `minecraft:falling_dust_sand_particle` |
| `minecraft:falling_dust_scaffolding_particle` |
| `minecraft:falling_dust_top_snow_particle` |
| `minecraft:heart_particle` |
| `minecraft:honey_drip_particle` |
| `minecraft:huge_explosion_lab_misc_emitter` |
| `minecraft:huge_explosion_emitter` |
| `minecraft:ice_evaporation_emitter` |
| `minecraft:knockback_roar_particle` |
| `minecraft:lab_table_misc_mystical_particle` |
| `minecraft:large_explosion` |
| `minecraft:lava_drip_particle` |
| `minecraft:lava_particle` |
| `minecraft:llama_spit_smoke` |
| `minecraft:magnesium_salts_emitter` |
| `minecraft:mob_portal` |
| `minecraft:mycelium_dust_particle` |
| `minecraft:obsidian_glow_dust_particle` |
| `minecraft:obsidian_tear_particle` |
| `minecraft:redstone_ore_dust_particle` |
| `minecraft:redstone_repeater_dust_particle` |
| `minecraft:redstone_torch_dust_particle` |
| `minecraft:redstone_wire_dust_particle` |
| `minecraft:rising_border_dust_particle` |
| `minecraft:sculk_sensor_redstone_particle` |
| `minecraft:snowflake_particle` |
| `minecraft:spore_blossom_ambient_particle` |
| `minecraft:spore_blossom_shower_particle` |
| `minecraft:stalactite_lava_drip_particle` |
| `minecraft:stalactite_water_drip_particle` |
| `minecraft:totem_particle` |
| `minecraft:villager_angry` |
| `minecraft:villager_happy` |
| `minecraft:water_drip_particle` |
| `minecraft:water_evaporation_bucket_emitter` |
| `minecraft:water_splash_particle_manual` |

## 可生成但可能报错的粒子

下列粒子通常能被命令触发，但可能因上下文变量不足而出现显示异常或内容日志报错。

| 粒子标识符 |
| --- |
| `minecraft:arrow_spell_emitter` |
| `minecraft:balloon_gas_particle` |
| `minecraft:basic_crit_particle` |
| `minecraft:conduit_absorb_particle` |
| `minecraft:conduit_attack_emitter` |
| `minecraft:dragon_breath_fire` |
| `minecraft:dragon_breath_lingering` |
| `minecraft:electric_spark_particle` |
| `minecraft:enchanting_table_particle` |
| `minecraft:elephant_tooth_paste_vapor_particle` |
| `minecraft:death_explosion_emitter` |
| `minecraft:eyeofender_death_explode_particle` |
| `minecraft:explosion_particle` |
| `minecraft:falling_dust_concrete_powder_particle` |
| `minecraft:lab_table_heatblock_dust_particle` |
| `minecraft:misc_fire_vapor_particle` |
| `minecraft:mobspell_emitter` |
| `minecraft:mob_block_spawn_emitter` |
| `minecraft:note_particle` |
| `minecraft:portal_directional` |
| `minecraft:portal_reverse_particle` |
| `minecraft:rain_splash_particle` |
| `minecraft:shulker_bullet` |
| `minecraft:silverfish_grief_emitter` |
| `minecraft:soul_particle` |
| `minecraft:sparkler_emitter` |
| `minecraft:splash_spell_emitter` |
| `minecraft:water_evaporation_actor_emitter` |
| `minecraft:water_splash_particle` |
| `minecraft:water_wake_particle` |
| `minecraft:wax_particle` |
| `minecraft:wither_boss_invulnerable` |

## 仅水下可见的粒子

| 粒子标识符 |
| --- |
| `minecraft:basic_bubble_particle` |
| `minecraft:basic_bubble_particle_manual` |
| `minecraft:bubble_column_bubble` |
| `minecraft:bubble_column_down_particle` |
| `minecraft:bubble_column_up_particle` |
| `minecraft:cauldron_bubble_particle` |
| `minecraft:cauldron_splash_particle` |
| `minecraft:dolphin_move_particle` |
| `minecraft:eye_of_ender_bubble_particle` |
| `minecraft:fish_hook_particle` |
| `minecraft:fish_pos_particle` |
| `minecraft:glow_particle` |
| `minecraft:guardian_attack_particle` |
| `minecraft:guardian_water_move_particle` |
| `minecraft:sponge_absorb_water_particle` |
| `minecraft:squid_flee_particle` |
| `minecraft:squid_ink_bubble` |
| `minecraft:squid_move_particle` |
| `minecraft:underwater_torch_particle` |

## 可能持续存在的粒子

下列粒子在旧版实测中可能长期存在，通常需要重新进入世界后才会清理。

| 粒子标识符 |
| --- |
| `minecraft:mobflame_emitter` |
| `minecraft:nectar_drip_particle` |
| `minecraft:phantom_trail_particle` |
| `minecraft:stunned_emitter` |

## 通常无法正常使用的粒子

| 粒子标识符 |
| --- |
| `minecraft:block_destruct` |
| `minecraft:block_slide` |
| `minecraft:breaking_item_icon` |
| `minecraft:breaking_item_terrain` |
| `minecraft:cauldron_spell_emitter` |
| `minecraft:ink_emitter` |
| `minecraft:portal_east_west` |
| `minecraft:portal_north_south` |
| `minecraft:vibration_signal` |
| `minecraft:colored_flame_particle` |

## 组件短名称

以下是部分原版粒子的组件短名称，可在实体行为组件（如`minecraft:particle_on_jump`等）的`particle_type`字段中使用，无需写出完整赋命名空间标识符。

/// note | 说明
此列表经社区实测证实可正常使用，但不保证完整。部分短名称的实际颜色或外观受组件上下文（如药水ID）影响。
///

| 短名称 | 备注 |
| --- | --- |
| `mobspellambient` | 颜色由组件中存在的药水ID决定 |
| `villagerangry` | |
| `bubble` | 仅水下可见 |
| `evaporation` | |
| `crit` | |
| `dragonbreath` | 仅对弹射物的AoE组件有效 |
| `driplava` | |
| `dripwater` | |
| `reddust` | |
| `enchantingtable` | |
| `endrod` | |
| `mobspell` | 颜色由组件中存在的药水ID决定 |
| `largeexplode` | |
| `hugeexplosion` | |
| `fallingdust` | 颜色由组件中存在的药水ID决定 |
| `waterwake` | |
| `flame` | |
| `villagerhappy` | |
| `heart` | |
| `mobspellinstantaneous` | |
| `iconcrack` | |
| `slime` | |
| `snowballpoof` | |
| `largesmoke` | |
| `lava` | |
| `mobflame` | |
| `townaura` | |
| `note` | |
| `explode` | |
| `portal` | |
| `rainsplash` | |
| `smoke` | |
| `watersplash` | |
| `ink` | |
| `terrain` | 纹理取自地形图集 |
| `totem` | |
| `witchspell` | |
| `soul` | |
| `spit` | |
| `sneeze` | |