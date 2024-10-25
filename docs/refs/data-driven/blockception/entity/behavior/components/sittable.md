# Sittable

> 文档版本：1.21.50.25

Defines the entity's `sit` state.

## 架构

```mcschema
sittable:
{
  event_object "sit_event"
  event_object "stand_event"
}

```

/// html | div.result
//// define
`sit_event`：<samp>event_object</samp> {#assets.schemas-blockception.behavior.entities.format.types.event_object.json}

- Event to run when the entity enters the `sit` state.


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
`stand_event`：<samp>[event_object](#assets.schemas-blockception.behavior.entities.format.types.event_object.json)</samp>

- Event to run when the entity exits the `sit` state.


////


///

