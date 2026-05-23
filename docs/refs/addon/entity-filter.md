# 实体过滤器

本页列出国际版官方实体参考中收录的实体过滤器测试。过滤器可用于实体事件、组件、AI意向、生成规则和客户端实体资源选择等场景，用于判断目标对象、环境或数值条件是否成立。

## 基本字段

| 字段 | 类型 | 说明 |
|---|---|---|
| `test` | 字符串 | 过滤器测试名。 |
| `subject` | 字符串 | 测试主体，常见值包括`self`、`other`、`player`、`target`、`parent`、`damager`和`block`。默认通常为`self`。 |
| `operator` | 字符串 | 比较运算符，常见值包括`==`、`!=`、`<`、`<=`、`>`、`>=`、`equals`和`not`。 |
| `value` | 任意 | 与测试结果比较的值，类型由具体测试决定。 |
| `domain` | 任意 | 可选。部分测试用于指定槽位、区域或其他测试域。 |

## 逻辑组合

`all_of`要求所有子过滤器通过，`any_of`要求至少一个子过滤器通过，`none_of`要求所有子过滤器均不通过。旧式大写键`AND`、`OR`、`NOT`在原版示例中仍可见，但新内容宜优先使用小写组合键。

## 测试列表

| 测试名 | 用途分类 |
|---|---|
| `actor_health` | 数值 |
| `all_slots_empty` | 物品与装备 |
| `any_slot_empty` | 物品与装备 |
| `bool_property` | 属性 |
| `clock_time` | 环境与位置 |
| `distance_to_nearest_player` | 数值 |
| `enum_property` | 属性 |
| `float_property` | 属性 |
| `has_ability` | 拥有关系 |
| `has_biome_tag` | 环境与位置 |
| `has_component` | 拥有关系 |
| `has_container_open` | 物品与装备 |
| `has_damage` | 数值 |
| `has_damaged_equipment` | 物品与装备 |
| `has_equipment` | 物品与装备 |
| `has_equipment_block_tag` | 物品与装备 |
| `has_equipment_tag` | 物品与装备 |
| `has_item_with_component` | 物品与装备 |
| `has_mob_effect` | 拥有关系 |
| `has_nametag` | 拥有关系 |
| `has_property` | 属性 |
| `has_ranged_weapon` | 物品与装备 |
| `has_same_equipment_in_slot_as` | 物品与装备 |
| `has_silk_touch` | 物品与装备 |
| `has_tag` | 拥有关系 |
| `has_target` | 拥有关系 |
| `has_trade_supply` | 拥有关系 |
| `home_distance` | 数值 |
| `hourly_clock_time` | 环境与位置 |
| `in_block` | 环境与位置 |
| `in_caravan` | 实体状态 |
| `in_clouds` | 环境与位置 |
| `in_contact_with_water` | 环境与位置 |
| `in_lava` | 环境与位置 |
| `in_nether` | 环境与位置 |
| `in_overworld` | 环境与位置 |
| `in_water` | 环境与位置 |
| `in_water_or_rain` | 环境与位置 |
| `inactivity_timer` | 数值 |
| `int_property` | 属性 |
| `is_altitude` | 环境与位置 |
| `is_avoiding_mobs` | 实体状态 |
| `is_baby` | 实体状态 |
| `is_biome` | 环境与位置 |
| `is_block` | 环境与位置 |
| `is_bound_to_creaking_heart` | 实体状态 |
| `is_brightness` | 环境与位置 |
| `is_climbing` | 实体状态 |
| `is_color` | 实体状态 |
| `is_controlling_passenger_family` | 实体状态 |
| `is_daytime` | 环境与位置 |
| `is_difficulty` | 实体状态 |
| `is_family` | 实体状态 |
| `is_game_rule` | 实体状态 |
| `is_humid` | 环境与位置 |
| `is_immobile` | 实体状态 |
| `is_in_same_vehicle` | 实体状态 |
| `is_in_village` | 实体状态 |
| `is_leashed` | 实体状态 |
| `is_leashed_to` | 实体状态 |
| `is_mark_variant` | 实体状态 |
| `is_missing_health` | 数值 |
| `is_moving` | 实体状态 |
| `is_navigating` | 实体状态 |
| `is_owner` | 实体状态 |
| `is_panicking` | 实体状态 |
| `is_persistent` | 实体状态 |
| `is_raider` | 实体状态 |
| `is_riding` | 实体状态 |
| `is_riding_self` | 实体状态 |
| `is_sitting` | 实体状态 |
| `is_skin_id` | 实体状态 |
| `is_sleeping` | 实体状态 |
| `is_sneak_held` | 实体状态 |
| `is_sneaking` | 实体状态 |
| `is_snow_covered` | 环境与位置 |
| `is_sprinting` | 实体状态 |
| `is_tamed` | 实体状态 |
| `is_target` | 实体状态 |
| `is_temperature_type` | 环境与位置 |
| `is_temperature_value` | 环境与位置 |
| `is_underground` | 环境与位置 |
| `is_underwater` | 环境与位置 |
| `is_variant` | 实体状态 |
| `is_vehicle_family` | 实体状态 |
| `is_visible` | 实体状态 |
| `is_waterlogged` | 环境与位置 |
| `is_weather` | 环境与位置 |
| `light_level` | 环境与位置 |
| `moon_intensity` | 环境与位置 |
| `moon_phase` | 环境与位置 |
| `on_fire` | 环境与位置 |
| `on_ground` | 环境与位置 |
| `on_hot_block` | 环境与位置 |
| `on_ladder` | 环境与位置 |
| `owner_distance` | 数值 |
| `property` | 属性 |
| `random_chance` | 数值 |
| `redstone_strength_at_position` | 其他 |
| `rider_count` | 数值 |
| `surface_mob` | 实体状态 |
| `taking_fire_damage` | 环境与位置 |
| `target_distance` | 数值 |
| `trusts` | 实体状态 |
| `was_last_hurt_by` | 实体状态 |
| `weather` | 环境与位置 |
| `weather_at_position` | 环境与位置 |
| `y_rotation` | 其他 |

<!-- md:sortable -->
