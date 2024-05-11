# Send Event

> 文档版本：1.21.0.24

Allows the mob to send an event to another mob.

## 架构

```mcschema
send_event:
{
  priority "priority"
  number "cast_duration" : opt
  boolean "look_at_target" : opt
  array "event_choices" : opt
  {
    object "<any array element>" : opt
    {
      number "min_activation_range" : opt
      number "max_activation_range" : opt
      number "cooldown_time" : opt
      number "cast_duration" : opt
      filters "filters"
      string "particle_color" : opt
      integer "weight" : opt
      sound_event "start_sound_event"
      array "sequence" : opt
      {
        object "<any array element>" : opt
        {
          number "base_delay" : opt
          string "event" : opt
          sound_event "sound_event"
        }
      }
    }
  }
  array "sequence" : opt
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
`cast_duration`：<samp>number</samp>

- Time in seconds for the entire event sending process.


////


//// define
`look_at_target`：<samp>boolean</samp>

- If true, the mob will face the entity it sends an event to.


////


//// define
`event_choices`：<samp>array</samp>

- List of spells for the mob to use.


////

<div class="language-text highlight"><span class="filename"><code>event_choices</code></span><pre id="__code_1"><span></span></pre></div>

//// html | div.result
///// define
`<any array element>`：<samp>object</samp>

- A spell that the mob can cast.


/////

<div class="language-text highlight"><span class="filename"><code>&lt;any array element&gt;</code></span><pre id="__code_1"><span></span></pre></div>

///// html | div.result
////// define
`min_activation_range`：<samp>number</samp>

- The minimum distance in blocks the target must be for this spell to be cast.


//////


////// define
`max_activation_range`：<samp>number</samp>

- The maxmimum distance in blocks the target must be for this spell to be cast.


//////


////// define
`cooldown_time`：<samp>number</samp>

- Time in seconds before the mob can use this spell again.


//////


////// define
`cast_duration`：<samp>number</samp>

- Time in seconds the spell casting will take.


//////


////// define
`filters`：<samp>filters</samp>

- 一个[过滤器组](../filter.md)。


//////


////// define
`particle_color`：<samp>string</samp>

- The color of the particles for this spell.


//////


////// define
`weight`：<samp>integer</samp>

- The weight of this spell. Controls how likely this spell will be picked


//////


////// define
`start_sound_event`：<samp>sound_event</samp> {#assets.schemas-blockception.general.sound_event.json}

- The sound event to play when using this spell.


//////

```mcschema
sound_event:
string

```

////// html | div.result

//////



////// define
`sequence`：<samp>array</samp>

- List of events to send.


//////

<div class="language-text highlight"><span class="filename"><code>sequence</code></span><pre id="__code_1"><span></span></pre></div>

////// html | div.result
/////// define
`<any array element>`：<samp>object</samp>


///////

<div class="language-text highlight"><span class="filename"><code>&lt;any array element&gt;</code></span><pre id="__code_1"><span></span></pre></div>

/////// html | div.result
//////// define
`base_delay`：<samp>number</samp>

- Amount of time in seconds before starting this step.


////////


//////// define
`event`：<samp>string</samp>

- The event to send to the entity.


////////


//////// define
`sound_event`：<samp>[sound_event](#assets.schemas-blockception.general.sound_event.json)</samp>

- The sound event to play when this step happens.


////////


///////


//////


/////


////


//// define
`sequence`：<samp>array</samp>

- List of events to send.


////

<div class="language-text highlight"><span class="filename"><code>sequence</code></span><pre id="__code_1"><span></span></pre></div>

//// html | div.result

////


///

