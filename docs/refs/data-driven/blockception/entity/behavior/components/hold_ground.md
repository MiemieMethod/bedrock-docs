# Hold Ground

> 文档版本：1.21.0.24

The mob freezes and looks at the mob they are targeting.

## 架构

```mcschema
hold_ground:
{
  priority "priority"
  boolean "broadcast" : opt
  number "broadcast_range" : opt
  number "min_radius" : opt
  event "within_radius_event"
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
`broadcast`：<samp>boolean</samp>

- Whether to broadcast out the mob's target to other mobs of the same type.


////


//// define
`broadcast_range`：<samp>number</samp>

- Range in blocks for how far to broadcast.


////


//// define
`min_radius`：<samp>number</samp>

- Minimum distance the target must be for the mob to run this goal.


////


//// define
`within_radius_event`：<samp>event</samp> {#assets.schemas-blockception.behavior.entities.format.types.event.json}

- Event to run when target is within the radius. This event is broadcasted if broadcast is true.


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

