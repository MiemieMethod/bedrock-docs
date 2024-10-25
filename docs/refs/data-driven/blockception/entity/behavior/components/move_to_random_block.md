# Move To Random Block

> 文档版本：1.21.50.25

Allows mob to move towards a random block.

## 架构

```mcschema
move_to_random_block:
{
  priority "priority"
  speed_multiplier "speed_multiplier"
  number "block_distance" : opt
  number "within_radius" : opt
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
`block_distance`：<samp>number</samp>

- Defines the distance from the mob, in blocks, that the block to move to will be chosen.


////


//// define
`within_radius`：<samp>number</samp>

- Defines the distance in blocks the mob has to be from the block for the movement to be finished.


////


///

