# Slime Float

> 文档版本：1.21.50.25

Allow slimes to float in water / lava. Can only be used by Slime and Magma Cubes.

## 架构

```mcschema
slime_float:
{
  priority "priority"
  speed_multiplier "speed_multiplier"
  number "jump_chance_percentage" : opt
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
`jump_chance_percentage`：<samp>number</samp>

- Percent chance a slime or magma cube has to jump while in water / lava.


////


///

