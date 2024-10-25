# Random Sitting

> 文档版本：1.21.50.25

Allows the mob to randomly sit for a duration.

## 架构

```mcschema
random_sitting:
{
  priority "priority"
  speed_multiplier "speed_multiplier"
  number "cooldown" : opt
  number "cooldown_time" : opt
  number "min_sit_time" : opt
  number "start_chance" : opt
  number "stop_chance" : opt
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
`cooldown`：<samp>number</samp>

- Time in seconds the mob has to wait before using the goal again.


////


//// define
`cooldown_time`：<samp>number</samp>

- Time in seconds the mob has to wait before using the goal again.


////


//// define
`min_sit_time`：<samp>number</samp>

- The minimum amount of time in seconds before the mob can stand back up.


////


//// define
`start_chance`：<samp>number</samp>

- This is the chance that the mob will start this goal, from 0 to 1.


////


//// define
`stop_chance`：<samp>number</samp>

- This is the chance that the mob will stop this goal, from 0 to 1.


////


///

