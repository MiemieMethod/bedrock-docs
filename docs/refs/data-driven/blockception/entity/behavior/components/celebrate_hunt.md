# Celebrate Hunt

> 文档版本：1.21.0.24

Specifies hunt celebration behavior.

## 架构

```mcschema
celebrate_hunt:
{
  boolean "broadcast" : opt
  filters "celebration_targets"
  sound_event "celebrate_sound"
  integer "duration" : opt
  number "radius" : opt
  array "sound_interval" : opt
  {
    number "0..0" : opt
    number "1..1" : opt
  }
  number "sound_interval" : opt
  object "sound_interval" : opt
  {
    number "range_min" : opt
    number "range_max" : opt
  }
}

```

/// html | div.result
//// define
`broadcast`：<samp>boolean</samp>

- If true, celebration will be broadcasted to other entities in the radius.


////


//// define
`celebration_targets`：<samp>filters</samp>

- 一个[过滤器组](../filter.md)。The list of conditions that target of hunt must satisfy to initiate celebration.


////


//// define
`celebrate_sound`：<samp>sound_event</samp> {#assets.schemas-blockception.general.sound_event.json}

- The sound event to play when the mob is celebrating.


////

```mcschema
sound_event:
string

```

//// html | div.result

////



//// define
`duration`：<samp>integer</samp>

- Duration, in seconds, of celebration.


////


//// define
`radius`：<samp>number</samp>

- If broadcast is enabled, specifies the radius in which it will notify other entities for celebration.


////


//// define
`sound_interval`：<samp>array</samp>

- The range of time in seconds to randomly wait before playing the sound again.


////

<div class="language-text highlight"><span class="filename"><code>sound_interval</code></span><pre id="__code_1"><span></span></pre></div>

//// html | div.result
///// define
`0..0`：<samp>number</samp>


/////


///// define
`1..1`：<samp>number</samp>


/////


////


//// define
`sound_interval`：<samp>number</samp>

- The range of time in seconds to randomly wait before playing the sound again.


////


//// define
`sound_interval`：<samp>object</samp>

- The range of time in seconds to randomly wait before playing the sound again.


////

<div class="language-text highlight"><span class="filename"><code>sound_interval</code></span><pre id="__code_1"><span></span></pre></div>

//// html | div.result
///// define
`range_min`：<samp>number</samp>

- Minimum.


/////


///// define
`range_max`：<samp>number</samp>

- Maximum.


/////


////



///

