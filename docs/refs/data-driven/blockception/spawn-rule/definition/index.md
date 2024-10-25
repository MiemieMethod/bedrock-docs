# Spawn Rules

> 文档版本：1.21.50.25

Data-Driven spawning allows you to adjust the spawn conditions of mobs.

## 架构

```mcschema
spawn_rules:
{
  string "format_version" : opt
  object "minecraft:spawn_rules" : opt
  {
    object "description" : opt
    {
      identifier "identifier"
      string "population_control" : opt
    }
    array "conditions" : opt
    {
      object "<any array element>" : opt
      {
        biome_filter "minecraft:biome_filter"
        brightness_filter "minecraft:brightness_filter"
        Delay_filter "minecraft:delay_filter"
        density_limit "minecraft:density_limit"
        difficulty_filter "minecraft:difficulty_filter"
        disallow_spawns_in_bubble "minecraft:disallow_spawns_in_bubble"
        distance_filter "minecraft:distance_filter"
        height_filter "minecraft:height_filter"
        height_filter "minecraft:herd"
        mob_event_filter "minecraft:mob_event_filter"
        permute_type "minecraft:permute_type"
        player_in_village_filter "minecraft:player_in_village_filter"
        spawn_event "minecraft:spawn_event"
        spawns_above_block_filter "minecraft:spawns_above_block_filter"
        spawns_lava "minecraft:spawns_lava"
        spawns_on_block_filter "minecraft:spawns_on_block_filter"
        spawns_on_block_prevented_filter "minecraft:spawns_on_block_prevented_filter"
        spawns_on_surface "minecraft:spawns_on_surface"
        spawns_underground "minecraft:spawns_underground"
        spawns_underwater "minecraft:spawns_underwater"
        weight "minecraft:weight"
        world_age_filter "minecraft:world_age_filter"
      }
    }
  }
}

```

/// html | div.result
//// define
`format_version`：<samp>string</samp>

- A version that tells minecraft what type of data format can be expected when reading this file.


////


//// define
`minecraft:spawn_rules`：<samp>object</samp>

- Data-Driven spawning allows you to adjust the spawn conditions of mobs.


////

<div class="language-text highlight"><span class="filename"><code>minecraft:spawn_rules</code></span><pre id="__code_1"><span></span></pre></div>

//// html | div.result
///// define
`description`：<samp>object</samp>

- The descripton of to which entity this spawn rule belongs.


/////

<div class="language-text highlight"><span class="filename"><code>description</code></span><pre id="__code_1"><span></span></pre></div>

