# Go Home

> 文档版本：1.21.0.24

Allows the mob to move back to the position they were spawned.

## 架构

```mcschema
go_home:
{
  priority "priority"
  speed_multiplier "speed_multiplier"
  number "goal_radius" : opt
  integer "interval" : opt
  trigger "on_home"
  array "on_failed" : opt
  {
    event "<any array element>"
  }
  number "calculate_new_path_radius" : opt
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
`goal_radius`：<samp>number</samp>

- Distance in blocks within the mob considers it has reached the goal. This is the `wiggle room` to stop the AI from bouncing back and forth trying to reach a specific spot


////


//// define
`interval`：<samp>integer</samp>

- A random value to determine when to randomly move somewhere. This has a 1/interval chance to choose this goal


////


//// define
`on_home`：<samp>trigger</samp> {#assets.schemas-blockception.behavior.entities.format.types.trigger.json}

- Event(s) to run when this mob gets home.


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
`on_failed`：<samp>array</samp>

- Event(s) to run when this goal fails.


////

<div class="language-text highlight"><span class="filename"><code>on_failed</code></span><pre id="__code_1"><span></span></pre></div>

//// html | div.result
///// define
`<any array element>`：<samp>event</samp> {#assets.schemas-blockception.behavior.entities.format.types.event.json}


/////

```mcschema
event:
string

```

///// html | div.result

/////


```mcschema
event:
{
  string "event" : opt
  string "target" : opt
}

```

///// html | div.result
////// define
`event`：<samp>string</samp>

- The event to fire.


//////


////// define
`target`：<samp>string</samp>

- The target of the event.


//////


/////




////


//// define
`calculate_new_path_radius`：<samp>number</samp>

- Distance in blocks that the mob is considered close enough to the end of the current path. A new path will then be calculated to continue toward home.


////


///

