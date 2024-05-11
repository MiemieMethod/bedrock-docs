# minecraft:barter

> 文档版本：1.21.0.24

Enables the component to drop an item as a barter exchange.

## 架构

```mcschema
minecraft:barter:
{
  string "barter_table" : opt
  integer "cooldown_after_being_attacked" : opt
}

```

/// html | div.result
//// define
`barter_table`：<samp>string</samp>

- Loot table that's used to drop a random item.


////


//// define
`cooldown_after_being_attacked`：<samp>integer</samp>

- Duration, in seconds, for which mob won't barter items if it was hurt.


////


///

