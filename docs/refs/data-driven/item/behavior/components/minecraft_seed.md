# 未命名

> 文档版本：1.21.0.24



## 架构

```mcschema
minecraft:seed:
{
  string "crop_result" : opt
  array "plant_at" : opt
  {
    block_descriptor "<any array element>"
  }
  boolean "plant_at_any_solid_surface" : opt
  string "plant_at_face" : opt
}

```

/// html | div.result
//// define
`crop_result`：<samp>string</samp>


////


//// define
`plant_at`：<samp>array</samp>


////

<div class="language-text highlight"><span class="filename"><code>plant_at</code></span><pre id="__code_1"><span></span></pre></div>

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


//// define
`plant_at_any_solid_surface`：<samp>boolean</samp>


////


//// define
`plant_at_face`：<samp>string</samp>


////


///

