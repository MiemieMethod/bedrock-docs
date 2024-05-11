# Celebrate

> 文档版本：1.21.0.24

Allows this entity to celebrate surviving a raid by making celebration sounds and jumping.

## 架构

```mcschema
celebrate:
{
  priority "priority"
  sound_event "celebration_sound"
  number "duration" : opt
  array "jump_interval" : opt
  {
    number "0..0" : opt
    number "1..1" : opt
  }
  number "jump_interval" : opt
  object "jump_interval" : opt
  {
    number "range_min" : opt
    number "range_max" : opt
  }
  trigger "on_celebration_end_event"
  range_number_type "sound_interval"
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
`celebration_sound`：<samp>sound_event</samp> {#assets.schemas-blockception.general.sound_event.json}

- The sound event to trigger during the celebration.


////

```mcschema
sound_event:
string

```

//// html | div.result

////



//// define
`duration`：<samp>number</samp>

- The duration in seconds that the celebration lasts for.


////


//// define
`jump_interval`：<samp>array</samp>

- Minimum and maximum time between jumping (positive, in seconds).


////

<div class="language-text highlight"><span class="filename"><code>jump_interval</code></span><pre id="__code_1"><span></span></pre></div>

//// html | div.result
///// define
`0..0`：<samp>number</samp>


/////


///// define
`1..1`：<samp>number</samp>


/////


////


//// define
`jump_interval`：<samp>number</samp>

- Minimum and maximum time between jumping (positive, in seconds).


////


//// define
`jump_interval`：<samp>object</samp>

- Minimum and maximum time between jumping (positive, in seconds).


////

<div class="language-text highlight"><span class="filename"><code>jump_interval</code></span><pre id="__code_1"><span></span></pre></div>

//// html | div.result
///// define
`range_min`：<samp>number</samp>


/////


///// define
`range_max`：<samp>number</samp>


/////


////



//// define
`on_celebration_end_event`：<samp>trigger</samp> {#assets.schemas-blockception.behavior.entities.format.types.trigger.json}

- The event to trigger when the goal's duration expires.


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
`sound_interval`：<samp>range_number_type</samp> {#assets.schemas-blockception.behavior.entities.format.types.range_number_type.json}

- Minimum and maximum time between sound events (positive, in seconds).


////

```mcschema
range_number_type:
number

```

//// html | div.result

////


```mcschema
range_number_type:
array
{
  number "0..0" : opt
  number "1..1" : opt
}

```

//// html | div.result
///// define
`0..0`：<samp>number</samp>

- The first value of the range.


/////


///// define
`1..1`：<samp>number</samp>

- The second value of the range.


/////


////


```mcschema
range_number_type:
{
  number "range_min" : opt
  number "range_max" : opt
}

```

//// html | div.result
///// define
`range_min`：<samp>number</samp>

- The minimum value of the range.


/////


///// define
`range_max`：<samp>number</samp>

- The maximum value of the range.


/////


////




///

