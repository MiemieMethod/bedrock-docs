# Fire At Target

> 文档版本：1.21.50.25

Allows an entity to attack by firing a shot with a delay. Anchor and offset parameters of this component overrides the anchor and offset from projectile component.

## 架构

```mcschema
fire_at_target:
{
  priority "priority"
  number "attack_cooldown" : opt
  vector_of_3_items "attack_range"
  integer "owner_anchor" : opt
  vector_of_3_items "owner_offset"
  integer "target_anchor" : opt
  vector_of_3_items "target_offset"
  number "post_shoot_delay" : opt
  number "pre_shoot_delay" : opt
  string "projectile_def" : opt
  number "ranged_fov" : opt
  number "max_head_rotation_x" : opt
  number "max_head_rotation_y" : opt
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
`attack_cooldown`：<samp>number</samp>

- The cooldown time in seconds before this goal can be used again.


////


//// define
`attack_range`：<samp>vector_of_3_items</samp> {#assets.schemas-blockception.general.vectors.number3.json}

- Target needs to be within this range for the attack to happen.


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
`owner_anchor`：<samp>integer</samp>

- Entity anchor for the projectile spawn location.


////


//// define
`owner_offset`：<samp>[vector_of_3_items](#assets.schemas-blockception.general.vectors.number3.json)</samp>

- Offset vector from the owner_anchor.


////


//// define
`target_anchor`：<samp>integer</samp>

- Entity anchor for projectile target.


////


//// define
`target_offset`：<samp>[vector_of_3_items](#assets.schemas-blockception.general.vectors.number3.json)</samp>

- Offset vector from the target_anchor.


////


//// define
`post_shoot_delay`：<samp>number</samp>

- Time in seconds between firing the projectile and ending the goal.


////


//// define
`pre_shoot_delay`：<samp>number</samp>

- Time in seconds before firing the projectile.


////


//// define
`projectile_def`：<samp>string</samp>

- Actor definition to use as projectile for the ranged attack. The actor must be a projectile.


////


//// define
`ranged_fov`：<samp>number</samp>

- Field of view (in degrees) when using sensing to detect a target for attack.


////


//// define
`max_head_rotation_x`：<samp>number</samp>

- Maximum head rotation (in degrees), on the X-axis, that this entity can apply while trying to look at the target.


////


//// define
`max_head_rotation_y`：<samp>number</samp>

- Maximum head rotation (in degrees), on the Y-axis, that this entity can apply while trying to look at the target.


////


//// define
`filters`：<samp>filters</samp>

- 一个[过滤器组](../filter.md)。Conditions that need to be met for the behavior to start.


////


///

