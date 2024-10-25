# Trade Table

> 文档版本：1.21.50.25

Defines this entity's ability to trade with players.

## 架构

```mcschema
trade_table:
{
  boolean "convert_trades_economy" : opt
  string "display_name" : opt
  boolean "new_screen" : opt
  boolean "persist_trades" : opt
  string "table" : opt
}

```

/// html | div.result
//// define
`convert_trades_economy`：<samp>boolean</samp>

- Determines when the mob transforms, if the trades should be converted when the new mob has a economy_trade_table. When the trades are converted, the mob will generate a new trade list with their new trade table, but then it will try to convert any of the same trades over to have the same enchantments and user data. For example, if the original has a Emerald to Enchanted Iron Sword (Sharpness 1), and the new trade also has an Emerald for Enchanted Iron Sword, then the enchantment will be Sharpness 1.


////


//// define
`display_name`：<samp>string</samp>

- Name to be displayed while trading with this entity.


////


//// define
`new_screen`：<samp>boolean</samp>

- Used to determine if trading with entity opens the new trade screen.


////


//// define
`persist_trades`：<samp>boolean</samp>

- Determines if the trades should persist when the mob transforms. This makes it so that the next time the mob is transformed to something with a trade_table or economy_trade_table, then it keeps their trades.


////


//// define
`table`：<samp>string</samp>

- File path relative to the resource pack root for this entity's trades.


////


///

