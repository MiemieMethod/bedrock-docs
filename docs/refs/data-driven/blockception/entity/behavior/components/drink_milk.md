# Drink Milk

> 文档版本：1.21.0.24

Allows the mob to drink milk based on specified environment conditions.

## 架构

```mcschema
drink_milk:
{
  priority "priority"
  number "cooldown_seconds" : opt
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
`cooldown_seconds`：<samp>number</samp>

- Time (in seconds) that the goal is on cooldown before it can be used again.


////


//// define
`filters`：<samp>filters</samp>

- 一个[过滤器组](../filter.md)。Conditions that need to be met for the behavior to start.


////


///

