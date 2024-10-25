# Work Composter

> 文档版本：1.21.50.25

Allows the NPC to use the composter POI to convert excess seeds into bone meal.

## 架构

```mcschema
work_composter:
{
  priority "priority"
  speed_multiplier "speed_multiplier"
  integer "active_time" : opt
  integer "block_interaction_max" : opt
  boolean "can_empty_composter" : opt
  boolean "can_fill_composter" : opt
  boolean "can_work_in_rain" : opt
  integer "goal_cooldown" : opt
  integer "items_per_use_max" : opt
  integer "min_item_count" : opt
  trigger "on_arrival"
  integer "sound_delay_max" : opt
  integer "sound_delay_min" : opt
  integer "use_block_max" : opt
  integer "use_block_min" : opt
  integer "work_in_rain_tolerance" : opt
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
`active_time`：<samp>integer</samp>

- The amount of ticks the NPC will stay in their the work location.


////


//// define
`block_interaction_max`：<samp>integer</samp>

- The maximum number of times the mob will interact with the composter.


////


//// define
`can_empty_composter`：<samp>boolean</samp>

- Determines whether the mob can empty a full composter.


////


//// define
`can_fill_composter`：<samp>boolean</samp>

- Determines whether the mob can add items to a composter given that it is not full.


////


//// define
`can_work_in_rain`：<samp>boolean</samp>

- If true, this entity can work when their jobsite POI is being rained on.


////


//// define
`goal_cooldown`：<samp>integer</samp>

- The amount of ticks the goal will be on cooldown before it can be used again.


////


//// define
`items_per_use_max`：<samp>integer</samp>

- The maximum number of items which can be added to the composter per block interaction.


////


//// define
`min_item_count`：<samp>integer</samp>

- Limits the amount of each compostable item the mob can use. Any amount held over this number will be composted if possible


////


//// define
`on_arrival`：<samp>trigger</samp> {#assets.schemas-blockception.behavior.entities.format.types.trigger.json}

- Event to run when the mob reaches their jobsite.


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
`sound_delay_max`：<samp>integer</samp>

- Unused.


////


//// define
`sound_delay_min`：<samp>integer</samp>

- Unused.


////


//// define
`use_block_max`：<samp>integer</samp>

- The maximum interval in which the mob will interact with the composter.


////


//// define
`use_block_min`：<samp>integer</samp>

- The minimum interval in which the mob will interact with the composter.


////


//// define
`work_in_rain_tolerance`：<samp>integer</samp>

- If "can_work_in_rain" is false, this is the maximum number of ticks left in the goal where rain will not interrupt the goal


////


///

