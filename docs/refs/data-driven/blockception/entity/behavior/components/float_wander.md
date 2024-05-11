# Float Wander

> 文档版本：1.21.0.24

Allows the mob to float around like the Ghast.

## 架构

```mcschema
float_wander:
{
  priority "priority"
  integer "xz_dist" : opt
  integer "y_dist" : opt
  number "y_offset" : opt
  boolean "must_reach" : opt
  boolean "random_reselect" : opt
  range_number_type "float_duration"
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
`xz_dist`：<samp>integer</samp>

- Distance in blocks on ground that the mob will look for a new spot to move to. Must be at least 1


////


//// define
`y_dist`：<samp>integer</samp>

- Distance in blocks that the mob will look up or down for a new spot to move to. Must be at least 1


////


//// define
`y_offset`：<samp>number</samp>

- Height in blocks to add to the selected target position.


////


//// define
`must_reach`：<samp>boolean</samp>

- If true, the point has to be reachable to be a valid target.


////


//// define
`random_reselect`：<samp>boolean</samp>

- If true, the mob will randomly pick a new point while moving to the previously selected one.


////


//// define
`float_duration`：<samp>range_number_type</samp> {#assets.schemas-blockception.behavior.entities.format.types.range_number_type.json}

- Range of time in seconds the mob will float around before landing and choosing to do something else.


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




///

