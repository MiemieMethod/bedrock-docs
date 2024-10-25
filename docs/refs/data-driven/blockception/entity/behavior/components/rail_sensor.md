# Rail Sensor

> 文档版本：1.21.50.25

Defines the behavior of the entity when the rail gets activated or deactivated.

## 架构

```mcschema
rail_sensor:
{
  boolean "check_block_types" : opt
  boolean "eject_on_activate" : opt
  boolean "eject_on_deactivate" : opt
  event_object "on_activate"
  event_object "on_deactivate"
  boolean "tick_command_block_on_activate" : opt
  boolean "tick_command_block_on_deactivate" : opt
}

```

/// html | div.result
//// define
`check_block_types`：<samp>boolean</samp>

- If true, on tick this entity will trigger its on_deactivate behavior.


////


//// define
`eject_on_activate`：<samp>boolean</samp>

- If true, this entity will eject all of its riders when it passes over an activated rail.


////


//// define
`eject_on_deactivate`：<samp>boolean</samp>

- If true, this entity will eject all of its riders when it passes over a deactivated rail.


////


//// define
`on_activate`：<samp>event_object</samp> {#assets.schemas-blockception.behavior.entities.format.types.event_object.json}

- Event to call when the rail is activated.


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
`on_deactivate`：<samp>[event_object](#assets.schemas-blockception.behavior.entities.format.types.event_object.json)</samp>

- Event to call when the rail is deactivated.


////


//// define
`tick_command_block_on_activate`：<samp>boolean</samp>

- If true, command blocks will start ticking when passing over an activated rail.


////


//// define
`tick_command_block_on_deactivate`：<samp>boolean</samp>

- If false, command blocks will stop ticking when passing over a deactivated rail.


////


///

