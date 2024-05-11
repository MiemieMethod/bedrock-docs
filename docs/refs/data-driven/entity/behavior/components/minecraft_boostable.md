# minecraft:boostable

> 文档版本：1.21.0.24

Defines the conditions and behavior of a rideable entity's boost.

## 架构

```mcschema
minecraft:boostable:
{
  array "boost_items" : opt
  {
    object "<any array element>" : opt
    {
      integer "damage" : opt
      string "item" : opt
      string "replace_item" : opt
    }
  }
  number "duration" : opt
  number "speed_multiplier" : opt
}

```

/// html | div.result
//// define
`boost_items`：<samp>array</samp>


////

<div class="language-text highlight"><span class="filename"><code>boost_items</code></span><pre id="__code_1"><span></span></pre></div>

//// html | div.result
///// define
`<any array element>`：<samp>object</samp>


/////

<div class="language-text highlight"><span class="filename"><code>&lt;any array element&gt;</code></span><pre id="__code_1"><span></span></pre></div>

///// html | div.result
////// define
`damage`：<samp>integer</samp>

- This is the damage that the item will take each time it is used.


//////


////// define
`item`：<samp>string</samp>

- Name of the item that can be used to boost.


//////


////// define
`replace_item`：<samp>string</samp>

- The item used to boost will become this item once it is used up.


//////


/////


////


//// define
`duration`：<samp>number</samp>

- Time in seconds for the boost.


////


//// define
`speed_multiplier`：<samp>number</samp>

- Factor by which the entity's normal speed increases. E.g. 2.0 means go twice as fast. Requires "format_version" of 1.20 or more, otherwise the value 1.35 will be used.


////


///

