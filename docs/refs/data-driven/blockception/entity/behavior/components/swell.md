# Swell

> 文档版本：1.21.0.24

Allows the creeper to swell up when a player is nearby. It can only be used by Creepers.

## 架构

```mcschema
swell:
{
  priority "priority"
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
`start_distance`：<samp>number</samp>

- This mob starts swelling when a target is at least this many blocks away.


////


//// define
`stop_distance`：<samp>number</samp>

- This mob stops swelling when a target has moved away at least this many blocks.


////


///

