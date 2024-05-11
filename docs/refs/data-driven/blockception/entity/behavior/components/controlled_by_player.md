# Controlled By Player

> 文档版本：1.21.0.24

Allows the entity to be controlled by the player using an item in the item_controllable property (required). Also requires the minecraft:movement property, and the minecraft:rideable property. On every tick, the entity will attempt to rotate towards where the player is facing with the control item whilst simultaneously moving forward.

## 架构

```mcschema
controlled_by_player:
{
  priority "priority"
  number "fractional_rotation" : opt
  number "fractional_rotation_limit" : opt
  number "mount_speed_multiplier" : opt
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
`fractional_rotation`：<samp>number</samp>

- The entity will attempt to rotate to face where the player is facing each tick. The entity will target this percentage of their difference in their current facing angles each tick (from 0.0 to 1.0 where 1.0 = 100%). This is limited by FractionalRotationLimit. A value of 0.0 will result in the entity no longer turning to where the player is facing.


////


//// define
`fractional_rotation_limit`：<samp>number</samp>

- Limits the total degrees the entity can rotate to face where the player is facing on each tick.


////


//// define
`mount_speed_multiplier`：<samp>number</samp>

- Speed multiplier of mount when controlled by player.


////


///

