# Pet Sleep With Owner

> 文档版本：1.21.0.24

Allows the mob to be tempted by food they like.

## 架构

```mcschema
pet_sleep_with_owner:
{
  priority "priority"
  speed_multiplier "speed_multiplier"
  number "goal_radius" : opt
  integer "search_height" : opt
  integer "search_radius" : opt
  integer "search_range" : opt
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
`goal_radius`：<samp>number</samp>

- Distance in blocks within the mob considers it has reached the goal. This is the "wiggle room" to stop the AI from bouncing back and forth trying to reach a specific spot


////


//// define
`search_height`：<samp>integer</samp>

- Height in blocks from the owner the pet can be to sleep with owner.


////


//// define
`search_radius`：<samp>integer</samp>

- The radius that the mob will search for an owner to curl up with.


////


//// define
`search_range`：<samp>integer</samp>

- The range that the mob will search for an owner to curl up with.


////


///

