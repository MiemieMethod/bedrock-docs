# Buoyant

> 文档版本：1.21.50.25

Enables an entity to float on the specified liquid blocks.

## 架构

```mcschema
buoyant:
{
  number "base_buoyancy" : opt
  boolean "apply_gravity" : opt
  number "buoyancy" : opt
  number "big_wave_probability" : opt
  number "big_wave_speed" : opt
  number "drag_down_on_buoyancy_removed" : opt
  array "liquid_blocks" : opt
  {
    reference "<any array element>"
  }
  boolean "simulate_waves" : opt
}

```

/// html | div.result
//// define
`base_buoyancy`：<samp>number</samp>

- Base buoyancy used to calculate how much will a mob float.


////


//// define
`apply_gravity`：<samp>boolean</samp>

- Applies gravity each tick. Causes more of a wave simulation, but will cause more gravity to be applied outside liquids.


////


//// define
`buoyancy`：<samp>number</samp>

- Base buoyancy used to calculate how much will a mob float.


////


//// define
`big_wave_probability`：<samp>number</samp>

- Probability for a big wave hitting the entity. Only used if `simulate_waves` is true.


////


//// define
`big_wave_speed`：<samp>number</samp>

- Multiplier for the speed to make a big wave. Triggered depending on `big_wave_probability`.


////


//// define
`drag_down_on_buoyancy_removed`：<samp>number</samp>

- How much an actor will be dragged down when the Buoyancy Component is removed.


////


//// define
`liquid_blocks`：<samp>array</samp>

- List of blocks this entity can float on. Must be a liquid block.


////

<div class="language-text highlight"><span class="filename"><code>liquid_blocks</code></span><pre id="__code_1"><span></span></pre></div>

//// html | div.result
///// define
`<any array element>`：<samp>reference</samp> {#assets.schemas-blockception.general.block.reference.json}


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
`simulate_waves`：<samp>boolean</samp>

- Should the movement simulate waves going through.


////


///

