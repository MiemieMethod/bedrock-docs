# Move Around Target

> 文档版本：1.21.50.25

Allows an entity to move around a target. If the entity is too close (i.e. closer than destination range min and height difference limit) it will try to move away from its target. If the entity is too far away from its target it will try to move closer to a random position within the destination range. A randomized amount of those positions will be behind the target, and the spread can be tweaked with 'destination_pos_search_spread_degrees'.

## 架构

```mcschema
move_around_target:
{
  priority "priority"
  number "destination_pos_search_spread_degrees" : opt
  vector_of_2_items "destination_position_range"
  number "height_difference_limit" : opt
  integer "horizontal_search_distance" : opt
  number "movement_speed" : opt
  integer "vertical_search_distance" : opt
  filters "filters"
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
`destination_pos_search_spread_degrees`：<samp>number</samp>

- This angle (in degrees) is used for controlling the spread when picking a destination position behind the target. A zero spread angle means the destination position will be straight behind the target with no variance. A 90 degree spread angle means the destination position can be up to 45 degrees to the left and to the right of the position straight behind the target's view direction.


////


//// define
`destination_position_range`：<samp>vector_of_2_items</samp> {#assets.schemas-blockception.general.vectors.number2.json}

- The range of distances from the target entity within which the goal should look for a position to move the owner entity to.


////

```mcschema
vector_of_2_items:
array
{
  number "0..0" : opt
  number "1..1" : opt
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


////



//// define
`height_difference_limit`：<samp>number</samp>

- Distance in height (in blocks) between the owner entity and the target has to be less than this value when owner checks if it is too close and should move away from the target. This value needs to be bigger than zero for the move away logic to trigger.


////


//// define
`horizontal_search_distance`：<samp>integer</samp>

- Horizontal search distance (in blocks) when searching for a position to move away from target.


////


//// define
`movement_speed`：<samp>number</samp>

- The speed with which the entity should move to its target position.


////


//// define
`vertical_search_distance`：<samp>integer</samp>

- Number of ticks needed to complete a stay at the block.


////


//// define
`filters`：<samp>filters</samp>

- 一个[过滤器组](../filter.md)。Conditions that need to be met for the behavior to start.


////


///

