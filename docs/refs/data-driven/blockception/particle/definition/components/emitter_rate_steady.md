# Emitter Rate Steady Component For 1.10.0

> 文档版本：1.21.0.24

UNDOCUMENTED.

## 架构

```mcschema
emitter_rate_steady:
{
  0 "max_particles"
  0 "spawn_rate"
}

```

/// html | div.result
//// define
`max_particles`：<samp>0</samp> {#assets.schemas-blockception.molang.number.json}

- Maximum number of particles that can be active at once for this emitter, evaluated once per particle emitter loop.


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
`spawn_rate`：<samp>[0](#assets.schemas-blockception.molang.number.json)</samp>

- How often a particle is emitted, in particles/sec evaluated once per particle emitted.


////


///

