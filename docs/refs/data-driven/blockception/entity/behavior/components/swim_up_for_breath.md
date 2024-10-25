# Swim Up For Breath

> 文档版本：1.21.50.25

Allows the mob to try to move to air once it is close to running out of its total breathable supply.

## 架构

```mcschema
swim_up_for_breath:
{
  priority "priority"
  string "material_type" : opt
  integer "search_height" : opt
  integer "search_radius" : opt
  number "speed_mod" : opt
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
`material_type`：<samp>string</samp>

- The material the mob is traveling in. An air block will only be considered valid to move to with a block of this material below it.


////


//// define
`search_height`：<samp>integer</samp>

- The height (in blocks) above the mob's current position that it will search for a valid air block to move to. If a valid block cannot be found, the mob will move to the position this many blocks above it.


////


//// define
`search_radius`：<samp>integer</samp>

- The radius (in blocks) around the mob's current position that it will search for a valid air block to move to.


////


//// define
`speed_mod`：<samp>number</samp>

- Movement speed multiplier of the mob when using this Goal.


////


///

