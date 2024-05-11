# Destructible By Mining

> 文档版本：1.21.0.24

Describes the destructible by mining properties for this block. If set to true, the block will take the default number of seconds to destroy. If set to false, this block is indestructible by mining. If the component is omitted, the block will take the default number of seconds to destroy.

## 架构

```mcschema
destructible_by_mining:
boolean

```

/// html | div.result

///


```mcschema
destructible_by_mining:
{
  number "seconds_to_destroy" : opt
}

```

/// html | div.result
//// define
`seconds_to_destroy`：<samp>number</samp>

- Sets the number of seconds it takes to destroy the block with base equipment. Greater numbers result in greater mining times.


////


///


