# Spawn Entity

> 文档版本：1.21.50.25

Adds a timer after which this entity will spawn another entity or item (similar to vanilla's chicken's egg-laying behavior).

## 架构

```mcschema
spawn_entity:
{
  object "entities" : opt
  {
    filters "filters"
    integer "max_wait_time" : opt
    integer "min_wait_time" : opt
    integer "num_to_spawn" : opt
    boolean "should_leash" : opt
    boolean "single_use" : opt
    string "spawn_entity" : opt
    string "spawn_event" : opt
    descriptor "spawn_item"
    string "spawn_method" : opt
    sound_event "spawn_sound"
    event_object "spawn_item_event"
  }
  array "entities" : opt
  {
    object "<any array element>" : opt
    {
    }
  }
}

```

/// html | div.result
//// define
`entities`：<samp>object</samp>

- The entities to spawn.


////

<div class="language-text highlight"><span class="filename"><code>entities</code></span><pre id="__code_1"><span></span></pre></div>

//// html | div.result
///// define
`filters`：<samp>filters</samp>

- 一个[过滤器组](../filter.md)。If present, the specified entity will only spawn if the filter evaluates to true.


/////


///// define
`max_wait_time`：<samp>integer</samp>

- Maximum amount of time to randomly wait in seconds before another entity is spawned.


/////


///// define
`min_wait_time`：<samp>integer</samp>

- Minimum amount of time to randomly wait in seconds before another entity is spawned.


/////


///// define
`num_to_spawn`：<samp>integer</samp>

- The number of entities of this type to spawn each time that this triggers.


/////


///// define
`should_leash`：<samp>boolean</samp>

- If true, this the spawned entity will be leashed to the parent.


/////


///// define
`single_use`：<samp>boolean</samp>

- If true, this component will only ever spawn the specified entity once.


/////


///// define
`spawn_entity`：<samp>string</samp>

- Identifier of the entity to spawn, leave empty to spawn the item defined above instead.


/////


///// define
`spawn_event`：<samp>string</samp>

- Event to call when the entity is spawned.


/////


///// define
`spawn_item`：<samp>descriptor</samp> {#assets.schemas-blockception.general.item.descriptor.json}

- Item identifier of the item to spawn.


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




///// define
`spawn_method`：<samp>string</samp>

- Method to use to spawn the entity.


/////


///// define
`spawn_sound`：<samp>sound_event</samp> {#assets.schemas-blockception.general.sound_event.json}

- Identifier of the sound effect to play when the entity is spawned.


/////

```mcschema
sound_event:
string

```

///// html | div.result

/////



///// define
`spawn_item_event`：<samp>event_object</samp> {#assets.schemas-blockception.behavior.entities.format.types.event_object.json}

- Event to call on this entity when the item is spawned.


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


//// define
`entities`：<samp>array</samp>

- The entities to spawn.


////

<div class="language-text highlight"><span class="filename"><code>entities</code></span><pre id="__code_1"><span></span></pre></div>

//// html | div.result
///// define
`<any array element>`：<samp>object</samp>


/////

<div class="language-text highlight"><span class="filename"><code>&lt;any array element&gt;</code></span><pre id="__code_1"><span></span></pre></div>

///// html | div.result

/////


////



///

