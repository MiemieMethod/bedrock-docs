# Target Nearby Sensor

> 文档版本：1.21.50.25

Defines the entity's range within which it can see or sense other entities to target them.

## 架构

```mcschema
target_nearby_sensor:
{
  boolean "must_see" : opt
  number "inside_range" : opt
  event_object "on_inside_range"
  event_object "on_outside_range"
  event_object "on_vision_lost_inside_range"
  number "outside_range" : opt
}

```

/// html | div.result
//// define
`must_see`：<samp>boolean</samp>

- Whether the other entity needs to be visible to trigger `inside` events.


////


//// define
`inside_range`：<samp>number</samp>

- Maximum distance in blocks that another entity will be considered in the `inside` range.


////


//// define
`on_inside_range`：<samp>event_object</samp> {#assets.schemas-blockception.behavior.entities.format.types.event_object.json}

- Event to call when an entity gets in the inside range. Can specify `event` for the name of the event and `target` for the target of the event


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
`on_outside_range`：<samp>[event_object](#assets.schemas-blockception.behavior.entities.format.types.event_object.json)</samp>

- Event to call when an entity gets in the outside range. Can specify `event` for the name of the event and `target` for the target of the event


////


//// define
`on_vision_lost_inside_range`：<samp>[event_object](#assets.schemas-blockception.behavior.entities.format.types.event_object.json)</samp>

- Event to call when an entity exits visual range. Can specify `event` for the name of the event and `target` for the target of the event


////


//// define
`outside_range`：<samp>number</samp>

- Maximum distance in blocks that another entity will be considered in the `outside` range.


////


///

