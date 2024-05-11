# Play

> 文档版本：1.21.0.24

Allows the mob to play with other baby villagers. This can only be used by Villagers.

## 架构

```mcschema
play:
{
  priority "priority"
  speed_multiplier "speed_multiplier"
  number "chance_to_start" : opt
  integer "follow_distance" : opt
  vector_of_3_items "friend_search_area"
  array "friend_types" : opt
  {
     "<any array element>" : opt
  }
  number "max_play_duration_seconds" : opt
  integer "random_pos_search_height" : opt
  integer "random_pos_search_range" : opt
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
`chance_to_start`：<samp>number</samp>

- Percent chance that the mob will start this goal, from 0 to 1.


////


//// define
`follow_distance`：<samp>integer</samp>

- The distance (in blocks) that the mob tries to be in range of the friend it's following.


////


//// define
`friend_search_area`：<samp>vector_of_3_items</samp> {#assets.schemas-blockception.general.vectors.number3.json}

- The dimensions of the AABB used to search for a potential friend to play with.


////

```mcschema
vector_of_3_items:
array
{
  number "0..0" : opt
  number "1..1" : opt
  number "2..2" : opt
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


///// define
`2..2`：<samp>number</samp>

- The Z component.


/////


////



//// define
`friend_types`：<samp>array</samp>

- The entity type(s) to consider when searching for a potential friend to play with.


////

<div class="language-text highlight"><span class="filename"><code>friend_types</code></span><pre id="__code_1"><span></span></pre></div>

//// html | div.result
///// define
`<any array element>`


/////


////


//// define
`max_play_duration_seconds`：<samp>number</samp>

- The max amount of seconds that the mob will play for before exiting the Goal.


////


//// define
`random_pos_search_height`：<samp>integer</samp>

- The height (in blocks) that the mob will search within to find a random position position to move to. Must be at least 1.


////


//// define
`random_pos_search_range`：<samp>integer</samp>

- The distance (in blocks) on ground that the mob will search within to find a random position to move to. Must be at least 1.


////


///

