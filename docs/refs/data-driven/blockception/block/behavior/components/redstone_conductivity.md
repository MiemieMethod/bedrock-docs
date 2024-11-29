# Redstone Conductivity

> 文档版本：1.21.50.25

The basic redstone properties of a block; if the component is not provided the default values are used.

## 架构

```mcschema
redstone_conductivity:
{
  boolean "allows_wire_to_step_down" : opt
  boolean "redstone_conductor" : opt
}

```

/// html | div.result
//// define
`allows_wire_to_step_down`：<samp>boolean</samp>

- Specifies if redstone wire can stair-step downward on the block.


////


//// define
`redstone_conductor`：<samp>boolean</samp>

- Specifies if the block can be powered by redstone.


////


///

