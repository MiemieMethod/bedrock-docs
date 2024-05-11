# Particle Lifetime Expression Component For 1.10.0

> 文档版本：1.21.0.24

UNDOCUMENTED:.

## 架构

```mcschema
particle_lifetime_expression:
{
  0 "expiration_expression"
  0 "max_lifetime"
}

```

/// html | div.result
//// define
`expiration_expression`：<samp>0</samp> {#assets.schemas-blockception.molang.number.json}

- This expression makes the particle expire when true (non-zero), The float/expr is evaluated once per particle, evaluated every frame.


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
`max_lifetime`：<samp>[0](#assets.schemas-blockception.molang.number.json)</samp>

- Alternate way to express lifetime, particle will expire after this much time, evaluated once.


////


///

