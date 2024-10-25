# Durability Sensor

> 文档版本：1.21.50.25

Defines both the durability threshold, and the effects emitted when that threshold is met.

## 架构

```mcschema
764203503:
{
  integer "durability" : opt
  string "particle_type" : opt
  sound_event "sound_event"
}

```

/// html | div.result
//// define
`durability`：<samp>integer</samp>

- The effects are emitted when the item durability value is less than or equal to this value.


////


//// define
`particle_type`：<samp>string</samp>

- Particle effect to emit when the threshold is met.


////


//// define
`sound_event`：<samp>sound_event</samp> {#assets.schemas-blockception.general.sound_event.json}

- Sound effect to emit when the threshold is met.


////

```mcschema
sound_event:
string

```

//// html | div.result

////



///

