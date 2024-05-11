# Swim Idle

> 文档版本：1.21.0.24

Allows the entity go idle, if swimming. Entity must be in water.

## 架构

```mcschema
swim_idle:
{
  priority "priority"
  number "idle_time" : opt
  number "success_rate" : opt
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
`idle_time`：<samp>number</samp>

- Amount of time (in seconds) to stay idle.


////


//// define
`success_rate`：<samp>number</samp>

- Percent chance this entity will go idle, 1.0 = 100%.


////


///

