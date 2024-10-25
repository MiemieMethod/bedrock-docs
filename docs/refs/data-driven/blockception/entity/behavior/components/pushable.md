# Pushable

> 文档版本：1.21.50.25

Defines what can push an entity between other entities and pistons.

## 架构

```mcschema
pushable:
{
  boolean "is_pushable" : opt
  boolean "is_pushable_by_piston" : opt
}

```

/// html | div.result
//// define
`is_pushable`：<samp>boolean</samp>

- Whether the entity can be pushed by other entities.


////


//// define
`is_pushable_by_piston`：<samp>boolean</samp>

- Whether the entity can be pushed by pistons safely.


////


///

