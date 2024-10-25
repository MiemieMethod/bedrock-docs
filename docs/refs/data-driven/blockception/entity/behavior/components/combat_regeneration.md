# Combat Regeneration

> 文档版本：1.21.50.25

Gives Regeneration I and removes Mining Fatigue from the mob that kills the Actor`s attack target.

## 架构

```mcschema
combat_regeneration:
{
  boolean "apply_to_family" : opt
  boolean "apply_to_self" : opt
  integer "regeneration_duration" : opt
}

```

/// html | div.result
//// define
`apply_to_family`：<samp>boolean</samp>

- Determines if the mob will grant mobs of the same type combat buffs if they kill the target.


////


//// define
`apply_to_self`：<samp>boolean</samp>

- Determines if the mob will grant itself the combat buffs if it kills the target.


////


//// define
`regeneration_duration`：<samp>integer</samp>

- The duration in seconds of Regeneration I added to the mob.


////


///

