# Mount Pathing

> 文档版本：1.21.0.24

Allows the mob to move around on its own while mounted seeking a target to attack.

## 架构

```mcschema
mount_pathing:
{
  priority "priority"
  speed_multiplier "speed_multiplier"
  number "target_dist" : opt
  boolean "track_target" : opt
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
`target_dist`：<samp>number</samp>

- The distance at which this mob wants to be away from its target.


////


//// define
`track_target`：<samp>boolean</samp>

- If true, this mob will chase after the target as long as it's a valid target.


////


///

