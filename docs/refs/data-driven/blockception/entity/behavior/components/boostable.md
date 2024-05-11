# Boostable

> 文档版本：1.21.0.24

Defines the conditions and behavior of a rideable entity's boost.

## 架构

```mcschema
boostable:
{
  number "duration" : opt
  number "speed_multiplier" : opt
  array "boost_items" : opt
  {
    object "<any array element>" : opt
    {
      integer "damage" : opt
      descriptor "item"
      descriptor "replace_item"
    }
  }
}

```

/// html | div.result
//// define
`duration`：<samp>number</samp>

- Time in seconds for the boost.


////


//// define
`speed_multiplier`：<samp>number</samp>

- Factor by which the entity's normal speed increases. E.g. 2.0 means go twice as fast.


////


//// define
`boost_items`：<samp>array</samp>

- List of items that can be used to boost while riding this entity.


////

<div class="language-text highlight"><span class="filename"><code>boost_items</code></span><pre id="__code_1"><span></span></pre></div>

//// html | div.result
///// define
`<any array element>`：<samp>object</samp>

- List of items that can be used to boost while riding this entity.


/////

<div class="language-text highlight"><span class="filename"><code>&lt;any array element&gt;</code></span><pre id="__code_1"><span></span></pre></div>

///// html | div.result
////// define
`damage`：<samp>integer</samp>

- This is the damage that the item will take each time it is used.


//////


////// define
`item`：<samp>descriptor</samp> {#assets.schemas-blockception.general.item.descriptor.json}

- Name of the item that can be used to boost.


//////

```mcschema
identifier:
string

```

////// html | div.result

//////



```mcschema
descriptor:
{
  identifier "item"
  object "item" : opt
  {
  }
  0 "tags"
  string "item_tag" : opt
}

```

////// html | div.result
/////// define
`item`：<samp>[identifier](#assets.schemas-blockception.general.item.identifier.json)</samp>


///////


/////// define
`item`：<samp>object</samp>

- An object that describes an item.


///////

<div class="language-text highlight"><span class="filename"><code>item</code></span><pre id="__code_1"><span></span></pre></div>

/////// html | div.result

///////



/////// define
`tags`：<samp>0</samp> {#assets.schemas-blockception.molang.string.json}

- [UNDOCUMENTED] A Molang expression ran against item or block to match.


///////

```mcschema
0:
string

```

/////// html | div.result

///////



/////// define
`item_tag`：<samp>string</samp>

- [UNDOCUMENTED] A tag to lookup item or block by.


///////


//////


```mcschema
descriptor:
{
  identifier "item"
  object "item" : opt
  {
    identifier "item"
    object "item" : opt
    {
    }
    0 "tags"
    string "item_tag" : opt
  }
}

```

////// html | div.result
/////// define
`item`：<samp>[identifier](#assets.schemas-blockception.general.item.identifier.json)</samp>


///////


/////// define
`item`：<samp>object</samp>

- An object that describes an item.


///////

<div class="language-text highlight"><span class="filename"><code>item</code></span><pre id="__code_1"><span></span></pre></div>

/////// html | div.result

///////



//////




////// define
`replace_item`：<samp>[descriptor](#assets.schemas-blockception.general.item.descriptor.json)</samp>

- The item used to boost will become this item once it is used up.


//////


/////


////


///

