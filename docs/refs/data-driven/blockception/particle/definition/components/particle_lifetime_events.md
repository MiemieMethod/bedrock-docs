# Particle Lifetime Events Component For 1.10.0

> 文档版本：1.21.0.24

UNDOCUMENTED.

## 架构

```mcschema
particle_lifetime_events:
{
  array "creation_event" : opt
  {
    string "<any array element>" : opt
  }
  string "creation_event" : opt
   "custom_events" : opt
  array "expiration_event" : opt
  {
    string "<any array element>" : opt
  }
  string "expiration_event" : opt
   "timeline" : opt
}

```

/// html | div.result
//// define
`creation_event`：<samp>array</samp>

- Fires when the particle is created.


////

<div class="language-text highlight"><span class="filename"><code>creation_event</code></span><pre id="__code_1"><span></span></pre></div>

//// html | div.result
///// define
`<any array element>`：<samp>string</samp>


/////


////


//// define
`creation_event`：<samp>string</samp>

- Fires when the particle is created.


////



//// define
`custom_events`

- UNDOCUMENTED, unclear structure :(.


////


//// define
`expiration_event`：<samp>array</samp>

- Fires when the particle expires (does not wait for particles to expire too).


////

<div class="language-text highlight"><span class="filename"><code>expiration_event</code></span><pre id="__code_1"><span></span></pre></div>

//// html | div.result
///// define
`<any array element>`：<samp>string</samp>


/////


////


//// define
`expiration_event`：<samp>string</samp>

- Fires when the particle expires (does not wait for particles to expire too).


////



//// define
`timeline`

- UNDOCUMENTED: timeline.


////


///

