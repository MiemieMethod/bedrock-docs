# Emitter Rate Manual Component 1.10.0

> 文档版本：1.21.50.25

UNDOCUMENTED.

## 架构

```mcschema
emitter_rate_manual:
{
  0 "activation_expression"
  0 "expiration_expression"
}

```

/// html | div.result
//// define
`activation_expression`：<samp>0</samp> {#assets.schemas-blockception.molang.number.json}

- When the expression is non-zero, the emitter will emit particles. Evaluated every frame


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
`expiration_expression`：<samp>[0](#assets.schemas-blockception.molang.number.json)</samp>

- Emitter will expire if the expression is non-zero. Evaluated every frame


////


///

