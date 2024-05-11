# Trusting

> 文档版本：1.21.0.24

Defines the rules for a mob to trust players.

## 架构

```mcschema
trusting:
{
  number "probability" : opt
  event_object "trust_event"
  array "trust_items" : opt
  {
    identifier "<any array element>"
  }
}

```

/// html | div.result
//// define
`probability`：<samp>number</samp>

- The chance of the entity trusting with each item use between 0.0 and 1.0, where 1.0 is 100%


////


//// define
`trust_event`：<samp>event_object</samp> {#assets.schemas-blockception.behavior.entities.format.types.event_object.json}

- Event to run when this entity becomes trusting.


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
`trust_items`：<samp>array</samp>

- The list of items that can be used to get the entity to trust players.


////

<div class="language-text highlight"><span class="filename"><code>trust_items</code></span><pre id="__code_1"><span></span></pre></div>

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


///

