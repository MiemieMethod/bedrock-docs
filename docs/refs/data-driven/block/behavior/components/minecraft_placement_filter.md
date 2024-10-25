# 未命名

> 文档版本：1.21.0.24

Sets rules for under what conditions the block can be placed or survive.

## 架构

```mcschema
minecraft:placement_filter:
{
  array "conditions" : opt
  {
    object "<any array element>" : opt
    {
      string "allowed_faces" : opt
      array "block_filter" : opt
      {
        block_descriptor "<any array element>"
      }
    }
    object "<any array element>" : opt
    {
      string "allowed_faces" : opt
      array "block_filter" : opt
      {
        string "<any array element>" : opt
      }
    }
  }
}

```

/// html | div.result
//// define
`conditions`：<samp>array</samp>


////

<div class="language-text highlight"><span class="filename"><code>conditions</code></span><pre id="__code_1"><span></span></pre></div>

//// html | div.result
///// define
`<any array element>`：<samp>object</samp>


/////

<div class="language-text highlight"><span class="filename"><code>&lt;any array element&gt;</code></span><pre id="__code_1"><span></span></pre></div>

///// html | div.result
////// define
`allowed_faces`：<samp>string</samp>

- List of any of the following strings describing which face(s) this block can be placed on: "up", "down", "north", "south", "east", "west", "side", "all". Limited to 6 faces.


//////


////// define
`block_filter`：<samp>array</samp>


//////

<div class="language-text highlight"><span class="filename"><code>block_filter</code></span><pre id="__code_1"><span></span></pre></div>

////// html | div.result
/////// define
`<any array element>`：<samp>block_descriptor</samp> {#assets.schemas.common.definition.block.block_descriptor.json}


///////

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

/////// html | div.result
//////// define
`name`：<samp>string</samp>


////////


//////// define
`states`：<samp>object</samp>


////////

<div class="language-text highlight"><span class="filename"><code>states</code></span><pre id="__code_1"><span></span></pre></div>

//////// html | div.result
///////// define
`<any object property>`：<samp>string</samp>


/////////


///////// define
`<any object property>`：<samp>integer</samp>


/////////



////////


//////// define
`tags`：<samp>expression_node_string</samp> {#assets.schemas.common.molang.expression_node_string.json}


////////

```mcschema
expression_node_string:
string

```

//////// html | div.result

////////



///////


```mcschema
block_descriptor:
string

```

/////// html | div.result

///////




//////


/////


///// define
`<any array element>`：<samp>object</samp>


/////

<div class="language-text highlight"><span class="filename"><code>&lt;any array element&gt;</code></span><pre id="__code_1"><span></span></pre></div>

///// html | div.result
////// define
`allowed_faces`：<samp>string</samp>

- List of any of the following strings describing which face(s) this block can be placed on: "up", "down", "north", "south", "east", "west", "side", "all". Limited to 6 faces.


//////


////// define
`block_filter`：<samp>array</samp>


//////

<div class="language-text highlight"><span class="filename"><code>block_filter</code></span><pre id="__code_1"><span></span></pre></div>

////// html | div.result
/////// define
`<any array element>`：<samp>string</samp>


///////


//////


/////



////


///

