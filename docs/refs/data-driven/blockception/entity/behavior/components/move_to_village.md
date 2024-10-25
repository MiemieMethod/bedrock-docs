# Move To Village

> 文档版本：1.21.50.25

Allows the mob to move into a random location within a village.

## 架构

```mcschema
move_to_village:
{
  priority "priority"
  speed_multiplier "speed_multiplier"
  number "cooldown_time" : opt
  number "goal_radius" : opt
  integer "search_range" : opt
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
`cooldown_time`：<samp>number</samp>

- Time in seconds the mob has to wait before using the goal again.


////


//// define
`goal_radius`：<samp>number</samp>

- Distance in blocks within the mob considers it has reached the goal. This is the `wiggle room` to stop the AI from bouncing back and forth trying to reach a specific spot


////


//// define
`search_range`：<samp>integer</samp>

- The distance in blocks to search for villages. If <= 0, find the closest village regardless of distance.


////


///

