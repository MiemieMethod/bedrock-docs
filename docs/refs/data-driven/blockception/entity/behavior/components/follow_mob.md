# Follow Mob

> 文档版本：1.21.50.25

Allows the mob to follow other mobs.

## 架构

```mcschema
follow_mob:
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

- The distance in blocks it will look for a mob to follow.


////


//// define
`stop_distance`：<samp>number</samp>

- The distance in blocks this mob stops from the mob it is following.


////


///

