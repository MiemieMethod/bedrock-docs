# minecraft:digger

> 文档版本：1.21.0.24

Digger item component specifies how quickly this item can dig specific blocks.

## 架构

```mcschema
minecraft:digger:
{
  array "destroy_speeds" : opt
  {
    object "<any array element>" : opt
    {
      block_descriptor "block"
      integer "speed" : opt
    }
  }
  boolean "use_efficiency" : opt
  definition_trigger "on_consume"
}

```

/// html | div.result
//// define
`destroy_speeds`：<samp>array</samp>

- A list of blocks to dig with correlating speeds of digging.


////

<div class="language-text highlight"><span class="filename"><code>destroy_speeds</code></span><pre id="__code_1"><span></span></pre></div>

//// html | div.result
///// define
`<any array element>`：<samp>object</samp>


/////

<div class="language-text highlight"><span class="filename"><code>&lt;any array element&gt;</code></span><pre id="__code_1"><span></span></pre></div>

///// html | div.result
////// define
`block`：<samp>block_descriptor</samp> {#assets.schemas.common.definition.block.block_descriptor.json}

- Block to be dug.


//////

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

////// html | div.result
/////// define
`name`：<samp>string</samp>


///////


/////// define
`states`：<samp>object</samp>


///////

<div class="language-text highlight"><span class="filename"><code>states</code></span><pre id="__code_1"><span></span></pre></div>

/////// html | div.result
//////// define
`<any object property>`：<samp>string</samp>


////////


//////// define
`<any object property>`：<samp>integer</samp>


////////



///////


/////// define
`tags`：<samp>expression_node_string</samp> {#assets.schemas.common.molang.expression_node_string.json}


///////

```mcschema
expression_node_string:
string

```

/////// html | div.result

///////



//////


```mcschema
block_descriptor:
string

```

////// html | div.result

//////




////// define
`speed`：<samp>integer</samp>

- Digging speed for the correlating block(s).


//////


/////


////


//// define
`use_efficiency`：<samp>boolean</samp>

- Determines whether this item should be impacted if the efficiency enchantment is applied to it.


////


//// define
`on_consume`：<samp>definition_trigger</samp> {#assets.schemas.common.definition.definition_trigger.json}

- Event trigger for when the item is consumed.


////

```mcschema
definition_trigger:
string

```

//// html | div.result

////


```mcschema
definition_trigger:
{
  string "event" : opt
  string "target" : opt
  expression_node "condition"
}

```

//// html | div.result
///// define
`event`：<samp>string</samp>


/////


///// define
`target`：<samp>string</samp>


/////


///// define
`condition`：<samp>expression_node</samp> {#assets.schemas.common.molang.expression_node.json}


/////

```mcschema
expression_node:
string

```

///// html | div.result

/////


```mcschema
expression_node:
number

```

///// html | div.result

/////


```mcschema
expression_node:
{
  string "expression" : opt
  integer "version" : opt
}

```

///// html | div.result
////// define
`expression`：<samp>string</samp>


//////


////// define
`version`：<samp>integer</samp>


//////


/////




////




///

