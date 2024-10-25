# Timer Flag

> 文档版本：1.21.50.25

Fires an event when this behavior starts, then waits for a duration before stopping. When stopping due to that timeout or due to being interrupted by another behavior, fires another event. query.timer_flag_<n> will return 1.0 on both the client and server when this behavior is running, and 0.0 otherwise.

## 架构

```mcschema
timer_flag:
{
  priority "priority"
  number "cooldown_range" : opt
  vector_of_2_items "cooldown_range"
  number "duration_range" : opt
  vector_of_2_items "duration_range"
  array "control_flags" : opt
  {
    string "<any array element>" : opt
  }
  trigger "on_end"
  trigger "on_start"
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
`cooldown_range`：<samp>number</samp>

- Goal cooldown range in seconds.


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
`duration_range`：<samp>number</samp>

- Goal duration range in seconds.


////


//// define
`duration_range`：<samp>[vector_of_2_items](#assets.schemas-blockception.general.vectors.number2.json)</samp>

- Goal duration range in seconds.


////



//// define
`control_flags`：<samp>array</samp>

- UNDOCUMENTED


////

<div class="language-text highlight"><span class="filename"><code>control_flags</code></span><pre id="__code_1"><span></span></pre></div>

//// html | div.result
///// define
`<any array element>`：<samp>string</samp>


/////


////


//// define
`on_end`：<samp>trigger</samp> {#assets.schemas-blockception.behavior.entities.format.types.trigger.json}

- Event to run when the goal ends.


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
`on_start`：<samp>[trigger](#assets.schemas-blockception.behavior.entities.format.types.trigger.json)</samp>

- Event to run when the goal starts.


////


///

