# Move To Block

> 文档版本：1.21.0.24

Allows mob to move towards a block.

## 架构

```mcschema
move_to_block:
{
  priority "priority"
  number "goal_radius" : opt
  trigger "on_stay_completed"
  trigger "on_reach"
  number "start_chance" : opt
  integer "search_range" : opt
  integer "search_height" : opt
  number "stay_duration" : opt
  string "target_selection_method" : opt
  array "target_offset" : opt
  {
    number "0..0" : opt
    number "1..1" : opt
    number "2..2" : opt
  }
  array "target_blocks" : opt
  {
    descriptor "<any array element>"
  }
  filters "target_block_filters"
  integer "tick_interval" : opt
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
`goal_radius`：<samp>number</samp>

- Distance in blocks within the mob considers it has reached the goal. This is the "wiggle room" to stop the AI from bouncing back and forth trying to reach a specific spot


////


//// define
`on_stay_completed`：<samp>trigger</samp> {#assets.schemas-blockception.behavior.entities.format.types.trigger.json}

- Event to run on completing a stay of stay_duration at the block.


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
`on_reach`：<samp>[trigger](#assets.schemas-blockception.behavior.entities.format.types.trigger.json)</samp>

- Event to run on block reached.


////


//// define
`start_chance`：<samp>number</samp>

- Chance to start the behavior (applied after each random tick_interval).


////


//// define
`search_range`：<samp>integer</samp>

- The distance in blocks that the mob will look for the block.


////


//// define
`search_height`：<samp>integer</samp>

- The height in blocks that the mob will look for the block.


////


//// define
`stay_duration`：<samp>number</samp>

- Number of ticks needed to complete a stay at the block.


////


//// define
`target_selection_method`：<samp>string</samp>

- Kind of block to find fitting the specification. Valid values are "random" and "nearest".


////


//// define
`target_offset`：<samp>array</samp>

- Offset to add to the selected target position.


////

<div class="language-text highlight"><span class="filename"><code>target_offset</code></span><pre id="__code_1"><span></span></pre></div>

//// html | div.result
///// define
`0..0`：<samp>number</samp>


/////


///// define
`1..1`：<samp>number</samp>


/////


///// define
`2..2`：<samp>number</samp>


/////


////


//// define
`target_blocks`：<samp>array</samp>

- Block types to move to.


////

<div class="language-text highlight"><span class="filename"><code>target_blocks</code></span><pre id="__code_1"><span></span></pre></div>

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
`target_block_filters`：<samp>filters</samp>

- 一个[过滤器组](../filter.md)。Filters to apply on the target blocks. Target blocks are only valid if the filters are true.


////


//// define
`tick_interval`：<samp>integer</samp>

- Average interval in ticks to try to run this behavior.


////


///

