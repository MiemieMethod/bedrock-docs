# Open Door

> 文档版本：1.21.50.25

Allows the mob to open doors. Requires the mob to be able to path through doors, otherwise the mob won't even want to try opening them.

## 架构

```mcschema
open_door:
{
  priority "priority"
  boolean "close_door_after" : opt
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
`close_door_after`：<samp>boolean</samp>

- If true, the mob will close the door after opening it and going through it.


////


///

