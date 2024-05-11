# Ram Attack

> 文档版本：1.21.0.24

Allows the mob to search for a random target and, if a direct path exists between the mob and the target, it will perform a charge. If the attack hits, the target will be knocked back based on the mob's speed.

## 架构

```mcschema
ram_attack:
{
  priority "priority"
  number "baby_knockback_modifier" : opt
  range_number_type "cooldown_range"
  number "knockback_force" : opt
  number "knockback_height" : opt
  number "min_ram_distance" : opt
  trigger "on_start"
  sound_event "pre_ram_sound"
  number "ram_distance" : opt
  sound_event "ram_impact_sound"
  number "ram_speed" : opt
  number "run_speed" : opt
  trigger "trigger"
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
`baby_knockback_modifier`：<samp>number</samp>

- The modifier to knockback that babies have.


////


//// define
`cooldown_range`：<samp>range_number_type</samp> {#assets.schemas-blockception.behavior.entities.format.types.range_number_type.json}

- Minimum and maximum cooldown time-range (positive, in seconds) between each attempted ram attack.


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




//// define
`knockback_force`：<samp>number</samp>

- The force of the knockback of the ram attack.


////


//// define
`knockback_height`：<samp>number</samp>

- The height of the knockback of the ram attack.


////


//// define
`min_ram_distance`：<samp>number</samp>

- The minimum distance at which the mob can start a ram attack.


////


//// define
`on_start`：<samp>trigger</samp> {#assets.schemas-blockception.behavior.entities.format.types.trigger.json}

- The event to trigger when attacking.


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
`pre_ram_sound`：<samp>sound_event</samp> {#assets.schemas-blockception.general.sound_event.json}

- The sound to play when an entity is about to perform a ram attack.


////

```mcschema
sound_event:
string

```

//// html | div.result

////



//// define
`ram_distance`：<samp>number</samp>

- The distance at which the mob start to run with ram speed.


////


//// define
`ram_impact_sound`：<samp>[sound_event](#assets.schemas-blockception.general.sound_event.json)</samp>

- The sound to play when an entity is impacting on a ram attack.


////


//// define
`ram_speed`：<samp>number</samp>

- Sets the entity's speed when charging toward the target.


////


//// define
`run_speed`：<samp>number</samp>

- Sets the entity's speed when running toward the target.


////


//// define
`trigger`：<samp>[trigger](#assets.schemas-blockception.behavior.entities.format.types.trigger.json)</samp>

- The event to trigger when attacking.


////


///

