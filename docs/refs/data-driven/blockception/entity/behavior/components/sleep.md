# Sleep

> 文档版本：1.21.50.25

Allows mobs that own a bed to in a village to move to and sleep in it.

## 架构

```mcschema
sleep:
{
  priority "priority"
  speed_multiplier "speed_multiplier"
  boolean "can_sleep_while_riding" : opt
  number "cooldown_time" : opt
  number "sleep_collider_height" : opt
  number "sleep_collider_width" : opt
  number "sleep_y_offset" : opt
  number "timeout_cooldown" : opt
  number "goal_radius" : opt
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
`can_sleep_while_riding`：<samp>boolean</samp>

- If true, the mob will be able to use the sleep goal if riding something.


////


//// define
`cooldown_time`：<samp>number</samp>

- Time in seconds the mob has to wait before using the goal again.


////


//// define
`sleep_collider_height`：<samp>number</samp>

- The height of the mob's collider while sleeping.


////


//// define
`sleep_collider_width`：<samp>number</samp>

- The width of the mob's collider while sleeping.


////


//// define
`sleep_y_offset`：<samp>number</samp>

- The y offset of the mob's collider while sleeping.


////


//// define
`timeout_cooldown`：<samp>number</samp>

- The cooldown time in seconds before the goal can be reused after a internal failure or timeout condition.


////


//// define
`goal_radius`：<samp>number</samp>

- Distance in blocks within the mob considers it has reached the goal. This is the "wiggle room" to stop the AI from bouncing back and forth trying to reach a specific spot


////


///

