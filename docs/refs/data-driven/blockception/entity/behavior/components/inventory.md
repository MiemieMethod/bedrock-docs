# Inventory

> 文档版本：1.21.50.25

Defines this entity's inventory properties.

## 架构

```mcschema
inventory:
{
  integer "additional_slots_per_strength" : opt
  boolean "can_be_siphoned_from" : opt
  string "container_type" : opt
  integer "inventory_size" : opt
  boolean "private" : opt
  boolean "restrict_to_owner" : opt
}

```

/// html | div.result
//// define
`additional_slots_per_strength`：<samp>integer</samp>

- Number of slots that this entity can gain per extra strength.


////


//// define
`can_be_siphoned_from`：<samp>boolean</samp>

- If true, the contents of this inventory can be removed by a hopper.


////


//// define
`container_type`：<samp>string</samp>

- Type of container this entity has. Can be horse, minecart_chest, chest_boat, minecart_hopper, inventory, container or hopper


////


//// define
`inventory_size`：<samp>integer</samp>

- Number of slots the container has.


////


//// define
`private`：<samp>boolean</samp>

- If true, only the entity can access the inventory.


////


//// define
`restrict_to_owner`：<samp>boolean</samp>

- If true, the entity's inventory can only be accessed by its owner or itself.


////


///

