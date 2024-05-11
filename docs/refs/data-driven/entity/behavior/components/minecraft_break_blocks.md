# minecraft:break_blocks

> 文档版本：1.21.0.24

Specifies the blocks that this entity can break as it moves around.

## 架构

```mcschema
minecraft:break_blocks:
{
  array "breakable_blocks" : opt
  {
    block_descriptor "<any array element>"
  }
}

```

/// html | div.result
//// define
`breakable_blocks`：<samp>array</samp>

- A list of the blocks that can be broken as this entity moves around.


////

<div class="language-text highlight"><span class="filename"><code>breakable_blocks</code></span><pre id="__code_1"><span></span></pre></div>

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

