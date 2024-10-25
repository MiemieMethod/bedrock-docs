# Share Items

> 文档版本：1.21.50.25

Allows the mob to give items it has to others.

## 架构

```mcschema
share_items:
{
  priority "priority"
  speed_multiplier "speed_multiplier"
  entity_types "entity_types"
  number "goal_radius" : opt
  number "max_dist" : opt
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

- List of entities this mob will share items with.


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
`goal_radius`：<samp>number</samp>

- Distance in blocks within the mob considers it has reached the goal. This is the `wiggle room` to stop the AI from bouncing back and forth trying to reach a specific spot


////


//// define
`max_dist`：<samp>number</samp>

- Maximum distance in blocks this mob will look for entities to share items with.


////


///

