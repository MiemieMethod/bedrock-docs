# Equippable

> 文档版本：1.21.50.25

Defines an entity's behavior for having items equipped to it.

## 架构

```mcschema
equippable:
{
  array "slots" : opt
  {
    object "<any array element>" : opt
    {
      integer "slot" : opt
      array "accepted_items" : opt
      {
        descriptor "<any array element>"
      }
      descriptor "item"
      string "interact_text" : opt
      event_object "on_equip"
      event_object "on_unequip"
    }
  }
}

```

/// html | div.result
//// define
`slots`：<samp>array</samp>

- List of slots and the item that can be equipped.


////

<div class="language-text highlight"><span class="filename"><code>slots</code></span><pre id="__code_1"><span></span></pre></div>

//// html | div.result
///// define
`<any array element>`：<samp>object</samp>

- A slot and the item that can be equipped.


/////

<div class="language-text highlight"><span class="filename"><code>&lt;any array element&gt;</code></span><pre id="__code_1"><span></span></pre></div>

///// html | div.result
////// define
`slot`：<samp>integer</samp>

- The slot number of this slot.


//////


////// define
`accepted_items`：<samp>array</samp>

- The list of items that can go in this slot.


//////

<div class="language-text highlight"><span class="filename"><code>accepted_items</code></span><pre id="__code_1"><span></span></pre></div>

////// html | div.result
/////// define
`<any array element>`：<samp>descriptor</samp> {#assets.schemas-blockception.general.item.descriptor.json}

- A item name.


///////

```mcschema
identifier:
string

```

/////// html | div.result

///////



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

/////// html | div.result
//////// define
`item`：<samp>[identifier](#assets.schemas-blockception.general.item.identifier.json)</samp>


////////


//////// define
`item`：<samp>object</samp>

- An object that describes an item.


////////

<div class="language-text highlight"><span class="filename"><code>item</code></span><pre id="__code_1"><span></span></pre></div>

//////// html | div.result

////////



//////// define
`tags`：<samp>0</samp> {#assets.schemas-blockception.molang.string.json}

- [UNDOCUMENTED] A Molang expression ran against item or block to match.


////////

```mcschema
0:
string

```

//////// html | div.result

////////



//////// define
`item_tag`：<samp>string</samp>

- [UNDOCUMENTED] A tag to lookup item or block by.


////////


///////


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

/////// html | div.result
//////// define
`item`：<samp>[identifier](#assets.schemas-blockception.general.item.identifier.json)</samp>


////////


//////// define
`item`：<samp>object</samp>

- An object that describes an item.


////////

<div class="language-text highlight"><span class="filename"><code>item</code></span><pre id="__code_1"><span></span></pre></div>

//////// html | div.result

////////



///////




//////


////// define
`item`：<samp>[descriptor](#assets.schemas-blockception.general.item.descriptor.json)</samp>

- Identifier of the item that can be equipped for this slot.


//////


////// define
`interact_text`：<samp>string</samp>

- Text to be displayed when the entity can be equipped with this item when playing with Touch-screen controls.


//////


////// define
`on_equip`：<samp>event_object</samp> {#assets.schemas-blockception.behavior.entities.format.types.event_object.json}

- Event to trigger when this entity is equipped with this item.


//////

```mcschema
event_object:
{
  filters "filters"
  string "event" : opt
  string "target" : opt
}

```

////// html | div.result
/////// define
`filters`：<samp>filters</samp>

- 一个[过滤器组](../filter.md)。


///////


/////// define
`event`：<samp>string</samp>

- The event to fire.


///////


/////// define
`target`：<samp>string</samp>

- The target of the event.


///////


//////



////// define
`on_unequip`：<samp>[event_object](#assets.schemas-blockception.behavior.entities.format.types.event_object.json)</samp>

- Event to trigger when this item is removed from this entity.


//////


/////


////


///

