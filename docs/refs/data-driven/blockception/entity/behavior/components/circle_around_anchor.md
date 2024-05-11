# Circle Around Anchor

> 文档版本：1.21.0.24

Causes an entity to circle around an anchor point placed near a point or target.

## 架构

```mcschema
circle_around_anchor:
{
  priority "priority"
  speed_multiplier "speed_multiplier"
  range_number_type "radius_range"
  integer "radius_change_chance" : opt
  range_number_type "height_above_target_range"
  range_number_type "height_offset_range"
  integer "height_change_chance" : opt
  number "goal_radius" : opt
  number "radius_change" : opt
  number "radius_adjustment_chance" : opt
  number "height_adjustment_chance" : opt
  number "angle_change" : opt
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
`radius_range`：<samp>range_number_type</samp> {#assets.schemas-blockception.behavior.entities.format.types.range_number_type.json}

- Horizontal distance from the anchor point this entity must stay within upon a successful radius adjustment.


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
`radius_change_chance`：<samp>integer</samp>

- A random value to determine when to increase the size of the radius up to the maximum. This has a 1/value chance every tick to do so.


////


//// define
`height_above_target_range`：<samp>[range_number_type](#assets.schemas-blockception.behavior.entities.format.types.range_number_type.json)</samp>

- The number of blocks above the target that the next anchor point can be set. This value is used only when the entity is tracking a target.


////


//// define
`height_offset_range`：<samp>[range_number_type](#assets.schemas-blockception.behavior.entities.format.types.range_number_type.json)</samp>

- The range of height in blocks offset the mob can have from it's anchor point.


////


//// define
`height_change_chance`：<samp>integer</samp>

- A random value to determine when to change the height of the mob from the anchor point. This has a 1/value chance every tick to do so.


////


//// define
`goal_radius`：<samp>number</samp>

- Maximum distance from the anchor-point in which this entity considers itself to have reached the anchor point. This is to prevent the entity from bouncing back and forth trying to reach a specific spot.


////


//// define
`radius_change`：<samp>number</samp>

- The number of blocks to increase the current movement radius by, upon successful `radius_adjustment_chance`. If the current radius increases over the range maximum, the current radius will be set back to the range minimum and the entity will change between clockwise and counter-clockwise movement.


////


//// define
`radius_adjustment_chance`：<samp>number</samp>

- Percent chance to determine how often to increase the size of the current movement radius around the anchor point. 1 = 100%. `radius_change_chance` is deprecated and has been replaced with `radius_adjustment_chance`.


////


//// define
`height_adjustment_chance`：<samp>number</samp>

- Percent chance to determine how often to increase or decrease the current height around the anchor point. 1 = 100%. `height_change_chance` is deprecated and has been replaced with `height_adjustment_chance`.


////


//// define
`angle_change`：<samp>number</samp>

- Number of degrees to change this entity's facing by, when the entity selects its next anchor point.


////


///

