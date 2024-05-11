# Scared

> 文档版本：1.21.0.24

Allows the a mob to become scared when the weather outside is thundering.

## 架构

```mcschema
scared:
{
  priority "priority"
  integer "sound_interval" : opt
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
`sound_interval`：<samp>integer</samp>

- The interval in which a sound will play when active in a 1/delay chance to kick off.


////


///

