# Instant Despawn

> 文档版本：1.21.50.25

Despawns the Actor immediately.

## 架构

```mcschema
instant_despawn:
{
  boolean "remove_child_entities" : opt
}

```

/// html | div.result
//// define
`remove_child_entities`：<samp>boolean</samp>

- If true, all entities linked to this entity in a child relationship (eg. leashed) will also be despawned.


////


///

