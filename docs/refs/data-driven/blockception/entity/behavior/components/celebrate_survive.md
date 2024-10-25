# Celebrate Survive

> 文档版本：1.21.50.25

Allows this entity to celebrate surviving a raid by shooting fireworks.

## 架构

```mcschema
celebrate_survive:
{
  priority "priority"
  speed_multiplier "speed_multiplier"
  range_number_type "fireworks_interval"
  number "duration" : opt
  event "on_celebration_end_event"
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
`speed_multiplier`：<samp>speed_multiplier</samp> {#assets.schemas-blockception.behavior.entities.format.behaviors.types.speed_multiplier.json}


////

```mcschema
speed_multiplier:
number

```

//// html | div.result

////



//// define
`fireworks_interval`：<samp>range_number_type</samp> {#assets.schemas-blockception.behavior.entities.format.types.range_number_type.json}

- Minimum and maximum time between firework (positive, in seconds).


////

```mcschema
range_number_type:
number

```

//// html | div.result

////


```mcschema
range_number_type:
array
{
  number "0..0" : opt
  number "1..1" : opt
}

```

//// html | div.result
///// define
`0..0`：<samp>number</samp>

- The first value of the range.


/////


///// define
`1..1`：<samp>number</samp>

- The second value of the range.


/////


////


```mcschema
range_number_type:
{
  number "range_min" : opt
  number "range_max" : opt
}

```

//// html | div.result
///// define
`range_min`：<samp>number</samp>

- The minimum value of the range.


/////


///// define
`range_max`：<samp>number</samp>

- The maximum value of the range.


/////


////




//// define
`duration`：<samp>number</samp>

- The duration in seconds that the celebration lasts for.


////


//// define
`on_celebration_end_event`：<samp>event</samp> {#assets.schemas-blockception.behavior.entities.format.types.event.json}

- The event to trigger when the goal's duration expires.


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

