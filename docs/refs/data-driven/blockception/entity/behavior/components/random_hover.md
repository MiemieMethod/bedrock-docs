# Random Hover

> 文档版本：1.21.0.24

Allows the mob to hover around randomly, close to the surface.

## 架构

```mcschema
random_hover:
{
  priority "priority"
  speed_multiplier "speed_multiplier"
  array "hover_height" : opt
  {
    number "0..0" : opt
    number "1..1" : opt
  }
  integer "interval" : opt
  integer "xz_dist" : opt
  integer "y_dist" : opt
  number "y_offset" : opt
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
`hover_height`：<samp>array</samp>

- The height above the surface which the mob will try to maintain.


////

<div class="language-text highlight"><span class="filename"><code>hover_height</code></span><pre id="__code_1"><span></span></pre></div>

//// html | div.result
///// define
`0..0`：<samp>number</samp>


/////


///// define
`1..1`：<samp>number</samp>


/////


////


//// define
`interval`：<samp>integer</samp>

- A random value to determine when to randomly move somewhere. This has a 1/interval chance to choose this goal


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


///

