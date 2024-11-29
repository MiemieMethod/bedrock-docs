# Entity Behavior

> 文档版本：1.21.50.25

The minecraft entity behavior specification.

## 架构

```mcschema
entities:
{
  format_version "format_version"
  minecraft:entity "minecraft:entity"
}

```

/// html | div.result
//// define
`format_version`：<samp>format_version</samp> {#assets.schemas-blockception.general.format_version.json}


////

```mcschema
format_version:
string

```

//// html | div.result

////



//// define
`minecraft:entity`：<samp>minecraft:entity</samp> {#assets.schemas-blockception.behavior.entities.format.minecraft.entity.json}


////

```mcschema
minecraft:entity:
{
  object "description" : opt
  {
    object "animations" : opt
    {
      string "<any object property>" : opt
    }
    identifier "identifier"
    boolean "is_spawnable" : opt
    boolean "is_summonable" : opt
    boolean "is_experimental" : opt
    object "properties" : opt
    {
      object "<any object property>" : opt
      {
         "type" : opt
        0 "default"
      }
      object "<any object property>" : opt
      {
         "type" : opt
        0 "default"
        array "range" : opt
        {
          integer "0..0" : opt
          integer "1..1" : opt
        }
      }
      object "<any object property>" : opt
      {
         "type" : opt
        0 "default"
        array "range" : opt
        {
          number "0..0" : opt
          number "1..1" : opt
        }
      }
      object "<any object property>" : opt
      {
         "type" : opt
        string "default" : opt
        boolean "client_sync" : opt
        array "values" : opt
        {
          string "<any array element>" : opt
        }
      }
    }
    string "runtime_identifier" : opt
    object "scripts" : opt
    {
      array "animate" : opt
      {
        string "<any array element>" : opt
        object "<any array element>" : opt
        {
          string "<any object property>" : opt
        }
      }
    }
    string "spawn_category" : opt
  }
  object "component_groups" : opt
  {
    components "<any object property>"
  }
  components "components"
  events "events"
}

```

//// html | div.result
///// define
`description`：<samp>object</samp>

- The description of the this entity.


/////

<div class="language-text highlight"><span class="filename"><code>description</code></span><pre id="__code_1"><span></span></pre></div>

///// html | div.result
////// define
`animations`：<samp>object</samp>

- Sets the mapping of internal animation / animation controllers references to actual animations. This is a JSON Object of name/animation pairs


//////

<div class="language-text highlight"><span class="filename"><code>animations</code></span><pre id="__code_1"><span></span></pre></div>

////// html | div.result
/////// define
`<any object property>`：<samp>string</samp>

- The name of the animation controller / animation.


///////


//////


////// define
`identifier`：<samp>identifier</samp> {#assets.schemas-blockception.general.entity.identifier.json}

- Sets the identifier for this entity's description.


//////

```mcschema
identifier:
string

```

////// html | div.result

//////



////// define
`is_spawnable`：<samp>boolean</samp>

- Sets whether or not this entity has a spawn egg in the creative ui.


//////


////// define
`is_summonable`：<samp>boolean</samp>

- Sets whether or not we can summon this entity using commands such as /summon.


//////


////// define
`is_experimental`：<samp>boolean</samp>

- Sets whether or not this entity is experimental. Experimental entities are only enabled when the experimental toggle is enabled.


//////


////// define
`properties`：<samp>object</samp>

- Experimental


//////

<div class="language-text highlight"><span class="filename"><code>properties</code></span><pre id="__code_1"><span></span></pre></div>

////// html | div.result
/////// define
`<any object property>`：<samp>object</samp>


///////

<div class="language-text highlight"><span class="filename"><code>&lt;any object property&gt;</code></span><pre id="__code_1"><span></span></pre></div>

/////// html | div.result
//////// define
`type`


////////


//////// define
`default`：<samp>0</samp> {#assets.schemas-blockception.molang.boolean.json}

- The default value of the property.


////////

```mcschema
0:
string

```

//////// html | div.result

////////


```mcschema
0:
boolean

```

//////// html | div.result

////////




///////


/////// define
`<any object property>`：<samp>object</samp>


///////

<div class="language-text highlight"><span class="filename"><code>&lt;any object property&gt;</code></span><pre id="__code_1"><span></span></pre></div>

/////// html | div.result
//////// define
`type`


////////


//////// define
`default`：<samp>0</samp> {#assets.schemas-blockception.molang.number.json}

- The default value of the property.


////////

```mcschema
0:
string

```

//////// html | div.result

////////


```mcschema
0:
number

```

//////// html | div.result

////////




//////// define
`range`：<samp>array</samp>

- The range of the property.


////////

<div class="language-text highlight"><span class="filename"><code>range</code></span><pre id="__code_1"><span></span></pre></div>

//////// html | div.result
///////// define
`0..0`：<samp>integer</samp>

- The minimum value of the property.


/////////


///////// define
`1..1`：<samp>integer</samp>

- The minimum value of the property.


/////////


////////


///////


/////// define
`<any object property>`：<samp>object</samp>


///////

<div class="language-text highlight"><span class="filename"><code>&lt;any object property&gt;</code></span><pre id="__code_1"><span></span></pre></div>

/////// html | div.result
//////// define
`type`


////////


//////// define
`default`：<samp>[0](#assets.schemas-blockception.molang.number.json)</samp>

- The default value of the property.


////////


//////// define
`range`：<samp>array</samp>

- The range of the property.


////////

<div class="language-text highlight"><span class="filename"><code>range</code></span><pre id="__code_1"><span></span></pre></div>

//////// html | div.result
///////// define
`0..0`：<samp>number</samp>

- The minimum value of the property.


/////////


///////// define
`1..1`：<samp>number</samp>

- The minimum value of the property.


/////////


////////


///////


/////// define
`<any object property>`：<samp>object</samp>


///////

<div class="language-text highlight"><span class="filename"><code>&lt;any object property&gt;</code></span><pre id="__code_1"><span></span></pre></div>

/////// html | div.result
//////// define
`type`


////////


//////// define
`default`：<samp>string</samp>


////////


//////// define
`client_sync`：<samp>boolean</samp>

- Sets whether or not the property is synced to the client.


////////


//////// define
`values`：<samp>array</samp>

- The values of the property.


////////

<div class="language-text highlight"><span class="filename"><code>values</code></span><pre id="__code_1"><span></span></pre></div>

//////// html | div.result
///////// define
`<any array element>`：<samp>string</samp>


/////////


////////


///////



//////


////// define
`runtime_identifier`：<samp>string</samp>

- Sets the name for the Vanilla Minecraft identifier this entity will use to build itself from.


//////


////// define
`scripts`：<samp>object</samp>

- Sets the mapping of internal animation controller references to actual animation controller. This is a JSON Array of name/animation-controller pairs


//////

<div class="language-text highlight"><span class="filename"><code>scripts</code></span><pre id="__code_1"><span></span></pre></div>

////// html | div.result
/////// define
`animate`：<samp>array</samp>

- Tells minecraft to run which animation / animation controllers and under what conditions.


///////

<div class="language-text highlight"><span class="filename"><code>animate</code></span><pre id="__code_1"><span></span></pre></div>

/////// html | div.result
//////// define
`<any array element>`：<samp>string</samp>

- The name of an animation controller referenced in animations.


////////


//////// define
`<any array element>`：<samp>object</samp>

- A conditional statement to run the animation under a specified condition.


////////

<div class="language-text highlight"><span class="filename"><code>&lt;any array element&gt;</code></span><pre id="__code_1"><span></span></pre></div>

//////// html | div.result
///////// define
`<any object property>`：<samp>string</samp>


/////////


////////



///////


//////


////// define
`spawn_category`：<samp>string</samp>

- At the moment, not fully implemented and does nothing. Recommended to leave it empty or set it to misc


//////


/////


///// define
`component_groups`：<samp>object</samp>

- Each group when add / remove the default components.


/////

<div class="language-text highlight"><span class="filename"><code>component_groups</code></span><pre id="__code_1"><span></span></pre></div>

///// html | div.result
////// define
`<any object property>`：<samp>components</samp> {#assets.schemas-blockception.behavior.entities.format.components.json}

- The components that are added as the foundation of the entity.


//////

```mcschema
components:
{
  attribute "minecraft:absorption"
  addrider "minecraft:addrider"
  admire_item "minecraft:admire_item"
  ageable "minecraft:ageable"
  ambient_sound_interval "minecraft:ambient_sound_interval"
  anger_level "minecraft:anger_level"
  angry "minecraft:angry"
  break_door "minecraft:annotation.break_door"
  open_door "minecraft:annotation.open_door"
  area_attack "minecraft:area_attack"
  attack_cooldown "minecraft:attack_cooldown"
  attribute "minecraft:attack_damage"
  attack "minecraft:attack"
  balloonable "minecraft:balloonable"
  barter "minecraft:barter"
  block_climber "minecraft:block_climber"
  block_sensor "minecraft:block_sensor"
  body_rotation_blocked "minecraft:body_rotation_blocked"
  boostable "minecraft:boostable"
  boss "minecraft:boss"
  break_blocks "minecraft:break_blocks"
  breathable "minecraft:breathable"
  breedable "minecraft:breedable"
  bribeable "minecraft:bribeable"
  buoyant "minecraft:buoyant"
  burns_in_daylight "minecraft:burns_in_daylight"
  can_climb "minecraft:can_climb"
  can_fly "minecraft:can_fly"
  can_join_raid "minecraft:can_join_raid"
  can_power_jump "minecraft:can_power_jump"
  celebrate_hunt "minecraft:celebrate_hunt"
  collision_box "minecraft:collision_box"
  color "minecraft:color"
  color2 "minecraft:color2"
  combat_regeneration "minecraft:combat_regeneration"
  conditional_bandwidth_optimization "minecraft:conditional_bandwidth_optimization"
  custom_hit_test "minecraft:custom_hit_test"
  damage_over_time "minecraft:damage_over_time"
  damage_sensor "minecraft:damage_sensor"
  dash "minecraft:dash"
  default_look_angle "minecraft:default_look_angle"
  despawn "minecraft:despawn"
  dimension_bound "minecraft:dimension_bound"
  drying_out_timer "minecraft:drying_out_timer"
  dweller "minecraft:dweller"
  economy_trade_table "minecraft:economy_trade_table"
  entity_sensor "minecraft:entity_sensor"
  environment_sensor "minecraft:environment_sensor"
  equip_item "minecraft:equip_item"
  equipment "minecraft:equipment"
  equippable "minecraft:equippable"
  exhaustion_values "minecraft:exhaustion_values"
  experience_reward "minecraft:experience_reward"
  explode "minecraft:explode"
  fall_damage "minecraft:fall_damage"
  fire_immune "minecraft:fire_immune"
  floats_in_liquid "minecraft:floats_in_liquid"
  flocking "minecraft:flocking"
  flying_speed "minecraft:flying_speed"
  attribute "minecraft:follow_range"
  friction_modifier "minecraft:friction_modifier"
  game_event_movement_tracking "minecraft:game_event_movement_tracking"
  genetics "minecraft:genetics"
  giveable "minecraft:giveable"
  ground_offset "minecraft:ground_offset"
  group_size "minecraft:group_size"
  grows_crop "minecraft:grows_crop"
  healable "minecraft:healable"
  attribute "minecraft:health"
  heartbeat "minecraft:heartbeat"
  hide "minecraft:hide"
  home "minecraft:home"
  jump_strength "minecraft:horse.jump_strength"
  hurt_on_condition "minecraft:hurt_on_condition"
  hurt_when_wet "minecraft:hurt_when_wet"
  input_ground_controlled "minecraft:input_ground_controlled"
  inside_block_notifier "minecraft:inside_block_notifier"
  insomnia "minecraft:insomnia"
  instant_despawn "minecraft:instant_despawn"
  interact "minecraft:interact"
  inventory "minecraft:inventory"
  is_baby "minecraft:is_baby"
  is_charged "minecraft:is_charged"
  is_chested "minecraft:is_chested"
  is_dyeable "minecraft:is_dyeable"
  is_hidden_when_invisible "minecraft:is_hidden_when_invisible"
  is_ignited "minecraft:is_ignited"
  is_illager_captain "minecraft:is_illager_captain"
  is_pregnant "minecraft:is_pregnant"
  is_saddled "minecraft:is_saddled"
  is_shaking "minecraft:is_shaking"
  is_sheared "minecraft:is_sheared"
  is_stackable "minecraft:is_stackable"
  is_stunned "minecraft:is_stunned"
  is_tamed "minecraft:is_tamed"
  item_controllable "minecraft:item_controllable"
  item_hopper "minecraft:item_hopper"
  dynamic "minecraft:jump.dynamic"
  static "minecraft:jump.static"
  attribute "minecraft:knockback_resistance"
  attribute "minecraft:lava_movement"
  leashable "minecraft:leashable"
  looked_at "minecraft:looked_at"
  loot "minecraft:loot"
  attribute "minecraft:luck"
  managed_wandering_trader "minecraft:managed_wandering_trader"
  mark_variant "minecraft:mark_variant"
  mob_effect "minecraft:mob_effect"
  mob_effect_immunity "minecraft:mob_effect_immunity"
  movement_sound_distance_offset "minecraft:movement_sound_distance_offset"
  amphibious "minecraft:movement.amphibious"
  basic "minecraft:movement.basic"
  fly "minecraft:movement.fly"
  generic "minecraft:movement.generic"
  glide "minecraft:movement.glide"
  hover "minecraft:movement.hover"
  jump "minecraft:movement.jump"
  skip "minecraft:movement.skip"
  sway "minecraft:movement.sway"
  attribute "minecraft:movement"
  nameable "minecraft:nameable"
  climb "minecraft:navigation.climb"
  float "minecraft:navigation.float"
  fly "minecraft:navigation.fly"
  generic "minecraft:navigation.generic"
  hover "minecraft:navigation.hover"
  swim "minecraft:navigation.swim"
  walk "minecraft:navigation.walk"
  npc "minecraft:npc"
  on_death "minecraft:on_death"
  on_friendly_anger "minecraft:on_friendly_anger"
  on_hurt_by_player "minecraft:on_hurt_by_player"
  on_hurt "minecraft:on_hurt"
  on_ignite "minecraft:on_ignite"
  on_start_landing "minecraft:on_start_landing"
  on_start_takeoff "minecraft:on_start_takeoff"
  on_target_acquired "minecraft:on_target_acquired"
  on_target_escape "minecraft:on_target_escape"
  on_wake_with_owner "minecraft:on_wake_with_owner"
  out_of_control "minecraft:out_of_control"
  peek "minecraft:peek"
  persistent "minecraft:persistent"
  physics "minecraft:physics"
  exhaustion "minecraft:player.exhaustion"
  experience "minecraft:player.experience"
  level "minecraft:player.level"
  saturation "minecraft:player.saturation"
  preferred_path "minecraft:preferred_path"
  projectile "minecraft:projectile"
  push_through "minecraft:push_through"
  pushable "minecraft:pushable"
  raid_trigger "minecraft:raid_trigger"
  rail_movement "minecraft:rail_movement"
  rail_sensor "minecraft:rail_sensor"
  ravager_blocked "minecraft:ravager_blocked"
  rideable "minecraft:rideable"
  reflect_projectiles "minecraft:reflect_projectiles"
  scale_by_age "minecraft:scale_by_age"
  scale "minecraft:scale"
  scheduler "minecraft:scheduler"
  shareables "minecraft:shareables"
  shooter "minecraft:shooter"
  sittable "minecraft:sittable"
  skin_id "minecraft:skin_id"
  sound_volume "minecraft:sound_volume"
  spawn_entity "minecraft:spawn_entity"
  spell_effects "minecraft:spell_effects"
  strength "minecraft:strength"
  suspect_tracking "minecraft:suspect_tracking"
  tameable "minecraft:tameable"
  tamemount "minecraft:tamemount"
  target_nearby_sensor "minecraft:target_nearby_sensor"
  teleport "minecraft:teleport"
  tick_world "minecraft:tick_world"
  timer "minecraft:timer"
  trade_resupply "minecraft:trade_resupply"
  trade_table "minecraft:trade_table"
  trail "minecraft:trail"
  transformation "minecraft:transformation"
  transient "minecraft:transient"
  trust "minecraft:trust"
  trusting "minecraft:trusting"
  type_family "minecraft:type_family"
  attribute "minecraft:underwater_movement"
  variable_max_auto_step "minecraft:variable_max_auto_step"
  variant "minecraft:variant"
  vibration_damper "minecraft:vibration_damper"
  vibration_listener "minecraft:vibration_listener"
  walk_animation_speed "minecraft:walk_animation_speed"
  wants_jockey "minecraft:wants_jockey"
  water_movement "minecraft:water_movement"
  admire_item "minecraft:behavior.admire_item"
  avoid_block "minecraft:behavior.avoid_block"
  avoid_mob_type "minecraft:behavior.avoid_mob_type"
  barter "minecraft:behavior.barter"
  beg "minecraft:behavior.beg"
  break_door "minecraft:behavior.break_door"
  breed "minecraft:behavior.breed"
  celebrate_survive "minecraft:behavior.celebrate_survive"
  celebrate "minecraft:behavior.celebrate"
  charge_attack "minecraft:behavior.charge_attack"
  charge_held_item "minecraft:behavior.charge_held_item"
  circle_around_anchor "minecraft:behavior.circle_around_anchor"
  controlled_by_player "minecraft:behavior.controlled_by_player"
  croak "minecraft:behavior.croak"
  defend_trusted_target "minecraft:behavior.defend_trusted_target"
  defend_village_target "minecraft:behavior.defend_village_target"
  delayed_attack "minecraft:behavior.delayed_attack"
  dig "minecraft:behavior.dig"
  door_interact "minecraft:behavior.door_interact"
  dragonchargeplayer "minecraft:behavior.dragonchargeplayer"
  dragondeath "minecraft:behavior.dragondeath"
  dragonflaming "minecraft:behavior.dragonflaming"
  dragonholdingpattern "minecraft:behavior.dragonholdingpattern"
  dragonlanding "minecraft:behavior.dragonlanding"
  dragonscanning "minecraft:behavior.dragonscanning"
  dragonstrafeplayer "minecraft:behavior.dragonstrafeplayer"
  dragontakeoff "minecraft:behavior.dragontakeoff"
  drink_milk "minecraft:behavior.drink_milk"
  drink_potion "minecraft:behavior.drink_potion"
  drop_item_for "minecraft:behavior.drop_item_for"
  eat_block "minecraft:behavior.eat_block"
  eat_carried_item "minecraft:behavior.eat_carried_item"
  eat_mob "minecraft:behavior.eat_mob"
  emerge "minecraft:behavior.emerge"
  enderman_leave_block "minecraft:behavior.enderman_leave_block"
  enderman_take_block "minecraft:behavior.enderman_take_block"
  equip_item "minecraft:behavior.equip_item"
  explore_outskirts "minecraft:behavior.explore_outskirts"
  fertilize_farm_block "minecraft:behavior.fertilize_farm_block"
  find_cover "minecraft:behavior.find_cover"
  find_mount "minecraft:behavior.find_mount"
  find_underwater_treasure "minecraft:behavior.find_underwater_treasure"
  fire_at_target "minecraft:behavior.fire_at_target"
  flee_sun "minecraft:behavior.flee_sun"
  float_wander "minecraft:behavior.float_wander"
  float "minecraft:behavior.float"
  follow_caravan "minecraft:behavior.follow_caravan"
  follow_mob "minecraft:behavior.follow_mob"
  follow_owner "minecraft:behavior.follow_owner"
  follow_parent "minecraft:behavior.follow_parent"
  follow_target_captain "minecraft:behavior.follow_target_captain"
  go_and_give_items_to_noteblock "minecraft:behavior.go_and_give_items_to_noteblock"
  go_and_give_items_to_owner "minecraft:behavior.go_and_give_items_to_owner"
  go_home "minecraft:behavior.go_home"
  guardian_attack "minecraft:behavior.guardian_attack"
  harvest_farm_block "minecraft:behavior.harvest_farm_block"
  hide "minecraft:behavior.hide"
  hold_ground "minecraft:behavior.hold_ground"
  hurt_by_target "minecraft:behavior.hurt_by_target"
  inspect_bookshelf "minecraft:behavior.inspect_bookshelf"
  investigate_suspicious_location "minecraft:behavior.investigate_suspicious_location"
  jump_around_target "minecraft:behavior.jump_around_target"
  jump_to_block "minecraft:behavior.jump_to_block"
  knockback_roar "minecraft:behavior.knockback_roar"
  lay_down "minecraft:behavior.lay_down"
  lay_egg "minecraft:behavior.lay_egg"
  leap_at_target "minecraft:behavior.leap_at_target"
  look_at_entity "minecraft:behavior.look_at_entity"
  look_at_player "minecraft:behavior.look_at_player"
  look_at_target "minecraft:behavior.look_at_target"
  look_at_trading_player "minecraft:behavior.look_at_trading_player"
  make_love "minecraft:behavior.make_love"
  melee_attack "minecraft:behavior.melee_attack"
  melee_box_attack "minecraft:behavior.melee_box_attack"
  mingle "minecraft:behavior.mingle"
  mount_pathing "minecraft:behavior.mount_pathing"
  move_indoors "minecraft:behavior.move_indoors"
  move_outdoors "minecraft:behavior.move_outdoors"
  move_through_village "minecraft:behavior.move_through_village"
  move_to_block "minecraft:behavior.move_to_block"
  move_to_land "minecraft:behavior.move_to_land"
  move_to_lava "minecraft:behavior.move_to_lava"
  move_to_liquid "minecraft:behavior.move_to_liquid"
  move_to_poi "minecraft:behavior.move_to_poi"
  move_to_random_block "minecraft:behavior.move_to_random_block"
  move_to_village "minecraft:behavior.move_to_village"
  move_to_water "minecraft:behavior.move_to_water"
  move_towards_dwelling_restriction "minecraft:behavior.move_towards_dwelling_restriction"
  move_towards_home_restriction "minecraft:behavior.move_towards_home_restriction"
  move_towards_restriction "minecraft:behavior.move_towards_restriction"
  move_towards_target "minecraft:behavior.move_towards_target"
  nap "minecraft:behavior.nap"
  nearest_attackable_target "minecraft:behavior.nearest_attackable_target"
  nearest_prioritized_attackable_target "minecraft:behavior.nearest_prioritized_attackable_target"
  ocelot_sit_on_block "minecraft:behavior.ocelot_sit_on_block"
  ocelotattack "minecraft:behavior.ocelotattack"
  offer_flower "minecraft:behavior.offer_flower"
  open_door "minecraft:behavior.open_door"
  owner_hurt_by_target "minecraft:behavior.owner_hurt_by_target"
  owner_hurt_target "minecraft:behavior.owner_hurt_target"
  panic "minecraft:behavior.panic"
  pet_sleep_with_owner "minecraft:behavior.pet_sleep_with_owner"
  pickup_items "minecraft:behavior.pickup_items"
  play_dead "minecraft:behavior.play_dead"
  play "minecraft:behavior.play"
  player_ride_tamed "minecraft:behavior.player_ride_tamed"
  raid_garden "minecraft:behavior.raid_garden"
  ram_attack "minecraft:behavior.ram_attack"
  random_breach "minecraft:behavior.random_breach"
  random_fly "minecraft:behavior.random_fly"
  random_hover "minecraft:behavior.random_hover"
  random_look_around_and_sit "minecraft:behavior.random_look_around_and_sit"
  random_look_around "minecraft:behavior.random_look_around"
  random_search_and_dig "minecraft:behavior.random_search_and_dig"
  random_sitting "minecraft:behavior.random_sitting"
  random_stroll "minecraft:behavior.random_stroll"
  random_swim "minecraft:behavior.random_swim"
  ranged_attack "minecraft:behavior.ranged_attack"
  receive_love "minecraft:behavior.receive_love"
  restrict_open_door "minecraft:behavior.restrict_open_door"
  restrict_sun "minecraft:behavior.restrict_sun"
  rise_to_liquid_level "minecraft:behavior.rise_to_liquid_level"
  roar "minecraft:behavior.roar"
  roll "minecraft:behavior.roll"
  run_around_like_crazy "minecraft:behavior.run_around_like_crazy"
  scared "minecraft:behavior.scared"
  send_event "minecraft:behavior.send_event"
  share_items "minecraft:behavior.share_items"
  silverfish_merge_with_stone "minecraft:behavior.silverfish_merge_with_stone"
  silverfish_wake_up_friends "minecraft:behavior.silverfish_wake_up_friends"
  skeleton_horse_trap "minecraft:behavior.skeleton_horse_trap"
  sleep "minecraft:behavior.sleep"
  slime_attack "minecraft:behavior.slime_attack"
  slime_float "minecraft:behavior.slime_float"
  slime_keep_on_jumping "minecraft:behavior.slime_keep_on_jumping"
  slime_random_direction "minecraft:behavior.slime_random_direction"
  snacking "minecraft:behavior.snacking"
  sneeze "minecraft:behavior.sneeze"
  sniff "minecraft:behavior.sniff"
  sonic_boom "minecraft:behavior.sonic_boom"
  squid_dive "minecraft:behavior.squid_dive"
  squid_flee "minecraft:behavior.squid_flee"
  squid_idle "minecraft:behavior.squid_idle"
  squid_move_away_from_ground "minecraft:behavior.squid_move_away_from_ground"
  squid_out_of_water "minecraft:behavior.squid_out_of_water"
  stalk_and_pounce_on_target "minecraft:behavior.stalk_and_pounce_on_target"
  stay_near_noteblock "minecraft:behavior.stay_near_noteblock"
  stay_while_sitting "minecraft:behavior.stay_while_sitting"
  stomp_attack "minecraft:behavior.stomp_attack"
  stomp_turtle_egg "minecraft:behavior.stomp_turtle_egg"
  stroll_towards_village "minecraft:behavior.stroll_towards_village"
  summon_entity "minecraft:behavior.summon_entity"
  swell "minecraft:behavior.swell"
  swim_idle "minecraft:behavior.swim_idle"
  swim_up_for_breath "minecraft:behavior.swim_up_for_breath"
  swim_wander "minecraft:behavior.swim_wander"
  swim_with_entity "minecraft:behavior.swim_with_entity"
  swoop_attack "minecraft:behavior.swoop_attack"
  take_flower "minecraft:behavior.take_flower"
  teleport_to_owner "minecraft:behavior.teleport_to_owner"
  move_around_target "minecraft:behavior.move_around_target"
  target_when_pushed "minecraft:behavior.target_when_pushed"
  tempt "minecraft:behavior.tempt"
  timer_flag "minecraft:behavior.timer_flag_1"
  timer_flag "minecraft:behavior.timer_flag_2"
  timer_flag "minecraft:behavior.timer_flag_3"
  trade_interest "minecraft:behavior.trade_interest"
  trade_with_player "minecraft:behavior.trade_with_player"
  vex_copy_owner_target "minecraft:behavior.vex_copy_owner_target"
  vex_random_move "minecraft:behavior.vex_random_move"
  wither_random_attack_pos_goal "minecraft:behavior.wither_random_attack_pos_goal"
  wither_target_highest_damage "minecraft:behavior.wither_target_highest_damage"
  work "minecraft:behavior.work"
  work_composter "minecraft:behavior.work_composter"
}

```

////// html | div.result
/////// define
`minecraft:absorption`：<samp>attribute</samp>

- [`minecraft:absorption`](./components/attribute.md)组件。A collection of components.


///////

/////// define
`minecraft:addrider`：<samp>addrider</samp>

- [`minecraft:addrider`](./components/addrider.md)组件。A collection of components.


///////

/////// define
`minecraft:admire_item`：<samp>admire_item</samp>

- [`minecraft:admire_item`](./components/admire_item.md)组件。A collection of components.


///////

/////// define
`minecraft:ageable`：<samp>ageable</samp>

- [`minecraft:ageable`](./components/ageable.md)组件。A collection of components.


///////

/////// define
`minecraft:ambient_sound_interval`：<samp>ambient_sound_interval</samp>

- [`minecraft:ambient_sound_interval`](./components/ambient_sound_interval.md)组件。A collection of components.


///////

/////// define
`minecraft:anger_level`：<samp>anger_level</samp>

- [`minecraft:anger_level`](./components/anger_level.md)组件。A collection of components.


///////

/////// define
`minecraft:angry`：<samp>angry</samp>

- [`minecraft:angry`](./components/angry.md)组件。A collection of components.


///////

/////// define
`minecraft:annotation.break_door`：<samp>break_door</samp>

- [`minecraft:annotation.break_door`](./components/annotation.break_door.md)组件。A collection of components.


///////

/////// define
`minecraft:annotation.open_door`：<samp>open_door</samp>

- [`minecraft:annotation.open_door`](./components/annotation.open_door.md)组件。A collection of components.


///////

/////// define
`minecraft:area_attack`：<samp>area_attack</samp>

- [`minecraft:area_attack`](./components/area_attack.md)组件。A collection of components.


///////

/////// define
`minecraft:attack_cooldown`：<samp>attack_cooldown</samp>

- [`minecraft:attack_cooldown`](./components/attack_cooldown.md)组件。A collection of components.


///////

/////// define
`minecraft:attack_damage`：<samp>attribute</samp>

- [`minecraft:attack_damage`](./components/attribute.md)组件。A collection of components.


///////

/////// define
`minecraft:attack`：<samp>attack</samp>

- [`minecraft:attack`](./components/attack.md)组件。A collection of components.


///////

/////// define
`minecraft:balloonable`：<samp>balloonable</samp>

- [`minecraft:balloonable`](./components/balloonable.md)组件。A collection of components.


///////

/////// define
`minecraft:barter`：<samp>barter</samp>

- [`minecraft:barter`](./components/barter.md)组件。A collection of components.


///////

/////// define
`minecraft:block_climber`：<samp>block_climber</samp>

- [`minecraft:block_climber`](./components/block_climber.md)组件。A collection of components.


///////

/////// define
`minecraft:block_sensor`：<samp>block_sensor</samp>

- [`minecraft:block_sensor`](./components/block_sensor.md)组件。A collection of components.


///////

/////// define
`minecraft:body_rotation_blocked`：<samp>body_rotation_blocked</samp>

- [`minecraft:body_rotation_blocked`](./components/body_rotation_blocked.md)组件。A collection of components.


///////

/////// define
`minecraft:boostable`：<samp>boostable</samp>

- [`minecraft:boostable`](./components/boostable.md)组件。A collection of components.


///////

/////// define
`minecraft:boss`：<samp>boss</samp>

- [`minecraft:boss`](./components/boss.md)组件。A collection of components.


///////

/////// define
`minecraft:break_blocks`：<samp>break_blocks</samp>

- [`minecraft:break_blocks`](./components/break_blocks.md)组件。A collection of components.


///////

/////// define
`minecraft:breathable`：<samp>breathable</samp>

- [`minecraft:breathable`](./components/breathable.md)组件。A collection of components.


///////

/////// define
`minecraft:breedable`：<samp>breedable</samp>

- [`minecraft:breedable`](./components/breedable.md)组件。A collection of components.


///////

/////// define
`minecraft:bribeable`：<samp>bribeable</samp>

- [`minecraft:bribeable`](./components/bribeable.md)组件。A collection of components.


///////

/////// define
`minecraft:buoyant`：<samp>buoyant</samp>

- [`minecraft:buoyant`](./components/buoyant.md)组件。A collection of components.


///////

/////// define
`minecraft:burns_in_daylight`：<samp>burns_in_daylight</samp>

- [`minecraft:burns_in_daylight`](./components/burns_in_daylight.md)组件。A collection of components.


///////

/////// define
`minecraft:can_climb`：<samp>can_climb</samp>

- [`minecraft:can_climb`](./components/can_climb.md)组件。A collection of components.


///////

/////// define
`minecraft:can_fly`：<samp>can_fly</samp>

- [`minecraft:can_fly`](./components/can_fly.md)组件。A collection of components.


///////

/////// define
`minecraft:can_join_raid`：<samp>can_join_raid</samp>

- [`minecraft:can_join_raid`](./components/can_join_raid.md)组件。A collection of components.


///////

/////// define
`minecraft:can_power_jump`：<samp>can_power_jump</samp>

- [`minecraft:can_power_jump`](./components/can_power_jump.md)组件。A collection of components.


///////

/////// define
`minecraft:celebrate_hunt`：<samp>celebrate_hunt</samp>

- [`minecraft:celebrate_hunt`](./components/celebrate_hunt.md)组件。A collection of components.


///////

/////// define
`minecraft:collision_box`：<samp>collision_box</samp>

- [`minecraft:collision_box`](./components/collision_box.md)组件。A collection of components.


///////

/////// define
`minecraft:color`：<samp>color</samp>

- [`minecraft:color`](./components/color.md)组件。A collection of components.


///////

/////// define
`minecraft:color2`：<samp>color2</samp>

- [`minecraft:color2`](./components/color2.md)组件。A collection of components.


///////

/////// define
`minecraft:combat_regeneration`：<samp>combat_regeneration</samp>

- [`minecraft:combat_regeneration`](./components/combat_regeneration.md)组件。A collection of components.


///////

/////// define
`minecraft:conditional_bandwidth_optimization`：<samp>conditional_bandwidth_optimization</samp>

- [`minecraft:conditional_bandwidth_optimization`](./components/conditional_bandwidth_optimization.md)组件。A collection of components.


///////

/////// define
`minecraft:custom_hit_test`：<samp>custom_hit_test</samp>

- [`minecraft:custom_hit_test`](./components/custom_hit_test.md)组件。A collection of components.


///////

/////// define
`minecraft:damage_over_time`：<samp>damage_over_time</samp>

- [`minecraft:damage_over_time`](./components/damage_over_time.md)组件。A collection of components.


///////

/////// define
`minecraft:damage_sensor`：<samp>damage_sensor</samp>

- [`minecraft:damage_sensor`](./components/damage_sensor.md)组件。A collection of components.


///////

/////// define
`minecraft:dash`：<samp>dash</samp>

- [`minecraft:dash`](./components/dash.md)组件。A collection of components.


///////

/////// define
`minecraft:default_look_angle`：<samp>default_look_angle</samp>

- [`minecraft:default_look_angle`](./components/default_look_angle.md)组件。A collection of components.


///////

/////// define
`minecraft:despawn`：<samp>despawn</samp>

- [`minecraft:despawn`](./components/despawn.md)组件。A collection of components.


///////

/////// define
`minecraft:dimension_bound`：<samp>dimension_bound</samp>

- [`minecraft:dimension_bound`](./components/dimension_bound.md)组件。A collection of components.


///////

/////// define
`minecraft:drying_out_timer`：<samp>drying_out_timer</samp>

- [`minecraft:drying_out_timer`](./components/drying_out_timer.md)组件。A collection of components.


///////

/////// define
`minecraft:dweller`：<samp>dweller</samp>

- [`minecraft:dweller`](./components/dweller.md)组件。A collection of components.


///////

/////// define
`minecraft:economy_trade_table`：<samp>economy_trade_table</samp>

- [`minecraft:economy_trade_table`](./components/economy_trade_table.md)组件。A collection of components.


///////

/////// define
`minecraft:entity_sensor`：<samp>entity_sensor</samp>

- [`minecraft:entity_sensor`](./components/entity_sensor.md)组件。A collection of components.


///////

/////// define
`minecraft:environment_sensor`：<samp>environment_sensor</samp>

- [`minecraft:environment_sensor`](./components/environment_sensor.md)组件。A collection of components.


///////

/////// define
`minecraft:equip_item`：<samp>equip_item</samp>

- [`minecraft:equip_item`](./components/equip_item.md)组件。A collection of components.


///////

/////// define
`minecraft:equipment`：<samp>equipment</samp>

- [`minecraft:equipment`](./components/equipment.md)组件。A collection of components.


///////

/////// define
`minecraft:equippable`：<samp>equippable</samp>

- [`minecraft:equippable`](./components/equippable.md)组件。A collection of components.


///////

/////// define
`minecraft:exhaustion_values`：<samp>exhaustion_values</samp>

- [`minecraft:exhaustion_values`](./components/exhaustion_values.md)组件。A collection of components.


///////

/////// define
`minecraft:experience_reward`：<samp>experience_reward</samp>

- [`minecraft:experience_reward`](./components/experience_reward.md)组件。A collection of components.


///////

/////// define
`minecraft:explode`：<samp>explode</samp>

- [`minecraft:explode`](./components/explode.md)组件。A collection of components.


///////

/////// define
`minecraft:fall_damage`：<samp>fall_damage</samp>

- [`minecraft:fall_damage`](./components/fall_damage.md)组件。A collection of components.


///////

/////// define
`minecraft:fire_immune`：<samp>fire_immune</samp>

- [`minecraft:fire_immune`](./components/fire_immune.md)组件。A collection of components.


///////

/////// define
`minecraft:floats_in_liquid`：<samp>floats_in_liquid</samp>

- [`minecraft:floats_in_liquid`](./components/floats_in_liquid.md)组件。A collection of components.


///////

/////// define
`minecraft:flocking`：<samp>flocking</samp>

- [`minecraft:flocking`](./components/flocking.md)组件。A collection of components.


///////

/////// define
`minecraft:flying_speed`：<samp>flying_speed</samp>

- [`minecraft:flying_speed`](./components/flying_speed.md)组件。A collection of components.


///////

/////// define
`minecraft:follow_range`：<samp>attribute</samp>

- [`minecraft:follow_range`](./components/attribute.md)组件。A collection of components.


///////

/////// define
`minecraft:friction_modifier`：<samp>friction_modifier</samp>

- [`minecraft:friction_modifier`](./components/friction_modifier.md)组件。A collection of components.


///////

/////// define
`minecraft:game_event_movement_tracking`：<samp>game_event_movement_tracking</samp>

- [`minecraft:game_event_movement_tracking`](./components/game_event_movement_tracking.md)组件。A collection of components.


///////

/////// define
`minecraft:genetics`：<samp>genetics</samp>

- [`minecraft:genetics`](./components/genetics.md)组件。A collection of components.


///////

/////// define
`minecraft:giveable`：<samp>giveable</samp>

- [`minecraft:giveable`](./components/giveable.md)组件。A collection of components.


///////

/////// define
`minecraft:ground_offset`：<samp>ground_offset</samp>

- [`minecraft:ground_offset`](./components/ground_offset.md)组件。A collection of components.


///////

/////// define
`minecraft:group_size`：<samp>group_size</samp>

- [`minecraft:group_size`](./components/group_size.md)组件。A collection of components.


///////

/////// define
`minecraft:grows_crop`：<samp>grows_crop</samp>

- [`minecraft:grows_crop`](./components/grows_crop.md)组件。A collection of components.


///////

/////// define
`minecraft:healable`：<samp>healable</samp>

- [`minecraft:healable`](./components/healable.md)组件。A collection of components.


///////

/////// define
`minecraft:health`：<samp>attribute</samp>

- [`minecraft:health`](./components/attribute.md)组件。A collection of components.


///////

/////// define
`minecraft:heartbeat`：<samp>heartbeat</samp>

- [`minecraft:heartbeat`](./components/heartbeat.md)组件。A collection of components.


///////

/////// define
`minecraft:hide`：<samp>hide</samp>

- [`minecraft:hide`](./components/hide.md)组件。A collection of components.


///////

/////// define
`minecraft:home`：<samp>home</samp>

- [`minecraft:home`](./components/home.md)组件。A collection of components.


///////

/////// define
`minecraft:horse.jump_strength`：<samp>jump_strength</samp>

- [`minecraft:horse.jump_strength`](./components/horse.jump_strength.md)组件。A collection of components.


///////

/////// define
`minecraft:hurt_on_condition`：<samp>hurt_on_condition</samp>

- [`minecraft:hurt_on_condition`](./components/hurt_on_condition.md)组件。A collection of components.


///////

/////// define
`minecraft:hurt_when_wet`：<samp>hurt_when_wet</samp>

- [`minecraft:hurt_when_wet`](./components/hurt_when_wet.md)组件。A collection of components.


///////

/////// define
`minecraft:input_ground_controlled`：<samp>input_ground_controlled</samp>

- [`minecraft:input_ground_controlled`](./components/input_ground_controlled.md)组件。A collection of components.


///////

/////// define
`minecraft:inside_block_notifier`：<samp>inside_block_notifier</samp>

- [`minecraft:inside_block_notifier`](./components/inside_block_notifier.md)组件。A collection of components.


///////

/////// define
`minecraft:insomnia`：<samp>insomnia</samp>

- [`minecraft:insomnia`](./components/insomnia.md)组件。A collection of components.


///////

/////// define
`minecraft:instant_despawn`：<samp>instant_despawn</samp>

- [`minecraft:instant_despawn`](./components/instant_despawn.md)组件。A collection of components.


///////

/////// define
`minecraft:interact`：<samp>interact</samp>

- [`minecraft:interact`](./components/interact.md)组件。A collection of components.


///////

/////// define
`minecraft:inventory`：<samp>inventory</samp>

- [`minecraft:inventory`](./components/inventory.md)组件。A collection of components.


///////

/////// define
`minecraft:is_baby`：<samp>is_baby</samp>

- [`minecraft:is_baby`](./components/is_baby.md)组件。A collection of components.


///////

/////// define
`minecraft:is_charged`：<samp>is_charged</samp>

- [`minecraft:is_charged`](./components/is_charged.md)组件。A collection of components.


///////

/////// define
`minecraft:is_chested`：<samp>is_chested</samp>

- [`minecraft:is_chested`](./components/is_chested.md)组件。A collection of components.


///////

/////// define
`minecraft:is_dyeable`：<samp>is_dyeable</samp>

- [`minecraft:is_dyeable`](./components/is_dyeable.md)组件。A collection of components.


///////

/////// define
`minecraft:is_hidden_when_invisible`：<samp>is_hidden_when_invisible</samp>

- [`minecraft:is_hidden_when_invisible`](./components/is_hidden_when_invisible.md)组件。A collection of components.


///////

/////// define
`minecraft:is_ignited`：<samp>is_ignited</samp>

- [`minecraft:is_ignited`](./components/is_ignited.md)组件。A collection of components.


///////

/////// define
`minecraft:is_illager_captain`：<samp>is_illager_captain</samp>

- [`minecraft:is_illager_captain`](./components/is_illager_captain.md)组件。A collection of components.


///////

/////// define
`minecraft:is_pregnant`：<samp>is_pregnant</samp>

- [`minecraft:is_pregnant`](./components/is_pregnant.md)组件。A collection of components.


///////

/////// define
`minecraft:is_saddled`：<samp>is_saddled</samp>

- [`minecraft:is_saddled`](./components/is_saddled.md)组件。A collection of components.


///////

/////// define
`minecraft:is_shaking`：<samp>is_shaking</samp>

- [`minecraft:is_shaking`](./components/is_shaking.md)组件。A collection of components.


///////

/////// define
`minecraft:is_sheared`：<samp>is_sheared</samp>

- [`minecraft:is_sheared`](./components/is_sheared.md)组件。A collection of components.


///////

/////// define
`minecraft:is_stackable`：<samp>is_stackable</samp>

- [`minecraft:is_stackable`](./components/is_stackable.md)组件。A collection of components.


///////

/////// define
`minecraft:is_stunned`：<samp>is_stunned</samp>

- [`minecraft:is_stunned`](./components/is_stunned.md)组件。A collection of components.


///////

/////// define
`minecraft:is_tamed`：<samp>is_tamed</samp>

- [`minecraft:is_tamed`](./components/is_tamed.md)组件。A collection of components.


///////

/////// define
`minecraft:item_controllable`：<samp>item_controllable</samp>

- [`minecraft:item_controllable`](./components/item_controllable.md)组件。A collection of components.


///////

/////// define
`minecraft:item_hopper`：<samp>item_hopper</samp>

- [`minecraft:item_hopper`](./components/item_hopper.md)组件。A collection of components.


///////

/////// define
`minecraft:jump.dynamic`：<samp>dynamic</samp>

- [`minecraft:jump.dynamic`](./components/jump.dynamic.md)组件。A collection of components.


///////

/////// define
`minecraft:jump.static`：<samp>static</samp>

- [`minecraft:jump.static`](./components/jump.static.md)组件。A collection of components.


///////

/////// define
`minecraft:knockback_resistance`：<samp>attribute</samp>

- [`minecraft:knockback_resistance`](./components/attribute.md)组件。A collection of components.


///////

/////// define
`minecraft:lava_movement`：<samp>attribute</samp>

- [`minecraft:lava_movement`](./components/attribute.md)组件。A collection of components.


///////

/////// define
`minecraft:leashable`：<samp>leashable</samp>

- [`minecraft:leashable`](./components/leashable.md)组件。A collection of components.


///////

/////// define
`minecraft:looked_at`：<samp>looked_at</samp>

- [`minecraft:looked_at`](./components/looked_at.md)组件。A collection of components.


///////

/////// define
`minecraft:loot`：<samp>loot</samp>

- [`minecraft:loot`](./components/loot.md)组件。A collection of components.


///////

/////// define
`minecraft:luck`：<samp>attribute</samp>

- [`minecraft:luck`](./components/attribute.md)组件。A collection of components.


///////

/////// define
`minecraft:managed_wandering_trader`：<samp>managed_wandering_trader</samp>

- [`minecraft:managed_wandering_trader`](./components/managed_wandering_trader.md)组件。A collection of components.


///////

/////// define
`minecraft:mark_variant`：<samp>mark_variant</samp>

- [`minecraft:mark_variant`](./components/mark_variant.md)组件。A collection of components.


///////

/////// define
`minecraft:mob_effect`：<samp>mob_effect</samp>

- [`minecraft:mob_effect`](./components/mob_effect.md)组件。A collection of components.


///////

/////// define
`minecraft:mob_effect_immunity`：<samp>mob_effect_immunity</samp>

- [`minecraft:mob_effect_immunity`](./components/mob_effect_immunity.md)组件。A collection of components.


///////

/////// define
`minecraft:movement_sound_distance_offset`：<samp>movement_sound_distance_offset</samp>

- [`minecraft:movement_sound_distance_offset`](./components/movement_sound_distance_offset.md)组件。A collection of components.


///////

/////// define
`minecraft:movement.amphibious`：<samp>amphibious</samp>

- [`minecraft:movement.amphibious`](./components/movement.amphibious.md)组件。A collection of components.


///////

/////// define
`minecraft:movement.basic`：<samp>basic</samp>

- [`minecraft:movement.basic`](./components/movement.basic.md)组件。A collection of components.


///////

/////// define
`minecraft:movement.fly`：<samp>fly</samp>

- [`minecraft:movement.fly`](./components/movement.fly.md)组件。A collection of components.


///////

/////// define
`minecraft:movement.generic`：<samp>generic</samp>

- [`minecraft:movement.generic`](./components/movement.generic.md)组件。A collection of components.


///////

/////// define
`minecraft:movement.glide`：<samp>glide</samp>

- [`minecraft:movement.glide`](./components/movement.glide.md)组件。A collection of components.


///////

/////// define
`minecraft:movement.hover`：<samp>hover</samp>

- [`minecraft:movement.hover`](./components/movement.hover.md)组件。A collection of components.


///////

/////// define
`minecraft:movement.jump`：<samp>jump</samp>

- [`minecraft:movement.jump`](./components/movement.jump.md)组件。A collection of components.


///////

/////// define
`minecraft:movement.skip`：<samp>skip</samp>

- [`minecraft:movement.skip`](./components/movement.skip.md)组件。A collection of components.


///////

/////// define
`minecraft:movement.sway`：<samp>sway</samp>

- [`minecraft:movement.sway`](./components/movement.sway.md)组件。A collection of components.


///////

/////// define
`minecraft:movement`：<samp>attribute</samp>

- [`minecraft:movement`](./components/attribute.md)组件。A collection of components.


///////

/////// define
`minecraft:nameable`：<samp>nameable</samp>

- [`minecraft:nameable`](./components/nameable.md)组件。A collection of components.


///////

/////// define
`minecraft:navigation.climb`：<samp>climb</samp>

- [`minecraft:navigation.climb`](./components/navigation.climb.md)组件。A collection of components.


///////

/////// define
`minecraft:navigation.float`：<samp>float</samp>

- [`minecraft:navigation.float`](./components/navigation.float.md)组件。A collection of components.


///////

/////// define
`minecraft:navigation.fly`：<samp>fly</samp>

- [`minecraft:navigation.fly`](./components/navigation.fly.md)组件。A collection of components.


///////

/////// define
`minecraft:navigation.generic`：<samp>generic</samp>

- [`minecraft:navigation.generic`](./components/navigation.generic.md)组件。A collection of components.


///////

/////// define
`minecraft:navigation.hover`：<samp>hover</samp>

- [`minecraft:navigation.hover`](./components/navigation.hover.md)组件。A collection of components.


///////

/////// define
`minecraft:navigation.swim`：<samp>swim</samp>

- [`minecraft:navigation.swim`](./components/navigation.swim.md)组件。A collection of components.


///////

/////// define
`minecraft:navigation.walk`：<samp>walk</samp>

- [`minecraft:navigation.walk`](./components/navigation.walk.md)组件。A collection of components.


///////

/////// define
`minecraft:npc`：<samp>npc</samp>

- [`minecraft:npc`](./components/npc.md)组件。A collection of components.


///////

/////// define
`minecraft:on_death`：<samp>on_death</samp>

- [`minecraft:on_death`](./components/on_death.md)组件。A collection of components.


///////

/////// define
`minecraft:on_friendly_anger`：<samp>on_friendly_anger</samp>

- [`minecraft:on_friendly_anger`](./components/on_friendly_anger.md)组件。A collection of components.


///////

/////// define
`minecraft:on_hurt_by_player`：<samp>on_hurt_by_player</samp>

- [`minecraft:on_hurt_by_player`](./components/on_hurt_by_player.md)组件。A collection of components.


///////

/////// define
`minecraft:on_hurt`：<samp>on_hurt</samp>

- [`minecraft:on_hurt`](./components/on_hurt.md)组件。A collection of components.


///////

/////// define
`minecraft:on_ignite`：<samp>on_ignite</samp>

- [`minecraft:on_ignite`](./components/on_ignite.md)组件。A collection of components.


///////

/////// define
`minecraft:on_start_landing`：<samp>on_start_landing</samp>

- [`minecraft:on_start_landing`](./components/on_start_landing.md)组件。A collection of components.


///////

/////// define
`minecraft:on_start_takeoff`：<samp>on_start_takeoff</samp>

- [`minecraft:on_start_takeoff`](./components/on_start_takeoff.md)组件。A collection of components.


///////

/////// define
`minecraft:on_target_acquired`：<samp>on_target_acquired</samp>

- [`minecraft:on_target_acquired`](./components/on_target_acquired.md)组件。A collection of components.


///////

/////// define
`minecraft:on_target_escape`：<samp>on_target_escape</samp>

- [`minecraft:on_target_escape`](./components/on_target_escape.md)组件。A collection of components.


///////

/////// define
`minecraft:on_wake_with_owner`：<samp>on_wake_with_owner</samp>

- [`minecraft:on_wake_with_owner`](./components/on_wake_with_owner.md)组件。A collection of components.


///////

/////// define
`minecraft:out_of_control`：<samp>out_of_control</samp>

- [`minecraft:out_of_control`](./components/out_of_control.md)组件。A collection of components.


///////

/////// define
`minecraft:peek`：<samp>peek</samp>

- [`minecraft:peek`](./components/peek.md)组件。A collection of components.


///////

/////// define
`minecraft:persistent`：<samp>persistent</samp>

- [`minecraft:persistent`](./components/persistent.md)组件。A collection of components.


///////

/////// define
`minecraft:physics`：<samp>physics</samp>

- [`minecraft:physics`](./components/physics.md)组件。A collection of components.


///////

/////// define
`minecraft:player.exhaustion`：<samp>exhaustion</samp>

- [`minecraft:player.exhaustion`](./components/player.exhaustion.md)组件。A collection of components.


///////

/////// define
`minecraft:player.experience`：<samp>experience</samp>

- [`minecraft:player.experience`](./components/player.experience.md)组件。A collection of components.


///////

/////// define
`minecraft:player.level`：<samp>level</samp>

- [`minecraft:player.level`](./components/player.level.md)组件。A collection of components.


///////

/////// define
`minecraft:player.saturation`：<samp>saturation</samp>

- [`minecraft:player.saturation`](./components/player.saturation.md)组件。A collection of components.


///////

/////// define
`minecraft:preferred_path`：<samp>preferred_path</samp>

- [`minecraft:preferred_path`](./components/preferred_path.md)组件。A collection of components.


///////

/////// define
`minecraft:projectile`：<samp>projectile</samp>

- [`minecraft:projectile`](./components/projectile.md)组件。A collection of components.


///////

/////// define
`minecraft:push_through`：<samp>push_through</samp>

- [`minecraft:push_through`](./components/push_through.md)组件。A collection of components.


///////

/////// define
`minecraft:pushable`：<samp>pushable</samp>

- [`minecraft:pushable`](./components/pushable.md)组件。A collection of components.


///////

/////// define
`minecraft:raid_trigger`：<samp>raid_trigger</samp>

- [`minecraft:raid_trigger`](./components/raid_trigger.md)组件。A collection of components.


///////

/////// define
`minecraft:rail_movement`：<samp>rail_movement</samp>

- [`minecraft:rail_movement`](./components/rail_movement.md)组件。A collection of components.


///////

/////// define
`minecraft:rail_sensor`：<samp>rail_sensor</samp>

- [`minecraft:rail_sensor`](./components/rail_sensor.md)组件。A collection of components.


///////

/////// define
`minecraft:ravager_blocked`：<samp>ravager_blocked</samp>

- [`minecraft:ravager_blocked`](./components/ravager_blocked.md)组件。A collection of components.


///////

/////// define
`minecraft:rideable`：<samp>rideable</samp>

- [`minecraft:rideable`](./components/rideable.md)组件。A collection of components.


///////

/////// define
`minecraft:reflect_projectiles`：<samp>reflect_projectiles</samp>

- [`minecraft:reflect_projectiles`](./components/reflect_projectiles.md)组件。A collection of components.


///////

/////// define
`minecraft:scale_by_age`：<samp>scale_by_age</samp>

- [`minecraft:scale_by_age`](./components/scale_by_age.md)组件。A collection of components.


///////

/////// define
`minecraft:scale`：<samp>scale</samp>

- [`minecraft:scale`](./components/scale.md)组件。A collection of components.


///////

/////// define
`minecraft:scheduler`：<samp>scheduler</samp>

- [`minecraft:scheduler`](./components/scheduler.md)组件。A collection of components.


///////

/////// define
`minecraft:shareables`：<samp>shareables</samp>

- [`minecraft:shareables`](./components/shareables.md)组件。A collection of components.


///////

/////// define
`minecraft:shooter`：<samp>shooter</samp>

- [`minecraft:shooter`](./components/shooter.md)组件。A collection of components.


///////

/////// define
`minecraft:sittable`：<samp>sittable</samp>

- [`minecraft:sittable`](./components/sittable.md)组件。A collection of components.


///////

/////// define
`minecraft:skin_id`：<samp>skin_id</samp>

- [`minecraft:skin_id`](./components/skin_id.md)组件。A collection of components.


///////

/////// define
`minecraft:sound_volume`：<samp>sound_volume</samp>

- [`minecraft:sound_volume`](./components/sound_volume.md)组件。A collection of components.


///////

/////// define
`minecraft:spawn_entity`：<samp>spawn_entity</samp>

- [`minecraft:spawn_entity`](./components/spawn_entity.md)组件。A collection of components.


///////

/////// define
`minecraft:spell_effects`：<samp>spell_effects</samp>

- [`minecraft:spell_effects`](./components/spell_effects.md)组件。A collection of components.


///////

/////// define
`minecraft:strength`：<samp>strength</samp>

- [`minecraft:strength`](./components/strength.md)组件。A collection of components.


///////

/////// define
`minecraft:suspect_tracking`：<samp>suspect_tracking</samp>

- [`minecraft:suspect_tracking`](./components/suspect_tracking.md)组件。A collection of components.


///////

/////// define
`minecraft:tameable`：<samp>tameable</samp>

- [`minecraft:tameable`](./components/tameable.md)组件。A collection of components.


///////

/////// define
`minecraft:tamemount`：<samp>tamemount</samp>

- [`minecraft:tamemount`](./components/tamemount.md)组件。A collection of components.


///////

/////// define
`minecraft:target_nearby_sensor`：<samp>target_nearby_sensor</samp>

- [`minecraft:target_nearby_sensor`](./components/target_nearby_sensor.md)组件。A collection of components.


///////

/////// define
`minecraft:teleport`：<samp>teleport</samp>

- [`minecraft:teleport`](./components/teleport.md)组件。A collection of components.


///////

/////// define
`minecraft:tick_world`：<samp>tick_world</samp>

- [`minecraft:tick_world`](./components/tick_world.md)组件。A collection of components.


///////

/////// define
`minecraft:timer`：<samp>timer</samp>

- [`minecraft:timer`](./components/timer.md)组件。A collection of components.


///////

/////// define
`minecraft:trade_resupply`：<samp>trade_resupply</samp>

- [`minecraft:trade_resupply`](./components/trade_resupply.md)组件。A collection of components.


///////

/////// define
`minecraft:trade_table`：<samp>trade_table</samp>

- [`minecraft:trade_table`](./components/trade_table.md)组件。A collection of components.


///////

/////// define
`minecraft:trail`：<samp>trail</samp>

- [`minecraft:trail`](./components/trail.md)组件。A collection of components.


///////

/////// define
`minecraft:transformation`：<samp>transformation</samp>

- [`minecraft:transformation`](./components/transformation.md)组件。A collection of components.


///////

/////// define
`minecraft:transient`：<samp>transient</samp>

- [`minecraft:transient`](./components/transient.md)组件。A collection of components.


///////

/////// define
`minecraft:trust`：<samp>trust</samp>

- [`minecraft:trust`](./components/trust.md)组件。A collection of components.


///////

/////// define
`minecraft:trusting`：<samp>trusting</samp>

- [`minecraft:trusting`](./components/trusting.md)组件。A collection of components.


///////

/////// define
`minecraft:type_family`：<samp>type_family</samp>

- [`minecraft:type_family`](./components/type_family.md)组件。A collection of components.


///////

/////// define
`minecraft:underwater_movement`：<samp>attribute</samp>

- [`minecraft:underwater_movement`](./components/attribute.md)组件。A collection of components.


///////

/////// define
`minecraft:variable_max_auto_step`：<samp>variable_max_auto_step</samp>

- [`minecraft:variable_max_auto_step`](./components/variable_max_auto_step.md)组件。A collection of components.


///////

/////// define
`minecraft:variant`：<samp>variant</samp>

- [`minecraft:variant`](./components/variant.md)组件。A collection of components.


///////

/////// define
`minecraft:vibration_damper`：<samp>vibration_damper</samp>

- [`minecraft:vibration_damper`](./components/vibration_damper.md)组件。A collection of components.


///////

/////// define
`minecraft:vibration_listener`：<samp>vibration_listener</samp>

- [`minecraft:vibration_listener`](./components/vibration_listener.md)组件。A collection of components.


///////

/////// define
`minecraft:walk_animation_speed`：<samp>walk_animation_speed</samp>

- [`minecraft:walk_animation_speed`](./components/walk_animation_speed.md)组件。A collection of components.


///////

/////// define
`minecraft:wants_jockey`：<samp>wants_jockey</samp>

- [`minecraft:wants_jockey`](./components/wants_jockey.md)组件。A collection of components.


///////

/////// define
`minecraft:water_movement`：<samp>water_movement</samp>

- [`minecraft:water_movement`](./components/water_movement.md)组件。A collection of components.


///////

/////// define
`minecraft:behavior.admire_item`：<samp>admire_item</samp>

- [`minecraft:behavior.admire_item`](./components/admire_item.md)组件。A collection of components.


///////

/////// define
`minecraft:behavior.avoid_block`：<samp>avoid_block</samp>

- [`minecraft:behavior.avoid_block`](./components/avoid_block.md)组件。A collection of components.


///////

/////// define
`minecraft:behavior.avoid_mob_type`：<samp>avoid_mob_type</samp>

- [`minecraft:behavior.avoid_mob_type`](./components/avoid_mob_type.md)组件。A collection of components.


///////

/////// define
`minecraft:behavior.barter`：<samp>barter</samp>

- [`minecraft:behavior.barter`](./components/barter.md)组件。A collection of components.


///////

/////// define
`minecraft:behavior.beg`：<samp>beg</samp>

- [`minecraft:behavior.beg`](./components/beg.md)组件。A collection of components.


///////

/////// define
`minecraft:behavior.break_door`：<samp>break_door</samp>

- [`minecraft:behavior.break_door`](./components/break_door.md)组件。A collection of components.


///////

/////// define
`minecraft:behavior.breed`：<samp>breed</samp>

- [`minecraft:behavior.breed`](./components/breed.md)组件。A collection of components.


///////

/////// define
`minecraft:behavior.celebrate_survive`：<samp>celebrate_survive</samp>

- [`minecraft:behavior.celebrate_survive`](./components/celebrate_survive.md)组件。A collection of components.


///////

/////// define
`minecraft:behavior.celebrate`：<samp>celebrate</samp>

- [`minecraft:behavior.celebrate`](./components/celebrate.md)组件。A collection of components.


///////

/////// define
`minecraft:behavior.charge_attack`：<samp>charge_attack</samp>

- [`minecraft:behavior.charge_attack`](./components/charge_attack.md)组件。A collection of components.


///////

/////// define
`minecraft:behavior.charge_held_item`：<samp>charge_held_item</samp>

- [`minecraft:behavior.charge_held_item`](./components/charge_held_item.md)组件。A collection of components.


///////

/////// define
`minecraft:behavior.circle_around_anchor`：<samp>circle_around_anchor</samp>

- [`minecraft:behavior.circle_around_anchor`](./components/circle_around_anchor.md)组件。A collection of components.


///////

/////// define
`minecraft:behavior.controlled_by_player`：<samp>controlled_by_player</samp>

- [`minecraft:behavior.controlled_by_player`](./components/controlled_by_player.md)组件。A collection of components.


///////

/////// define
`minecraft:behavior.croak`：<samp>croak</samp>

- [`minecraft:behavior.croak`](./components/croak.md)组件。A collection of components.


///////

/////// define
`minecraft:behavior.defend_trusted_target`：<samp>defend_trusted_target</samp>

- [`minecraft:behavior.defend_trusted_target`](./components/defend_trusted_target.md)组件。A collection of components.


///////

/////// define
`minecraft:behavior.defend_village_target`：<samp>defend_village_target</samp>

- [`minecraft:behavior.defend_village_target`](./components/defend_village_target.md)组件。A collection of components.


///////

/////// define
`minecraft:behavior.delayed_attack`：<samp>delayed_attack</samp>

- [`minecraft:behavior.delayed_attack`](./components/delayed_attack.md)组件。A collection of components.


///////

/////// define
`minecraft:behavior.dig`：<samp>dig</samp>

- [`minecraft:behavior.dig`](./components/dig.md)组件。A collection of components.


///////

/////// define
`minecraft:behavior.door_interact`：<samp>door_interact</samp>

- [`minecraft:behavior.door_interact`](./components/door_interact.md)组件。A collection of components.


///////

/////// define
`minecraft:behavior.dragonchargeplayer`：<samp>dragonchargeplayer</samp>

- [`minecraft:behavior.dragonchargeplayer`](./components/dragonchargeplayer.md)组件。A collection of components.


///////

/////// define
`minecraft:behavior.dragondeath`：<samp>dragondeath</samp>

- [`minecraft:behavior.dragondeath`](./components/dragondeath.md)组件。A collection of components.


///////

/////// define
`minecraft:behavior.dragonflaming`：<samp>dragonflaming</samp>

- [`minecraft:behavior.dragonflaming`](./components/dragonflaming.md)组件。A collection of components.


///////

/////// define
`minecraft:behavior.dragonholdingpattern`：<samp>dragonholdingpattern</samp>

- [`minecraft:behavior.dragonholdingpattern`](./components/dragonholdingpattern.md)组件。A collection of components.


///////

/////// define
`minecraft:behavior.dragonlanding`：<samp>dragonlanding</samp>

- [`minecraft:behavior.dragonlanding`](./components/dragonlanding.md)组件。A collection of components.


///////

/////// define
`minecraft:behavior.dragonscanning`：<samp>dragonscanning</samp>

- [`minecraft:behavior.dragonscanning`](./components/dragonscanning.md)组件。A collection of components.


///////

/////// define
`minecraft:behavior.dragonstrafeplayer`：<samp>dragonstrafeplayer</samp>

- [`minecraft:behavior.dragonstrafeplayer`](./components/dragonstrafeplayer.md)组件。A collection of components.


///////

/////// define
`minecraft:behavior.dragontakeoff`：<samp>dragontakeoff</samp>

- [`minecraft:behavior.dragontakeoff`](./components/dragontakeoff.md)组件。A collection of components.


///////

/////// define
`minecraft:behavior.drink_milk`：<samp>drink_milk</samp>

- [`minecraft:behavior.drink_milk`](./components/drink_milk.md)组件。A collection of components.


///////

/////// define
`minecraft:behavior.drink_potion`：<samp>drink_potion</samp>

- [`minecraft:behavior.drink_potion`](./components/drink_potion.md)组件。A collection of components.


///////

/////// define
`minecraft:behavior.drop_item_for`：<samp>drop_item_for</samp>

- [`minecraft:behavior.drop_item_for`](./components/drop_item_for.md)组件。A collection of components.


///////

/////// define
`minecraft:behavior.eat_block`：<samp>eat_block</samp>

- [`minecraft:behavior.eat_block`](./components/eat_block.md)组件。A collection of components.


///////

/////// define
`minecraft:behavior.eat_carried_item`：<samp>eat_carried_item</samp>

- [`minecraft:behavior.eat_carried_item`](./components/eat_carried_item.md)组件。A collection of components.


///////

/////// define
`minecraft:behavior.eat_mob`：<samp>eat_mob</samp>

- [`minecraft:behavior.eat_mob`](./components/eat_mob.md)组件。A collection of components.


///////

/////// define
`minecraft:behavior.emerge`：<samp>emerge</samp>

- [`minecraft:behavior.emerge`](./components/emerge.md)组件。A collection of components.


///////

/////// define
`minecraft:behavior.enderman_leave_block`：<samp>enderman_leave_block</samp>

- [`minecraft:behavior.enderman_leave_block`](./components/enderman_leave_block.md)组件。A collection of components.


///////

/////// define
`minecraft:behavior.enderman_take_block`：<samp>enderman_take_block</samp>

- [`minecraft:behavior.enderman_take_block`](./components/enderman_take_block.md)组件。A collection of components.


///////

/////// define
`minecraft:behavior.equip_item`：<samp>equip_item</samp>

- [`minecraft:behavior.equip_item`](./components/equip_item.md)组件。A collection of components.


///////

/////// define
`minecraft:behavior.explore_outskirts`：<samp>explore_outskirts</samp>

- [`minecraft:behavior.explore_outskirts`](./components/explore_outskirts.md)组件。A collection of components.


///////

/////// define
`minecraft:behavior.fertilize_farm_block`：<samp>fertilize_farm_block</samp>

- [`minecraft:behavior.fertilize_farm_block`](./components/fertilize_farm_block.md)组件。A collection of components.


///////

/////// define
`minecraft:behavior.find_cover`：<samp>find_cover</samp>

- [`minecraft:behavior.find_cover`](./components/find_cover.md)组件。A collection of components.


///////

/////// define
`minecraft:behavior.find_mount`：<samp>find_mount</samp>

- [`minecraft:behavior.find_mount`](./components/find_mount.md)组件。A collection of components.


///////

/////// define
`minecraft:behavior.find_underwater_treasure`：<samp>find_underwater_treasure</samp>

- [`minecraft:behavior.find_underwater_treasure`](./components/find_underwater_treasure.md)组件。A collection of components.


///////

/////// define
`minecraft:behavior.fire_at_target`：<samp>fire_at_target</samp>

- [`minecraft:behavior.fire_at_target`](./components/fire_at_target.md)组件。A collection of components.


///////

/////// define
`minecraft:behavior.flee_sun`：<samp>flee_sun</samp>

- [`minecraft:behavior.flee_sun`](./components/flee_sun.md)组件。A collection of components.


///////

/////// define
`minecraft:behavior.float_wander`：<samp>float_wander</samp>

- [`minecraft:behavior.float_wander`](./components/float_wander.md)组件。A collection of components.


///////

/////// define
`minecraft:behavior.float`：<samp>float</samp>

- [`minecraft:behavior.float`](./components/float.md)组件。A collection of components.


///////

/////// define
`minecraft:behavior.follow_caravan`：<samp>follow_caravan</samp>

- [`minecraft:behavior.follow_caravan`](./components/follow_caravan.md)组件。A collection of components.


///////

/////// define
`minecraft:behavior.follow_mob`：<samp>follow_mob</samp>

- [`minecraft:behavior.follow_mob`](./components/follow_mob.md)组件。A collection of components.


///////

/////// define
`minecraft:behavior.follow_owner`：<samp>follow_owner</samp>

- [`minecraft:behavior.follow_owner`](./components/follow_owner.md)组件。A collection of components.


///////

/////// define
`minecraft:behavior.follow_parent`：<samp>follow_parent</samp>

- [`minecraft:behavior.follow_parent`](./components/follow_parent.md)组件。A collection of components.


///////

/////// define
`minecraft:behavior.follow_target_captain`：<samp>follow_target_captain</samp>

- [`minecraft:behavior.follow_target_captain`](./components/follow_target_captain.md)组件。A collection of components.


///////

/////// define
`minecraft:behavior.go_and_give_items_to_noteblock`：<samp>go_and_give_items_to_noteblock</samp>

- [`minecraft:behavior.go_and_give_items_to_noteblock`](./components/go_and_give_items_to_noteblock.md)组件。A collection of components.


///////

/////// define
`minecraft:behavior.go_and_give_items_to_owner`：<samp>go_and_give_items_to_owner</samp>

- [`minecraft:behavior.go_and_give_items_to_owner`](./components/go_and_give_items_to_owner.md)组件。A collection of components.


///////

/////// define
`minecraft:behavior.go_home`：<samp>go_home</samp>

- [`minecraft:behavior.go_home`](./components/go_home.md)组件。A collection of components.


///////

/////// define
`minecraft:behavior.guardian_attack`：<samp>guardian_attack</samp>

- [`minecraft:behavior.guardian_attack`](./components/guardian_attack.md)组件。A collection of components.


///////

/////// define
`minecraft:behavior.harvest_farm_block`：<samp>harvest_farm_block</samp>

- [`minecraft:behavior.harvest_farm_block`](./components/harvest_farm_block.md)组件。A collection of components.


///////

/////// define
`minecraft:behavior.hide`：<samp>hide</samp>

- [`minecraft:behavior.hide`](./components/hide.md)组件。A collection of components.


///////

/////// define
`minecraft:behavior.hold_ground`：<samp>hold_ground</samp>

- [`minecraft:behavior.hold_ground`](./components/hold_ground.md)组件。A collection of components.


///////

/////// define
`minecraft:behavior.hurt_by_target`：<samp>hurt_by_target</samp>

- [`minecraft:behavior.hurt_by_target`](./components/hurt_by_target.md)组件。A collection of components.


///////

/////// define
`minecraft:behavior.inspect_bookshelf`：<samp>inspect_bookshelf</samp>

- [`minecraft:behavior.inspect_bookshelf`](./components/inspect_bookshelf.md)组件。A collection of components.


///////

/////// define
`minecraft:behavior.investigate_suspicious_location`：<samp>investigate_suspicious_location</samp>

- [`minecraft:behavior.investigate_suspicious_location`](./components/investigate_suspicious_location.md)组件。A collection of components.


///////

/////// define
`minecraft:behavior.jump_around_target`：<samp>jump_around_target</samp>

- [`minecraft:behavior.jump_around_target`](./components/jump_around_target.md)组件。A collection of components.


///////

/////// define
`minecraft:behavior.jump_to_block`：<samp>jump_to_block</samp>

- [`minecraft:behavior.jump_to_block`](./components/jump_to_block.md)组件。A collection of components.


///////

/////// define
`minecraft:behavior.knockback_roar`：<samp>knockback_roar</samp>

- [`minecraft:behavior.knockback_roar`](./components/knockback_roar.md)组件。A collection of components.


///////

/////// define
`minecraft:behavior.lay_down`：<samp>lay_down</samp>

- [`minecraft:behavior.lay_down`](./components/lay_down.md)组件。A collection of components.


///////

/////// define
`minecraft:behavior.lay_egg`：<samp>lay_egg</samp>

- [`minecraft:behavior.lay_egg`](./components/lay_egg.md)组件。A collection of components.


///////

/////// define
`minecraft:behavior.leap_at_target`：<samp>leap_at_target</samp>

- [`minecraft:behavior.leap_at_target`](./components/leap_at_target.md)组件。A collection of components.


///////

/////// define
`minecraft:behavior.look_at_entity`：<samp>look_at_entity</samp>

- [`minecraft:behavior.look_at_entity`](./components/look_at_entity.md)组件。A collection of components.


///////

/////// define
`minecraft:behavior.look_at_player`：<samp>look_at_player</samp>

- [`minecraft:behavior.look_at_player`](./components/look_at_player.md)组件。A collection of components.


///////

/////// define
`minecraft:behavior.look_at_target`：<samp>look_at_target</samp>

- [`minecraft:behavior.look_at_target`](./components/look_at_target.md)组件。A collection of components.


///////

/////// define
`minecraft:behavior.look_at_trading_player`：<samp>look_at_trading_player</samp>

- [`minecraft:behavior.look_at_trading_player`](./components/look_at_trading_player.md)组件。A collection of components.


///////

/////// define
`minecraft:behavior.make_love`：<samp>make_love</samp>

- [`minecraft:behavior.make_love`](./components/make_love.md)组件。A collection of components.


///////

/////// define
`minecraft:behavior.melee_attack`：<samp>melee_attack</samp>

- [`minecraft:behavior.melee_attack`](./components/melee_attack.md)组件。A collection of components.


///////

/////// define
`minecraft:behavior.melee_box_attack`：<samp>melee_box_attack</samp>

- [`minecraft:behavior.melee_box_attack`](./components/melee_box_attack.md)组件。A collection of components.


///////

/////// define
`minecraft:behavior.mingle`：<samp>mingle</samp>

- [`minecraft:behavior.mingle`](./components/mingle.md)组件。A collection of components.


///////

/////// define
`minecraft:behavior.mount_pathing`：<samp>mount_pathing</samp>

- [`minecraft:behavior.mount_pathing`](./components/mount_pathing.md)组件。A collection of components.


///////

/////// define
`minecraft:behavior.move_indoors`：<samp>move_indoors</samp>

- [`minecraft:behavior.move_indoors`](./components/move_indoors.md)组件。A collection of components.


///////

/////// define
`minecraft:behavior.move_outdoors`：<samp>move_outdoors</samp>

- [`minecraft:behavior.move_outdoors`](./components/move_outdoors.md)组件。A collection of components.


///////

/////// define
`minecraft:behavior.move_through_village`：<samp>move_through_village</samp>

- [`minecraft:behavior.move_through_village`](./components/move_through_village.md)组件。A collection of components.


///////

/////// define
`minecraft:behavior.move_to_block`：<samp>move_to_block</samp>

- [`minecraft:behavior.move_to_block`](./components/move_to_block.md)组件。A collection of components.


///////

/////// define
`minecraft:behavior.move_to_land`：<samp>move_to_land</samp>

- [`minecraft:behavior.move_to_land`](./components/move_to_land.md)组件。A collection of components.


///////

/////// define
`minecraft:behavior.move_to_lava`：<samp>move_to_lava</samp>

- [`minecraft:behavior.move_to_lava`](./components/move_to_lava.md)组件。A collection of components.


///////

/////// define
`minecraft:behavior.move_to_liquid`：<samp>move_to_liquid</samp>

- [`minecraft:behavior.move_to_liquid`](./components/move_to_liquid.md)组件。A collection of components.


///////

/////// define
`minecraft:behavior.move_to_poi`：<samp>move_to_poi</samp>

- [`minecraft:behavior.move_to_poi`](./components/move_to_poi.md)组件。A collection of components.


///////

/////// define
`minecraft:behavior.move_to_random_block`：<samp>move_to_random_block</samp>

- [`minecraft:behavior.move_to_random_block`](./components/move_to_random_block.md)组件。A collection of components.


///////

/////// define
`minecraft:behavior.move_to_village`：<samp>move_to_village</samp>

- [`minecraft:behavior.move_to_village`](./components/move_to_village.md)组件。A collection of components.


///////

/////// define
`minecraft:behavior.move_to_water`：<samp>move_to_water</samp>

- [`minecraft:behavior.move_to_water`](./components/move_to_water.md)组件。A collection of components.


///////

/////// define
`minecraft:behavior.move_towards_dwelling_restriction`：<samp>move_towards_dwelling_restriction</samp>

- [`minecraft:behavior.move_towards_dwelling_restriction`](./components/move_towards_dwelling_restriction.md)组件。A collection of components.


///////

/////// define
`minecraft:behavior.move_towards_home_restriction`：<samp>move_towards_home_restriction</samp>

- [`minecraft:behavior.move_towards_home_restriction`](./components/move_towards_home_restriction.md)组件。A collection of components.


///////

/////// define
`minecraft:behavior.move_towards_restriction`：<samp>move_towards_restriction</samp>

- [`minecraft:behavior.move_towards_restriction`](./components/move_towards_restriction.md)组件。A collection of components.


///////

/////// define
`minecraft:behavior.move_towards_target`：<samp>move_towards_target</samp>

- [`minecraft:behavior.move_towards_target`](./components/move_towards_target.md)组件。A collection of components.


///////

/////// define
`minecraft:behavior.nap`：<samp>nap</samp>

- [`minecraft:behavior.nap`](./components/nap.md)组件。A collection of components.


///////

/////// define
`minecraft:behavior.nearest_attackable_target`：<samp>nearest_attackable_target</samp>

- [`minecraft:behavior.nearest_attackable_target`](./components/nearest_attackable_target.md)组件。A collection of components.


///////

/////// define
`minecraft:behavior.nearest_prioritized_attackable_target`：<samp>nearest_prioritized_attackable_target</samp>

- [`minecraft:behavior.nearest_prioritized_attackable_target`](./components/nearest_prioritized_attackable_target.md)组件。A collection of components.


///////

/////// define
`minecraft:behavior.ocelot_sit_on_block`：<samp>ocelot_sit_on_block</samp>

- [`minecraft:behavior.ocelot_sit_on_block`](./components/ocelot_sit_on_block.md)组件。A collection of components.


///////

/////// define
`minecraft:behavior.ocelotattack`：<samp>ocelotattack</samp>

- [`minecraft:behavior.ocelotattack`](./components/ocelotattack.md)组件。A collection of components.


///////

/////// define
`minecraft:behavior.offer_flower`：<samp>offer_flower</samp>

- [`minecraft:behavior.offer_flower`](./components/offer_flower.md)组件。A collection of components.


///////

/////// define
`minecraft:behavior.open_door`：<samp>open_door</samp>

- [`minecraft:behavior.open_door`](./components/open_door.md)组件。A collection of components.


///////

/////// define
`minecraft:behavior.owner_hurt_by_target`：<samp>owner_hurt_by_target</samp>

- [`minecraft:behavior.owner_hurt_by_target`](./components/owner_hurt_by_target.md)组件。A collection of components.


///////

/////// define
`minecraft:behavior.owner_hurt_target`：<samp>owner_hurt_target</samp>

- [`minecraft:behavior.owner_hurt_target`](./components/owner_hurt_target.md)组件。A collection of components.


///////

/////// define
`minecraft:behavior.panic`：<samp>panic</samp>

- [`minecraft:behavior.panic`](./components/panic.md)组件。A collection of components.


///////

/////// define
`minecraft:behavior.pet_sleep_with_owner`：<samp>pet_sleep_with_owner</samp>

- [`minecraft:behavior.pet_sleep_with_owner`](./components/pet_sleep_with_owner.md)组件。A collection of components.


///////

/////// define
`minecraft:behavior.pickup_items`：<samp>pickup_items</samp>

- [`minecraft:behavior.pickup_items`](./components/pickup_items.md)组件。A collection of components.


///////

/////// define
`minecraft:behavior.play_dead`：<samp>play_dead</samp>

- [`minecraft:behavior.play_dead`](./components/play_dead.md)组件。A collection of components.


///////

/////// define
`minecraft:behavior.play`：<samp>play</samp>

- [`minecraft:behavior.play`](./components/play.md)组件。A collection of components.


///////

/////// define
`minecraft:behavior.player_ride_tamed`：<samp>player_ride_tamed</samp>

- [`minecraft:behavior.player_ride_tamed`](./components/player_ride_tamed.md)组件。A collection of components.


///////

/////// define
`minecraft:behavior.raid_garden`：<samp>raid_garden</samp>

- [`minecraft:behavior.raid_garden`](./components/raid_garden.md)组件。A collection of components.


///////

/////// define
`minecraft:behavior.ram_attack`：<samp>ram_attack</samp>

- [`minecraft:behavior.ram_attack`](./components/ram_attack.md)组件。A collection of components.


///////

/////// define
`minecraft:behavior.random_breach`：<samp>random_breach</samp>

- [`minecraft:behavior.random_breach`](./components/random_breach.md)组件。A collection of components.


///////

/////// define
`minecraft:behavior.random_fly`：<samp>random_fly</samp>

- [`minecraft:behavior.random_fly`](./components/random_fly.md)组件。A collection of components.


///////

/////// define
`minecraft:behavior.random_hover`：<samp>random_hover</samp>

- [`minecraft:behavior.random_hover`](./components/random_hover.md)组件。A collection of components.


///////

/////// define
`minecraft:behavior.random_look_around_and_sit`：<samp>random_look_around_and_sit</samp>

- [`minecraft:behavior.random_look_around_and_sit`](./components/random_look_around_and_sit.md)组件。A collection of components.


///////

/////// define
`minecraft:behavior.random_look_around`：<samp>random_look_around</samp>

- [`minecraft:behavior.random_look_around`](./components/random_look_around.md)组件。A collection of components.


///////

/////// define
`minecraft:behavior.random_search_and_dig`：<samp>random_search_and_dig</samp>

- [`minecraft:behavior.random_search_and_dig`](./components/random_search_and_dig.md)组件。A collection of components.


///////

/////// define
`minecraft:behavior.random_sitting`：<samp>random_sitting</samp>

- [`minecraft:behavior.random_sitting`](./components/random_sitting.md)组件。A collection of components.


///////

/////// define
`minecraft:behavior.random_stroll`：<samp>random_stroll</samp>

- [`minecraft:behavior.random_stroll`](./components/random_stroll.md)组件。A collection of components.


///////

/////// define
`minecraft:behavior.random_swim`：<samp>random_swim</samp>

- [`minecraft:behavior.random_swim`](./components/random_swim.md)组件。A collection of components.


///////

/////// define
`minecraft:behavior.ranged_attack`：<samp>ranged_attack</samp>

- [`minecraft:behavior.ranged_attack`](./components/ranged_attack.md)组件。A collection of components.


///////

/////// define
`minecraft:behavior.receive_love`：<samp>receive_love</samp>

- [`minecraft:behavior.receive_love`](./components/receive_love.md)组件。A collection of components.


///////

/////// define
`minecraft:behavior.restrict_open_door`：<samp>restrict_open_door</samp>

- [`minecraft:behavior.restrict_open_door`](./components/restrict_open_door.md)组件。A collection of components.


///////

/////// define
`minecraft:behavior.restrict_sun`：<samp>restrict_sun</samp>

- [`minecraft:behavior.restrict_sun`](./components/restrict_sun.md)组件。A collection of components.


///////

/////// define
`minecraft:behavior.rise_to_liquid_level`：<samp>rise_to_liquid_level</samp>

- [`minecraft:behavior.rise_to_liquid_level`](./components/rise_to_liquid_level.md)组件。A collection of components.


///////

/////// define
`minecraft:behavior.roar`：<samp>roar</samp>

- [`minecraft:behavior.roar`](./components/roar.md)组件。A collection of components.


///////

/////// define
`minecraft:behavior.roll`：<samp>roll</samp>

- [`minecraft:behavior.roll`](./components/roll.md)组件。A collection of components.


///////

/////// define
`minecraft:behavior.run_around_like_crazy`：<samp>run_around_like_crazy</samp>

- [`minecraft:behavior.run_around_like_crazy`](./components/run_around_like_crazy.md)组件。A collection of components.


///////

/////// define
`minecraft:behavior.scared`：<samp>scared</samp>

- [`minecraft:behavior.scared`](./components/scared.md)组件。A collection of components.


///////

/////// define
`minecraft:behavior.send_event`：<samp>send_event</samp>

- [`minecraft:behavior.send_event`](./components/send_event.md)组件。A collection of components.


///////

/////// define
`minecraft:behavior.share_items`：<samp>share_items</samp>

- [`minecraft:behavior.share_items`](./components/share_items.md)组件。A collection of components.


///////

/////// define
`minecraft:behavior.silverfish_merge_with_stone`：<samp>silverfish_merge_with_stone</samp>

- [`minecraft:behavior.silverfish_merge_with_stone`](./components/silverfish_merge_with_stone.md)组件。A collection of components.


///////

/////// define
`minecraft:behavior.silverfish_wake_up_friends`：<samp>silverfish_wake_up_friends</samp>

- [`minecraft:behavior.silverfish_wake_up_friends`](./components/silverfish_wake_up_friends.md)组件。A collection of components.


///////

/////// define
`minecraft:behavior.skeleton_horse_trap`：<samp>skeleton_horse_trap</samp>

- [`minecraft:behavior.skeleton_horse_trap`](./components/skeleton_horse_trap.md)组件。A collection of components.


///////

/////// define
`minecraft:behavior.sleep`：<samp>sleep</samp>

- [`minecraft:behavior.sleep`](./components/sleep.md)组件。A collection of components.


///////

/////// define
`minecraft:behavior.slime_attack`：<samp>slime_attack</samp>

- [`minecraft:behavior.slime_attack`](./components/slime_attack.md)组件。A collection of components.


///////

/////// define
`minecraft:behavior.slime_float`：<samp>slime_float</samp>

- [`minecraft:behavior.slime_float`](./components/slime_float.md)组件。A collection of components.


///////

/////// define
`minecraft:behavior.slime_keep_on_jumping`：<samp>slime_keep_on_jumping</samp>

- [`minecraft:behavior.slime_keep_on_jumping`](./components/slime_keep_on_jumping.md)组件。A collection of components.


///////

/////// define
`minecraft:behavior.slime_random_direction`：<samp>slime_random_direction</samp>

- [`minecraft:behavior.slime_random_direction`](./components/slime_random_direction.md)组件。A collection of components.


///////

/////// define
`minecraft:behavior.snacking`：<samp>snacking</samp>

- [`minecraft:behavior.snacking`](./components/snacking.md)组件。A collection of components.


///////

/////// define
`minecraft:behavior.sneeze`：<samp>sneeze</samp>

- [`minecraft:behavior.sneeze`](./components/sneeze.md)组件。A collection of components.


///////

/////// define
`minecraft:behavior.sniff`：<samp>sniff</samp>

- [`minecraft:behavior.sniff`](./components/sniff.md)组件。A collection of components.


///////

/////// define
`minecraft:behavior.sonic_boom`：<samp>sonic_boom</samp>

- [`minecraft:behavior.sonic_boom`](./components/sonic_boom.md)组件。A collection of components.


///////

/////// define
`minecraft:behavior.squid_dive`：<samp>squid_dive</samp>

- [`minecraft:behavior.squid_dive`](./components/squid_dive.md)组件。A collection of components.


///////

/////// define
`minecraft:behavior.squid_flee`：<samp>squid_flee</samp>

- [`minecraft:behavior.squid_flee`](./components/squid_flee.md)组件。A collection of components.


///////

/////// define
`minecraft:behavior.squid_idle`：<samp>squid_idle</samp>

- [`minecraft:behavior.squid_idle`](./components/squid_idle.md)组件。A collection of components.


///////

/////// define
`minecraft:behavior.squid_move_away_from_ground`：<samp>squid_move_away_from_ground</samp>

- [`minecraft:behavior.squid_move_away_from_ground`](./components/squid_move_away_from_ground.md)组件。A collection of components.


///////

/////// define
`minecraft:behavior.squid_out_of_water`：<samp>squid_out_of_water</samp>

- [`minecraft:behavior.squid_out_of_water`](./components/squid_out_of_water.md)组件。A collection of components.


///////

/////// define
`minecraft:behavior.stalk_and_pounce_on_target`：<samp>stalk_and_pounce_on_target</samp>

- [`minecraft:behavior.stalk_and_pounce_on_target`](./components/stalk_and_pounce_on_target.md)组件。A collection of components.


///////

/////// define
`minecraft:behavior.stay_near_noteblock`：<samp>stay_near_noteblock</samp>

- [`minecraft:behavior.stay_near_noteblock`](./components/stay_near_noteblock.md)组件。A collection of components.


///////

/////// define
`minecraft:behavior.stay_while_sitting`：<samp>stay_while_sitting</samp>

- [`minecraft:behavior.stay_while_sitting`](./components/stay_while_sitting.md)组件。A collection of components.


///////

/////// define
`minecraft:behavior.stomp_attack`：<samp>stomp_attack</samp>

- [`minecraft:behavior.stomp_attack`](./components/stomp_attack.md)组件。A collection of components.


///////

/////// define
`minecraft:behavior.stomp_turtle_egg`：<samp>stomp_turtle_egg</samp>

- [`minecraft:behavior.stomp_turtle_egg`](./components/stomp_turtle_egg.md)组件。A collection of components.


///////

/////// define
`minecraft:behavior.stroll_towards_village`：<samp>stroll_towards_village</samp>

- [`minecraft:behavior.stroll_towards_village`](./components/stroll_towards_village.md)组件。A collection of components.


///////

/////// define
`minecraft:behavior.summon_entity`：<samp>summon_entity</samp>

- [`minecraft:behavior.summon_entity`](./components/summon_entity.md)组件。A collection of components.


///////

/////// define
`minecraft:behavior.swell`：<samp>swell</samp>

- [`minecraft:behavior.swell`](./components/swell.md)组件。A collection of components.


///////

/////// define
`minecraft:behavior.swim_idle`：<samp>swim_idle</samp>

- [`minecraft:behavior.swim_idle`](./components/swim_idle.md)组件。A collection of components.


///////

/////// define
`minecraft:behavior.swim_up_for_breath`：<samp>swim_up_for_breath</samp>

- [`minecraft:behavior.swim_up_for_breath`](./components/swim_up_for_breath.md)组件。A collection of components.


///////

/////// define
`minecraft:behavior.swim_wander`：<samp>swim_wander</samp>

- [`minecraft:behavior.swim_wander`](./components/swim_wander.md)组件。A collection of components.


///////

/////// define
`minecraft:behavior.swim_with_entity`：<samp>swim_with_entity</samp>

- [`minecraft:behavior.swim_with_entity`](./components/swim_with_entity.md)组件。A collection of components.


///////

/////// define
`minecraft:behavior.swoop_attack`：<samp>swoop_attack</samp>

- [`minecraft:behavior.swoop_attack`](./components/swoop_attack.md)组件。A collection of components.


///////

/////// define
`minecraft:behavior.take_flower`：<samp>take_flower</samp>

- [`minecraft:behavior.take_flower`](./components/take_flower.md)组件。A collection of components.


///////

/////// define
`minecraft:behavior.teleport_to_owner`：<samp>teleport_to_owner</samp>

- [`minecraft:behavior.teleport_to_owner`](./components/teleport_to_owner.md)组件。A collection of components.


///////

/////// define
`minecraft:behavior.move_around_target`：<samp>move_around_target</samp>

- [`minecraft:behavior.move_around_target`](./components/move_around_target.md)组件。A collection of components.


///////

/////// define
`minecraft:behavior.target_when_pushed`：<samp>target_when_pushed</samp>

- [`minecraft:behavior.target_when_pushed`](./components/target_when_pushed.md)组件。A collection of components.


///////

/////// define
`minecraft:behavior.tempt`：<samp>tempt</samp>

- [`minecraft:behavior.tempt`](./components/tempt.md)组件。A collection of components.


///////

/////// define
`minecraft:behavior.timer_flag_1`：<samp>timer_flag</samp>

- [`minecraft:behavior.timer_flag_1`](./components/timer_flag.md)组件。A collection of components.


///////

/////// define
`minecraft:behavior.timer_flag_2`：<samp>timer_flag</samp>

- [`minecraft:behavior.timer_flag_2`](./components/timer_flag.md)组件。A collection of components.


///////

/////// define
`minecraft:behavior.timer_flag_3`：<samp>timer_flag</samp>

- [`minecraft:behavior.timer_flag_3`](./components/timer_flag.md)组件。A collection of components.


///////

/////// define
`minecraft:behavior.trade_interest`：<samp>trade_interest</samp>

- [`minecraft:behavior.trade_interest`](./components/trade_interest.md)组件。A collection of components.


///////

/////// define
`minecraft:behavior.trade_with_player`：<samp>trade_with_player</samp>

- [`minecraft:behavior.trade_with_player`](./components/trade_with_player.md)组件。A collection of components.


///////

/////// define
`minecraft:behavior.vex_copy_owner_target`：<samp>vex_copy_owner_target</samp>

- [`minecraft:behavior.vex_copy_owner_target`](./components/vex_copy_owner_target.md)组件。A collection of components.


///////

/////// define
`minecraft:behavior.vex_random_move`：<samp>vex_random_move</samp>

- [`minecraft:behavior.vex_random_move`](./components/vex_random_move.md)组件。A collection of components.


///////

/////// define
`minecraft:behavior.wither_random_attack_pos_goal`：<samp>wither_random_attack_pos_goal</samp>

- [`minecraft:behavior.wither_random_attack_pos_goal`](./components/wither_random_attack_pos_goal.md)组件。A collection of components.


///////

/////// define
`minecraft:behavior.wither_target_highest_damage`：<samp>wither_target_highest_damage</samp>

- [`minecraft:behavior.wither_target_highest_damage`](./components/wither_target_highest_damage.md)组件。A collection of components.


///////

/////// define
`minecraft:behavior.work`：<samp>work</samp>

- [`minecraft:behavior.work`](./components/work.md)组件。A collection of components.


///////

/////// define
`minecraft:behavior.work_composter`：<samp>work_composter</samp>

- [`minecraft:behavior.work_composter`](./components/work_composter.md)组件。A collection of components.


///////

//////



/////


///// define
`components`：<samp>[components](#assets.schemas-blockception.behavior.entities.format.components.json)</samp>

- The components that are added as the foundation of the entity.


/////


///// define
`events`：<samp>events</samp> {#assets.schemas-blockception.behavior.entities.format.events.json}

- The events that the entity can run, these add or remove components_groups.


/////

```mcschema
events:
{
  object "minecraft:entity_transformed" : opt
  {
    filters "filters"
    trigger "trigger"
    object "add" : opt
    {
      array "component_groups" : opt
      {
        string "<any array element>" : opt
      }
    }
    object "remove" : opt
    {
    }
    array "randomize" : opt
    {
      object "<any array element>" : opt
      {
        filters "filters"
        trigger "trigger"
        object "add" : opt
        {
        }
        object "remove" : opt
        {
        }
        array "randomize" : opt
        {
          object "<any array element>" : opt
          {
          }
        }
        array "sequence" : opt
        {
          object "<any array element>" : opt
          {
          }
        }
        object "emit_vibration" : opt
        {
          string "vibration" : opt
        }
        object "set_property" : opt
        {
          ['string', 'number', 'integer', 'boolean'] "<any object property>" : opt
        }
        object "queue_command" : opt
        {
          string "command" : opt
          array "command" : opt
          {
            string "<any array element>" : opt
          }
        }
        number "weight" : opt
      }
    }
    array "sequence" : opt
    {
      object "<any array element>" : opt
      {
      }
    }
    object "execute_event_on_home_block" : opt
    {
      string "event" : opt
    }
    object "reset_target" : opt
    {
    }
    object "emit_vibration" : opt
    {
      string "vibration" : opt
    }
    object "set_property" : opt
    {
      ['string', 'number', 'integer', 'boolean'] "<any object property>" : opt
    }
    object "queue_command" : opt
    {
      string "command" : opt
      array "command" : opt
      {
        string "<any array element>" : opt
      }
    }
  }
  object "minecraft:entity_born" : opt
  {
  }
  object "minecraft:entity_spawned" : opt
  {
  }
  object "minecraft:on_prime" : opt
  {
  }
  object "<any object property>" : opt
  {
  }
}

```

///// html | div.result
////// define
`minecraft:entity_transformed`：<samp>object</samp>

- Event called on an entity that transforms into another entity.


//////

<div class="language-text highlight"><span class="filename"><code>minecraft:entity_transformed</code></span><pre id="__code_1"><span></span></pre></div>

////// html | div.result
/////// define
`filters`：<samp>filters</samp>

- 一个[过滤器组](./filter.md)。


///////


/////// define
`trigger`：<samp>trigger</samp> {#assets.schemas-blockception.behavior.entities.format.types.trigger.json}

- Triggers additional events.


///////

```mcschema
trigger:
string

```

/////// html | div.result

///////


```mcschema
trigger:
{
  string "event" : opt
  filters "filters"
  subject "target"
}

```

/////// html | div.result
//////// define
`event`：<samp>string</samp>

- The event to run when the conditions for this trigger are met.


////////


//////// define
`filters`：<samp>filters</samp>

- 一个[过滤器组](./filter.md)。The list of conditions for this trigger to execute.


////////


//////// define
`target`：<samp>subject</samp> {#assets.schemas-blockception.behavior.entities.filters.filters.types.subject.json}

- The target of the event.


////////

```mcschema
subject:
string

```

//////// html | div.result

////////



///////


```mcschema
trigger:
array
{
  object "<any array element>" : opt
  {
    string "event" : opt
    filters "filters"
    subject "target"
  }
}

```

/////// html | div.result
//////// define
`<any array element>`：<samp>object</samp>


////////

<div class="language-text highlight"><span class="filename"><code>&lt;any array element&gt;</code></span><pre id="__code_1"><span></span></pre></div>

//////// html | div.result

////////


///////




/////// define
`add`：<samp>object</samp>

- The components groups to add or remove.


///////

<div class="language-text highlight"><span class="filename"><code>add</code></span><pre id="__code_1"><span></span></pre></div>

/////// html | div.result
//////// define
`component_groups`：<samp>array</samp>

- The components groups to add or remove.


////////

<div class="language-text highlight"><span class="filename"><code>component_groups</code></span><pre id="__code_1"><span></span></pre></div>

//////// html | div.result
///////// define
`<any array element>`：<samp>string</samp>

- A reference to a component group.


/////////


////////


///////


/////// define
`remove`：<samp>object</samp>

- The components groups to add or remove.


///////

<div class="language-text highlight"><span class="filename"><code>remove</code></span><pre id="__code_1"><span></span></pre></div>

/////// html | div.result

///////


/////// define
`randomize`：<samp>array</samp>

- Randomly selects one of the following items based upon their weight and the total weights.


///////

<div class="language-text highlight"><span class="filename"><code>randomize</code></span><pre id="__code_1"><span></span></pre></div>

/////// html | div.result
//////// define
`<any array element>`：<samp>object</samp>

- Randomly selects one of the following items based upon their weight and the total weights.


////////

<div class="language-text highlight"><span class="filename"><code>&lt;any array element&gt;</code></span><pre id="__code_1"><span></span></pre></div>

//////// html | div.result
///////// define
`filters`：<samp>filters</samp>

- 一个[过滤器组](./filter.md)。


/////////


///////// define
`trigger`：<samp>[trigger](#assets.schemas-blockception.behavior.entities.format.types.trigger.json)</samp>

- Triggers additional events.


/////////


///////// define
`add`：<samp>object</samp>

- The components groups to add or remove.


/////////

<div class="language-text highlight"><span class="filename"><code>add</code></span><pre id="__code_1"><span></span></pre></div>

///////// html | div.result

/////////


///////// define
`remove`：<samp>object</samp>

- The components groups to add or remove.


/////////

<div class="language-text highlight"><span class="filename"><code>remove</code></span><pre id="__code_1"><span></span></pre></div>

///////// html | div.result

/////////


///////// define
`randomize`：<samp>array</samp>

- Randomly selects one of the following items based upon their weight and the total weights.


/////////

<div class="language-text highlight"><span class="filename"><code>randomize</code></span><pre id="__code_1"><span></span></pre></div>

///////// html | div.result
////////// define
`<any array element>`：<samp>object</samp>

- Randomly selects one of the following items based upon their weight and the total weights.


//////////

<div class="language-text highlight"><span class="filename"><code>&lt;any array element&gt;</code></span><pre id="__code_1"><span></span></pre></div>

////////// html | div.result

//////////


/////////


///////// define
`sequence`：<samp>array</samp>

- A series of filters and components to be added.


/////////

<div class="language-text highlight"><span class="filename"><code>sequence</code></span><pre id="__code_1"><span></span></pre></div>

///////// html | div.result
////////// define
`<any array element>`：<samp>object</samp>

- Filters and components to be added.


//////////

<div class="language-text highlight"><span class="filename"><code>&lt;any array element&gt;</code></span><pre id="__code_1"><span></span></pre></div>

////////// html | div.result

//////////


/////////


///////// define
`emit_vibration`：<samp>object</samp>

- UNDOCUMENTED


/////////

<div class="language-text highlight"><span class="filename"><code>emit_vibration</code></span><pre id="__code_1"><span></span></pre></div>

///////// html | div.result
////////// define
`vibration`：<samp>string</samp>


//////////


/////////


///////// define
`set_property`：<samp>object</samp>

- Sets a property on the entity.


/////////

<div class="language-text highlight"><span class="filename"><code>set_property</code></span><pre id="__code_1"><span></span></pre></div>

///////// html | div.result
////////// define
`<any object property>`：<samp>['string', 'number', 'integer', 'boolean']</samp>

- The value to set the property to.


//////////


/////////


///////// define
`queue_command`：<samp>object</samp>

- Queues a command to be executed.


/////////

<div class="language-text highlight"><span class="filename"><code>queue_command</code></span><pre id="__code_1"><span></span></pre></div>

///////// html | div.result
////////// define
`command`：<samp>string</samp>

- The command to execute.


//////////


////////// define
`command`：<samp>array</samp>

- The command to execute.


//////////

<div class="language-text highlight"><span class="filename"><code>command</code></span><pre id="__code_1"><span></span></pre></div>

////////// html | div.result
/////////// define
`<any array element>`：<samp>string</samp>

- The command to execute.


///////////


//////////



/////////


///////// define
`weight`：<samp>number</samp>

- The weight on how likely this section is to trigger.


/////////


////////


///////


/////// define
`sequence`：<samp>array</samp>

- A series of filters and components to be added.


///////

<div class="language-text highlight"><span class="filename"><code>sequence</code></span><pre id="__code_1"><span></span></pre></div>

/////// html | div.result
//////// define
`<any array element>`：<samp>object</samp>

- Filters and components to be added.


////////

<div class="language-text highlight"><span class="filename"><code>&lt;any array element&gt;</code></span><pre id="__code_1"><span></span></pre></div>

//////// html | div.result

////////


///////


/////// define
`execute_event_on_home_block`：<samp>object</samp>

- Allows the entity to execute an event on the block at its home position


///////

<div class="language-text highlight"><span class="filename"><code>execute_event_on_home_block</code></span><pre id="__code_1"><span></span></pre></div>

/////// html | div.result
//////// define
`event`：<samp>string</samp>

- The event to execute


////////


///////


/////// define
`reset_target`：<samp>object</samp>

- Allows an entity to reset its target.


///////

<div class="language-text highlight"><span class="filename"><code>reset_target</code></span><pre id="__code_1"><span></span></pre></div>

/////// html | div.result

///////


/////// define
`emit_vibration`：<samp>object</samp>

- UNDOCUMENTED


///////

<div class="language-text highlight"><span class="filename"><code>emit_vibration</code></span><pre id="__code_1"><span></span></pre></div>

/////// html | div.result
//////// define
`vibration`：<samp>string</samp>


////////


///////


/////// define
`set_property`：<samp>object</samp>

- Sets a property on the entity.


///////

<div class="language-text highlight"><span class="filename"><code>set_property</code></span><pre id="__code_1"><span></span></pre></div>

/////// html | div.result
//////// define
`<any object property>`：<samp>['string', 'number', 'integer', 'boolean']</samp>

- The value to set the property to.


////////


///////


/////// define
`queue_command`：<samp>object</samp>

- Queues a command to be executed.


///////

<div class="language-text highlight"><span class="filename"><code>queue_command</code></span><pre id="__code_1"><span></span></pre></div>

/////// html | div.result
//////// define
`command`：<samp>string</samp>

- The command to execute.


////////


//////// define
`command`：<samp>array</samp>

- The command to execute.


////////

<div class="language-text highlight"><span class="filename"><code>command</code></span><pre id="__code_1"><span></span></pre></div>

//////// html | div.result
///////// define
`<any array element>`：<samp>string</samp>

- The command to execute.


/////////


////////



///////


//////


////// define
`minecraft:entity_born`：<samp>object</samp>

- Event called on an entity that is spawned through two entities breeding.


//////

<div class="language-text highlight"><span class="filename"><code>minecraft:entity_born</code></span><pre id="__code_1"><span></span></pre></div>

////// html | div.result

//////


////// define
`minecraft:entity_spawned`：<samp>object</samp>

- Event called on an entity that is placed in the level.


//////

<div class="language-text highlight"><span class="filename"><code>minecraft:entity_spawned</code></span><pre id="__code_1"><span></span></pre></div>

////// html | div.result

//////


////// define
`minecraft:on_prime`：<samp>object</samp>

- Event called on an entity whose fuse is lit and is ready to explode.


//////

<div class="language-text highlight"><span class="filename"><code>minecraft:on_prime</code></span><pre id="__code_1"><span></span></pre></div>

////// html | div.result

//////


////// define
`<any object property>`：<samp>object</samp>


//////

<div class="language-text highlight"><span class="filename"><code>&lt;any object property&gt;</code></span><pre id="__code_1"><span></span></pre></div>

////// html | div.result

//////


/////



////



///

