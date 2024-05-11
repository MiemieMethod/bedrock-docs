# Flammable

> 文档版本：1.21.0.24

Describes the flammable properties for this block. If set to true, default values are used. If set to false, or if this component is omitted, the block will not be able to catch on fire naturally from neighbors, but it can still be directly ignited.

## 架构

```mcschema
flammable:
boolean

```

/// html | div.result

///


```mcschema
flammable:
{
  number "catch_chance_modifier" : opt
  number "destroy_chance_modifier" : opt
}

```

/// html | div.result
//// define
`catch_chance_modifier`：<samp>number</samp>

- A modifier affecting the chance that this block will catch flame when next to a fire. Values are greater than or equal to 0, with a higher number meaning more likely to catch on fire


////


//// define
`destroy_chance_modifier`：<samp>number</samp>

- A modifier affecting the chance that this block will be destroyed by flames when on fire.


////


///


