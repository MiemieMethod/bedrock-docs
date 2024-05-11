# Area Attack

> 文档版本：1.21.0.24

A component that does damage to entities that get within range.

## 架构

```mcschema
area_attack:
{
  entity_damage_source "cause"
  number "damage_cooldown" : opt
  integer "damage_per_tick" : opt
  number "damage_range" : opt
  filters "entity_filter"
  boolean "play_attack_sound" : opt
}

```

/// html | div.result
//// define
`cause`：<samp>entity_damage_source</samp> {#assets.schemas-blockception.general.entity.damage_source.json}

- The type of damage that is applied to entities that enter the damage range.


////

```mcschema
entity_damage_source:
string

```

//// html | div.result

////



//// define
`damage_cooldown`：<samp>number</samp>

- Attack cooldown (in seconds) for how often this entity can attack a target.


////


//// define
`damage_per_tick`：<samp>integer</samp>

- How much damage per tick is applied to entities that enter the damage range.


////


//// define
`damage_range`：<samp>number</samp>

- How close a hostile entity must be to have the damage applied.


////


//// define
`entity_filter`：<samp>filters</samp>

- 一个[过滤器组](../filter.md)。The set of entities that are valid to apply the damage to when within range.


////


//// define
`play_attack_sound`：<samp>boolean</samp>

- If the entity should play their attack sound when attacking a target.


////


///

