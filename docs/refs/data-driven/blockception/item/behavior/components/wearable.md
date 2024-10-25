# Wearable

> 文档版本：1.21.50.25

Wearable item component.

## 架构

```mcschema
minecraft:wearable:
{
  integer "protection" : opt
  boolean "dispensable" : opt
  string "slot" : opt
}

```

/// html | div.result
//// define
`protection`：<samp>integer</samp>

- How much protection does the armor item have.


////


//// define
`dispensable`：<samp>boolean</samp>

- Sets if the item can be dropped by a dispenser block


////


//// define
`slot`：<samp>string</samp>

- Which equipment slot the item can fit in


////


///

