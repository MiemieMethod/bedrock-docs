# Guardian Attack

> 文档版本：1.21.0.24

Allows this entity to use a laser beam attack. Can only be used by Guardians and Elder Guardians.

## 架构

```mcschema
guardian_attack:
{
  priority "priority"
  integer "elder_extra_magic_damage" : opt
  integer "hard_mode_extra_magic_damage" : opt
  integer "magic_damage" : opt
  number "min_distance" : opt
  number "sound_delay_time" : opt
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
`elder_extra_magic_damage`：<samp>integer</samp>

- Amount of additional damage dealt from an elder guardian's magic attack.


////


//// define
`hard_mode_extra_magic_damage`：<samp>integer</samp>

- In hard difficulty, amount of additional damage dealt from a guardian's magic attack.


////


//// define
`magic_damage`：<samp>integer</samp>

- Amount of damage dealt from a guardian's magic attack. Magic attack damage is added to the guardian's base attack damage.


////


//// define
`min_distance`：<samp>number</samp>

- Guardian attack behavior stops if the target is closer than this distance (doesn't apply to elders).


////


//// define
`sound_delay_time`：<samp>number</samp>

- Time (in seconds) to wait after starting an attack before playing the guardian attack sound.


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

