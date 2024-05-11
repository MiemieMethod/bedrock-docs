# Swim With Entity

> 文档版本：1.21.0.24

Allows the entity follow another entity. Both entities must be swimming and in water.

## 架构

```mcschema
swim_with_entity:
{
  priority "priority"
  speed_multiplier "speed_multiplier"
  number "success_rate" : opt
  number "chance_to_stop" : opt
  number "state_check_interval" : opt
  number "catch_up_threshold" : opt
  number "match_direction_threshold" : opt
  number "catch_up_multiplier" : opt
  number "search_range" : opt
  number "stop_distance" : opt
  entity_types "entity_types"
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
`success_rate`：<samp>number</samp>

- Percent chance to start following another entity, if not already doing so. 1.0 = 100%


////


//// define
`chance_to_stop`：<samp>number</samp>

- Percent chance to stop following the current entity, if they're riding another entity or they're not swimming. 1.0 = 100%


////


//// define
`state_check_interval`：<samp>number</samp>

- Time (in seconds) between checks to determine if this entity should catch up to the entity being followed or match the direction of the entity being followed.


////


//// define
`catch_up_threshold`：<samp>number</samp>

- Distance, from the entity being followed, at which this entity will speed up to reach that entity.


////


//// define
`match_direction_threshold`：<samp>number</samp>

- Distance, from the entity being followed, at which this entity will try to match that entity's direction.


////


//// define
`catch_up_multiplier`：<samp>number</samp>

- The multiplier this entity's speed is modified by when matching another entity's direction.


////


//// define
`search_range`：<samp>number</samp>

- Radius around this entity to search for another entity to follow.


////


//// define
`stop_distance`：<samp>number</samp>

- Distance, from the entity being followed, at which this entity will stop following that entity.


////


//// define
`entity_types`：<samp>entity_types</samp> {#assets.schemas-blockception.behavior.entities.format.types.entity_types.json}

- Filters which determine what entites are valid to follow.


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




///

