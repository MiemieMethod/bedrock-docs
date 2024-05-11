# Harvest Farm Block

> 文档版本：1.21.0.24

Allows the entity to search within an area for farmland with air above it. If found, the entity will replace the air block by planting a seed item from its inventory on the farmland block. This goal requires "minecraft:inventory" and "minecraft:navigation" to execute. This goal will not execute if the entity does not have an item in its inventory.

## 架构

```mcschema
harvest_farm_block:
{
  priority "priority"
  speed_multiplier "speed_multiplier"
  number "max_seconds_before_search" : opt
  number "search_cooldown_max_seconds" : opt
  integer "search_count" : opt
  integer "search_height" : opt
  integer "search_range" : opt
  number "seconds_until_new_task" : opt
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
`max_seconds_before_search`：<samp>number</samp>

- The maximum amount of time in seconds that the goal can take before searching for the first harvest block. The time is chosen between 0 and this number.


////


//// define
`search_cooldown_max_seconds`：<samp>number</samp>

- The maximum amount of time in seconds that the goal can take before searching again, after failing to find a a harvest block already. The time is chosen between 0 and this number.


////


//// define
`search_count`：<samp>integer</samp>

- The number of randomly selected blocks each tick that the entity will check within its search range and height for a valid block to move to. A value of 0 will have the mob check every block within range in one tick.


////


//// define
`search_height`：<samp>integer</samp>

- The height in blocks the entity will search within to find a valid target position.


////


//// define
`search_range`：<samp>integer</samp>

- The distance in blocks the entity will search within to find a valid target position.


////


//// define
`seconds_until_new_task`：<samp>number</samp>

- The amount of time in seconds that the goal will cooldown after a successful reap/sow, before it can start again.


////


///

