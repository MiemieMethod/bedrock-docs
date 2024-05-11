# Raid Garden

> 文档版本：1.21.0.24

Allows the mob to eat/raid crops out of farms until they are full.

## 架构

```mcschema
raid_garden:
{
  priority "priority"
  speed_multiplier "speed_multiplier"
  array "blocks" : opt
  {
    reference "<any array element>"
  }
  integer "eat_delay" : opt
  integer "full_delay" : opt
  integer "initial_eat_delay" : opt
  number "goal_radius" : opt
  integer "max_to_eat" : opt
  integer "search_range" : opt
  integer "search_height" : opt
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
`blocks`：<samp>array</samp>

- Blocks that the mob is looking for to eat.


////

<div class="language-text highlight"><span class="filename"><code>blocks</code></span><pre id="__code_1"><span></span></pre></div>

//// html | div.result
///// define
`<any array element>`：<samp>reference</samp> {#assets.schemas-blockception.general.block.reference.json}

- A block identifier.


/////

```mcschema
identifier:
string

```

///// html | div.result

/////



```mcschema
reference:
{
  identifier "name"
  object "states" : opt
  {
    ['boolean', 'integer', 'string'] "\w*:?\w+" : opt
  }
  0 "tags"
}

```

///// html | div.result
////// define
`name`：<samp>[identifier](#assets.schemas-blockception.general.block.identifier.json)</samp>


//////


////// define
`states`：<samp>object</samp>


//////

<div class="language-text highlight"><span class="filename"><code>states</code></span><pre id="__code_1"><span></span></pre></div>

////// html | div.result
/////// define
`\w*:?\w+`：<samp>['boolean', 'integer', 'string']</samp>

- The key of property is the name of the block state/property, the value must be the same as the block properties accepted values.


///////


//////


////// define
`tags`：<samp>0</samp> {#assets.schemas-blockception.molang.string.json}

- A condition using Molang queries that results to true/false that can be used to query for blocks with certain tags.


//////

```mcschema
0:
string

```

////// html | div.result

//////



/////




////


//// define
`eat_delay`：<samp>integer</samp>

- Time in seconds between each time it eats.


////


//// define
`full_delay`：<samp>integer</samp>

- Amount of time in seconds before this mob wants to eat again.


////


//// define
`initial_eat_delay`：<samp>integer</samp>

- Time in seconds before starting to eat/raid once it arrives at it.


////


//// define
`goal_radius`：<samp>number</samp>

- Distance in blocks within the mob considers it has reached the goal. This is the `wiggle room` to stop the AI from bouncing back and forth trying to reach a specific spot


////


//// define
`max_to_eat`：<samp>integer</samp>

- Maximum number of things this entity wants to eat.


////


//// define
`search_range`：<samp>integer</samp>

- Distance in blocks the mob will look for crops to eat.


////


//// define
`search_height`：<samp>integer</samp>

- Height in blocks the mob will look for crops to eat.


////


///

