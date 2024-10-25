# Tamemount

> 文档版本：1.21.50.25

Allows the Entity to be tamed by mounting it.

## 架构

```mcschema
tamemount:
{
  integer "attempt_temper_mod" : opt
  object "auto_reject_items" : opt
  {
    descriptor "item"
  }
  array "auto_reject_items" : opt
  {
    object "<any array element>" : opt
    {
    }
  }
  string "feed_text" : opt
  object "feed_items" : opt
  {
    descriptor "item"
    number "temper_mod" : opt
  }
  array "feed_items" : opt
  {
    object "<any array element>" : opt
    {
    }
  }
  integer "max_temper" : opt
  integer "min_temper" : opt
  string "ride_text" : opt
  event_object "tame_event"
}

```

/// html | div.result
//// define
`attempt_temper_mod`：<samp>integer</samp>

- The amount the entity's temper will increase when mounted.


////


//// define
`auto_reject_items`：<samp>object</samp>

- The list of items that this entity dislikes and will cause it to get angry if used while untamed.


////

<div class="language-text highlight"><span class="filename"><code>auto_reject_items</code></span><pre id="__code_1"><span></span></pre></div>

//// html | div.result
///// define
`item`：<samp>descriptor</samp> {#assets.schemas-blockception.general.item.descriptor.json}

- Name of the item this entity dislikes and will cause it to get angry if used while untamed.


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
`auto_reject_items`：<samp>array</samp>

- The list of items that, if carried while interacting with the entity, will anger it.


////

<div class="language-text highlight"><span class="filename"><code>auto_reject_items</code></span><pre id="__code_1"><span></span></pre></div>

//// html | div.result
///// define
`<any array element>`：<samp>object</samp>

- The list of items that this entity dislikes and will cause it to get angry if used while untamed.


/////

<div class="language-text highlight"><span class="filename"><code>&lt;any array element&gt;</code></span><pre id="__code_1"><span></span></pre></div>

///// html | div.result

/////


////



//// define
`feed_text`：<samp>string</samp>

- The text that shows in the feeding interact button.


////


//// define
`feed_items`：<samp>object</samp>

- The list of items that can be used to increase the entity's temper and speed up the taming process.


////

<div class="language-text highlight"><span class="filename"><code>feed_items</code></span><pre id="__code_1"><span></span></pre></div>

//// html | div.result
///// define
`item`：<samp>[descriptor](#assets.schemas-blockception.general.item.descriptor.json)</samp>

- Name of the item this entity likes and can be used to increase this entity's temper.


/////


///// define
`temper_mod`：<samp>number</samp>

- The amount of temper this entity gains when fed this item.


/////


////


//// define
`feed_items`：<samp>array</samp>

- The list of items that can be used to increase the entity's temper and speed up the taming process.


////

<div class="language-text highlight"><span class="filename"><code>feed_items</code></span><pre id="__code_1"><span></span></pre></div>

//// html | div.result
///// define
`<any array element>`：<samp>object</samp>

- The list of items that can be used to increase the entity's temper and speed up the taming process.


/////

<div class="language-text highlight"><span class="filename"><code>&lt;any array element&gt;</code></span><pre id="__code_1"><span></span></pre></div>

///// html | div.result

/////


////



//// define
`max_temper`：<samp>integer</samp>

- The maximum value for the entity's random starting temper.


////


//// define
`min_temper`：<samp>integer</samp>

- The minimum value for the entity's random starting temper.


////


//// define
`ride_text`：<samp>string</samp>

- The text that shows in the riding interact button.


////


//// define
`tame_event`：<samp>event_object</samp> {#assets.schemas-blockception.behavior.entities.format.types.event_object.json}

- Event that triggers when the entity becomes tamed.


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



///

