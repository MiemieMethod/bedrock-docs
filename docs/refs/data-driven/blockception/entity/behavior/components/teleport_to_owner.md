# Teleport To Owner

> 文档版本：1.21.50.25

Allows an entity to teleport to its owner.

## 架构

```mcschema
teleport_to_owner:
{
  priority "priority"
  number "cooldown" : opt
  filters "filters"
}

```

/// html | div.result
//// define
`priority`：<samp>priority</samp> {#assets.schemas-blockception.behavior.entities.format.behaviors.types.priority.json}


////

```mcschema
priority:
integer

```

//// html | div.result

////



//// define
`cooldown`：<samp>number</samp>

- The time in seconds that must pass for the entity to be able to try to teleport again.


////


//// define
`filters`：<samp>filters</samp>

- 一个[过滤器组](../filter.md)。Conditions to be satisfied for the entity to teleport to its owner.


////


///

