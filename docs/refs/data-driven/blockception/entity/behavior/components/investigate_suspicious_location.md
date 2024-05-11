# Inspect Bookshelf

> 文档版本：1.21.0.24

Allows the mob to inspect bookshelves.

## 架构

```mcschema
investigate_suspicious_location:
{
  number "goal_radius" : opt
  integer "priority" : opt
  number "speed_multiplier" : opt
}

```

/// html | div.result
//// define
`goal_radius`：<samp>number</samp>

- Distance in blocks within the entity considers it has reached its target position.


////


//// define
`priority`：<samp>integer</samp>

- The higher the priority, the sooner this behavior will be executed as a goal.


////


//// define
`speed_multiplier`：<samp>number</samp>

- Movement speed multiplier.


////


///

