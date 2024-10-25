# Move Towards Target

> 文档版本：1.21.50.25

Allows mob to move towards its current target.

## 架构

```mcschema
move_towards_target:
{
  priority "priority"
  speed_multiplier "speed_multiplier"
  number "within_radius" : opt
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
`within_radius`：<samp>number</samp>

- Defines the radius in blocks that the mob tries to be from the target. A value of 0 means it tries to occupy the same block as the target


////


///

