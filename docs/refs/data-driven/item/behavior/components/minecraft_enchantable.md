# minecraft:enchantable

> 文档版本：1.21.0.24

The enchantable component specifies what enchantments can be applied to the item. Not all enchantments will have an effect on all item components.

## 架构

```mcschema
minecraft:enchantable:
{
  string "slot" : opt
  integer "value" : opt
}

```

/// html | div.result
//// define
`slot`：<samp>string</samp>

- Specifies which types of enchantments can be applied. For example, `bow` would allow this item to be enchanted as if it were a bow.


////


//// define
`value`：<samp>integer</samp>

- Specifies the value of the enchantment (minimum of 0).


////


///

