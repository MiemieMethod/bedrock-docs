# Random Look Around And Sit

> 文档版本：1.21.0.24

Allows the mob to randomly sit and look around for a duration. Note: Must have a sitting animation set up to use this.

## 架构

```mcschema
random_look_around_and_sit:
{
  priority "priority"
  boolean "continue_if_leashed" : opt
  boolean "continue_sitting_on_reload" : opt
  number "max_angle_of_view_horizontal" : opt
  integer "max_look_count" : opt
  integer "max_look_time" : opt
  number "min_angle_of_view_horizontal" : opt
  integer "min_look_count" : opt
  integer "min_look_time" : opt
  number "probability" : opt
  integer "random_look_around_cooldown" : opt
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
`continue_if_leashed`：<samp>boolean</samp>

- If the goal should continue to be used as long as the mob is leashed.


////


//// define
`continue_sitting_on_reload`：<samp>boolean</samp>

- The mob will stay sitting on reload.


////


//// define
`max_angle_of_view_horizontal`：<samp>number</samp>

- The rightmost angle a mob can look at on the horizontal plane with respect to its initial facing direction.


////


//// define
`max_look_count`：<samp>integer</samp>

- The max amount of unique looks a mob will have while looking around.


////


//// define
`max_look_time`：<samp>integer</samp>

- The max amount of time (in ticks) a mob will stay looking at a direction while looking around.


////


//// define
`min_angle_of_view_horizontal`：<samp>number</samp>

- The leftmost angle a mob can look at on the horizontal plane with respect to its initial facing direction.


////


//// define
`min_look_count`：<samp>integer</samp>

- The min amount of unique looks a mob will have while looking around.


////


//// define
`min_look_time`：<samp>integer</samp>

- The min amount of time (in ticks) a mob will stay looking at a direction while looking around.


////


//// define
`probability`：<samp>number</samp>

- The probability of randomly looking around/sitting.


////


//// define
`random_look_around_cooldown`：<samp>integer</samp>

- The cooldown in seconds before the goal can be used again.


////


///

