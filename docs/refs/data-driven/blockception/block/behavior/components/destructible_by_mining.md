# Destructible By Mining

> 文档版本：1.21.50.25

Describes the destructible by mining properties for this block. If set to true, the block will take the default number of seconds to destroy. If set to false, this block is indestructible by mining. If the component is omitted, the block will take the default number of seconds to destroy.

## 架构

```mcschema
destructible_by_mining:
boolean

```

/// html | div.result

///


```mcschema
destructible_by_mining:
{
  number "seconds_to_destroy" : opt
  array "item_specific_speeds" : opt
  {
    object "<any array element>" : opt
    {
      string "item" : opt
      object "item" : opt
      {
        string "tags" : opt
      }
      number "destroy_speed" : opt
    }
  }
}

```

/// html | div.result
//// define
`seconds_to_destroy`：<samp>number</samp>

- Sets the number of seconds it takes to destroy the block with base equipment. Greater numbers result in greater mining times.


////


//// define
`item_specific_speeds`：<samp>array</samp>

- Optional array of objects to describe item-specific block destroy speeds.


////

<div class="language-text highlight"><span class="filename"><code>item_specific_speeds</code></span><pre id="__code_1"><span></span></pre></div>

//// html | div.result
///// define
`<any array element>`：<samp>object</samp>


/////

<div class="language-text highlight"><span class="filename"><code>&lt;any array element&gt;</code></span><pre id="__code_1"><span></span></pre></div>

///// html | div.result
////// define
`item`：<samp>string</samp>

- ItemDescriptor filtering for the item used while mining.


//////


////// define
`item`：<samp>object</samp>

- ItemDescriptor filtering for the item used while mining.


//////

<div class="language-text highlight"><span class="filename"><code>item</code></span><pre id="__code_1"><span></span></pre></div>

////// html | div.result
/////// define
`tags`：<samp>string</samp>

- Molang or tag


///////


//////



////// define
`destroy_speed`：<samp>number</samp>

- Sets the number of seconds it takes to destroy the block with base equipment. Greater numbers result in greater mining times.


//////


/////


////


///


