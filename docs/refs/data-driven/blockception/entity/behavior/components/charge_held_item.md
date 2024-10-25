# Charge Held Item

> 文档版本：1.21.50.25

Allows an entity to charge and use their held item.

## 架构

```mcschema
charge_held_item:
{
  priority "priority"
  array "items" : opt
  {
    descriptor "<any array element>"
  }
}

```

/// html | div.result
//// define
`priority`：<samp>priority</samp> {#assets.schemas-blockception.behavior.entities.format.behaviors.types.priority.json}


////

```mcschema
priority:
integer

```

//// html | div.result

////



//// define
`items`：<samp>array</samp>

- The list of items that can be used to charge the held item. This list is required and must have at least one item in it.


////

<div class="language-text highlight"><span class="filename"><code>items</code></span><pre id="__code_1"><span></span></pre></div>

//// html | div.result
///// define
`<any array element>`：<samp>descriptor</samp> {#assets.schemas-blockception.general.item.descriptor.json}

- Items names to be used.


/////

```mcschema
identifier:
string

```

///// html | div.result

/////



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

///// html | div.result
////// define
`item`：<samp>[identifier](#assets.schemas-blockception.general.item.identifier.json)</samp>


//////


////// define
`item`：<samp>object</samp>

- An object that describes an item.


//////

<div class="language-text highlight"><span class="filename"><code>item</code></span><pre id="__code_1"><span></span></pre></div>

////// html | div.result

//////



////// define
`tags`：<samp>0</samp> {#assets.schemas-blockception.molang.string.json}

- [UNDOCUMENTED] A Molang expression ran against item or block to match.


//////

```mcschema
0:
string

```

////// html | div.result

//////



////// define
`item_tag`：<samp>string</samp>

- [UNDOCUMENTED] A tag to lookup item or block by.


//////


/////


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

///// html | div.result
////// define
`item`：<samp>[identifier](#assets.schemas-blockception.general.item.identifier.json)</samp>


//////


////// define
`item`：<samp>object</samp>

- An object that describes an item.


//////

<div class="language-text highlight"><span class="filename"><code>item</code></span><pre id="__code_1"><span></span></pre></div>

////// html | div.result

//////



/////




////


///

