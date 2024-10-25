# Enchantable

> 文档版本：1.21.50.25

The enchantable component determines what enchantments can be applied to the item.

## 架构

```mcschema
minecraft:enchantable:
{
  string "slot" : opt
  number "value" : opt
}

```

/// html | div.result
//// define
`slot`：<samp>string</samp>

- If true you can always eat this item (even when not hungry), defaults to false.


////


//// define
`value`：<samp>number</samp>

- The value of the enchantment.


////


///

