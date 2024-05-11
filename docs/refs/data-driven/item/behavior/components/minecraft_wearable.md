# minecraft:wearable

> 文档版本：1.21.0.24

Wearable items can be worn by a player in the head, chest, legs, feet, or off-hand slots.

## 架构

```mcschema
minecraft:wearable:
{
  integer "protection" : opt
  string "slot" : opt
}

```

/// html | div.result
//// define
`protection`：<samp>integer</samp>

- How much protection the wearable item provides. Default is set to 0.


////


//// define
`slot`：<samp>string</samp>

- Specifies where the item can be worn. If any non-hand slot is chosen, the max stack size is set to 1.


////


///

