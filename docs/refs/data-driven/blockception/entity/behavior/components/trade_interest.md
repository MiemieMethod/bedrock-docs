# Trade Interest

> 文档版本：1.21.0.24

Allows the mob to look at a player that is holding a tradable item.

## 架构

```mcschema
trade_interest:
{
  priority "priority"
  number "carried_item_switch_time" : opt
  number "cooldown" : opt
  number "interest_time" : opt
  number "remove_item_time" : opt
  number "within_radius" : opt
}

```

/// html | div.result
//// define
`priority`：<samp>priority</samp> {#assets.schemas-blockception.behavior.entities.format.behaviors.types.priority.json}


////

```mcschema
priority:
integer

```

//// html | div.result

////



//// define
`carried_item_switch_time`：<samp>number</samp>

- The Maximum time in seconds that the trader will hold an item before attempting to switch for a different item that takes the same trade.


////


//// define
`cooldown`：<samp>number</samp>

- The time in seconds before the trader can use this goal again.


////


//// define
`interest_time`：<samp>number</samp>

- The Maximum time in seconds that the trader will be interested with showing it's trade items.


////


//// define
`remove_item_time`：<samp>number</samp>

- The Maximum time in seconds that the trader will wait when you no longer have items to trade.


////


//// define
`within_radius`：<samp>number</samp>

- Distance in blocks this mob can be interested by a player holding an item they like.


////


///

