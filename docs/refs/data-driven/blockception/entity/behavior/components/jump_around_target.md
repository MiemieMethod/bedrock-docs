# Jump Around Target

> 文档版本：1.21.50.25

Allows an entity to jump around a target.

## 架构

```mcschema
jump_around_target:
{
  priority "priority"
  boolean "check_collision" : opt
   "entity_bounding_box_scale" : opt
  array "jump_angles" : opt
  {
    number "<any array element>" : opt
  }
  number "jump_cooldown_duration" : opt
  number "jump_cooldown_when_hurt_duration" : opt
  vector_of_2_items "landing_distance_from_target"
  integer "landing_position_spread_degrees" : opt
  number "last_hurt_duration" : opt
  integer "line_of_sight_obstruction_height_ignore" : opt
  number "max_jump_velocity" : opt
  number "prepare_jump_duration" : opt
  integer "required_vertical_space" : opt
  integer "snap_to_surface_block_range" : opt
  vector_of_2_items "valid_distance_to_target"
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
`check_collision`：<samp>boolean</samp>

- Enables collision checks when calculating the jump. Setting check_collision to true may affect performance and should be used with care.


////


//// define
`entity_bounding_box_scale`

- Scaling temporarily applied to the entity's AABB bounds when jumping. A smaller bounding box reduces the risk of collisions during the jump. When check_collision is true it also increases the chance of being able to jump when close to obstacles.


////


//// define
`jump_angles`：<samp>array</samp>

- The jump angles in float degrees that are allowed when performing the jump. The order in which the angles are chosen is randomized.


////

<div class="language-text highlight"><span class="filename"><code>jump_angles</code></span><pre id="__code_1"><span></span></pre></div>

//// html | div.result
///// define
`<any array element>`：<samp>number</samp>


/////


////


//// define
`jump_cooldown_duration`：<samp>number</samp>

- The time in seconds to spend in cooldown before this goal can be used again.


////


//// define
`jump_cooldown_when_hurt_duration`：<samp>number</samp>

- The time in seconds to spend in cooldown after being hurt before this goal can be used again.


////


//// define
`landing_distance_from_target`：<samp>vector_of_2_items</samp> {#assets.schemas-blockception.general.vectors.number2.json}

- The range deciding how close to and how far away from the target the landing position can be when jumping.


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
`landing_position_spread_degrees`：<samp>integer</samp>

- This angle (in degrees) is used for controlling the spread when picking a landing position behind the target. A zero spread angle means the landing position will be straight behind the target with no variance. A 90 degree spread angle means the landing position can be up to 45 degrees to the left and to the right of the position straight behind the target's view direction.


////


//// define
`last_hurt_duration`：<samp>number</samp>

- If the entity was hurt within these last seconds, the jump_cooldown_when_hurt_duration will be used instead of jump_cooldown_duration.


////


//// define
`line_of_sight_obstruction_height_ignore`：<samp>integer</samp>

- If the entity's line of sight towards its target is obstructed by an obstacle with a height below this number, the obstacle will be ignored, and the goal will try to find a valid landing position.


////


//// define
`max_jump_velocity`：<samp>number</samp>

- Maximum velocity a jump can be performed at.


////


//// define
`prepare_jump_duration`：<samp>number</samp>

- The time in seconds to spend preparing for the jump.


////


//// define
`required_vertical_space`：<samp>integer</samp>

- The number of blocks above the entity's head that has to be air for this goal to be usable.


////


//// define
`snap_to_surface_block_range`：<samp>integer</samp>

- The number of blocks above and below from the jump target position that will be checked to find a surface to land on.


////


//// define
`valid_distance_to_target`：<samp>[vector_of_2_items](#assets.schemas-blockception.general.vectors.number2.json)</samp>

- Target needs to be within this range for the jump to happen.


////


//// define
`filters`：<samp>filters</samp>

- 一个[过滤器组](../filter.md)。Conditions that need to be met for the behavior to start.


////


///

