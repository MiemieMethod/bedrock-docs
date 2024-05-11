# Mob Effect

> 文档版本：1.21.0.24

A component that applies a mob effect to entities that get within range.

## 架构

```mcschema
mob_effect:
{
  integer "cooldown_time" : opt
  number "effect_range" : opt
  integer "effect_time" : opt
  filters "entity_filter"
  string "mob_effect" : opt
}

```

/// html | div.result
//// define
`cooldown_time`：<samp>integer</samp>

- Time in seconds to wait between each application of the effect.


////


//// define
`effect_range`：<samp>number</samp>

- How close a hostile entity must be to have the mob effect applied.


////


//// define
`effect_time`：<samp>integer</samp>

- How long the applied mob effect lasts in seconds.


////


//// define
`entity_filter`：<samp>filters</samp>

- 一个[过滤器组](../filter.md)。Filter to use for conditions.


////


//// define
`mob_effect`：<samp>string</samp>

- The mob effect that is applied to entities that enter this entities effect range.


////


///

