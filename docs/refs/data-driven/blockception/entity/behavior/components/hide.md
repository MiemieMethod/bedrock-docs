# Hide

> 文档版本：1.21.50.25

Allows a mob with the hide component to attempt to move to - and hide at - an owned or nearby POI.

## 架构

```mcschema
hide:
{
  priority "priority"
  speed_multiplier "speed_multiplier"
  number "duration" : opt
  string "poi_type" : opt
  number "timeout_cooldown" : opt
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
`duration`：<samp>number</samp>

- Amount of time in seconds that the mob reacts.


////


//// define
`poi_type`：<samp>string</samp>

- Defines what POI type to hide at.


////


//// define
`timeout_cooldown`：<samp>number</samp>

- The cooldown time in seconds before the goal can be reused after a internal failure or timeout condition.


////


///

