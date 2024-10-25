# Follow Owner

> 文档版本：1.21.50.25

Allows the mob to follow the player that owns them.

## 架构

```mcschema
follow_owner:
{
  priority "priority"
  number "post_teleport_distance" : opt
  speed_multiplier "speed_multiplier"
  boolean "can_teleport" : opt
  boolean "ignore_vibration" : opt
  number "max_distance" : opt
  number "start_distance" : opt
  number "stop_distance" : opt
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
`post_teleport_distance`：<samp>number</samp>

- Defines how far (in blocks) the entity will be from its owner after teleporting. If not specified, it defaults to "stop_distance" + 1, allowing the entity to seamlessly resume navigation.


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
`can_teleport`：<samp>boolean</samp>

- Specify if the mob can teleport to the player if it is too far away.


////


//// define
`ignore_vibration`：<samp>boolean</samp>

- Specify if the mob will follow the owner if it has heard a vibration lately.


////


//// define
`max_distance`：<samp>number</samp>

- The maximum distance in blocks this mob can be from its owner to start following, only used when canTeleport is false.


////


//// define
`start_distance`：<samp>number</samp>

- The distance in blocks that the owner can be away from this mob before it starts following it.


////


//// define
`stop_distance`：<samp>number</samp>

- The distance in blocks this mob will stop from its owner while following it.


////


///

