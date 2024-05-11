# Move Through Village

> 文档版本：1.21.0.24

Can only be used by Villagers. Allows the villagers to create paths around the village.

## 架构

```mcschema
move_through_village:
{
  priority "priority"
  speed_multiplier "speed_multiplier"
  boolean "only_at_night" : opt
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
`only_at_night`：<samp>boolean</samp>

- If true, the mob will only move through the village during night time.


////


///

