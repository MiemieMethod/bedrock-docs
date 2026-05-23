# 命令参数类型

本页基于Microsoft Learn的CommandTypeList与54个参数类型子页整理。参数类型名称与格式声明保持官方定义，用于命令语法对照和版本排查。

## 别名类型

| 类型名称 | 别名关系 |
|---|---|
| Entity Selector | 别名指向`SELECTION` |
| Block Name | 别名指向`BLOCK` |
| Boolean | 别名指向`BOOLEAN` |
| Enchantment | 别名指向`ENCHANT` |
| Entity Type | 别名指向`ENTITY_TYPE` |
| Integer | 别名指向`INT` |
| Item Name | 别名指向`ITEM` |

## 类型总表

| 类型名称 | 格式 | 示例值 | 官方说明 | 来源文件 |
|---|---|---|---|---|
| Entity Selector | `@a, @e, @p, @r, @s` | — | Targets entities. | `type_actor.md` |
| Biome | `biome_name` | `plains`; `desert`; `forest` | A biome identifier. | `type_biome.md` |
| Block ID | `namespace:block_name or block_name` | `stone`; `minecraft:diamond_block`; `oak_planks` | A block type identifier. | `type_block.md` |
| Block Name | — | — | A block type identifier. | `type_blockname.md` |
| Block Position | `x y z or ~ ~ ~` | `~ ~ ~`; `0 64 0` | Block coordinates as integers. | `type_blockpos.md` |
| Boolean | — | — | A true or false value. | `type_bool.md` |
| Boolean | `true or false` | `true`; `false` | A true or false value. | `type_boolean.md` |
| Camera Preset | `namespace:preset_name` | `minecraft:free`; `minecraft:first_person`; `minecraft:third_person` | Named camera preset from behavior packs. | `type_camerapresetid.md` |
| Clip Mode | `player, camera, or default` | `player`; `camera` | How to handle entity clipping during camera/spectator mode. | `type_clipmode.md` |
| Comparison Operator | `<, <=, =, >=, or >` | `<`; `<=`; `=` | Operator for comparing values in scoreboard tests. | `type_compareoperator.md` |
| Difficulty | `peaceful, easy, normal, or hard` | `peaceful`; `easy`; `normal` | The world difficulty level. | `type_difficulty.md` |
| Dimension | `dimension_name` | `overworld`; `nether`; `the_end` | A dimension identifier. | `type_dimensiontype.md` |
| Easing Type | `linear, ease_in, ease_out, ease_in_out, etc.` | `linear`; `ease_in`; `ease_out` | Animation easing function for camera transitions. | `type_easetype.md` |
| Effect | `effect_name` | `speed`; `strength`; `invisibility` | A status effect (potion effect) identifier. | `type_effect.md` |
| Enchantment | `enchantment_name` | `sharpness`; `protection`; `efficiency` | An enchantment identifier. | `type_enchant.md` |
| Enchantment | — | — | An enchantment identifier. | `type_enchantmenttype.md` |
| Entity Type | — | — | An entity type identifier. | `type_entitytype.md` |
| Entity Type | `namespace:entity_type or entity_type` | `pig`; `minecraft:zombie`; `armor_stand` | An entity type identifier (mob, item, projectile, etc.). | `type_entity_type.md` |
| File Path | `path/to/file` | — | A path to a file or resource. | `type_filepath.md` |
| Decimal Number | `0, 1.5, -3.14, etc.` | `0`; `0.5`; `1.5` | A number that can include decimals. | `type_float.md` |
| Integer Range | `min..max, ..max, min.., or single value` | `1..10`; `..5`; `10..` | A range of integers, or a single integer. | `type_fullintegerrange.md` |
| Game Mode | `survival, creative, adventure, or spectator` | `survival`; `creative`; `adventure` | The player's game mode. | `type_gamemode.md` |
| Game Rule | `gamerule_name` | `doDaylightCycle`; `doWeatherCycle`; `doMobSpawning` | A world setting that can be changed. | `type_gamerule.md` |
| Identifier | `lowercase_name` | `my_objective`; `player_score` | A unique identifier string. | `type_id.md` |
| Integer | `..., -2, -1, 0, 1, 2, ...` | `0`; `64`; `-10` | A whole number (no decimals). | `type_int.md` |
| Integer | — | — | A whole number (no decimals). | `type_integer.md` |
| Item ID | `namespace:item_name or item_name` | `diamond`; `minecraft:iron_sword`; `golden_apple` | An item type identifier. | `type_item.md` |
| Item Name | — | — | An item type identifier. | `type_itemname.md` |
| JSON Object | `{"key": "value", ...}` | `{"key":"value"}` | A JSON object with key-value pairs. | `type_json_object.md` |
| Message | — | — | A text message. | `type_message.md` |
| Message | `Any text, optionally with @selectors` | `Hello World!`; `Welcome, @p!`; `@a has joined the game` | A text message that will be displayed to players. | `type_message_root.md` |
| Objective Criteria | `dummy (most common)` | `dummy` | The criteria type for a scoreboard objective. | `type_objectivecriteria.md` |
| Scoreboard Objective | `alphanumeric with underscores, max 16 characters` | `kills`; `deaths`; `score` | Name of a scoreboard objective. | `type_objectivename.md` |
| Scoreboard Operation | `+=, -=, *=, /=, %=, =, <, >, or ><` | `+=`; `-=`; `*=` | Mathematical operation for scoreboard calculations. | `type_operator.md` |
| Function Path | `namespace:path/to/function` | `mypack:setup`; `mypack:utils/helper`; `tick` | Path to a function file within a behavior pack. | `type_pathcommand.md` |
| Player Selector | `@a, @p, @r, or @s` | `@a`; `@p`; `@r` | Targets one or more players. | `type_player_selector.md` |
| Block Position | `x y z or ~ ~ ~` | `100 64 -200`; `~10 ~ ~`; `~ ~5 ~` | A 3D block position (integer coordinates). | `type_position.md` |
| Position (x y z) | `x y z, ~ ~ ~, or ^ ^ ^` | `~ ~ ~`; `~ ~1 ~`; `~ ~-1 ~` | A 3D position in the world. | `type_position_float.md` |
| Suffixed Value | `number with suffix (e.g., 5s, 10t)` | `5s`; `100t`; `1d` | A value with a unit suffix. | `type_postfixvalue.md` |
| Raw JSON Text | `{"rawtext":[{"text":"..."}]}` | `{"rawtext":[{"text":"Hello World"}]}`; `{"rawtext":[{"translate":"commands.op.success","with":["PlayerName"]}]}`; `{"rawtext":[{"selector":"@p"}]}` | A JSON text component for rich formatting. | `type_rawtext.md` |
| Relative Number | `value or ~offset` | `10`; `~5`; `~-3` | A number that can be relative to current value using ~. | `type_relativefloat.md` |
| RGB Color | `0-255 for each component` | `255 0 0`; `0 255 0`; `0 0 255` | Color value as red, green, blue components. | `type_rgb.md` |
| Rotation Value | `0-360 or ~offset` | `0`; `90`; `180` | A rotation angle in degrees. | `type_rval.md` |
| Entity Selector | `@a, @e, @p, @r, @s, or @e[type=...]` | `@a`; `@e`; `@p` | Targets one or more entities using selector syntax. | `type_selection.md` |
| Slot Number | `0-26 for inventory, 0-8 for hotbar` | `0`; `8`; `26` | Numeric slot index within a slot type. | `type_slotid.md` |
| Equipment Slot Type | `slot.weapon, slot.armor, slot.inventory, etc.` | `slot.weapon.mainhand`; `slot.weapon.offhand`; `slot.armor.head` | Category of inventory or equipment slot. | `type_slottype.md` |
| Text String | `text or "quoted text"` | `MyName`; `"My Name With Spaces"` | A text value. | `type_string.md` |
| Structure Type | `structure_name` | `village`; `stronghold`; `mineshaft` | A structure identifier for locate command. | `type_structuretype.md` |
| Target Selector | `@a, @e, @p, @r, @s` | — | Targets entities or players. | `type_target.md` |
| Time | `ticks or day/night/noon/midnight/sunrise/sunset` | `day`; `night`; `noon` | Time value in ticks or named time. | `type_time.md` |
| Value | — | — | A numeric value. | `type_val.md` |
| Weather Type | `clear, rain, or thunder` | `clear`; `rain`; `thunder` | The weather condition. | `type_weather.md` |
| Pitch Rotation | `-90 to 90, or ~` | — | Vertical rotation (pitch) in degrees. | `type_xrot.md` |
| Yaw Rotation | `-180 to 180, or ~` | — | Horizontal rotation (yaw) in degrees. | `type_yrot.md` |

## 维护备注

- `CommandTypeList.md`中的`Player Selector`链接写作`type_player.selector.md`，实际文件为`type_player_selector.md`。本页已按实际文件解析。
