# Float

> 文档版本：1.21.50.25

Allows the mob to stay afloat while swimming.

## 架构

```mcschema
float:
{
  priority "priority"
  boolean "sink_with_passengers" : opt
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
`sink_with_passengers`：<samp>boolean</samp>

- If true, the mob will keep sinking as long as it has passengers.


////


///

