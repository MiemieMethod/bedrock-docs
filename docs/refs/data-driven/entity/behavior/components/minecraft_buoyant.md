# minecraft:buoyant

> 文档版本：1.21.0.24

Enables an entity to float on the specified liquid blocks.

## 架构

```mcschema
minecraft:buoyant:
{
  boolean "apply_gravity" : opt
  number "base_buoyancy" : opt
  number "big_wave_probability" : opt
  number "big_wave_speed" : opt
  number "drag_down_on_buoyancy_removed" : opt
  array "liquid_blocks" : opt
  {
    item_descriptor "<any array element>"
  }
  boolean "simulate_waves" : opt
}

```

/// html | div.result
//// define
`apply_gravity`：<samp>boolean</samp>

- Applies gravity each tick. Causes more of a wave simulation, but will cause more gravity to be applied outside liquids.


////


//// define
`base_buoyancy`：<samp>number</samp>

- Base buoyancy used to calculate how much will a mob float.


////


//// define
`big_wave_probability`：<samp>number</samp>

- Probability for a big wave hitting the entity. Only used if `simulate_waves` is true.


////


//// define
`big_wave_speed`：<samp>number</samp>

- Multiplier for the speed to make a big wave. Triggered depending on 'big_wave_probability'.


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
`<any array element>`：<samp>item_descriptor</samp> {#assets.schemas.common.definition.item.item_descriptor.json}


/////

```mcschema
item_descriptor:
string

```

///// html | div.result

/////


```mcschema
item_descriptor:
{
  string "<any object property>" : opt
}

```

///// html | div.result
////// define
`<any object property>`：<samp>string</samp>


//////


/////




////


//// define
`simulate_waves`：<samp>boolean</samp>

- Should the movement simulate waves going through.


////


///

