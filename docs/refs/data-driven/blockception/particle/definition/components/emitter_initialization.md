# Emitter Initialization Component For 1.10.0

> 文档版本：1.21.0.24

This component allows the emitter to run some Molang at creation, primarily to populate any Molang variables that get used later.

## 架构

```mcschema
emitter_initialization:
{
  0 "creation_expression"
  0 "per_update_expression"
}

```

/// html | div.result
//// define
`creation_expression`：<samp>0</samp> {#assets.schemas-blockception.molang.string.json}

- This is run once at emitter startup.


////

```mcschema
0:
string

```

//// html | div.result

////



//// define
`per_update_expression`：<samp>[0](#assets.schemas-blockception.molang.string.json)</samp>

- This is run once per emitter update.


////


///

