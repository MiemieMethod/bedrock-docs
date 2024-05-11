# minecraft:block_placer

> 文档版本：1.21.0.24

Items with the block_placer component will place a block when used.

## 架构

```mcschema
minecraft:block_placer:
{
  string "block" : opt
  array "use_on" : opt
  {
    block_descriptor "<any array element>"
  }
}

```

/// html | div.result
//// define
`block`：<samp>string</samp>

- Defines the block that will be placed.


////


//// define
`use_on`：<samp>array</samp>

- List of block descriptors of the blocks that this item can be used on. If left empty, all blocks will be allowed.


////

<div class="language-text highlight"><span class="filename"><code>use_on</code></span><pre id="__code_1"><span></span></pre></div>

//// html | div.result
///// define
`<any array element>`：<samp>block_descriptor</samp> {#assets.schemas.common.definition.block.block_descriptor.json}


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


///

