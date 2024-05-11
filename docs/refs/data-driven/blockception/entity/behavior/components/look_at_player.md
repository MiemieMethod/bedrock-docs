# Look At Player

> 文档版本：1.21.0.24

Allows the mob to look at the player when the player is nearby.

## 架构

```mcschema
look_at_player:
{
  priority "priority"
  integer "angle_of_view_vertical" : opt
  integer "angle_of_view_horizontal" : opt
  number "look_distance" : opt
  number "probability" : opt
  array "look_time" : opt
  {
    number "0..0" : opt
    number "1..1" : opt
  }
  number "target_distance" : opt
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
`angle_of_view_vertical`：<samp>integer</samp>

- The angle in degrees that the mob can see in the X-axis (left-right).


////


//// define
`angle_of_view_horizontal`：<samp>integer</samp>

- The angle in degrees that the mob can see in the Y-axis (up-down).


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
`look_time`：<samp>array</samp>

- Time range to look at the entity.


////

<div class="language-text highlight"><span class="filename"><code>look_time</code></span><pre id="__code_1"><span></span></pre></div>

//// html | div.result
///// define
`0..0`：<samp>number</samp>

- The minimum amount of time to look.


/////


///// define
`1..1`：<samp>number</samp>

- The maximum amount of time to look.


/////


////


//// define
`target_distance`：<samp>number</samp>

- The distance in blocks from which the entity will choose a target.


////


///

