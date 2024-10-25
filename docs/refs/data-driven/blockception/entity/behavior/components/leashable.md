# Leashable

> 文档版本：1.21.50.25

Allows this entity to be leashed and defines the conditions and events for this entity when is leashed.

## 架构

```mcschema
leashable:
{
  boolean "can_be_stolen" : opt
  number "hard_distance" : opt
  number "max_distance" : opt
  event_object "on_leash"
  event_object "on_unleash"
  number "soft_distance" : opt
}

```

/// html | div.result
//// define
`can_be_stolen`：<samp>boolean</samp>

- If true, players can leash this entity even if it is already leashed to another mob.


////


//// define
`hard_distance`：<samp>number</samp>

- Distance in blocks at which the leash stiffens, restricting movement.


////


//// define
`max_distance`：<samp>number</samp>

- Distance in blocks at which the leash breaks.


////


//// define
`on_leash`：<samp>event_object</samp> {#assets.schemas-blockception.behavior.entities.format.types.event_object.json}

- Event to call when this entity is leashed.


////

```mcschema
event_object:
{
  filters "filters"
  string "event" : opt
  string "target" : opt
}

```

//// html | div.result
///// define
`filters`：<samp>filters</samp>

- 一个[过滤器组](../filter.md)。


/////


///// define
`event`：<samp>string</samp>

- The event to fire.


/////


///// define
`target`：<samp>string</samp>

- The target of the event.


/////


////



//// define
`on_unleash`：<samp>[event_object](#assets.schemas-blockception.behavior.entities.format.types.event_object.json)</samp>

- Event to call when this entity is unleashed.


////


//// define
`soft_distance`：<samp>number</samp>

- Distance in blocks at which the `spring` effect starts acting to keep this entity close to the entity that leashed it.


////


///

