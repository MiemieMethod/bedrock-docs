# Fertilize Farm Block

> 文档版本：1.21.50.25

Allows the mob to search within an area for a growable crop block. If found, the mob will use any available fertilizer in their inventory on the crop. This goal will not execute if the mob does not have a fertilizer item in its inventory.

## 架构

```mcschema
fertilize_farm_block:
{
  priority "priority"
  speed_multiplier "speed_multiplier"
  number "goal_radius" : opt
  integer "max_fertilizer_usage" : opt
  number "search_cooldown_max_seconds" : opt
  integer "search_count" : opt
  integer "search_height" : opt
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
`goal_radius`：<samp>number</samp>

- Distance in blocks within the mob considers it has reached it's target position.


////


//// define
`max_fertilizer_usage`：<samp>integer</samp>

- The maximum number of times the mob will use fertilzer on the target block.


////


//// define
`search_cooldown_max_seconds`：<samp>number</samp>

- The maximum amount of time in seconds that the goal can take before searching again. The time is chosen between 0 and this number.


////


//// define
`search_count`：<samp>integer</samp>

- The number of randomly selected blocks each tick that the mob will check within its search range and height for a valid block to move to. A value of 0 will have the mob check every block within range in one tick.


////


//// define
`search_height`：<samp>integer</samp>

- The Height in blocks the mob will search within to find a valid target position.


////


//// define
`search_range`：<samp>integer</samp>

- The distance in blocks the mob will search within to find a valid target position.


////


///

