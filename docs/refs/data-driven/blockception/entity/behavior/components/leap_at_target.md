# Leap At Target

> 文档版本：1.21.0.24

Allows monsters to jump at and attack their target. Can only be used by hostile mobs.

## 架构

```mcschema
leap_at_target:
{
  priority "priority"
  boolean "must_be_on_ground" : opt
  boolean "set_persistent" : opt
  number "yd" : opt
  number "target_dist" : opt
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
`must_be_on_ground`：<samp>boolean</samp>

- If true, the mob will only jump at its target if its on the ground. Setting it to false will allow it to jump even if its already in the air


////


//// define
`set_persistent`：<samp>boolean</samp>

- Allows the actor to be set to persist upon targeting a player.


////


//// define
`yd`：<samp>number</samp>

- The height in blocks the mob jumps when leaping at its target.


////


//// define
`target_dist`：<samp>number</samp>

- Distance in blocks the mob jumps when leaping at its target.


////


///

