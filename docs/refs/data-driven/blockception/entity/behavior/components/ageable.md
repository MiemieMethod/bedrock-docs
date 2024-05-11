# Ageable

> 文档版本：1.21.0.24

Adds a timer for the entity to grow up. It can be accelerated by giving the entity the items it likes as defined by feedItems.

## 架构

```mcschema
ageable:
{
  array "drop_items" : opt
  {
    descriptor "<any array element>"
  }
  descriptor "drop_items"
  number "duration" : opt
  array "feed_items" : opt
  {
    identifier "<any array element>"
    object "<any array element>" : opt
    {
      number "growth" : opt
      descriptor "item"
    }
  }
  identifier "feed_items"
  event_object "grow_up"
  descriptor "transform_to_item"
  filters "interact_filters"
}

```

/// html | div.result
//// define
`drop_items`：<samp>array</samp>

- List of items that the entity drops when it grows up.


////

<div class="language-text highlight"><span class="filename"><code>drop_items</code></span><pre id="__code_1"><span></span></pre></div>

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
`drop_items`：<samp>[descriptor](#assets.schemas-blockception.general.item.descriptor.json)</samp>

- List of items that the entity drops when it grows up.


////



//// define
`duration`：<samp>number</samp>

- Amount of time before the entity grows up, -1 for always a baby.


////


//// define
`feed_items`：<samp>array</samp>

- List of items that can be fed to the entity. Includes `item` for the item name and `growth` to define how much time it grows up by


////

<div class="language-text highlight"><span class="filename"><code>feed_items</code></span><pre id="__code_1"><span></span></pre></div>

//// html | div.result
///// define
`<any array element>`：<samp>[identifier](#assets.schemas-blockception.general.item.identifier.json)</samp>


/////


///// define
`<any array element>`：<samp>object</samp>


/////

<div class="language-text highlight"><span class="filename"><code>&lt;any array element&gt;</code></span><pre id="__code_1"><span></span></pre></div>

///// html | div.result
////// define
`growth`：<samp>number</samp>


//////


////// define
`item`：<samp>[descriptor](#assets.schemas-blockception.general.item.descriptor.json)</samp>


//////


/////



////


//// define
`feed_items`：<samp>[identifier](#assets.schemas-blockception.general.item.identifier.json)</samp>

- List of items that can be fed to the entity. Includes `item` for the item name and `growth` to define how much time it grows up by


////



//// define
`grow_up`：<samp>event_object</samp> {#assets.schemas-blockception.behavior.entities.format.types.event_object.json}

- Event to run when this entity grows up.


////

```mcschema
event_object:
{
  filters "filters"
  string "event" : opt
  string "target" : opt
}

```

//// html | div.result
///// define
`filters`：<samp>filters</samp>

- 一个[过滤器组](../filter.md)。


/////


///// define
`event`：<samp>string</samp>

- The event to fire.


/////


///// define
`target`：<samp>string</samp>

- The target of the event.


/////


////



//// define
`transform_to_item`：<samp>[descriptor](#assets.schemas-blockception.general.item.descriptor.json)</samp>

- The feed item used will transform to this item upon successful interaction. Format: itemName:auxValue


////


//// define
`interact_filters`：<samp>filters</samp>

- 一个[过滤器组](../filter.md)。List of conditions to meet so that the entity can be fed.


////


///

