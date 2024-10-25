# Move Outdoors

> 文档版本：1.21.50.25

Forces the entity to move `outside`, whatever that means.

## 架构

```mcschema
move_outdoors:
{
  priority "priority"
  speed_multiplier "speed_multiplier"
  number "goal_radius" : opt
  integer "search_count" : opt
  integer "search_height" : opt
  integer "search_range" : opt
  number "timeout_cooldown" : opt
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
`goal_radius`：<samp>number</samp>

- The radius away from the target block to count as reaching the goal.


////


//// define
`search_count`：<samp>integer</samp>

- The amount of times to try finding a random outdoors position before failing.


////


//// define
`search_height`：<samp>integer</samp>

- The y range to search for an outdoors position for.


////


//// define
`search_range`：<samp>integer</samp>

- The x and z range to search for an outdoors position for.


////


//// define
`timeout_cooldown`：<samp>number</samp>

- The cooldown time in seconds before the goal can be reused after pathfinding fails.


////


///

