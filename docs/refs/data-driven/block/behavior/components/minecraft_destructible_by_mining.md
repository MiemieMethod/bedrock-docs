# 未命名

> 文档版本：1.21.0.24

Describes the destructible by mining properties for this block. If set to true, the block will take the default number of seconds to destroy. If set to false, this block is indestructible by mining. If the component is omitted, the block will take the default number of seconds to destroy.

## 架构

```mcschema
minecraft:destructible_by_mining:
boolean

```

/// html | div.result

///


```mcschema
minecraft:destructible_by_mining:
{
  array "item_specific_speeds" : opt
  {
    object "<any array element>" : opt
    {
      item_descriptor "item"
      number "destroy_speed" : opt
    }
  }
  number "seconds_to_destroy" : opt
}

```

/// html | div.result
//// define
`item_specific_speeds`：<samp>array</samp>


////

<div class="language-text highlight"><span class="filename"><code>item_specific_speeds</code></span><pre id="__code_1"><span></span></pre></div>

//// html | div.result
///// define
`<any array element>`：<samp>object</samp>


/////

<div class="language-text highlight"><span class="filename"><code>&lt;any array element&gt;</code></span><pre id="__code_1"><span></span></pre></div>

///// html | div.result
////// define
`item`：<samp>item_descriptor</samp> {#assets.schemas.common.definition.item.item_descriptor.json}

- item is required and it is an ItemDescriptor filtering for the item used while mining.


//////

```mcschema
item_descriptor:
string

```

////// html | div.result

//////


```mcschema
item_descriptor:
{
  string "<any object property>" : opt
}

```

////// html | div.result
/////// define
`<any object property>`：<samp>string</samp>


///////


//////




////// define
`destroy_speed`：<samp>number</samp>

- destroy_speed is required and it is the speed applied while using the defined item.


//////


/////


////


//// define
`seconds_to_destroy`：<samp>number</samp>

- Sets the number of seconds it takes to destroy the block with base equipment. Greater numbers result in greater mining times.


////


///


