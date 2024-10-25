# Stay Near Noteblock

> 文档版本：1.21.50.25

[EXPERIMENTAL BEHAVIOR] The entity will attempt to toss the items from its inventory to a nearby recently played noteblock.

## 架构

```mcschema
stay_near_noteblock:
{
  priority "priority"
  integer "listen_time" : opt
  number "speed" : opt
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
`listen_time`：<samp>integer</samp>

- Sets the time an entity should stay near a noteblock after hearing it.


////


//// define
`speed`：<samp>number</samp>

- Sets the entity's speed when moving toward the block.


////


//// define
`start_distance`：<samp>number</samp>

- Sets the distance the entity needs to be away from the block to attempt to start the goal.


////


//// define
`stop_distance`：<samp>number</samp>

- Sets the distance from the block the entity will attempt to reach.


////


///

