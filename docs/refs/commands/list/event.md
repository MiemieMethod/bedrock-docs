# `/event`

> 文档版本：1.21.0.24

`/event`命令command.event.description

/// settings | 执行条件
该命令需要权限等级：`gamedirectors`|`1`。该命令需要开启作弊。
///

## 用法

/// tab | 重载1
```mcfunction
/event entity <target:target> <eventName:EntityEvents>
```

//// html | div.result
command.event.1.description

///// define
`entity`：<!-- md:samp EventEntityAction -->

- 枚举类型。command.enum.evententityaction.description单值枚举，请直接使用`entity`。

`target`：<!-- md:samp target -->

- 基本类型。command.event.target.description

`eventName`：<!-- md:samp EntityEvents -->

- 枚举类型。command.enum.entityevents.description枚举值如下：

  |值|描述|
  |---|---|
  |`abort_sheltering`|command.enum.entityevents.abort_sheltering|
  |`admire_item_started_event`|command.enum.entityevents.admire_item_started_event|
  |`admire_item_stopped_event`|command.enum.entityevents.admire_item_stopped_event|
  |`ageable_grow_up`|command.enum.entityevents.ageable_grow_up|
  |`attack_cooldown_complete_event`|command.enum.entityevents.attack_cooldown_complete_event|
  |`attacked`|command.enum.entityevents.attacked|
  |`be_sheared`|command.enum.entityevents.be_sheared|
  |`become_angry`|command.enum.entityevents.become_angry|
  |`become_angry_event`|command.enum.entityevents.become_angry_event|
  |`become_calm_event`|command.enum.entityevents.become_calm_event|
  |`become_cow`|command.enum.entityevents.become_cow|
  |`become_pregnant`|command.enum.entityevents.become_pregnant|
  |`become_stray_event`|command.enum.entityevents.become_stray_event|
  |`become_witch`|command.enum.entityevents.become_witch|
  |`become_zombie`|command.enum.entityevents.become_zombie|
  |`become_zombie_event`|command.enum.entityevents.become_zombie_event|
  |`calmed_down`|command.enum.entityevents.calmed_down|
  |`change_to_skeleton`|command.enum.entityevents.change_to_skeleton|
  |`collected_nectar`|command.enum.entityevents.collected_nectar|
  |`countdown_to_perish_event`|command.enum.entityevents.countdown_to_perish_event|
  |`dried_out`|command.enum.entityevents.dried_out|
  |`enter_water`|command.enum.entityevents.enter_water|
  |`escaped_event`|command.enum.entityevents.escaped_event|
  |`find_flower_timeout`|command.enum.entityevents.find_flower_timeout|
  |`find_hive_event`|command.enum.entityevents.find_hive_event|
  |`find_hive_timeout`|command.enum.entityevents.find_hive_timeout|
  |`from_egg`|command.enum.entityevents.from_egg|
  |`from_explosion`|command.enum.entityevents.from_explosion|
  |`from_village`|command.enum.entityevents.from_village|
  |`go_back_to_spawn_failed`|command.enum.entityevents.go_back_to_spawn_failed|
  |`got_in_powder_snow`|command.enum.entityevents.got_in_powder_snow|
  |`got_out_of_powder_snow`|command.enum.entityevents.got_out_of_powder_snow|
  |`grow_up`|command.enum.entityevents.grow_up|
  |`hive_destroyed`|command.enum.entityevents.hive_destroyed|
  |`important_block_destroyed_event`|command.enum.entityevents.important_block_destroyed_event|
  |`in_desert`|command.enum.entityevents.in_desert|
  |`in_snow`|command.enum.entityevents.in_snow|
  |`killed_enemy_event`|command.enum.entityevents.killed_enemy_event|
  |`laid_egg`|command.enum.entityevents.laid_egg|
  |`minecraft:add_attributes`|command.enum.entityevents.minecraft:add_attributes|
  |`minecraft:add_biome_and_skin`|command.enum.entityevents.minecraft:add_biome_and_skin|
  |`minecraft:add_can_ride`|command.enum.entityevents.minecraft:add_can_ride|
  |`minecraft:ageable_grow_up`|command.enum.entityevents.minecraft:ageable_grow_up|
  |`minecraft:ageable_set_baby`|command.enum.entityevents.minecraft:ageable_set_baby|
  |`minecraft:ambient_night`|command.enum.entityevents.minecraft:ambient_night|
  |`minecraft:ambient_normal`|command.enum.entityevents.minecraft:ambient_normal|
  |`minecraft:ambient_sleep`|command.enum.entityevents.minecraft:ambient_sleep|
  |`minecraft:as_adult`|command.enum.entityevents.minecraft:as_adult|
  |`minecraft:as_baby`|command.enum.entityevents.minecraft:as_baby|
  |`minecraft:ate_allium`|command.enum.entityevents.minecraft:ate_allium|
  |`minecraft:ate_bluet`|command.enum.entityevents.minecraft:ate_bluet|
  |`minecraft:ate_cornflower`|command.enum.entityevents.minecraft:ate_cornflower|
  |`minecraft:ate_daisy`|command.enum.entityevents.minecraft:ate_daisy|
  |`minecraft:ate_dandelion`|command.enum.entityevents.minecraft:ate_dandelion|
  |`minecraft:ate_lily`|command.enum.entityevents.minecraft:ate_lily|
  |`minecraft:ate_orchid`|command.enum.entityevents.minecraft:ate_orchid|
  |`minecraft:ate_poppy`|command.enum.entityevents.minecraft:ate_poppy|
  |`minecraft:ate_rose`|command.enum.entityevents.minecraft:ate_rose|
  |`minecraft:ate_torchflower`|command.enum.entityevents.minecraft:ate_torchflower|
  |`minecraft:ate_tulip`|command.enum.entityevents.minecraft:ate_tulip|
  |`minecraft:baby_on_calm`|command.enum.entityevents.minecraft:baby_on_calm|
  |`minecraft:become_aggressive`|command.enum.entityevents.minecraft:become_aggressive|
  |`minecraft:become_aggro`|command.enum.entityevents.minecraft:become_aggro|
  |`minecraft:become_anenonme`|command.enum.entityevents.minecraft:become_anenonme|
  |`minecraft:become_angry`|command.enum.entityevents.minecraft:become_angry|
  |`minecraft:become_armorable`|command.enum.entityevents.minecraft:become_armorable|
  |`minecraft:become_armorer`|command.enum.entityevents.minecraft:become_armorer|
  |`minecraft:become_black_tang`|command.enum.entityevents.minecraft:become_black_tang|
  |`minecraft:become_blue_dory`|command.enum.entityevents.minecraft:become_blue_dory|
  |`minecraft:become_brown`|command.enum.entityevents.minecraft:become_brown|
  |`minecraft:become_brown_adult`|command.enum.entityevents.minecraft:become_brown_adult|
  |`minecraft:become_butcher`|command.enum.entityevents.minecraft:become_butcher|
  |`minecraft:become_butterfly_fish`|command.enum.entityevents.minecraft:become_butterfly_fish|
  |`minecraft:become_calm`|command.enum.entityevents.minecraft:become_calm|
  |`minecraft:become_cartographer`|command.enum.entityevents.minecraft:become_cartographer|
  |`minecraft:become_cc_betta`|command.enum.entityevents.minecraft:become_cc_betta|
  |`minecraft:become_charged`|command.enum.entityevents.minecraft:become_charged|
  |`minecraft:become_cichlid`|command.enum.entityevents.minecraft:become_cichlid|
  |`minecraft:become_cleric`|command.enum.entityevents.minecraft:become_cleric|
  |`minecraft:become_clownfish`|command.enum.entityevents.minecraft:become_clownfish|
  |`minecraft:become_dog_fish`|command.enum.entityevents.minecraft:become_dog_fish|
  |`minecraft:become_e_red_snapper`|command.enum.entityevents.minecraft:become_e_red_snapper|
  |`minecraft:become_farmer`|command.enum.entityevents.minecraft:become_farmer|
  |`minecraft:become_fisherman`|command.enum.entityevents.minecraft:become_fisherman|
  |`minecraft:become_fletcher`|command.enum.entityevents.minecraft:become_fletcher|
  |`minecraft:become_goat_fish`|command.enum.entityevents.minecraft:become_goat_fish|
  |`minecraft:become_hostile`|command.enum.entityevents.minecraft:become_hostile|
  |`minecraft:become_leatherworker`|command.enum.entityevents.minecraft:become_leatherworker|
  |`minecraft:become_librarian`|command.enum.entityevents.minecraft:become_librarian|
  |`minecraft:become_mason`|command.enum.entityevents.minecraft:become_mason|
  |`minecraft:become_moorish_idol`|command.enum.entityevents.minecraft:become_moorish_idol|
  |`minecraft:become_neutral`|command.enum.entityevents.minecraft:become_neutral|
  |`minecraft:become_ornate_butterfly`|command.enum.entityevents.minecraft:become_ornate_butterfly|
  |`minecraft:become_parrot_fish`|command.enum.entityevents.minecraft:become_parrot_fish|
  |`minecraft:become_pregnant`|command.enum.entityevents.minecraft:become_pregnant|
  |`minecraft:become_queen_angel_fish`|command.enum.entityevents.minecraft:become_queen_angel_fish|
  |`minecraft:become_red`|command.enum.entityevents.minecraft:become_red|
  |`minecraft:become_red_adult`|command.enum.entityevents.minecraft:become_red_adult|
  |`minecraft:become_red_cichlid`|command.enum.entityevents.minecraft:become_red_cichlid|
  |`minecraft:become_red_lipped_benny`|command.enum.entityevents.minecraft:become_red_lipped_benny|
  |`minecraft:become_red_snapper`|command.enum.entityevents.minecraft:become_red_snapper|
  |`minecraft:become_scared`|command.enum.entityevents.minecraft:become_scared|
  |`minecraft:become_sheperd`|command.enum.entityevents.minecraft:become_sheperd|
  |`minecraft:become_stunned`|command.enum.entityevents.minecraft:become_stunned|
  |`minecraft:become_threadfin`|command.enum.entityevents.minecraft:become_threadfin|
  |`minecraft:become_tomato_clown`|command.enum.entityevents.minecraft:become_tomato_clown|
  |`minecraft:become_toolsmith`|command.enum.entityevents.minecraft:become_toolsmith|
  |`minecraft:become_triggerfish`|command.enum.entityevents.minecraft:become_triggerfish|
  |`minecraft:become_unskilled`|command.enum.entityevents.minecraft:become_unskilled|
  |`minecraft:become_weaponsmith`|command.enum.entityevents.minecraft:become_weaponsmith|
  |`minecraft:become_yellow_tail_parrot`|command.enum.entityevents.minecraft:become_yellow_tail_parrot|
  |`minecraft:become_yellow_tang`|command.enum.entityevents.minecraft:become_yellow_tang|
  |`minecraft:born_default`|command.enum.entityevents.minecraft:born_default|
  |`minecraft:born_screamer`|command.enum.entityevents.minecraft:born_screamer|
  |`minecraft:calm`|command.enum.entityevents.minecraft:calm|
  |`minecraft:camel_saddled`|command.enum.entityevents.minecraft:camel_saddled|
  |`minecraft:camel_unsaddled`|command.enum.entityevents.minecraft:camel_unsaddled|
  |`minecraft:cat_gifted_owner`|command.enum.entityevents.minecraft:cat_gifted_owner|
  |`minecraft:clear_add_raid_omen`|command.enum.entityevents.minecraft:clear_add_raid_omen|
  |`minecraft:command_block_activate`|command.enum.entityevents.minecraft:command_block_activate|
  |`minecraft:command_block_deactivate`|command.enum.entityevents.minecraft:command_block_deactivate|
  |`minecraft:convert_to_drowned`|command.enum.entityevents.minecraft:convert_to_drowned|
  |`minecraft:convert_to_zombie`|command.enum.entityevents.minecraft:convert_to_zombie|
  |`minecraft:crystal_explode`|command.enum.entityevents.minecraft:crystal_explode|
  |`minecraft:defend_wandering_trader`|command.enum.entityevents.minecraft:defend_wandering_trader|
  |`minecraft:donkey_saddled`|command.enum.entityevents.minecraft:donkey_saddled|
  |`minecraft:donkey_unsaddled`|command.enum.entityevents.minecraft:donkey_unsaddled|
  |`minecraft:emerged`|command.enum.entityevents.minecraft:emerged|
  |`minecraft:end_roar`|command.enum.entityevents.minecraft:end_roar|
  |`minecraft:entered_bubble_column_down`|command.enum.entityevents.minecraft:entered_bubble_column_down|
  |`minecraft:entered_bubble_column_up`|command.enum.entityevents.minecraft:entered_bubble_column_up|
  |`minecraft:entity_born`|command.enum.entityevents.minecraft:entity_born|
  |`minecraft:entity_born_wild`|command.enum.entityevents.minecraft:entity_born_wild|
  |`minecraft:entity_spawned`|command.enum.entityevents.minecraft:entity_spawned|
  |`minecraft:entity_transformed`|command.enum.entityevents.minecraft:entity_transformed|
  |`minecraft:exited_bubble_column`|command.enum.entityevents.minecraft:exited_bubble_column|
  |`minecraft:exited_disturbed_hive`|command.enum.entityevents.minecraft:exited_disturbed_hive|
  |`minecraft:exited_hive`|command.enum.entityevents.minecraft:exited_hive|
  |`minecraft:exited_hive_on_fire`|command.enum.entityevents.minecraft:exited_hive_on_fire|
  |`minecraft:explode`|command.enum.entityevents.minecraft:explode|
  |`minecraft:flowerless`|command.enum.entityevents.minecraft:flowerless|
  |`minecraft:fox_configure_day`|command.enum.entityevents.minecraft:fox_configure_day|
  |`minecraft:fox_configure_defending`|command.enum.entityevents.minecraft:fox_configure_defending|
  |`minecraft:fox_configure_docile_day`|command.enum.entityevents.minecraft:fox_configure_docile_day|
  |`minecraft:fox_configure_docile_night`|command.enum.entityevents.minecraft:fox_configure_docile_night|
  |`minecraft:fox_configure_night`|command.enum.entityevents.minecraft:fox_configure_night|
  |`minecraft:fox_configure_thunderstorm`|command.enum.entityevents.minecraft:fox_configure_thunderstorm|
  |`minecraft:from_full_puff`|command.enum.entityevents.minecraft:from_full_puff|
  |`minecraft:from_player`|command.enum.entityevents.minecraft:from_player|
  |`minecraft:from_village`|command.enum.entityevents.minecraft:from_village|
  |`minecraft:from_wandering_trader`|command.enum.entityevents.minecraft:from_wandering_trader|
  |`minecraft:gain_raid_omen`|command.enum.entityevents.minecraft:gain_raid_omen|
  |`minecraft:go_lay_egg`|command.enum.entityevents.minecraft:go_lay_egg|
  |`minecraft:has_target`|command.enum.entityevents.minecraft:has_target|
  |`minecraft:hive_full`|command.enum.entityevents.minecraft:hive_full|
  |`minecraft:hopper_activate`|command.enum.entityevents.minecraft:hopper_activate|
  |`minecraft:hopper_deactivate`|command.enum.entityevents.minecraft:hopper_deactivate|
  |`minecraft:horse_saddled`|command.enum.entityevents.minecraft:horse_saddled|
  |`minecraft:horse_unsaddled`|command.enum.entityevents.minecraft:horse_unsaddled|
  |`minecraft:increase_max_health`|command.enum.entityevents.minecraft:increase_max_health|
  |`minecraft:join_caravan`|command.enum.entityevents.minecraft:join_caravan|
  |`minecraft:laid_egg`|command.enum.entityevents.minecraft:laid_egg|
  |`minecraft:leave_caravan`|command.enum.entityevents.minecraft:leave_caravan|
  |`minecraft:lost_target`|command.enum.entityevents.minecraft:lost_target|
  |`minecraft:mad_at_wolf`|command.enum.entityevents.minecraft:mad_at_wolf|
  |`minecraft:make_black`|command.enum.entityevents.minecraft:make_black|
  |`minecraft:make_brown`|command.enum.entityevents.minecraft:make_brown|
  |`minecraft:make_chestnut`|command.enum.entityevents.minecraft:make_chestnut|
  |`minecraft:make_creamy`|command.enum.entityevents.minecraft:make_creamy|
  |`minecraft:make_darkbrown`|command.enum.entityevents.minecraft:make_darkbrown|
  |`minecraft:make_gray`|command.enum.entityevents.minecraft:make_gray|
  |`minecraft:make_white`|command.enum.entityevents.minecraft:make_white|
  |`minecraft:melee_mode`|command.enum.entityevents.minecraft:melee_mode|
  |`minecraft:mule_saddled`|command.enum.entityevents.minecraft:mule_saddled|
  |`minecraft:mule_unsaddled`|command.enum.entityevents.minecraft:mule_unsaddled|
  |`minecraft:no_threat_detected`|command.enum.entityevents.minecraft:no_threat_detected|
  |`minecraft:on_anger`|command.enum.entityevents.minecraft:on_anger|
  |`minecraft:on_calm`|command.enum.entityevents.minecraft:on_calm|
  |`minecraft:on_chest`|command.enum.entityevents.minecraft:on_chest|
  |`minecraft:on_deflate`|command.enum.entityevents.minecraft:on_deflate|
  |`minecraft:on_eat_block`|command.enum.entityevents.minecraft:on_eat_block|
  |`minecraft:on_full_puff`|command.enum.entityevents.minecraft:on_full_puff|
  |`minecraft:on_half_puff`|command.enum.entityevents.minecraft:on_half_puff|
  |`minecraft:on_hurt_event`|command.enum.entityevents.minecraft:on_hurt_event|
  |`minecraft:on_instant_prime`|command.enum.entityevents.minecraft:on_instant_prime|
  |`minecraft:on_leash`|command.enum.entityevents.minecraft:on_leash|
  |`minecraft:on_normal_puff`|command.enum.entityevents.minecraft:on_normal_puff|
  |`minecraft:on_not_riding_player`|command.enum.entityevents.minecraft:on_not_riding_player|
  |`minecraft:on_prime`|command.enum.entityevents.minecraft:on_prime|
  |`minecraft:on_riding_player`|command.enum.entityevents.minecraft:on_riding_player|
  |`minecraft:on_saddled`|command.enum.entityevents.minecraft:on_saddled|
  |`minecraft:on_scared`|command.enum.entityevents.minecraft:on_scared|
  |`minecraft:on_sheared`|command.enum.entityevents.minecraft:on_sheared|
  |`minecraft:on_tame`|command.enum.entityevents.minecraft:on_tame|
  |`minecraft:on_trust`|command.enum.entityevents.minecraft:on_trust|
  |`minecraft:on_unleash`|command.enum.entityevents.minecraft:on_unleash|
  |`minecraft:panda_aggressive`|command.enum.entityevents.minecraft:panda_aggressive|
  |`minecraft:panda_brown`|command.enum.entityevents.minecraft:panda_brown|
  |`minecraft:panda_lazy`|command.enum.entityevents.minecraft:panda_lazy|
  |`minecraft:panda_playful`|command.enum.entityevents.minecraft:panda_playful|
  |`minecraft:panda_weak`|command.enum.entityevents.minecraft:panda_weak|
  |`minecraft:panda_worried`|command.enum.entityevents.minecraft:panda_worried|
  |`minecraft:pet_slept_with_owner`|command.enum.entityevents.minecraft:pet_slept_with_owner|
  |`minecraft:promote_to_illager_captain`|command.enum.entityevents.minecraft:promote_to_illager_captain|
  |`minecraft:promote_to_patrol_captain`|command.enum.entityevents.minecraft:promote_to_patrol_captain|
  |`minecraft:raid_expired`|command.enum.entityevents.minecraft:raid_expired|
  |`minecraft:ranged_mode`|command.enum.entityevents.minecraft:ranged_mode|
  |`minecraft:remove_persistence`|command.enum.entityevents.minecraft:remove_persistence|
  |`minecraft:remove_raid_trigger`|command.enum.entityevents.minecraft:remove_raid_trigger|
  |`minecraft:resupply_trades`|command.enum.entityevents.minecraft:resupply_trades|
  |`minecraft:roll_up`|command.enum.entityevents.minecraft:roll_up|
  |`minecraft:schedule_bed_villager`|command.enum.entityevents.minecraft:schedule_bed_villager|
  |`minecraft:schedule_gather_villager`|command.enum.entityevents.minecraft:schedule_gather_villager|
  |`minecraft:schedule_home_villager`|command.enum.entityevents.minecraft:schedule_home_villager|
  |`minecraft:schedule_play_villager`|command.enum.entityevents.minecraft:schedule_play_villager|
  |`minecraft:schedule_wander_villager`|command.enum.entityevents.minecraft:schedule_wander_villager|
  |`minecraft:schedule_work_farmer`|command.enum.entityevents.minecraft:schedule_work_farmer|
  |`minecraft:schedule_work_fisher`|command.enum.entityevents.minecraft:schedule_work_fisher|
  |`minecraft:schedule_work_librarian`|command.enum.entityevents.minecraft:schedule_work_librarian|
  |`minecraft:schedule_work_pro_villager`|command.enum.entityevents.minecraft:schedule_work_pro_villager|
  |`minecraft:scheduled`|command.enum.entityevents.minecraft:scheduled|
  |`minecraft:set_trap`|command.enum.entityevents.minecraft:set_trap|
  |`minecraft:sink`|command.enum.entityevents.minecraft:sink|
  |`minecraft:spawn_adult`|command.enum.entityevents.minecraft:spawn_adult|
  |`minecraft:spawn_armorer`|command.enum.entityevents.minecraft:spawn_armorer|
  |`minecraft:spawn_as_illager_captain`|command.enum.entityevents.minecraft:spawn_as_illager_captain|
  |`minecraft:spawn_as_patrol_follower`|command.enum.entityevents.minecraft:spawn_as_patrol_follower|
  |`minecraft:spawn_as_strider_jockey`|command.enum.entityevents.minecraft:spawn_as_strider_jockey|
  |`minecraft:spawn_baby`|command.enum.entityevents.minecraft:spawn_baby|
  |`minecraft:spawn_baby_strider_jockey`|command.enum.entityevents.minecraft:spawn_baby_strider_jockey|
  |`minecraft:spawn_butcher`|command.enum.entityevents.minecraft:spawn_butcher|
  |`minecraft:spawn_cleric`|command.enum.entityevents.minecraft:spawn_cleric|
  |`minecraft:spawn_emerging`|command.enum.entityevents.minecraft:spawn_emerging|
  |`minecraft:spawn_farmer`|command.enum.entityevents.minecraft:spawn_farmer|
  |`minecraft:spawn_for_raid`|command.enum.entityevents.minecraft:spawn_for_raid|
  |`minecraft:spawn_for_raid_with_evoker_rider`|command.enum.entityevents.minecraft:spawn_for_raid_with_evoker_rider|
  |`minecraft:spawn_for_raid_with_pillager_rider`|command.enum.entityevents.minecraft:spawn_for_raid_with_pillager_rider|
  |`minecraft:spawn_from_village`|command.enum.entityevents.minecraft:spawn_from_village|
  |`minecraft:spawn_librarian`|command.enum.entityevents.minecraft:spawn_librarian|
  |`minecraft:spawn_midnight_cat`|command.enum.entityevents.minecraft:spawn_midnight_cat|
  |`minecraft:spawn_skilled_adult`|command.enum.entityevents.minecraft:spawn_skilled_adult|
  |`minecraft:spawn_tame_adult`|command.enum.entityevents.minecraft:spawn_tame_adult|
  |`minecraft:spawn_tame_baby`|command.enum.entityevents.minecraft:spawn_tame_baby|
  |`minecraft:spawn_wild_adult`|command.enum.entityevents.minecraft:spawn_wild_adult|
  |`minecraft:spawn_wild_ashen`|command.enum.entityevents.minecraft:spawn_wild_ashen|
  |`minecraft:spawn_wild_baby`|command.enum.entityevents.minecraft:spawn_wild_baby|
  |`minecraft:spawn_wild_baby_or_adult`|command.enum.entityevents.minecraft:spawn_wild_baby_or_adult|
  |`minecraft:spawn_wild_black`|command.enum.entityevents.minecraft:spawn_wild_black|
  |`minecraft:spawn_wild_chestnut`|command.enum.entityevents.minecraft:spawn_wild_chestnut|
  |`minecraft:spawn_wild_pale`|command.enum.entityevents.minecraft:spawn_wild_pale|
  |`minecraft:spawn_wild_rusty`|command.enum.entityevents.minecraft:spawn_wild_rusty|
  |`minecraft:spawn_wild_snowy`|command.enum.entityevents.minecraft:spawn_wild_snowy|
  |`minecraft:spawn_wild_spotted`|command.enum.entityevents.minecraft:spawn_wild_spotted|
  |`minecraft:spawn_wild_striped`|command.enum.entityevents.minecraft:spawn_wild_striped|
  |`minecraft:spawn_wild_woods`|command.enum.entityevents.minecraft:spawn_wild_woods|
  |`minecraft:spawn_with_pillager_captain_rider`|command.enum.entityevents.minecraft:spawn_with_pillager_captain_rider|
  |`minecraft:spawn_with_pillager_rider`|command.enum.entityevents.minecraft:spawn_with_pillager_rider|
  |`minecraft:spawn_with_vindicator_captain_rider`|command.enum.entityevents.minecraft:spawn_with_vindicator_captain_rider|
  |`minecraft:spawn_with_vindicator_rider`|command.enum.entityevents.minecraft:spawn_with_vindicator_rider|
  |`minecraft:spring_trap`|command.enum.entityevents.minecraft:spring_trap|
  |`minecraft:start_celebrating`|command.enum.entityevents.minecraft:start_celebrating|
  |`minecraft:start_death`|command.enum.entityevents.minecraft:start_death|
  |`minecraft:start_despawn`|command.enum.entityevents.minecraft:start_despawn|
  |`minecraft:start_exploding`|command.enum.entityevents.minecraft:start_exploding|
  |`minecraft:start_exploding_forced`|command.enum.entityevents.minecraft:start_exploding_forced|
  |`minecraft:start_fly`|command.enum.entityevents.minecraft:start_fly|
  |`minecraft:start_full_puff`|command.enum.entityevents.minecraft:start_full_puff|
  |`minecraft:start_half_puff`|command.enum.entityevents.minecraft:start_half_puff|
  |`minecraft:start_johnny`|command.enum.entityevents.minecraft:start_johnny|
  |`minecraft:start_land`|command.enum.entityevents.minecraft:start_land|
  |`minecraft:start_peeking`|command.enum.entityevents.minecraft:start_peeking|
  |`minecraft:start_playing_idle_ground_sound`|command.enum.entityevents.minecraft:start_playing_idle_ground_sound|
  |`minecraft:start_roar`|command.enum.entityevents.minecraft:start_roar|
  |`minecraft:start_sitting`|command.enum.entityevents.minecraft:start_sitting|
  |`minecraft:start_transforming`|command.enum.entityevents.minecraft:start_transforming|
  |`minecraft:start_unrolling`|command.enum.entityevents.minecraft:start_unrolling|
  |`minecraft:stop_aggro`|command.enum.entityevents.minecraft:stop_aggro|
  |`minecraft:stop_celebrating`|command.enum.entityevents.minecraft:stop_celebrating|
  |`minecraft:stop_exploding`|command.enum.entityevents.minecraft:stop_exploding|
  |`minecraft:stop_johnny`|command.enum.entityevents.minecraft:stop_johnny|
  |`minecraft:stop_peeking`|command.enum.entityevents.minecraft:stop_peeking|
  |`minecraft:stop_playing_idle_ground_sound`|command.enum.entityevents.minecraft:stop_playing_idle_ground_sound|
  |`minecraft:stop_sitting`|command.enum.entityevents.minecraft:stop_sitting|
  |`minecraft:stop_transforming`|command.enum.entityevents.minecraft:stop_transforming|
  |`minecraft:switch_to_melee`|command.enum.entityevents.minecraft:switch_to_melee|
  |`minecraft:switch_to_ranged`|command.enum.entityevents.minecraft:switch_to_ranged|
  |`minecraft:target_far_enough`|command.enum.entityevents.minecraft:target_far_enough|
  |`minecraft:target_too_close`|command.enum.entityevents.minecraft:target_too_close|
  |`minecraft:threat_detected`|command.enum.entityevents.minecraft:threat_detected|
  |`minecraft:to_full_puff`|command.enum.entityevents.minecraft:to_full_puff|
  |`minecraft:trigger_raid`|command.enum.entityevents.minecraft:trigger_raid|
  |`minecraft:turn_black`|command.enum.entityevents.minecraft:turn_black|
  |`minecraft:turn_blue`|command.enum.entityevents.minecraft:turn_blue|
  |`minecraft:turn_brown`|command.enum.entityevents.minecraft:turn_brown|
  |`minecraft:turn_cyan`|command.enum.entityevents.minecraft:turn_cyan|
  |`minecraft:turn_gray`|command.enum.entityevents.minecraft:turn_gray|
  |`minecraft:turn_green`|command.enum.entityevents.minecraft:turn_green|
  |`minecraft:turn_light_blue`|command.enum.entityevents.minecraft:turn_light_blue|
  |`minecraft:turn_lime`|command.enum.entityevents.minecraft:turn_lime|
  |`minecraft:turn_magenta`|command.enum.entityevents.minecraft:turn_magenta|
  |`minecraft:turn_orange`|command.enum.entityevents.minecraft:turn_orange|
  |`minecraft:turn_pink`|command.enum.entityevents.minecraft:turn_pink|
  |`minecraft:turn_purple`|command.enum.entityevents.minecraft:turn_purple|
  |`minecraft:turn_red`|command.enum.entityevents.minecraft:turn_red|
  |`minecraft:turn_silver`|command.enum.entityevents.minecraft:turn_silver|
  |`minecraft:turn_white`|command.enum.entityevents.minecraft:turn_white|
  |`minecraft:turn_yellow`|command.enum.entityevents.minecraft:turn_yellow|
  |`minecraft:unroll`|command.enum.entityevents.minecraft:unroll|
  |`navigation_off_land`|command.enum.entityevents.navigation_off_land|
  |`navigation_on_land`|command.enum.entityevents.navigation_on_land|
  |`on_calm`|command.enum.entityevents.on_calm|
  |`on_digging_event`|command.enum.entityevents.on_digging_event|
  |`on_digging_start`|command.enum.entityevents.on_digging_start|
  |`on_egg_spawned`|command.enum.entityevents.on_egg_spawned|
  |`on_fail_during_digging`|command.enum.entityevents.on_fail_during_digging|
  |`on_fail_during_searching`|command.enum.entityevents.on_fail_during_searching|
  |`on_feeling_happy_end`|command.enum.entityevents.on_feeling_happy_end|
  |`on_item_found`|command.enum.entityevents.on_item_found|
  |`on_not_riding_parent`|command.enum.entityevents.on_not_riding_parent|
  |`on_pregnant`|command.enum.entityevents.on_pregnant|
  |`on_rising_end`|command.enum.entityevents.on_rising_end|
  |`on_scenting_success`|command.enum.entityevents.on_scenting_success|
  |`on_search_and_digging_success`|command.enum.entityevents.on_search_and_digging_success|
  |`perish_event`|command.enum.entityevents.perish_event|
  |`pickup_item_delay`|command.enum.entityevents.pickup_item_delay|
  |`pickup_item_delay_complete`|command.enum.entityevents.pickup_item_delay_complete|
  |`recover_after_dried_out`|command.enum.entityevents.recover_after_dried_out|
  |`seek_shelter`|command.enum.entityevents.seek_shelter|
  |`spawn_adult`|command.enum.entityevents.spawn_adult|
  |`spawn_adult_melee`|command.enum.entityevents.spawn_adult_melee|
  |`spawn_adult_melee_no_hunting`|command.enum.entityevents.spawn_adult_melee_no_hunting|
  |`spawn_adult_no_hunting`|command.enum.entityevents.spawn_adult_no_hunting|
  |`spawn_adult_parent_jockey`|command.enum.entityevents.spawn_adult_parent_jockey|
  |`spawn_adult_piglin_jockey`|command.enum.entityevents.spawn_adult_piglin_jockey|
  |`spawn_adult_ranged`|command.enum.entityevents.spawn_adult_ranged|
  |`spawn_adult_ranged_no_hunting`|command.enum.entityevents.spawn_adult_ranged_no_hunting|
  |`spawn_adult_unhuntable`|command.enum.entityevents.spawn_adult_unhuntable|
  |`spawn_baby`|command.enum.entityevents.spawn_baby|
  |`spawn_cold`|command.enum.entityevents.spawn_cold|
  |`spawn_large`|command.enum.entityevents.spawn_large|
  |`spawn_medium`|command.enum.entityevents.spawn_medium|
  |`spawn_small`|command.enum.entityevents.spawn_small|
  |`spawn_temperate`|command.enum.entityevents.spawn_temperate|
  |`spawn_warm`|command.enum.entityevents.spawn_warm|
  |`start_drying_out`|command.enum.entityevents.start_drying_out|
  |`start_dryingout`|command.enum.entityevents.start_dryingout|
  |`start_event`|command.enum.entityevents.start_event|
  |`start_suffocating`|command.enum.entityevents.start_suffocating|
  |`start_zombification_event`|command.enum.entityevents.start_zombification_event|
  |`stop_drying_out`|command.enum.entityevents.stop_drying_out|
  |`stop_dryingout`|command.enum.entityevents.stop_dryingout|
  |`stop_panicking_after_fire`|command.enum.entityevents.stop_panicking_after_fire|
  |`stop_suffocating`|command.enum.entityevents.stop_suffocating|
  |`stop_zombification_event`|command.enum.entityevents.stop_zombification_event|
  |`switch_to_melee`|command.enum.entityevents.switch_to_melee|
  |`switch_to_ranged`|command.enum.entityevents.switch_to_ranged|
  |`villager_converted`|command.enum.entityevents.villager_converted|
  |`wololo`|command.enum.entityevents.wololo|



/////

////

///