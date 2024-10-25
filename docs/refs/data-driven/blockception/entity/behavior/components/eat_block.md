# Eat Block

> 文档版本：1.21.50.25

Allows the entity to consume a block, replace the eaten block with another block, and trigger an event as a result.

## 架构

```mcschema
eat_block:
{
  priority "priority"
  trigger "on_eat"
  0 "success_chance"
  number "time_until_eat" : opt
  array "eat_and_replace_block_pairs" : opt
  {
    object "<any array element>" : opt
    {
      identifier "eat_block"
      identifier "replace_block"
    }
  }
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
`on_eat`：<samp>trigger</samp> {#assets.schemas-blockception.behavior.entities.format.types.trigger.json}

- The event to trigger when the block eating animation has completed.


////

```mcschema
trigger:
string

```

//// html | div.result

////


```mcschema
trigger:
{
  string "event" : opt
  filters "filters"
  subject "target"
}

```

//// html | div.result
///// define
`event`：<samp>string</samp>

- The event to run when the conditions for this trigger are met.


/////


///// define
`filters`：<samp>filters</samp>

- 一个[过滤器组](../filter.md)。The list of conditions for this trigger to execute.


/////


///// define
`target`：<samp>subject</samp> {#assets.schemas-blockception.behavior.entities.filters.filters.types.subject.json}

- The target of the event.


/////

```mcschema
subject:
string

```

///// html | div.result

/////



////


```mcschema
trigger:
array
{
  object "<any array element>" : opt
  {
    string "event" : opt
    filters "filters"
    subject "target"
  }
}

```

//// html | div.result
///// define
`<any array element>`：<samp>object</samp>


/////

<div class="language-text highlight"><span class="filename"><code>&lt;any array element&gt;</code></span><pre id="__code_1"><span></span></pre></div>

///// html | div.result

/////


////




//// define
`success_chance`：<samp>0</samp> {#assets.schemas-blockception.molang.number.json}

- A molang expression defining the success chance the entity has to consume a block.


////

```mcschema
0:
string

```

//// html | div.result

////


```mcschema
0:
number

```

//// html | div.result

////




//// define
`time_until_eat`：<samp>number</samp>

- The amount of time (in seconds) it takes for the block to be eaten upon a successful eat attempt.


////


//// define
`eat_and_replace_block_pairs`：<samp>array</samp>

- A collection of pairs of blocks; the first ("eat_block")is the block the entity should eat, the second ("replace_block") is the block that should replace the eaten block.


////

<div class="language-text highlight"><span class="filename"><code>eat_and_replace_block_pairs</code></span><pre id="__code_1"><span></span></pre></div>

//// html | div.result
///// define
`<any array element>`：<samp>object</samp>

- The block to eat and the block to replace it with.


/////

<div class="language-text highlight"><span class="filename"><code>&lt;any array element&gt;</code></span><pre id="__code_1"><span></span></pre></div>

///// html | div.result
////// define
`eat_block`：<samp>identifier</samp> {#assets.schemas-blockception.general.block.identifier.json}

- The block to eat.


//////

```mcschema
identifier:
string

```

////// html | div.result

//////



////// define
`replace_block`：<samp>[identifier](#assets.schemas-blockception.general.block.identifier.json)</samp>

- The block to replace the eaten block with.


//////


/////


////


///

