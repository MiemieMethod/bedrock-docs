# Emitter Lifetime Looping Component For 1.10.0

> 文档版本：1.21.50.25

UNDOCUMENTED.

## 架构

```mcschema
emitter_lifetime_looping:
{
  0 "active_time"
  0 "sleep_time"
}

```

/// html | div.result
//// define
`active_time`：<samp>0</samp> {#assets.schemas-blockception.molang.number.json}

- Emitter will emit particles for this time per loop evaluated once per particle emitter loop.


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
`sleep_time`：<samp>[0](#assets.schemas-blockception.molang.number.json)</samp>

- Emitter will pause emitting particles for this time per loop evaluated once per particle emitter loop.


////


///

