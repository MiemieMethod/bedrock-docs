# Knockback Roar

> 文档版本：1.21.0.24

Allows the mob to perform a damaging knockback that affects all nearby entities.

## 架构

```mcschema
knockback_roar:
{
  priority "priority"
  number "attack_time" : opt
  number "cooldown_time" : opt
  filters "damage_filters"
  number "duration" : opt
  integer "knockback_damage" : opt
  integer "knockback_strength" : opt
  filters "knockback_filters"
  integer "knockback_horizontal_strength" : opt
  integer "knockback_range" : opt
  integer "knockback_vertical_strength" : opt
  number "knockback_height_cap" : opt
  boolean "track_target" : opt
  event "on_roar_end"
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
`attack_time`：<samp>number</samp>

- The delay after which the knockback occurs (in seconds).


////


//// define
`cooldown_time`：<samp>number</samp>

- Time in seconds the mob has to wait before using the goal again.


////


//// define
`damage_filters`：<samp>filters</samp>

- 一个[过滤器组](../filter.md)。The list of conditions another entity must meet to be a valid target to apply damage to.


////


//// define
`duration`：<samp>number</samp>

- The duration of the roar (in seconds).


////


//// define
`knockback_damage`：<samp>integer</samp>

- The damage dealt by the knockback roar.


////


//// define
`knockback_strength`：<samp>integer</samp>

- The strength of the knockback.


////


//// define
`knockback_filters`：<samp>filters</samp>

- 一个[过滤器组](../filter.md)。The list of conditions another entity must meet to be a valid target to apply knockback to.


////


//// define
`knockback_horizontal_strength`：<samp>integer</samp>

- The strength of the horizontal knockback.


////


//// define
`knockback_range`：<samp>integer</samp>

- The radius (in blocks) of the knockback effect.


////


//// define
`knockback_vertical_strength`：<samp>integer</samp>

- The strength of the vertical knockback.


////


//// define
`knockback_height_cap`：<samp>number</samp>

- The maximum height for vertical knockback.


////


//// define
`track_target`：<samp>boolean</samp>

- If true, this mob will chase after the target as long as it's a valid target.


////


//// define
`on_roar_end`：<samp>event</samp> {#assets.schemas-blockception.behavior.entities.format.types.event.json}

- Event that is triggered when the roar ends.


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

