# Dragonchargeplayer

> 文档版本：1.21.0.24

Allows this entity to attack a player by charging at them. The player is chosen by the "minecraft:behavior.dragonscanning". Note: This behavior can only be used by the ender_dragon entity type.

## 架构

```mcschema
dragonchargeplayer:
{
  priority "priority"
  number "active_speed" : opt
  number "continue_charge_threshold_time" : opt
  number "flight_speed" : opt
  range_number_type "target_zone"
  number "turn_speed" : opt
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
`continue_charge_threshold_time`：<samp>number</samp>

- If the dragon is outside the "target_zone" for longer than "continue_charge_threshold_time" seconds, the charge is canceled.


////


//// define
`flight_speed`：<samp>number</samp>

- The speed this entity moves while this behavior is not active.


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


///

