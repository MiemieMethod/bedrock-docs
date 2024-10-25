# Move Towards Home Restriction

> 文档版本：1.21.50.25

Allows mobs with the home component to move toward their pre-defined area that the mob should be restricted to.

## 架构

```mcschema
move_towards_home_restriction:
{
  priority "priority"
  speed_multiplier "speed_multiplier"
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



///

