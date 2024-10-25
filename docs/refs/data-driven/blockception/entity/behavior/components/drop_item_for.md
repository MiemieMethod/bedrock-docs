# Drop Item For

> 文档版本：1.21.50.25

Allows the entity to move toward a target, and drop an item near the target. This goal requires a "minecraft:navigation" to execute.

## 架构

```mcschema
drop_item_for:
{
  priority "priority"
  speed_multiplier "speed_multiplier"
  entity_types "entity_types"
  number "cooldown" : opt
  number "drop_item_chance" : opt
  number "goal_radius" : opt
  string "loot_table" : opt
  number "max_head_look_at_height" : opt
  number "minimum_teleport_distance" : opt
  number "offering_distance" : opt
  trigger "on_drop_attempt"
  integer "search_count" : opt
  integer "search_height" : opt
  integer "search_range" : opt
  number "seconds_before_pickup" : opt
  vector_of_3_items "target_range"
  vector_of_3_items "teleport_offset"
  range_number_type "time_of_day_range"
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
`speed_multiplier`：<samp>speed_multiplier</samp> {#assets.schemas-blockception.behavior.entities.format.behaviors.types.speed_multiplier.json}


////

```mcschema
speed_multiplier:
number

```

//// html | div.result

////



//// define
`entity_types`：<samp>entity_types</samp> {#assets.schemas-blockception.behavior.entities.format.types.entity_types.json}

- The list of conditions another entity must meet to be a valid target to drop an item for.


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
`cooldown`：<samp>number</samp>

- Total time that the goal is on cooldown before it can be used again.


////


//// define
`drop_item_chance`：<samp>number</samp>

- The percent chance the entity will drop an item when using this goal.


////


//// define
`goal_radius`：<samp>number</samp>

- Distance in blocks within the entity considers it has reached it's target position.


////


//// define
`loot_table`：<samp>string</samp>

- The loot table that contains the possible loot the entity can drop with this goal.


////


//// define
`max_head_look_at_height`：<samp>number</samp>

- The maximum height the entities head will look at when dropping the item. The entity will always be looking at its target.


////


//// define
`minimum_teleport_distance`：<samp>number</samp>

- If the target position is farther away than this distance on any tick, the entity will teleport to the target position.


////


//// define
`offering_distance`：<samp>number</samp>

- The preferred distance the entity tries to be from the target it is dropping an item for.


////


//// define
`on_drop_attempt`：<samp>trigger</samp> {#assets.schemas-blockception.behavior.entities.format.types.trigger.json}

- The event to trigger when the entity attempts to drop an item.


////

```mcschema
trigger:
string

```

//// html | div.result

////


```mcschema
trigger:
{
  string "event" : opt
  filters "filters"
  subject "target"
}

```

//// html | div.result
///// define
`event`：<samp>string</samp>

- The event to run when the conditions for this trigger are met.


/////


///// define
`filters`：<samp>filters</samp>

- 一个[过滤器组](../filter.md)。The list of conditions for this trigger to execute.


/////


///// define
`target`：<samp>subject</samp> {#assets.schemas-blockception.behavior.entities.filters.filters.types.subject.json}

- The target of the event.


/////

```mcschema
subject:
string

```

///// html | div.result

/////



////


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

//// html | div.result
///// define
`<any array element>`：<samp>object</samp>


/////

<div class="language-text highlight"><span class="filename"><code>&lt;any array element&gt;</code></span><pre id="__code_1"><span></span></pre></div>

///// html | div.result

/////


////




//// define
`search_count`：<samp>integer</samp>

- The number of blocks each tick that the entity will check within its search range and height for a valid block to move to. A value of 0 will have the mob check every block within range in one tick.


////


//// define
`search_height`：<samp>integer</samp>

- The Height in blocks the entity will search within to find a valid target position.


////


//// define
`search_range`：<samp>integer</samp>

- The distance in blocks the entity will search within to find a valid target position.


////


//// define
`seconds_before_pickup`：<samp>number</samp>

- The numbers of seconds that will pass before the dropped entity can be picked up from the ground.


////


//// define
`target_range`：<samp>vector_of_3_items</samp> {#assets.schemas-blockception.general.vectors.number3.json}

- The range in blocks within which the entity searches to find a target to drop an item for.


////

```mcschema
vector_of_3_items:
array
{
  number "0..0" : opt
  number "1..1" : opt
  number "2..2" : opt
}

```

//// html | div.result
///// define
`0..0`：<samp>number</samp>

- The X component.


/////


///// define
`1..1`：<samp>number</samp>

- The Y component.


/////


///// define
`2..2`：<samp>number</samp>

- The Z component.


/////


////



//// define
`teleport_offset`：<samp>[vector_of_3_items](#assets.schemas-blockception.general.vectors.number3.json)</samp>

- When the entity teleports, offset the teleport position by this many blocks in the X, Y, and Z coordinate.


////


//// define
`time_of_day_range`：<samp>range_number_type</samp> {#assets.schemas-blockception.behavior.entities.format.types.range_number_type.json}

- The valid times of day that this goal can be used. For reference: noon is 0.0, sunset is 0.25, midnight is 0.5, and sunrise is 0.75, and back to noon for 1.0.


////

```mcschema
range_number_type:
number

```

//// html | div.result

////


```mcschema
range_number_type:
array
{
  number "0..0" : opt
  number "1..1" : opt
}

```

//// html | div.result
///// define
`0..0`：<samp>number</samp>

- The first value of the range.


/////


///// define
`1..1`：<samp>number</samp>

- The second value of the range.


/////


////


```mcschema
range_number_type:
{
  number "range_min" : opt
  number "range_max" : opt
}

```

//// html | div.result
///// define
`range_min`：<samp>number</samp>

- The minimum value of the range.


/////


///// define
`range_max`：<samp>number</samp>

- The maximum value of the range.


/////


////




///

