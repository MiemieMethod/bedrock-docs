# minecraft:use_modifiers

> 文档版本：1.21.0.24

This component modifies use effects, including how long the item takes to use and the player's speed when used in combination with components like "shooter", "throwable", or "food".

## 架构

```mcschema
minecraft:use_modifiers:
{
  number "movement_modifier" : opt
  number "use_duration" : opt
}

```

/// html | div.result
//// define
`movement_modifier`：<samp>number</samp>

- Modifier value to scale the players movement speed when item is in use.


////


//// define
`use_duration`：<samp>number</samp>

- How long the item takes to use in seconds.


////


///

