# Inside Block Notifier

> 文档版本：1.21.50.25

Verifies whether the entity is inside any of the listed blocks.

## 架构

```mcschema
inside_block_notifier:
{
  array "block_list" : opt
  {
    object "<any array element>" : opt
    {
      block "block"
      event_object "entered_block_event"
      event_object "exited_block_event"
    }
  }
}

```

/// html | div.result
//// define
`block_list`：<samp>array</samp>

- List of blocks, with certain block states, that we are monitoring to see if the entity is inside.


////

<div class="language-text highlight"><span class="filename"><code>block_list</code></span><pre id="__code_1"><span></span></pre></div>

//// html | div.result
///// define
`<any array element>`：<samp>object</samp>

- A of block, with certain block states, that we are monitoring to see if the entity is inside.


/////

<div class="language-text highlight"><span class="filename"><code>&lt;any array element&gt;</code></span><pre id="__code_1"><span></span></pre></div>

///// html | div.result
////// define
`block`：<samp>block</samp> {#assets.schemas-blockception.general.block_definition.json}


//////

```mcschema
block:
{
  string "name" : opt
  object "states" : opt
  {
    string "<any object property>" : opt
    boolean "<any object property>" : opt
    number "<any object property>" : opt
  }
}

```

////// html | div.result
/////// define
`name`：<samp>string</samp>

- The block id, for example: `minecraft:air'.


///////


/////// define
`states`：<samp>object</samp>

- The block states.


///////

<div class="language-text highlight"><span class="filename"><code>states</code></span><pre id="__code_1"><span></span></pre></div>

/////// html | div.result
//////// define
`<any object property>`：<samp>string</samp>

- A single state of a block.


////////


//////// define
`<any object property>`：<samp>boolean</samp>

- A single state of a block.


////////


//////// define
`<any object property>`：<samp>number</samp>

- A single state of a block.


////////



///////


//////



////// define
`entered_block_event`：<samp>event_object</samp> {#assets.schemas-blockception.behavior.entities.format.types.event_object.json}

- Event to run when this mob enters a valid block.


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
`exited_block_event`：<samp>[event_object](#assets.schemas-blockception.behavior.entities.format.types.event_object.json)</samp>

- Event to run when this mob leaves a valid block.


//////


/////


////


///

