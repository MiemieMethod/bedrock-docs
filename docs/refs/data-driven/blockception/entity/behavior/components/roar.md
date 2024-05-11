# Roar

> 文档版本：1.21.0.24

[EXPERIMENTAL BEHAVIOR] Plays the provided sound and activates the `ROARING` actor flag during the specified duration

## 架构

```mcschema
roar:
{
  priority "priority"
  number "duration" : opt
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
`duration`：<samp>number</samp>

- Goal duration in seconds.


////


///

