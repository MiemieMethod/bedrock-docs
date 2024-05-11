# Avoid Mob Type

> 文档版本：1.21.0.24

Allows the entity to run away from other entities that meet the criteria specified.

## 架构

```mcschema
avoid_mob_type:
{
  priority "priority"
  sound_event "avoid_mob_sound"
  integer "avoid_target_xz" : opt
  integer "avoid_target_y" : opt
  boolean "ignore_visibilty" : opt
  number "max_dist" : opt
  number "max_flee" : opt
  number "probability_per_strength" : opt
  boolean "remove_target" : opt
  number "sprint_distance" : opt
  number "sprint_speed_multiplier" : opt
  number "walk_speed_multiplier" : opt
  boolean "ignore_visibility" : opt
  entity_types "entity_types"
  event "on_escape_event"
  array "sound_interval" : opt
  {
    number "0..0" : opt
    number "1..1" : opt
  }
  number "sound_interval" : opt
  object "sound_interval" : opt
  {
    number "range_min" : opt
    number "range_max" : opt
  }
}

```

/// html | div.result
//// define
`priority`：<samp>priority</samp> {#assets.schemas-blockception.behavior.entities.format.behaviors.types.priority.json}


////

```mcschema
priority:
integer

```

//// html | div.result

////



//// define
`avoid_mob_sound`：<samp>sound_event</samp> {#assets.schemas-blockception.general.sound_event.json}

- The sound event to play when the mob is avoiding another mob.


////

```mcschema
sound_event:
string

```

//// html | div.result

////



//// define
`avoid_target_xz`：<samp>integer</samp>

- The next target position the entity chooses to avoid another entity will be chosen within this XZ Distance.


////


//// define
`avoid_target_y`：<samp>integer</samp>

- The next target position the entity chooses to avoid another entity will be chosen within this Y Distance.


////


//// define
`ignore_visibilty`：<samp>boolean</samp>

- Whether or not to ignore direct line of sight while this entity is running away from other specified entities.


////


//// define
`max_dist`：<samp>number</samp>

- Maximum distance to look for an avoid target for the entity.


////


//// define
`max_flee`：<samp>number</samp>

- How many blocks away from its avoid target the entity must be for it to stop fleeing from the avoid target.


////


//// define
`probability_per_strength`：<samp>number</samp>

- Percent chance this entity will stop avoiding another entity based on that entity's strength, where 1.0 = 100%.


////


//// define
`remove_target`：<samp>boolean</samp>

- Determine if we should remove target when fleeing or not.


////


//// define
`sprint_distance`：<samp>number</samp>

- How many blocks within range of its avoid target the entity must be for it to begin sprinting away from the avoid target.


////


//// define
`sprint_speed_multiplier`：<samp>number</samp>

- Multiplier for sprint speed. 1.0 means keep the regular speed, while higher numbers make the sprint speed faster.


////


//// define
`walk_speed_multiplier`：<samp>number</samp>

- Multiplier for walking speed. 1.0 means keep the regular speed, while higher numbers make the walking speed faster.


////


//// define
`ignore_visibility`：<samp>boolean</samp>

- If true, visbility between this entity and the mob type will not be checked.


////


//// define
`entity_types`：<samp>entity_types</samp> {#assets.schemas-blockception.behavior.entities.format.types.entity_types.json}

- The list of conditions another entity must meet to be a valid target to avoid.


////

```mcschema
entity_types:
array
{
  object "<any array element>" : opt
  {
    filters "filters"
    number "cooldown" : opt
    number "max_dist" : opt
    number "max_height" : opt
    number "max_flee" : opt
    number "priority" : opt
    number "within_default" : opt
    boolean "check_if_outnumbered" : opt
    boolean "must_see" : opt
    number "must_see_forget_duration" : opt
    boolean "reevaluate_description" : opt
    number "sprint_speed_multiplier" : opt
    number "walk_speed_multiplier" : opt
  }
}

```

//// html | div.result
///// define
`<any array element>`：<samp>object</samp>

- The entity type.


/////

<div class="language-text highlight"><span class="filename"><code>&lt;any array element&gt;</code></span><pre id="__code_1"><span></span></pre></div>

///// html | div.result
////// define
`filters`：<samp>filters</samp>

- 一个[过滤器组](../filter.md)。


//////


////// define
`cooldown`：<samp>number</samp>

- The amount of time in seconds that the mob has to wait before selecting a target of the same type again


//////


////// define
`max_dist`：<samp>number</samp>

- Maximum distance this mob can be away to be a valid choice.


//////


////// define
`max_height`：<samp>number</samp>

- UNDOCUMENTED.


//////


////// define
`max_flee`：<samp>number</samp>

- UNDOCUMENTED.


//////


////// define
`priority`：<samp>number</samp>

- UNDOCUMENTED.


//////


////// define
`within_default`：<samp>number</samp>

- UNDOCUMENTED.


//////


////// define
`check_if_outnumbered`：<samp>boolean</samp>

- UNDOCUMENTED.


//////


////// define
`must_see`：<samp>boolean</samp>

- If true, the mob has to be visible to be a valid choice.


//////


////// define
`must_see_forget_duration`：<samp>number</samp>

- Determines the amount of time in seconds that this mob will look for a target before forgetting about it and looking for a new one when the target isn't visible any more.


//////


////// define
`reevaluate_description`：<samp>boolean</samp>

- If true, the mob will stop being targeted if it stops meeting any conditions.


//////


////// define
`sprint_speed_multiplier`：<samp>number</samp>

- Multiplier for the running speed. A value of 1.0 means the speed is unchanged


//////


////// define
`walk_speed_multiplier`：<samp>number</samp>

- Multiplier for the walking speed. A value of 1.0 means the speed is unchanged


//////


/////


////


```mcschema
entity_types:
{
  filters "filters"
  number "cooldown" : opt
  number "max_dist" : opt
  number "max_height" : opt
  number "max_flee" : opt
  number "priority" : opt
  number "within_default" : opt
  boolean "check_if_outnumbered" : opt
  boolean "must_see" : opt
  number "must_see_forget_duration" : opt
  boolean "reevaluate_description" : opt
  number "sprint_speed_multiplier" : opt
  number "walk_speed_multiplier" : opt
}

```

//// html | div.result

////




//// define
`on_escape_event`：<samp>event</samp> {#assets.schemas-blockception.behavior.entities.format.types.event.json}

- Event that is triggered when escaping from a mob.


////

```mcschema
event:
string

```

//// html | div.result

////


```mcschema
event:
{
  string "event" : opt
  string "target" : opt
}

```

//// html | div.result
///// define
`event`：<samp>string</samp>

- The event to fire.


/////


///// define
`target`：<samp>string</samp>

- The target of the event.


/////


////




//// define
`sound_interval`：<samp>array</samp>

- The range of time in seconds to randomly wait before playing the sound again.


////

<div class="language-text highlight"><span class="filename"><code>sound_interval</code></span><pre id="__code_1"><span></span></pre></div>

//// html | div.result
///// define
`0..0`：<samp>number</samp>


/////


///// define
`1..1`：<samp>number</samp>


/////


////


//// define
`sound_interval`：<samp>number</samp>

- The range of time in seconds to randomly wait before playing the sound again.


////


//// define
`sound_interval`：<samp>object</samp>

- The range of time in seconds to randomly wait before playing the sound again.


////

<div class="language-text highlight"><span class="filename"><code>sound_interval</code></span><pre id="__code_1"><span></span></pre></div>

//// html | div.result
///// define
`range_min`：<samp>number</samp>


/////


///// define
`range_max`：<samp>number</samp>


/////


////



///

