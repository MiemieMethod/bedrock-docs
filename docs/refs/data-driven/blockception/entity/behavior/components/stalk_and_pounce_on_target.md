# Stalk And Pounce On Target

> 文档版本：1.21.50.25

Allows an entity to stalk a specific target. Once within range of the target, the entity will then leap at the target and deal damage based upon its attack attribute.

## 架构

```mcschema
stalk_and_pounce_on_target:
{
  priority "priority"
  number "interest_time" : opt
  number "leap_distance" : opt
  number "leap_height" : opt
  number "max_stalk_dist" : opt
  number "pounce_max_dist" : opt
  boolean "set_persistent" : opt
  number "stalk_speed" : opt
  number "strike_dist" : opt
  number "stuck_time" : opt
  number "leap_dist" : opt
  filters "stuck_blocks"
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
`interest_time`：<samp>number</samp>

- The amount of time the mob will be interested before pouncing. This happens when the mob is within range of pouncing


////


//// define
`leap_distance`：<samp>number</samp>

- The distance in blocks the mob jumps in the direction of its target.


////


//// define
`leap_height`：<samp>number</samp>

- The height in blocks the mob jumps when leaping at its target.


////


//// define
`max_stalk_dist`：<samp>number</samp>

- The maximum distance away a target can be before the mob gives up on stalking.


////


//// define
`pounce_max_dist`：<samp>number</samp>

- The maximum distance away from the target in blocks to begin pouncing at the target.


////


//// define
`set_persistent`：<samp>boolean</samp>

- Allows the actor to be set to persist upon targeting a player.


////


//// define
`stalk_speed`：<samp>number</samp>

- The movement speed in which you stalk your target.


////


//// define
`strike_dist`：<samp>number</samp>

- The Maximum distance away from the target when landing from the pounce that will still result in damaging the target.


////


//// define
`stuck_time`：<samp>number</samp>

- The amount of time the mob will be stuck if they fail and land on a block they can be stuck on.


////


//// define
`leap_dist`：<samp>number</samp>

- The distance in blocks the mob jumps in the direction of their target.


////


//// define
`stuck_blocks`：<samp>filters</samp>

- 一个[过滤器组](../filter.md)。Filters to apply on the block the mob lands on to determine if it is valid for getting stuck.


////


///

