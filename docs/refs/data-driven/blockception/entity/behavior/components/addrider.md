# Add Rider

> 文档版本：1.21.50.25

Adds a rider to the entity. Requires `minecraft:rideable.`

## 架构

```mcschema
addrider:
{
  string "entity_type" : opt
  string "spawn_event" : opt
}

```

/// html | div.result
//// define
`entity_type`：<samp>string</samp>

- The entity type that will be riding this entity.


////


//// define
`spawn_event`：<samp>string</samp>

- The spawn event that will be used when the riding entity is created.


////


///

