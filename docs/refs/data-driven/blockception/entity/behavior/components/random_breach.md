# Random Breach

> 文档版本：1.21.0.24

Allows the mob to randomly break surface of the water.

## 架构

```mcschema
random_breach:
{
  priority "priority"
  speed_multiplier "speed_multiplier"
  number "cooldown_time" : opt
  integer "interval" : opt
  integer "xz_dist" : opt
  integer "y_dist" : opt
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
`interval`：<samp>integer</samp>

- A random value to determine when to randomly move somewhere. This has a 1/interval chance to choose this goal


////


//// define
`xz_dist`：<samp>integer</samp>

- Distance in blocks on ground that the mob will look for a new spot to move to. Must be at least 1


////


//// define
`y_dist`：<samp>integer</samp>

- Distance in blocks that the mob will look up or down for a new spot to move to. Must be at least 1


////


///

