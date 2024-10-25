# Dragonflaming

> 文档版本：1.21.50.25

Allows this entity to use a flame-breath attack. Note: This behavior can only be used by the ender_dragon entity type.

## 架构

```mcschema
dragonflaming:
{
  priority "priority"
  number "cooldown_time" : opt
  number "flame_time" : opt
  integer "ground_flame_count" : opt
  number "roar_time" : opt
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
`cooldown_time`：<samp>number</samp>

- Time (in seconds), after roar, to breath flame.


////


//// define
`flame_time`：<samp>number</samp>

- Time (in seconds), after roar, to breath flame.


////


//// define
`ground_flame_count`：<samp>integer</samp>

- Number of ground flame-breath attacks to use before flight-takeoff.


////


//// define
`roar_time`：<samp>number</samp>

- Time (in seconds) to roar, before breathing flame.


////


///

