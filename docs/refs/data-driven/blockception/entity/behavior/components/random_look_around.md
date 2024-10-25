# Random Look Around

> 文档版本：1.21.50.25

Allows the mob to randomly look around.

## 架构

```mcschema
random_look_around:
{
  priority "priority"
  integer "angle_of_view_horizontal" : opt
  integer "angle_of_view_vertical" : opt
  number "look_distance" : opt
  vector_of_2_items "look_time"
  number "probability" : opt
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
`angle_of_view_horizontal`：<samp>integer</samp>

- The angle in degrees that an entity can see in the Y-axis (up-down).


////


//// define
`angle_of_view_vertical`：<samp>integer</samp>

- The angle in degrees that an entity can see in the X-axis (left-right).


////


//// define
`look_distance`：<samp>number</samp>

- The distance in blocks from which the entity will look at.


////


//// define
`look_time`：<samp>vector_of_2_items</samp> {#assets.schemas-blockception.general.vectors.number2.json}

- The range of time in seconds the mob will stay looking in a random direction before looking elsewhere


////

```mcschema
vector_of_2_items:
array
{
  number "0..0" : opt
  number "1..1" : opt
}

```

//// html | div.result
///// define
`0..0`：<samp>number</samp>

- The X component.


/////


///// define
`1..1`：<samp>number</samp>

- The Y component.


/////


////



//// define
`probability`：<samp>number</samp>

- The probability of looking at the target. A value of 1.00 is 100%.


////


///

