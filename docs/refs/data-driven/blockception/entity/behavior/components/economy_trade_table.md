# Economy Trade Table

> 文档版本：1.21.0.24

Defines this entity's ability to trade with players.

## 架构

```mcschema
economy_trade_table:
{
  boolean "convert_trades_economy" : opt
  array "cured_discount" : opt
  {
    integer "0..0" : opt
    integer "1..1" : opt
  }
  string "display_name" : opt
  integer "hero_demand_discount" : opt
  array "max_cured_discount" : opt
  {
    integer "0..0" : opt
    integer "1..1" : opt
  }
  integer "max_nearby_cured_discount" : opt
  integer "nearby_cured_discount" : opt
  boolean "new_screen" : opt
  boolean "persist_trades" : opt
  boolean "show_trade_screen" : opt
  string "table" : opt
  boolean "use_legacy_price_formula" : opt
}

```

/// html | div.result
//// define
`convert_trades_economy`：<samp>boolean</samp>

- Determines when the mob transforms, if the trades should be converted when the new mob has a economy_trade_table. When the trades are converted, the mob will generate a new trade list with their new trade table, but then it will try to convert any of the same trades over to have the same enchantments and user data. For example, if the original has a Emerald to Enchanted Iron Sword (Sharpness 1), and the new trade also has an Emerald for Enchanted Iron Sword, then the enchantment will be Sharpness 1.


////


//// define
`cured_discount`：<samp>array</samp>

- How much should the discount be modified by when the player has cured the Zombie Villager. Can be specified as a pair of numbers (low-tier trade discount and high-tier trade discount)


////

<div class="language-text highlight"><span class="filename"><code>cured_discount</code></span><pre id="__code_1"><span></span></pre></div>

//// html | div.result
///// define
`0..0`：<samp>integer</samp>

- Minimum.


/////


///// define
`1..1`：<samp>integer</samp>

- Maximum.


/////


////


//// define
`display_name`：<samp>string</samp>

- Name to be displayed while trading with this entity.


////


//// define
`hero_demand_discount`：<samp>integer</samp>

- Used in legacy prices to determine how much should Demand be modified by when the player has the Hero of the Village mob effect.


////


//// define
`max_cured_discount`：<samp>array</samp>

- The Maximum the discount can be modified by when the player has cured the Zombie Villager. Can be specified as a pair of numbers (low-tier trade discount and high-tier trade discount)


////

<div class="language-text highlight"><span class="filename"><code>max_cured_discount</code></span><pre id="__code_1"><span></span></pre></div>

//// html | div.result
///// define
`0..0`：<samp>integer</samp>

- Minimum.


/////


///// define
`1..1`：<samp>integer</samp>

- Maximum.


/////


////


//// define
`max_nearby_cured_discount`：<samp>integer</samp>

- The Maximum the discount can be modified by when the player has cured a nearby Zombie Villager.


////


//// define
`nearby_cured_discount`：<samp>integer</samp>

- How much should the discount be modified by when the player has cured a nearby Zombie Villager.


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
`show_trade_screen`：<samp>boolean</samp>

- Show an in game trade screen when interacting with the mob.


////


//// define
`table`：<samp>string</samp>

- File path relative to the resource pack root for this entity's trades.


////


//// define
`use_legacy_price_formula`：<samp>boolean</samp>

- Determines whether the legacy formula is used to determines the trade prices.


////


///

