# Snacking

> 文档版本：1.21.0.24

Allows the mob to take a load off and snack on food that it found nearby.

## 架构

```mcschema
snacking:
{
  priority "priority"
  array "items" : opt
  {
    descriptor "<any array element>"
  }
  descriptor "items"
  number "snacking_cooldown" : opt
  number "snacking_cooldown_min" : opt
  number "snacking_stop_chance" : opt
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

- Items that we are interested in snacking on.


////

<div class="language-text highlight"><span class="filename"><code>items</code></span><pre id="__code_1"><span></span></pre></div>

//// html | div.result
///// define
`<any array element>`：<samp>descriptor</samp> {#assets.schemas-blockception.general.item.descriptor.json}


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


//// define
`items`：<samp>[descriptor](#assets.schemas-blockception.general.item.descriptor.json)</samp>

- Items that we are interested in snacking on.


////



//// define
`snacking_cooldown`：<samp>number</samp>

- The cooldown time in seconds before the mob is able to snack again.


////


//// define
`snacking_cooldown_min`：<samp>number</samp>

- The minimum time in seconds before the mob is able to snack again.


////


//// define
`snacking_stop_chance`：<samp>number</samp>

- This is the chance that the mob will stop snacking, from 0 to 1.


////


///

