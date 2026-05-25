# Molang查询函数

本页汇总Molang查询函数。函数名和说明来源于MolangReference。

## 常规查询函数

当前共收录316个常规查询函数。

| 函数 | 说明（官方原文） |
| --- | --- |
| `query.above_top_solid` | Returns the height of the block immediately above the highest solid block at the input (x,z) position |
| `query.actor_count` | Returns the number of entities (actors) rendered in the last frame. |
| `query.all` | Evaluates the first argument, then returns 1.0 if all of the following arguments evaluate to the same value as the first. |
| `query.all_animations_finished` | Returns 1.0 if all animations in the current animation controller state have played through at least once, else it returns 0.0. |
| `query.all_tags` | Returns if the item or block has all of the tags specified. |
| `query.anger_level` | Returns the anger level of the entity [0,n). |
| `query.anim_time` | Returns the time in seconds since the current animation started, else 0.0 if not called within an animation. |
| `query.any` | Evaluates the first argument, then returns 1.0 if any of the following arguments evaluate to the same value as the first. |
| `query.any_animation_finished` | Returns 1.0 if any animation in the current animation controller state has played through at least once, else it returns 0.0. |
| `query.any_tag` | Returns if the item or block has any of the tags specified. |
| `query.approx_eq` | Returns 1.0 if all of the arguments are within the smallest unit of measurement possible for the computer running this query of each other, else 0.0. |
| `query.armor_color_slot` | Takes the armor slot index as a parameter, and returns the color of the armor in the requested slot. |
| `query.armor_damage_slot` | Takes the armor slot index as a parameter, and returns the damage value of the requested slot. |
| `query.armor_material_slot` | Takes the armor slot index as a parameter, and returns the armor material type in the requested armor slot. |
| `query.armor_texture_slot` | Takes the armor slot index as a parameter, and returns the texture type of the requested slot. |
| `query.average_frame_time` | Returns the time in *seconds* of the average frame time over the last 'n' frames. |
| `query.base_swing_duration` | Returns the duration of the mob's swing/attack animation, determined by the carried item and unmodified by effects applied on the mob. |
| `query.block_face` | Returns the block face for this (only valid for certain triggers such as placing blocks, or interacting with block) (Down=0.0, Up=1.0, North=2.0, South=3.0, West=4.0, East=5.0, Undefined=6.0). |
| `query.block_has_all_tags` | Takes a world-origin-relative position and one or more tag names, and returns either 0 or 1 based on if the block at that position has all of the tags provided. |
| `query.block_has_any_tag` | Takes a world-origin-relative position and one or more tag names, and returns either 0 or 1 based on if the block at that position has any of the tags provided. |
| `query.block_neighbor_has_all_tags` | Takes a block-relative position and one or more tag names, and returns either 0 or 1 based on if the block at that position has all of the tags provided. |
| `query.block_neighbor_has_any_tag` | Takes a block-relative position and one or more tag names, and returns either 0 or 1 based on if the block at that position has any of the tags provided. |
| `query.block_property` | Returns the value of the associated block's Block State. |
| `query.block_state` | Returns the value of the associated block's block state. |
| `query.blocking` | Returns 1.0 if the entity is blocking, else it returns 0.0. |
| `query.body_x_rotation` | Returns the body pitch rotation if called on an entity, else it returns 0.0. |
| `query.body_y_rotation` | Returns the body yaw rotation if called on an entity, else it returns 0.0. |
| `query.bone_aabb` | Returns the axis aligned bounding box of a bone as a structure with members '.min', '.max', along with '.x', '.y', and '.z' values for each. |
| `query.bone_orientation_matrix` | Returns the bone orientation (as a matrix) of the desired bone provided it exists in the queryable geometry of the mob, else this returns the identity matrix and throws a content error. |
| `query.bone_orientation_trs` | Returns the bone orientation matrix decomposed into the component translation/rotation/scale (TRS) parts of the desired bone provided it exists in the queryable geometry of the mob, else this returns the identity matrix and throws a content error. |
| `query.bone_origin` | Returns the initial (from the .geo) pivot of a bone as a structure with members '.x', '.y', and '.z'. |
| `query.bone_rotation` | Returns the initial (from the .geo) rotation of a bone as a structure with members '.x', '.y', and '.z' in degrees. |
| `query.camera_distance_range_lerp` | Takes two distances (any order) and return a number from 0 to 1 based on the camera distance between the two ranges clamped to that range. |
| `query.camera_rotation` | Returns the rotation of the camera. |
| `query.can_climb` | Returns 1.0 if the entity can climb, else it returns 0.0. |
| `query.can_damage_nearby_mobs` | Returns 1.0 if the entity can damage nearby mobs, else it returns 0.0. |
| `query.can_dash` | Returns 1.0 if the entity can dash, else it returns 0.0 |
| `query.can_fly` | Returns 1.0 if the entity can fly, else it returns 0.0. |
| `query.can_power_jump` | Returns 1.0 if the entity can power jump, else it returns 0.0. |
| `query.can_swim` | Returns 1.0 if the entity can swim, else it returns 0.0. |
| `query.can_walk` | Returns 1.0 if the entity can walk, else it returns 0.0. |
| `query.cape_flap_amount` | Returns value between 0.0 and 1.0 with 0.0 meaning cape is fully down and 1.0 is cape is fully up. |
| `query.cardinal_block_face_placed_on` | DEPRECATED (please use query.block_face instead) Returns the block face for this (only valid for on_placed_by_player trigger) (Down=0.0, Up=1.0, North=2.0, South=3.0, West=4.0, East=5.0, Undefined=6.0). |
| `query.cardinal_facing` | Returns the current facing of the player (Down=0.0, Up=1.0, North=2.0, South=3.0, West=4.0, East=5.0, Undefined=6.0). |
| `query.cardinal_facing_2d` | Returns the current facing of the player ignoring up/down part of the direction (North=2.0, South=3.0, West=4.0, East=5.0, Undefined=6.0). |
| `query.cardinal_player_facing` | Returns the current facing of the player (Down=0.0, Up=1.0, North=2.0, South=3.0, West=4.0, East=5.0, Undefined=6.0). |
| `query.client_max_render_distance` | Returns the max render distance in chunks of the current client. |
| `query.client_memory_tier` | Returns a number representing the client RAM memory tier, 0 = 'SuperLow', 1 = 'Low', 2 = 'Mid', 3 = 'High', or 4 = 'SuperHigh'. |
| `query.combine_entities` | Combines any valid entity references from all arguments into a single array. |
| `query.cooldown_time` | Returns the total cooldown time in seconds for the item held or worn by the specified equipment slot name (and if required second numerical slot id), otherwise returns 0. |
| `query.cooldown_time_remaining` | Returns the cooldown time remaining in seconds for specified cooldown type or the item held or worn by the specified equipment slot name (and if required second numerical slot id), otherwise returns 0. |
| `query.count` | Counts the number of things passed to it (arrays are counted as the number of elements they contain; non-arrays count as 1). |
| `query.current_squish_value` | Returns the squish value for the current entity, or 0.0 if this doesn't make sense. |
| `query.dash_cooldown_progress` | DEPRECATED. DO NOT USE AFTER 1.20.40. Please see camel.entity.json script.pre_animation for example of how to now process dash cooldown. Returns dash cooldown progress if the entity can dash, else it returns 0.0. |
| `query.day` | Returns the day of the current world. |
| `query.death_ticks` | Returns the elapsed ticks since the mob started dying. |
| `query.debug_output` | debug log a value to the output debug window for builds that have one |
| `query.delta_time` | Returns the time in seconds since the previous frame. |
| `query.distance_from_camera` | Returns the distance of the root of this entity or particle emitter from the camera. |
| `query.effect_emitter_count` | Returns the total number of active emitters of the callee's particle effect type. |
| `query.effect_particle_count` | Returns the total number of active particles of the callee's particle effect type. |
| `query.entity_biome_has_all_tags` | Compares the biome the entity is standing in with one or more tag names, and returns either 0 or 1 based on if all of the tag names match. |
| `query.entity_biome_has_any_identifier` | Compares the biome the entity is standing in with one or more identifier names, and returns either 0 or 1 based on if any of the identifier names match. |
| `query.entity_biome_has_any_tags` | Compares the biome the entity is standing in with one or more tag names, and returns either 0 or 1 based on if any of the tag names match. |
| `query.equipment_count` | Returns the number of equipped armor pieces for an entity from 0 to 5, not counting items held in hands. |
| `query.equipped_item_all_tags` | Takes a slot name followed by any tag you want to check for in the form of 'tag_name' and returns 1 if all of the tags are on that equipped item, 0 otherwise. |
| `query.equipped_item_any_tag` | Takes a slot name followed by any tag you want to check for in the form of 'tag_name' and returns 0 if none of the tags are on that equipped item or 1 if at least 1 tag exists. |
| `query.equipped_item_is_attachable` | Takes the desired hand slot as a parameter (0 or 'main_hand' for main hand, 1 or 'off_hand' for off hand), and returns whether the item is an attachable or not. |
| `query.eye_target_x_rotation` | Returns the X eye rotation of the entity, else it returns 0.0. |
| `query.eye_target_y_rotation` | Returns the Y eye rotation of the entity, else it returns 0.0. |
| `query.facing_target_to_range_attack` | Returns 1.0 if the entity is attacking from range (i.e. |
| `query.frame_alpha` | Returns the ratio (from 0 to 1) of how much between AI ticks this frame is being rendered. |
| `query.fuse_time` | Returns the remaining fuse time of the entity. |
| `query.get_actor_info_id` | Returns the integer id of an entity (actor) by its string name. |
| `query.get_animation_frame` | Returns the current texture of an item whose appearance can change (such as a drawn bow). |
| `query.get_default_bone_pivot` | Gets specified axis of the specified bone orientation pivot. |
| `query.get_equipped_item_name` | DEPRECATED (Use query.is_item_name_any instead if possible so names can be changed later without breaking content.) Takes one optional hand slot as a parameter (0 or 'main_hand' for main hand, 1 or 'off_hand' for off hand), and a second parameter (0=default) if you would like the equipped item or any non-zero number for the currently rendered item, and returns the name of the item in the requested slot (defaulting to the main hand if no parameter is supplied) if there is one, otherwise returns ''. |
| `query.get_level_seed_based_fraction` | Returns a value in range [0.0, 1.0] based on the level seed. |
| `query.get_locator_offset` | Gets specified axis of the specified locator offset. |
| `query.get_name` | DEPRECATED (Use query.is_name_any instead if possible so names can be changed later without breaking content.) Get the name of the mob if there is one, otherwise return ''. |
| `query.get_pack_setting` | Returns value of Pack Setting slider, parameter is name of slider. |
| `query.get_root_locator_offset` | Gets specified axis of the specified locator offset of the root model. |
| `query.graphics_mode_is_any` | If the graphics mode of the client matches any of the arguments, return 1.0. |
| `query.ground_speed` | Returns the ground speed of the entity in meters/second. |
| `query.had_component_group` | If the entity is being loaded from data that was last saved with a component_group with the specified name, returns 1.0, otherwise returns 0.0. |
| `query.has_any_family` | Returns 1 if the entity has any of the specified type families, else 0. |
| `query.has_any_leashed_entity_of_type` | Returns whether or not the entity is currently leashing other entities of the designated types. |
| `query.has_armor_slot` | Takes the armor slot index as a parameter, and returns 1.0 if the entity has armor in the requested slot, else it returns 0.0. |
| `query.has_biome_tag` | Returns whether or not a block placement target has a specific biome tag. |
| `query.has_block_property` | Returns 1.0 if the associated block has the given block state or 0.0 if not. |
| `query.has_block_state` | Returns 1.0 if the associated block has the given block state or 0.0 if not. |
| `query.has_cape` | Returns 1.0 if the player has a cape, else it returns 0.0. |
| `query.has_collision` | Returns 1.0 if the entity has collisions enabled, else it returns 0.0. |
| `query.has_dash_cooldown` | Returns 1.0 if the entity has cooldown on its dash, else it returns 0.0 |
| `query.has_gravity` | Returns 1.0 if the entity is affected by gravity, else it returns 0.0. |
| `query.has_head_gear` | Returns boolean whether an entity has an item in their head armor slot or not, or false if no entity in current context |
| `query.has_owner` | Returns true if the entity has an owner ID else it returns false. |
| `query.has_player_rider` | Returns 1 if the entity has a player riding it in any seat, else it returns 0. |
| `query.has_property` | Returns 1.0 if a property with the given name exists, 0 otherwise. |
| `query.has_rider` | Returns 1.0 if the entity has a rider, else it returns 0.0 |
| `query.has_target` | Returns 1.0 if the entity has a target, else it returns 0.0 |
| `query.head_roll_angle` | Returns the roll angle of the head of the entity if it makes sense, else it returns 0.0. |
| `query.head_x_rotation` | Returns the nth head x rotation of the entity if it makes sense, else it returns 0.0. |
| `query.head_y_rotation` | Returns the nth head y rotation of the entity if it makes sense, else it returns 0.0. |
| `query.health` | Returns the health of the entity, or 0.0 if it doesn't make sense to call on this entity. |
| `query.heartbeat_interval` | Returns the heartbeat interval of the entity in seconds. |
| `query.heartbeat_phase` | Returns the heartbeat phase of the entity. |
| `query.heightmap` | Returns the world height (Y value) of the terrain at the specified position. |
| `query.hurt_direction` | Returns the hurt direction for the entity, otherwise returns 0. |
| `query.hurt_time` | Returns the hurt time for the entity, otherwise returns 0. |
| `query.in_range` | If the first argument is between the minimum and maximum (inclusive), returns 1.0. |
| `query.invulnerable_ticks` | Returns the number of ticks of invulnerability the entity has left if it makes sense, else it returns 0.0. |
| `query.is_admiring` | Returns 1.0 if the entity is admiring, else it returns 0.0. |
| `query.is_alive` | Returns 1.0 if the entity is alive, and 0.0 if it's dead. |
| `query.is_angry` | Returns 1.0 if the entity is angry, else it returns 0.0. |
| `query.is_attached` | Returns 1.0 if the entity is attached to another entity (such as being held or worn), else it will return 0.0. |
| `query.is_attached_to_entity` | Returns 1.0 if the entity is attached to another entity, else it will return 0.0. |
| `query.is_avoiding_block` | Returns 1.0 if the entity is fleeing from a block, else it returns 0.0. |
| `query.is_avoiding_mobs` | Returns 1.0 if the entity is fleeing from mobs, else it returns 0.0. |
| `query.is_baby` | Returns 1.0 if the entity has a `is_baby` component, else it returns 0.0. |
| `query.is_breathing` | Returns 1.0 if the entity is breathing, else it returns 0.0. |
| `query.is_bribed` | Returns 1.0 if the entity has been bribed, else it returns 0.0. |
| `query.is_carrying_block` | Returns 1.0 if the entity is carrying a block, else it returns 0.0. |
| `query.is_casting` | Returns 1.0 if the entity is casting, else it returns 0.0. |
| `query.is_celebrating` | Returns 1.0 if the entity is celebrating, else it returns 0.0. |
| `query.is_celebrating_special` | Returns 1.0 if the entity is doing a special celebration, else it returns 0.0. |
| `query.is_charged` | Returns 1.0 if the entity has the `is_charged` component, else it returns 0.0. |
| `query.is_charging` | Returns 1.0 if the entity is charging, else it returns 0.0. |
| `query.is_chested` | Returns 1.0 if the entity has chests attached to it (has the `is_chested` component), else it returns 0.0. |
| `query.is_cooldown_category` | Returns 1.0 if the specified held or worn item has the specified cooldown category, otherwise returns 0.0. |
| `query.is_crawling` | Returns 1.0 if the entity is crawling, else it returns 0.0 |
| `query.is_critical` | Returns 1.0 if the entity is at a critical level of damage, else it returns 0.0. |
| `query.is_croaking` | Returns 1.0 if the entity is croaking, else it returns 0.0. |
| `query.is_dancing` | Returns 1.0 if the entity is dancing, else it returns 0.0. |
| `query.is_delayed_attacking` | Returns 1.0 if the entity is attacking using the delayed attack, else it returns 0.0. |
| `query.is_digging` | Returns 1.0 if the entity is digging, else it returns 0.0. |
| `query.is_eating` | Returns 1.0 if the entity is eating, else it returns 0.0. |
| `query.is_eating_mob` | Returns 1.0 if the entity is eating a mob, else it returns 0.0. |
| `query.is_elder` | Returns 1.0 if the entity is an elder version of it, else it returns 0.0. |
| `query.is_emerging` | Returns 1.0 if the entity is emerging, else it returns 0.0. |
| `query.is_emoting` | Returns 1.0 if the entity is emoting, else it returns 0.0. |
| `query.is_enchanted` | Returns 1.0 if the entity is enchanted, else it returns 0.0. |
| `query.is_feeling_happy` | DEPRECATED after 1.20.40. Returns 1.0 if behavior.timer_flag_2 is running, else it returns 0.0. |
| `query.is_fire_immune` | Returns 1.0 if the entity is immune to fire (has the `fire_immune` component), else it returns 0.0. |
| `query.is_first_person` | Returns 1.0 if the entity is being rendered in first person mode, else it returns 0.0. |
| `query.is_ghost` | Returns 1.0 if an entity is a ghost, else it returns 0.0. |
| `query.is_gliding` | Returns 1.0 if the entity is gliding, else it returns 0.0. |
| `query.is_grazing` | Returns 1.0 if the entity is grazing, or 0.0 if not. |
| `query.is_idling` | Returns 1.0 if the entity is idling, else it returns 0.0. |
| `query.is_ignited` | Returns 1.0 if the entity is ignited (has the `is_ignited` component), else it returns 0.0. |
| `query.is_illager_captain` | Returns 1.0 if the entity is an illager captain (has the `is_illager_captain` component), else it returns 0.0. |
| `query.is_in_contact_with_water` | Returns 1.0 if the entity is in contact with any water (water, rain, splash water bottle), else it returns 0.0. |
| `query.is_in_lava` | Returns 1.0 if the entity is in lava, else it returns 0.0. |
| `query.is_in_love` | Returns 1.0 if the entity is in love (has a love-hearts animation), else it returns 0.0. |
| `query.is_in_ui` | Returns 1.0 if the entity is rendered as part of the UI, else it returns 0.0. |
| `query.is_in_water` | Returns 1.0 if the entity is in water, else it returns 0.0. |
| `query.is_in_water_or_rain` | Returns 1.0 if the entity is in water or rain, else it returns 0.0. |
| `query.is_interested` | Returns 1.0 if the entity is interested, else it returns 0.0. |
| `query.is_invisible` | Returns 1.0 if the entity is invisible (using render controllers), else it returns 0.0. |
| `query.is_item_equipped` | Takes one optional hand slot as a parameter (0 or 'main_hand' for main hand, 1 or 'off_hand' for off hand), and returns 1.0 if there is an item in the requested slot (defaulting to the main hand if no parameter is supplied), otherwise returns 0.0. |
| `query.is_item_name_any` | Returns 1.0 if an item in the specified slot has any of the specified names, otherwise returns 0.0. |
| `query.is_jump_goal_jumping` | Returns 1.0 if the entity is doing a jump goal jump, else it returns 0.0. |
| `query.is_jumping` | Returns 1.0 if the entity is jumping, else it returns 0.0. |
| `query.is_laying_down` | Returns 1.0 if the entity is laying down, else it returns 0.0. |
| `query.is_laying_egg` | Returns 1.0 if the entity is laying an egg, else it returns 0.0. |
| `query.is_leashed` | Returns 1.0 if the entity is leashed to something, else it returns 0.0. |
| `query.is_levitating` | Returns 1.0 if the entity is levitating, else it returns 0.0. |
| `query.is_lingering` | Returns 1.0 if the potion type or effect is lingering, else it returns 0.0. |
| `query.is_local_player` | Returns 1.0 if the entity is the local player for the current game window, else it returns 0.0. |
| `query.is_moving` | Returns 1.0 if the entity is moving, else it returns 0.0. |
| `query.is_name_any` | Takes one or more arguments. |
| `query.is_on_fire` | Returns 1.0 if the entity is on fire, else it returns 0.0. |
| `query.is_on_ground` | Returns 1.0 if the entity is on the ground, else it returns 0.0. |
| `query.is_on_screen` | Returns 1.0 if this is called on an entity at a time when it is known if it is on screen, else it returns 0.0. |
| `query.is_onfire` | Returns 1.0 if the entity is on fire, else it returns 0.0. |
| `query.is_orphaned` | Returns 1.0 if the entity is orphaned, else it returns 0.0. |
| `query.is_owner_identifier_any` | Returns whether the root entity identifier is any of the specified strings. |
| `query.is_pack_setting_enabled` | Returns 1.0 if the Pack Setting toggle is enabled, parameter is name of toggle. |
| `query.is_pack_setting_selected` | Returns 1.0 if the Pack Setting dropdown (first parameter) matches the string value of the second parameter (selection). |
| `query.is_persona_or_premium_skin` | Returns 1.0 if the player has a persona or premium skin, else it returns 0.0. |
| `query.is_playing_dead` | Returns 1.0 if the entity is playing dead, else it returns 0.0. |
| `query.is_powered` | Returns 1.0 if the entity is powered, else it returns 0.0. |
| `query.is_pregnant` | Returns 1.0 if the entity is pregnant, else it returns 0.0. |
| `query.is_ram_attacking` | Returns 1.0 if the entity is using a ram attack, else it returns 0.0. |
| `query.is_resting` | Returns 1.0 if the entity is resting, else it returns 0.0. |
| `query.is_riding` | Returns 1.0 if the entity is riding, else it returns 0.0. |
| `query.is_riding_any_entity_of_type` | Returns whether or not the entity is currently riding an entity of any of the designated types. |
| `query.is_rising` | Returns 1.0 if behavior.timer_flag_2 is running, else it returns 0.0. |
| `query.is_roaring` | Returns 1.0 if the entity is currently roaring, else it returns 0.0. |
| `query.is_rolling` | Returns 1.0 if the entity is rolling, else it returns 0.0. |
| `query.is_saddled` | Returns 1.0 if the entity has a saddle (has the `is_saddled` component), else it returns 0.0. |
| `query.is_scared` | Returns 1.0 if the entity is scared, else it returns 0.0. |
| `query.is_scenting` | Returns 1.0 if behavior.timer_flag_1 is running, else it returns 0.0. |
| `query.is_searching` | Returns 1.0 if the entity is searching, else it returns 0.0. |
| `query.is_selected_item` | Returns true if the player has selected an item in the inventory, else it returns 0.0. |
| `query.is_shaking` | Returns 1.0 if the entity is shaking, else it returns 0.0. |
| `query.is_shaking_wetness` | Returns 1.0 if the entity is shaking water off, else it returns 0.0. |
| `query.is_sheared` | Returns 1.0 if the entity is able to be sheared and is sheared, else it returns 0.0. |
| `query.is_shield_powered` | Returns 1.0 if the entity has an active powered shield if it makes sense, else it returns 0.0. |
| `query.is_silent` | Returns 1.0 if the entity is silent, else it returns 0.0. |
| `query.is_sitting` | Returns 1.0 if the entity is sitting, else it returns 0.0. |
| `query.is_sleeping` | Returns 1.0 if the entity is sleeping, else it returns 0.0. |
| `query.is_sneaking` | Returns 1.0 if the entity is sneaking, else it returns 0.0. |
| `query.is_sneezing` | Returns 1.0 if the entity is sneezing, else it returns 0.0. |
| `query.is_sniffing` | Returns 1.0 if the entity is sniffing, else it returns 0.0. |
| `query.is_sonic_boom` | Returns 1.0 if the entity is using sonic boom, else it returns 0.0. |
| `query.is_spectator` | Returns 1.0 if the entity (player) is in spectator mode, else it returns 0.0. |
| `query.is_sprinting` | Returns 1.0 if the entity is sprinting, else it returns 0.0. |
| `query.is_stackable` | Returns 1.0 if the entity is stackable (has the `is_stackable` component), else it returns 0.0. |
| `query.is_stalking` | Returns 1.0 if the entity is stalking, else it returns 0.0. |
| `query.is_standing` | Returns 1.0 if the entity is standing, else it returns 0.0. |
| `query.is_stunned` | Returns 1.0 if the entity is currently stunned, else it returns 0.0. |
| `query.is_swimming` | Returns 1.0 if the entity is swimming, else it returns 0.0. |
| `query.is_tamed` | Returns 1.0 if the entity is tamed, else it returns 0.0. |
| `query.is_transforming` | Returns 1.0 if the entity is transforming, else it returns 0.0. |
| `query.is_using_item` | Returns 1.0 if the entity is using an item, else it returns 0.0. |
| `query.is_wall_climbing` | Returns 1.0 if the entity is climbing a wall, else it returns 0.0. |
| `query.item_in_use_duration` | Returns the amount of time an item has been in use in seconds up to the maximum duration, else 0.0 if it doesn't make sense. |
| `query.item_is_charged` | Takes one optional hand slot as a parameter (0 or 'main_hand' for main hand, 1 or 'off_hand' for off hand), and returns 1.0 if the item is charged in the requested slot (defaulting to the main hand if no parameter is supplied), otherwise returns 0.0. |
| `query.item_max_use_duration` | Returns the maximum amount of time the item can be used, else 0.0 if it doesn't make sense. |
| `query.item_remaining_use_duration` | Returns the amount of time an item has left to use, else 0.0 if it doesn't make sense. |
| `query.item_slot_to_bone_name` | This function returns the name of the bone this entity has mapped to that slot. |
| `query.key_frame_lerp_time` | Returns the ratio between the previous and next key frames. |
| `query.kinetic_weapon_damage_duration` | Returns the "max_duration" value of "damage_conditions" from the main-hand item's "minecraft:kinetic_weapon" component, or 0 if the component is not present. |
| `query.kinetic_weapon_delay` | Returns the "delay" value from the main-hand item's "minecraft:kinetic_weapon" component, or 0 if the component is not present. |
| `query.kinetic_weapon_dismount_duration` | Returns the "max_duration" value of "dismount_conditions" from the main-hand item's "minecraft:kinetic_weapon" component, or 0 if the component is not present. |
| `query.kinetic_weapon_knockback_duration` | Returns the "max_duration" value of "knockback_conditions" from the main-hand item's "minecraft:kinetic_weapon" component, or 0 if the component is not present. |
| `query.last_frame_time` | Returns the time in *seconds* of the last frame. |
| `query.last_hit_by_player` | Returns 1.0 if the entity was last hit by the player, else it returns 0.0. |
| `query.last_input_mode_is_any` | Takes one or more arguments ('keyboard_and_mouse', 'touch', or 'gamepad'). |
| `query.leashed_entity_count` | Returns the number of entities for which this entity is the leash holder. |
| `query.lie_amount` | Returns the lie down amount for the entity. |
| `query.life_span` | Returns the limited life span of an entity, or 0.0 if it lives forever. |
| `query.life_time` | Returns the time in seconds since the current animation started, else 0.0 if not called within an animation. |
| `query.lod_index` | Takes an array of distances and returns the zero-based index of which range the actor is in based on distance from the camera. For example, 'query.lod_index(10, 20, 30)' will return 0, 1, or 2 based on whether the mob is less than 10, 20, or 30 units away from the camera, or it will return 3 if it is greater than 30. |
| `query.log` | Debug log a value to the content file. |
| `query.main_hand_item_max_duration` | Returns the use time maximum duration for the main hand item if it makes sense, else it returns 0.0. |
| `query.main_hand_item_use_duration` | Returns the use time for the main hand item. |
| `query.mark_variant` | Returns the entity's mark variant value, if the entity has the `mark_variant` component. |
| `query.max_durability` | Returns the max durability an item can take. |
| `query.max_health` | Returns the maximum health of the entity, or 0.0 if it doesn't make sense to call on this entity. |
| `query.max_trade_tier` | Returns the maximum trade tier of the entity if it can perform trades, else it returns 0.0 |
| `query.maximum_frame_time` | Returns the time in *seconds* of the most expensive frame over the last 'n' frames. |
| `query.minimum_frame_time` | Returns the time in *seconds* of the least expensive frame over the last 'n' frames. |
| `query.model_scale` | Returns the scale of the current entity. |
| `query.modified_distance_moved` | Returns the total distance the entity has moved horizontally in meters (since the entity was last loaded, not necessarily since it was originally created). |
| `query.modified_move_speed` | Returns the current walk speed of the entity. |
| `query.modified_swing_duration` | Returns the duration of the mob's swing/attack animation, determined by the carried item and modified by effects applied on the mob. |
| `query.moon_brightness` | Returns the brightness of the moon (FULL_MOON=1.0, WANING_GIBBOUS=0.75, FIRST_QUARTER=0.5, WANING_CRESCENT=0.25, NEW_MOON=0.0, WAXING_CRESCENT=0.25, LAST_QUARTER=0.5, WAXING_GIBBOUS=0.75). |
| `query.moon_phase` | Returns the phase of the moon (FULL_MOON=0, WANING_GIBBOUS=1, FIRST_QUARTER=2, WANING_CRESCENT=3, NEW_MOON=4, WAXING_CRESCENT=5, LAST_QUARTER=6, WAXING_GIBBOUS=7). |
| `query.movement_direction` | Returns the specified axis of the normalized position delta of the entity. |
| `query.noise` | Queries a Perlin Noise Map. |
| `query.on_fire_time` | Returns the time that the entity is on fire, else it returns 0.0. |
| `query.out_of_control` | Returns 1.0 if the entity is out of control (has the `out_of_control` component), else it returns 0.0. |
| `query.overlay_alpha` | DEPRECATED (Do not use - this function is deprecated and will be removed). |
| `query.owner_identifier` | DEPRECATED (Use query.is_owner_identifier_any instead if possible so names can be changed later without breaking content.) Returns the root actor identifier. |
| `query.player_level` | Returns the players level if the entity is a player, otherwise returns 0. |
| `query.position` | Returns the absolute position of an entity. |
| `query.position_delta` | Returns the position delta for an entity. |
| `query.previous_squish_value` | Returns the previous squish value for the current entity, or 0.0 if this doesn't make sense. |
| `query.property` | Returns the value of that property if it exists, else 0.0 if not. |
| `query.relative_block_has_all_tags` | Takes an entity-relative position and one or more tag names, and returns either 0 or 1 based on if the block at that position has all of the tags provided. |
| `query.relative_block_has_any_tag` | Takes an entity-relative position and one or more tag names, and returns either 0 or 1 based on if the block at that position has any of the tags provided. |
| `query.remaining_durability` | Returns how much durability an item has remaining. |
| `query.ride_body_x_rotation` | Returns the body pitch world-rotation of the ride an entity, else it returns 0.0. |
| `query.ride_body_y_rotation` | Returns the body yaw world-rotation of the ride of on an entity, else it returns 0.0. |
| `query.ride_head_x_rotation` | Returns the head x world-rotation of the ride of an entity, else it returns 0.0. |
| `query.ride_head_y_rotation` | Returns the head y world-rotation of the ride of an entity, else it returns 0.0. |
| `query.rider_body_x_rotation` | Returns the body pitch world-rotation of a valid rider at the provided index if called on an entity, else it returns 0.0. |
| `query.rider_body_y_rotation` | Returns the body yaw world-rotation of a valid rider at the provided index if called on an entity, else it returns 0.0. |
| `query.rider_head_x_rotation` | Returns the head x world-rotation of the rider entity at the provided index, else it returns 0.0. |
| `query.rider_head_y_rotation` | Returns the head y world-rotation of the rider entity at the provided index, else it returns 0.0. |
| `query.roll_counter` | Returns the roll counter of the entity. |
| `query.rotation_to_camera` | Returns the rotation required to aim at the camera. |
| `query.scoreboard` | Returns the specified scoreboard value for this entity. |
| `query.server_memory_tier` | Returns a number representing the server RAM memory tier, 0 = 'SuperLow', 1 = 'Low', 2 = 'Mid', 3 = 'High', or 4 = 'SuperHigh'. |
| `query.shake_angle` | Returns the shaking angle of the entity if it makes sense, else it returns 0.0. |
| `query.shake_time` | Returns the shake time of the entity. |
| `query.shield_blocking_bob` | Returns the how much the offhand shield should translate down when blocking and being hit. |
| `query.show_bottom` | Returns 1.0 if we render the entity's bottom, else it returns 0.0. |
| `query.sit_amount` | Returns the current sit amount of the entity. |
| `query.skin_id` | Returns the entity's skin ID (related to the `skin_id` component). |
| `query.sleep_rotation` | Returns the rotation of the bed the player is sleeping on. |
| `query.sneeze_counter` | Returns the sneeze counter of the entity. |
| `query.spellcolor` | Returns a struct representing the entity spell color for the specified entity. |
| `query.standing_scale` | Returns the scale of how standing up the entity is. |
| `query.state_time` | Returns the time in seconds in the current animation controller state. |
| `query.structural_integrity` | Returns the structural integrity for the entity, otherwise returns 0. |
| `query.surface_particle_color` | Returns the particle color for the block located in the surface below the entity (scanned up to 10 blocks down). |
| `query.surface_particle_texture_coordinate` | Returns the texture coordinate for generating particles for the block located in the surface below the entity (scanned up to 10 blocks down) in a structure with 'u' and 'v' keys. |
| `query.surface_particle_texture_size` | Returns the texture size for generating particles for the block located in the surface below the entity (scanned up to 10 blocks down). |
| `query.swell_amount` | Returns how swollen an entity is. |
| `query.swelling_dir` | Returns the swelling direction of the entity if it makes sense, else it returns 0.0. |
| `query.swim_amount` | Returns the amount the current entity is swimming. |
| `query.tail_angle` | Returns the angle of the tail of the entity if it makes sense, else it returns 0.0. |
| `query.target_x_rotation` | Returns the x rotation required to aim at the entity's current target if it has one, else it returns 0.0. |
| `query.target_y_rotation` | Returns the y rotation required to aim at the entity's current target if it has one, else it returns 0.0. |
| `query.texture_frame_index` | Returns the icon index of the experience orb. |
| `query.ticks_since_last_kinetic_weapon_hit` | Returns the number of ticks elapsed since the user last hit something while using a kinetic weapon. |
| `query.time_of_day` | Returns the time of day (midnight=0.0, sunrise=0.25, noon=0.5, sunset=0.75) of the dimension the entity is in. |
| `query.time_since_last_vibration_detection` | Returns the time in seconds since the last vibration detected by the entity. |
| `query.time_stamp` | Returns the current time stamp of the level. |
| `query.timer_flag_1` | Returns 1.0 if behavior.timer_flag_1 is running, else it returns 0.0. |
| `query.timer_flag_2` | Returns 1.0 if behavior.timer_flag_2 is running, else it returns 0.0. |
| `query.timer_flag_3` | Returns 1.0 if behavior.timer_flag_3 is running, else it returns 0.0. |
| `query.total_emitter_count` | Returns the total number of active emitters in the world. |
| `query.total_particle_count` | Returns the total number of active particles in the world. |
| `query.touch_only_affects_hotbar` | Returns 1.0 if the touch input only affects the touchbar, otherwise returns 0.0. |
| `query.trade_tier` | Returns the trade tier of the entity if it makes sense, else it returns 0.0. |
| `query.unhappy_counter` | Always returns zero. (Was originally meant to indicate Panda unhappiness but due to an early code change it has always only returned zero) |
| `query.variant` | Returns the entity's variant index. |
| `query.vertical_speed` | Returns the speed of the entity up or down in meters/second, where positive is up. |
| `query.walk_distance` | Returns the total distance traveled by an entity while on the ground and not sneaking. |
| `query.wing_flap_position` | Returns the wing flap position of the entity, or 0.0 if this doesn't make sense. |
| `query.wing_flap_speed` | Returns the wing flap speed of the entity, or 0.0 if this doesn't make sense. |
| `query.yaw_speed` | Returns the entity's yaw speed. |

## 内部或已弃用查询函数

当前共收录11个内部或已弃用查询函数。

| 函数 | 说明（官方原文） |
| --- | --- |
| `query_block_property` | Returns the value of the associated block's block state. |
| `query_cardinal_block_face_placed_on` | Returns the block face for this (only valid for on_placed_by_player trigger) (Down=0.0, Up=1.0, North=2.0, South=3.0, West=4.0, East=5.0, Undefined=6.0). |
| `query_dash_cooldown_progress` | Returns dash cooldown progress if the entity can dash, else it returns 0.0. |
| `query_debug_output` | Debug log a value to the output debug window for builds that have one. |
| `query_get_equipped_item_name` | Takes one optional hand slot as a parameter (0 or 'main_hand' for main hand, 1 or 'off_hand' for off hand), and a second parameter (0=default) if you would like the equipped item or any non-zero number for the currently rendered item, and returns the name of the item in the requested slot (defaulting to the main hand if no parameter is supplied) if there is one, otherwise returns ''. |
| `query_get_name` | Get the name of the mob if there is one, otherwise return ''. |
| `query_has_block_property` | Returns 1.0 if the associated block has the given block state or 0.0 if not. |
| `query_is_feeling_happy` | Returns 1.0 if behavior.timer_flag_2 is running, else it returns 0.0. |
| `query_overlay_alpha` | Deprecated; this function is deprecated and will be removed. |
| `query_owner_identifier` | Returns the root entity identifier. |
| `query_unhappy_counter` | Always returns zero. |

## 相关参考

- [Molang](../../docs/general/molang.md)
- [Molang数学函数](molang-math-function.md)