# Move To Liquid

> 文档版本：1.21.50.25

Allows the mob to move into a liquid when on land.

## 架构

```mcschema
move_to_liquid:
{
  priority "priority"
  speed_multiplier "speed_multiplier"
  number "goal_radius" : opt
  integer "search_count" : opt
  integer "search_height" : opt
  integer "search_range" : opt
  string "material_type" : opt
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

- Distance in blocks within the mob considers it has reached the goal. This is the `wiggle room` to stop the AI from bouncing back and forth trying to reach a specific spot


////


//// define
`search_count`：<samp>integer</samp>

- The number of blocks each tick that the mob will check within it's search range and height for a valid block to move to. A value of 0 will have the mob check every block within range in one tick


////


//// define
`search_height`：<samp>integer</samp>

- Height in blocks the mob will look for lava to move towards.


////


//// define
`search_range`：<samp>integer</samp>

- The distance in blocks it will look for lava to move towards.


////


//// define
`material_type`：<samp>string</samp>

- The material type of the liquid block to find. Valid values are 'Any', 'Water', and 'Lava'.


////


///

