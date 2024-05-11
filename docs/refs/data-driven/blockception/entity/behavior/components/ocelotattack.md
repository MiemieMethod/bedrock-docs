# Ocelotattack

> 文档版本：1.21.0.24

Can only be used by the Ocelot. Allows it to perform the sneak and pounce attack.

## 架构

```mcschema
ocelotattack:
{
  priority "priority"
  number "cooldown_time" : opt
  number "max_distance" : opt
  number "max_sneak_range" : opt
  number "max_sprint_range" : opt
  number "reach_multiplier" : opt
  number "sneak_speed_multiplier" : opt
  number "sprint_speed_multiplier" : opt
  number "walk_speed_multiplier" : opt
  number "x_max_rotation" : opt
  number "y_max_head_rotation" : opt
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
`cooldown_time`：<samp>number</samp>

- Time (in seconds) between attacks.


////


//// define
`max_distance`：<samp>number</samp>

- Max distance from the target, this entity will use this attack behavior.


////


//// define
`max_sneak_range`：<samp>number</samp>

- Max distance from the target, this entity starts sneaking.


////


//// define
`max_sprint_range`：<samp>number</samp>

- Max distance from the target, this entity starts sprinting (sprinting takes priority over sneaking).


////


//// define
`reach_multiplier`：<samp>number</samp>

- Used with the base size of the entity to determine minimum target-distance before trying to deal attack damage.


////


//// define
`sneak_speed_multiplier`：<samp>number</samp>

- Modifies the attacking entity's movement speed while sneaking.


////


//// define
`sprint_speed_multiplier`：<samp>number</samp>

- Modifies the attacking entity's movement speed while sprinting.


////


//// define
`walk_speed_multiplier`：<samp>number</samp>

- Modifies the attacking entity's movement speed when not sneaking or sprinting, but still within attack range.


////


//// define
`x_max_rotation`：<samp>number</samp>

- Maximum rotation (in degrees), on the X-axis, this entity can rotate while trying to look at the target.


////


//// define
`y_max_head_rotation`：<samp>number</samp>

- Maximum rotation (in degrees), on the Y-axis, this entity can rotate its head while trying to look at the target.


////


///

