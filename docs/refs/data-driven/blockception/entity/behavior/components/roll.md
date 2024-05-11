# Roll

> 文档版本：1.21.0.24

This allows the mob to roll forward.

## 架构

```mcschema
roll:
{
  priority "priority"
  number "probability" : opt
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
`probability`：<samp>number</samp>

- The probability that the mob will use the goal.


////


///

