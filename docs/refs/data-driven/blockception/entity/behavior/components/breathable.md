# Breathable

> 文档版本：1.21.50.25

Defines what blocks this entity can breathe in and gives them the ability to suffocate.

## 架构

```mcschema
breathable:
{
  integer "total_supply" : opt
  integer "suffocate_time" : opt
  number "inhale_time" : opt
  boolean "breathes_air" : opt
  boolean "breathes_water" : opt
  boolean "breathes_lava" : opt
  boolean "breathes_solids" : opt
  boolean "generates_bubbles" : opt
  array "breathe_blocks" : opt
  {
    reference "<any array element>"
  }
  array "non_breathe_blocks" : opt
  {
    reference "<any array element>"
  }
}

```

/// html | div.result
//// define
`total_supply`：<samp>integer</samp>

- Time in seconds the entity can hold its breath.


////


//// define
`suffocate_time`：<samp>integer</samp>

- Time in seconds between suffocation damage.


////


//// define
`inhale_time`：<samp>number</samp>

- Time in seconds to recover breath to maximum.


////


//// define
`breathes_air`：<samp>boolean</samp>

- If true, this entity can breathe in air.


////


//// define
`breathes_water`：<samp>boolean</samp>

- If true, this entity can breathe in water.


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
`generates_bubbles`：<samp>boolean</samp>

- If true, this entity will have visible bubbles while in water.


////


//// define
`breathe_blocks`：<samp>array</samp>

- List of blocks this entity can breathe in, in addition to the above.


////

<div class="language-text highlight"><span class="filename"><code>breathe_blocks</code></span><pre id="__code_1"><span></span></pre></div>

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
`non_breathe_blocks`：<samp>array</samp>

- List of blocks this entity can't breathe in, in addition to the above.


////

<div class="language-text highlight"><span class="filename"><code>non_breathe_blocks</code></span><pre id="__code_1"><span></span></pre></div>

//// html | div.result
///// define
`<any array element>`：<samp>[reference](#assets.schemas-blockception.general.block.reference.json)</samp>


/////


////


///

