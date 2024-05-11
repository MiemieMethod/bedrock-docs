# Move Indoors

> 文档版本：1.21.0.24

Can only be used by Villagers. Allows them to seek shelter indoors.

## 架构

```mcschema
move_indoors:
{
  priority "priority"
  speed_multiplier "speed_multiplier"
  number "timeout_cooldown" : opt
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
`timeout_cooldown`：<samp>number</samp>

- The cooldown time in seconds before the goal can be reused after pathfinding fails.


////


///

