# Offer Flower

> 文档版本：1.21.0.24

Allows the mob to offer the player a flower like the Iron Golem does.

## 架构

```mcschema
offer_flower:
{
  priority "priority"
  number "chance_to_start" : opt
  filters "filters"
  number "max_head_rotation_y" : opt
  number "max_offer_flower_duration" : opt
  number "max_rotation_x" : opt
  vector_of_3_items "search_area"
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
`chance_to_start`：<samp>number</samp>

- Percent chance that the mob will start this goal from 0.0 to 1.0 (where 1.0 = 100%).


////


//// define
`filters`：<samp>filters</samp>

- 一个[过滤器组](../filter.md)。Conditions that need to be met for the behavior to start.


////


//// define
`max_head_rotation_y`：<samp>number</samp>

- Maximum rotation (in degrees), on the Y-axis, this entity can rotate its head while trying to look at the target.


////


//// define
`max_offer_flower_duration`：<samp>number</samp>

- The max amount of time (in seconds) that the mob will offer the flower for before exiting the Goal.


////


//// define
`max_rotation_x`：<samp>number</samp>

- Maximum rotation (in degrees), on the X-axis, this entity can rotate while trying to look at the target.


////


//// define
`search_area`：<samp>vector_of_3_items</samp> {#assets.schemas-blockception.general.vectors.number3.json}

- The dimensions of the AABB used to search for a potential mob to offer flower to.


////

```mcschema
vector_of_3_items:
array
{
  number "0..0" : opt
  number "1..1" : opt
  number "2..2" : opt
}

```

//// html | div.result
///// define
`0..0`：<samp>number</samp>

- The X component.


/////


///// define
`1..1`：<samp>number</samp>

- The Y component.


/////


///// define
`2..2`：<samp>number</samp>

- The Z component.


/////


////



///

