# Storage Item

> 文档版本：1.21.50.25

[EXPERIMENTAL] Storage Items can be used by other components to store other items within this item.

## 架构

```mcschema
minecraft:storage_item:
{
  boolean "allow_nested_storage_items" : opt
  array "allowed_items" : opt
  {
    string "<any array element>" : opt
  }
  array "banned_items" : opt
  {
    string "<any array element>" : opt
  }
  integer "max_slots" : opt
  integer "max_weight_limit" : opt
  integer "weight_in_storage_item" : opt
}

```

/// html | div.result
//// define
`allow_nested_storage_items`：<samp>boolean</samp>

- Determines whether another Storage Item is allowed inside of this item. Default is true.


////


//// define
`allowed_items`：<samp>array</samp>

- List of items that are exclusively allowed in this Storage Item. If empty all items are allowed.


////

<div class="language-text highlight"><span class="filename"><code>allowed_items</code></span><pre id="__code_1"><span></span></pre></div>

//// html | div.result
///// define
`<any array element>`：<samp>string</samp>


/////


////


//// define
`banned_items`：<samp>array</samp>

- List of items that are not allowed in this Storage Item.


////

<div class="language-text highlight"><span class="filename"><code>banned_items</code></span><pre id="__code_1"><span></span></pre></div>

//// html | div.result
///// define
`<any array element>`：<samp>string</samp>


/////


////


//// define
`max_slots`：<samp>integer</samp>

- The maximum number of different item stacks. Maximum is 64. Default is 64.


////


//// define
`max_weight_limit`：<samp>integer</samp>

- The maximum allowed weight of the sum of all contained items. Maximum is 64. Default is 64.


////


//// define
`weight_in_storage_item`：<samp>integer</samp>

- The weight of this item when inside another Storage Item. Default is 4. 0 means item is not allowed in another Storage Item.


////


///

