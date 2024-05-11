# minecraft:projectile

> 文档版本：1.21.0.24

Projectile items shoot out, like an arrow.

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

- Specifies how long a player must charge a projectile for it to critically hit.


////


//// define
`projectile_entity`：<samp>string</samp>

- Which entity is to be fired as a projectile.


////


///

