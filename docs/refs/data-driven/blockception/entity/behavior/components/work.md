# Work

> 文档版本：1.21.0.24

Allows the NPC to use the POI.

## 架构

```mcschema
work:
{
  priority "priority"
  speed_multiplier "speed_multiplier"
  integer "active_time" : opt
  boolean "can_work_in_rain" : opt
  integer "goal_cooldown" : opt
  trigger "on_arrival"
  integer "sound_delay_max" : opt
  integer "sound_delay_min" : opt
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
`can_work_in_rain`：<samp>boolean</samp>

- If true, this entity can work when their jobsite POI is being rained on.


////


//// define
`goal_cooldown`：<samp>integer</samp>

- The amount of ticks the goal will be on cooldown before it can be used again.


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

- The max interval in which a sound will play.


////


//// define
`sound_delay_min`：<samp>integer</samp>

- The min interval in which a sound will play.


////


//// define
`work_in_rain_tolerance`：<samp>integer</samp>

- If "can_work_in_rain" is false, this is the maximum number of ticks left in the goal where rain will not interrupt the goal


////


///

