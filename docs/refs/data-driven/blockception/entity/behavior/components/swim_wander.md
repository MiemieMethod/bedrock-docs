# Swim Wander

> 文档版本：1.21.0.24

Has the fish swim around when they can't pathfind.

## 架构

```mcschema
swim_wander:
{
  priority "priority"
  speed_multiplier "speed_multiplier"
  number "interval" : opt
  number "look_ahead" : opt
  number "wander_time" : opt
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
`interval`：<samp>number</samp>

- Percent chance to start wandering, when not path-finding. 1 = 100%


////


//// define
`look_ahead`：<samp>number</samp>

- Distance to look ahead for obstacle avoidance, while wandering.


////


//// define
`wander_time`：<samp>number</samp>

- Amount of time (in seconds) to wander after wandering behavior was successfully started.


////


///

