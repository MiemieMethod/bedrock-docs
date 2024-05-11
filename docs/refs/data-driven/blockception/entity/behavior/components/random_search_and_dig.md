# Random Look Around

> 文档版本：1.21.0.24

Allows this entity to locate a random target block that it can path find to. Once found, the entity will move towards it and dig up an item.

## 架构

```mcschema
random_search_and_dig:
{
  priority "priority"
  speed_multiplier "speed_multiplier"
  vector_of_2_items "cooldown_range"
  number "cooldown_range" : opt
  vector_of_2_items "digging_duration_range"
  number "find_valid_position_retries" : opt
  number "goal_radius" : opt
  string "item_table" : opt
  trigger "on_digging_start"
  trigger "on_fail_during_digging"
  trigger "on_fail_during_searching"
  trigger "on_item_found"
  trigger "on_searching_start"
  trigger "on_success"
  number "search_range_xz" : opt
  number "search_range_y" : opt
  number "spawn_item_after_seconds" : opt
  number "spawn_item_pos_offset" : opt
  array "target_blocks" : opt
  {
    reference "<any array element>"
  }
  number "target_dig_position_offset" : opt
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
`speed_multiplier`：<samp>speed_multiplier</samp> {#assets.schemas-blockception.behavior.entities.format.behaviors.types.speed_multiplier.json}


////

```mcschema
speed_multiplier:
number

```

//// html | div.result

////



//// define
`cooldown_range`：<samp>vector_of_2_items</samp> {#assets.schemas-blockception.general.vectors.number2.json}

- Goal cooldown range in seconds.


////

```mcschema
vector_of_2_items:
array
{
  number "0..0" : opt
  number "1..1" : opt
}

```

//// html | div.result
///// define
`0..0`：<samp>number</samp>

- The X component.


/////


///// define
`1..1`：<samp>number</samp>

- The Y component.


/////


////



//// define
`cooldown_range`：<samp>number</samp>

- Goal cooldown range in seconds.


////



//// define
`digging_duration_range`：<samp>[vector_of_2_items](#assets.schemas-blockception.general.vectors.number2.json)</samp>

- Digging duration in seconds.


////


//// define
`find_valid_position_retries`：<samp>number</samp>

- Amount of retries to find a valid target position within search range.


////


//// define
`goal_radius`：<samp>number</samp>

- Distance in blocks within the entity to considers it has reached it's target position.


////


//// define
`item_table`：<samp>string</samp>

- File path relative to the resource pack root for items to spawn list (loot table format).


////


//// define
`on_digging_start`：<samp>trigger</samp> {#assets.schemas-blockception.behavior.entities.format.types.trigger.json}

- Event to run when the goal ends searching has begins digging.


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
`on_fail_during_digging`：<samp>[trigger](#assets.schemas-blockception.behavior.entities.format.types.trigger.json)</samp>

- Event to run when the goal failed while in digging state.


////


//// define
`on_fail_during_searching`：<samp>[trigger](#assets.schemas-blockception.behavior.entities.format.types.trigger.json)</samp>

- Event to run when the goal failed while in searching state.


////


//// define
`on_item_found`：<samp>[trigger](#assets.schemas-blockception.behavior.entities.format.types.trigger.json)</samp>

- Event to run when the goal find a item.


////


//// define
`on_searching_start`：<samp>[trigger](#assets.schemas-blockception.behavior.entities.format.types.trigger.json)</samp>

- Event to run when the goal starts searching.


////


//// define
`on_success`：<samp>[trigger](#assets.schemas-blockception.behavior.entities.format.types.trigger.json)</samp>

- Event to run when searching and digging has ended.


////


//// define
`search_range_xz`：<samp>number</samp>

- Width and length of the volume around the entity used to find a valid target position


////


//// define
`search_range_y`：<samp>number</samp>

- Height of the volume around the entity used to find a valid target position


////


//// define
`spawn_item_after_seconds`：<samp>number</samp>

- Digging duration before spawning item in seconds.


////


//// define
`spawn_item_pos_offset`：<samp>number</samp>

- Distance to offset the item's spawn location in the direction the mob is facing.


////


//// define
`target_blocks`：<samp>array</samp>

- List of target block types the goal will look to dig on. Overrides the default list.


////

<div class="language-text highlight"><span class="filename"><code>target_blocks</code></span><pre id="__code_1"><span></span></pre></div>

//// html | div.result
///// define
`<any array element>`：<samp>reference</samp> {#assets.schemas-blockception.general.block.reference.json}


/////

```mcschema
identifier:
string

```

///// html | div.result

/////



```mcschema
reference:
{
  identifier "name"
  object "states" : opt
  {
    ['boolean', 'integer', 'string'] "\w*:?\w+" : opt
  }
  0 "tags"
}

```

///// html | div.result
////// define
`name`：<samp>[identifier](#assets.schemas-blockception.general.block.identifier.json)</samp>


//////


////// define
`states`：<samp>object</samp>


//////

<div class="language-text highlight"><span class="filename"><code>states</code></span><pre id="__code_1"><span></span></pre></div>

////// html | div.result
/////// define
`\w*:?\w+`：<samp>['boolean', 'integer', 'string']</samp>

- The key of property is the name of the block state/property, the value must be the same as the block properties accepted values.


///////


//////


////// define
`tags`：<samp>0</samp> {#assets.schemas-blockception.molang.string.json}

- A condition using Molang queries that results to true/false that can be used to query for blocks with certain tags.


//////

```mcschema
0:
string

```

////// html | div.result

//////



/////




////


//// define
`target_dig_position_offset`：<samp>number</samp>

- Dig target position offset from the feet position of the mob in their facing direction.


////


///

