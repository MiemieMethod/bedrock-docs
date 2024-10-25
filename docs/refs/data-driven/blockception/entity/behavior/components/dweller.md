# Dweller

> 文档版本：1.21.50.25

Allows a mob to join and migrate between villages and other dwellings.

## 架构

```mcschema
dweller:
{
  string "dwelling_type" : opt
  string "dweller_role" : opt
  number "update_interval_base" : opt
  number "update_interval_variant" : opt
  boolean "can_find_poi" : opt
  integer "first_founding_reward" : opt
  boolean "can_migrate" : opt
  number "dwelling_bounds_tolerance" : opt
  string "preferred_profession" : opt
}

```

/// html | div.result
//// define
`dwelling_type`：<samp>string</samp>

- The type of dwelling the mob wishes to join. Current Types: village


////


//// define
`dweller_role`：<samp>string</samp>

- The role of which the mob plays in the dwelling. Current Roles: inhabitant, defender, hostile, passive.


////


//// define
`update_interval_base`：<samp>number</samp>

- How often the mob checks on their dwelling status in ticks. Positive values only.


////


//// define
`update_interval_variant`：<samp>number</samp>

- The variant value in ticks that will be added to the update_interval_base.


////


//// define
`can_find_poi`：<samp>boolean</samp>

- Whether or not the mob can find and add POI's to the dwelling.


////


//// define
`first_founding_reward`：<samp>integer</samp>

- How much reputation should the players be rewarded on first founding?.


////


//// define
`can_migrate`：<samp>boolean</samp>

- Can this mob migrate between dwellings? Or does it only have its initial dwelling?.


////


//// define
`dwelling_bounds_tolerance`：<samp>number</samp>

- A padding distance for checking if the mob is within the dwelling.


////


//// define
`preferred_profession`：<samp>string</samp>

- Allows the user to define a starting profession for this particular Dweller, instead of letting them choose organically. (They still need to gain experience from trading before this takes effect.)


////


///

