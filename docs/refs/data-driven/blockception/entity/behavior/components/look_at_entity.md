# Look At Entity

> 文档版本：1.21.0.24

Allows the mob to look at nearby entities.

## 架构

```mcschema
look_at_entity:
{
  priority "priority"
  number "look_distance" : opt
  number "probability" : opt
  range_number_type "look_time"
  integer "angle_of_view_vertical" : opt
  integer "angle_of_view_horizontal" : opt
  filters "filters"
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
`look_distance`：<samp>number</samp>

- The distance in blocks from which the entity will look at.


////


//// define
`probability`：<samp>number</samp>

- The probability of looking at the target. A value of 1.00 is 100%


////


//// define
`look_time`：<samp>range_number_type</samp> {#assets.schemas-blockception.behavior.entities.format.types.range_number_type.json}

- Time range to look at the entity.


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
`angle_of_view_vertical`：<samp>integer</samp>

- The angle in degrees that the mob can see in the X-axis (left-right).


////


//// define
`angle_of_view_horizontal`：<samp>integer</samp>

- The angle in degrees that the mob can see in the Y-axis (up-down).


////


//// define
`filters`：<samp>filters</samp>

- 一个[过滤器组](../filter.md)。Filter to determine the conditions for this mob to look at the entity.


////


///

