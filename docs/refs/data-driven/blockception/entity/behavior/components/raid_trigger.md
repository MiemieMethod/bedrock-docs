# Raid Trigger

> 文档版本：1.21.0.24

Attempts to trigger a raid at the entity's location.

## 架构

```mcschema
raid_trigger:
{
  event "triggered_event"
}

```

/// html | div.result
//// define
`triggered_event`：<samp>event</samp> {#assets.schemas-blockception.behavior.entities.format.types.event.json}

- Event to run we attempt to trigger a raid on the village.


////

```mcschema
event:
string

```

//// html | div.result

////


```mcschema
event:
{
  string "event" : opt
  string "target" : opt
}

```

//// html | div.result
///// define
`event`：<samp>string</samp>

- The event to fire.


/////


///// define
`target`：<samp>string</samp>

- The target of the event.


/////


////




///

