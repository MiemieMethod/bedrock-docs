# On Fall On

> 文档版本：1.21.0.24

[Experimental] Describes event for this block.

## 架构

```mcschema
on_fall_on:
{
  string "condition" : opt
  string "event" : opt
  number "min_fall_distance" : opt
  string "target" : opt
}

```

/// html | div.result
//// define
`condition`：<samp>string</samp>

- The condition of event to be executed on the block.


////


//// define
`event`：<samp>string</samp>

- The event executed on the block.


////


//// define
`min_fall_distance`：<samp>number</samp>

- The minimum distance in blocks that an actor needs to fall to trigger this event.


////


//// define
`target`：<samp>string</samp>

- The target of event executed on the block.


////


///

