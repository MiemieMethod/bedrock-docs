# Peek

> 文档版本：1.21.50.25

Defines the entity's `peek` behavior, defining the events that should be called during it.

## 架构

```mcschema
peek:
{
  event_object "on_close"
  event_object "on_open"
  event_object "on_target_open"
}

```

/// html | div.result
//// define
`on_close`：<samp>event_object</samp> {#assets.schemas-blockception.behavior.entities.format.types.event_object.json}

- Event to call when the entity is done peeking.


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
`on_open`：<samp>[event_object](#assets.schemas-blockception.behavior.entities.format.types.event_object.json)</samp>

- Event to call when the entity starts peeking.


////


//// define
`on_target_open`：<samp>[event_object](#assets.schemas-blockception.behavior.entities.format.types.event_object.json)</samp>

- Event to call when the entity's target entity starts peeking.


////


///

