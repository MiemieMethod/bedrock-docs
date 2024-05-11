# minecraft:durability

> 文档版本：1.21.0.24

The durability item component specifies how much damage the item takes before breaking, and allows the item to be combined to repair or augment them.

## 架构

```mcschema
minecraft:durability:
{
  int_range "damage_chance"
  integer "max_durability" : opt
  integer "max_damage" : opt
}

```

/// html | div.result
//// define
`damage_chance`：<samp>int_range</samp> {#assets.schemas.common.struct.int_range.json}

- Specifies the percentage chance of this item losing durability. Default is set to 100. Defined as an int range with min and max value.


////

```mcschema
int_range:
{
  integer "max" : opt
  integer "min" : opt
}

```

//// html | div.result
///// define
`max`：<samp>integer</samp>


/////


///// define
`min`：<samp>integer</samp>


/////


////



//// define
`max_durability`：<samp>integer</samp>

- Max durability is the amount of damage that this item can take before breaking. This is a required parameter and has a minimum of 0.


////


//// define
`max_damage`：<samp>integer</samp>


////


///

