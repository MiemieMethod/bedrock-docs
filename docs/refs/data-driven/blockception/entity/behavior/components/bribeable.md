# Bribeable

> 文档版本：1.21.0.24

Defines the way an entity can get into the 'bribed' state.

## 架构

```mcschema
bribeable:
{
  number "bribe_cooldown" : opt
  array "bribe_items" : opt
  {
    descriptor "<any array element>"
  }
}

```

/// html | div.result
//// define
`bribe_cooldown`：<samp>number</samp>

- Time in seconds before the Entity can be bribed again.


////


//// define
`bribe_items`：<samp>array</samp>

- The list of items that can be used to bribe the entity.


////

<div class="language-text highlight"><span class="filename"><code>bribe_items</code></span><pre id="__code_1"><span></span></pre></div>

//// html | div.result
///// define
`<any array element>`：<samp>descriptor</samp> {#assets.schemas-blockception.general.item.descriptor.json}

- An item that can be used to bribe the entity.


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

