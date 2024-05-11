# Angry

> 文档版本：1.21.0.24

Defines the entity's 'angry' state using a timer.

## 架构

```mcschema
angry:
{
  boolean "broadcast_anger" : opt
  filters "broadcast_filters"
  filters "filters"
  integer "broadcast_range" : opt
  array "broadcast_targets" : opt
  {
    string "<any array element>" : opt
  }
  event_object "calm_event"
  sound_event "angry_sound"
  boolean "broadcast_anger_on_attack" : opt
  boolean "broadcast_anger_on_being_attacked" : opt
  integer "duration" : opt
  integer "duration_delta" : opt
  array "sound_interval" : opt
  {
    integer "0..0" : opt
    integer "1..1" : opt
  }
  object "sound_interval" : opt
  {
    number "range_min" : opt
    number "range_max" : opt
  }
}

```

/// html | div.result
//// define
`broadcast_anger`：<samp>boolean</samp>

- If true, other entities of the same entity definition within the broadcastRange will also become angry.


////


//// define
`broadcast_filters`：<samp>filters</samp>

- 一个[过滤器组](../filter.md)。Conditions that make this entry in the list valid.


////


//// define
`filters`：<samp>filters</samp>

- 一个[过滤器组](../filter.md)。Filter out mob types that it should not attack while angry (other Piglins).


////


//// define
`broadcast_range`：<samp>integer</samp>

- Distance in blocks within which other entities of the same entity definition will become angry.


////


//// define
`broadcast_targets`：<samp>array</samp>

- A list of entity families to broadcast anger to.


////

<div class="language-text highlight"><span class="filename"><code>broadcast_targets</code></span><pre id="__code_1"><span></span></pre></div>

//// html | div.result
///// define
`<any array element>`：<samp>string</samp>

- An entity family.


/////


////


//// define
`calm_event`：<samp>event_object</samp> {#assets.schemas-blockception.behavior.entities.format.types.event_object.json}

- Event to run after the number of seconds specified in duration expires (when the entity stops being "angry")


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
`angry_sound`：<samp>sound_event</samp> {#assets.schemas-blockception.general.sound_event.json}

- The sound event to play when the mob is angry.


////

```mcschema
sound_event:
string

```

//// html | div.result

////



//// define
`broadcast_anger_on_attack`：<samp>boolean</samp>

- If true, other entities of the same entity definition within the broadcastRange will also become angry whenever this mob attacks.


////


//// define
`broadcast_anger_on_being_attacked`：<samp>boolean</samp>

- If true, other entities of the same entity definition within the broadcastRange will also become angry whenever this mob is attacked.


////


//// define
`duration`：<samp>integer</samp>

- The amount of time in seconds that the entity will be angry.


////


//// define
`duration_delta`：<samp>integer</samp>

- Variance in seconds added to the duration [-delta, delta].


////


//// define
`sound_interval`：<samp>array</samp>

- The range of time in seconds to randomly wait before playing the sound again.


////

<div class="language-text highlight"><span class="filename"><code>sound_interval</code></span><pre id="__code_1"><span></span></pre></div>

//// html | div.result
///// define
`0..0`：<samp>integer</samp>

- The minimum interval.


/////


///// define
`1..1`：<samp>integer</samp>

- The maximum interval.


/////


////


//// define
`sound_interval`：<samp>object</samp>

- The range of time in seconds to randomly wait before playing the sound again.


////

<div class="language-text highlight"><span class="filename"><code>sound_interval</code></span><pre id="__code_1"><span></span></pre></div>

//// html | div.result
///// define
`range_min`：<samp>number</samp>

- The minimum interval.


/////


///// define
`range_max`：<samp>number</samp>

- The maximum interval.


/////


////



///

