# 未命名

> 文档版本：1.21.0.24

Describes the destructible by explosion properties for this block. If set to true, the block will have the default explosion resistance. If set to false, this block is indestructible by explosion. If the component is omitted, the block will have the default explosion resistance.

## 架构

```mcschema
minecraft:destructible_by_explosion:
boolean

```

/// html | div.result

///


```mcschema
minecraft:destructible_by_explosion:
{
  number "explosion_resistance" : opt
}

```

/// html | div.result
//// define
`explosion_resistance`：<samp>number</samp>

- Describes how resistant the block is to explosion. Greater values mean the block is less likely to break when near an explosion (or has higher resistance to explosions). The scale will be different for different explosion power levels. A negative value or 0 means it will easily explode; larger numbers increase level of resistance.


////


///


