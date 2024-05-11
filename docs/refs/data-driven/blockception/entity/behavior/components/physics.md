# Physics

> 文档版本：1.21.0.24

Defines the physical properties of an actor, including whether it is affected by gravity, whether it collides with objects, or whether it is pushed to the closest space.

## 架构

```mcschema
physics:
{
  boolean "has_collision" : opt
  boolean "has_gravity" : opt
  boolean "push_towards_closest_space" : opt
}

```

/// html | div.result
//// define
`has_collision`：<samp>boolean</samp>

- Whether or not the entity collides with things.


////


//// define
`has_gravity`：<samp>boolean</samp>

- Whether or not the entity is affected by gravity.


////


//// define
`push_towards_closest_space`：<samp>boolean</samp>

- Whether or not the entity is pushed to the closest space.


////


///

