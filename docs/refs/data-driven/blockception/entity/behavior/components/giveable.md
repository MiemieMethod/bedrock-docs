# Giveable

> 文档版本：1.21.0.24

Defines sets of items that can be used to trigger events when used on this entity. The item will also be taken and placed in the entity's inventory.

## 架构

```mcschema
giveable:
{
  object "triggers" : opt
  {
    number "cooldown" : opt
    array "items" : opt
    {
      descriptor "<any array element>"
    }
    event_object "on_give"
  }
}

```

/// html | div.result
//// define
`triggers`：<samp>object</samp>

- Defines sets of items that can be used to trigger events when used on this entity. The item will also be taken and placed in the entity's inventory.


////

<div class="language-text highlight"><span class="filename"><code>triggers</code></span><pre id="__code_1"><span></span></pre></div>

//// html | div.result
///// define
`cooldown`：<samp>number</samp>

- An optional cool down in seconds to prevent spamming interactions.


/////


///// define
`items`：<samp>array</samp>

- The list of items that can be given to the entity to place in their inventory.


/////

<div class="language-text highlight"><span class="filename"><code>items</code></span><pre id="__code_1"><span></span></pre></div>

///// html | div.result
////// define
`<any array element>`：<samp>descriptor</samp> {#assets.schemas-blockception.general.item.descriptor.json}

- An items that can be given to the entity to place in their inventory.


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




/////


///// define
`on_give`：<samp>event_object</samp> {#assets.schemas-blockception.behavior.entities.format.types.event_object.json}

- Event to fire when the correct item is given.


/////

```mcschema
event_object:
{
  filters "filters"
  string "event" : opt
  string "target" : opt
}

```

///// html | div.result
////// define
`filters`：<samp>filters</samp>

- 一个[过滤器组](../filter.md)。


//////


////// define
`event`：<samp>string</samp>

- The event to fire.


//////


////// define
`target`：<samp>string</samp>

- The target of the event.


//////


/////



////


///

