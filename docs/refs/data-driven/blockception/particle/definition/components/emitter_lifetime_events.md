# Emitter Lifetime Events Component For 1.10.0

> 文档版本：1.21.0.24

UNDOCUMENTED.

## 架构

```mcschema
emitter_lifetime_events:
{
  array "creation_event" : opt
  {
    string "<any array element>" : opt
  }
  string "creation_event" : opt
  array "expiration_event" : opt
  {
    string "<any array element>" : opt
  }
  string "expiration_event" : opt
  object "timeline" : opt
  {
    array "^[\d\.]+$" : opt
    {
      string "<any array element>" : opt
    }
    string "^[\d\.]+$" : opt
  }
   "travel_distance_events" : opt
  array "looping_travel_distance_events" : opt
  {
    object "<any array element>" : opt
    {
      number "distance" : opt
      array "effects" : opt
      {
        string "<any array element>" : opt
      }
      string "effects" : opt
    }
  }
}

```

/// html | div.result
//// define
`creation_event`：<samp>array</samp>

- Fires when the emitter is created.


////

<div class="language-text highlight"><span class="filename"><code>creation_event</code></span><pre id="__code_1"><span></span></pre></div>

//// html | div.result
///// define
`<any array element>`：<samp>string</samp>


/////


////


//// define
`creation_event`：<samp>string</samp>

- Fires when the emitter is created.


////



//// define
`expiration_event`：<samp>array</samp>

- Fires when the emitter expires (does not wait for particles to expire too).


////

<div class="language-text highlight"><span class="filename"><code>expiration_event</code></span><pre id="__code_1"><span></span></pre></div>

//// html | div.result
///// define
`<any array element>`：<samp>string</samp>


/////


////


//// define
`expiration_event`：<samp>string</samp>

- Fires when the emitter expires (does not wait for particles to expire too).


////



//// define
`timeline`：<samp>object</samp>

- A series of times, e.g. 0.0 or 1.0, that trigger the event, these get fired on every loop the emitter goes through, `time` is the time, e.g. one line might be: `0.4`: `event`


////

<div class="language-text highlight"><span class="filename"><code>timeline</code></span><pre id="__code_1"><span></span></pre></div>

//// html | div.result
///// define
`^[\d\.]+$`：<samp>array</samp>

- A single point in time that executes commands/molang/events.


/////

<div class="language-text highlight"><span class="filename"><code>^[\d\.]+$</code></span><pre id="__code_1"><span></span></pre></div>

///// html | div.result
////// define
`<any array element>`：<samp>string</samp>


//////


/////


///// define
`^[\d\.]+$`：<samp>string</samp>

- A single point in time that executes commands/molang/events.


/////



////


//// define
`travel_distance_events`

- A series of distances, e.g. 0.0 or 1.0, that trigger the event these get fired when the emitter has moved by the specified input distance, e.g. one line might be: `0.4`: `event`


////


//// define
`looping_travel_distance_events`：<samp>array</samp>

- A series of events that occur at set intervals these get fired every time the emitter has moved the specified input distance from the last time it was fired.


////

<div class="language-text highlight"><span class="filename"><code>looping_travel_distance_events</code></span><pre id="__code_1"><span></span></pre></div>

//// html | div.result
///// define
`<any array element>`：<samp>object</samp>


/////

<div class="language-text highlight"><span class="filename"><code>&lt;any array element&gt;</code></span><pre id="__code_1"><span></span></pre></div>

///// html | div.result
////// define
`distance`：<samp>number</samp>

- UNDOCUMENTED.


//////


////// define
`effects`：<samp>array</samp>

- UNDOCUMENTED.


//////

<div class="language-text highlight"><span class="filename"><code>effects</code></span><pre id="__code_1"><span></span></pre></div>

////// html | div.result
/////// define
`<any array element>`：<samp>string</samp>


///////


//////


////// define
`effects`：<samp>string</samp>

- UNDOCUMENTED.


//////



/////


////


///

