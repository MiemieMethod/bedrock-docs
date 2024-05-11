# minecraft:record

> 文档版本：1.21.0.24

Record Item Component. Used by record items to play music.

## 架构

```mcschema
minecraft:record:
{
  integer "comparator_signal" : opt
  number "duration" : opt
  string "sound_event" : opt
}

```

/// html | div.result
//// define
`comparator_signal`：<samp>integer</samp>

- Specifies signal strength for comparator blocks to use, from 1 - 13.


////


//// define
`duration`：<samp>number</samp>

- Specifies duration of sound event in seconds, float value.


////


//// define
`sound_event`：<samp>string</samp>

- Sound event type: 13, cat, blocks, chirp, far, mall, mellohi, stal, strad, ward, 11, wait, pigstep, otherside, 5, relic.


////


///

