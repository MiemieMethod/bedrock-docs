# Nap

> 文档版本：1.21.0.24

Allows mobs to occassionally stop and take a nap under certain conditions.

## 架构

```mcschema
nap:
{
  priority "priority"
  speed_multiplier "speed_multiplier"
  number "cooldown_max" : opt
  number "cooldown_min" : opt
  number "mob_detect_dist" : opt
  number "mob_detect_height" : opt
  filters "can_nap_filters"
  filters "wake_mob_exceptions"
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
`cooldown_max`：<samp>number</samp>

- Maximum time in seconds the mob has to wait before using the goal again.


////


//// define
`cooldown_min`：<samp>number</samp>

- Minimum time in seconds the mob has to wait before using the goal again.


////


//// define
`mob_detect_dist`：<samp>number</samp>

- The block distance in x and z that will be checked for mobs that this mob detects.


////


//// define
`mob_detect_height`：<samp>number</samp>

- The block distance in y that will be checked for mobs that this mob detects.


////


//// define
`can_nap_filters`：<samp>filters</samp>

- 一个[过滤器组](../filter.md)。The filters that need to be met for the nap to take place.


////


//// define
`wake_mob_exceptions`：<samp>filters</samp>

- 一个[过滤器组](../filter.md)。Filters that can trigger the entity to wake up from it nap.


////


///

