# minecraft:block_sensor

> 文档版本：1.21.0.24

Fires off a specified event when a block in the block list is broken within the sensor range.

## 架构

```mcschema
minecraft:block_sensor:
{
  array "on_break" : opt
  {
    object "<any array element>" : opt
    {
      array "block_list" : opt
      {
        block_descriptor "<any array element>"
      }
      string "on_block_broken" : opt
    }
  }
  number "sensor_radius" : opt
  array "sources" : opt
  {
    entity_filters "<any array element>"
  }
}

```

/// html | div.result
//// define
`on_break`：<samp>array</samp>


////

<div class="language-text highlight"><span class="filename"><code>on_break</code></span><pre id="__code_1"><span></span></pre></div>

//// html | div.result
///// define
`<any array element>`：<samp>object</samp>


/////

<div class="language-text highlight"><span class="filename"><code>&lt;any array element&gt;</code></span><pre id="__code_1"><span></span></pre></div>

///// html | div.result
////// define
`block_list`：<samp>array</samp>


//////

<div class="language-text highlight"><span class="filename"><code>block_list</code></span><pre id="__code_1"><span></span></pre></div>

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


////// define
`on_block_broken`：<samp>string</samp>


//////


/////


////


//// define
`sensor_radius`：<samp>number</samp>

- The maximum radial distance in which a specified block can be detected. The biggest radius is 32.0.


////


//// define
`sources`：<samp>array</samp>

- List of sources that break the block to listen for. If none are specified, all block breaks will be detected.


////

<div class="language-text highlight"><span class="filename"><code>sources</code></span><pre id="__code_1"><span></span></pre></div>

//// html | div.result
///// define
`<any array element>`：<samp>entity_filters</samp> {#assets.schemas.common.definition.entity.entity_filters.json}


/////

```mcschema
entity_filters:
{
  sub_filter "any_of"
  sub_filter "all_of"
  sub_filter "none_of"
}

```

///// html | div.result
////// define
`any_of`：<samp>sub_filter</samp> {#assets.schemas.common.definition.entity.sub_filter.json}


//////

```mcschema
sub_filter:
{
  string "test" : opt
  string "subject" : opt
  string "operator" : opt
  string "value" : opt
}

```

////// html | div.result
/////// define
`test`：<samp>string</samp>


///////


/////// define
`subject`：<samp>string</samp>


///////


/////// define
`operator`：<samp>string</samp>


///////


/////// define
`value`：<samp>string</samp>


///////


//////


```mcschema
sub_filter:
array
{
  object "<any array element>" : opt
  {
    string "test" : opt
    string "subject" : opt
    string "operator" : opt
    string "value" : opt
  }
}

```

////// html | div.result
/////// define
`<any array element>`：<samp>object</samp>


///////

<div class="language-text highlight"><span class="filename"><code>&lt;any array element&gt;</code></span><pre id="__code_1"><span></span></pre></div>

/////// html | div.result
//////// define
`test`：<samp>string</samp>


////////


//////// define
`subject`：<samp>string</samp>


////////


//////// define
`operator`：<samp>string</samp>


////////


//////// define
`value`：<samp>string</samp>


////////


///////


//////




////// define
`all_of`：<samp>[sub_filter](#assets.schemas.common.definition.entity.sub_filter.json)</samp>


//////


////// define
`none_of`：<samp>[sub_filter](#assets.schemas.common.definition.entity.sub_filter.json)</samp>


//////


/////



////


///

