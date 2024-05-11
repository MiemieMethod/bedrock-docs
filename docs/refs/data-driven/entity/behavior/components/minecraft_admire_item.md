# minecraft:admire_item

> 文档版本：1.21.0.24

Causes the mob to ignore attackable targets for a given duration.

## 架构

```mcschema
minecraft:admire_item:
{
  integer "cooldown_after_being_attacked" : opt
  integer "duration" : opt
}

```

/// html | div.result
//// define
`cooldown_after_being_attacked`：<samp>integer</samp>

- Duration, in seconds, for which mob won't admire items if it was hurt.


////


//// define
`duration`：<samp>integer</samp>

- Duration, in seconds, that the mob is pacified.


////


///

