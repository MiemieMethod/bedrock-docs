# Charge Attack

> 文档版本：1.21.50.25

Allows this entity to damage a target by using a running attack.

## 架构

```mcschema
charge_attack:
{
  priority "priority"
  speed_multiplier "speed_multiplier"
  number "max_distance" : opt
  number "min_distance" : opt
  number "success_rate" : opt
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
`max_distance`：<samp>number</samp>

- A charge attack cannot start if the entity is farther than this distance to the target.


////


//// define
`min_distance`：<samp>number</samp>

- A charge attack cannot start if the entity is closer than this distance to the target.


////


//// define
`success_rate`：<samp>number</samp>

- Percent chance this entity will start a charge attack, if not already attacking (1.0 = 100%)


////


///

