# Damage Over Time

> 文档版本：1.21.0.24

Applies defined amount of damage to the entity at specified intervals.

## 架构

```mcschema
damage_over_time:
{
  integer "damage_per_hurt" : opt
  number "time_between_hurt" : opt
}

```

/// html | div.result
//// define
`damage_per_hurt`：<samp>integer</samp>

- Amount of damage caused each hurt.


////


//// define
`time_between_hurt`：<samp>number</samp>

- Time in seconds between damage.


////


///

