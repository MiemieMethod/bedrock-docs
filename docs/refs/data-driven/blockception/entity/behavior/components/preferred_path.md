# Preferred Path

> 文档版本：1.21.0.24

Specifies costing information for mobs that prefer to walk on preferred paths.

## 架构

```mcschema
preferred_path:
{
  number "default_block_cost" : opt
  integer "jump_cost" : opt
  integer "max_fall_blocks" : opt
  array "preferred_path_blocks" : opt
  {
    object "<any array element>" : opt
    {
      number "cost" : opt
      array "blocks" : opt
      {
        reference "<any array element>"
      }
    }
  }
}

```

/// html | div.result
//// define
`default_block_cost`：<samp>number</samp>

- Cost for non-preferred blocks.


////


//// define
`jump_cost`：<samp>integer</samp>

- Added cost for jumping up a node.


////


//// define
`max_fall_blocks`：<samp>integer</samp>

- Distance mob can fall without taking damage.


////


//// define
`preferred_path_blocks`：<samp>array</samp>

- A list of blocks with their associated cost.


////

<div class="language-text highlight"><span class="filename"><code>preferred_path_blocks</code></span><pre id="__code_1"><span></span></pre></div>

//// html | div.result
///// define
`<any array element>`：<samp>object</samp>

- Blocks cost.


/////

<div class="language-text highlight"><span class="filename"><code>&lt;any array element&gt;</code></span><pre id="__code_1"><span></span></pre></div>

///// html | div.result
////// define
`cost`：<samp>number</samp>


//////


////// define
`blocks`：<samp>array</samp>


//////

<div class="language-text highlight"><span class="filename"><code>blocks</code></span><pre id="__code_1"><span></span></pre></div>

////// html | div.result
/////// define
`<any array element>`：<samp>reference</samp> {#assets.schemas-blockception.general.block.reference.json}


///////

```mcschema
identifier:
string

```

/////// html | div.result

///////



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

/////// html | div.result
//////// define
`name`：<samp>[identifier](#assets.schemas-blockception.general.block.identifier.json)</samp>


////////


//////// define
`states`：<samp>object</samp>


////////

<div class="language-text highlight"><span class="filename"><code>states</code></span><pre id="__code_1"><span></span></pre></div>

//////// html | div.result
///////// define
`\w*:?\w+`：<samp>['boolean', 'integer', 'string']</samp>

- The key of property is the name of the block state/property, the value must be the same as the block properties accepted values.


/////////


////////


//////// define
`tags`：<samp>0</samp> {#assets.schemas-blockception.molang.string.json}

- A condition using Molang queries that results to true/false that can be used to query for blocks with certain tags.


////////

```mcschema
0:
string

```

//////// html | div.result

////////



///////




//////


/////


////


///

