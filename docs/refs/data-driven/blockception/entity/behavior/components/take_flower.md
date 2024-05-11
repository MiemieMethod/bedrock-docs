# Take Flower

> 文档版本：1.21.0.24

Can only be used by Villagers. Allows the mob to accept flowers from Iron Golems.

## 架构

```mcschema
take_flower:
{
  priority "priority"
  speed_multiplier "speed_multiplier"
  filters "filters"
  number "max_head_rotation_y" : opt
  number "max_rotation_x" : opt
  number "max_wait_time" : opt
  number "min_distance_to_target" : opt
  number "min_wait_time" : opt
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
`speed_multiplier`：<samp>speed_multiplier</samp> {#assets.schemas-blockception.behavior.entities.format.behaviors.types.speed_multiplier.json}


////

```mcschema
speed_multiplier:
number

```

//// html | div.result

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
`max_rotation_x`：<samp>number</samp>

- Maximum rotation (in degrees), on the X-axis, this entity can rotate while trying to look at the target.


////


//// define
`max_wait_time`：<samp>number</samp>

- The maximum amount of time (in seconds) for the mob to randomly wait for before taking the flower.


////


//// define
`min_distance_to_target`：<samp>number</samp>

- Minimum distance (in blocks) for the entity to be considered having reached its target.


////


//// define
`min_wait_time`：<samp>number</samp>

- The minimum amount of time (in seconds) for the mob to randomly wait for before taking the flower.


////


//// define
`search_area`：<samp>vector_of_3_items</samp> {#assets.schemas-blockception.general.vectors.number3.json}

- The dimensions of the AABB used to search for a potential mob to take a flower from.


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

