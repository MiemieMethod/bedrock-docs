# Drying Out Timer

> 文档版本：1.21.0.24

Adds a timer for drying out that will count down and fire `dried_out_event` or will stop as soon as the entity will get under rain or water and fire `stopped_drying_out_event`.

## 架构

```mcschema
drying_out_timer:
{
  event_object "dried_out_event"
  event_object "recover_after_dried_out_event"
  event_object "stopped_drying_out_event"
  number "total_time" : opt
  number "water_bottle_refill_time" : opt
}

```

/// html | div.result
//// define
`dried_out_event`：<samp>event_object</samp> {#assets.schemas-blockception.behavior.entities.format.types.event_object.json}

- Event to fire when the drying out time runs out.


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
`recover_after_dried_out_event`：<samp>[event_object](#assets.schemas-blockception.behavior.entities.format.types.event_object.json)</samp>

- Event to fire when entity was already dried out but received increase in water supply.


////


//// define
`stopped_drying_out_event`：<samp>[event_object](#assets.schemas-blockception.behavior.entities.format.types.event_object.json)</samp>

- Event to fire when entity stopped drying out, for example got into water or under rain.


////


//// define
`total_time`：<samp>number</samp>

- Amount of time in seconds to dry out fully.


////


//// define
`water_bottle_refill_time`：<samp>number</samp>

- Optional amount of additional time in seconds given by using splash water bottle on entity.


////


///

