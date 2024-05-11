# Dig

> 文档版本：1.21.0.24

[EXPERIMENTAL BEHAVIOR] Activates the `DIGGING` actor flag during the specified duration. Currently only Warden can use the Dig goal

## 架构

```mcschema
dig:
{
  priority "priority"
  boolean "allow_dig_when_named" : opt
  boolean "digs_in_daylight" : opt
  number "duration" : opt
  number "idle_time" : opt
  boolean "suspicion_is_disturbance" : opt
  boolean "vibration_is_disturbance" : opt
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
`allow_dig_when_named`：<samp>boolean</samp>

- If true, this behavior can run when this entity is named. Otherwise not.


////


//// define
`digs_in_daylight`：<samp>boolean</samp>

- Indicates that the actor should start digging when it sees daylight.


////


//// define
`duration`：<samp>number</samp>

- Goal duration in seconds.


////


//// define
`idle_time`：<samp>number</samp>

- The minimum idle time in seconds between the last detected disturbance to the start of digging.


////


//// define
`suspicion_is_disturbance`：<samp>boolean</samp>

- If true, finding new suspicious locations count as disturbances that may delay the start of this goal.


////


//// define
`vibration_is_disturbance`：<samp>boolean</samp>

- If true, vibrations count as disturbances that may delay the start of this goal.


////


//// define
`on_start`：<samp>trigger</samp> {#assets.schemas-blockception.behavior.entities.format.types.trigger.json}

- The event to run when the goal start


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




///

