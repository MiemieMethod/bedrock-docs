# Balloonable

> 文档版本：1.21.0.24

allows the entity to have a balloon attached and defines the conditions and events for the entity when is ballooned.

## 架构

```mcschema
balloonable:
{
  number "soft_distance" : opt
  number "max_distance" : opt
  string "on_balloon" : opt
  string "on_unballoon" : opt
  number "mass" : opt
}

```

/// html | div.result
//// define
`soft_distance`：<samp>number</samp>

- Distance in blocks where the 'spring' effect lifts the entity.


////


//// define
`max_distance`：<samp>number</samp>

- Distance in blocks where the balloon breaks.


////


//// define
`on_balloon`：<samp>string</samp>

- Event to call when the entity is ballooned.


////


//// define
`on_unballoon`：<samp>string</samp>

- Event to call when the entity is unballooned.


////


//// define
`mass`：<samp>number</samp>

- Mass that the entity has when computing balloon pull forces.


////


///

