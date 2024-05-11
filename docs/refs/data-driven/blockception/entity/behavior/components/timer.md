# Timer

> 文档版本：1.21.0.24

Adds a timer after which an event will fire.

## 架构

```mcschema
timer:
{
  boolean "looping" : opt
  boolean "randomInterval" : opt
  array "time" : opt
  {
    number "0..0" : opt
    number "1..1" : opt
  }
  number "time" : opt
  event_object "time_down_event"
  array "random_time_choices" : opt
  {
    object "<any array element>" : opt
    {
      integer "weight" : opt
      integer "value" : opt
    }
  }
}

```

/// html | div.result
//// define
`looping`：<samp>boolean</samp>

- If true, the timer will restart every time after it fires.


////


//// define
`randomInterval`：<samp>boolean</samp>

- If true, the amount of time on the timer will be random between the Minimum and Maximum values specified in time.


////


//// define
`time`：<samp>array</samp>

- Amount of time in seconds for the timer. Can be specified as a number or a pair of numbers (Minimum and max). Incompatible with random_time_choices.


////

<div class="language-text highlight"><span class="filename"><code>time</code></span><pre id="__code_1"><span></span></pre></div>

//// html | div.result
///// define
`0..0`：<samp>number</samp>


/////


///// define
`1..1`：<samp>number</samp>


/////


////


//// define
`time`：<samp>number</samp>

- Amount of time in seconds for the timer. Can be specified as a number or a pair of numbers (Minimum and max). Incompatible with random_time_choices.


////



//// define
`time_down_event`：<samp>event_object</samp> {#assets.schemas-blockception.behavior.entities.format.types.event_object.json}

- Event to fire when the time on the timer runs out.


////

```mcschema
event_object:
{
  filters "filters"
  string "event" : opt
  string "target" : opt
}

```

//// html | div.result
///// define
`filters`：<samp>filters</samp>

- 一个[过滤器组](../filter.md)。


/////


///// define
`event`：<samp>string</samp>

- The event to fire.


/////


///// define
`target`：<samp>string</samp>

- The target of the event.


/////


////



//// define
`random_time_choices`：<samp>array</samp>

- This is a list of objects, representing one value in seconds that can be picked before firing the event and an optional weight. Incompatible with time.


////

<div class="language-text highlight"><span class="filename"><code>random_time_choices</code></span><pre id="__code_1"><span></span></pre></div>

//// html | div.result
///// define
`<any array element>`：<samp>object</samp>

- representing one value in seconds that can be picked before firing the event and an optional weight. Incompatible with time.


/////

<div class="language-text highlight"><span class="filename"><code>&lt;any array element&gt;</code></span><pre id="__code_1"><span></span></pre></div>

///// html | div.result
////// define
`weight`：<samp>integer</samp>

- The weight on how likely this section is to trigger.


//////


////// define
`value`：<samp>integer</samp>

- The value in seconds that would be used if this section was picked.


//////


/////


////


///

