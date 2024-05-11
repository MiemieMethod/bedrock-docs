# Navigation Walk

> 文档版本：1.21.0.24

Allows this entity to generate paths by walking around and jumping up and down a block like regular mobs.

## 架构

```mcschema
walk:
{
  boolean "avoid_damage_blocks" : opt
  boolean "avoid_portals" : opt
  boolean "avoid_sun" : opt
  boolean "avoid_water" : opt
  array "blocks_to_avoid" : opt
  {
    reference "<any array element>"
  }
  boolean "can_breach" : opt
  boolean "can_break_doors" : opt
  boolean "can_jump" : opt
  boolean "can_float" : opt
  boolean "can_open_doors" : opt
  boolean "can_open_iron_doors" : opt
  boolean "can_pass_doors" : opt
  boolean "can_path_from_air" : opt
  boolean "can_path_over_lava" : opt
  boolean "can_path_over_water" : opt
  boolean "can_sink" : opt
  boolean "can_swim" : opt
  boolean "can_walk" : opt
  boolean "can_walk_in_lava" : opt
  boolean "is_amphibious" : opt
}

```

/// html | div.result
//// define
`avoid_damage_blocks`：<samp>boolean</samp>

- Tells the pathfinder to avoid blocks that cause damage when finding a path.


////


//// define
`avoid_portals`：<samp>boolean</samp>

- Tells the pathfinder to avoid portals (like nether portals) when finding a path.


////


//// define
`avoid_sun`：<samp>boolean</samp>

- Whether or not the pathfinder should avoid tiles that are exposed to the sun when creating paths.


////


//// define
`avoid_water`：<samp>boolean</samp>

- Tells the pathfinder to avoid water when creating a path.


////


//// define
`blocks_to_avoid`：<samp>array</samp>

- Tells the pathfinder which blocks to avoid when creating a path.


////

<div class="language-text highlight"><span class="filename"><code>blocks_to_avoid</code></span><pre id="__code_1"><span></span></pre></div>

//// html | div.result
///// define
`<any array element>`：<samp>reference</samp> {#assets.schemas-blockception.general.block.reference.json}

- Tells the pathfinder which blocks to avoid when creating a path.


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
`can_breach`：<samp>boolean</samp>

- Tells the pathfinder whether or not it can jump out of water (like a dolphin).


////


//// define
`can_break_doors`：<samp>boolean</samp>

- Tells the pathfinder that it can path through a closed door and break it.


////


//// define
`can_jump`：<samp>boolean</samp>

- Tells the pathfinder whether or not it can jump up blocks.


////


//// define
`can_float`：<samp>boolean</samp>

- Tells the pathfinder whether or not it float.


////


//// define
`can_open_doors`：<samp>boolean</samp>

- Tells the pathfinder that it can path through a closed door assuming the AI will open the door.


////


//// define
`can_open_iron_doors`：<samp>boolean</samp>

- Tells the pathfinder that it can path through a closed iron door assuming the AI will open the door.


////


//// define
`can_pass_doors`：<samp>boolean</samp>

- Whether a path can be created through a door.


////


//// define
`can_path_from_air`：<samp>boolean</samp>

- Tells the pathfinder that it can start pathing when in the air.


////


//// define
`can_path_over_lava`：<samp>boolean</samp>

- Tells the pathfinder whether or not it can travel on the surface of the lava.


////


//// define
`can_path_over_water`：<samp>boolean</samp>

- Tells the pathfinder whether or not it can travel on the surface of the water.


////


//// define
`can_sink`：<samp>boolean</samp>

- Tells the pathfinder whether or not it will be pulled down by gravity while in water.


////


//// define
`can_swim`：<samp>boolean</samp>

- Tells the pathfinder whether or not it can path anywhere through water and plays swimming animation along that path.


////


//// define
`can_walk`：<samp>boolean</samp>

- Tells the pathfinder whether or not it can walk on the ground outside water.


////


//// define
`can_walk_in_lava`：<samp>boolean</samp>

- Tells the pathfinder whether or not it can travel in lava like walking on ground.


////


//// define
`is_amphibious`：<samp>boolean</samp>

- Tells the pathfinder whether or not it can walk on the ground underwater.


////


///

