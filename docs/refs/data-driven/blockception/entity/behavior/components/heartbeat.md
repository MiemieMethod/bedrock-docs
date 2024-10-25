# Heartbeat

> 文档版本：1.21.50.25

defines the entity's heartbeat..

## 架构

```mcschema
heartbeat:
{
  0 "interval"
  string "sound_event" : opt
}

```

/// html | div.result
//// define
`interval`：<samp>0</samp> {#assets.schemas-blockception.molang.number.json}

- A Molang expression defining the inter-beat interval in seconds. A value of zero or less means no heartbeat..


////

```mcschema
0:
string

```

//// html | div.result

////


```mcschema
0:
number

```

//// html | div.result

////




//// define
`sound_event`：<samp>string</samp>

- Level sound event to be played as the heartbeat sound.


////


///

