# Slime Random Direction

> 文档版本：1.21.0.24

Can only be used by Slimes and Magma Cubes. Allows the mob to move in random directions like a slime.

## 架构

```mcschema
slime_random_direction:
{
  priority "priority"
  integer "add_random_time_range" : opt
  number "min_change_direction_time" : opt
  integer "turn_range" : opt
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
`add_random_time_range`：<samp>integer</samp>

- Additional time (in whole seconds), chosen randomly in the range of [0, "add_random_time_range"], to add to "min_change_direction_time".


////


//// define
`min_change_direction_time`：<samp>number</samp>

- Constant minimum time (in seconds) to wait before choosing a new direction.


////


//// define
`turn_range`：<samp>integer</samp>

- Maximum rotation angle range (in degrees) when randomly choosing a new direction.


////


///

