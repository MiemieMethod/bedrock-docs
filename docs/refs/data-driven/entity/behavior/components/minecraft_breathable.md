# minecraft:breathable

> 文档版本：1.21.0.24

Defines what blocks this entity can breathe in and gives them the ability to suffocate.

## 架构

```mcschema
minecraft:breathable:
{
  array "breathe_blocks" : opt
  {
    block_descriptor "<any array element>"
  }
  boolean "breathes_air" : opt
  boolean "breathes_lava" : opt
  boolean "breathes_solids" : opt
  boolean "breathes_water" : opt
  boolean "generates_bubbles" : opt
  number "inhale_time" : opt
  array "non_breathe_blocks" : opt
  {
    block_descriptor "<any array element>"
  }
  integer "suffocate_time" : opt
  integer "total_supply" : opt
}

```

/// html | div.result
//// define
`breathe_blocks`：<samp>array</samp>


////

<div class="language-text highlight"><span class="filename"><code>breathe_blocks</code></span><pre id="__code_1"><span></span></pre></div>

//// html | div.result
///// define
`<any array element>`：<samp>block_descriptor</samp> {#assets.schemas.common.definition.block.block_descriptor.json}

- List of blocks this entity can breathe in, in addition to the other "breathes" parameters.


/////

```mcschema
block_descriptor:
{
  string "name" : opt
  object "states" : opt
  {
    string "<any object property>" : opt
    integer "<any object property>" : opt
  }
  expression_node_string "tags"
}

```

///// html | div.result
////// define
`name`：<samp>string</samp>


//////


////// define
`states`：<samp>object</samp>


//////

<div class="language-text highlight"><span class="filename"><code>states</code></span><pre id="__code_1"><span></span></pre></div>

////// html | div.result
/////// define
`<any object property>`：<samp>string</samp>


///////


/////// define
`<any object property>`：<samp>integer</samp>


///////



//////


////// define
`tags`：<samp>expression_node_string</samp> {#assets.schemas.common.molang.expression_node_string.json}


//////

```mcschema
expression_node_string:
string

```

////// html | div.result

//////



/////


```mcschema
block_descriptor:
string

```

///// html | div.result

/////




////


//// define
`breathes_air`：<samp>boolean</samp>

- If true, this entity can breathe in air.


////


//// define
`breathes_lava`：<samp>boolean</samp>

- If true, this entity can breathe in lava.


////


//// define
`breathes_solids`：<samp>boolean</samp>

- If true, this entity can breathe in solid blocks.


////


//// define
`breathes_water`：<samp>boolean</samp>

- If true, this entity can breathe in water.


////


//// define
`generates_bubbles`：<samp>boolean</samp>

- If true, this entity will have visible bubbles while in water.


////


//// define
`inhale_time`：<samp>number</samp>

- Time in seconds to recover breath to maximum.


////


//// define
`non_breathe_blocks`：<samp>array</samp>


////

<div class="language-text highlight"><span class="filename"><code>non_breathe_blocks</code></span><pre id="__code_1"><span></span></pre></div>

//// html | div.result
///// define
`<any array element>`：<samp>[block_descriptor](#assets.schemas.common.definition.block.block_descriptor.json)</samp>

- List of blocks this entity can't breathe in, in addition to the other "breathes" parameters.


/////


////


//// define
`suffocate_time`：<samp>integer</samp>

- Time in seconds between suffocation damage.


////


//// define
`total_supply`：<samp>integer</samp>

- Time in seconds the entity can hold its breath.


////


///

