# Projectile

> 文档版本：1.21.50.25

Compels the item shoot, like an arrow.  Pair with minecraft:shooter for dispensers or as ammunition.  Pair with minecraft:throwable to set the entity spawned.

## 架构

```mcschema
minecraft:projectile:
{
  number "minimum_critical_power" : opt
  string "projectile_entity" : opt
}

```

/// html | div.result
//// define
`minimum_critical_power`：<samp>number</samp>

- How long you must charge a projectile for it to critically hit.


////


//// define
`projectile_entity`：<samp>string</samp>

- The entity to be fired as a projectile.


////


///