///// html | div.result
////// define
`identifier`：<samp>identifier</samp> {#assets.schemas-blockception.general.entity.identifier.json}

- The entity identifier this spawn rule will apply to, entity must exist.


//////

```mcschema
identifier:
string

```

////// html | div.result

//////



////// define
`population_control`：<samp>string</samp>

- Setting an entity to a pool it will spawn as long as that pool hasn't reached the spawn limit.


//////


/////


///// define
`conditions`：<samp>array</samp>

- UNDOCUMENTED.


/////

<div class="language-text highlight"><span class="filename"><code>conditions</code></span><pre id="__code_1"><span></span></pre></div>

///// html | div.result
////// define
`<any array element>`：<samp>object</samp>

- UNDOCUMENTED.


//////

<div class="language-text highlight"><span class="filename"><code>&lt;any array element&gt;</code></span><pre id="__code_1"><span></span></pre></div>

////// html | div.result
/////// define
`minecraft:biome_filter`：<samp>biome_filter</samp> {#assets.schemas-blockception.behavior.spawn_rules.components.biome_filter.json}


///////

```mcschema
biome_filter:
array
{
  filters "<any array element>"
}

```

/////// html | div.result
//////// define
`<any array element>`：<samp>filters</samp>

- 一个[过滤器组](./filter.md)。


////////


///////






/////// define
`minecraft:brightness_filter`：<samp>brightness_filter</samp> {#assets.schemas-blockception.behavior.spawn_rules.components.brightness_filter.json}


///////

```mcschema
brightness_filter:
{
  integer "min" : opt
  integer "max" : opt
  boolean "adjust_for_weather" : opt
}

```

/////// html | div.result
//////// define
`min`：<samp>integer</samp>

- This is the minimum light level value that allows the mob to spawn.


////////


//////// define
`max`：<samp>integer</samp>

- This is the maximum light level value that allows the mob to spawn.


////////


//////// define
`adjust_for_weather`：<samp>boolean</samp>

- This determines if weather can affect the light level conditions that cause the mob to spawn (e.g. Allowing hostile mobs to spawn during the day when it rains.)


////////


///////



/////// define
`minecraft:delay_filter`：<samp>Delay_filter</samp> {#assets.schemas-blockception.behavior.spawn_rules.components.delay_filter.json}


///////

```mcschema
Delay_filter:
{
  integer "min" : opt
  integer "max" : opt
  identifier "identifier"
  number "spawn_chance" : opt
}

```

/////// html | div.result
//////// define
`min`：<samp>integer</samp>

- This is the minimum delay that a mob spawns.


////////


//////// define
`max`：<samp>integer</samp>

- This is the maximum delay that a mob spawns.


////////


//////// define
`identifier`：<samp>[identifier](#assets.schemas-blockception.general.entity.identifier.json)</samp>

- The identifier of the mob that will spawn.


////////


//////// define
`spawn_chance`：<samp>number</samp>

- The percent chance that this entity will spawn.


////////


///////



/////// define
`minecraft:density_limit`：<samp>density_limit</samp> {#assets.schemas-blockception.behavior.spawn_rules.components.density_limit.json}


///////

```mcschema
density_limit:
{
  integer "surface" : opt
  integer "underground" : opt
}

```

/////// html | div.result
//////// define
`surface`：<samp>integer</samp>

- This is the maximum number of mobs of this type spawnable on the surface.


////////


//////// define
`underground`：<samp>integer</samp>

- This is the maximum number of mobs of this type spawnable underground.


////////


///////



/////// define
`minecraft:difficulty_filter`：<samp>difficulty_filter</samp> {#assets.schemas-blockception.behavior.spawn_rules.components.difficulty_filter.json}


///////

```mcschema
difficulty_filter:
{
  string "min" : opt
  string "max" : opt
}

```

/////// html | div.result
//////// define
`min`：<samp>string</samp>

- This is the minimum difficulty level that a mob spawns.


////////


//////// define
`max`：<samp>string</samp>

- This is the maximum difficulty level that a mob spawns.


////////


///////



/////// define
`minecraft:disallow_spawns_in_bubble`：<samp>disallow_spawns_in_bubble</samp> {#assets.schemas-blockception.behavior.spawn_rules.components.disallow_spawns_in_bubble.json}


///////

```mcschema
disallow_spawns_in_bubble:
{
}

```

/////// html | div.result

///////



/////// define
`minecraft:distance_filter`：<samp>distance_filter</samp> {#assets.schemas-blockception.behavior.spawn_rules.components.distance_filter.json}


///////

```mcschema
distance_filter:
{
  integer "min" : opt
  integer "max" : opt
}

```

/////// html | div.result
//////// define
`min`：<samp>integer</samp>

- This is the minimum distance level that a mob spawns.


////////


//////// define
`max`：<samp>integer</samp>

- This is the maximum distance level that a mob spawns.


////////


///////



/////// define
`minecraft:height_filter`：<samp>height_filter</samp> {#assets.schemas-blockception.behavior.spawn_rules.components.height_filter.json}


///////

```mcschema
height_filter:
{
  integer "min" : opt
  integer "max" : opt
}

```

/////// html | div.result
//////// define
`min`：<samp>integer</samp>

- This is the minimum height level that a mob spawns.


////////


//////// define
`max`：<samp>integer</samp>

- This is the maximum height level that a mob spawns.


////////


///////



/////// define
`minecraft:herd`：<samp>height_filter</samp> {#assets.schemas-blockception.behavior.spawn_rules.components.herd.json}


///////

```mcschema
height_filter:
{
  string "initial_event" : opt
  integer "initial_event_count" : opt
  integer "min_size" : opt
  integer "max_size" : opt
  string "event" : opt
  integer "event_skip_count" : opt
}

```

/////// html | div.result
//////// define
`initial_event`：<samp>string</samp>

- Runs an event on the first entities in a group.


////////


//////// define
`initial_event_count`：<samp>integer</samp>

- The number of entities that "initial_event" should trigger on.


////////


//////// define
`min_size`：<samp>integer</samp>

- This is the minimum number of mobs that spawn in a herd.


////////


//////// define
`max_size`：<samp>integer</samp>

- This is the maximum number of mobs that spawn in a herd.


////////


//////// define
`event`：<samp>string</samp>

- This is an event that can be triggered from spawning.


////////


//////// define
`event_skip_count`：<samp>integer</samp>

- This is the number of mobs spawned before the specified event is triggered.


////////


///////


```mcschema
height_filter:
array
{
  object "<any array element>" : opt
  {
    string "initial_event" : opt
    integer "initial_event_count" : opt
    integer "min_size" : opt
    integer "max_size" : opt
    string "event" : opt
    integer "event_skip_count" : opt
  }
}

```

/////// html | div.result
//////// define
`<any array element>`：<samp>object</samp>

- Herd.


////////

<div class="language-text highlight"><span class="filename"><code>&lt;any array element&gt;</code></span><pre id="__code_1"><span></span></pre></div>

//////// html | div.result

////////


///////




/////// define
`minecraft:mob_event_filter`：<samp>mob_event_filter</samp> {#assets.schemas-blockception.behavior.spawn_rules.components.mob_event_filter.json}


///////

```mcschema
mob_event_filter:
{
  string "event" : opt
}

```

/////// html | div.result
//////// define
`event`：<samp>string</samp>

- The event String in this JSON Object is used to filter the spawn rules of the mob type. Can be type minecraft:pillager_patrols_event, minecraft:wandering_trader_event, or minecraft:ender_dragon_event..


////////


///////



/////// define
`minecraft:permute_type`：<samp>permute_type</samp> {#assets.schemas-blockception.behavior.spawn_rules.components.permute_type.json}


///////

```mcschema
permute_type:
{
  integer "weight" : opt
  string "entity_type" : opt
  number "guaranteed_count" : opt
}

```

/////// html | div.result
//////// define
`weight`：<samp>integer</samp>

- The percentage of 100 of a type of mob that should spawn. If there are multiple weights, they must add up to 100.


////////


//////// define
`entity_type`：<samp>string</samp>

- The type of mob to spawn.


////////


//////// define
`guaranteed_count`：<samp>number</samp>

- Causes mobs to spawn with a guaranteed_count before mobs that do not have this spawn condition.


////////


///////


```mcschema
permute_type:
array
{
  object "<any array element>" : opt
  {
    integer "weight" : opt
    string "entity_type" : opt
    number "guaranteed_count" : opt
  }
}

```

/////// html | div.result
//////// define
`<any array element>`：<samp>object</samp>

- UNDOCUMENTED.


////////

<div class="language-text highlight"><span class="filename"><code>&lt;any array element&gt;</code></span><pre id="__code_1"><span></span></pre></div>

//////// html | div.result

////////


///////




/////// define
`minecraft:player_in_village_filter`：<samp>player_in_village_filter</samp> {#assets.schemas-blockception.behavior.spawn_rules.components.player_in_village_filter.json}


///////

```mcschema
player_in_village_filter:
{
  integer "distance" : opt
  integer "village_border_tolerance" : opt
}

```

/////// html | div.result
//////// define
`distance`：<samp>integer</samp>

- This is the maximum mob_event level that an entity spawns.


////////


//////// define
`village_border_tolerance`：<samp>integer</samp>

- This is the minimum mob_event level that an entity spawns.


////////


///////



/////// define
`minecraft:spawn_event`：<samp>spawn_event</samp> {#assets.schemas-blockception.behavior.spawn_rules.components.spawn_event.json}


///////

```mcschema
spawn_event:
{
  string "event" : opt
}

```

/////// html | div.result
//////// define
`event`：<samp>string</samp>

- UNDOCUMENTED.


////////


///////



/////// define
`minecraft:spawns_above_block_filter`：<samp>spawns_above_block_filter</samp> {#assets.schemas-blockception.behavior.spawn_rules.components.spawns_above_block_filter.json}


///////

```mcschema
spawns_above_block_filter:
{
  string "blocks" : opt
  array "blocks" : opt
  {
    string "<any array element>" : opt
  }
  number "distance" : opt
}

```

/////// html | div.result
//////// define
`blocks`：<samp>string</samp>

- UNDOCUMENTED.


////////


//////// define
`blocks`：<samp>array</samp>

- UNDOCUMENTED.


////////

<div class="language-text highlight"><span class="filename"><code>blocks</code></span><pre id="__code_1"><span></span></pre></div>

//////// html | div.result
///////// define
`<any array element>`：<samp>string</samp>


/////////


////////



//////// define
`distance`：<samp>number</samp>

- UNDOCUMENTED.


////////


///////



/////// define
`minecraft:spawns_lava`：<samp>spawns_lava</samp> {#assets.schemas-blockception.behavior.spawn_rules.components.spawns_lava.json}


///////

```mcschema
spawns_lava:
{
}

```

/////// html | div.result

///////



/////// define
`minecraft:spawns_on_block_filter`：<samp>spawns_on_block_filter</samp> {#assets.schemas-blockception.behavior.spawn_rules.components.spawns_on_block_filter.json}


///////

```mcschema
spawns_on_block_filter:
string

```

/////// html | div.result

///////


```mcschema
spawns_on_block_filter:
array
{
  string "<any array element>" : opt
}

```

/////// html | div.result
//////// define
`<any array element>`：<samp>string</samp>


////////


///////




/////// define
`minecraft:spawns_on_block_prevented_filter`：<samp>spawns_on_block_prevented_filter</samp> {#assets.schemas-blockception.behavior.spawn_rules.components.spawns_on_block_prevented_filter.json}


///////

```mcschema
spawns_on_block_prevented_filter:
string

```

/////// html | div.result

///////


```mcschema
spawns_on_block_prevented_filter:
array
{
  string "<any array element>" : opt
}

```

/////// html | div.result
//////// define
`<any array element>`：<samp>string</samp>


////////


///////




/////// define
`minecraft:spawns_on_surface`：<samp>spawns_on_surface</samp> {#assets.schemas-blockception.behavior.spawn_rules.components.spawns_on_surface.json}


///////

```mcschema
spawns_on_surface:
{
}

```

/////// html | div.result

///////



/////// define
`minecraft:spawns_underground`：<samp>spawns_underground</samp> {#assets.schemas-blockception.behavior.spawn_rules.components.spawns_underground.json}


///////

```mcschema
spawns_underground:
{
}

```

/////// html | div.result

///////



/////// define
`minecraft:spawns_underwater`：<samp>spawns_underwater</samp> {#assets.schemas-blockception.behavior.spawn_rules.components.spawns_underwater.json}


///////

```mcschema
spawns_underwater:
{
}

```

/////// html | div.result

///////



/////// define
`minecraft:weight`：<samp>weight</samp> {#assets.schemas-blockception.behavior.spawn_rules.components.weight.json}


///////

```mcschema
weight:
{
  integer "default" : opt
  integer "rarity" : opt
}

```

/////// html | div.result
//////// define
`default`：<samp>integer</samp>

- This is the priority of the mob spawning out of 100.


////////


//////// define
`rarity`：<samp>integer</samp>

- UNDOCUMENTED.


////////


///////



/////// define
`minecraft:world_age_filter`：<samp>world_age_filter</samp> {#assets.schemas-blockception.behavior.spawn_rules.components.world_age_filter.json}


///////

```mcschema
world_age_filter:
{
  integer "min" : opt
}

```

/////// html | div.result
//////// define
`min`：<samp>integer</samp>

- This is the minimum world_age_filter level that a mob spawns measured in seconds.


////////


///////



//////


/////


////


///

