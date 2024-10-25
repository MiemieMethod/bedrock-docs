# Find Cover

> 文档版本：1.21.50.25

Allows the mob to seek shade.

## 架构

```mcschema
find_cover:
{
  priority "priority"
  speed_multiplier "speed_multiplier"
  number "cooldown_time" : opt
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


///

