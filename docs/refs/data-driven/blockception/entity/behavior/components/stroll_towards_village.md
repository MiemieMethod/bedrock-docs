# Stroll Towards Village

> 文档版本：1.21.50.25

Allows the mob to move into a random location within a village within the search range.

## 架构

```mcschema
stroll_towards_village:
{
  priority "priority"
  number "cooldown_time" : opt
  number "goal_radius" : opt
  integer "search_range" : opt
  number "speed_multiplier" : opt
  number "start_chance" : opt
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
`cooldown_time`：<samp>number</samp>

- Time in seconds the mob has to wait before using the goal again.


////


//// define
`goal_radius`：<samp>number</samp>

- Distance in blocks within the mob considers it has reached the goal. This is the `wiggle room` to stop the AI from bouncing back and forth trying to reach a specific spot


////


//// define
`search_range`：<samp>integer</samp>

- The distance in blocks to search for points inside villages. If <= 0, find the closest village regardless of distance.


////


//// define
`speed_multiplier`：<samp>number</samp>

- Movement speed multiplier of the mob when using this AI Goal.


////


//// define
`start_chance`：<samp>number</samp>

- This is the chance that the mob will start this goal, from 0 to 1.


////


///

