# Scheduler

> 文档版本：1.21.0.24

fires off scheduled mob events at time of day events.

## 架构

```mcschema
scheduler:
{
  number "min_delay_secs" : opt
  number "max_delay_secs" : opt
  array "scheduled_events" : opt
  {
    object "<any array element>" : opt
    {
      filters "filters"
      event "event"
    }
  }
}

```

/// html | div.result
//// define
`min_delay_secs`：<samp>number</samp>

- The minimum the scheduler will be delayed.


////


//// define
`max_delay_secs`：<samp>number</samp>

- The maximum the scheduler will be delayed.


////


//// define
`scheduled_events`：<samp>array</samp>

- The list of triggers that fire when the conditions match the given filter criteria. If any filter criteria overlap the first defined event will be picked.


////

<div class="language-text highlight"><span class="filename"><code>scheduled_events</code></span><pre id="__code_1"><span></span></pre></div>

//// html | div.result
///// define
`<any array element>`：<samp>object</samp>

- A filter and event pair. The event runs when the filter criteria succeeds


/////

<div class="language-text highlight"><span class="filename"><code>&lt;any array element&gt;</code></span><pre id="__code_1"><span></span></pre></div>

///// html | div.result
////// define
`filters`：<samp>filters</samp>

- 一个[过滤器组](../filter.md)。


//////


////// define
`event`：<samp>event</samp> {#assets.schemas-blockception.behavior.entities.format.types.event.json}


//////

```mcschema
event:
string

```

////// html | div.result

//////


```mcschema
event:
{
  string "event" : opt
  string "target" : opt
}

```

////// html | div.result
/////// define
`event`：<samp>string</samp>

- The event to fire.


///////


/////// define
`target`：<samp>string</samp>

- The target of the event.


///////


//////




/////


////


///

