# Random Swim

> 文档版本：1.21.50.25

Allows an entity to randomly move through water.

## 架构

```mcschema
random_swim:
{
  priority "priority"
  speed_multiplier "speed_multiplier"
  boolean "avoid_surface" : opt
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
`avoid_surface`：<samp>boolean</samp>

- If true, the mob will avoid surface water blocks by swimming below them.


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

