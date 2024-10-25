# Attack Cooldown

> 文档版本：1.21.50.25

Adds a cooldown to a mob. The intention of this cooldown is to be used to prevent the mob from attempting to aquire new attack targets.

## 架构

```mcschema
attack_cooldown:
{
  trigger "attack_cooldown_complete_event"
  array "attack_cooldown_time" : opt
  {
    number "0..0" : opt
    number "1..1" : opt
  }
  number "attack_cooldown_time" : opt
}

```

/// html | div.result
//// define
`attack_cooldown_complete_event`：<samp>trigger</samp> {#assets.schemas-blockception.behavior.entities.format.types.trigger.json}

- Event to be run when the cooldown is complete.


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
`attack_cooldown_time`：<samp>array</samp>

- Amount of time in seconds for the cooldown. Can be specified as a number or a pair of numbers (Minimum and max).


////

<div class="language-text highlight"><span class="filename"><code>attack_cooldown_time</code></span><pre id="__code_1"><span></span></pre></div>

//// html | div.result
///// define
`0..0`：<samp>number</samp>


/////


///// define
`1..1`：<samp>number</samp>


/////


////


//// define
`attack_cooldown_time`：<samp>number</samp>

- Amount of time in seconds for the cooldown. Can be specified as a number or a pair of numbers (Minimum and max).


////



///

