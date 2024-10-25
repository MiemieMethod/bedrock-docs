# Slime Attack

> 文档版本：1.21.50.25

Can only be used by Slimes and Magma Cubes. Allows the mob to use a melee attack like the slime's.

## 架构

```mcschema
slime_attack:
{
  priority "priority"
  speed_multiplier "speed_multiplier"
  boolean "set_persistent" : opt
  number "x_max_rotation" : opt
  number "y_max_rotation" : opt
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
`set_persistent`：<samp>boolean</samp>

- Allows the actor to be set to persist upon targeting a player.


////


//// define
`x_max_rotation`：<samp>number</samp>

- Maximum rotation (in degrees), on the X-axis, this entity can rotate while trying to look at the target.


////


//// define
`y_max_rotation`：<samp>number</samp>

- Maximum rotation (in degrees), on the Y-axis, this entity can rotate while trying to look at the target.


////


///

