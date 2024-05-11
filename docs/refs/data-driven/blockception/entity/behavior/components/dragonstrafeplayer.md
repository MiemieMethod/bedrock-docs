# Dragonstrafeplayer

> 文档版本：1.21.0.24

Allows this entity to fly around looking for a player to shoot fireballs at. Note: This behavior can only be used by the ender_dragon entity type.

## 架构

```mcschema
dragonstrafeplayer:
{
  priority "priority"
  number "active_speed" : opt
  number "fireball_range" : opt
  number "flight_speed" : opt
  number "switch_direction_probability" : opt
  number "target_in_range_and_in_view_time" : opt
  range_number_type "target_zone"
  number "turn_speed" : opt
  number "view_angle" : opt
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
`active_speed`：<samp>number</samp>

- The speed this entity moves when this behavior has started or while it's active.


////


//// define
`fireball_range`：<samp>number</samp>

- Maximum distance of this entity's fireball attack while strafing.


////


//// define
`flight_speed`：<samp>number</samp>

- The speed this entity moves while this behavior is not active.


////


//// define
`switch_direction_probability`：<samp>number</samp>

- Percent chance to to switch this entity's strafe direction between clockwise and counterclockwise. Switch direction chance occurs each time a new target is chosen (1.0 = 100%).


////


//// define
`target_in_range_and_in_view_time`：<samp>number</samp>

- Time (in seconds) the target must be in fireball range, and in view [ie, no solid terrain in-between the target and this entity], before a fireball can be shot.


////


//// define
`target_zone`：<samp>range_number_type</samp> {#assets.schemas-blockception.behavior.entities.format.types.range_number_type.json}

- Minimum and maximum distance, from the target, this entity can use this behavior.


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
`turn_speed`：<samp>number</samp>

- The speed at which this entity turns while using this behavior.


////


//// define
`view_angle`：<samp>number</samp>

- The target must be within "view_angle" degrees of the dragon's current rotation before a fireball can be shot.


////


///

