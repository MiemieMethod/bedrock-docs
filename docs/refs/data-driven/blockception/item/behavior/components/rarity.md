# Rarity

> 文档版本：1.21.50.25

Specifies the base rarity and subsequently color of the item name when the player hovers the cursor over the item.

## 架构

```mcschema
minecraft:rarity:
string

```

/// html | div.result

///


```mcschema
minecraft:rarity:
{
  string "value" : opt
}

```

/// html | div.result
//// define
`value`：<samp>string</samp>

- Sets the base rarity of the item. The rarity of an item automatically increases when enchanted, either to Rare when the base rarity is Common or Uncommon, or Epic when the base rarity is Rare.


////


///


