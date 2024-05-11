# Explore Outskirts

> 文档版本：1.21.0.24

Allows the entity to first travel to a random point on the outskirts of the village, and then explore random points within a small distance. This goal requires "minecraft:dweller" and "minecraft:navigation" to execute.

## 架构

```mcschema
explore_outskirts:
{
  priority "priority"
  speed_multiplier "speed_multiplier"
  vector_of_3_items "dist_from_boundary"
  number "explore_dist" : opt
  number "max_travel_time" : opt
  number "max_wait_time" : opt
  number "min_dist_from_target" : opt
  number "min_perimeter" : opt
  number "min_wait_time" : opt
  integer "next_xz" : opt
  integer "next_y" : opt
  number "timer_ratio" : opt
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
`dist_from_boundary`：<samp>vector_of_3_items</samp> {#assets.schemas-blockception.general.vectors.number3.json}

- The distance from the boundary the villager must be within in to explore the outskirts.


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



//// define
`explore_dist`：<samp>number</samp>

- Total distance in blocks the the entity will explore beyond the village bounds when choosing its travel point.


////


//// define
`max_travel_time`：<samp>number</samp>

- This is the maximum amount of time an entity will attempt to reach it's travel point on the outskirts of the village before the goal exits.


////


//// define
`max_wait_time`：<samp>number</samp>

- The wait time in seconds between choosing new explore points will be chosen on a random interval between this value and the minimum wait time. This value is also the total amount of time the entity will explore random points before the goal stops.


////


//// define
`min_dist_from_target`：<samp>number</samp>

- The entity must be within this distance for it to consider it has successfully reached its target.


////


//// define
`min_perimeter`：<samp>number</samp>

- The minimum perimeter of the village required to run this goal.


////


//// define
`min_wait_time`：<samp>number</samp>

- The wait time in seconds between choosing new explore points will be chosen on a random interval between this value and the maximum wait time.


////


//// define
`next_xz`：<samp>integer</samp>

- A new explore point will randomly be chosen within this XZ distance of the current target position when navigation has finished and the wait timer has elapsed.


////


//// define
`next_y`：<samp>integer</samp>

- A new explore point will randomly be chosen within this Y distance of the current target position when navigation has finished and the wait timer has elapsed.


////


//// define
`timer_ratio`：<samp>number</samp>

- Each new explore point will be chosen on a random interval between the minimum and the maximum wait time, divided by this value. This does not apply to the first explore point chosen when the goal runs.


////


///

