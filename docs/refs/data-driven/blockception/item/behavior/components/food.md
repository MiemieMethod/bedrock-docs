# Food

> 文档版本：1.21.50.25

When an item has a food component, it becomes edible to the player.

## 架构

```mcschema
minecraft:food:
{
  boolean "can_always_eat" : opt
  number "nutrition" : opt
  number "saturation_modifier" : opt
  string "using_converts_to" : opt
}

```

/// html | div.result
//// define
`can_always_eat`：<samp>boolean</samp>

- If true you can always eat this item (even when not hungry), defaults to false.


////


//// define
`nutrition`：<samp>number</samp>

- How much nutrition does this food item give the player when eaten.


////


//// define
`saturation_modifier`：<samp>number</samp>

- Saturation Modifier is used in this formula: (nutrition * saturation_modifier * 2) when appling the saturation buff. Which happens when you eat the item.


////


//// define
`using_converts_to`：<samp>string</samp>

- When used, convert the *this* item to the one specified by `using_converts_to`.


////


///

