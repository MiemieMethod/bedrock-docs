# Movement Sway

> 文档版本：1.21.50.25

This move control causes the mob to sway side to side giving the impression it is swimming.

## 架构

```mcschema
sway:
{
  number "max_turn" : opt
  number "sway_amplitude" : opt
  number "sway_frequency" : opt
}

```

/// html | div.result
//// define
`max_turn`：<samp>number</samp>

- The maximum number in degrees the mob can turn per tick.


////


//// define
`sway_amplitude`：<samp>number</samp>

- Strength of the sway movement.


////


//// define
`sway_frequency`：<samp>number</samp>

- Multiplier for the frequency of the sway movement.


////


///

