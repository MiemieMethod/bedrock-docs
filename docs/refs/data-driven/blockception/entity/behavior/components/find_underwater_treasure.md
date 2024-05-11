# Find Underwater Treasure

> 文档版本：1.21.0.24

Allows the mob to move towards the nearest underwater ruin or shipwreck.

## 架构

```mcschema
find_underwater_treasure:
{
  priority "priority"
  speed_multiplier "speed_multiplier"
  integer "search_range" : opt
  number "stop_distance" : opt
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
`search_range`：<samp>integer</samp>

- The range that the mob will search for a treasure chest within a ruin or shipwreck to move towards.


////


//// define
`stop_distance`：<samp>number</samp>

- The distance the mob will move before stopping.


////


///

