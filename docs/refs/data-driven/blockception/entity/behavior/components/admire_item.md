# Admire Item

> 文档版本：1.21.0.24

Enables the mob to admire items that have been configured as admirable. Must be used in combination with the admire_item component.

## 架构

```mcschema
admire_item:
{
  priority "priority"
  sound_event "admire_item_sound"
  event "on_admire_item_start"
  event "on_admire_item_stop"
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
`priority`：<samp>priority</samp> {#assets.schemas-blockception.behavior.entities.format.behaviors.types.priority.json}


////

```mcschema
priority:
integer

```

//// html | div.result

////



//// define
`admire_item_sound`：<samp>sound_event</samp> {#assets.schemas-blockception.general.sound_event.json}

- The sound event to play when admiring the item.


////

```mcschema
sound_event:
string

```

//// html | div.result

////



//// define
`on_admire_item_start`：<samp>event</samp> {#assets.schemas-blockception.behavior.entities.format.types.event.json}

- The event to run when admiring the item.


////

```mcschema
event:
string

```

//// html | div.result

////


```mcschema
event:
{
  string "event" : opt
  string "target" : opt
}

```

//// html | div.result
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
`on_admire_item_stop`：<samp>[event](#assets.schemas-blockception.behavior.entities.format.types.event.json)</samp>

- The event to run when no longer admiring the item.


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


/////


///// define
`range_max`：<samp>number</samp>


/////


////



///

