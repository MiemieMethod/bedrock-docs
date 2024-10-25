# Record

> 文档版本：1.21.50.25

Used by record items to play music.

## 架构

```mcschema
minecraft:record:
{
  number "comparator_signal" : opt
  number "duration" : opt
  string "sound_event" : opt
}

```

/// html | div.result
//// define
`comparator_signal`：<samp>number</samp>

- Signal strength for comparator blocks to use, from 1 - 13


////


//// define
`duration`：<samp>number</samp>

- Duration of sound event in seconds, float value.


////


//// define
`sound_event`：<samp>string</samp>

- Sound event type: 13, cat, blocks, chirp, far, mall, mellohi, stal, strad, ward, 11, wait, pigstep, otherside, 5, relic.


////


///

