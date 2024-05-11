# Random Fly

> 文档版本：1.21.0.24

Allows a mob to randomly fly around.

## 架构

```mcschema
random_fly:
{
  priority "priority"
  speed_multiplier "speed_multiplier"
  boolean "avoid_damage_blocks" : opt
  boolean "can_land_on_trees" : opt
  integer "xz_dist" : opt
  integer "y_dist" : opt
  integer "y_offset" : opt
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
`avoid_damage_blocks`：<samp>boolean</samp>

- If true, the mob will avoid blocks that cause damage.


////


//// define
`can_land_on_trees`：<samp>boolean</samp>

- If true, the mob can stop flying and land on a tree instead of the ground.


////


//// define
`xz_dist`：<samp>integer</samp>

- Distance in blocks on ground that the mob will look for a new spot to move to. Must be at least 1


////


//// define
`y_dist`：<samp>integer</samp>

- Distance in blocks that the mob will look up or down for a new spot to move to. Must be at least 1


////


//// define
`y_offset`：<samp>integer</samp>

- Height in blocks to add to the selected target position.


////


///

