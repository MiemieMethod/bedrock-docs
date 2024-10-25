# Lay Down

> 文档版本：1.21.50.25

Allows mobs to lay down at times.

## 架构

```mcschema
lay_down:
{
  priority "priority"
  integer "interval" : opt
  integer "random_stop_interval" : opt
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
`interval`：<samp>integer</samp>

- A random value to determine at what intervals something can occur. This has a 1/interval chance to choose this goal


////


//// define
`random_stop_interval`：<samp>integer</samp>

- A random value in which the goal can use to pull out of the behavior. This is a 1/interval chance to play the sound


////


///

