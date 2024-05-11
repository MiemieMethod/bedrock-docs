# Ranged Attack

> 文档版本：1.21.0.24

Allows the mob to use ranged attacks like shooting arrows.

## 架构

```mcschema
ranged_attack:
{
  priority "priority"
  speed_multiplier "speed_multiplier"
  number "attack_interval" : opt
  number "attack_interval_max" : opt
  number "attack_interval_min" : opt
  number "attack_radius" : opt
  number "attack_radius_min" : opt
  number "burst_interval" : opt
  integer "burst_shots" : opt
  number "charge_charged_trigger" : opt
  number "charge_shoot_trigger" : opt
  number "ranged_fov" : opt
  boolean "set_persistent" : opt
  boolean "swing" : opt
  number "target_in_sight_time" : opt
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
`speed_multiplier`：<samp>speed_multiplier</samp> {#assets.schemas-blockception.behavior.entities.format.behaviors.types.speed_multiplier.json}


////

```mcschema
speed_multiplier:
number

```

//// html | div.result

////



//// define
`attack_interval`：<samp>number</samp>

- Alternative to "attack_interval_min" & "attack_interval_max". Consistent reload-time (in seconds), when not using a charged shot. Does not scale with target-distance.


////


//// define
`attack_interval_max`：<samp>number</samp>

- Maximum bound for reload-time range (in seconds), when not using a charged shot. Reload-time range scales with target-distance.


////


//// define
`attack_interval_min`：<samp>number</samp>

- Minimum bound for reload-time range (in seconds), when not using a charged shot. Reload-time range scales with target-distance.


////


//// define
`attack_radius`：<samp>number</samp>

- Minimum distance to target before this entity will attempt to shoot.


////


//// define
`attack_radius_min`：<samp>number</samp>

- Minimum distance the target can be for this mob to fire. If the target is closer, this mob will move first before firing


////


//// define
`burst_interval`：<samp>number</samp>

- Time (in seconds) between each individual shot when firing a burst of shots from a charged up attack.


////


//// define
`burst_shots`：<samp>integer</samp>

- Number of shots fired every time the attacking entity uses a charged up attack.


////


//// define
`charge_charged_trigger`：<samp>number</samp>

- Time (in seconds, then add "charge_shoot_trigger"), before a charged up attack is done charging. Charge-time decays while target is not in sight.


////


//// define
`charge_shoot_trigger`：<samp>number</samp>

- Amount of time (in seconds, then doubled) a charged shot must be charging before reloading burst shots. Charge-time decays while target is not in sight.


////


//// define
`ranged_fov`：<samp>number</samp>

- Field of view (in degrees) when using sensing to detect a target for attack.


////


//// define
`set_persistent`：<samp>boolean</samp>

- Allows the actor to be set to persist upon targeting a player.


////


//// define
`swing`：<samp>boolean</samp>

- If a swing animation (using variable.attack_time) exists, this causes the actor to swing their arm(s) upon firing the ranged attack.


////


//// define
`target_in_sight_time`：<samp>number</samp>

- Minimum amount of time (in seconds) the attacking entity needs to see the target before moving toward it.


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

