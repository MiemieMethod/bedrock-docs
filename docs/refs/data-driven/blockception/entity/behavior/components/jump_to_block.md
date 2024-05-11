# Jump To Block

> 文档版本：1.21.0.24

Allows an entity to jump to another random block.

## 架构

```mcschema
jump_to_block:
{
  priority "priority"
  vector_of_2_items "cooldown_range"
  array "forbidden_blocks" : opt
  {
    descriptor "<any array element>"
  }
  number "max_velocity" : opt
  integer "minimum_distance" : opt
  integer "minimum_path_length" : opt
  array "preferred_blocks" : opt
  {
    descriptor "<any array element>"
  }
  number "preferred_blocks_chance" : opt
  number "scale_factor" : opt
  integer "search_height" : opt
  integer "search_width" : opt
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
`cooldown_range`：<samp>vector_of_2_items</samp> {#assets.schemas-blockception.general.vectors.number2.json}

- Minimum and maximum cooldown time-range (positive, in seconds) between each attempted jump.


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
`forbidden_blocks`：<samp>array</samp>

- Blocks that the mob can't jump to.


////

<div class="language-text highlight"><span class="filename"><code>forbidden_blocks</code></span><pre id="__code_1"><span></span></pre></div>

//// html | div.result
///// define
`<any array element>`：<samp>descriptor</samp> {#assets.schemas-blockception.general.item.descriptor.json}


/////

```mcschema
identifier:
string

```

///// html | div.result

/////



```mcschema
descriptor:
{
  identifier "item"
  object "item" : opt
  {
  }
  0 "tags"
  string "item_tag" : opt
}

```

///// html | div.result
////// define
`item`：<samp>[identifier](#assets.schemas-blockception.general.item.identifier.json)</samp>


//////


////// define
`item`：<samp>object</samp>

- An object that describes an item.


//////

<div class="language-text highlight"><span class="filename"><code>item</code></span><pre id="__code_1"><span></span></pre></div>

////// html | div.result

//////



////// define
`tags`：<samp>0</samp> {#assets.schemas-blockception.molang.string.json}

- [UNDOCUMENTED] A Molang expression ran against item or block to match.


//////

```mcschema
0:
string

```

////// html | div.result

//////



////// define
`item_tag`：<samp>string</samp>

- [UNDOCUMENTED] A tag to lookup item or block by.


//////


/////


```mcschema
descriptor:
{
  identifier "item"
  object "item" : opt
  {
    identifier "item"
    object "item" : opt
    {
    }
    0 "tags"
    string "item_tag" : opt
  }
}

```

///// html | div.result
////// define
`item`：<samp>[identifier](#assets.schemas-blockception.general.item.identifier.json)</samp>


//////


////// define
`item`：<samp>object</samp>

- An object that describes an item.


//////

<div class="language-text highlight"><span class="filename"><code>item</code></span><pre id="__code_1"><span></span></pre></div>

////// html | div.result

//////



/////




////


//// define
`max_velocity`：<samp>number</samp>

- The maximum velocity with which the mob can jump.


////


//// define
`minimum_distance`：<samp>integer</samp>

- The minimum distance (in blocks) from the mob to a block, in order to consider jumping to it.


////


//// define
`minimum_path_length`：<samp>integer</samp>

- The minimum length (in blocks) of the mobs path to a block, in order to consider jumping to it.


////


//// define
`preferred_blocks`：<samp>array</samp>

- Blocks that the mob prefers jumping to.


////

<div class="language-text highlight"><span class="filename"><code>preferred_blocks</code></span><pre id="__code_1"><span></span></pre></div>

//// html | div.result
///// define
`<any array element>`：<samp>[descriptor](#assets.schemas-blockception.general.item.descriptor.json)</samp>


/////


////


//// define
`preferred_blocks_chance`：<samp>number</samp>

- Chance (between 0.0 and 1.0) that the mob will jump to a preferred block, if in range. Only matters if preferred blocks are defined.


////


//// define
`scale_factor`：<samp>number</samp>

- The scalefactor of the bounding box of the mob while it is jumping.


////


//// define
`search_height`：<samp>integer</samp>

- The height (in blocks, in range [2, 15]) of the search box, centered around the mob.


////


//// define
`search_width`：<samp>integer</samp>

- The width (in blocks, in range [2, 15]) of the search box, centered around the mob.


////


///

