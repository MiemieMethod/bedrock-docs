# Tameable

> 文档版本：1.21.50.25

Defines the rules for a mob to be tamed by the player.

## 架构

```mcschema
tameable:
{
  number "probability" : opt
  event_object "tame_event"
  array "tame_items" : opt
  {
    identifier "<any array element>"
  }
  identifier "tame_items"
}

```

/// html | div.result
//// define
`probability`：<samp>number</samp>

- The chance of taming the entity with each item use between 0.0 and 1.0, where 1.0 is 100%


////


//// define
`tame_event`：<samp>event_object</samp> {#assets.schemas-blockception.behavior.entities.format.types.event_object.json}

- Event to run when this entity becomes tamed.


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
`tame_items`：<samp>array</samp>

- The list of items that can be used to tame this entity.


////

<div class="language-text highlight"><span class="filename"><code>tame_items</code></span><pre id="__code_1"><span></span></pre></div>

//// html | div.result
///// define
`<any array element>`：<samp>identifier</samp> {#assets.schemas-blockception.general.item.identifier.json}


/////

```mcschema
identifier:
string

```

///// html | div.result

/////



////


//// define
`tame_items`：<samp>[identifier](#assets.schemas-blockception.general.item.identifier.json)</samp>

- The list of items that can be used to tame this entity.


////



///

