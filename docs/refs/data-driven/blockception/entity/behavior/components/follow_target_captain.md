# Follow Target Captain

> 文档版本：1.21.50.25

Allows mob to move towards its current target captain.

## 架构

```mcschema
follow_target_captain:
{
  priority "priority"
  speed_multiplier "speed_multiplier"
  number "follow_distance" : opt
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
`follow_distance`：<samp>number</samp>

- Defines the distance in blocks the mob will stay from its target while following.


////


//// define
`within_radius`：<samp>number</samp>

- Defines the maximum distance in blocks a mob can get from its target captain before giving up trying to follow it.


////


///

